"""Front matter and reference sections."""
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, Spacer,
                                Table, TableStyle)

from bookkit import blocks as B
from bookkit import figures as F
from bookkit import style as st
from bookkit.mathparse import rich


def _h(text, size=20, colour=st.NAVY, before=0, after=8):
    return Paragraph(text, ParagraphStyle("h", fontName="Sans-Bold", fontSize=size,
                                          leading=size * 1.2, textColor=colour,
                                          spaceBefore=before, spaceAfter=after))


def _rule(width=st.TEXT_W, colour=None, thick=2.2):
    t = Table([[""]], colWidths=[width], rowHeights=[thick])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), thick, colour or st.TEAL)]))
    return t


def title_page():
    s = [Spacer(1, 54)]
    s.append(Paragraph("MIDDLE YEARS PROGRAMME · YEAR 1",
                       ParagraphStyle("a", fontName="Sans-Bold", fontSize=8.4, leading=11,
                                      textColor=st.TEAL)))
    s.append(Spacer(1, 4))
    s.append(Paragraph("MYP", ParagraphStyle("b", fontName="Sans-Bold", fontSize=13,
                                             leading=16, textColor=st.INK_SOFT)))
    s.append(Paragraph("MATHEMATICS 1", ParagraphStyle(
        "c", fontName="Sans-Bold", fontSize=40, leading=44, textColor=st.NAVY)))
    s.append(Spacer(1, 6))
    s.append(Paragraph("Student Coursebook", ParagraphStyle(
        "d", fontName="Sans", fontSize=16, leading=20, textColor=st.TEAL)))
    s.append(Spacer(1, 10))
    s.append(_rule(120, st.TEAL, 3))
    s.append(Spacer(1, 12))
    s.append(Paragraph("Improved First Edition", ParagraphStyle(
        "e", fontName="Sans-Bold", fontSize=12, leading=16, textColor=st.INK)))
    s.append(Spacer(1, 18))
    s.append(Paragraph(
        "An inquiry-led introduction to number, place value, proportion, algebra, "
        "geometry, measurement, sets and data, built around the concepts, contexts and "
        "assessment criteria of the Middle Years Programme.",
        ParagraphStyle("f", fontName="Book", fontSize=11, leading=16.5,
                       textColor=st.INK_SOFT, alignment=0)))
    s.append(Spacer(1, 200))
    s.append(Paragraph("SADIKOU MOUKODDIM", ParagraphStyle(
        "g", fontName="Sans-Bold", fontSize=14, leading=18, textColor=st.NAVY)))
    s.append(Spacer(1, 3))
    s.append(Paragraph("Head of Mathematics Department · Mathematics Teacher · Category 1",
                       ParagraphStyle("h", fontName="Sans", fontSize=8.6, leading=11.5,
                                      textColor=st.INK_SOFT)))
    return s


COPYRIGHT_BLOCKS = [
    ("Edition", "Improved first edition of *MYP Mathematics 1 — Student Coursebook*. "
                "This edition revises and expands the first edition. It is not a "
                "second edition and does not replace any other edition."),
    ("Copyright", "Copyright © SADIKOU Moukoddim. All rights reserved. No part of this "
                  "publication may be reproduced, stored in a retrieval system, or transmitted "
                  "in any form or by any means — electronic, mechanical, photocopying, "
                  "recording or otherwise — without prior written permission from the author, "
                  "except for brief quotations in reviews and for classroom use by the "
                  "purchasing teacher."),
    ("Author and publisher", "SADIKOU Moukoddim · Head of Mathematics Department · "
                             "Mathematics Teacher · Category 1."),
    ("Independence statement", "This is an independent educational publication. It is not "
                               "published, sponsored, endorsed by, or affiliated with the "
                               "International Baccalaureate Organization. “IB”, “IBO” and “MYP” "
                               "are trademarks of the International Baccalaureate Organization. "
                               "References to the MYP framework describe curriculum alignment and "
                               "planning only and do not imply endorsement. Teachers should "
                               "consult the current official MYP Mathematics subject guide and "
                               "their own programme documentation for authoritative requirements."),
    ("Originality", "All explanatory prose, examples, exercises, investigations, sample "
                    "responses, diagrams, page layouts and cover artwork in this book are "
                    "original to this edition and were written and drawn for it. Publicly "
                    "available curriculum descriptions were consulted only as reference points "
                    "for topic coverage and progression. No third-party textbook text, exercise, "
                    "illustration or layout is reproduced or adapted."),
    ("Scope and sequence", "The order of chapters is one defensible school sequence, not an "
                           "official required sequence. MYP schools design their own units "
                           "around conceptual understandings and local contexts. Teachers should "
                           "check the sequence against their programme documentation and their "
                           "students' prior learning."),
    ("Data and contexts", "Real-world scenarios use rounded, simplified or classroom-generated "
                          "data. Figures are chosen to support the mathematics and may not "
                          "reflect the most recent published statistics unless a source is "
                          "named. Students should verify current data from a reliable source when "
                          "a task requires it."),
    ("Assessment", "Criterion tasks, rubrics and level descriptors in this book are teaching "
                   "tools written for formative classroom use. They paraphrase and interpret the "
                   "MYP assessment criteria; they are not official IB descriptors and do not "
                   "replace the current subject guide."),
    ("Production", "Typeset in DejaVu Serif and DejaVu Sans under the SIL Open Font License. "
                   "Mathematical notation set inline with the text. All diagrams and cover "
                   "artwork created as original vector illustrations for this edition. Produced "
                   "with an original ReportLab paged-media pipeline."),
    ("Images", "This edition contains no third-party photographs. Every visual is an original "
               "diagram created for this book; the image reference list in the project reports "
               "records this and states the licence under which the diagrams may be reused."),
]

ICONS = [
    ("DEF", "Definition", "The precise meaning of a term, in the words the course uses."),
    ("KEY", "Key idea", "The principle behind a method, so that the method can be adapted."),
    ("ERR", "Common error", "A mistake worth anticipating, with the correction beside it."),
    ("ATL", "ATL skill", "An approaches-to-learning skill, and the activity that develops it."),
    ("NOTE", "Note", "A reminder, a convention or a useful piece of background information."),
    ("VOCAB", "Mathematical language", "Vocabulary to use, spell and explain accurately."),
    ("METHOD", "Method", "A reliable sequence of steps for a familiar type of question."),
    ("INVEST", "Investigation", "A structured exploration with a question to answer."),
    ("APPLY", "Application", "Mathematics used in a realistic setting with a decision to make."),
    ("CRIT", "Criterion task", "An assessed task naming the criterion strands it develops."),
]


def copyright_page():
    s = [_h("About this edition", 15)]
    s.append(_rule(90, st.TEAL, 2.4))
    s.append(Spacer(1, 8))
    rows = []
    for lab, txt in COPYRIGHT_BLOCKS:
        rows.append([Paragraph(lab, ParagraphStyle("l", fontName="Sans-Bold", fontSize=7.6,
                                                   leading=10.4, textColor=st.TEAL)),
                     Paragraph(txt, ParagraphStyle("t", fontName="Book", fontSize=7.9,
                                                   leading=10.9, textColor=st.INK))])
    t = Table(rows, colWidths=[88, st.TEXT_W - 88])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, st.RULE_LIGHT),
    ]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(Paragraph("No ISBN has been assigned to this independent edition. The book is "
                       "not an officially approved or endorsed IB textbook.",
                       ParagraphStyle("n", fontName="Sans", fontSize=7.4, leading=10,
                                      textColor=st.INK_SOFT)))
    return s


def contents_title():
    s = [_h("Contents", 22)]
    s.append(_rule(70, st.TEAL, 2.6))
    s.append(Spacer(1, 10))
    return s


