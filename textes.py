"""Textes des pages modifiables depuis l'application (data/textes.json).

Règle d'or : ce qui n'est pas renseigné garde le texte d'origine (content.T). Un champ vide, une liste vide ou une
donnée mal formée ne casse donc jamais une page."""
from __future__ import annotations

import copy

PARAGRAPH_KEYS = {"story"}                       # textes que le site garde en liste de paragraphes
SINGLE_KEYS = {                                   # rubriques « bloc » : champ -> clé de texte du site (identiques)
    "txt_accueil", "txt_apropos", "txt_gouvernance", "txt_adhesion", "txt_contact", "txt_statuts", "txt_guide", "txt_legal"}
LISTS = {                                         # rubrique -> clé de la liste du site, champs repris, champ obligatoire
    "faq": ("faq", ("q", "a"), "q"),
    "guide_faq": ("guide_faq", ("q", "a"), "q"),
    "glossaire": ("glossary", ("term", "full", "d"), "term"),
    "missions": ("missions", ("t", "d"), "t"),
    "chronologie": ("timeline", ("date", "t", "d"), "t"),
    "statuts_points": ("rules", ("t", "d"), "t"),
    "droits": ("rights", ("t", "d"), "t"),
    "devoirs": ("duties", ("t", "d"), "t"),
    "mentions": ("legal", ("t", "p"), "t"),
    "confidentialite": ("privacy", ("t", "p"), "t"),
}
PARAGRAPH_FIELDS = {"p"}                          # champs « texte » d'un élément qui deviennent une liste de paragraphes


def _s(v) -> str:
    return v.strip() if isinstance(v, str) else ""


def _lang(v, lang: str) -> str:
    return _s(v.get(lang)) if isinstance(v, dict) else _s(v)


def _paras(text: str) -> list[str]:
    return [p.strip() for p in text.replace("\r", "").split("\n") if p.strip()]


def apply(T: dict, data) -> dict:
    """Copie de T où les textes renseignés dans `data` remplacent ceux d'origine."""
    out = copy.deepcopy(T)
    if not isinstance(data, dict):
        return out
    for key in SINGLE_KEYS:
        block = data.get(key)
        if not isinstance(block, dict):
            continue
        for name, value in block.items():
            for lang in ("fr", "ar"):
                if name not in out[lang]:
                    continue                     # on ne crée jamais de clé inconnue
                text = _lang(value, lang) if isinstance(value, dict) else (_s(value) if name.startswith("phone") else "")
                if not text:
                    continue
                if isinstance(out[lang][name], list):
                    paras = _paras(text)
                    if paras:
                        out[lang][name] = paras
                elif isinstance(out[lang][name], str):
                    out[lang][name] = text
    for key, (tkey, fields, required) in LISTS.items():
        rows = data.get(key)
        if not isinstance(rows, list) or tkey not in out["fr"]:
            continue
        for lang in ("fr", "ar"):
            old = out[lang][tkey]
            items = []
            for i, row in enumerate(r for r in rows if isinstance(r, dict)):
                if not _lang(row.get(required), lang):
                    continue
                item = {}
                for f in fields:
                    text = _lang(row.get(f), lang)
                    item[f] = _paras(text) if f in PARAGRAPH_FIELDS else text
                if tkey in ("rules", "rights", "duties"):     # l'icône reste celle de l'élément d'origine, par rang
                    item["i"] = old[len(items)]["i"] if len(items) < len(old) and "i" in old[len(items)] else "check"
                items.append(item)
            if items:
                out[lang][tkey] = items
    return out
