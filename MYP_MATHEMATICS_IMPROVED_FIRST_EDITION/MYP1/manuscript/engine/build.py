"""Build the MYP1 Mathematics Improved First Edition PDF.

Two passes: the first records the physical page of every heading for the table
of contents and index, the second renders with real page numbers.
"""
import os
import sys

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, FrameBreak,
                                KeepTogether, NextPageTemplate, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bookkit import blocks as B          # noqa: E402
from bookkit import content as C         # noqa: E402
from bookkit import style as st          # noqa: E402
from bookkit.mathparse import rich       # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

ROMAN = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi",
         "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx"]


def roman(n):
    if n < len(ROMAN):
        return ROMAN[n]
    vals = [(100, "c"), (90, "xc"), (50, "l"), (40, "xl"), (10, "x"),
            (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


# ------------------------------------------------------------------ furniture
def draw_cover(c):
    W, H = st.PAGE_W, st.PAGE_H
    c.saveState()
    c.setFillColor(st.NAVY)
    c.rect(0, 0, W, H, stroke=0, fill=1)

    # motif: concentric arcs, top right
    c.saveState()
    c.setStrokeColor(HexColor("#1C4A66"))
    c.setLineWidth(0.9)
    for i in range(11):
        c.circle(W - 12, H - 6, 46 + i * 30, stroke=1, fill=0)
    # faint coordinate lattice, lower middle
    c.setStrokeColor(HexColor("#173F57"))
    c.setLineWidth(0.5)
    for i in range(0, 13):
        c.line(26, 196 + i * 15, W - 26, 196 + i * 15)
    for i in range(0, 16):
        c.line(26 + i * 11, 196, 26 + i * 11, 376)
    c.setStrokeColor(HexColor("#21546F"))
    c.setLineWidth(0.35)
    for i in range(0, 8):
        c.line(26, 196 + i * 26, W - 26, 196 + i * 26)
    c.restoreState()

    # header labels
    c.setFillColor(HexColor("#86C0C6"))
    c.setFont("Sans-Bold", 8.0)
    c.drawString(30, H - 46, "MIDDLE YEARS PROGRAMME")
    c.drawString(30, H - 58, "YEAR 1  ·  MATHEMATICS")

    # title block
    c.setFillColor(colors.white)
    c.setFont("Sans-Bold", 13)
    c.drawString(30, H - 118, "MYP")
    c.setFont("Sans-Bold", 44)
    c.drawString(30, H - 164, "MATHEMATICS")
    c.setFont("Sans-Bold", 44)
    c.drawString(30, H - 210, "1")

    c.setFillColor(HexColor("#86C0C6"))
    c.setFont("Sans-Bold", 12.5)
    c.drawString(30, H - 252, "S T U D E N T   C O U R S E B O O K")

    c.setStrokeColor(HexColor("#0E6E76"))
    c.setLineWidth(4)
    c.line(30, H - 270, 132, H - 270)

    c.setFillColor(colors.white)
    c.setFont("Sans", 15)
    c.drawString(30, H - 296, "Improved First Edition")
    c.setFillColor(HexColor("#B9D2DA"))
    c.setFont("Sans", 9.6)
    c.drawString(30, H - 316, "A concept-driven, inquiry-led course in number, proportion,")
    c.drawString(30, H - 330, "algebra, shape, measurement, sets and data.")

    # movement chips
    chips = ["ENGAGE", "EXPLORE", "EXPLAIN", "PRACTISE", "APPLY", "REFLECT"]
    y = H - 372
    x = 30
    c.setFont("Sans-Bold", 7.2)
    for chx in chips:
        w = c.stringWidth(chx, "Sans-Bold", 7.2) + 14
        c.setFillColor(HexColor("#123F58"))
        c.roundRect(x, y - 4, w, 16, 3, stroke=0, fill=1)
        c.setFillColor(HexColor("#9CCFD3"))
        c.drawString(x + 7, y, chx)
        x += w + 6
    c.setFillColor(HexColor("#86C0C6"))
    c.setFont("Sans", 8.2)
    c.drawString(30, y - 22, "Ten chapters  ·  Five parts  ·  Full answers, investigations and criterion tasks")

    # author block
    c.setFillColor(colors.white)
    c.setFont("Sans-Bold", 12.5)
    c.drawString(30, 118, "SADIKOU MOUKODDIM")
    c.setFillColor(HexColor("#86C0C6"))
    c.setFont("Sans", 7.8)
    c.drawString(30, 104, "Head of Mathematics Department  ·  Mathematics Teacher  ·  Category 1")

    # topic strip
    c.setFillColor(HexColor("#0B2436"))
    c.rect(0, 0, W, 90, stroke=0, fill=1)
    c.setFillColor(HexColor("#8FB6C2"))
    c.setFont("Sans", 7.2)
    topics = ["Number systems and place value", "Powers and order of operations",
              "Factors, multiples and primes", "Fractions and decimals",
              "Percentages and applications", "Patterns, expressions and equations",
              "Lines, angles and constructions", "Sets and classification",
              "Perimeter, area and volume", "Data, tables and graphs"]
    colx = [26, W / 2 + 6]
    for i, t in enumerate(topics):
        col = 0 if i < 5 else 1
        row = i if i < 5 else i - 5
        c.drawString(colx[col], 72 - row * 12, "·  " + t)
    c.setFillColor(HexColor("#2C6C7A"))
    c.setFont("Sans", 6.4)
    c.drawString(26, 12, "All diagrams original to this edition")
    c.restoreState()


def draw_back_cover(c):
    W, H = st.PAGE_W, st.PAGE_H
    c.saveState()
    c.setFillColor(st.NAVY)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Sans-Bold", 20)
    c.drawString(30, H - 90, "MYP MATHEMATICS 1")
    c.setFillColor(HexColor("#8FC3C8"))
    c.setFont("Sans", 11.5)
    c.drawString(30, H - 112, "Improved First Edition  ·  Student Coursebook")
    c.setStrokeColor(HexColor("#0E6E76"))
    c.setLineWidth(3)
    c.line(30, H - 126, 110, H - 126)

    body = ("This improved first edition rebuilds the Year 1 course around a single "
            "rhythm: engage, explore, explain, practise, apply, reflect. Every chapter "
            "opens with a situation worth questioning, investigates it before naming the "
            "mathematics, and closes with a summary, a reflection and mixed revision.")
    _wrap_para(c, body, 30, H - 158, W - 60, font="Sans", size=10, leading=15,
               colour=HexColor("#DCE8EC"))

    feats = [
        ("Engage", "A real situation, puzzle or claim that creates a need for the mathematics"),
        ("Explore", "Structured investigations with recording tables and conjecture prompts"),
        ("Explain", "Definitions, visual models, notation and the reasoning behind each rule"),
        ("Worked examples", "Given, asked, method, steps, answer and a check"),
        ("Practice", "Fluency, reasoning, problem solving and extension, with full answers"),
        ("Apply", "Criterion B, C and D tasks with rubrics written for classroom use"),
        ("Reflect", "Vocabulary, key ideas, misconceptions, self-assessment and revision"),
    ]
    y = H - 250
    for name, desc in feats:
        c.setFillColor(HexColor("#0E6E76"))
        c.setFont("Sans-Bold", 9.5)
        c.drawString(30, y, name.upper())
        _wrap_para(c, desc, 128, y + 1, W - 158, font="Sans", size=9, leading=12.5,
                   colour=HexColor("#C9DCE3"))
        y -= max(26, 8 + 12.5 * (1 + len(desc) // 62))

    c.setFillColor(HexColor("#0B2436"))
    c.rect(0, 0, W, 108, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Sans-Bold", 11)
    c.drawString(30, 72, "SADIKOU MOUKODDIM")
    c.setFillColor(HexColor("#8FC3C8"))
    c.setFont("Sans", 8)
    c.drawString(30, 58, "Head of Mathematics Department  ·  Mathematics Teacher  ·  Category 1")
    _wrap_para(c, "An independent educational publication. Not published, sponsored or "
                  "endorsed by the International Baccalaureate Organization.",
               30, 30, W - 60, font="Sans", size=7, leading=9.5,
               colour=HexColor("#7FA0AE"))
    c.restoreState()


def _wrap_para(c, text, x, y, width, font="Sans", size=9, leading=12, colour=None):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    words = text.split()
    line = ""
    for w in words:
        trial = (line + " " + w).strip()
        if stringWidth(trial, font, size) <= width:
            line = trial
        else:
            c.setFont(font, size)
            if colour:
                c.setFillColor(colour)
            c.drawString(x, y, line)
            y -= leading
            line = w
    c.setFont(font, size)
    if colour:
        c.setFillColor(colour)
    c.drawString(x, y, line)
    return y - leading


def draw_chapter_open(c, doc, meta, accent, tint, part_label):
    W, H = st.PAGE_W, st.PAGE_H
    c.saveState()
    band_h = H * 0.46
    c.setFillColor(accent)
    c.rect(0, H - band_h, W, band_h, stroke=0, fill=1)
    # darker foot of the band
    c.setFillColor(HexColor("#000000"))
    c.setFillAlpha(0.10)
    c.rect(0, H - band_h, W, 4, stroke=0, fill=1)
    c.setFillAlpha(1)
    # chapter number badge
    bx, by, bs = W - 92, H - band_h + 26, 46
    c.setStrokeColor(HexColor("#FFFFFF"))
    c.setLineWidth(0.9)
    c.rect(bx, by, bs, bs, stroke=1, fill=0)
    c.setFillColor(HexColor("#FFFFFF"))
    c.setFont("Sans-Bold", 17)
    c.drawCentredString(bx + bs / 2, by + bs / 2 - 6, "%02d" % meta["n"])
    c.setFont("Sans", 5.6)
    c.drawCentredString(bx + bs / 2, by + 8, "CHAPTER")
    # page number
    draw_footer_number(c, doc, accent)
    c.restoreState()


def draw_part_open(c, doc, part_idx, accent, title, chapters, numeral):
    W, H = st.PAGE_W, st.PAGE_H
    c.saveState()
    c.setFillColor(accent)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    # decorative arcs
    c.setStrokeColor(HexColor("#FFFFFF"))
    c.setStrokeAlpha(0.13)
    c.setLineWidth(1.2)
    for i in range(7):
        c.circle(W - 40, 40, 90 + i * 46, stroke=1, fill=0)
    c.setStrokeAlpha(1)
    # numeral badge
    c.setFillColor(HexColor("#FFFFFF"))
    c.setFillAlpha(0.14)
    c.circle(W - 96, H - 96, 34, stroke=0, fill=1)
    c.setFillAlpha(1)
    c.setFillColor(HexColor("#FFFFFF"))
    c.setFont("Sans-Bold", 26)
    c.drawCentredString(W - 96, H - 106, numeral)
    c.setFillColor(HexColor("#FFFFFF"))
    c.setFont("Sans-Bold", 8.2)
    c.drawString(30, H - 62, "PART " + numeral)
    avail = W - 210
    size = 30.0
    while size > 18 and c.stringWidth(title, "Sans-Bold", size) > avail:
        size -= 1.0
    c.setFont("Sans-Bold", size)
    words, lines, cur = title.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if c.stringWidth(trial, "Sans-Bold", size) <= avail or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    y = H - 108
    for ln in lines:
        c.drawString(30, y, ln)
        y -= size * 1.16
    c.setStrokeColor(HexColor("#FFFFFF"))
    c.setLineWidth(1.4)
    c.line(30, y - 4, 130, y - 4)
    y -= 30
    c.setFont("Sans", 10.2)
    for n, t in chapters:
        c.setFillColor(HexColor("#FFFFFF"))
        c.setFillAlpha(0.75)
        c.setFont("Sans-Bold", 10.2)
        c.drawString(30, y, "%02d" % n)
        c.setFillAlpha(1)
        c.setFont("Sans", 10.2)
        c.drawString(58, y, t)
        y -= 20
    c.setFillColor(HexColor("#FFFFFF"))
    c.setFillAlpha(0.8)
    c.setFont("Sans", 8.2)
    c.drawString(30, 40, "MYP MATHEMATICS 1  ·  IMPROVED FIRST EDITION")
    c.restoreState()


def _split_lines(text, size, width=None, font="Sans-Bold"):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    width = width or (st.PAGE_W - 60)
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if stringWidth(trial, font, size) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_footer_number(c, doc, accent, white=False):
    num = printed_page(doc)
    if num is None:
        return
    W = st.PAGE_W
    c.saveState()
    c.setFillColor(HexColor("#FFFFFF") if white else accent)
    c.setFont("Sans-Bold", 8.4)
    c.drawRightString(W - st.MARGIN_R, 30, str(num))
    c.restoreState()


def printed_page(doc):
    p = doc.page
    offset = getattr(doc, "body_offset", None)
    if offset is None:
        return None
    if p < offset:
        return roman(p)
    return p - offset + 1


def on_body_page(canvas, doc, chapter_title, accent, part_name):
    W, H = st.PAGE_W, st.PAGE_H
    canvas.saveState()
    canvas.setStrokeColor(st.RULE_LIGHT)
    canvas.setLineWidth(0.7)
    canvas.line(st.MARGIN_L, H - st.MARGIN_T + 16, W - st.MARGIN_R, H - st.MARGIN_T + 16)
    canvas.setFont("Sans", 6.9)
    canvas.setFillColor(st.INK_SOFT)
    canvas.drawString(st.MARGIN_L, H - st.MARGIN_T + 22,
                      "MYP MATHEMATICS 1  ·  IMPROVED FIRST EDITION")
    canvas.drawRightString(W - st.MARGIN_R, H - st.MARGIN_T + 22, chapter_title.upper())
    canvas.line(st.MARGIN_L, st.MARGIN_B - 16, W - st.MARGIN_R, st.MARGIN_B - 16)
    canvas.setFont("Sans", 6.6)
    canvas.drawString(st.MARGIN_L, st.MARGIN_B - 26, part_name.upper())
    num = printed_page(doc)
    if num is not None:
        canvas.setFillColor(accent)
        canvas.setFont("Sans-Bold", 8.4)
        canvas.drawRightString(W - st.MARGIN_R, st.MARGIN_B - 26, str(num))
    canvas.restoreState()


def on_front_page(canvas, doc, section=""):
    W, H = st.PAGE_W, st.PAGE_H
    canvas.saveState()
    canvas.setStrokeColor(st.RULE_LIGHT)
    canvas.setLineWidth(0.7)
    canvas.line(st.MARGIN_L, H - st.MARGIN_T + 16, W - st.MARGIN_R, H - st.MARGIN_T + 16)
    canvas.setFont("Sans", 6.9)
    canvas.setFillColor(st.INK_SOFT)
    canvas.drawString(st.MARGIN_L, H - st.MARGIN_T + 22,
                      "MYP MATHEMATICS 1  ·  IMPROVED FIRST EDITION")
    canvas.drawRightString(W - st.MARGIN_R, H - st.MARGIN_T + 22, section.upper())
    canvas.setFont("Sans", 7.2)
    num = printed_page(doc)
    if num is not None:
        canvas.drawCentredString(W / 2, st.MARGIN_B - 26, str(num))
    canvas.restoreState()


def on_plain(canvas, doc):
    pass


# ------------------------------------------------------------------ TOC
class TocLine(Flowable):
    def __init__(self, text, page, level=1, accent=st.TEAL, width=st.TEXT_W):
        Flowable.__init__(self)
        self.text, self.page, self.level = text, page, level
        self.accent, self.width = accent, width
        self.height = 14.2 if level == 1 else (11.6 if level == 2 else 10.6)

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        from reportlab.pdfbase.pdfmetrics import stringWidth
        if self.level == 1:
            c.setFillColor(st.NAVY)
            c.setFont("Sans-Bold", 10.2)
            x = 0
        elif self.level == 2:
            c.setFillColor(st.INK)
            c.setFont("Sans", 8.7)
            x = 16
        else:
            c.setFillColor(st.INK_SOFT)
            c.setFont("Sans", 8.0)
            x = 30
        label = self.text
        c.drawString(x, 4, label)
        w = stringWidth(label, "Sans-Bold" if self.level == 1 else "Sans",
                        10.2 if self.level == 1 else (8.7 if self.level == 2 else 8.0))
        c.setFillColor(HexColor("#9AAAAF"))
        c.setFont("Sans", 7)
        dots_start = x + w + 4
        dots_end = self.width - 30
        if dots_end > dots_start:
            c.setDash(0.6, 3.0)
            c.setStrokeColor(HexColor("#B7C4CA"))
            c.setLineWidth(0.7)
            c.line(dots_start, 5, dots_end, 5)
            c.setDash()
        c.setFillColor(self.accent if self.level == 1 else st.INK_SOFT)
        c.setFont("Sans-Bold" if self.level == 1 else "Sans",
                  9.6 if self.level == 1 else 8.4)
        c.drawRightString(self.width, 4, str(self.page))


# ------------------------------------------------------------------ document
class Book(BaseDocTemplate):
    def __init__(self, filename, data, pages_map, offset=None, index_pages=None):
        BaseDocTemplate.__init__(
            self, filename, pagesize=(st.PAGE_W, st.PAGE_H),
            leftMargin=st.MARGIN_L, rightMargin=st.MARGIN_R,
            topMargin=st.MARGIN_T, bottomMargin=st.MARGIN_B,
            title="MYP Mathematics 1 — Student Coursebook (Improved First Edition)",
            author="SADIKOU Moukoddim",
            subject="MYP Year 1 mathematics coursebook, improved first edition",
            creator="Original ReportLab typesetting pipeline")
        self.data = data
        self.pages_map = pages_map
        self.body_offset = offset
        self.index_pages = index_pages or {}
        self._build_templates()

    def _build_templates(self):
        W, H = st.PAGE_W, st.PAGE_H
        fw = st.TEXT_W
        fh = H - st.MARGIN_T - st.MARGIN_B
        full = Frame(0, 0, W, H, 0, 0, 0, 0, id="full")
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[full], onPage=lambda c, d: draw_cover(c)),
            PageTemplate(id="backcover", frames=[full], onPage=lambda c, d: draw_back_cover(c)),
        ])
        fm_frame = Frame(st.MARGIN_L, st.MARGIN_B, fw, fh, id="front")
        self.addPageTemplates([
            PageTemplate(id="front", frames=[fm_frame],
                         onPage=lambda c, d: on_front_page(c, d, "Front matter")),
            PageTemplate(id="front_plain", frames=[fm_frame],
                         onPage=lambda c, d: on_plain(c, d)),
        ])
        # part openers (fully drawn)
        for i, (numeral, name, accent, tint) in enumerate(st.PART_COLOURS, 1):
            chapters = [(ch["n"], ch["title"]) for ch in self.data["chapters"]
                        if ch["part"] == i]
            t = PageTemplate(
                id="part%d" % i, frames=[full],
                onPage=lambda c, d, i=i, numeral=numeral, name=name, accent=accent,
                chapters=chapters: draw_part_open(c, d, i, accent, name, chapters, numeral))
            self.addPageTemplates([t])
        # chapters
        for ch in self.data["chapters"]:
            accent = st.chapter_colour(ch["part"])
            tint = st.chapter_tint(ch["part"])
            part_name = st.PART_COLOURS[ch["part"] - 1][1]
            band_h = H * 0.46
            band_frame = Frame(st.MARGIN_L, H - band_h + 8, fw,
                               band_h - st.MARGIN_T - 8, id="open%d" % ch["n"])
            open_frame = Frame(st.MARGIN_L, st.MARGIN_B, fw,
                               H - band_h - st.MARGIN_B - 6, id="opnb%d" % ch["n"])
            body_frame = Frame(st.MARGIN_L, st.MARGIN_B, fw, fh, id="body%d" % ch["n"])
            self.addPageTemplates([
                PageTemplate(id="ch%d_open" % ch["n"],
                             frames=[band_frame, open_frame],
                             onPage=lambda c, d, ch=ch, accent=accent, tint=tint,
                             part_name=part_name: draw_chapter_open(
                                 c, d, ch, accent, tint, part_name)),
                PageTemplate(id="ch%d_body" % ch["n"], frames=[body_frame],
                             onPage=lambda c, d, ch=ch, accent=accent,
                             part_name=part_name: on_body_page(
                                 c, d, ch["short"], accent, part_name)),
            ])
        # reference / answers
        ans_w = (fw - 14) / 2
        af = [Frame(st.MARGIN_L, st.MARGIN_B, ans_w, fh, id="a1"),
              Frame(st.MARGIN_L + ans_w + 14, st.MARGIN_B, ans_w, fh, id="a2")]
        self.addPageTemplates([
            PageTemplate(id="answers", frames=af,
                         onPage=lambda c, d: on_body_page(
                             c, d, "Answers and worked solutions", st.NAVY,
                             "Reference")),
            PageTemplate(id="reference", frames=[Frame(st.MARGIN_L, st.MARGIN_B, fw, fh,
                                                       id="ref")],
                         onPage=lambda c, d: on_body_page(
                             c, d, "Reference", st.NAVY, "Reference")),
        ])


# ------------------------------------------------------------------ story parts
def spacer(h=6):
    return Spacer(1, h)


def white_style(size=10, leading=14, bold=False, italic=False, colour="#FFFFFF",
                align=TA_LEFT):
    from bookkit.style import BODY_FONT
    name = "Sans-Bold" if bold else ("Sans-Italic" if italic else "Sans")
    return ParagraphStyle("w%s%s%s" % (size, bold, italic), fontName=name, fontSize=size,
                          leading=leading, textColor=HexColor(colour), alignment=align)


def chapter_opener_story(ch):
    accent = st.chapter_colour(ch["part"])
    for f in ():
        pass
    part = st.PART_COLOURS[ch["part"] - 1]
    s = []
    s.append(Spacer(1, 2))
    s.append(Paragraph("PART %s  ·  %s" % (part[0], part[1]),
                       white_style(7.4, 10, True, colour="#E4EFF1")))
    s.append(Spacer(1, 3))
    s.append(Paragraph("CHAPTER %02d" % ch["n"],
                       white_style(8.2, 11, True, colour="#E4EFF1")))
    s.append(Spacer(1, 2))
    s.append(Paragraph(ch["title"], white_style(24, 27, True)))
    s.append(Spacer(1, 7))
    s.append(Paragraph(ch["blurb"], white_style(9.8, 13.8, colour="#F0F6F7")))
    s.append(Spacer(1, 12))

    # concept lines
    rows = []
    for lab, val in ch["concepts"]:
        rows.append([Paragraph(lab.upper(),
                               ParagraphStyle("cl", fontName="Sans-Bold", fontSize=5.8,
                                              leading=8, textColor=HexColor("#CFE3E6"))),
                     Paragraph(val, ParagraphStyle("cv", fontName="Sans-Bold",
                                                   fontSize=7.6, leading=9.6,
                                                   textColor=colors.white))])
    t = Table(rows, colWidths=[82, 130])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.6),
    ]))
    s.append(t)

    # ---- white area
    s.append(FrameBreak())
    inq = Paragraph(
        '<font name="Sans-Bold" size="6.8" color="#0E6E76">INQUIRY QUESTION</font><br/>'
        '<font name="Sans" size="10.2" color="#17222B">%s</font>' % rich(ch["inquiry"]),
        ParagraphStyle("inq", fontName="Sans", fontSize=10.2, leading=14.6,
                       textColor=st.INK))
    box = Table([[inq]], colWidths=[st.TEXT_W])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), st.PAPER_TINT),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
    ]))
    s.append(box)
    s.append(Spacer(1, 10))
    s.append(Paragraph(rich(ch["opener_teaser"]),
                       ParagraphStyle("ot", fontName="Book", fontSize=9.2, leading=13.2,
                                      textColor=st.INK_SOFT, alignment=4)))
    s.append(Spacer(1, 10))

    # in this chapter
    s.append(B.MiniHead("In this chapter", accent))
    secs = ch.get("_sections", [])
    cols = []
    for num, title in secs:
        if not num:
            continue
        cols.append(Paragraph(
            '<font name="Sans-Bold" size="7.4" color="%s">%s</font> '
            '<font name="Sans" size="7.6" color="#2B3A44">%s</font>'
            % (accent.hexval().replace("0x", "#"), num, title),
            ParagraphStyle("sc", fontName="Sans", fontSize=7.6, leading=11.4,
                           textColor=st.INK, spaceAfter=2.5)))
    if cols:
        half = (len(cols) + 1) // 2
        left, right = cols[:half], cols[half:]
        data = []
        for i in range(half):
            data.append([left[i], right[i] if i < len(right) else ""])
        tt = Table(data, colWidths=[st.TEXT_W / 2, st.TEXT_W / 2])
        tt.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (0, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        s.append(tt)
    s.append(Spacer(1, 8))
    s.append(Paragraph(
        '<font name="Sans-Bold" size="7" color="#7C8B95">APPROXIMATELY %d HOURS</font>  '
        '<font name="Sans" size="7" color="#7C8B95">including investigation, application '
        'and review</font>' % ch["hours"],
        ParagraphStyle("hrs", fontName="Sans", fontSize=7, leading=10,
                       textColor=st.INK_SOFT)))
    return s


def planner_story(ch, registry):
    accent = st.chapter_colour(ch["part"])
    tint = st.chapter_tint(ch["part"])
    s = [Paragraph("UNIT PLANNER", ParagraphStyle(
        "pl", fontName="Sans-Bold", fontSize=7.6, leading=10, textColor=accent))]
    s.append(B.MiniHead("Framing the inquiry", accent))
    s.append(Paragraph(rich(ch["soi_intro"] or ""), st.STYLES["lead"]))

    # concepts column and context column
    left = []
    for lab, val, txt in ch["concept_blocks"]:
        left.append(Paragraph('<font name="Sans-Bold" size="6.4" color="#7C8B95">%s</font>'
                              % lab.upper(),
                              ParagraphStyle("cl", fontName="Sans-Bold", fontSize=6.4,
                                             leading=9, textColor=st.INK_SOFT)))
        left.append(Paragraph('<font name="Sans-Bold" size="9.2" color="#12344D">%s</font> '
                              '<font name="Sans" size="8.6" color="#17222B">%s</font>'
                              % (val + ".", rich(txt)),
                              ParagraphStyle("cv", fontName="Sans", fontSize=8.6,
                                             leading=12.2, textColor=st.INK,
                                             spaceAfter=5)))
    right = [Paragraph('<font name="Sans-Bold" size="6.4" color="#7C8B95">GLOBAL CONTEXT</font>',
                       ParagraphStyle("gl", fontName="Sans-Bold", fontSize=6.4,
                                      leading=9, textColor=st.INK_SOFT)),
             Paragraph('<font name="Sans-Bold" size="9.2" color="#12344D">%s</font>'
                       % ch["context"],
                       ParagraphStyle("gv", fontName="Sans-Bold", fontSize=9.2,
                                      leading=12.4, textColor=st.NAVY, spaceAfter=3)),
             Paragraph('<font name="Sans-Bold" size="6.6" color="#7C8B95">EXPLORATION</font>',
                       ParagraphStyle("ex", fontName="Sans-Bold", fontSize=6.6,
                                      leading=9, textColor=st.INK_SOFT)),
             Paragraph(rich(ch["context_exploration"]),
                       ParagraphStyle("gx", fontName="Sans", fontSize=8.6, leading=12.2,
                                      textColor=st.INK))]
    t = Table([[left, right]], colWidths=[st.TEXT_W * 0.52, st.TEXT_W * 0.48])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 12),
        ("LEFTPADDING", (1, 0), (1, 0), 12),
        ("RIGHTPADDING", (1, 0), (1, 0), 0),
        ("LINEBEFORE", (1, 0), (1, 0), 0.6, st.RULE_LIGHT),
    ]))
    s.append(spacer(4))
    s.append(t)
    s.append(spacer(8))

    # inquiry questions
    qs = [[Paragraph('<font name="Sans-Bold" size="6.4" color="#0E6E76">FACTUAL</font><br/>'
                     + rich(ch["factual"]),
                     ParagraphStyle("q", fontName="Sans", fontSize=8.5, leading=12,
                                    textColor=st.INK)),
           Paragraph('<font name="Sans-Bold" size="6.4" color="#B4701A">CONCEPTUAL</font><br/>'
                     + rich(ch["conceptual"]),
                     ParagraphStyle("q2", fontName="Sans", fontSize=8.5, leading=12,
                                    textColor=st.INK)),
           Paragraph('<font name="Sans-Bold" size="6.4" color="#7A2E52">DEBATABLE</font><br/>'
                     + rich(ch["debatable"]),
                     ParagraphStyle("q3", fontName="Sans", fontSize=8.5, leading=12,
                                    textColor=st.INK))]]
    qt = Table(qs, colWidths=[st.TEXT_W / 3] * 3)
    qt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#F6F8F9")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LINEAFTER", (0, 0), (1, 0), 0.6, st.RULE_LIGHT),
    ]))
    s.append(qt)
    s.append(spacer(9))

    # criteria table
    rows = [[Paragraph('<font name="Sans-Bold" size="7" color="#FFFFFF">CRITERION</font>',
                       ParagraphStyle("ch", fontName="Sans-Bold", fontSize=7,
                                      leading=9.4, textColor=colors.white)),
             Paragraph('<font name="Sans-Bold" size="7" color="#FFFFFF">STRANDS</font>',
                       ParagraphStyle("ch2", fontName="Sans-Bold", fontSize=7,
                                      leading=9.4, textColor=colors.white)),
             Paragraph('<font name="Sans-Bold" size="7" color="#FFFFFF">EVIDENCE IN THIS CHAPTER</font>',
                       ParagraphStyle("ch3", fontName="Sans-Bold", fontSize=7,
                                      leading=9.4, textColor=colors.white))]]
    for crit, strands, ev in ch["criteria"]:
        rows.append([Paragraph(crit, st.STYLES["cell"]),
                     Paragraph(strands, st.STYLES["cell"]),
                     Paragraph(rich(ev), st.STYLES["cell"])])
    ct = Table(rows, colWidths=[st.TEXT_W * 0.30, st.TEXT_W * 0.14, st.TEXT_W * 0.56])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), accent),
        ("BACKGROUND", (0, 1), (-1, -1), tint),
        ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#FFFFFF")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.8),
    ]))
    s.append(ct)
    s.append(spacer(8))

    atl = Paragraph(
        '<font name="Sans-Bold" size="6.4" color="#4A3F87">ATL SKILL · %s</font><br/>'
        % ch["atl_focus"].upper() + rich(ch["atl"]),
        ParagraphStyle("atl", fontName="Sans", fontSize=8.6, leading=12.4,
                       textColor=st.INK))
    ab = Table([[atl]], colWidths=[st.TEXT_W])
    ab.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), st.INDIGO_T),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, st.INDIGO),
    ]))
    s.append(ab)
    s.append(spacer(9))

    soi = Paragraph(
        '<font name="Sans-Bold" size="6.4" color="#FFFFFF">STATEMENT OF INQUIRY</font><br/>'
        '<font name="Sans-Bold" size="10" color="#FFFFFF">%s</font>' % rich(ch["soi"]),
        ParagraphStyle("soi", fontName="Sans", fontSize=10, leading=14,
                       textColor=colors.white))
    sb = Table([[soi]], colWidths=[st.TEXT_W])
    sb.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), st.NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
    ]))
    s.append(sb)
    return s


