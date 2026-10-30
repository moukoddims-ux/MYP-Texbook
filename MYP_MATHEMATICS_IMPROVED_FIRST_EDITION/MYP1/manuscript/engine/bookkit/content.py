"""Parser for the manuscript format used in content/*.txt."""
import re

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (CondPageBreak, Flowable, KeepTogether, ListFlowable,
                                ListItem, PageBreak, Paragraph, Spacer, Table, TableStyle)

from . import blocks as B
from . import style as st
from .mathparse import rich


class IndexMark(Flowable):
    """Invisible marker that records the page on which a term occurs."""

    def __init__(self, registry, term):
        Flowable.__init__(self)
        self.registry = registry
        self.term = term
        self.width = 0
        self.height = 0

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        try:
            page = self.canv.getPageNumber()
        except Exception:
            page = 0
        self.registry.add(self.term, page)


class TitleHead(Flowable):
    """Front-matter page title."""

    def __init__(self, text, accent=st.TEAL, width=st.TEXT_W):
        Flowable.__init__(self)
        self.text, self.accent, self.width = text, accent, width
        self.height = 46

    def wrap(self, aw, ah):
        self.width = aw
        return aw, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(self.accent)
        c.rect(0, self.height - 5, 34, 3.2, stroke=0, fill=1)
        c.setFillColor(st.NAVY)
        c.setFont("Sans-Bold", 20)
        c.drawString(0, 12, self.text)

    def drawOn(self, canvas, x, y, _sW=0):
        self.canv = canvas
        canvas.saveState()
        canvas.translate(x, y)
        self.draw()
        canvas.restoreState()

    def getSpaceAfter(self):
        return 12


class TocMark(Flowable):
    """Records the page of a heading for the table of contents."""

    def __init__(self, registry, key, title, level):
        Flowable.__init__(self)
        self.registry, self.key, self.title, self.level = registry, key, title, level
        self.width = 0
        self.height = 0

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        self.registry[self.key] = self.canv.getPageNumber()


def _split_fields(line):
    body = line.split("|")
    return [x.strip() for x in body]


def _body_lines(lines):
    return [ln.rstrip() for ln in lines]


def _rich_paras(lines, style="body"):
    """Turn loose body lines into paragraphs, bullets, equations."""
    out = []
    para = []
    i = 0

    def flush():
        nonlocal para
        if para:
            out.append(Paragraph(rich(" ".join(para)), st.STYLES[style]))
            para = []

    for ln in lines:
        s = ln.strip()
        if not s:
            flush()
            continue
        if s.startswith("- "):
            flush()
            out.append(Paragraph(rich(s[2:]), st.STYLES["bullet"], bulletText="•"))
        elif s.startswith("* "):
            flush()
            out.append(Paragraph(rich(s[2:]), st.STYLES["bullet"], bulletText="▸"))
        elif re.match(r"^\d+\.\s", s):
            flush()
            num, rest = s.split(".", 1)
            out.append(Paragraph(rich(rest.strip()), st.STYLES["steps"],
                                 bulletText=num + "."))
        elif s.startswith("> "):
            flush()
            out.append(Paragraph(rich(s[2:]), st.STYLES["eq_left"]))
        elif s.startswith("= "):
            flush()
            out.append(Paragraph(rich(s[2:]), st.STYLES["eq"]))
        elif s.startswith("$") and s.endswith("$") and len(s) > 2:
            flush()
            out.append(Paragraph(rich(s), st.STYLES["eq"]))
        else:
            para.append(s)
    flush()
    return out


class ChapterSource:
    """A parsed chapter: front matter data plus story content."""

    def __init__(self, meta, path, figures=None, registry=None):
        self.meta = meta
        self.path = path
        self.figures = figures or {}
        self.answers = []          # [(practice id, [(n, answer)])]
        self.toc = []              # [(level, title, key)]
        self.story = []
        self.registry = registry if registry is not None else {}