# ------------------------------------------------------------------ orientation
def page_welcome():
    s = [_h("Welcome to Year 1 mathematics", 19)]
    s.append(_rule(80, st.TEAL, 2.6))
    s.append(Spacer(1, 8))
    body = [
        "This is a working book. Expect to write in the margins, test an idea, compare your "
        "method with a classmate's and return to a question after your thinking has changed.",
        "Year 1 is where many familiar ideas become precise. You already know how numbers are "
        "written, how shapes are named and how data can be displayed. This course asks you to "
        "look underneath those familiar forms: why a digit's position changes its value, why "
        "equivalent fractions name the same quantity, why an angle rule must hold for every "
        "triangle rather than merely for the one drawn on the page.",
        "The book is arranged in five parts. **Part I** builds the grammar of number: place "
        "value, powers, factors and the rules that keep calculation reliable. **Part II** treats "
        "fractions, decimals and percentages as three ways of describing the same quantity. "
        "**Part III** turns pattern into algebra, and algebra into a tool for finding what is "
        "unknown. **Part IV** brings sets, shape and measurement together, with constructions "
        "that make geometry reproducible. **Part V** examines data, graphs and the claims people "
        "make from them.",
        "Every chapter follows the same rhythm. A situation raises a question. An exploration "
        "gives you something to notice before anyone names the rule. The explanation then gives "
        "names, notation and reasons. Carefully written worked examples make the reasoning "
        "visible, practice makes the method dependable, and an investigation, an application and "
        "a criterion task ask you to use the mathematics beyond the original example.",
        "The answer section confirms your reasoning rather than replacing it. Attempt the "
        "question fully before you look: if your answer differs, find the first line where your "
        "reasoning diverges. That line is the most useful part of the page.",
    ]
    for i, p in enumerate(body):
        s.append(Paragraph(rich(p), ParagraphStyle("b", fontName="Book", fontSize=9.6,
                                                   leading=14.2, textColor=st.INK,
                                                   spaceAfter=7, alignment=4)))
    s.append(Spacer(1, 4))
    s.append(B.card("NOTE", "How the course is organised",
                    [Paragraph(rich("Each part opens with a page naming the chapters it "
                                    "contains. Each chapter opens with a full-page invitation "
                                    "and then a unit planner: the concepts, the global context, "
                                    "the statement of inquiry, the inquiry questions and the "
                                    "criteria the chapter develops. The teaching pages follow "
                                    "the engage–explore–explain–practice–apply–reflect rhythm "
                                    "described on the next pages."),
                                   st.STYLES["defn"])],
                    accent=st.TEAL, tint=st.TEAL_T))
    return s


def page_how_to_use():
    s = [_h("How to use this coursebook", 19)]
    s.append(_rule(80, st.TEAL, 2.6))
    s.append(Spacer(1, 8))
    s.append(Paragraph(rich(
        "Six movements are repeated in every chapter. Knowing what each movement is for helps "
        "you use the pages deliberately rather than reading them passively."),
        ParagraphStyle("b", fontName="Book", fontSize=9.6, leading=14.2, textColor=st.INK,
                       spaceAfter=8, alignment=4)))
    moves = [
        ("01", "Engage", "A situation, puzzle or claim you cannot yet explain. Your first job "
                          "is to ask questions, not to calculate."),
        ("02", "Explore", "A structured investigation with materials, a table or a diagram. "
                           "Record what you notice before anyone tells you the rule."),
        ("03", "Explain", "Definitions, vocabulary, notation and the reasons behind each rule. "
                           "This is where the mathematics gets its name."),
        ("04", "Worked examples", "Given, asked, method, steps, answer and check. Cover the "
                                   "answer, follow the method, then reproduce it unaided."),
        ("05", "Practice", "Fluency, reasoning, problem solving and extension, labelled so you "
                            "can choose an entry point and then move beyond it."),
        ("06", "Investigate, apply and reflect", "Investigations, real-life applications, "
                                                  "criterion tasks, a chapter review and mixed "
                                                  "practice that combines earlier chapters."),
    ]
    rows = []
    for num, name, txt in moves:
        rows.append([Paragraph(num, ParagraphStyle("n", fontName="Sans-Bold", fontSize=14,
                                                   leading=17, textColor=st.TEAL)),
                     Paragraph('<font name="Sans-Bold" size="9.4" color="#12344D">%s</font><br/>'
                               '<font name="Sans" size="8.8" color="#17222B">%s</font>'
                               % (name, txt),
                               ParagraphStyle("d", fontName="Sans", fontSize=8.8,
                                              leading=12.2, textColor=st.INK))])
    t = Table(rows, colWidths=[26, st.TEXT_W - 26])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, st.RULE_LIGHT),
    ]))
    s.append(t)
    s.append(Spacer(1, 9))
    s.append(B.MiniHead("Exercise types", st.TEAL))
    s.append(Paragraph(rich(
        "Practice questions carry a short label so that you can see what kind of thinking is "
        "being asked for. A question may belong to more than one type; the label names the "
        "dominant demand."), st.STYLES["small"]))
    s.append(Spacer(1, 4))
    rows = []
    for letter, name, col, txt in [
            ("F", "Fluency", "#0E6E76", "Short, deliberate practice that makes a method accurate and efficient."),
            ("R", "Reasoning", "#4A3F87", "Explain, compare, justify, find a counterexample or diagnose an error."),
            ("P", "Problem solving", "#B4701A", "Multi-step and unfamiliar contexts that require choosing a strategy."),
            ("E", "Extension", "#7A2E52", "Deeper structure, generalisation or a more open task within Year 1.")]:
        rows.append([Paragraph('<font name="Sans-Bold" size="8.4" color="%s">%s</font>'
                               % (col, letter),
                               ParagraphStyle("l", fontName="Sans-Bold", fontSize=8.4,
                                              leading=11, textColor=HexColor(col))),
                     Paragraph('<font name="Sans-Bold" size="8.2" color="#12344D">%s </font>'
                               '<font name="Sans" size="8.2" color="#17222B">%s</font>'
                               % (name, txt),
                               ParagraphStyle("e", fontName="Sans", fontSize=8.2,
                                              leading=11.4, textColor=st.INK))])
    t2 = Table(rows, colWidths=[22, st.TEXT_W - 22])
    t2.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    s.append(t2)
    s.append(Spacer(1, 8))
    s.append(B.card("ATL", "Using the answer key well",
                    [Paragraph(rich(
                        "Attempt the question fully before checking. If your answer differs, "
                        "locate the first line where your reasoning diverges, mark the correction "
                        "in a different colour and write one sentence explaining why the "
                        "alternative was wrong. That sentence is often worth more than the "
                        "correct number."), st.STYLES["defn"])],
                    accent=st.INDIGO, tint=st.INDIGO_T))
    return s