def intentions_story(ch, registry, answers_sink):
    accent = st.chapter_colour(ch["part"])
    tint = st.chapter_tint(ch["part"])
    s = [B.MiniHead("Learning intentions and success criteria", accent)]
    left = [Paragraph('<font name="Sans-Bold" size="6.4" color="#7C8B95">YOU ARE LEARNING TO</font>',
                      ParagraphStyle("li", fontName="Sans-Bold", fontSize=6.4, leading=9,
                                     textColor=st.INK_SOFT))]
    left += [Paragraph(rich(x), st.STYLES["bullet"], bulletText="•")
             for x in ch["intentions"]]
    right = [Paragraph('<font name="Sans-Bold" size="6.4" color="#7C8B95">SUCCESS CRITERIA</font>',
                       ParagraphStyle("sc", fontName="Sans-Bold", fontSize=6.4, leading=9,
                                      textColor=st.INK_SOFT))]
    right += [Paragraph(rich(x), st.STYLES["bullet"], bulletText="✓")
              for x in ch["success"]]
    t = Table([[left, right]], colWidths=[st.TEXT_W * 0.48, st.TEXT_W * 0.52])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 10),
        ("LEFTPADDING", (1, 0), (1, 0), 10),
        ("RIGHTPADDING", (1, 0), (1, 0), 0),
        ("LINEBEFORE", (1, 0), (1, 0), 0.6, st.RULE_LIGHT),
    ]))
    s.append(t)
    s.append(spacer(8))

    # prerequisite check
    items = ch["prereq"]
    rows = []
    for i, (q, a) in enumerate(items, 1):
        rows.append([Paragraph("<b>%d.</b>" % i, st.STYLES["prac"]),
                     Paragraph(rich(q), st.STYLES["prac"])])
    pt = Table(rows, colWidths=[16, st.TEXT_W - 16])
    pt.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    s.append(B.card("NOTE", "Prerequisite check · 10 minutes, no calculator",
                    [pt, Spacer(1, 3), Paragraph(rich(ch["prereq_note"]),
                                                 st.STYLES["small"])],
                    accent=st.INK_SOFT, tint=st.SLATE_T))
    answers_sink.append(("Prerequisite check", [(i, a) for i, (q, a) in enumerate(items, 1)]))

    # before / this chapter / later
    trio = [[Paragraph('<font name="Sans-Bold" size="6.4" color="#7C8B95">BEFORE YEAR 1</font><br/>'
                       + rich(ch["before"]),
                       ParagraphStyle("t1", fontName="Sans", fontSize=8.2, leading=11.6,
                                      textColor=st.INK)),
             Paragraph('<font name="Sans-Bold" size="6.4" color="#%s">YEAR 1 · THIS CHAPTER</font><br/>'
                       % accent.hexval()[2:] + rich(ch["this"]),
                       ParagraphStyle("t2", fontName="Sans", fontSize=8.2, leading=11.6,
                                      textColor=st.INK)),
             Paragraph('<font name="Sans-Bold" size="6.4" color="#7C8B95">LATER</font><br/>'
                       + rich(ch["later"]),
                       ParagraphStyle("t3", fontName="Sans", fontSize=8.2, leading=11.6,
                                      textColor=st.INK))]]
    tt = Table(trio, colWidths=[st.TEXT_W / 3] * 3)
    tt.setStyle(TableStyle([
        ("BACKGROUND", (1, 0), (1, 0), tint),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LINEAFTER", (0, 0), (1, 0), 0.6, st.RULE_LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.6, st.RULE_LIGHT),
    ]))
    s.append(spacer(7))
    s.append(tt)
    s.append(spacer(8))

    # inquiry pathway
    s.append(B.MiniHead("Inquiry pathway for this chapter", accent))
    cells = []
    for lab, txt in ch["pathway"]:
        cells.append(Paragraph(
            '<font name="Sans-Bold" size="6.2" color="#7C8B95">%s</font><br/>'
            '<font name="Sans" size="7.6" color="#17222B">%s</font>' % (lab.upper(), rich(txt)),
            ParagraphStyle("pw", fontName="Sans", fontSize=7.6, leading=10.4,
                           textColor=st.INK)))
    prow = Table([cells], colWidths=[st.TEXT_W / len(cells)] * len(cells))
    prow.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#F6F8F9")),
        ("LINEAFTER", (0, 0), (-2, -1), 0.6, HexColor("#FFFFFF")),
    ]))
    s.append(prow)
    return s


