import re
"""Reusable page furniture: cards, section headers, practice sets, tables."""
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (Flowable, KeepTogether, Paragraph, Spacer,
                                Table, TableStyle)

from . import style as st
from .mathparse import rich


# --------------------------------------------------------------------- helpers
def P(text, style="body", **kw):
    return Paragraph(rich(text), st.STYLES[style], **kw)


def paras(text, style="body"):
    out = []
    for chunk in [c.strip() for c in text.split("\n\n") if c.strip()]:
        out.append(Paragraph(rich(" ".join(chunk.split("\n"))), st.STYLES[style]))
    return out


def space(h=6):
    return Spacer(1, h)


# --------------------------------------------------------------------- section header
class SectionHeader(Flowable):
    """Coloured band announcing a numbered section; notifies the table of contents."""

    def __init__(self, number, title, criterion="", accent=st.TEAL, tint=st.TEAL_T,
                 toc_level=1, width=st.TEXT_W):
        Flowable.__init__(self)
        parts = [p.strip() for p in str(criterion).split(";") if p.strip()]
        crit = " · ".join(re.sub(r"^criterion\s+", "", p, flags=re.I) for p in parts)
        self.number, self.title, self.criterion = number, title, crit
        self.accent, self.tint = accent, tint
        self.toc_level = toc_level
        self.width = width
        self.height = 40 if criterion else 32

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        import re as _re
        c = self.canv
        h = 34
        c.setFillColor(self.accent)
        c.roundRect(0, 0, self.width, h, 3, stroke=0, fill=1)
        c.setFillColor(colors.white)
        numeric = bool(_re.fullmatch(r"[\d.]+", self.number or ""))
        if numeric:
            c.setFont("Sans-Bold", 20)
            c.drawString(9, 9, self.number)
            num_w = c.stringWidth(self.number, "Sans-Bold", 20)
            title_x = 20 + num_w
        else:
            c.setFont("Sans-Bold", 7.6)
            c.drawString(9, 13, (self.number or "").upper())
            num_w = c.stringWidth((self.number or "").upper(), "Sans-Bold", 7.6)
            title_x = 16 + num_w
        c.setLineWidth(0)
        c.setStrokeColor(colors.white)
        c.setLineWidth(0.8)
        c.line(14 + num_w, 11, 14 + num_w, 24)
        # title (wrap if long)
        c.setFont("Sans-Bold", 13.2)
        avail = self.width - title_x - 8
        words = self.title.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "Sans-Bold", 13.2) <= avail:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
        y = 19 if len(lines) == 1 else 25
        for ln in lines[:2]:
            c.drawString(title_x, y, ln)
            y -= 14
        if self.criterion:
            c.setFont("Sans", 7.2)
            c.setFillColor(colors.white)
            c.drawRightString(self.width - 8, 10, self.criterion.upper())

    def drawOn(self, canvas, x, y, _sW=0):
        self.canv = canvas
        canvas.saveState()
        canvas.translate(x, y)
        self.draw()
        canvas.restoreState()

    def getSpaceBefore(self):
        return 14

    def getSpaceAfter(self):
        return 8

    def getKeepWithNext(self):
        return 1


class MiniHead(Flowable):
    """Small all-caps subheading with a rule, used inside review sections."""

    def __init__(self, text, accent=st.TEAL, width=st.TEXT_W):
        Flowable.__init__(self)
        self.text, self.accent, self.width = text, accent, width
        self.height = 16

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setFont("Sans-Bold", 8.2)
        c.setFillColor(self.accent)
        c.drawString(0, 4, self.text.upper())
        w = c.stringWidth(self.text.upper(), "Sans-Bold", 8.2)
        c.setStrokeColor(st.RULE_LIGHT)
        c.setLineWidth(0.6)
        c.line(w + 6, 6.2, self.width, 6.2)

    def drawOn(self, canvas, x, y, _sW=0):
        self.canv = canvas
        canvas.saveState()
        canvas.translate(x, y)
        self.draw()
        canvas.restoreState()

    def getSpaceBefore(self):
        return 9

    def getSpaceAfter(self):
        return 3


# --------------------------------------------------------------------- cards
KINDS = {
    "DEF": ("DEFINITION", st.NAVY, st.NAVY_T),
    "KEY": ("KEY IDEA", st.TEAL, st.TEAL_T),
    "ERR": ("COMMON ERROR", st.RED, st.RED_T),
    "ATL": ("APPROACHES TO LEARNING", st.INDIGO, st.INDIGO_T),
    "NOTE": ("NOTE", st.INK_SOFT, st.SLATE_T),
    "VOCAB": ("MATHEMATICAL LANGUAGE", st.AMBER, st.AMBER_T),
    "METHOD": ("METHOD", st.GREEN, st.GREEN_T),
    "INVEST": ("INVESTIGATION", st.GREEN, st.GREEN_T),
    "APPLY": ("APPLICATION", st.AMBER, st.AMBER_T),
    "CRIT": ("CRITERION TASK", st.PLUM, st.PLUM_T),
    "REFLECT": ("REFLECTION", st.INDIGO, st.INDIGO_T),
    "SUPPORT": ("SUPPORT", st.TEAL, st.TEAL_T),
}


