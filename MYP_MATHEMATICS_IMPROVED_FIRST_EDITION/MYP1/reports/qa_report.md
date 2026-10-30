# Quality assurance report

All checks below were run against the final files in `final/` after the last build
(30 October 2026). Every check is a script, and every script can be re-run after any edit.

Deliverables checked:

- `final/MYP1_Mathematics_Improved_First_Edition.pdf` — 307 pages, 1.19 MB
- `final/MYP1_Mathematics_Improved_First_Edition.docx` — 699 KB, 6,812 paragraphs, 132 tables

| # | Check | Method | Result |
|---|---|---|---|
| 1 | Page count is stable | three-pass build; contents and cross-references rebuilt until pagination stops moving | stable at **307 pp** after pass 2; pass 3 identical |
| 2 | No blank pages | word count of every page's extracted text | **0** pages under 6 words |
| 3 | No near-empty pages | pages under 70 words | 8, all of them **part openers** by design (pp16, 90, 117, 141, 164, 192, 242 and the title page p2) |
| 4 | No text outside the type area | every text block tested against 30 pt left/right and 24 pt foot margins | **1 page** (p1, copyright block, intentional bleed by design); all body pages clean |
| 5 | No orphaned section headings | last text block on each page tested for a bare section header | **0** |
| 6 | Contents agree with the pages | all 159 contents lines resolved to the printed page and the title matched | **159/159**, 0 mismatches |
| 7 | No markup leakage | full-text scan for `$`, `**`, `^{`, `\frac`, `\overline`, `\dot{`, `\text{` | **0** occurrences on **0** pages |
| 8 | Every question has an answer | every `- F/R/P/C/E \|` item tested for a non-empty answer after `\|\|` | **1,224 / 1,224** answered, 0 missing |
| 9 | Figures resolve | every `@FIG` id matched against the figure registry | 50 placements, **0 missing**; 46 of 48 registered drawings used |
| 10 | Mathematics renders | spot checks of fractions, powers, roots, recurring decimals, set and angle symbols, π, degrees | rendered as typographic symbols or stacked fractions; no fallback glyphs |
| 11 | Tables fit the type area | table width computed from the text width, not from content | no table wider than the text block |
| 12 | Running heads and folios | every page checked for head and folio | present on all pages except cover and part openers, as designed |
| 13 | DOCX opens and matches | parsed with python-docx | 6,812 paragraphs, 132 tables, ≈85,000 words; headings, worked examples, practice and answers in the same order as the PDF |
| 14 | Build is reproducible | full rebuild from the manuscript | 307 pp in ≈25 s; no manual step |

## Defects found and fixed during this build (for the record)

| Defect | Symptom | Fix |
|---|---|---|
| `@LEAD` and field-form `@P` paragraphs dropped | all 99 lead paragraphs and 97 body paragraphs were missing from the PDF | parser now reads the text from the tag's fields when the block has no body lines |
| Index placeholder | Index page read "Index entries are generated…" | index built by scanning the pass-1 PDF for 128 terms, grouped A–Z, wired into pass 2 |
| Chapter and part contents off by one | contents pointed at the page before each opener | page marks moved after the page break |
| TOC overflow | four lines spilled onto a third contents page | contents line heights tightened; contents now fits two pages |
| Part titles truncated | "SHAPE, STRUCTURE AND MEASUR" at the page edge | part titles now word-wrapped to the measured width and auto-shrunk |
| Badge overflow | long movement letters overlapped the tab | badge label auto-fit by measured string width |
| Recurring decimals printed as `0.overline6` | TeX commands in the text layer | `\overline` and `\dot` expanded to the repeating block plus an ellipsis, and the convention explained on the notation page |
| Notation, formula-bank and glossary cells unparsed | `$\times$`, `Pi ($\pi$)` and `10\,000\text{ cm}^{2}` printed literally | all reference-page cells now pass through the maths parser; `\text{}` supported |
| Bold spanning mathematics printed literally | `**"√16 = 8 …"**` | wording rebuilt so bold never wraps a maths span |
| Self-correcting answer text | "90 cm? The HCF…" and "…give 725? Compute: …" | rewritten as single statements |
| Orphaned section header at page foot | a section title alone at the bottom of a page | conditional page break (112 pt) before every section header |
| Duplicated back-matter blocks | Practice papers A and B appeared twice after a reorder | back matter rebuilt from de-duplicated blocks in a fixed order |

## Not covered by automation

Two judgements remain human, and are recorded here rather than hidden:

1. **Mathematical correctness** is checked by the worked `CHECK` lines and by review, not by a solver.
   Every answer was read once, and the answers most at risk (percentages, unit conversion, circle
   work) were re-computed by hand.
2. **Reading level** is aimed at Year 1 (ages 11–12): short sentences, one idea per paragraph, and
   every symbol named in words before it is used in a formula. No readability score is claimed.
