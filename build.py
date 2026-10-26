"""Génère le site statique (français à la racine, arabe dans /ar/) dans le dossier dist/.

Réglages par variables d'environnement (tous facultatifs) :
  API_BASE       adresse de l'application (ex. https://app.exemple.org) : source des membres et actualités
  APP_URL        adresse vers laquelle pointent « Adhérer », « Suivre ma demande » et « Connexion »
                 (par défaut : API_BASE)
  SITE_URL       adresse publique du site (ex. https://tolobayounousaa225-prog.github.io/PSIE) : sert aux
                 adresses canoniques, au plan du site et aux liens entre langues
  CUSTOM_DOMAIN  nom de domaine du site (ex. psie-ci.org) : écrit le fichier CNAME de GitHub Pages
  DIST           dossier de sortie (par défaut : dist)

Usage :  python build.py
"""

import json
import os
from urllib.parse import quote
import re
import shutil
import sys
from pathlib import Path

import extras
from jinja2 import Environment, FileSystemLoader, select_autoescape

from content import PAGES, SITE_NAME, T

ROOT = Path(__file__).resolve().parent
URL_RE = re.compile(r"^https?://[A-Za-z0-9.-]+(:\d{1,5})?$")
SITE_URL_RE = re.compile(r"^https?://[A-Za-z0-9.-]+(:\d{1,5})?(/[A-Za-z0-9._~-]+)*$")
DOMAIN_RE = re.compile(r"^(?=.{4,253}$)([A-Za-z0-9-]+\.)+[A-Za-z]{2,}$")
LOGOS = ("logo.svg", "logo.png", "logo.webp")
DATA = ROOT / "data"
ASSET_RE = re.compile(r"^assets/[A-Za-z0-9._/-]+\.(jpg|jpeg|png|webp|svg|pdf)$", re.I)
LINK_RE = re.compile(r"^https://[^\s\"'<>]+$")
SITE_RE = re.compile(r"^https?://[^\s\"'<>]+$")   # sites externes des faîtières : certains n'ont pas encore de https
COUNTER_RE = re.compile(r"^[a-z0-9-]{2,40}$")
# Pages du menu principal (les autres sont dans le pied de page)
NAV = [("index", "nav_home"), ("apropos", "nav_about"), ("gouvernance", "nav_gov"), ("membres", "nav_members"),
       ("actualites", "nav_news"), ("adhesion", "nav_join"), ("contact", "nav_contact")]


def read_data(name: str, default):
    """Lit data/<name>.json ; message clair si le fichier est mal écrit (virgule oubliée, etc.)."""
    path = DATA / f"{name}.json"
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"data/{name}.json : erreur de syntaxe ligne {e.lineno}, colonne {e.colno} ({e.msg}).")


def asset_path(where: str, value) -> str:
    """Chemin d'un fichier du site (image, PDF) : sûr et existant, sinon le site refuse de se construire."""
    value = (value or "").strip()
    if not value:
        return ""
    if ".." in value or not ASSET_RE.match(value):
        sys.exit(f"{where} : chemin de fichier invalide « {value} » (attendu : assets/dossier/nom.jpg, .png, .webp, .svg ou .pdf).")
    if not (ROOT / value).is_file():
        sys.exit(f"{where} : le fichier « {value} » n'existe pas dans le dépôt.")
    return value


def safe_link(where: str, value, allow_http: bool = False) -> str:
    value = (value or "").strip()
    if value and "://" not in value and allow_http:
        value = "https://" + value                      # « lecim-ci.org » -> « https://lecim-ci.org »
    if value and not (SITE_RE if allow_http else LINK_RE).match(value):
        sys.exit(f"{where} : le lien doit commencer par https:// et ne pas contenir d'espace (« {value} »).")
    return value


def bi(where: str, value) -> dict:
    """Texte bilingue {fr, ar} ; une simple chaîne vaut pour les deux langues."""
    if isinstance(value, str):
        return {"fr": value, "ar": value}
    if not isinstance(value, dict):
        sys.exit(f"{where} : attendu {{\"fr\": ..., \"ar\": ...}}.")
    return {"fr": str(value.get("fr", "") or ""), "ar": str(value.get("ar", "") or "")}