def card(kind, title, body, width=st.TEXT_W, accent=None, tint=None,
         label=None, pad=8, extra_style=None):
    lab, ac, ti = KINDS.get(kind, ("", st.TEAL, st.TEAL_T))
    ac = accent or ac
    ti = tint or ti
    lab = label if label is not None else lab

    head_cells = []
    head = []
    if lab:
        head.append(Paragraph(
            '<font name="Sans-Bold" size="6.4" color="#FFFFFF">%s</font>' % lab,
            ParagraphStyle("l", fontName="Sans-Bold", fontSize=6.4, leading=8.4,
                           textColor=colors.white)))
    if title:
        head.append(Paragraph(
            '<font name="Sans-Bold" size="10.2" color="#FFFFFF">%s</font>'
            % rich(title), ParagraphStyle("t", fontName="Sans-Bold", fontSize=10.2,
                                          leading=12.6, textColor=colors.white,
                                          spaceBefore=0)))
    head_cells.append(head)

    t = Table([[head], [body]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), ac),
        ("BACKGROUND", (0, 1), (-1, 1), ti),
        ("LEFTPADDING", (0, 0), (-1, -1), pad),
        ("RIGHTPADDING", (0, 0), (-1, -1), pad),
        ("TOPPADDING", (0, 0), (-1, 0), 5),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
        ("TOPPADDING", (0, 1), (-1, 1), pad - 1),
        ("BOTTOMPADDING", (0, 1), (-1, 1), pad - 1),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBEFORE", (0, 0), (0, -1), 0, ac),
        ("ROUNDEDCORNERS", [3, 3, 3, 3]),
    ]))
    t.hAlign = "LEFT"
    return KeepTogether([t])


# --------------------------------------------------------------------- worked example
def worked_example(ref, title, given, asked, method, steps, answer, check=None,
                   watch=None, width=st.TEXT_W, accent=st.NAVY, tint=HexColor("#F2F6F8")):
    head = [[
        Paragraph('<font name="Sans-Bold" size="6.4" color="#FFFFFF">WORKED EXAMPLE %s</font>'
                  % ref, ParagraphStyle("a", fontName="Sans-Bold", fontSize=6.4,
                                        leading=8.6, textColor=colors.white)),
        Paragraph('<font name="Sans-Bold" size="9.6" color="#FFFFFF">%s</font>' % rich(title),
                  ParagraphStyle("b", fontName="Sans-Bold", fontSize=9.6, leading=12.2,
                                 textColor=colors.white)),
    ]]
    body = []
    lab = ParagraphStyle("lab", fontName="Sans-Bold", fontSize=7.4, leading=11.0,
                         textColor=accent, spaceBefore=1.2)
    val = ParagraphStyle("val", fontName=st.BODY_FONT, fontSize=9.1, leading=12.6,
                         textColor=st.INK, spaceBefore=1.2)
    rows = []
    if given:
        rows.append(("GIVEN", given))
    if asked:
        rows.append(("ASKED", asked))
    if method:
        rows.append(("METHOD", method))
    if rows:
        mt = Table([[Paragraph(l, lab), Paragraph(rich(t), val)] for l, t in rows],
                   colWidths=[46, width - 16 - 46])
        mt.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
        ]))
        body.append(mt)
    body.append(Spacer(1, 3))
    step_style = ParagraphStyle("st", fontName=st.BODY_FONT, fontSize=9.1, leading=12.7,
                                leftIndent=15, bulletIndent=0, spaceAfter=3.0,
                                textColor=st.INK)
    for i, s2 in enumerate(steps, 1):
        body.append(Paragraph(rich(s2), step_style, bulletText="%d." % i))
    if answer:
        body.append(Spacer(1, 2))
        body.append(Paragraph(
            '<font name="Sans-Bold" size="8.6" color="#0E6E76">ANSWER </font>'
            + rich(answer),
            ParagraphStyle("ans", fontName=st.BODY_FONT, fontSize=9.3, leading=13,
                           textColor=st.INK, spaceBefore=2)))
    if check:
        body.append(Paragraph(
            '<font name="Sans-Bold" size="8.2" color="#2F6B3E">CHECK </font>' + rich(check),
            ParagraphStyle("chk", fontName=st.BODY_FONT, fontSize=8.7, leading=12,
                           textColor=st.INK_SOFT, spaceBefore=3)))
    if watch:
        body.append(Paragraph(
            '<font name="Sans-Bold" size="8.2" color="#A03028">WATCH OUT </font>' + rich(watch),
            ParagraphStyle("wch", fontName=st.BODY_FONT, fontSize=8.7, leading=12,
                           textColor=st.INK_SOFT, spaceBefore=3)))

    t = Table([[head[0][0]], [head[0][1]], [body]], colWidths=[width])
    t.setStyle(TableStyle([
        ("SPAN", (0, 0), (0, 0)),
        ("BACKGROUND", (0, 0), (-1, 0), accent),
        ("BACKGROUND", (0, 1), (-1, 1), accent),
        ("BACKGROUND", (0, 2), (-1, 2), tint),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, 1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, 1), 2),
        ("TOPPADDING", (0, 2), (-1, 2), 7),
        ("BOTTOMPADDING", (0, 2), (-1, 2), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROUNDEDCORNERS", [3, 3, 3, 3]),
    ]))
    return KeepTogether([t])


