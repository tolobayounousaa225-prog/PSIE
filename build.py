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
import re
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from content import PAGES, SITE_NAME, T

ROOT = Path(__file__).resolve().parent
URL_RE = re.compile(r"^https?://[A-Za-z0-9.-]+(:\d{1,5})?$")
SITE_URL_RE = re.compile(r"^https?://[A-Za-z0-9.-]+(:\d{1,5})?(/[A-Za-z0-9._~-]+)*$")
DOMAIN_RE = re.compile(r"^(?=.{4,253}$)([A-Za-z0-9-]+\.)+[A-Za-z]{2,}$")
LOGOS = ("logo.svg", "logo.png", "logo.webp")
# Pages du menu principal (les autres sont dans le pied de page)
NAV = [("index", "nav_home"), ("apropos", "nav_about"), ("gouvernance", "nav_gov"), ("membres", "nav_members"),
       ("actualites", "nav_news"), ("adhesion", "nav_join"), ("contact", "nav_contact")]


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
        for page, nav_key, in_sitemap in PAGES:
            t = T[lang]
            alternates = []
            if site_url and in_sitemap:
                alternates = [("fr", page_url(site_url, "fr", page)), ("ar", page_url(site_url, "ar", page)),
                              ("x-default", page_url(site_url, "fr", page))]
            jsonld = json.dumps({
                "@context": "https://schema.org", "@type": "Organization", "name": SITE_NAME[lang], "alternateName": "PSIE",
                "url": site_url, "foundingDate": "2021-09-03",
                "address": {"@type": "PostalAddress", "streetAddress": t["address"], "addressLocality": "Abidjan",
                            "addressCountry": "CI"},
                "telephone": [t["phone1"], t["phone2"]],
            }, ensure_ascii=False).replace("</", "<\\/") if site_url else ""
            html = env.get_template(f"{page}.html").render(
                t=t, lang=lang, dir="rtl" if lang == "ar" else "ltr", site_name=SITE_NAME[lang],
                page=page, nav_key=nav_key, nav=NAV, root=base, api_base=api_base, app_url=app_url, logo=logo,
                description=t.get(f"desc_{page}", t["desc_default"]), noindex=not in_sitemap,
                site_url=site_url, canonical=page_url(site_url, lang, page) if site_url and in_sitemap else "",
                alternates=alternates, jsonld=jsonld,
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
    if site_url:
        entries = []
        for page, _, in_sitemap in PAGES:
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
