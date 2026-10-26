"""Fichiers générés à la construction du site : QR codes (SVG et PNG) et plaquette de présentation (PDF)."""

import io
from pathlib import Path

import qrcode
import qrcode.image.svg
from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont, features

FONTS = Path(__file__).resolve().parent / "tools" / "fonts"
GREEN, GOLD, GREY = (10, 58, 39), (183, 138, 44), (86, 101, 93)


def qr_svg(url: str) -> bytes:
    """QR code vectoriel (idéal pour l'impression), niveau de correction élevé."""
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=10, border=2,
                       image_factory=qrcode.image.svg.SvgPathImage)
    qr.add_data(url)
    qr.make(fit=True)
    buf = io.BytesIO()
    qr.make_image(fill_color="#0a3a27").save(buf)
    return buf.getvalue()


def qr_png(url: str, box_size: int = 12) -> bytes:
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=box_size, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    buf = io.BytesIO()
    qr.make_image(fill_color=GREEN, back_color="white").save(buf, format="PNG")
    return buf.getvalue()


def _pdf() -> FPDF:
    pdf = FPDF(format="A4")
    pdf.add_font("dv", "", str(FONTS / "DejaVuSans.ttf"))
    pdf.add_font("dv", "B", str(FONTS / "DejaVuSans-Bold.ttf"))
    pdf.set_text_shaping(True)             # lettres arabes liées, sens de lecture droite-gauche
    pdf.set_auto_page_break(False)
    pdf.set_title("PSIE")
    pdf.set_creator("PSIE — site vitrine")
    pdf.add_page()
    return pdf