# --------------------------------------------------------------------- practice
BADGE = {"F": ("FLUENCY", "#0E6E76"), "R": ("REASONING", "#4A3F87"),
         "P": ("PROBLEM SOLVING", "#B4701A"), "E": ("EXTENSION", "#7A2E52"),
         "C": ("COMMUNICATING", "#7A2E52")}


def practice_block(pid, title, levels, items, accent=st.TEAL, width=st.TEXT_W):
    """items: list of (type, question, answer)."""
    banner = bool((title or "").strip())
    head_left = Paragraph(
        '<font name="Sans-Bold" size="10.0" color="#FFFFFF">PRACTICE %s</font>'
        '<font name="Sans" size="10.0" color="#FFFFFF"> · %s</font>' % (pid, rich(title)),
        ParagraphStyle("ph", fontName="Sans-Bold", fontSize=10, leading=12.6,
                       textColor=colors.white))
    head_right = Paragraph(
        '<font name="Sans" size="6.8" color="#FFFFFF">%s</font>' % levels,
        ParagraphStyle("pl", fontName="Sans", fontSize=6.8, leading=9.2,
                       textColor=colors.white, alignment=2))
    rows = [[head_left, head_right]] if banner else []
    if not banner:
        style = [("BACKGROUND", (0, 0), (-1, -1), HexColor("#FBFCFC")),
                 ("LEFTPADDING", (0, 0), (-1, -1), 7),
                 ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                 ("TOPPADDING", (0, 0), (-1, -1), 3.4),
                 ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
                 ("VALIGN", (0, 0), (-1, -1), "TOP"),
                 ("LINEBELOW", (0, 0), (-1, -2), 0.25, st.RULE_LIGHT),
                 ("ROUNDEDCORNERS", [3, 3, 3, 3])]
    style = style if not banner else [
        ("SPAN", (0, 0), (1, 0)),
        ("BACKGROUND", (0, 0), (-1, 0), accent),
        ("BACKGROUND", (0, 0), (-1, 0), accent),
        ("BACKGROUND", (0, 1), (-1, -1), HexColor("#FBFCFC")),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, accent),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, 0), 4),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 4),
        ("TOPPADDING", (0, 1), (-1, -1), 3.4),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 3.4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.25, st.RULE_LIGHT),
        ("ROUNDEDCORNERS", [3, 3, 3, 3]),
    ]
    answers = []
    num = 0
    for it in items:
        typ = (it[0] or "").strip().upper()
        q = it[1]
        a = it[2] if len(it) > 2 else ""
        if it[0] == "NOTE":
            rows.append(["", Paragraph(rich(q), ParagraphStyle(
                "pn", fontName="Sans-Italic", fontSize=8.2, leading=11,
                textColor=st.INK_SOFT))])
            style.append(("SPAN", (0, len(rows) - 1), (1, len(rows) - 1)))
            continue
        num += 1
        badge = ""
        if typ in BADGE:
            nm, col = BADGE[typ]
            badge = ('<font name="Sans-Bold" size="5.9" color="%s">%s</font>' % (col, nm))
        qp = Paragraph(rich(q), st.STYLES["prac"])
        if badge:
            qp = Table([[qp, Paragraph(badge, ParagraphStyle(
                "bd", fontName="Sans-Bold", fontSize=5.9, leading=7.8,
                textColor=st.INK_SOFT, alignment=2))]],
                colWidths=[width - 40 - 62, 62],
                style=TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("VALIGN", (0, 0), (-1, -1), "TOP")]))
        rows.append([Paragraph('%d' % num, ParagraphStyle(
            "num", fontName="Sans-Bold", fontSize=8.2, leading=11.6,
            textColor=accent, alignment=2)), qp])
        answers.append((num, a))
    t = Table(rows, colWidths=[26, width - 26])
    style.append(("LEFTPADDING", (0, 0), (0, -1), 3))
    style.append(("RIGHTPADDING", (0, 0), (0, -1), 4))
    t.setStyle(TableStyle(style))
    return t, answers