def page_icons():
    s = [_h("Visual guide to the book", 19)]
    s.append(_rule(80, st.TEAL, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "Every coloured panel has a job. The label at the top of the panel tells you what kind "
        "of information to expect, so that you can decide whether to read it carefully, copy it "
        "into your notes or use it as a checklist."),
        ParagraphStyle("b", fontName="Book", fontSize=9.4, leading=13.6, textColor=st.INK,
                       spaceAfter=8, alignment=4)))
    rows = []
    for kind, name, desc in ICONS:
        lab, ac, ti = B.KINDS[kind]
        rows.append([Table([[Paragraph('<font name="Sans-Bold" size="6.2" color="#FFFFFF">%s</font>'
                                       % lab, ParagraphStyle("k", fontName="Sans-Bold",
                                                             fontSize=6.2, leading=8,
                                                             textColor=colors.white))]],
                           colWidths=[74],
                           style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), ac),
                                             ("LEFTPADDING", (0, 0), (-1, -1), 5),
                                             ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                                             ("TOPPADDING", (0, 0), (-1, -1), 3),
                                             ("BOTTOMPADDING", (0, 0), (-1, -1), 3)])),
                     Paragraph('<font name="Sans-Bold" size="8.6" color="#12344D">%s</font><br/>'
                               '<font name="Sans" size="8.2" color="#17222B">%s</font>'
                               % (name, desc),
                               ParagraphStyle("i", fontName="Sans", fontSize=8.2,
                                              leading=11.4, textColor=st.INK))])
    t = Table(rows, colWidths=[80, st.TEXT_W - 80])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, st.RULE_LIGHT),
    ]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(B.card("KEY", "Three habits this book rewards",
                    [Paragraph(rich(
                        "**Estimate first.** Predict the size of an answer before calculating; "
                        "an estimate turns a wrong keypress into a visible mistake."), st.STYLES["defn"]),
                     Paragraph(rich(
                        "**Say the reason.** After each method, write one sentence that begins "
                        "“This works because…”. If you cannot finish the sentence, the method is "
                        "not yet yours."), st.STYLES["defn"]),
                     Paragraph(rich(
                        "**Compare representations.** Ask how the diagram, the table, the "
                        "fraction, the decimal and the formula describe the same quantity. "
                        "Moving between them is the core skill of Year 1."), st.STYLES["defn"])],
                    accent=st.TEAL, tint=st.TEAL_T))
    return s


def page_framework():
    s = [_h("The MYP framework in this course", 19)]
    s.append(_rule(80, st.TEAL, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "The Middle Years Programme asks students to learn mathematics as a connected, "
        "conceptual and applicable discipline. Concepts organise the content, contexts give it "
        "purpose, and criteria make the quality of thinking visible. In Year 1 the emphasis is on "
        "strong foundations: fluent number sense, careful use of notation, spatial reasoning, and "
        "the first deliberate steps from arithmetic towards algebra."),
        ParagraphStyle("b", fontName="Book", fontSize=9.5, leading=14.0, textColor=st.INK,
                       spaceAfter=8, alignment=4)))
    s.append(B.MiniHead("Key concepts used in this book", st.TEAL))
    kcs = [
        ("Form", "The shape, structure and organisation of mathematical objects: how a decimal "
                 "is arranged, how an angle is drawn, how an expression is built. Form helps us "
                 "notice what is the same beneath different appearances."),
        ("Logic", "The reasoning that connects claims to conclusions. Logic asks not only “Is it "
                  "true?” but “How do we know, and for which cases?”"),
        ("Relationships", "Connections between quantities, variables, representations and ideas. "
                          "A percentage, a formula, an angle pair and a graph are different ways "
                          "of expressing relationships."),
        ("Change", "How one quantity responds when another changes — growth, discount, "
                   "sequence, trend."),
    ]
    rows = []
    for name, txt in kcs:
        rows.append([Paragraph('<font name="Sans-Bold" size="9" color="#0E6E76">%s</font>' % name,
                               ParagraphStyle("k", fontName="Sans-Bold", fontSize=9,
                                              leading=12, textColor=st.TEAL)),
                     Paragraph(txt, st.STYLES["cell"])])
    t = Table(rows, colWidths=[74, st.TEXT_W - 74])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 3),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                           ("LINEBELOW", (0, 0), (-1, -2), 0.3, st.RULE_LIGHT)]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(B.MiniHead("Global contexts in this course", st.TEAL))
    ctx = [
        ("Identities and relationships", "How categories, groups and belonging can be described "
                                          "and questioned; how sets and classification represent "
                                          "inclusion and difference."),
        ("Orientation in space and time", "How number systems, calendars and measurement developed "
                                          "across cultures; how scale and position structure space."),
        ("Personal and cultural expression", "How proportion, pattern and geometry shape design, "
                                             "craft and architecture."),
        ("Scientific and technical innovation", "How measurement, formulas and data displays "
                                                "support invention, engineering and scientific claims."),
        ("Fairness and development", "How budgets, percentages, comparisons and data can support "
                                     "or distort fair decisions."),
        ("Globalization and sustainability", "How quantities are compared across communities and "
                                             "environments, and how claims about resources are communicated."),
    ]
    rows = []
    for name, txt in ctx:
        rows.append([Paragraph(name, ParagraphStyle("c", fontName="Sans-Bold", fontSize=7.9,
                                                    leading=10.6, textColor=st.NAVY)),
                     Paragraph(txt, st.STYLES["cell"])])
    t = Table(rows, colWidths=[112, st.TEXT_W - 112])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (0, -1), 6),
                           ("TOPPADDING", (0, 0), (-1, -1), 3),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                           ("LINEBELOW", (0, 0), (-1, -2), 0.3, st.RULE_LIGHT)]))
    s.append(t)
    s.append(Spacer(1, 8))
    s.append(B.MiniHead("The inquiry pathway", st.TEAL))
    steps = [("PROVOKE", "Notice a situation, pattern or claim that is not yet explainable."),
             ("QUESTION", "Turn the noticing into a mathematical question with quantities or objects."),
             ("REPRESENT", "Choose diagrams, tables, symbols or materials that reveal structure."),
             ("GENERALISE", "Move from examples to a rule, testing it against further cases."),
             ("APPLY", "Use the rule in a context and judge whether the answer makes sense."),
             ("REFLECT", "Evaluate the method, the evidence and the limits of the conclusion.")]
    cells = [Paragraph('<font name="Sans-Bold" size="6.2" color="#FFFFFF">%s</font><br/>'
                       '<font name="Sans" size="7.4" color="#FFFFFF">%s</font>' % (a, b),
                       ParagraphStyle("s", fontName="Sans", fontSize=7.4, leading=10,
                                      textColor=colors.white)) for a, b in steps]
    t = Table([cells], colWidths=[st.TEXT_W / 6] * 6)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), st.NAVY),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 5),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                           ("TOPPADDING", (0, 0), (-1, -1), 6),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                           ("LINEAFTER", (0, 0), (-2, -1), 0.5, HexColor("#2C5670"))]))
    s.append(t)
    return s


