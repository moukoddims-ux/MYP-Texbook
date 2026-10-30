"""Typography, colour and paragraph styles for the MYP1 improved edition."""
import os

from reportlab.lib import colors  # noqa: F401  (re-exported)
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(os.path.dirname(HERE), "fonts")

# ---------------------------------------------------------------- page geometry
PAGE_W, PAGE_H = 210 * 2.834645669, 297 * 2.834645669  # A4 in points
MARGIN_L = 56.0
MARGIN_R = 50.0
MARGIN_T = 58.0
MARGIN_B = 56.0
TEXT_W = PAGE_W - MARGIN_L - MARGIN_R

# ---------------------------------------------------------------- palette
INK = HexColor("#17222B")
INK_SOFT = HexColor("#3E4C56")
RULE = HexColor("#C9D3DA")
RULE_LIGHT = HexColor("#E3EAEE")
PAPER_TINT = HexColor("#F6F8F9")

NAVY = HexColor("#12344D")
TEAL = HexColor("#0E6E76")
AMBER = HexColor("#B4701A")
INDIGO = HexColor("#4A3F87")
GREEN = HexColor("#2F6B3E")
PLUM = HexColor("#7A2E52")
RED = HexColor("#A03028")

TEAL_T = HexColor("#E7F1F1")
AMBER_T = HexColor("#FBF0DF")
INDIGO_T = HexColor("#ECEAF7")
GREEN_T = HexColor("#E9F2E9")
PLUM_T = HexColor("#F7E9EE")
RED_T = HexColor("#FAE9E6")
NAVY_T = HexColor("#E8EDF1")
SLATE_T = HexColor("#EDF1F4")

PART_COLOURS = [
    ("I", "THE GRAMMAR OF NUMBER", TEAL, TEAL_T),
    ("II", "PARTS AND PROPORTIONS", AMBER, AMBER_T),
    ("III", "PATTERNS AND SYMBOLS", INDIGO, INDIGO_T),
    ("IV", "SHAPE, STRUCTURE AND MEASURE", GREEN, GREEN_T),
    ("V", "DATA AND DECISIONS", PLUM, PLUM_T),
]

# ---------------------------------------------------------------- fonts
_FONT_FILES = {
    "Book": "DejaVuSerif.ttf",
    "Book-Bold": "DejaVuSerif-Bold.ttf",
    "Book-Italic": "DejaVuSerif-Italic.ttf",
    "Book-BoldItalic": "DejaVuSerif-BoldItalic.ttf",
    "Sans": "DejaVuSans.ttf",
    "Sans-Bold": "DejaVuSans-Bold.ttf",
    "Sans-Italic": "DejaVuSans-Oblique.ttf",
    "Sans-BoldItalic": "DejaVuSans-BoldOblique.ttf",
    "Mono": "DejaVuSansMono.ttf",
}

BODY_FONT = "Book"
HEAD_FONT = "Sans"


def register_fonts():
    for name, fname in _FONT_FILES.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fname)))
    pdfmetrics.registerFontFamily(
        "Book", normal="Book", bold="Book-Bold",
        italic="Book-Italic", boldItalic="Book-BoldItalic")
    pdfmetrics.registerFontFamily(
        "Sans", normal="Sans", bold="Sans-Bold",
        italic="Sans-Italic", boldItalic="Sans-BoldItalic")