# --------------------------------------------------------------------- data tables
def data_table(rows, col_widths=None, header=True, caption=None, accent=st.TEAL,
               tint=st.SLATE_T, font_size=8.3, width=st.TEXT_W, align="LEFT",
               highlight_rows=()):
    ncol = max(len(r) for r in rows)
    if col_widths is None:
        col_widths = [width / ncol] * ncol
    cell_style = ParagraphStyle("c", fontName=st.BODY_FONT, fontSize=font_size,
                                leading=font_size * 1.35, textColor=st.INK,
                                alignment=TA_LEFT)
    head_style = ParagraphStyle("h", fontName="Sans-Bold", fontSize=font_size - 0.3,
                                leading=(font_size - 0.3) * 1.35, textColor=colors.white)
    body = []
    for i, r in enumerate(rows):
        cells = []
        for c in r:
            cells.append(Paragraph(rich(str(c)), head_style if (header and i == 0) else cell_style))
        body.append(cells)
    t = Table(body, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.4, st.RULE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 2.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.8),
    ]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), accent),
                  ("ROUNDEDCORNERS", [2, 2, 2, 2])]
        style += [("BACKGROUND", (0, i), (-1, i), tint)
                  for i in range(1, len(rows)) if i % 2 == 0]
    for r in highlight_rows:
        style.append(("BACKGROUND", (0, r), (-1, r), HexColor("#FFF6E6")))
    t.setStyle(TableStyle(style))
    t.hAlign = "CENTER" if align == "CENTER" else "LEFT"
    if caption:
        return [t, P(caption, "caption")]
    return t


def figure(flowable, caption, source=None):
    out = [Spacer(1, 3), flowable]
    if caption:
        txt = caption
        if source:
            txt += ' <font name="Sans" size="6.4" color="#7C8B95">%s</font>' % source
        out.append(P(txt, "caption"))
    out.append(Spacer(1, 5))
    return out


def bullets(items, style="bullet", bullet="•"):
    return [Paragraph(rich(it), st.STYLES[style], bulletText=bullet) for it in items]


def numbered(items, style="num", start=1):
    return [Paragraph(rich(it), st.STYLES[style], bulletText="%d." % (i + start))
            for i, it in enumerate(items)]


def divider(width=st.TEXT_W, colour=None):
    t = Table([[""]], colWidths=[width], rowHeights=[1])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), 0.7, colour or st.RULE)]))
    return t


def callout_line(text, accent=st.TEAL, width=st.TEXT_W, bg=HexColor("#F2F6F8")):
    p = Paragraph(rich(text), ParagraphStyle("co", fontName=st.BODY_FONT, fontSize=9.0,
                                             leading=12.6, textColor=st.INK))
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.4, accent),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


class MovementHead(Flowable):
    """Banner for the pedagogical movements A–G inside a chapter."""

    def __init__(self, letter, title, subtitle="", accent=st.TEAL, tint=st.TEAL_T,
                 width=st.TEXT_W):
        Flowable.__init__(self)
        self.letter, self.title, self.subtitle = letter, title, subtitle
        self.accent, self.tint, self.width = accent, tint, width
        self.height = 30

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(self.tint)
        c.roundRect(0, 0, self.width, self.height - 2, 3, stroke=0, fill=1)
        c.setFillColor(self.accent)
        c.roundRect(0, 0, 26, self.height - 2, 3, stroke=0, fill=1)
        c.setFillColor(colors.white)
        size = 13.0
        lab = (self.letter or "").upper()
        while size > 5.6 and c.stringWidth(lab, "Sans-Bold", size) > 22:
            size -= 0.4
        c.setFont("Sans-Bold", size)
        c.drawCentredString(13, 8.5 + (size - 13) * 0.25, lab)
        c.setFillColor(self.accent)
        c.setFont("Sans-Bold", 9.6)
        c.drawString(36, 15.5, self.title.upper())
        if self.subtitle:
            c.setFont("Sans", 7.6)
            c.setFillColor(st.INK_SOFT)
            c.drawString(36, 6.5, self.subtitle)

    def drawOn(self, canvas, x, y, _sW=0):
        self.canv = canvas
        canvas.saveState()
        canvas.translate(x, y)
        self.draw()
        canvas.restoreState()

    def getSpaceBefore(self):
        return 10

    def getSpaceAfter(self):
        return 6
