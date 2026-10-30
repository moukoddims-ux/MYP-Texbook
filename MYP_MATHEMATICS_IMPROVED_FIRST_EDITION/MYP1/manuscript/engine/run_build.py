"""Two-pass build driver for the improved first edition."""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build as B                      # noqa: E402
import chapterdata                     # noqa: E402
from bookkit import content as C       # noqa: E402
from bookkit import style as st        # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(os.path.dirname(ROOT), "final")
WORK = os.path.join(os.path.dirname(ROOT), "working")


def make_story(pages_map, index_registry, offset, pass_no):
    chapters = chapterdata.build_all(pages_map, index_registry)
    data = {"chapters": chapters}
    story = []
    story.append(B.NextPageTemplate("front"))
    from reportlab.platypus import PageBreak, NextPageTemplate, Spacer
    import frontmatter
    story.append(PageBreak())

    story.extend(frontmatter.title_page())
    story.append(PageBreak())
    story.extend(frontmatter.copyright_page())
    story.append(PageBreak())

    story.extend(frontmatter.contents_title())
    for lvl, title, key in chapterdata.toc_entries(chapters, pages_map):
        pg = pages_map.get(key, "—")
        story.append(B.TocLine(title, _display(pg, offset), lvl))
    story.append(PageBreak())

    for i, (name, builder) in enumerate(frontmatter.SECTIONS):
        story.append(NextPageTemplate("front_plain"))
        story.append(C.TocMark(pages_map, "front:" + name, name, 2))
        story.extend(builder())
        if i < len(frontmatter.SECTIONS) - 1:
            story.append(PageBreak())

    for part_idx, (numeral, pname, accent, tint) in enumerate(st.PART_COLOURS, 1):
        chs = [c for c in chapters if c["part"] == part_idx]
        if not chs:
            continue
        story.append(NextPageTemplate("part%d" % part_idx))
        story.append(PageBreak())
        story.append(C.TocMark(pages_map, "part:%d" % part_idx, "PART", 0))
        story.append(Spacer(1, 1))
        for ch in chs:
            story.append(NextPageTemplate("ch%d_open" % ch["n"]))
            story.append(PageBreak())
            story.append(C.TocMark(pages_map, "ch:%d" % ch["n"], ch["title"], 1))
            story.extend(B.chapter_opener_story(ch))
            story.append(NextPageTemplate("ch%d_body" % ch["n"]))
            story.append(PageBreak())
            story.extend(B.planner_story(ch, pages_map))
            story.append(PageBreak())
            story.extend(B.intentions_story(ch, pages_map, ch["_prereq_answers"]))
            story.append(PageBreak())
            story.extend(ch["_story"])

    story.append(NextPageTemplate("reference"))
    story.append(PageBreak())
    story.append(C.TocMark(pages_map, "ref:start", "", 0))
    story.append(C.TocMark(pages_map, "ref:Cumulative revision", "", 2))
    rev_story, rev_answers = chapterdata.revision_story(pages_map, index_registry)
    story.extend(rev_story)

    story.append(NextPageTemplate("answers"))
    story.append(PageBreak())
    story.append(C.TocMark(pages_map, "ref:Answers and worked solutions", "", 2))
    rev_ch = {"n": 0, "part": 1, "title": "Cumulative revision",
              "_answers": rev_answers, "_prereq_answers": []}
    story.extend(frontmatter.answers_section({"chapters": chapters}, chapters + [rev_ch]))

    story.append(NextPageTemplate("reference"))
    story.append(PageBreak())
    story.append(C.TocMark(pages_map, "ref:Formula bank", "", 2))
    story.extend(frontmatter.formula_bank())
    story.append(PageBreak())
    story.append(C.TocMark(pages_map, "ref:Glossary", "", 2))
    story.extend(frontmatter.glossary())
    story.append(PageBreak())
    story.append(C.TocMark(pages_map, "ref:Index", "", 2))
    story.extend(frontmatter.index_section(index_registry, offset or 0))
    story.append(PageBreak())
    story.append(C.TocMark(pages_map, "ref:References and acknowledgements", "", 2))
    story.extend(frontmatter.acknowledgements())
    story.append(NextPageTemplate("backcover"))
    story.append(PageBreak())
    story.append(Spacer(1, 1))
    return story