def page_criteria():
    s = [_h("Assessment criteria in practice", 19)]
    s.append(_rule(80, st.TEAL, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "MYP mathematics uses four criteria. They describe different qualities of mathematical "
        "work, not four separate syllabuses: a single rich task can provide evidence for more "
        "than one criterion. Most questions in this book are formative practice. A criterion task "
        "is different: it is planned to collect evidence, and it names its audience, product and "
        "expectations."),
        ParagraphStyle("b", fontName="Book", fontSize=9.4, leading=13.8, textColor=st.INK,
                       spaceAfter=8, alignment=4)))
    crit = [
        ("A", "Knowing and understanding", st.TEAL, st.TEAL_T,
         ["Select appropriate mathematics for familiar and unfamiliar problems.",
          "Apply the selected mathematics successfully.",
          "Solve problems correctly across a range of contexts."],
         "Definitions, place value, operations, fractions, percentages, angle rules, area and volume."),
        ("B", "Investigating patterns", st.AMBER, st.AMBER_T,
         ["Apply problem-solving techniques to recognise patterns.",
          "Describe patterns as relationships or general rules consistent with the findings.",
          "Verify whether a pattern works for other examples."],
         "Sequences, factor structures, constructed figures, set patterns and measurement relationships."),
        ("C", "Communicating", st.INDIGO, st.INDIGO_T,
         ["Use appropriate mathematical language, notation and symbols.",
          "Use different forms of representation and move between them.",
          "Present complete, coherent and concise lines of reasoning.",
          "Organise information using a logical structure."],
         "Explanations, diagrams, tables, graphs, units and justified working."),
        ("D", "Applying mathematics in real-life contexts", st.PLUM, st.PLUM_T,
         ["Identify the relevant elements of authentic situations.",
          "Select and apply mathematical strategies.",
          "Justify the degree of accuracy of a result.",
          "Interpret results in context and evaluate the solution."],
         "Budgets, packaging, timetables, surveys, design constraints and public claims."),
    ]
    for letter, name, ac, ti, strands, evidence in crit:
        head = Paragraph('<font name="Sans-Bold" size="8.4" color="#FFFFFF">CRITERION %s · %s</font>'
                         % (letter, name.upper()),
                         ParagraphStyle("ch", fontName="Sans-Bold", fontSize=8.4, leading=11,
                                        textColor=colors.white))
        left = [Paragraph("Students:", ParagraphStyle("l", fontName="Sans-Bold", fontSize=7.4,
                                                      leading=10, textColor=ac))]
        left += [Paragraph(x, ParagraphStyle("li", fontName="Book", fontSize=8.0, leading=11,
                                             leftIndent=9, bulletIndent=0, textColor=st.INK))
                 for x in strands]
        right = [Paragraph("In this course:", ParagraphStyle("r", fontName="Sans-Bold",
                                                             fontSize=7.4, leading=10,
                                                             textColor=ac)),
                 Paragraph(evidence, ParagraphStyle("rt", fontName="Book", fontSize=8.0,
                                                    leading=11, textColor=st.INK))]
        inner = Table([[left, right]], colWidths=[st.TEXT_W * 0.52 - 12, st.TEXT_W * 0.48 - 12])
        inner.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                   ("RIGHTPADDING", (0, 0), (0, 0), 8),
                                   ("TOPPADDING", (0, 0), (-1, -1), 0),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
        t = Table([[head], [inner]], colWidths=[st.TEXT_W])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), ac),
            ("BACKGROUND", (0, 1), (-1, 1), ti),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, 0), 3),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 3),
            ("TOPPADDING", (0, 1), (-1, 1), 5),
            ("BOTTOMPADDING", (0, 1), (-1, 1), 6),
        ]))
        s.append(t)
        s.append(Spacer(1, 5))
    s.append(Spacer(1, 4))
    s.append(B.card("NOTE", "Formative practice is not a formal assessment",
                    [Paragraph(rich(
                        "Practice questions are designed for learning, feedback and improvement, "
                        "and may be attempted more than once as understanding develops. The "
                        "criterion label at the head of a task states which criteria and strands "
                        "are targeted; it is not a formal IB grade, and the rubrics in this book "
                        "are classroom tools written for formative use."), st.STYLES["defn"])],
                    accent=st.INK_SOFT, tint=st.SLATE_T))
    return s


def page_course_map():
    s = [_h("Course map and progression", 19)]
    s.append(_rule(80, st.TEAL, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "The ten chapters form five parts. Each chapter names what it assumes, what it teaches "
        "and what it prepares. Reading the map before you begin helps you see that the course is "
        "a sequence of connected ideas rather than ten separate topics."),
        ParagraphStyle("b", fontName="Book", fontSize=9.4, leading=13.6, textColor=st.INK,
                       spaceAfter=8, alignment=4)))
    rows = [["Part", "Chapter", "Core content", "Builds towards"]]
    data = [
        ["I · The grammar of number",
         "1  Number systems and place value",
         "Number families, decimal place value, expanded form, ordering, rounding, estimation",
         "All later number work; measurement precision"],
        ["", "2  Powers and order of operations",
         "Index notation, powers of ten, squares and roots, order of operations, substitution",
         "Prime factorisation; algebra; standard form"],
        ["", "3  Factors, multiples and primes",
         "Factor pairs, divisibility, primes, prime factorisation, HCF and LCM",
         "Fraction simplification; scheduling problems"],
        ["II · Parts and proportions",
         "4  Fractions and decimals",
         "Equivalence, ordering, four operations, decimal place value, rounding, conversions",
         "Percentages; ratio; algebraic fractions"],
        ["", "5  Percentages and applications",
         "Percent of a quantity, increase and decrease, discounts, taxes, budgets",
         "Proportional reasoning; financial contexts"],
        ["III · Patterns and symbols",
         "6  Patterns, expressions and equations",
         "Sequences, general rules, substitution, like terms, expanding, one- and two-step equations",
         "Linear functions; formula rearrangement"],
        ["IV · Shape, structure and measure",
         "7  Lines, angles, triangles and constructions",
         "Angle facts, parallel lines, triangle and polygon angle sums, ruler-and-compass work",
         "Pythagoras; congruence; circle theorems"],
        ["", "8  Sets and classification",
         "Set notation, subsets, Venn diagrams, number sets, surveys and decisions",
         "Probability; logic; data handling"],
        ["", "9  Perimeter, area, surface area and volume",
         "Perimeter and area, circles, composite shapes, nets, volume and capacity",
         "Similarity; trigonometry; optimisation"],
        ["V · Data and decisions",
         "10  Data, tables and graphs",
         "Data types, frequency and two-way tables, charts, averages, trends, misleading graphs",
         "Statistics; statistical literacy"],
    ]
    rows.extend(data)
    t = Table(rows, colWidths=[86, 108, st.TEXT_W - 194 - 88, 88], repeatRows=1)
    style = [("BACKGROUND", (0, 0), (-1, 0), st.NAVY),
             ("GRID", (0, 0), (-1, -1), 0.35, st.RULE),
             ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 4),
             ("RIGHTPADDING", (0, 0), (-1, -1), 4),
             ("TOPPADDING", (0, 0), (-1, -1), 2.6),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    for i in range(1, len(rows)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), HexColor("#F4F7F8")))
    t.setStyle(TableStyle(style))
    body = []
    for i, r in enumerate(rows):
        cells = []
        for j, c in enumerate(r):
            if i == 0:
                cells.append(Paragraph('<font name="Sans-Bold" size="6.6" color="#FFFFFF">%s</font>'
                                       % c, ParagraphStyle("hh", fontName="Sans-Bold",
                                                           fontSize=6.6, leading=9,
                                                           textColor=colors.white)))
            elif j == 0:
                cells.append(Paragraph('<font name="Sans-Bold" size="6.8" color="#0E6E76">%s</font>'
                                       % c.replace("·", "·<br/>"),
                                       ParagraphStyle("p", fontName="Sans-Bold", fontSize=6.8,
                                                      leading=9.4, textColor=st.TEAL)))
            elif j == 1:
                cells.append(Paragraph('<font name="Sans-Bold" size="7.4" color="#12344D">%s</font>'
                                       % c, ParagraphStyle("cc", fontName="Sans-Bold",
                                                           fontSize=7.4, leading=10,
                                                           textColor=st.NAVY)))
            else:
                cells.append(Paragraph(c, ParagraphStyle("dd", fontName="Sans", fontSize=7.0,
                                                         leading=9.6, textColor=st.INK)))
        body.append(cells)
    t = Table(body, colWidths=[86, 108, st.TEXT_W - 194 - 88, 88], repeatRows=1)
    t.setStyle(TableStyle(style))
    s.append(t)
    return s