def parse(path, meta, figures, toc_registry, index_registry, accent, tint,
          answers_out):
    """Parse a content file into flowables."""
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()

    lines = raw.split("\n")
    blocks = []            # (tag, fields, body-lines)
    cur = None
    for ln in lines:
        if ln.startswith("@") and re.match(r"^@[A-Z0-9_]+\b", ln):
            tag = ln.split()[0][1:]
            rest = ln[len(tag) + 1:].strip()
            if rest.startswith("|"):
                rest = rest[1:]
            fields = [f.strip() for f in rest.split("|")] if rest else []
            cur = (tag, fields, [])
            blocks.append(cur)
        elif cur is not None:
            cur[2].append(ln)
        # lines before the first marker are ignored (comments)

    story = []
    chap_answers = []
    sec_no = 0
    merged = []
    i = 0
    while i < len(blocks):
        tag, fields, body = blocks[i]
        if tag in ("METHOD", "KEY", "DEF", "ERR", "NOTE", "ATL", "INVEST") \
                and not "\n".join(body).strip() and i + 1 < len(blocks):
            ntag, nfields, nbody = blocks[i + 1]
            if ntag in ("LISTO", "LISTU") and "\n".join(nbody).strip():
                body = nbody
                i += 1
        merged.append((tag, fields, body))
        i += 1
    blocks = merged
    INLINE_TAGS = {"SEC", "MINI", "H2", "H3", "MOVE", "CALLOUT", "FIG", "DIV",
                   "SPACE", "PAGEBREAK", "IDX", "H1", "RAWSPACER"}

    for tag, fields, body in blocks:
        text = "\n".join(body)

        if tag == "SEC":
            num, title, crit = (fields + ["", "", ""])[:3]
            story.append(CondPageBreak(112))
            story.append(B.SectionHeader(num, title, crit, accent=accent, tint=tint))
            story.append(TocMark(toc_registry, "sec:%s:%s" % (meta.get("n"), num),
                               f"{num}  {title}", 2))
            sec_no += 1
        elif tag == "H1":
            story.append(TitleHead(fields[0] if fields else "", accent))
            if len(fields) > 1:
                story.append(TocMark(toc_registry, "h1:" + (fields[0] if fields else ""),
                                     fields[0] if fields else "", 1))
        elif tag == "MOVE":
            letter = fields[0] if fields else ""
            title = fields[1] if len(fields) > 1 else ""
            sub = fields[2] if len(fields) > 2 else ""
            story.append(B.MovementHead(letter, title, sub, accent=accent, tint=tint))
        elif tag == "H2":
            story.append(B.MiniHead(fields[0] if fields else "", accent))
        elif tag == "H3":
            story.append(Paragraph(
                rich(fields[0] if fields else ""),
                ParagraphStyle("h3x", fontName="Sans-Bold", fontSize=9.6, leading=13,
                               textColor=accent, spaceBefore=7, spaceAfter=2.5)))
        elif tag == "LEAD":
            lead_txt = "\n".join(body).strip() or (fields[0] if fields else "")
            story.extend(_rich_paras(lead_txt.split("\n"), "lead"))
        elif tag == "P":
            p_txt = "\n".join(body).strip()
            if not p_txt and fields:
                p_txt = " ".join(f for f in fields if f)
            story.extend(_rich_paras(p_txt.split("\n"), "body"))
        elif tag in ("DEF", "KEY", "ERR", "ATL", "NOTE", "VOCAB", "METHOD",
                     "INVEST", "APPLY", "CRIT", "REFLECT", "SUPPORT"):
            title = fields[0] if fields else ""
            bodyflow = _rich_paras(body, "defn")
            listy = any(re.match(r"^(\d+\.|-)\s", l.strip()) for l in body)
            if tag == "METHOD" and any(re.match(r"^\d+\.", l.strip()) for l in body):
                items = [re.sub(r"^\d+\.\s*", "", l.strip()) for l in body
                         if re.match(r"^\d+\.", l.strip())]
                ms = ParagraphStyle("meth", parent=st.STYLES["defn"], leftIndent=14,
                                    firstLineIndent=-14, spaceBefore=2.6,
                                    spaceAfter=0)
                bodyflow = [Paragraph(
                    '<font name="Sans-Bold" size="7.6" color="#0E6B72">%d.</font> %s'
                    % (k + 1, rich(i)), ms) for k, i in enumerate(items)]
            elif listy:
                ms = ParagraphStyle("lst", parent=st.STYLES["defn"], leftIndent=13,
                                    firstLineIndent=-13, spaceBefore=2.4,
                                    spaceAfter=0)
                rows2 = []
                num = 0
                for l in body:
                    q = l.strip()
                    if not q:
                        continue
                    if re.match(r"^\d+\.", q):
                        num += 1
                        mark = "%d." % num
                        q = re.sub(r"^\d+\.\s*", "", q)
                    else:
                        mark = "•"
                        q = re.sub(r"^-\s*", "", q)
                    rows2.append(Paragraph(
                        '<font name="Sans-Bold" size="8" color="#0E6B72">%s</font> %s'
                        % (mark, rich(q)), ms))
                bodyflow = rows2
            if not bodyflow:
                story.append(B.MiniHead(title or fields[0] if fields else "", accent))
                story.append(Spacer(1, 2))
                continue
            story.insert(len(story), Spacer(1, 4))
            story.append(B.card(tag, title, bodyflow, accent=accent if tag in
                                ("DEF", "KEY", "INVEST", "SUPPORT") else None,
                                tint=tint if tag in ("DEF", "KEY", "INVEST", "SUPPORT")
                                else None))
            story.append(Spacer(1, 6))
        elif tag == "EX":
            ref = fields[0] if fields else ""
            title = fields[1] if len(fields) > 1 else ""
            parsed = {"given": "", "asked": "", "method": "", "answer": "",
                      "check": "", "watch": ""}
            steps = []
            bucket = None
            buf = {}
            for ln in body:
                s = ln.strip()
                if not s:
                    continue
                m = re.match(r"^(GIVEN|ASKED|METHOD|ANSWER|CHECK|WATCH|STEPS?)\s*:\s*(.*)$", s)
                if m:
                    bucket = m.group(1).lower()
                    if bucket == "steps":
                        bucket = "step"
                    if bucket != "step":
                        buf[bucket] = m.group(2).strip()
                    continue
                if bucket == "step":
                    s2 = re.sub(r"^\d+\.\s*", "", s)
                    steps.append(s2)
                elif bucket:
                    buf[bucket] = (buf.get(bucket, "") + " " + s).strip()
            for k in parsed:
                parsed[k] = buf.get(k, "")
            story.append(B.worked_example(
                ref, title, parsed["given"], parsed["asked"], parsed["method"],
                steps, parsed["answer"], parsed["check"] or None,
                parsed["watch"] or None, accent=accent))
            story.append(Spacer(1, 8))
        elif tag == "PRACTICE":
            pid = fields[0] if fields else ""
            ptitle = fields[1] if len(fields) > 1 else ""
            levels = fields[2] if len(fields) > 2 else ""
            items = []
            for ln in body:
                s = ln.rstrip()
                if not s.strip():
                    continue
                if s.startswith("- "):
                    s = s[2:]
                    parts = s.split("||")
                    qpart = parts[0].strip()
                    ans = parts[1].strip() if len(parts) > 1 else ""
                    if "|" in qpart:
                        typ, q = qpart.split("|", 1)
                        typ, q = typ.strip(), q.strip()
                    else:
                        typ, q = "", qpart
                    items.append((typ, q, ans))
                elif s.startswith("+ ") and items:
                    typ, q, ans = items[-1]
                    extra = s[2:].strip()
                    if "||" in extra:
                        more_q, more_a = extra.split("||", 1)
                        items[-1] = (typ, q + " " + more_q.strip(),
                                     (ans + "; " + more_a.strip()).strip("; "))
                    else:
                        items[-1] = (typ, q + " " + extra, ans)
                elif s.startswith("!") and items:
                    items[-1] = ("NOTE", s[1:].strip(), "")
            tbl, ans = B.practice_block(pid, ptitle, levels, items, accent=accent)
            story.append(tbl)
            story.append(Spacer(1, 9))
            chap_answers.append((pid, ptitle, ans))
        elif tag == "TABLE":
            caption = fields[0] if fields else ""
            widths = None
            if len(fields) > 1 and fields[1]:
                try:
                    widths = [float(x) for x in fields[1].split(",")]
                    tot = sum(widths)
                    widths = [st.TEXT_W * w / tot for w in widths]
                except ValueError:
                    widths = None
            rows = []
            for ln in body:
                if ln.strip():
                    rows.append([c.strip() for c in ln.split(";")])
            out = B.data_table(rows, col_widths=widths, caption=caption or None,
                               accent=accent, tint=tint)
            if isinstance(out, list):
                story.extend(out)
            else:
                story.append(out)
            story.append(Spacer(1, 7))
        elif tag == "FIG":
            fid = fields[0] if fields else ""
            entry = figures.get(fid)
            if entry is None:
                story.append(Paragraph("[missing figure %s]" % fid, st.STYLES["body"]))
            else:
                draw_fn, caption, source = entry
                story.extend(B.figure(draw_fn(), caption, source))
        elif tag == "MINI":
            story.append(B.MiniHead(fields[0] if fields else "", accent))
        elif tag == "LISTU":
            story.extend(B.bullets([ln.strip()[2:] for ln in body if ln.strip().startswith("- ")]))
        elif tag == "LISTO":
            story.extend([Paragraph(rich(re.sub(r"^\d+\.\s*", "", ln.strip())),
                                    st.STYLES["num"], bulletText=ln.strip().split(".")[0] + ".")
                          for ln in body if ln.strip()])
        elif tag == "EQ":
            eqfields = [f for f in fields if f]
            for f in eqfields:
                story.append(Paragraph(rich(f), st.STYLES["eq"]))
            for ln in body:
                if ln.strip():
                    story.append(Paragraph(rich(ln.strip()), st.STYLES["eq"]))
        elif tag == "CALLOUT":
            story.append(B.callout_line(fields[0] if fields else "", accent))
            story.append(Spacer(1, 6))
        elif tag == "IDX":
            for term in fields:
                if term:
                    story.append(IndexMark(index_registry, term))
        elif tag == "DIV":
            story.append(Spacer(1, 4))
            story.append(B.divider(colour=HexColor("#C9D3DA")))
            story.append(Spacer(1, 6))
        elif tag == "SPACE":
            h = float(fields[0]) if fields else 6
            story.append(Spacer(1, h))
        elif tag == "PAGEBREAK":
            story.append(PageBreak())
        elif tag == "RAWSPACER":
            story.append(Spacer(1, 12))
        else:
            raise ValueError("Unknown tag %s in %s" % (tag, path))

        if tag in INLINE_TAGS and body and "\n".join(body).strip():
            story.extend(_rich_paras(body, "body"))

    answers_out.extend(chap_answers)
    return story, chap_answers


class TermIndex:
    def __init__(self):
        self.map = {}
        self.display = {}

    def add(self, term, page):
        key = term.strip().lower()
        self.map.setdefault(key, []).append(page)
        self.display.setdefault(key, term.strip())

    def entries(self):
        out = []
        for k in sorted(self.map):
            uniq = sorted({p for p in self.map[k] if p})
            if uniq:
                out.append((self.display.get(k, k), uniq))
        return out
