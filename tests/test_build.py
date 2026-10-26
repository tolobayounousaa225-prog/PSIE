import html as htmllib
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import build as site  # noqa: E402
import content  # noqa: E402

API = "https://app.example.org"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.tags, self.attrs = [], [], []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.tags.append((tag, d))
        for k in ("href", "src"):
            if d.get(k):
                self.links.append(d[k])
        self.attrs.extend(d.keys())


def parse(path: Path) -> Page:
    p = Page()
    p.feed(path.read_text(encoding="utf-8"))
    return p


@pytest.fixture
def dist(tmp_path, monkeypatch):
    monkeypatch.setenv("API_BASE", API)
    monkeypatch.delenv("APP_URL", raising=False)
    monkeypatch.setenv("CUSTOM_DOMAIN", "psie-ci.org")
    return site.build(tmp_path / "dist")


def html_files(dist):
    return sorted(dist.rglob("*.html"))


def test_both_languages_are_generated(dist):
    for name in ("index", "apropos", "gouvernance", "membres", "adhesion", "verification", "actualites", "faq", "contact", "mentions", "actualite"):
        assert (dist / f"{name}.html").exists() and (dist / "ar" / f"{name}.html").exists()
    fr, ar = (dist / "index.html").read_text(encoding="utf-8"), (dist / "ar" / "index.html").read_text(encoding="utf-8")
    assert 'lang="fr" dir="ltr"' in fr and "Nos missions" in fr
    assert 'lang="ar" dir="rtl"' in ar and "مهامنا" in ar and "Nos missions" not in ar


def test_no_inline_script_style_or_event_handlers(dist):
    """Compatible avec la politique de sécurité du site (script-src et style-src 'self' seulement)."""
    for f in html_files(dist):
        text = f.read_text(encoding="utf-8")
        p = parse(f)
        for tag, attrs in p.tags:
            if tag == "script" and attrs.get("type") == "application/ld+json":
                continue                                    # données structurées : jamais exécutées
            if tag == "script":
                assert attrs.get("src") and not attrs.get("src").startswith("http"), f
            assert "style" not in attrs, f
            assert not any(k.startswith("on") for k in attrs), f
        assert "javascript:" not in text.lower(), f


def test_csp_matches_api_origin(dist):
    for f in html_files(dist):
        if f.name == "404.html":
            continue
        text = htmllib.unescape(f.read_text(encoding="utf-8"))   # valeur lue par le navigateur
        assert f"connect-src {API};" in text and "script-src 'self'" in text, f


def test_relative_links_all_resolve(dist):
    for f in html_files(dist):
        for link in parse(f).links:
            if re.match(r"^(https?:|mailto:|tel:|#)", link):
                continue
            target = (f.parent / link.split("?")[0].split("#")[0]).resolve()
            assert target.exists(), f"{f.relative_to(dist)} -> {link}"


def test_language_switch_points_to_the_counterpart_page(dist):
    for name in ("index", "membres", "actualite"):
        fr = parse(dist / f"{name}.html")
        ar = parse(dist / "ar" / f"{name}.html")
        assert f"ar/{name}.html" in fr.links and f"../{name}.html" in ar.links


def test_app_links_when_configured(tmp_path, monkeypatch):
    monkeypatch.setenv("API_BASE", API)
    monkeypatch.setenv("APP_URL", "https://app2.example.org")
    d = site.build(tmp_path / "d")
    links = parse(d / "index.html").links
    assert "https://app2.example.org/adhesion" in links and "https://app2.example.org/login" in links
    assert "https://app2.example.org/adhesion/suivi" in links


def test_without_app_url_buttons_are_disabled(tmp_path, monkeypatch, capsys):
    monkeypatch.delenv("API_BASE", raising=False)
    monkeypatch.delenv("APP_URL", raising=False)
    monkeypatch.delenv("CUSTOM_DOMAIN", raising=False)
    d = site.build(tmp_path / "d")
    text = (d / "index.html").read_text(encoding="utf-8")
    assert 'href="/adhesion' not in text and 'href="/login' not in text and "/login" not in text
    assert "connect-src 'none'" in htmllib.unescape(text) and not (d / "CNAME").exists()
    assert "API_BASE non défini" in capsys.readouterr().err


@pytest.mark.parametrize("bad", ["javascript:alert(1)", "https://x.org/chemin", "https://x.org\"><script>", "app.example.org",
                                 "https://a b.org", "ftp://x.org", "https://x.org;evil"])
