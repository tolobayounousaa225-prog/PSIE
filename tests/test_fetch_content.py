import hashlib
import json
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import fetch_content as fc  # noqa: E402

LISTS = ("actualites", "equipe", "partenaires", "documents", "transparence", "galerie", "faitieres", "regions")
PNG = b"\x89PNG\r\n\x1a\n" + b"0" * 50


def document(**over):
    doc = {"annonce": {"actif": False, "fr": "", "ar": "", "lien": ""}, "president": {"nom": "Dr X", "photo": "assets/media/7.png"},
           "contact": {}, "media": [{"path": "assets/media/7.png", "url": "/medias/7.png", "sha256": hashlib.sha256(PNG).hexdigest()}],
           "version": "abc123"}
    doc.update({k: [] for k in LISTS})
    doc.update(over)
    return doc


@pytest.fixture
def server():
    routes = {}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            hit = routes.get(self.path)
            if hit is None:
                self.send_response(404)
                self.end_headers()
            elif isinstance(hit, tuple):                  # redirection
                self.send_response(302)
                self.send_header("Location", hit[0])
                self.end_headers()
            else:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(hit)

        def log_message(self, *args):
            pass

    httpd = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    routes["base"] = f"http://127.0.0.1:{httpd.server_port}"
    yield routes
    httpd.shutdown()


@pytest.fixture
def site(tmp_path):
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "annonce.json").write_text('{"ancien": true}', encoding="utf-8")
    (tmp_path / "assets" / "media").mkdir(parents=True)
    (tmp_path / "assets" / "media" / "vieux.png").write_bytes(b"vieux")
    return tmp_path


def publish(routes, doc=None):
    routes["/api/public/site.json"] = json.dumps(doc if doc is not None else document()).encode()
    routes["/medias/7.png"] = PNG
    return routes["base"] + "/api/public/site.json"


def unchanged(site):
    return (json.loads((site / "data" / "annonce.json").read_text()) == {"ancien": True}
            and (site / "assets" / "media" / "vieux.png").exists() and not (site / ".contenu-staging").exists())


def test_content_and_files_replace_the_local_ones(server, site):
    info = fc.run(publish(server), site, allow_insecure=True)
    assert info == {"version": "abc123", "fichiers": 1}
    assert json.loads((site / "data" / "president.json").read_text(encoding="utf-8"))["nom"] == "Dr X"
    assert (site / "assets" / "media" / "7.png").read_bytes() == PNG
    assert not (site / "assets" / "media" / "vieux.png").exists()          # le dossier est celui de l'application
    assert {p.stem for p in (site / "data").glob("*.json")} == set(fc.SINGLETONS + fc.LISTS + fc.OPTIONAL_LISTS + fc.OPTIONAL_DICTS)
    assert not (site / ".contenu-staging").exists()


@pytest.mark.parametrize("break_it,message", [
    (lambda r: r.pop("/medias/7.png"), "erreur 404"),
    (lambda r: r.__setitem__("/medias/7.png", PNG + b"altere"), "altéré"),
    (lambda r: r.__setitem__("/medias/7.png", b"x" * (fc.MAX_FILE + 10)), "trop volumineuse"),
    (lambda r: r.__setitem__("/api/public/site.json", b"<html>erreur</html>"), "JSON valide"),
    (lambda r: r.__setitem__("/api/public/site.json", b"[]"), "objet JSON"),
    (lambda r: r.pop("/api/public/site.json"), "erreur 404"),
])
def test_any_problem_leaves_everything_untouched(server, site, break_it, message):
    url = publish(server)
    break_it(server)
    with pytest.raises(fc.FetchError, match=message):
        fc.run(url, site, allow_insecure=True)
    assert unchanged(site)


@pytest.mark.parametrize("doc,message", [
    (document(actualites="pas une liste"), "actualites"),
    (document(president=[]), "president"),
    (document(media="x"), "liste des fichiers"),
    (document(media=[{"path": "../../etc/passwd", "url": "/medias/7.png", "sha256": "0" * 64}]), "invalide"),
    (document(media=[{"path": "assets/media/7.png", "url": "https://evil.example/x.png", "sha256": "0" * 64}]), "invalide"),
    (document(media=[{"path": "assets/media/7.svg", "url": "/medias/7.svg", "sha256": "0" * 64}]), "invalide"),
    (document(media=[{"path": "assets/media/7.png", "url": "/medias/7.png", "sha256": "zz"}]), "invalide"),
    (document(media=document()["media"] * 2), "en double"),
])
def test_malformed_content_is_refused(server, site, doc, message):
    with pytest.raises(fc.FetchError, match=message):
        fc.run(publish(server, doc), site, allow_insecure=True)
    assert unchanged(site)


def test_only_https_urls_are_accepted_in_production(site):
    for url in ("http://app.example.org/api/public/site.json", "ftp://x/y", "https://user:pw@app.example.org/x", "https:///x",
                "http://127.0.0.1:9/x"):
        with pytest.raises(fc.FetchError, match="https"):
            fc.run(url, site)
    assert unchanged(site)


def test_redirects_are_refused(server, site):
    server["/api/public/site.json"] = ("http://169.254.169.254/latest/meta-data",)
    with pytest.raises(fc.FetchError, match="redirection"):
        fc.run(server["base"] + "/api/public/site.json", site, allow_insecure=True)
    assert unchanged(site)


def test_unreachable_application_is_an_error(site):
    with pytest.raises(fc.FetchError, match="injoignable"):
        fc.run("http://127.0.0.1:9/api/public/site.json", site, allow_insecure=True)
    assert unchanged(site)


def test_cli_does_nothing_without_a_url_and_fails_loudly_with_a_bad_one(monkeypatch, capsys):
    monkeypatch.delenv("CONTENT_URL", raising=False)
    assert fc.main() == 0 and "conservé" in capsys.readouterr().out
    monkeypatch.setenv("CONTENT_URL", "http://pas-https.example")
    assert fc.main() == 1 and "construction annulée" in capsys.readouterr().err


def test_directory_list_is_optional_validated_and_written(server, site):
    old = document()                                             # application sans annuaire : liste vide, pas d'échec
    assert "annuaire" not in old
    fc.run(publish(server, old), site, allow_insecure=True)
    assert json.loads((site / "data" / "annuaire.json").read_text()) == []
    good = document(annuaire=[{"nom": "École A", "niveau": "primaire", "localite": "X", "drena": "Y", "faitiere": "LECIM"}])
    fc.run(publish(server, good), site, allow_insecure=True)
    assert json.loads((site / "data" / "annuaire.json").read_text())[0]["nom"] == "École A"
    for bad in ("pas une liste", [{"nom": 3}], [["x"]], [{"nom": "x" * 300}]):
        with pytest.raises(fc.FetchError):
            fc.run(publish(server, document(annuaire=bad)), site, allow_insecure=True)
    assert json.loads((site / "data" / "annuaire.json").read_text())[0]["nom"] == "École A"      # rien n'a changé après un échec


def test_page_texts_are_optional_and_validated(server, site):
    fc.run(publish(server, document()), site, allow_insecure=True)             # ancienne application : textes d'origine
    assert json.loads((site / "data" / "textes.json").read_text()) == {}
    good = {"faq": [{"q": {"fr": "Q", "ar": ""}, "a": {"fr": "R", "ar": ""}}]}
    fc.run(publish(server, document(textes=good)), site, allow_insecure=True)
    assert json.loads((site / "data" / "textes.json").read_text()) == good
    with pytest.raises(fc.FetchError):
        fc.run(publish(server, document(textes=["pas un objet"])), site, allow_insecure=True)
