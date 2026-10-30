# MYP Mathematics 1 — Improved First Edition

Student coursebook for MYP Year 1 mathematics, rebuilt from the first edition: **307 pages**, ten
chapters in five parts, 1,224 practice items, 165 worked examples, 48 original vector figures,
three practice papers, full answers, glossary and index.

**Author:** SADIKOU MOUKODDIM

## Deliverables

| File | What it is |
|---|---|
| `MYP1/final/MYP1_Mathematics_Improved_First_Edition.pdf` | print-ready interior, 307 pp, fonts embedded |
| `MYP1/final/MYP1_Mathematics_Improved_First_Edition.docx` | editable Word edition, ≈85,000 words, 132 tables |

## Layout of the repository

```
MYP1/
  manuscript/content/   the book itself: ch01.txt … ch10.txt, revision.txt (lightweight markup)
  manuscript/engine/    the build: build.py, chapterdata.py, frontmatter.py, make_docx.py,
                        bookkit/ (blocks, content parser, maths parser, figures, styles), fonts/
  final/                the two deliverables
  working/              build scratch: fig_*.pdf|png (figures), pass1.pdf, preview/*.png
  reports/              improvement report (12 points), QA report
  source_audit/         preservation report: every first-edition section mapped to this edition
  image_references/     figure inventory and the image-licensing position
```

## Build

Requires Python 3.11 with `reportlab`, `pymupdf`, `pypdf`, `python-docx`, `pillow`, `fontTools`.

```bash
cd MYP1/manuscript/engine
PYTHONPATH=. python run_build.py     # PDF, three passes (contents and index settle), ~25 s
PYTHONPATH=. python make_docx.py     # Word edition, ~10 s
```

The build is deterministic: page marks are written during pass 1, the index is built by scanning the
pass-1 PDF, and passes 2–3 repeat until pagination stops moving. `reports/qa_report.md` lists the
checks that were run and their results.

## Content markup (short version)

One line per element, pipe-separated fields:

```
@MOVE | letter | title | subtitle      @SEC | number | title | criteria
@LEAD | …        @P | …                @DEF | title      @KEY | title
@METHOD | title  @ERR | title          @TABLE | caption   (rows follow, ' ; ' between cells)
@FIG | figure_id @EX | number | title  @PRACTICE | id | title | tier line
- F | question || answer              F fluency · R reasoning · P problem solving · C communicating · E extension
```

## Fonts and licences

The build embeds **DejaVu Serif** and **DejaVu Sans** (DejaVu licence, `manuscript/engine/fonts/DEJAVU-LICENSE.txt`),
which permit redistribution and embedding. All figures are original vector drawings produced by the
build; no third-party images, artwork or text are used. See `MYP1/image_references/README.md`.