def page_notation():
    s = [_h("Notation, working and habits", 19)]
    s.append(_rule(80, st.TEAL, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "Mathematical notation is a shared agreement. Using it precisely makes your reasoning "
        "checkable by someone else, including your teacher and your future self. The table records "
        "the conventions used throughout this book."),
        ParagraphStyle("b", fontName="Book", fontSize=9.4, leading=13.6, textColor=st.INK,
                       spaceAfter=8, alignment=4)))
    rows = [["Symbol or convention", "Meaning", "Example"],
            ["$\\times$, $\\cdot$", "multiplication", "$7 \\times 4 = 28$"],
            ["$\\div$ or fraction bar", "division", "$12 \\div 3 = \\frac{12}{3} = 4$"],
            ["$=$", "is equal to; both sides have the same value", "$3 + 4 = 7$"],
            ["$\\approx$", "is approximately equal to", "$\\pi \\approx 3.14$"],
            ["$<$, $>$", "is less than; is greater than", "$-3 < 2$, $5 > -1$"],
            ["$\\le$, $\\ge$", "is less than or equal to; is greater than or equal to", "$x \\le 5$"],
            ["$\\ne$", "is not equal to", "$0.5 \\ne 0.05$"],
            ["$x^{2}$, $x^{3}$", "power: repeated multiplication", "$5^{2} = 25$"],
            ["$\\sqrt{49}$", "square root", "$\\sqrt{49} = 7$"],
            ["$\\%$", "per cent, out of 100", "$25\\% = 0.25 = \\frac{1}{4}$"],
            ["$\\angle ABC$", "the angle at vertex $B$", "$\\angle ABC = 90\\degree$"],
            ["$\\triangle ABC$", "the triangle with vertices $A$, $B$, $C$", ""],
            ["$\\parallel$, $\\perp$", "is parallel to; is perpendicular to", "$AB \\parallel CD$"],
            ["$\\in$, $\\notin$", "is an element of; is not an element of", "$3 \\in \\mathbb{N}$"],
            ["$A \\cup B$, $A \\cap B$", "union; intersection", "$\\{1,2\\} \\cup \\{2,3\\} = \\{1,2,3\\}$"],
            ["$\\pi$", "the ratio of circumference to diameter", "$\\pi \\approx 3.14159$"],
            ["$0.363636\\dots$", "a recurring decimal: the block 36 repeats for ever", "$\\frac{4}{11}$"],
            ["cm, m, km, cm², m³, L", "units of length, area, volume and capacity", "1 m² = 10,000 cm²"],
            ]
    body = []
    for i, r in enumerate(rows):
        cells = []
        for j, c in enumerate(r):
            if i == 0:
                cells.append(Paragraph('<font name="Sans-Bold" size="6.8" color="#FFFFFF">%s</font>'
                                       % c, ParagraphStyle("hh", fontName="Sans-Bold",
                                                           fontSize=6.8, leading=9,
                                                           textColor=colors.white)))
            else:
                cells.append(Paragraph(rich(c),
                                       ParagraphStyle("nn", fontName="Book", fontSize=7.8,
                                                      leading=10.6, textColor=st.INK)))
        body.append(cells)
    t = Table(body, colWidths=[92, st.TEXT_W - 92 - 92, 92], repeatRows=1)
    style = [("BACKGROUND", (0, 0), (-1, 0), st.NAVY),
             ("GRID", (0, 0), (-1, -1), 0.35, st.RULE),
             ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("LEFTPADDING", (0, 0), (-1, -1), 4),
             ("RIGHTPADDING", (0, 0), (-1, -1), 4),
             ("TOPPADDING", (0, 0), (-1, -1), 2.4),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 2.8)]
    for i in range(1, len(body)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), HexColor("#F4F7F8")))
    t.setStyle(TableStyle(style))
    s.append(t)
    s.append(Spacer(1, 9))
    steps = [
        ("Record the question.", "Copy the important information, including units."),
        ("Sketch or tabulate.", "A small diagram or table prevents more errors than any "
                               "other single habit."),
        ("Estimate.", "Write the size you expect."),
        ("Calculate.", "Show each step, one line at a time."),
        ("State the answer with its unit.", ""),
        ("Check.", "Compare with your estimate, or substitute back into the original "
                   "statement."),
    ]
    step_style = ParagraphStyle("mstep", parent=st.STYLES["defn"], leftIndent=15,
                                firstLineIndent=-15, spaceBefore=3.2, spaceAfter=0)
    s.append(B.card("METHOD", "A dependable way to write up work",
                    [Paragraph('<font name="Sans-Bold" size="7.8" color="#0E6B72">%d</font>&nbsp;&nbsp;'
                               '<b>%s</b> %s' % (k + 1, head, tail), step_style)
                     for k, (head, tail) in enumerate(steps)],
                    accent=st.GREEN, tint=st.GREEN_T))
    s.append(Spacer(1, 8))
    s.append(B.card("ATL", "Academic honesty",
                    [Paragraph(rich(
                        "Copying a solution without understanding it creates the appearance of "
                        "progress and hides a gap. Use sample answers to compare methods, not to "
                        "replace your attempt. In investigations, report your own data and "
                        "reasoning and acknowledge every source you use."), st.STYLES["defn"])],
                    accent=st.INDIGO, tint=st.INDIGO_T))
    return s


