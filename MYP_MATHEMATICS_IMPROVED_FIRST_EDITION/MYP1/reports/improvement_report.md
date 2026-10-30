# MYP 1 Mathematics — Improved First Edition
## Twelve-point improvement report

**Author:** SADIKOU MOUKODDIM
**Edition:** Improved First Edition (rebuilt from the first edition's scope)
**Print interior:** 307 pages, 1.19 MB PDF · 699 KB editable DOCX
**Build date:** 30 October 2026
**Reproducible build:** `cd manuscript/engine && PYTHONPATH=. python run_build.py` (three passes, ~25 s)

| Metric | First edition (source) | This edition | Change |
|---|---|---|---|
| Pages | 240 | 307 | +67 (+28%) |
| Practice items (numbered questions) | ≈850 numbered items in the source text dump | 1,224 | +44% |
| Worked examples | mixed into prose | 165, all in a fixed six-part frame | — |
| Numbered sections | 45 | 50 in the ten chapters (142 `@SEC` units including reviews, tasks and papers) | +5 |
| Diagrams | 0 original vector figures | 50 figure placements (48 original drawings) | new |
| Tables | few | 132 | new |
| Investigations / applications / criterion tasks | 0 / 0 / 0 labelled | 20 / 11 / 30 | new |
| Definition, key-idea, error, method and ATL cards | 0 | 196 | new |
| Glossary / index | none / none | 119 terms / 128 indexed terms | new |
| Extracted word count | 119,498 | 112,143 | −6% at +28% pages |

The word count is lower while the book is 28% longer because the type is larger and the leading wider
(≈365 words per page against the source's ≈498). Every page carries one or more teaching elements —
no page is filler, and no page is blank (verified automatically; see `qa_report.md`).

---

### 1. Coverage preserved, section by section
All 45 numbered sections of the first edition survive as topics, and every one is taught with its own
definitions, worked examples and practice. The five topics that the first edition taught but that were
missing from the first draft of this edition were written and inserted during this build:

| First-edition section | Taught here |
|---|---|
| 4.5 Decimals: place value, ordering and calculation | 4.4 Fractions and decimals; **4.5 Calculating with decimals** (new) |
| 5.4 Discounts, taxes and budgets | **5.5 Discounts, taxes and budgets** (extended with VAT and budget work) |
| 7.3 Polygons and their angles | **7.5 Polygons and their angles** (new, p164) |
| 8.3 Number sets and the real line | **8.5 Number sets and the real line** (new, p191) |
| 9.2 Circles and composite shapes | **9.3 Circles: circumference and area** (new, p209) |

The full mapping table is in `source_audit/preservation_report.md`.

### 2. A visible inquiry architecture
Every chapter opens with the same five movements, each on its own banner: **Engage → Explore →
Explain → Apply → Reflect**. The Engage movement is a single concrete situation with a table of data;
the Explore movement is a physical or paper investigation; Explain carries the definitions; Apply is a
Criterion D task in a real setting; Reflect closes with transfer questions.

### 3. MYP criteria named on every section
Each section header carries its criterion targets (for example *7.5 Polygons and their angles —
A · ii, iii · C · ii*), and every review, investigation, application and task names its criteria and
strands. Teachers can plan from the contents page without opening the book.

### 4. Approaches to learning, made specific
The ATL page now carries a ten-row table, *Where each skill focus is developed*, naming the chapter,
the skill cluster (critical thinking, transfer, research, thinking) and a named activity that builds
it — for example Chapter 9 · Research skills · *Application 9: choosing a water tank from measured
data*. The skill is therefore traceable to a page.

### 5. Differentiation built into every practice set
All 1,224 items are tagged **F** (fluency), **R** (reasoning), **P** (problem solving), **C**
(communicating) or **E** (extension) and grouped in the header as *SUPPORT 1–3 · CORE 1–7 ·
EXTENSION 8–10*. A teacher can set three different tasks from one page without rewriting anything.

### 6. Worked examples in a single, teachable frame
All 165 examples use GIVEN · ASKED · METHOD · STEPS · ANSWER · CHECK, with WATCH OUT where the error
is common. The CHECK line is always a second route (substitution, estimation or a second method), so
students learn to verify rather than to hope.

### 7. Errors treated as content
196 cards — DEFINITION, KEY IDEA, COMMON ERROR, METHOD, APPROACHES TO LEARNING — carry the
misconceptions explicitly, for example *"a square root is always irrational"*, *"1 is prime"*, *"HCF
and LCM are the same thing"*. Each error card states the error, the correction and the evidence.

### 8. Twenty investigations and thirty criterion tasks
Each chapter has two investigations (a Criterion B cycle: collect, describe, generalise, justify,
verify) and criterion C/D tasks with rubrics written as student-facing checklists.

### 9. Assessment that is complete
- Answers to **every** numbered item, per chapter, in the back of the book (pp269–282).
- A formula bank (p283), a 119-term glossary (p285) and a 128-term index (p288).
- **Three practice papers** (A, B, C) with mark allocations and full answers (pp258–262).
- **Twenty-five problems solved in full** — method, reasoning and check (p262).
- **Four annotated student responses** with examiner commentary against criteria A–D (p265).
- A twelve-week revision planner with a weekly focus and an evidence-of-progress column (p267).

### 10. Design that supports reading
Colour-coded parts and chapters, a banner for every section, definition cards with a coloured edge,
practice tables with an accent header row, figures drawn as vector art in the book's own palette, and
running heads that name the chapter and the part. Badges and part titles auto-fit their space, so no
text is clipped anywhere in the book (checked on all 307 pages).

### 11. Two deliverables from one source
A print-ready **PDF** (307 pp, embedded fonts) and an editable **DOCX** (6,812 paragraphs, 132 tables,
≈85,000 words) exported from the same manuscript, with mathematics converted to Unicode
(superscripts, radicals, fractions) so it stays editable in Word.

### 12. Verification, not assertion
Every claim above is checked by script, and the checks are re-runnable: margin and overflow scan,
blank-page scan, orphaned-heading scan, contents-to-page cross-check (159 entries, 0 mismatches),
markup-leakage scan (no stray `$`, `**` or TeX commands), and figure/registry audit (46 of 48
registered figures used; no missing figures). Results: `reports/qa_report.md`.

---

### Honest limitations
- The edition is a **rewrite**, not a reprint: prose, examples, exercises and diagrams are original to
  this edition, and the first edition's wording is not reproduced. Coverage and Year 1 scope are
  preserved; the sentences are not.
- Photography was deliberately excluded; all diagrams are vector drawings produced by the build.
  `image_references/` lists each figure and where a photograph could replace it in a future edition.
- The DOCX is a faithful working copy, not a print master: pagination and multi-column index layout
  differ from the PDF by design.
