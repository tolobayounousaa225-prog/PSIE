"""Récupère le contenu du site depuis l'application (backend) avant la construction.

Usage (dans le workflow, ou à la main) :
    CONTENT_URL=https://app.exemple.org/api/public/site.json python tools/fetch_content.py

Remplace data/*.json et assets/media/ par le contenu de l'application. Règle d'or : TOUT OU RIEN.
Au moindre doute (application injoignable, réponse mal formée, fichier altéré ou trop gros), rien n'est
modifié et le programme s'arrête en erreur : la construction échoue et la version déjà en ligne reste en place.
"""

import hashlib
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SINGLETONS = ("annonce", "president", "contact")
OPTIONAL_LISTS = ("annuaire",)         # absente chez une ancienne application : remplacée par une liste vide
LISTS = ("actualites", "equipe", "partenaires", "documents", "transparence", "galerie", "faitieres", "regions")
MEDIA_PATH_RE = re.compile(r"assets/media/\d{1,9}\.(jpg|png|webp|pdf)")
MEDIA_URL_RE = re.compile(r"/medias/\d{1,9}\.(jpg|png|webp|pdf)")
MAX_JSON = 5 * 1024 * 1024
MAX_FILE = 20 * 1024 * 1024
MAX_FILES = 2000
TIMEOUT = 30


class FetchError(RuntimeError):
    """Message lisible : il s'affiche tel quel dans le journal de la construction."""


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise FetchError("l'application a répondu par une redirection (refusée par sécurité)")


def _check_url(url: str, allow_insecure: bool) -> urllib.parse.ParseResult:
    p = urllib.parse.urlparse(url)
    local = p.hostname in ("127.0.0.1", "localhost")
    if not p.hostname or p.username or (p.scheme != "https" and not (allow_insecure and local and p.scheme == "http")):
        raise FetchError("CONTENT_URL doit être une adresse https:// (sans identifiant)")
    return p


def _get(url: str, limit: int) -> bytes:
    opener = urllib.request.build_opener(_NoRedirect)
    request = urllib.request.Request(url, headers={"User-Agent": "psie-site-build", "Accept": "*/*"})
    try:
        with opener.open(request, timeout=TIMEOUT) as response:
            if response.status != 200:
                raise FetchError(f"réponse inattendue ({response.status}) pour {url}")
            body = response.read(limit + 1)
    except FetchError:
        raise
    except urllib.error.HTTPError as e:
        raise FetchError(f"{url} : erreur {e.code}")
    except (urllib.error.URLError, OSError, TimeoutError) as e:
        raise FetchError(f"{url} : application injoignable ({type(e).__name__})")
    if len(body) > limit:
        raise FetchError(f"{url} : réponse trop volumineuse")
    return body


def _validate(doc) -> list[dict]:
    if not isinstance(doc, dict):
        raise FetchError("contenu mal formé : un objet JSON est attendu")
    for key in SINGLETONS:
        if not isinstance(doc.get(key), dict):
            raise FetchError(f"contenu mal formé : « {key} » manquant ou invalide")
    for key in LISTS:
        if not isinstance(doc.get(key), list):
            raise FetchError(f"contenu mal formé : « {key} » manquant ou invalide")
    for key in OPTIONAL_LISTS:
        rows = doc.setdefault(key, [])
        if not isinstance(rows, list) or len(rows) > 5000 or not all(
                isinstance(r, dict) and all(isinstance(v, str) and len(v) <= 255 for v in r.values()) for r in rows):
            raise FetchError(f"contenu mal formé : « {key} » invalide")
    media = doc.get("media")
    if not isinstance(media, list) or len(media) > MAX_FILES:
        raise FetchError("contenu mal formé : liste des fichiers manquante ou trop longue")
    seen = set()
    for m in media:
        if not (isinstance(m, dict) and isinstance(m.get("path"), str) and MEDIA_PATH_RE.fullmatch(m["path"])
                and isinstance(m.get("url"), str) and MEDIA_URL_RE.fullmatch(m["url"])
                and isinstance(m.get("sha256"), str) and re.fullmatch(r"[0-9a-f]{64}", m["sha256"])):
            raise FetchError(f"liste des fichiers invalide : {str(m)[:120]}")
        if m["path"] in seen:
            raise FetchError(f"fichier en double : {m['path']}")
        seen.add(m["path"])
    return media


def run(content_url: str, root: Path = ROOT, allow_insecure: bool = False) -> dict:
    base = _check_url(content_url, allow_insecure)
    try:
        doc = json.loads(_get(content_url, MAX_JSON))
    except json.JSONDecodeError:
        raise FetchError("la réponse n'est pas du JSON valide")
    media = _validate(doc)
    origin = f"{base.scheme}://{base.netloc}"            # les fichiers ne sont lus que sur la même application
    staging = root / ".contenu-staging"
    shutil.rmtree(staging, ignore_errors=True)
    try:
        (staging / "data").mkdir(parents=True)
        (staging / "media").mkdir()
        for m in media:
            blob = _get(origin + m["url"], MAX_FILE)
            if hashlib.sha256(blob).hexdigest() != m["sha256"]:
                raise FetchError(f"fichier altéré ou incomplet : {m['url']}")
            (staging / "media" / Path(m["path"]).name).write_bytes(blob)
        for key in SINGLETONS + LISTS + OPTIONAL_LISTS:
            (staging / "data" / f"{key}.json").write_text(
                json.dumps(doc[key], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        # Tout est prêt et vérifié : on remplace d'un bloc.
        (root / "data").mkdir(exist_ok=True)
        for key in SINGLETONS + LISTS + OPTIONAL_LISTS:
            os.replace(staging / "data" / f"{key}.json", root / "data" / f"{key}.json")
        target = root / "assets" / "media"
        shutil.rmtree(target, ignore_errors=True)
        (root / "assets").mkdir(exist_ok=True)
        os.replace(staging / "media", target)
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    return {"version": doc.get("version"), "fichiers": len(media)}


def main() -> int:
    url = os.environ.get("CONTENT_URL", "").strip()
    if not url:
        print("CONTENT_URL non défini : le contenu du dossier data/ est conservé.")
        return 0
    try:
        info = run(url)
    except FetchError as e:
        print(f"ERREUR — contenu non récupéré, construction annulée : {e}", file=sys.stderr)
        return 1
    print(f"Contenu récupéré (version {info['version']}, {info['fichiers']} fichier(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