def test_hostile_or_malformed_urls_are_rejected(tmp_path, monkeypatch, bad):
    monkeypatch.setenv("API_BASE", bad)
    with pytest.raises(SystemExit):
        site.build(tmp_path / "d")


def test_custom_domain_validation(tmp_path, monkeypatch):
    monkeypatch.setenv("API_BASE", API)
    monkeypatch.setenv("CUSTOM_DOMAIN", "psie-ci.org")
    assert (site.build(tmp_path / "ok") / "CNAME").read_text().strip() == "psie-ci.org"
    for bad in ("psie ci.org", "http://psie-ci.org", "psie", "a.org\nb.org"):
        monkeypatch.setenv("CUSTOM_DOMAIN", bad)
        with pytest.raises(SystemExit):
            site.build(tmp_path / "bad")


def test_javascript_never_builds_html_from_data():
    """Garde-fou : les données du serveur ne doivent jamais être interprétées comme du HTML."""
    js = (ROOT / "assets" / "site.js").read_text(encoding="utf-8")
    for forbidden in ("innerHTML", "outerHTML", "insertAdjacentHTML", "eval(", "document.write", "new Function", "setTimeout(\""):
        assert forbidden not in js, forbidden
    assert 'credentials: "omit"' in js                      # jamais de cookies vers l'application


def test_arabic_phone_numbers_keep_their_digit_order(dist):
    ar = (dist / "ar" / "index.html").read_text(encoding="utf-8")
    assert 'dir="ltr">+225 07 07 83 63 73</a>' in ar


def test_page_titles_and_accessibility_basics(dist):
    for f in html_files(dist):
        if f.name == "404.html":
            continue
        text = f.read_text(encoding="utf-8")
        assert "<title>" in text and 'name="viewport"' in text and 'class="skip"' in text, f


def test_french_and_arabic_content_have_the_same_structure():
    def shape(v):
        if isinstance(v, dict):
            return {k: shape(x) for k, x in v.items()}
        if isinstance(v, (list, tuple)):
            return [shape(x) for x in v]
        return type(v).__name__
    assert shape(content.T["fr"]) == shape(content.T["ar"])


def test_titles_are_unique_per_language(dist):
    for base in (dist, dist / "ar"):
        titles = []
        for f in base.glob("*.html"):
            if f.name in ("404.html", "actualite.html"):   # le détail partage le titre de la liste
                continue
            titles.append(re.search(r"<title>(.*?)</title>", f.read_text(encoding="utf-8"), re.S).group(1))
        assert len(titles) == len(set(titles))


def test_seo_files(tmp_path, monkeypatch):
    monkeypatch.setenv("API_BASE", API)
    monkeypatch.setenv("SITE_URL", "https://psie.example.org")
    d = site.build(tmp_path / "d")
    sitemap = (d / "sitemap.xml").read_text(encoding="utf-8")
    assert "https://psie.example.org/gouvernance.html" in sitemap and "hreflang" in sitemap
    assert "actualite.html" not in sitemap                  # page de détail : noindex
    assert "Sitemap: https://psie.example.org/sitemap.xml" in (d / "robots.txt").read_text(encoding="utf-8")
    page = (d / "index.html").read_text(encoding="utf-8")
    assert 'rel="canonical"' in page and 'hreflang="ar"' in page and "application/ld+json" in page


# ---------- ressources : données modifiables, nouvelles pages ----------

@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    """Copie du dépôt dans laquelle on peut écrire des données d'essai sans toucher au vrai dossier data/."""
    import shutil
    root = tmp_path / "repo"
    shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "dist", "__pycache__", ".pytest_cache"))
    monkeypatch.setattr(site, "ROOT", root)
    monkeypatch.setattr(site, "DATA", root / "data")
    monkeypatch.setenv("API_BASE", API)
    monkeypatch.delenv("GOATCOUNTER", raising=False)
    return root


def write_json(root, name, value):
    import json
    (root / "data" / f"{name}.json").write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")


def test_new_pages_and_member_sheets_exist(dist):
    for name in ("documents", "regions", "galerie", "faitiere-lecim", "faitiere-al-hikma"):
        assert (dist / f"{name}.html").exists() and (dist / "ar" / f"{name}.html").exists()
    assert "faitiere-lecim.html" in parse(dist / "membres.html").links