EXTRA_INDEX_TERMS = [
    "Expanded form", "Rounding", "Estimation", "Power", "Exponent", "Square root",
    "Order of operations", "Substitution", "Factor pair", "Prime factorisation",
    "Divisibility test", "HCF", "LCM", "Equivalent fraction", "Improper fraction",
    "Mixed number", "Recurring decimal", "Terminating decimal", "Percentage",
    "Percentage change", "Discount", "VAT", "Budget", "Like terms", "Expanding",
    "Solving an equation", "Inverse operation", "Angle on a straight line",
    "Vertically opposite", "Alternate angles", "Corresponding angles",
    "Co-interior angles", "Interior angle", "Exterior angle", "Construction",
    "Perpendicular bisector", "Universal set", "Complement", "Intersection", "Union",
    "Two-way table", "Composite shape", "Circumference", "Surface area", "Volume",
    "Capacity", "Cross-section", "Net", "Mean", "Median", "Mode", "Range", "Bar chart",
    "Pie chart", "Histogram", "Dot plot", "Outlier", "Misleading graph",
    "Frequency table", "Sector",
]


def build_index(registry, pdf_path, first_page, last_page):
    """Populate the index registry by scanning the pass-1 PDF."""
    import re
    import unicodedata

    import chapterdata
    try:
        import pymupdf as fitz
    except ImportError:                                    # pragma: no cover
        return
    try:
        doc = fitz.open(pdf_path)
    except Exception:                                      # pragma: no cover
        return

    terms = []
    seen = set()
    skip = {"index", "notation"}
    for t, _ in chapterdata.GLOSSARY:
        t = re.sub(r"\$[^$]*\$", "", t).strip()
        stem = t.lower().rstrip("s")
        if t and t.lower() not in seen and stem not in seen and t.lower() not in skip:
            seen.add(t.lower())
            seen.add(stem)
            terms.append(t)
    for t in EXTRA_INDEX_TERMS:
        stem = t.lower().rstrip("s")
        if t.lower() not in seen and stem not in seen:
            seen.add(t.lower())
            seen.add(stem)
            terms.append(t)

    def norm(t):
        t = unicodedata.normalize("NFKD", t)
        t = re.sub(r"[^A-Za-z0-9 ]", " ", t)
        return re.sub(r"\s+", " ", t).lower().strip()

    pages = {}
    for pno in range(first_page, min(last_page, doc.page_count) + 1):
        pages[pno] = " " + norm(doc[pno - 1].get_text()) + " "

    for term in terms:
        key = norm(term)
        if not key:
            continue
        needle = " " + key + " "
        hits = [p for p in sorted(pages) if needle in pages[p]]
        if not hits:
            continue
        if len(hits) > 4:
            hits = hits[:4]
        for p in hits:
            registry.add(term, p)
    doc.close()


def _display(pg, offset):
    if not isinstance(pg, int):
        return "—"
    if not offset:
        return "—"
    if pg < offset:
        return B.roman(pg)
    return str(pg - offset + 1)


def run():
    st.register_fonts()
    st.init_styles()
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(WORK, exist_ok=True)

    t0 = time.time()
    pages_map = {}
    index_registry = C.TermIndex()
    tmp = os.path.join(WORK, "pass1.pdf")
    import chaptermeta
    doc = B.Book(tmp, {"chapters": chaptermeta.CHAPTERS}, pages_map)
    doc.build(make_story(pages_map, index_registry, None, 1))
    offset = pages_map.get("ch:1")
    n1 = doc.page
    print("pass 1: %d pages, body starts at physical page %s (%.1fs)"
          % (n1, offset, time.time() - t0))

    pages_map2 = dict(pages_map)
    index_registry2 = C.TermIndex()
    final = os.path.join(OUT, "MYP1_Mathematics_Improved_First_Edition.pdf")
    index_end = pages_map.get("ref:Answers and worked solutions", n1) - 1
    build_index(index_registry2, tmp, offset, index_end)
    print("index: %d terms from pages %s–%s" % (len(index_registry2.entries()), offset, index_end))
    # Repeat passes until the pagination stops moving, so that the contents
    # page and every cross-reference agree with the final layout.
    prev_pages, prev_map = n1, dict(pages_map)
    for pass_no in range(2, 6):
        pages_in = dict(prev_map)
        doc2 = B.Book(final, {"chapters": chaptermeta.CHAPTERS}, pages_in,
                      offset=offset, index_pages=index_registry2)
        doc2.build(make_story(pages_in, index_registry2, offset, pass_no))
        print("pass %d: %d pages -> %s (%.1fs)"
              % (pass_no, doc2.page, final, time.time() - t0))
        stable = (doc2.page == prev_pages) and (pages_in == prev_map)
        prev_pages, prev_map = doc2.page, dict(pages_in)
        if stable:
            break
    else:
        print("WARNING: pagination did not settle after 5 passes")
    return final


if __name__ == "__main__":
    run()