MONTHS = {
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
    "ar": ["يناير", "فبراير", "مارس", "أبريل", "ماي", "يونيو", "يوليوز", "غشت", "شتنبر", "أكتوبر", "نونبر", "دجنبر"],
}


def long_date(iso: str, lang: str) -> str:
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d}{'er' if d == 1 and lang == 'fr' else ''} {MONTHS[lang][m - 1]} {y}"


def load_site_data() -> dict:
    annonce = read_data("annonce", {})
    president = read_data("president", {})
    documents, galerie, regions, faitieres, actualites, equipe, partenaires = (
        read_data(n, []) for n in ("documents", "galerie", "regions", "faitieres", "actualites", "equipe", "partenaires"))
    contact = read_data("contact", {})
    for name, value in (("documents", documents), ("galerie", galerie), ("regions", regions), ("faitieres", faitieres),
                        ("actualites", actualites), ("equipe", equipe), ("partenaires", partenaires)):
        if not isinstance(value, list):
            sys.exit(f"data/{name}.json : une liste [ ... ] est attendue.")

    out = {
        "annonce": {"actif": bool(annonce.get("actif")), "texte": bi("data/annonce.json", {"fr": annonce.get("fr"), "ar": annonce.get("ar")}),
                    "lien": safe_link("data/annonce.json", annonce.get("lien"))},
        "president": {"nom": str(president.get("nom", "")).strip(), "fonction": bi("president.fonction", president.get("fonction", "")),
                      "photo": asset_path("data/president.json (photo)", president.get("photo")),
                      "message": bi("president.message", president.get("message", ""))},
        "documents": [], "galerie": [], "regions": [], "faitieres": [], "actualites": [], "equipe": [], "partenaires": [],
        "contact": {},
    }
    for i, m in enumerate(equipe, 1):
        organe = str(m.get("organe", "")).strip()
        if organe not in ("den", "ca", "cc"):
            sys.exit(f"data/equipe.json [{i}] : « organe » doit valoir den, ca ou cc (reçu : « {organe} »).")
        out["equipe"].append({"nom": str(m.get("nom", "")).strip(), "fonction": bi(f"equipe[{i}].fonction", m.get("fonction", "")),
                              "organisation": str(m.get("organisation", "")).strip(), "organe": organe,
                              "photo": asset_path(f"data/equipe.json [{i}] (photo)", m.get("photo"))})
    for i, pt in enumerate(partenaires, 1):
        kind = str(pt.get("type", "")).strip()
        if kind not in ("etat", "technique", "financier"):
            sys.exit(f"data/partenaires.json [{i}] : « type » doit valoir etat, technique ou financier (reçu : « {kind} »).")
        out["partenaires"].append({"nom": str(pt.get("nom", "")).strip(), "type": kind,
                                   "logo": asset_path(f"data/partenaires.json [{i}] (logo)", pt.get("logo")),
                                   "site_web": safe_link(f"data/partenaires.json [{i}] (site_web)", pt.get("site_web"), allow_http=True),
                                   "description": bi(f"partenaires[{i}].description", pt.get("description", ""))})
    wa = re.sub(r"[\s+().-]", "", str(contact.get("whatsapp", "")))
    if wa and not re.fullmatch(r"\d{8,15}", wa):
        sys.exit(f"data/contact.json : numéro WhatsApp invalide « {contact.get('whatsapp')} » (chiffres uniquement, avec l'indicatif, ex. 22507XXXXXXXX).")
    msg = bi("contact.message", contact.get("message", ""))
    out["contact"] = {"whatsapp_link": {l: f"https://wa.me/{wa}?text={quote(msg[l])}" for l in ("fr", "ar")} if wa else {},
                      "social": [(k, safe_link(f"data/contact.json ({k})", contact.get(k))) for k in ("facebook", "youtube", "instagram")
                                 if contact.get(k)]}
    seen_news = set()
    for i, n in enumerate(actualites, 1):
        slug, date = str(n.get("slug", "")).strip(), str(n.get("date", "")).strip()
        if not re.fullmatch(r"[a-z0-9-]{2,60}", slug) or slug in seen_news:
            sys.exit(f"data/actualites.json [{i}] : « slug » invalide ou en double (lettres minuscules, chiffres et tirets).")
        if not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])", date):
            sys.exit(f"data/actualites.json [{i}] : « date » invalide « {date} » (format attendu : AAAA-MM-JJ, ex. 2026-12-15).")
        seen_news.add(slug)
        out["actualites"].append({
            "slug": slug, "date": date, "date_long": {l: long_date(date, l) for l in ("fr", "ar")},
            "titre": bi(f"actualites[{i}].titre", n.get("titre", "")), "resume": bi(f"actualites[{i}].resume", n.get("resume", "")),
            "contenu": bi(f"actualites[{i}].contenu", n.get("contenu", "")),
            "image": asset_path(f"data/actualites.json [{i}] (image)", n.get("image"))})
    out["actualites"].sort(key=lambda n: n["date"], reverse=True)
    for i, d in enumerate(documents, 1):
        out["documents"].append({"titre": bi(f"documents[{i}].titre", d.get("titre", "")), "description": bi(f"documents[{i}].description", d.get("description", "")),
                                 "fichier": asset_path(f"data/documents.json [{i}]", d.get("fichier")), "categorie": str(d.get("categorie", ""))})
    for i, g in enumerate(galerie, 1):
        out["galerie"].append({"image": asset_path(f"data/galerie.json [{i}]", g.get("image")), "legende": bi(f"galerie[{i}].legende", g.get("legende", "")),
                               "date": str(g.get("date", ""))})
    for i, r in enumerate(regions, 1):
        item = {"drena": str(r.get("drena", "")).strip(), "region": str(r.get("region", "")).strip(),
                "delegue": str(r.get("delegue", "")).strip(), "telephone": str(r.get("telephone", "")).strip(), "lat": None, "lon": None}
        lat, lon = r.get("lat"), r.get("lon")
        if isinstance(lat, (int, float)) and isinstance(lon, (int, float)) and not isinstance(lat, bool) and not isinstance(lon, bool):
            if not (3.5 <= lat <= 11.5 and -9.5 <= lon <= -2.0):
                sys.exit(f"data/regions.json [{i}] ({item['drena']}) : coordonnées hors de la Côte d'Ivoire (lat {lat}, lon {lon}).")
            item["lat"], item["lon"] = float(lat), float(lon)
        out["regions"].append(item)
    seen = set()
    for i, f in enumerate(faitieres, 1):
        slug = str(f.get("slug", "")).strip()
        if not re.fullmatch(r"[a-z0-9-]{2,40}", slug) or slug in seen:
            sys.exit(f"data/faitieres.json [{i}] : « slug » invalide ou en double (lettres minuscules, chiffres et tirets).")
        seen.add(slug)
        out["faitieres"].append({
            "slug": slug, "sigle": str(f.get("sigle", "")).strip() or slug.upper(), "nom": bi(f"faitieres[{i}].nom", f.get("nom", "")),
            "presentation": bi(f"faitieres[{i}].presentation", f.get("presentation", "")),
            "logo": asset_path(f"data/faitieres.json [{i}] (logo)", f.get("logo")),
            "annee_creation": str(f.get("annee_creation", "")).strip(), "nombre_ecoles": str(f.get("nombre_ecoles", "")).strip(),
            "telephone": str(f.get("telephone", "")).strip(), "email": str(f.get("email", "")).strip(),
            "adresse": str(f.get("adresse", "")).strip(), "site_web": safe_link(f"data/faitieres.json [{i}] (site_web)", f.get("site_web"), allow_http=True)})
    return out