def test_empty_data_shows_soon_messages_and_hides_optional_blocks(dist):
    docs = (dist / "documents.html").read_text(encoding="utf-8")
    assert "bientôt disponibles" in docs
    home = (dist / "index.html").read_text(encoding="utf-8")
    assert "Le mot du Président" not in home and 'class="announce"' not in home


def test_filled_data_is_rendered(sandbox, tmp_path):
    (sandbox / "assets" / "docs").mkdir(exist_ok=True)
    (sandbox / "assets" / "docs" / "statuts.pdf").write_bytes(b"%PDF-1.4")
    write_json(sandbox, "documents", [{"titre": {"fr": "Statuts", "ar": "النظام"}, "fichier": "assets/docs/statuts.pdf"}])
    write_json(sandbox, "annonce", {"actif": True, "fr": "AG le 15 décembre", "ar": "الجمعية", "lien": "https://example.org/ag"})
    write_json(sandbox, "president", {"nom": "A. B.", "message": {"fr": "Bonjour\nTous", "ar": "مرحبا"}})
    write_json(sandbox, "regions", [{"drena": "Bouaké", "region": "Gbêkê", "lat": 7.69, "lon": -5.03}])
    d = site.build(tmp_path / "out")
    assert "assets/docs/statuts.pdf" in parse(d / "documents.html").links
    home = (d / "index.html").read_text(encoding="utf-8")
    assert "AG le 15 décembre" in home and 'href="https://example.org/ag"' in home and "Le mot du Président" in home
    assert 'data-lat="7.69"' in (d / "regions.html").read_text(encoding="utf-8")


def test_html_in_data_is_escaped(sandbox, tmp_path):
    write_json(sandbox, "annonce", {"actif": True, "fr": "<script>alert(1)</script>", "ar": "x"})
    d = site.build(tmp_path / "out")
    text = (d / "index.html").read_text(encoding="utf-8")
    assert "<script>alert(1)</script>" not in text and "&lt;script&gt;" in text


@pytest.mark.parametrize("name,value", [
    ("documents", [{"titre": "x", "fichier": "../secret.pdf"}]),
    ("documents", [{"titre": "x", "fichier": "assets/docs/absent.pdf"}]),
    ("galerie", [{"image": "http://evil.example/x.jpg"}]),
    ("annonce", {"actif": True, "fr": "x", "ar": "x", "lien": "javascript:alert(1)"}),
    ("faitieres", [{"slug": "Mauvais Slug", "sigle": "X"}]),
    ("faitieres", [{"slug": "a", "sigle": "A", "site_web": "javascript:alert(1)"}]),
    ("faitieres", [{"slug": "a", "sigle": "A", "site_web": "https://x.org/a b"}]),
    ("regions", {"pas": "une liste"}),
])
def test_invalid_data_is_refused_with_a_clear_message(sandbox, tmp_path, name, value):
    write_json(sandbox, name, value)
    with pytest.raises(SystemExit) as e:
        site.build(tmp_path / "out")
    assert str(e.value)                       # message lisible, pas une trace technique


def test_json_syntax_error_names_the_file_and_line(sandbox, tmp_path):
    (sandbox / "data" / "documents.json").write_text('[\n  {"titre": "x",\n]', encoding="utf-8")
    with pytest.raises(SystemExit) as e:
        site.build(tmp_path / "out")
    assert "documents.json" in str(e.value) and "ligne" in str(e.value)


def test_analytics_is_opt_in_and_widens_csp_only_then(sandbox, tmp_path, monkeypatch):
    plain = (site.build(tmp_path / "a") / "index.html").read_text(encoding="utf-8")
    assert "goatcounter" not in plain
    monkeypatch.setenv("GOATCOUNTER", "psie")
    text = (site.build(tmp_path / "b") / "index.html").read_text(encoding="utf-8")
    assert 'data-goatcounter="https://psie.goatcounter.com/count"' in text and "https://gc.zgo.at" in htmllib.unescape(text)
    monkeypatch.setenv("GOATCOUNTER", "x\"><script>")
    with pytest.raises(SystemExit):
        site.build(tmp_path / "c")


def test_member_website_without_scheme_gets_https(sandbox, tmp_path):
    write_json(sandbox, "faitieres", [{"slug": "lecim", "sigle": "LECIM", "site_web": "lecim-ci.org"}])
    d = site.build(tmp_path / "out")
    assert 'href="https://lecim-ci.org"' in (d / "faitiere-lecim.html").read_text(encoding="utf-8")