def brochure(t: dict, site_name: str, lang: str, url: str, logo: Path | None) -> bytes:
    """Plaquette d'une page, construite à partir des textes du site (aucune saisie à refaire)."""
    rtl = lang == "ar"
    align = "R" if rtl else "L"
    pdf = _pdf()
    left, width = 15, 180

    # Bandeau
    pdf.set_fill_color(*GREEN)
    pdf.rect(0, 0, 210, 40, style="F")
    text_x, text_w = (left, width - 28) if not rtl else (left, width - 28)
    if logo and logo.exists():
        pdf.image(str(logo), x=(left if not rtl else 210 - left - 24), y=8, w=24, h=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("dv", "B", 13)
    pdf.set_xy(left + (28 if not rtl else 0), 11)
    pdf.multi_cell(width - 28, 7, site_name, align=align, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("dv", "", 9)
    pdf.set_x(left + (28 if not rtl else 0))
    pdf.multi_cell(width - 28, 5, t["footer_tag"], align=align)

    # Titre et introduction
    pdf.set_text_color(*GREEN)
    pdf.set_xy(left, 50)
    pdf.set_font("dv", "B", 20)
    pdf.multi_cell(width, 10, f"{t['hero_title_a']} {t['hero_title_hl']}", align=align, new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("dv", "", 10.5)
    pdf.ln(2)
    pdf.multi_cell(width, 5.6, t["hero_intro"], align=align, new_x="LMARGIN", new_y="NEXT")

    # Chiffres clés
    y = pdf.get_y() + 6
    box_w, gap = 41.25, 5
    stats = t["stats"][:4]
    order = list(reversed(stats)) if rtl else stats
    for i, s in enumerate(order):
        x = left + i * (box_w + gap)
        pdf.set_fill_color(240, 244, 241)
        pdf.rect(x, y, box_w, 27, style="F")
        pdf.set_xy(x, y + 3)
        pdf.set_text_color(*GREEN)
        pdf.set_font("dv", "B", 20)
        pdf.cell(box_w, 10, str(s["value"]), align="C", new_x="LEFT", new_y="NEXT")
        pdf.set_x(x + 2)
        pdf.set_text_color(*GREY)
        pdf.set_font("dv", "", 7.2)
        pdf.multi_cell(box_w - 4, 3.6, s["label"], align="C")
    pdf.set_y(y + 33)

    # Objet et missions
    def heading(label: str) -> None:
        pdf.set_x(left)
        pdf.set_text_color(*GOLD)
        pdf.set_font("dv", "B", 11)
        pdf.cell(width, 7, label.upper() if not rtl else label, align=align, new_x="LMARGIN", new_y="NEXT")

    heading(t["object_title"])
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("dv", "", 9.5)
    pdf.multi_cell(width, 5, t["object"], align=align, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    heading(t["missions_title"])
    pdf.set_font("dv", "", 9.5)
    for m in t["missions"]:
        pdf.set_x(left)
        pdf.set_text_color(*GREEN)
        pdf.set_font("dv", "B", 9.5)
        pdf.multi_cell(width, 5, ("• " if not rtl else "") + m["t"] + ("" if not rtl else " •"), align=align, new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(60, 60, 60)
        pdf.set_font("dv", "", 8.8)
        pdf.set_x(left + (4 if not rtl else 0))
        pdf.multi_cell(width - 4, 4.4, m["d"], align=align, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    heading(t["founders_title"])
    pdf.set_text_color(*GREEN)
    pdf.set_font("dv", "B", 10)
    pdf.set_x(left)
    pdf.multi_cell(width, 6, "  ·  ".join(t["founders"]), align=align, new_x="LMARGIN", new_y="NEXT")

    # Pied : contact + QR code
    pdf.set_fill_color(*GREEN)
    pdf.rect(0, 258, 210, 39, style="F")
    qr_x = 210 - left - 28 if not rtl else left
    if url:
        pdf.image(io.BytesIO(qr_png(url, 8)), x=qr_x, y=261, w=28, h=28)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("dv", "", 9)
    tx = left if not rtl else left + (34 if url else 0)
    pdf.set_xy(tx, 263)
    pdf.multi_cell(width - (34 if url else 0), 5, t["address"], align=align, new_x="LEFT", new_y="NEXT")
    pdf.set_x(tx)
    phones = [f"\u2066{t['phone1']}\u2069", f"\u2066{t['phone2']}\u2069"]      # isolats : l'ordre des chiffres reste lisible en arabe
    pdf.cell(width - 34, 5, "   ".join(phones[::-1] if rtl else phones), align=align, new_x="LEFT", new_y="NEXT")
    pdf.set_x(tx)
    if url:
        pdf.set_font("dv", "B", 9.5)
        pdf.set_x(tx)
        pdf.cell(width - 34, 6, f"\u2066{url}\u2069", align=align)
    return bytes(pdf.output())


def og_card(title: str, site_name: str, lang: str, logo: Path | None) -> bytes | None:
    """Image 1200×630 affichée quand on partage une page (WhatsApp, Facebook…). None si l'arabe ne peut pas être mis en forme."""
    rtl = lang == "ar"
    if rtl and not features.check("raqm"):
        return None
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), GREEN)
    d = ImageDraw.Draw(img)
    for y in range(H):                      # léger dégradé vertical
        k = y / H
        d.line([(0, y), (W, y)], fill=tuple(int(c * (1 - 0.35 * k) + 8 * 0.35 * k) for c in GREEN))
    d.rectangle([0, H - 14, W, H], fill=(201, 162, 75))
    layout = ImageFont.Layout.RAQM if features.check("raqm") else ImageFont.Layout.BASIC
    big = ImageFont.truetype(str(FONTS / "DejaVuSans-Bold.ttf"), 64, layout_engine=layout)
    small = ImageFont.truetype(str(FONTS / "DejaVuSans.ttf"), 30, layout_engine=layout)
    margin, box = 80, 150
    x_logo = W - margin - box if rtl else margin
    if logo and logo.exists():
        try:
            lg = Image.open(logo).convert("RGBA")
            lg.thumbnail((box, box))
            d.rounded_rectangle([x_logo - 10, 70, x_logo + box + 10, 70 + box + 20], radius=24, fill=(255, 255, 255))
            img.paste(lg, (x_logo + (box - lg.width) // 2, 80 + (box - lg.height) // 2), lg)
        except OSError:
            pass
    anchor, x = ("ra", W - margin) if rtl else ("la", margin)
    kw = {"direction": "rtl", "language": "ar"} if rtl else {}
    max_w = W - 2 * margin
    lines, cur = [], ""
    for word in title.split():
        trial = f"{cur} {word}".strip()
        if cur and d.textlength(trial, font=big, **kw) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    lines.append(cur)
    y = 300
    for line in lines[:3]:
        d.text((x, y), line, font=big, fill=(255, 255, 255), anchor=anchor, **kw)
        y += 82
    d.text((x, H - 70), site_name, font=small, fill=(231, 207, 142), anchor="ls" if not rtl else "rs", **kw)
    out = io.BytesIO()
    img.save(out, "JPEG", quality=82, optimize=True)
    return out.getvalue()