def clean_url(name: str, value: str, pattern=URL_RE, hint="https://nom-de-domaine (sans chemin ni espace)") -> str:
    value = (value or "").strip().rstrip("/")
    if value and not pattern.match(value):
        sys.exit(f"{name} invalide : « {value} ». Attendu : {hint}.")
    return value


def page_url(site_url: str, lang: str, page: str) -> str:
    folder = "ar/" if lang == "ar" else ""
    name = "" if page == "index" else f"{page}.html"
    return f"{site_url}/{folder}{name}"


def build(dist: Path | None = None) -> Path:
    api_base = clean_url("API_BASE", os.environ.get("API_BASE", ""))
    app_url = clean_url("APP_URL", os.environ.get("APP_URL", "")) or api_base
    site_url = clean_url("SITE_URL", os.environ.get("SITE_URL", ""), SITE_URL_RE,
                         "https://domaine ou https://domaine/chemin (sans espace)")
    domain = os.environ.get("CUSTOM_DOMAIN", "").strip()
    if domain and not DOMAIN_RE.match(domain):
        sys.exit(f"CUSTOM_DOMAIN invalide : « {domain} ».")
    if domain and not site_url:
        site_url = f"https://{domain}"
    counter = os.environ.get("GOATCOUNTER", "").strip().lower()
    if counter and not COUNTER_RE.match(counter):
        sys.exit(f"GOATCOUNTER invalide : « {counter} » (attendu : le code de votre compte, ex. psie).")
    dist = dist or Path(os.environ.get("DIST", ROOT / "dist"))
    site_data = load_site_data()
    pages = (list(PAGES) + [(f"faitiere-{f['slug']}", "nav_members", True) for f in site_data["faitieres"]]
             + [(f"actualite-{n['slug']}", "nav_news", True) for n in site_data["actualites"]])
    def csp_for(page: str, base_href: str = "") -> str:
        """Politique de sécurité : élargie seulement là où c'est nécessaire (fonds de carte, statistiques)."""
        img = ["'self'", "data:"] + (["https://tile.openstreetmap.org"] if page == "regions" else []) + ([f"https://{counter}.goatcounter.com"] if counter else [])
        base_uri = "'self'" if base_href else "'none'"
        script = ["'self'"] + (["https://gc.zgo.at"] if counter else [])
        connect = [api_base or "'none'"] + ([f"https://{counter}.goatcounter.com"] if counter else [])
        return (f"default-src 'self'; script-src {' '.join(script)}; style-src 'self'; img-src {' '.join(img)}; "
                f"connect-src {' '.join(connect)}; base-uri {base_uri}; form-action 'none'; object-src 'none'")

    if dist.exists():
        shutil.rmtree(dist)
    (dist / "ar").mkdir(parents=True)
    shutil.copytree(ROOT / "assets", dist / "assets")
    logo = next((n for n in LOGOS if (ROOT / "assets" / n).exists()), None)

    # Fichiers générés : QR codes et plaquettes (toujours à jour avec les textes du site)
    downloads = dist / "assets" / "dl"
    downloads.mkdir(parents=True, exist_ok=True)
    qr_items = []
    logo_file = ROOT / "assets" / logo if logo and logo.lower().endswith((".png", ".jpg", ".jpeg")) else None
    for lang in ("fr", "ar"):
        url = f"{site_url}/{'ar/' if lang == 'ar' else ''}" if site_url else ""
        if url:
            (downloads / f"qr-psie-{lang}.svg").write_bytes(extras.qr_svg(url))
            (downloads / f"qr-psie-{lang}.png").write_bytes(extras.qr_png(url))
            qr_items.append({"lang": lang, "url": url, "org": SITE_NAME[lang], "heading": T[lang]["poster_heading"], "tag": T[lang]["footer_tag"]})
        (downloads / f"plaquette-psie-{lang}.pdf").write_bytes(extras.brochure(T[lang], SITE_NAME[lang], lang, url, logo_file))
    bars = []
    for f in site_data["faitieres"]:
        digits = re.match(r"\s*(\d[\d\s.,]*)", f["nombre_ecoles"] or "")
        if digits and digits.group(1).replace(" ", "").replace(",", "").replace(".", "").isdigit():
            bars.append({"sigle": f["sigle"], "text": f["nombre_ecoles"], "value": int(re.sub(r"\D", "", digits.group(1)))})
    bars.sort(key=lambda b: -b["value"])

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))

    def render(lang, page, nav_key, in_sitemap, template, root, **extra):
        t, other = T[lang], ("ar" if lang == "fr" else "fr")
        alternates = []
        if site_url and in_sitemap:
            alternates = [("fr", page_url(site_url, "fr", page)), ("ar", page_url(site_url, "ar", page)),
                          ("x-default", page_url(site_url, "fr", page))]
        jsonld = json.dumps({
            "@context": "https://schema.org", "@type": "Organization", "name": SITE_NAME[lang], "alternateName": "PSIE",
            "url": site_url, "foundingDate": "2021-09-03",
            "address": {"@type": "PostalAddress", "streetAddress": t["address"], "addressLocality": "Abidjan", "addressCountry": "CI"},
            "telephone": [t["phone1"], t["phone2"]],
        }, ensure_ascii=False).replace("</", "<\\/") if site_url else ""
        return env.get_template(template).render(
            data=site_data, counter=counter, csp=csp_for(page, extra.get("base_href", "")), qr=qr_items, bars=bars,
            t=t, lang=lang, dir="rtl" if lang == "ar" else "ltr", site_name=SITE_NAME[lang],
            page=page, nav_key=nav_key, nav=NAV, root=root, api_base=api_base, app_url=app_url, logo=logo,
            description=t.get(f"desc_{page}", t["desc_default"]), noindex=not in_sitemap,
            site_url=site_url, canonical=page_url(site_url, lang, page) if site_url and in_sitemap else "",
            alternates=alternates, jsonld=jsonld,
            other_href=("ar/index.html" if page == "404" else f"ar/{page}.html" if lang == "fr" else f"../{page}.html"), other_lang=other,
            other_label=T[other]["lang_other"], **{"fa": None, "ne": None, **extra})

    for lang in ("fr", "ar"):
        base = "" if lang == "fr" else "../"
        for page, nav_key, in_sitemap in pages:
            fa = next((f for f in site_data["faitieres"] if page == f"faitiere-{f['slug']}"), None)
            ne = next((n for n in site_data["actualites"] if page == f"actualite-{n['slug']}"), None)
            html = render(lang, page, nav_key, in_sitemap, "faitiere.html" if fa else "actualite_article.html" if ne else f"{page}.html",
                          base, fa=fa, ne=ne)
            (dist / ("ar" if lang == "ar" else "") / f"{page}.html").write_text(html, encoding="utf-8")

    # Page « introuvable » : GitHub Pages la sert à n'importe quelle profondeur d'adresse, d'où la balise <base>
    (dist / "404.html").write_text(
        render("fr", "404", "nav_home", False, "404.html", "", base_href=f"{site_url}/" if site_url else ""), encoding="utf-8")
    if domain:
        (dist / "CNAME").write_text(domain + "\n", encoding="utf-8")
    (dist / ".nojekyll").write_text("", encoding="utf-8")
    if site_url:
        entries = []
        for page, _, in_sitemap in pages:
            if not in_sitemap:
                continue
            links = "".join(
                f'<xhtml:link rel="alternate" hreflang="{code}" href="{page_url(site_url, code, page)}"/>'
                for code in ("fr", "ar"))
            for lang in ("fr", "ar"):
                entries.append(f"<url><loc>{page_url(site_url, lang, page)}</loc>{links}</url>")
        (dist / "sitemap.xml").write_text(
            '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(entries) + "\n</urlset>\n", encoding="utf-8")
        (dist / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {site_url}/sitemap.xml\n", encoding="utf-8")
    else:
        (dist / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    (dist / "build-info.json").write_text(
        json.dumps({"api_base": api_base, "app_url": app_url, "site_url": site_url, "domain": domain or None}, indent=2),
        encoding="utf-8")
    if not api_base:
        print("Avertissement : API_BASE non défini, membres et actualités ne s'afficheront pas.", file=sys.stderr)
    if not app_url:
        print("Avertissement : APP_URL non défini, les boutons « Adhérer » et « Connexion » seront inactifs.", file=sys.stderr)
    return dist


if __name__ == "__main__":
    print(f"Site généré dans {build()}")