def test_interactive_map_markup(dist):
    page = parse(dist / "regions.html")
    ids = {d.get("id") for _, d in page.tags}
    assert {"civ-map", "civ-info", "region-search", "region-list"} <= ids
    assert "assets/vendor/leaflet/leaflet.js" in page.links and "assets/vendor/leaflet/leaflet.css" in page.links
    assert (dist / "assets" / "vendor" / "leaflet" / "leaflet.js").exists() and (dist / "assets" / "vendor" / "leaflet" / "LICENSE").exists()
    rows = [d for t, d in page.tags if t == "li" and "data-lat" in d]
    located = [d for d in rows if d["data-lat"] != ""]
    assert len(rows) == 41 and len(located) == 41 and all(d.get("tabindex") == "0" for d in located)


def test_map_tiles_are_allowed_only_on_the_map_page(dist):
    def csp(name):
        return htmllib.unescape(re.search(r'http-equiv="Content-Security-Policy" content="([^"]*)"', (dist / name).read_text(encoding="utf-8")).group(1))
    assert "https://tile.openstreetmap.org" in csp("regions.html") and "https://tile.openstreetmap.org" in csp("ar/regions.html")
    for other in ("index.html", "membres.html", "contact.html", "faitiere-lecim.html"):
        assert "openstreetmap" not in csp(other), other
    assert "script-src 'self';" in csp("regions.html")          # aucun script tiers : Leaflet est dans le site


def test_region_coordinates_outside_the_country_are_refused(sandbox, tmp_path):
    write_json(sandbox, "regions", [{"drena": "Erreur", "lat": 48.85, "lon": 2.35}])
    with pytest.raises(SystemExit) as e:
        site.build(tmp_path / "out")
    assert "hors de la Côte d'Ivoire" in str(e.value)


# ---------- actualités publiées dans le site ----------

def test_news_without_data_or_server_shows_a_message_not_a_loading_placeholder(tmp_path, monkeypatch):
    monkeypatch.delenv("API_BASE", raising=False)
    monkeypatch.delenv("APP_URL", raising=False)
    d = site.build(tmp_path / "d")
    news = (d / "actualites.html").read_text(encoding="utf-8")
    assert "skeleton" not in news and "Aucune actualité pour le moment" in news
    assert 'id="home-news-section"' not in (d / "index.html").read_text(encoding="utf-8")


def test_news_with_server_but_no_published_items_keeps_loading_placeholders(dist):
    assert "skeleton" in (dist / "actualites.html").read_text(encoding="utf-8")


def test_published_news_pages_and_cards(sandbox, tmp_path):
    write_json(sandbox, "actualites", [
        {"slug": "ag-2026", "date": "2026-12-15", "titre": {"fr": "AG <b>2026</b>", "ar": "الجمعية"},
         "resume": {"fr": "Rendez-vous à Bouaké.", "ar": "موعد ببواكي."}, "contenu": {"fr": "Premier paragraphe.\nSecond.", "ar": "نص"}},
        {"slug": "ouverture", "date": "2026-10-20", "titre": {"fr": "Ouverture", "ar": "فتح"}, "resume": {"fr": "x", "ar": "x"}, "contenu": {"fr": "y", "ar": "y"}},
    ])
    d = site.build(tmp_path / "out")
    assert (d / "actualite-ag-2026.html").exists() and (d / "ar" / "actualite-ag-2026.html").exists()
    listing = (d / "actualites.html").read_text(encoding="utf-8")
    assert listing.index("AG &lt;b&gt;2026") < listing.index("Ouverture")        # la plus récente d'abord, texte échappé
    assert "15 décembre 2026" in listing and "skeleton" not in listing
    assert "<b>2026</b>" not in listing
    assert "Second." in (d / "actualite-ag-2026.html").read_text(encoding="utf-8")
    assert "actualite-ag-2026.html" in (d / "sitemap.xml").read_text(encoding="utf-8") if (d / "sitemap.xml").exists() else True
    assert 'id="home-news-section"' in (d / "index.html").read_text(encoding="utf-8")


@pytest.mark.parametrize("item", [
    {"slug": "Mauvais Slug", "date": "2026-12-15"}, {"slug": "ok", "date": "15/12/2026"}, {"slug": "ok", "date": "2026-13-40"},
])
def test_invalid_news_is_refused(sandbox, tmp_path, item):
    write_json(sandbox, "actualites", [item])
    with pytest.raises(SystemExit) as e:
        site.build(tmp_path / "out")
    assert "actualites.json" in str(e.value)