# ---------------------------------------------------------------- styles
def S(name, **kw):
    base = dict(fontName=BODY_FONT, fontSize=9.9, leading=14.4,
                textColor=INK, alignment=TA_JUSTIFY, spaceBefore=0, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(name, **base)


STYLES = {}


def init_styles():
    st = STYLES
    st["body"] = S("body", spaceAfter=5.2)
    st["body_tight"] = S("body_tight", spaceAfter=1.5)
    st["body_first"] = S("body_first", spaceAfter=5.2)
    st["lead"] = S("lead", fontSize=10.9, leading=15.9, spaceAfter=6,
                   textColor=INK_SOFT)
    st["small"] = S("small", fontSize=8.2, leading=11.4)
    st["small_centre"] = S("small_centre", fontSize=8.2, leading=11.4,
                           alignment=TA_CENTER)
    st["caption"] = S("caption", fontName="Sans", fontSize=7.3, leading=10.0,
                      textColor=INK_SOFT, alignment=TA_LEFT, spaceBefore=3)
    st["defn"] = S("defn", fontSize=9.8, leading=14.0, spaceAfter=3.6)
    st["bullet"] = S("bullet", fontSize=9.8, leading=13.9, leftIndent=12,
                     bulletIndent=2, spaceAfter=2.4, alignment=TA_LEFT)
    st["num"] = S("num", fontSize=9.8, leading=13.9, leftIndent=16,
                  bulletIndent=0, spaceAfter=2.4, alignment=TA_LEFT)
    st["steps"] = S("steps", fontSize=9.8, leading=13.9, leftIndent=15,
                    bulletIndent=0, spaceAfter=2.6, alignment=TA_LEFT)
    st["h1"] = S("h1", fontName=HEAD_FONT + "-Bold", fontSize=19, leading=23,
                 textColor=NAVY, alignment=TA_LEFT, spaceBefore=6, spaceAfter=8)
    st["h2"] = S("h2", fontName=HEAD_FONT + "-Bold", fontSize=12.4, leading=15.6,
                 textColor=NAVY, alignment=TA_LEFT, spaceBefore=10, spaceAfter=4)
    st["h3"] = S("h3", fontName=HEAD_FONT + "-Bold", fontSize=9.8, leading=13,
                 textColor=TEAL, alignment=TA_LEFT, spaceBefore=7, spaceAfter=2.5)
    st["boxhead"] = S("boxhead", fontName=HEAD_FONT + "-Bold", fontSize=10.4,
                      leading=13, textColor=NAVY, alignment=TA_LEFT)
    st["boxhead_w"] = S("boxhead_w", fontName=HEAD_FONT + "-Bold", fontSize=10.4,
                        leading=13, textColor=colors.white, alignment=TA_LEFT)
    st["boxlabel"] = S("boxlabel", fontName=HEAD_FONT + "-Bold", fontSize=6.6,
                       leading=9, textColor=colors.white, alignment=TA_LEFT)
    st["eq"] = S("eq", fontSize=10.2, leading=16, alignment=TA_CENTER,
                 spaceBefore=4, spaceAfter=5)
    st["eq_left"] = S("eq_left", fontSize=9.8, leading=15, alignment=TA_LEFT,
                      leftIndent=10, spaceBefore=2, spaceAfter=3)
    st["prac"] = S("prac", fontSize=9.6, leading=13.6, spaceAfter=2.8,
                   alignment=TA_LEFT)
    st["prac_head"] = S("prac_head", fontName=HEAD_FONT + "-Bold", fontSize=10.6,
                        leading=13.4, textColor=colors.white, alignment=TA_LEFT)
    st["toc1"] = S("toc1", fontName=HEAD_FONT + "-Bold", fontSize=10.5,
                   leading=15, textColor=NAVY, alignment=TA_LEFT)
    st["toc2"] = S("toc2", fontName=HEAD_FONT, fontSize=8.6, leading=12.4,
                   textColor=INK, alignment=TA_LEFT)
    st["tocpart"] = S("tocpart", fontName=HEAD_FONT + "-Bold", fontSize=7.6,
                      leading=11, textColor=TEAL, alignment=TA_LEFT)
    st["table"] = S("table", fontSize=8.2, leading=10.8, alignment=TA_LEFT)
    st["table_h"] = S("table_h", fontName=HEAD_FONT + "-Bold", fontSize=7.8,
                      leading=10.4, textColor=colors.white, alignment=TA_LEFT)
    st["cell"] = S("cell", fontSize=8.7, leading=12.0, alignment=TA_LEFT)
    st["answer"] = S("answer", fontSize=8.3, leading=11.1, alignment=TA_LEFT,
                     spaceAfter=1.2)
    st["running"] = S("running", fontName=HEAD_FONT, fontSize=7.0, leading=9,
                      textColor=INK_SOFT, alignment=TA_LEFT)
    return st


def chapter_colour(part_index):
    return PART_COLOURS[part_index - 1][2]


def chapter_tint(part_index):
    return PART_COLOURS[part_index - 1][3]