def page_atl():
    s = [_h("Approaches to learning", 19)]
    s.append(_rule(80, st.INDIGO, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "The approaches to learning (ATL) skills are the methods a student uses to learn "
        "mathematics, not an extra subject. Each chapter names one skill focus and builds it "
        "through a specific activity, in the form: *In order for a student to …, students "
        "must …* The table shows how the ten chapters develop the five skill categories."),
        ParagraphStyle("b", fontName="Book", fontSize=9.4, leading=13.6, textColor=st.INK,
                       spaceAfter=8, alignment=4)))
    rows = [["Skill category", "Chapters", "What the activity requires"],
            ["Communication", "1, 3, 8", "Explaining a method to a named audience, choosing notation "
             "that a reader can follow."],
            ["Research", "9, 10", "Deciding which measurement or sample answers the question, and "
             "stating the limits of the data."],
            ["Thinking (critical)", "2, 5, 6, 10", "Testing a claim, checking a counterexample, "
             "distinguishing a pattern from a proof."],
            ["Thinking (transfer)", "2, 4", "Using one representation in a new context, such as a "
             "multiplier in a shop and in a science measurement."],
            ["Self-management", "all", "Recording working, keeping units, and returning to a "
             "question that has been left incomplete."],
            ["Collaboration", "all investigations", "Agreeing a method, dividing the recording, and "
             "reconciling two different answers."]]
    body = []
    for i, r in enumerate(rows):
        cells = []
        for j, c in enumerate(r):
            if i == 0:
                cells.append(Paragraph('<font name="Sans-Bold" size="6.8" color="#FFFFFF">%s</font>' % c,
                                       ParagraphStyle("hh", fontName="Sans-Bold", fontSize=6.8,
                                                      leading=9, textColor=colors.white)))
            else:
                cells.append(Paragraph(rich(c), ParagraphStyle("nn", fontName="Book", fontSize=8.0,
                                                               leading=10.8, textColor=st.INK)))
        body.append(cells)
    t = Table(body, colWidths=[86, 70, st.TEXT_W - 156], repeatRows=1)
    style = [("BACKGROUND", (0, 0), (-1, 0), st.INDIGO),
             ("GRID", (0, 0), (-1, -1), 0.35, st.RULE),
             ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 4),
             ("RIGHTPADDING", (0, 0), (-1, -1), 4),
             ("TOPPADDING", (0, 0), (-1, -1), 3),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4)]
    for i in range(1, len(body)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), HexColor("#F4F5F9")))
    t.setStyle(TableStyle(style))
    s.append(t)
    s.append(Spacer(1, 10))
    s.append(B.card("ATL", "One example of the structure in practice",
                    [Paragraph(rich(
                        "Chapter 3, critical thinking: *In order for a student to test whether a "
                        "classification is sound, students must construct a set of categories, apply "
                        "them to awkward cases such as 1 and 91, and revise the categories when a "
                        "case fits two of them or none.* The activity is the classification "
                        "task, not a sentence about being careful."), st.STYLES["defn"])],
                    accent=st.INDIGO, tint=st.INDIGO_T))
    s.append(Spacer(1, 8))
    s.append(Paragraph(rich(
        "Skills are assessed through the work they produce: the explanation a student writes, the "
        "table they record, the justification they give. A skill that leaves no trace in the work "
        "has not been developed, only mentioned."), st.STYLES["small"]))
    s.append(Spacer(1, 10))
    s.append(B.MiniHead("Where each skill focus is developed", st.INDIGO))
    rows2 = [["Chapter", "Skill focus", "Activity that builds it"]]
    focus = {1: ("Critical thinking", "Investigation 1 · counting the numbers digit cards can make"),
             2: ("Transfer", "Application 2 · comparing binary and decimal storage claims"),
             3: ("Critical thinking", "Investigation 3 · why squares have an odd number of factors"),
             4: ("Transfer", "Application 4 · scaling a canteen recipe and costing the packs"),
             5: ("Critical thinking", "Investigation 5 · whether two discounts add up"),
             6: ("Critical thinking", "Investigation 6 · generalising the matchstick chain"),
             7: ("Thinking skills", "Investigation 7 · the triangle inequality"),
             8: ("Thinking skills", "Investigation 8 · how much overlap two sets can have"),
             9: ("Research skills", "Application 9 · choosing a water tank from measured data"),
             10: ("Critical thinking", "Application 10 · designing and reporting a survey")}
    for n in range(1, 11):
        rows2.append(["%d" % n, focus[n][0], focus[n][1]])
    body2 = []
    for i, r in enumerate(rows2):
        cells = []
        for j, c in enumerate(r):
            if i == 0:
                cells.append(Paragraph('<font name="Sans-Bold" size="6.8" color="#FFFFFF">%s</font>' % c,
                                       ParagraphStyle("hh3", fontName="Sans-Bold", fontSize=6.8,
                                                      leading=9, textColor=colors.white)))
            else:
                cells.append(Paragraph(rich(c), ParagraphStyle("nn3", fontName="Book", fontSize=8.0,
                                                               leading=10.6, textColor=st.INK)))
        body2.append(cells)
    t2 = Table(body2, colWidths=[46, 92, st.TEXT_W - 138], repeatRows=1)
    st2 = [("BACKGROUND", (0, 0), (-1, 0), st.INDIGO),
           ("GRID", (0, 0), (-1, -1), 0.35, st.RULE),
           ("VALIGN", (0, 0), (-1, -1), "TOP"),
           ("LEFTPADDING", (0, 0), (-1, -1), 4),
           ("RIGHTPADDING", (0, 0), (-1, -1), 4),
           ("TOPPADDING", (0, 0), (-1, -1), 2.6),
           ("BOTTOMPADDING", (0, 0), (-1, -1), 3.0)]
    for i in range(1, len(body2)):
        if i % 2 == 0:
            st2.append(("BACKGROUND", (0, i), (-1, i), HexColor("#F4F5F9")))
    t2.setStyle(TableStyle(st2))
    s.append(t2)
    return s


def page_command_terms():
    s = [_h("Command terms and assessment", 19)]
    s.append(_rule(80, st.PLUM, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "Command terms tell you what kind of answer is expected. They are not decoration: "
        "“state” requires a short answer with no working, while “explain” requires a reason. "
        "The descriptors below are teaching interpretations written for this course; the "
        "authoritative definitions are in the current MYP Mathematics guide."),
        ParagraphStyle("b", fontName="Book", fontSize=9.4, leading=13.6, textColor=st.INK,
                       spaceAfter=8, alignment=4)))
    rows = [["Command term", "What your answer must contain", "Typical instruction"],
            ["State / Write down", "A short answer, no working required", "State the value of the digit 4"],
            ["Calculate", "Working shown, answer with units", "Calculate the area of the triangle"],
            ["Describe", "What happens, in words, without explaining why", "Describe the pattern in the table"],
            ["Explain", "A reason or mechanism, linked to the mathematics", "Explain why 1 is not prime"],
            ["Justify / Verify", "Evidence that supports a stated conclusion", "Justify that the lines are parallel"],
            ["Compare", "Both similarities and differences, with reference to values", "Compare the two averages"],
            ["Show that", "A logical chain that ends at the given result", "Show that the angles sum to 180°"],
            ["Investigate", "A systematic process, a generalisation and a test", "Investigate the number of matches"],
            ["Evaluate / Discuss", "A judgement supported by evidence, with limitations", "Evaluate the two proposals"]]
    body = []
    for i, r in enumerate(rows):
        cells = []
        for j, c in enumerate(r):
            if i == 0:
                cells.append(Paragraph('<font name="Sans-Bold" size="6.8" color="#FFFFFF">%s</font>' % c,
                                       ParagraphStyle("hh2", fontName="Sans-Bold", fontSize=6.8,
                                                      leading=9, textColor=colors.white)))
            else:
                cells.append(Paragraph(rich(c), ParagraphStyle("nn2", fontName="Book", fontSize=8.0,
                                                               leading=10.8, textColor=st.INK)))
        body.append(cells)
    t = Table(body, colWidths=[76, 210, st.TEXT_W - 286], repeatRows=1)
    style = [("BACKGROUND", (0, 0), (-1, 0), st.PLUM),
             ("GRID", (0, 0), (-1, -1), 0.35, st.RULE),
             ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 4),
             ("RIGHTPADDING", (0, 0), (-1, -1), 4),
             ("TOPPADDING", (0, 0), (-1, -1), 3),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4)]
    for i in range(1, len(body)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), HexColor("#F1F7F7")))
    t.setStyle(TableStyle(style))
    s.append(t)
    s.append(Spacer(1, 10))
    s.append(B.card("NOTE", "How the four criteria are used in this book",
                    [Paragraph(rich(
                        "<b>A Knowing and understanding</b> — fluency questions and worked examples. "
                        "<b>B Investigating patterns</b> — the investigation in each chapter, which "
                        "asks for a generalisation and a test. <b>C Communicating</b> — the Task C "
                        "writing task. <b>D Applying mathematics in real-life contexts</b> — the "
                        "application task, which always names the constraints and asks for a "
                        "justified decision. Criteria are attached to activities that genuinely "
                        "require them, not to ordinary exercises."), st.STYLES["defn"])],
                    accent=st.SLATE_T, tint=HexColor("#F2F4F6")))
    s.append(Spacer(1, 8))
    s.append(Paragraph(rich(
        "Levels are awarded on the evidence a student produces in the activity, using the "
        "success criteria printed beside each task. A task that has been attempted but not "
        "completed still provides evidence; a blank page provides none."), st.STYLES["small"]))
    return s


SECTIONS = [
    ("Welcome", page_welcome),
    ("How to use this book", page_how_to_use),
    ("Visual guide", page_icons),
    ("The MYP framework", page_framework),
    ("Assessment criteria", page_criteria),
    ("Course map", page_course_map),
    ("Approaches to learning", page_atl),
    ("Command terms and assessment", page_command_terms),
    ("Notation and habits", page_notation),
]


