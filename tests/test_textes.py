import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import content  # noqa: E402
import textes  # noqa: E402

T = content.T


def test_without_data_nothing_changes():
    assert textes.apply(T, {}) == T and textes.apply(T, None) == T and textes.apply(T, "x") == T
    assert textes.apply(T, {"faq": "pas une liste", "txt_accueil": []}) == T


def test_blocks_override_only_filled_fields_per_language():
    data = {"txt_accueil": {"hero_title_a": {"fr": "Nouveau titre", "ar": ""}, "hero_intro": {"fr": "", "ar": ""},
                            "inconnu": {"fr": "x", "ar": "x"}}}
    out = textes.apply(T, data)
    assert out["fr"]["hero_title_a"] == "Nouveau titre"
    assert out["ar"]["hero_title_a"] == T["ar"]["hero_title_a"]          # arabe vide : texte d'origine
    assert out["fr"]["hero_intro"] == T["fr"]["hero_intro"]
    assert "inconnu" not in out["fr"]
    assert T["fr"]["hero_title_a"] != "Nouveau titre"                    # l'original n'est pas modifié


def test_paragraph_fields_and_phones():
    out = textes.apply(T, {"txt_apropos": {"story": {"fr": "Un.\n\nDeux.\nTrois.", "ar": ""}},
                           "txt_contact": {"phone1": "+225 01 02 03 04"}})
    assert out["fr"]["story"] == ["Un.", "Deux.", "Trois."] and out["ar"]["story"] == T["ar"]["story"]
    assert out["fr"]["phone1"] == out["ar"]["phone1"] == "+225 01 02 03 04"


def test_lists_replace_when_filled_and_skip_incomplete_items():
    rows = [{"q": {"fr": "Q1 ?", "ar": "س1"}, "a": {"fr": "R1", "ar": "ج1"}},
            {"q": {"fr": "Q2 ?", "ar": ""}, "a": {"fr": "R2", "ar": "ج2"}}]
    out = textes.apply(T, {"faq": rows})
    assert [x["q"] for x in out["fr"]["faq"]] == ["Q1 ?", "Q2 ?"]
    assert [x["q"] for x in out["ar"]["faq"]] == ["س1"]                  # l'élément sans question arabe est ignoré
    assert textes.apply(T, {"faq": []}) == T                             # liste vide : texte d'origine
    bad = textes.apply(T, {"faq": [{"q": {"fr": "", "ar": ""}}, "x", 3]})
    assert bad["fr"]["faq"] == T["fr"]["faq"]


def test_legal_paragraphs_and_rule_icons():
    out = textes.apply(T, {"mentions": [{"t": {"fr": "Bloc", "ar": ""}, "p": {"fr": "A\nB", "ar": ""}}],
                           "statuts_points": [{"t": {"fr": "Point", "ar": ""}, "d": {"fr": "D", "ar": ""}}]})
    assert out["fr"]["legal"] == [{"t": "Bloc", "p": ["A", "B"]}]
    assert out["fr"]["rules"][0]["i"] == T["fr"]["rules"][0]["i"]


def test_every_default_key_exists_in_the_site_texts():
    for key in textes.SINGLE_KEYS:
        pass
    for key, (tkey, fields, required) in textes.LISTS.items():
        assert tkey in T["fr"] and tkey in T["ar"], key
        for item in T["fr"][tkey]:
            assert set(fields) <= set(item) | {"full"}, key