# ------------------------------------------------------------------ assembly
def gather_story(data, pages_map, offset, index_registry, pass_no):
    story = []
    chapters = data["chapters"]

    # ---------------- cover
    story.append(NextPageTemplate("front"))
    story.append(PageBreak())

    # ---------------- title page
    story.extend(frontmatter.title_page())
    story.append(PageBreak())
    story.extend(frontmatter.copyright_page())
    story.append(PageBreak())

    # ---------------- contents
    story.extend(frontmatter.contents_title())
    toc_entries = data["toc_entries"]
    for lvl, title, key in toc_entries:
        pg = pages_map.get(key, "—")
        story.append(TocLine(title, pg, lvl))
    story.append(PageBreak())

    # ---------------- orientation pages
    for key, builder in frontmatter.SECTIONS:
        story.append(NextPageTemplate("front_plain"))
        story.extend(builder())
        story.append(PageBreak())

    # ---------------- parts and chapters
    for part_idx, (numeral, pname, accent, tint) in enumerate(st.PART_COLOURS, 1):
        chs = [c for c in chapters if c["part"] == part_idx]
        if not chs:
            continue
        story.append(NextPageTemplate("part%d" % part_idx))
        story.append(PageBreak())
        story.append(Spacer(1, 1))
        for ch in chs:
            story.append(NextPageTemplate("ch%d_open" % ch["n"]))
            story.append(PageBreak())
            story.extend(chapter_opener_story(ch))
            story.append(NextPageTemplate("ch%d_body" % ch["n"]))
            story.append(PageBreak())
            story.extend(planner_story(ch, pages_map))
            story.append(PageBreak())
            story.extend(intentions_story(ch, pages_map, ch["_prereq_answers"]))
            story.append(PageBreak())
            story.extend(ch["_story"])

    # ---------------- answers
    story.append(NextPageTemplate("answers"))
    story.append(PageBreak())
    story.extend(frontmatter.answers_section(data, chapters))

    # ---------------- reference
    story.append(NextPageTemplate("reference"))
    story.append(PageBreak())
    story.extend(frontmatter.formula_bank())
    story.append(PageBreak())
    story.extend(frontmatter.glossary())
    story.append(PageBreak())
    story.extend(frontmatter.index_section(index_registry, offset))
    story.append(PageBreak())
    story.extend(frontmatter.acknowledgements())
    story.append(NextPageTemplate("backcover"))
    story.append(PageBreak())
    story.append(Spacer(1, 1))
    return story


def load_data():
    import chapterdata
    import frontmatter
    data = chapterdata.load()
    return data, frontmatter


if __name__ == "__main__":
    pass