# ------------------------------------------------------------------ answers
def answers_section(data, chapters):
    s = [_h("Answers and worked solutions", 20)]
    s.append(_rule(70, st.TEAL, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "Answers are given so that you can check your reasoning, not replace it. Where a "
        "question has more than one sensible answer, a sample answer is shown. Where a "
        "question asks you to explain, the answer shows the kind of reasoning expected."),
        st.STYLES["small"]))
    s.append(Spacer(1, 8))
    for ch in chapters:
        accent = st.chapter_colour(ch["part"])
        heading = ("CUMULATIVE REVISION" if ch["n"] == 0
                   else "CHAPTER %02d · %s" % (ch["n"], ch["title"].upper()))
        s.append(Paragraph(heading,
                           ParagraphStyle("ca", fontName="Sans-Bold", fontSize=9.4,
                                          leading=12.6, textColor=accent,
                                          spaceBefore=8, spaceAfter=4)))
        for pid, ptitle, items in ch["_answers"]:
            s.append(Paragraph('<font name="Sans-Bold" size="7.6" color="#17222B">Practice %s</font>'
                               '<font name="Sans" size="7.6" color="#4A4A4A"> · %s</font>'
                               % (pid, ptitle),
                               ParagraphStyle("ap", fontName="Sans-Bold", fontSize=7.6,
                                              leading=10.4, textColor=st.INK,
                                              spaceBefore=3, spaceAfter=2)))
            for n, a in items:
                if not a:
                    continue
                s.append(Paragraph('<font name="Sans-Bold" size="7.2" color="#0E6E76">%d.</font> '
                                   '<font name="Sans" size="7.2" color="#17222B">%s</font>'
                                   % (n, rich(a)),
                                   ParagraphStyle("an", fontName="Sans", fontSize=7.2,
                                                  leading=9.8, textColor=st.INK,
                                                  leftIndent=9, firstLineIndent=-9,
                                                  spaceAfter=1.2)))
        for pid, items in ch.get("_prereq_answers", []):
            s.append(Paragraph('<font name="Sans-Bold" size="7.6" color="#17222B">%s</font>'
                               % pid,
                               ParagraphStyle("ap2", fontName="Sans-Bold", fontSize=7.6,
                                              leading=10.4, textColor=st.INK,
                                              spaceBefore=3, spaceAfter=2)))
            for n, a in items:
                s.append(Paragraph('<font name="Sans-Bold" size="7.2" color="#0E6E76">%d.</font> '
                                   '<font name="Sans" size="7.2" color="#17222B">%s</font>'
                                   % (n, rich(a)),
                                   ParagraphStyle("an2", fontName="Sans", fontSize=7.2,
                                                  leading=9.8, textColor=st.INK,
                                                  leftIndent=9, firstLineIndent=-9,
                                                  spaceAfter=1.2)))
    return s


# ------------------------------------------------------------------ reference
FORMULAS = [
    ("Number and place value", [
        ("Place value in a base-ten number", "each place is 10 times the place on its right"),
        ("Expanded form", "$3{,}048 = 3\\times1000 + 0\\times100 + 4\\times10 + 8\\times1$"),
    ]),
    ("Powers and roots", [
        ("Power notation", "$a^{n} = a \\times a \\times \\dots \\times a$ ($n$ factors)"),
        ("Multiplying powers of the same base", "$a^{m} \\times a^{n} = a^{m+n}$"),
        ("Dividing powers of the same base", "$a^{m} \\div a^{n} = a^{m-n}$ ($m>n$)"),
        ("Power of a power", "$(a^{m})^{n} = a^{mn}$"),
        ("Zero and first powers", "$a^{0} = 1$, $a^{1} = a$ ($a \\ne 0$)"),
        ("Square root", "$\\sqrt{a}$ is the positive number whose square is $a$"),
    ]),
    ("Factors and multiples", [
        ("Highest common factor", "HCF: the largest number dividing both exactly"),
        ("Lowest common multiple", "LCM: the smallest number divisible by both"),
        ("Relationship", "HCF $\\times$ LCM $= a \\times b$ for positive integers $a$, $b$"),
    ]),
    ("Fractions and decimals", [
        ("Equivalent fractions", "$\\frac{a}{b} = \\frac{ak}{bk}$ ($k \\ne 0$)"),
        ("Adding and subtracting", "$\\frac{a}{b} \\pm \\frac{c}{d} = \\frac{ad \\pm bc}{bd}$"),
        ("Multiplying", "$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{ac}{bd}$"),
        ("Dividing", "$\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c}$"),
        ("Fraction to decimal", "divide the numerator by the denominator"),
    ]),
    ("Percentages", [
        ("Percentage of a quantity", "amount $= \\frac{p}{100} \\times$ quantity"),
        ("Increase by $p\\%$", "multiply by $1 + \\frac{p}{100}$"),
        ("Decrease by $p\\%$", "multiply by $1 - \\frac{p}{100}$"),
        ("Successive changes", "multiply the multipliers: $1.2 \\times 0.9$"),
        ("Percentage change", "$\\frac{\\text{change}}{\\text{original}} \\times 100\\%$"),
    ]),
    ("Algebra", [
        ("Collecting like terms", "$3x + 2x = 5x$"),
        ("Expanding", "$a(b + c) = ab + ac$"),
        ("Solving a two-step equation", "undo the addition, then undo the multiplication"),
        ("Perimeter of a rectangle", "$P = 2(l + w)$"),
        ("Area of a rectangle", "$A = lw$"),
    ]),
    ("Geometry", [
        ("Angles on a straight line", "sum to $180\\degree$"),
        ("Angles at a point", "sum to $360\\degree$"),
        ("Vertically opposite angles", "equal"),
        ("Alternate angles between parallel lines", "equal"),
        ("Corresponding angles between parallel lines", "equal"),
        ("Co-interior angles between parallel lines", "sum to $180\\degree$"),
        ("Angle sum of a triangle", "$180\\degree$"),
        ("Exterior angle of a triangle", "equals the sum of the two opposite interior angles"),
        ("Angle sum of a polygon", "$(n-2) \\times 180\\degree$"),
        ("Exterior angle of a regular polygon", "$\\frac{360\\degree}{n}$"),
    ]),
    ("Measurement", [
        ("Perimeter", "the total distance around a shape"),
        ("Area of a triangle", "$A = \\frac{1}{2}bh$"),
        ("Area of a parallelogram", "$A = bh$"),
        ("Area of a trapezium", "$A = \\frac{1}{2}(a+b)h$"),
        ("Circumference of a circle", "$C = 2\\pi r = \\pi d$"),
        ("Area of a circle", "$A = \\pi r^{2}$"),
        ("Volume of a prism", "$V = $ area of cross-section $\\times$ length"),
        ("Volume of a cuboid", "$V = lwh$"),
        ("Surface area of a cuboid", "$A = 2(lw + lh + wh)$"),
        ("Capacity", "$1\\text{ L} = 1000\\text{ cm}^{3}$, $1\\text{ m}^{3} = 1000\\text{ L}$"),
        ("Unit conversions", "$1\\text{ m} = 100\\text{ cm}$, $1\\text{ km} = 1000\\text{ m}$; "
                             "1 m² = 10,000 cm²"),
    ]),
    ("Sets", [
        ("Number of elements", "$n(A \\cup B) = n(A) + n(B) - n(A \\cap B)$"),
        ("Complement", "$n(A') = n(U) - n(A)$"),
    ]),
    ("Data", [
        ("Mean", "sum of values $\\div$ number of values"),
        ("Median", "middle value of an ordered list"),
        ("Mode", "the most frequent value"),
        ("Range", "largest value $-$ smallest value"),
        ("Sector angle", "$\\frac{\\text{frequency}}{\\text{total}} \\times 360\\degree$"),
        ("Frequency density idea", "a histogram shows frequency by area"),
    ]),
]


