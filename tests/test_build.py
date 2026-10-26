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