# ---------- histoire, bureau, partenaires, glossaire, confidentialité, 404, réseaux ----------

def test_new_informational_pages_exist_in_both_languages(dist):
    for name in ("equipe", "partenaires", "glossaire", "confidentialite"):
        assert (dist / f"{name}.html").exists() and (dist / "ar" / f"{name}.html").exists()
    about = (dist / "apropos.html").read_text(encoding="utf-8")
    assert about.count('class="dot"') == 4 and "3 septembre 2021" in about
    gloss = (dist / "ar" / "glossaire.html").read_text(encoding="utf-8")
    assert "DRENA" in gloss and "النصاب" in gloss


def test_404_page_works_at_any_depth_and_stays_safe(tmp_path, monkeypatch):
    monkeypatch.setenv("API_BASE", API)
    monkeypatch.setenv("SITE_URL", "https://x.github.io/PSIE")
    d = site.build(tmp_path / "d")
    text = (d / "404.html").read_text(encoding="utf-8")
    assert '<base href="https://x.github.io/PSIE/">' in text and "base-uri &#39;self&#39;" in text and "Page introuvable" in text
    assert "ar/index.html" in text and "noindex" in text
    other = (d / "index.html").read_text(encoding="utf-8")
    assert "<base " not in other and "base-uri &#39;none&#39;" in other          # seule la 404 a besoin de <base>
    monkeypatch.delenv("SITE_URL")
    assert "<base " not in (site.build(tmp_path / "e") / "404.html").read_text(encoding="utf-8")


def test_team_partners_whatsapp_and_social(sandbox, tmp_path):
    (sandbox / "assets" / "equipe").mkdir(exist_ok=True)
    write_json(sandbox, "equipe", [{"nom": "A. Diallo", "fonction": {"fr": "Directeur Exécutif National", "ar": "المدير"}, "organisation": "LECIM", "organe": "den"},
                                   {"nom": "B. <b>X</b>", "fonction": "Administrateur", "organe": "ca"}])
    write_json(sandbox, "partenaires", [{"nom": "Ministère", "type": "etat", "site_web": "https://example.org"}])
    write_json(sandbox, "contact", {"whatsapp": "+225 07 07 83 63 73", "message": {"fr": "Bonjour & merci", "ar": "سلام"},
                                    "facebook": "https://facebook.com/psie", "youtube": ""})
    d = site.build(tmp_path / "out")
    team = (d / "equipe.html").read_text(encoding="utf-8")
    assert "Direction Exécutive Nationale" in team and "A. Diallo" in team and "B. &lt;b&gt;X&lt;/b&gt;" in team
    assert team.index("Direction Exécutive Nationale") < team.index("Conseil d&#39;Administration")
    assert 'href="https://wa.me/22507078363' in (d / "contact.html").read_text(encoding="utf-8")
    assert "Bonjour%20%26%20merci" in (d / "contact.html").read_text(encoding="utf-8")
    foot = (d / "index.html").read_text(encoding="utf-8")
    assert "https://facebook.com/psie" in foot and "youtube.com" not in foot
    assert "example.org" in (d / "partenaires.html").read_text(encoding="utf-8")


@pytest.mark.parametrize("name,value", [
    ("equipe", [{"nom": "X", "organe": "president"}]),
    ("partenaires", [{"nom": "X", "type": "ami"}]),
    ("contact", {"whatsapp": "abc"}),
    ("contact", {"facebook": "javascript:alert(1)"}),
])
def test_invalid_team_partner_contact_data_is_refused(sandbox, tmp_path, name, value):
    write_json(sandbox, name, value)
    with pytest.raises(SystemExit):
        site.build(tmp_path / "out")


def test_privacy_and_legal_texts_follow_the_analytics_setting(sandbox, tmp_path, monkeypatch):
    off = site.build(tmp_path / "a")
    assert "n'utilise aucun outil de mesure d'audience" in (off / "confidentialite.html").read_text(encoding="utf-8").replace("&#39;", "'")
    assert "GoatCounter" not in (off / "mentions.html").read_text(encoding="utf-8")
    monkeypatch.setenv("GOATCOUNTER", "psie")
    on = site.build(tmp_path / "b")
    assert "GoatCounter" in (on / "confidentialite.html").read_text(encoding="utf-8") and "GoatCounter" in (on / "mentions.html").read_text(encoding="utf-8")
    assert "OpenStreetMap" in (on / "confidentialite.html").read_text(encoding="utf-8")        # la carte est annoncée dans tous les cas


