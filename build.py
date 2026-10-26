"""Génère le site statique (français à la racine, arabe dans /ar/) dans le dossier dist/.

Réglages par variables d'environnement (tous facultatifs) :
  API_BASE       adresse de l'application (ex. https://app.exemple.org) : source des membres et actualités
  APP_URL        adresse vers laquelle pointent « Adhérer », « Suivre ma demande » et « Connexion »
                 (par défaut : API_BASE)
  CUSTOM_DOMAIN  nom de domaine du site (ex. psie-ci.org) : écrit le fichier CNAME de GitHub Pages
  DIST           dossier de sortie (par défaut : dist)

Usage :  python build.py
"""

import json
import os
import re
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from content import SITE_NAME, T

ROOT = Path(__file__).resolve().parent
URL_RE = re.compile(r"^https?://[A-Za-z0-9.-]+(:\d{1,5})?$")
DOMAIN_RE = re.compile(r"^(?=.{4,253}$)([A-Za-z0-9-]+\.)+[A-Za-z]{2,}$")
PAGES = ["index", "apropos", "membres", "actualites", "actualite"]
LOGOS = ("logo.svg", "logo.png", "logo.webp")


def clean_url(name: str, value: str) -> str:
    value = (value or "").strip().rstrip("/")
    if value and not URL_RE.match(value):
        sys.exit(f"{name} invalide : « {value} ». Attendu : https://nom-de-domaine (sans chemin ni espace).")
    return value


def build(dist: Path | None = None) -> Path:
    api_base = clean_url("API_BASE", os.environ.get("API_BASE", ""))
    app_url = clean_url("APP_URL", os.environ.get("APP_URL", "")) or api_base
    domain = os.environ.get("CUSTOM_DOMAIN", "").strip()
    if domain and not DOMAIN_RE.match(domain):
        sys.exit(f"CUSTOM_DOMAIN invalide : « {domain} ».")
    dist = dist or Path(os.environ.get("DIST", ROOT / "dist"))

    if dist.exists():
        shutil.rmtree(dist)
    (dist / "ar").mkdir(parents=True)
    shutil.copytree(ROOT / "assets", dist / "assets")
    logo = next((n for n in LOGOS if (ROOT / "assets" / n).exists()), None)

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))
    for lang in ("fr", "ar"):
        other = "ar" if lang == "fr" else "fr"
        base = "" if lang == "fr" else "../"
        for page in PAGES:
            html = env.get_template(f"{page}.html").render(
                t=T[lang], lang=lang, dir="rtl" if lang == "ar" else "ltr", site_name=SITE_NAME[lang],
                page=page, root=base, api_base=api_base, app_url=app_url, logo=logo,
                # lien vers la même page dans l'autre langue
                other_href=(f"ar/{page}.html" if lang == "fr" else f"../{page}.html"), other_lang=other,
                other_label=T[other]["lang_other"],
            )
            out = dist / ("ar" if lang == "ar" else "") / f"{page}.html"
            out.write_text(html, encoding="utf-8")
    (dist / "404.html").write_text(
        '<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=./">'
        '<title>PSIE</title><a href="./">PSIE</a>', encoding="utf-8")
    if domain:
        (dist / "CNAME").write_text(domain + "\n", encoding="utf-8")
    (dist / ".nojekyll").write_text("", encoding="utf-8")
    (dist / "build-info.json").write_text(
        json.dumps({"api_base": api_base, "app_url": app_url, "domain": domain or None}, indent=2), encoding="utf-8")
    if not api_base:
        print("Avertissement : API_BASE non défini, membres et actualités ne s'afficheront pas.", file=sys.stderr)
    if not app_url:
        print("Avertissement : APP_URL non défini, les boutons « Adhérer » et « Connexion » seront inactifs.", file=sys.stderr)
    return dist


if __name__ == "__main__":
    print(f"Site généré dans {build()}")