def formula_bank():
    s = [_h("Formula bank", 20)]
    s.append(_rule(70, st.TEAL, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "Formulas are collected here for reference. A formula is a compressed relationship: read "
        "it slowly, name each symbol and its unit, and check that the result is sensible before "
        "using it in a problem."), st.STYLES["small"]))
    s.append(Spacer(1, 6))
    for group, items in FORMULAS:
        s.append(B.MiniHead(group, st.TEAL))
        rows = []
        for name, formula in items:
            rows.append([Paragraph(rich(name), ParagraphStyle("f", fontName="Sans", fontSize=7.8,
                                                        leading=10.6, textColor=st.INK)),
                         Paragraph(rich(formula), ParagraphStyle("g", fontName="Book",
                                                                 fontSize=8.0, leading=11,
                                                                 textColor=st.INK))])
        t = Table(rows, colWidths=[st.TEXT_W * 0.40, st.TEXT_W * 0.60])
        t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 2),
                               ("TOPPADDING", (0, 0), (-1, -1), 2),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 2.4),
                               ("LINEBELOW", (0, 0), (-1, -2), 0.25, st.RULE_LIGHT)]))
        s.append(t)
    return s


def glossary():
    import chapterdata
    s = [_h("Glossary", 20)]
    s.append(_rule(70, st.TEAL, 2.6))
    s.append(Spacer(1, 6))
    s.append(Paragraph(rich(
        "Each entry gives the meaning used in this course. Where a term has a wider meaning in "
        "mathematics, the entry states the Year 1 boundary."), st.STYLES["small"]))
    s.append(Spacer(1, 6))
    rows = []
    for term, defn in sorted(chapterdata.GLOSSARY, key=lambda x: x[0].lower()):
        rows.append([Paragraph('<font name="Sans-Bold" size="7.8" color="#12344D">%s</font>' % rich(term),
                               ParagraphStyle("gt", fontName="Sans-Bold", fontSize=7.8,
                                              leading=10.4, textColor=st.NAVY)),
                     Paragraph(rich(defn), ParagraphStyle("gd", fontName="Book",
                                                          fontSize=7.8, leading=10.4,
                                                          textColor=st.INK))])
    t = Table(rows, colWidths=[104, st.TEXT_W - 104])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (0, -1), 8),
                           ("TOPPADDING", (0, 0), (-1, -1), 1.8),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
                           ("LINEBELOW", (0, 0), (-1, -2), 0.22, st.RULE_LIGHT)]))
    s.append(t)
    return s


def index_section(registry, offset):
    s = [_h("Index", 20)]
    s.append(_rule(70, st.TEAL, 2.6))
    s.append(Spacer(1, 5))
    entries = registry.entries()
    if not entries:
        s.append(Paragraph("No index entries were registered during this build.",
                           st.STYLES["body"]))
        return s
    s.append(Paragraph(rich(
        "Page numbers are the printed page numbers at the foot of each page; the first "
        "number is usually the section where the idea is introduced."), st.STYLES["small"]))
    s.append(Spacer(1, 4))

    shown = []
    for term, pages in entries:
        nums = sorted({p - offset + 1 for p in pages if p >= offset})
        if not nums:
            continue
        out, i = [], 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1
            out.append(str(nums[i]) if j == i else ("%d–%d" % (nums[i], nums[j])))
            i = j + 1
        shown.append((term, ", ".join(out)))
    shown.sort(key=lambda x: x[0].lower())

    term_style = ParagraphStyle("it", fontName="Sans", fontSize=7.4, leading=10.0,
                                textColor=st.INK)
    page_style = ParagraphStyle("ip", fontName="Sans", fontSize=7.4, leading=10.0,
                                textColor=st.INK_SOFT, alignment=2)
    letter_style = ParagraphStyle("il", fontName="Sans-Bold", fontSize=9.0, leading=13,
                                  textColor=st.TEAL, spaceBefore=5, spaceAfter=1)

    groups = []
    for term, nums in shown:
        letter = term[0].upper()
        if not letter.isalpha():
            letter = "Numbers and symbols"
        if not groups or groups[-1][0] != letter:
            groups.append((letter, []))
        groups[-1][1].append((term, nums))

    half = st.TEXT_W / 2.0
    widths = [half - 88, 82, half - 88, 82]
    for letter, items in groups:
        s.append(Paragraph(letter, letter_style))
        rows = []
        col = (len(items) + 1) // 2
        left, right = items[:col], items[col:]
        for i in range(col):
            r = [Paragraph(left[i][0], term_style), Paragraph(left[i][1], page_style)]
            if i < len(right):
                r += [Paragraph(right[i][0], term_style), Paragraph(right[i][1], page_style)]
            else:
                r += ["", ""]
            rows.append(r)
        t = Table(rows, colWidths=widths)
        t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (0, -1), 8),
                               ("RIGHTPADDING", (1, 0), (1, -1), 14),
                               ("RIGHTPADDING", (2, 0), (2, -1), 8),
                               ("RIGHTPADDING", (3, 0), (3, -1), 0),
                               ("TOPPADDING", (0, 0), (-1, -1), 0.8),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 1.0)]))
        s.append(t)
    return s


def acknowledgements():
    s = [_h("References and acknowledgements", 20)]
    s.append(_rule(70, st.TEAL, 2.6))
    s.append(Spacer(1, 8))
    blocks = [
        ("Curriculum framework", "The concepts, global contexts, inquiry structure and "
                                 "assessment criteria referenced in this book follow the publicly "
                                 "described Middle Years Programme framework. Teachers should "
                                 "consult the current official MYP Mathematics subject guide and "
                                 "their school's programme documentation for authoritative "
                                 "requirements. No official IB descriptor is reproduced here."),
        ("Originality of content", "All prose, worked examples, exercises, investigations, "
                                   "criterion tasks, rubrics, diagrams and layouts in this book "
                                   "were created for this edition. The improved first edition "
                                   "reorganises and expands the author's first edition; it "
                                   "preserves the first edition's topic coverage and intended "
                                   "Year 1 scope while rebuilding the pedagogy and presentation."),
        ("Pedagogical references", "The arrangement of each chapter — engage, explore, explain, "
                                   "worked examples, graduated practice, investigation, "
                                   "application and reflection — reflects widely used "
                                   "inquiry-based and concept-driven design principles in "
                                   "lower-secondary mathematics. No third-party text or layout "
                                   "is reproduced."),
        ("Diagrams", "Every figure is an original vector diagram drawn for this book. The "
                     "diagram set, its purpose and its licence are recorded in the project's "
                     "image reference list. No third-party photographs are used."),
        ("Fonts and software", "DejaVu Serif and DejaVu Sans are used under the SIL Open Font "
                               "License. The book was typeset with an original Python/ReportLab "
                               "paged-media pipeline written for this project."),
        ("Data", "Contexts use rounded or classroom-generated figures, chosen to make the "
                 "mathematics visible. Where a source is named in a task, the figure is "
                 "reproduced for teaching purposes and students should verify current values."),
        ("Author", "SADIKOU Moukoddim · Head of Mathematics Department · Mathematics Teacher · "
                   "Category 1."),
    ]
    rows = []
    for lab, txt in blocks:
        rows.append([Paragraph(lab, ParagraphStyle("l", fontName="Sans-Bold", fontSize=7.6,
                                                   leading=10.4, textColor=st.TEAL)),
                     Paragraph(txt, ParagraphStyle("t", fontName="Book", fontSize=8.0,
                                                   leading=11.2, textColor=st.INK))])
    t = Table(rows, colWidths=[96, st.TEXT_W - 96])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                           ("TOPPADDING", (0, 0), (-1, -1), 4),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                           ("LINEBELOW", (0, 0), (-1, -2), 0.3, st.RULE_LIGHT)]))
    s.append(t)
    return s