# ---------- statuts en bref, questionnaire, organigramme, affiche, plaquette, graphique ----------

def test_rules_page_has_ten_cards_in_both_languages(dist):
    for base in (dist, dist / "ar"):
        text = (base / "statuts.html").read_text(encoding="utf-8")
        assert text.count('class="card rule tilt"') == 10
    assert "quinze jours" in (dist / "statuts.html").read_text(encoding="utf-8")


def test_eligibility_checker_is_built_from_the_site_conditions(dist):
    for base in (dist, dist / "ar"):
        page = parse(base / "adhesion.html")
        questions = [d for t, d in page.tags if t == "li" and "data-condition" in d]
        assert len(questions) == 5 and all(q["data-condition"] for q in questions)
    assert len(content.T["fr"]["elig_questions"]) == len(content.T["fr"]["elig_conditions"]) == len(content.T["ar"]["elig_questions"])


def test_interactive_org_chart_markup(dist):
    page = parse(dist / "gouvernance.html")
    organs = [d for t, d in page.tags if "data-organ" in d]
    cards = [d for t, d in page.tags if "data-organ-card" in d]
    assert len(organs) == 4 and len(cards) == 4
    assert "organ-panel" in {d.get("id") for _, d in page.tags}


def test_qr_codes_and_brochures_are_generated(tmp_path, monkeypatch):
    monkeypatch.setenv("API_BASE", API)
    monkeypatch.setenv("SITE_URL", "https://x.github.io/PSIE")
    d = site.build(tmp_path / "d")
    for lang in ("fr", "ar"):
        pdf = (d / "assets" / "dl" / f"plaquette-psie-{lang}.pdf").read_bytes()
        assert pdf.startswith(b"%PDF") and pdf.count(b"/Type /Page\n") + pdf.count(b"/Type /Page ") >= 1 and len(pdf) > 20000
        assert (d / "assets" / "dl" / f"qr-psie-{lang}.png").read_bytes().startswith(b"\x89PNG")
        assert b"<svg" in (d / "assets" / "dl" / f"qr-psie-{lang}.svg").read_bytes()
    poster = (d / "affiche.html").read_text(encoding="utf-8")
    assert "https://x.github.io/PSIE/ar/" in poster and poster.count('class="poster ') == 2
    assert "affiche.html" in (d / "sitemap.xml").read_text(encoding="utf-8")


def test_poster_without_site_address_explains_why_but_brochures_still_exist(tmp_path, monkeypatch):
    monkeypatch.setenv("API_BASE", API)
    monkeypatch.delenv("SITE_URL", raising=False)
    monkeypatch.delenv("CUSTOM_DOMAIN", raising=False)
    d = site.build(tmp_path / "d")
    assert "dès que l'adresse du site sera définie" in (d / "affiche.html").read_text(encoding="utf-8").replace("&#39;", "'")
    assert (d / "assets" / "dl" / "plaquette-psie-fr.pdf").exists() and not (d / "assets" / "dl" / "qr-psie-fr.svg").exists()


def test_size_chart_needs_two_numeric_values(sandbox, tmp_path):
    write_json(sandbox, "faitieres", [{"slug": "aaa", "sigle": "AAA", "nombre_ecoles": "430+"}, {"slug": "bbb", "sigle": "BBB", "nombre_ecoles": "5"},
                                      {"slug": "ccc", "sigle": "CCC", "nombre_ecoles": "inconnu"}])
    d = site.build(tmp_path / "ok")
    text = (d / "membres.html").read_text(encoding="utf-8")
    assert 'id="repartition"' in text and text.index("AAA") < text.index("BBB") and "CCC</span>" not in text.split('id="repartition"')[1].split("</section>")[0]
    write_json(sandbox, "faitieres", [{"slug": "aaa", "sigle": "AAA", "nombre_ecoles": "430+"}])
    assert 'id="repartition"' not in (site.build(tmp_path / "one") / "membres.html").read_text(encoding="utf-8")


# ---------- centre de transparence, devenir partenaire, guide de l'espace membre ----------

def test_transparency_partnership_and_guide_pages_exist(dist):
    for name in ("transparence", "partenariat", "guide"):
        assert (dist / f"{name}.html").exists() and (dist / "ar" / f"{name}.html").exists()
    assert "Les premiers documents seront bientôt publiés" in (dist / "transparence.html").read_text(encoding="utf-8")
    assert "partenariat.html" in parse(dist / "partenaires.html").links


def test_transparency_documents_are_grouped_by_year_with_filters(sandbox, tmp_path):
    (sandbox / "assets" / "transparence").mkdir(exist_ok=True)
    for name in ("a", "b", "c"):
        (sandbox / "assets" / "transparence" / f"{name}.pdf").write_bytes(b"%PDF-1.4 " + b"x" * 2048)
    write_json(sandbox, "transparence", [
        {"titre": {"fr": "Rapport <b>2026</b>", "ar": "تقرير"}, "categorie": "rapport_activite", "annee": 2026, "fichier": "assets/transparence/a.pdf"},
        {"titre": "États 2025", "categorie": "etats_financiers", "annee": 2025, "fichier": "assets/transparence/b.pdf"},
        {"titre": "PV 2025", "categorie": "proces_verbal", "annee": 2025, "fichier": "assets/transparence/c.pdf"},
    ])
    text = (site.build(tmp_path / "out") / "transparence.html").read_text(encoding="utf-8")
    assert text.index("2026") < text.index("2025")                       # années récentes d'abord
    assert text.count('data-filter="kind"') == 1 and text.count('data-filter="year"') == 1
    assert 'data-kind="etats_financiers"' in text and "Rapport &lt;b&gt;2026" in text and "PDF · 2 Ko" in text
    assert 'data-value="budget"' not in text                              # pas de filtre sur un type absent


@pytest.mark.parametrize("item", [
    {"titre": "x", "categorie": "inconnu", "annee": 2026, "fichier": "assets/transparence/a.pdf"},
    {"titre": "x", "categorie": "budget", "annee": "2026", "fichier": "assets/transparence/a.pdf"},
    {"titre": "x", "categorie": "budget", "annee": 1999, "fichier": "assets/transparence/a.pdf"},
    {"titre": "x", "categorie": "budget", "annee": 2026, "fichier": "assets/logo.png"},
    {"titre": "x", "categorie": "budget", "annee": 2026, "fichier": "assets/transparence/absent.pdf"},
])
def test_invalid_transparency_entries_are_refused(sandbox, tmp_path, item):
    (sandbox / "assets" / "transparence").mkdir(exist_ok=True)
    (sandbox / "assets" / "transparence" / "a.pdf").write_bytes(b"%PDF-1.4")
    write_json(sandbox, "transparence", [item])
    with pytest.raises(SystemExit) as e:
        site.build(tmp_path / "out")
    assert "transparence.json" in str(e.value)


def test_partnership_whatsapp_uses_its_own_message(sandbox, tmp_path):
    write_json(sandbox, "contact", {"whatsapp": "22507078363", "message": {"fr": "Salut général", "ar": "x"},
                                    "message_partenariat": {"fr": "Partenariat svp", "ar": "شراكة"}})
    d = site.build(tmp_path / "out")
    part = (d / "partenariat.html").read_text(encoding="utf-8")
    button = re.search(r'class="btn whatsapp" href="([^"]+)"', part).group(1)          # le bouton de la page, pas l'icône du pied de page
    assert "Partenariat%20svp" in button and "Salut" not in button
    contact_button = re.search(r'class="btn whatsapp" href="([^"]+)"', (d / "contact.html").read_text(encoding="utf-8")).group(1)
    assert "Salut%20g" in contact_button
    write_json(sandbox, "contact", {})
    assert "wa.me" not in (site.build(tmp_path / "out2") / "partenariat.html").read_text(encoding="utf-8")


def test_guide_shows_login_links_only_when_the_app_is_configured(tmp_path, monkeypatch):
    monkeypatch.delenv("API_BASE", raising=False)
    monkeypatch.delenv("APP_URL", raising=False)
    off = (site.build(tmp_path / "a") / "guide.html").read_text(encoding="utf-8")
    assert "ouvrira prochainement" in off and "/login" not in off
    monkeypatch.setenv("APP_URL", "https://app.example.org")
    on = (site.build(tmp_path / "b") / "guide.html").read_text(encoding="utf-8")
    assert 'href="https://app.example.org/login"' in on and "ouvrira prochainement" not in on
