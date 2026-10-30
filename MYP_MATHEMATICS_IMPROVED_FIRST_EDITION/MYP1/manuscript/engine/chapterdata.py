"""Chapter assembly: metadata, figures, parsed content, TOC entries."""
import os
import re

from bookkit import content as C
from bookkit import style as st

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def scan_sections(path):
    out = []
    with open(path, encoding="utf-8") as fh:
        for ln in fh:
            if ln.startswith("@SEC"):
                parts = [p.strip() for p in ln[4:].strip().lstrip("|").split("|")]
                if len(parts) >= 2:
                    out.append((parts[0], parts[1]))
            elif ln.startswith("@SPECIAL"):
                parts = [p.strip() for p in ln[8:].strip().lstrip("|").split("|")]
                if parts and parts[0]:
                    out.append(("", parts[0]))
    return out


def load():
    import chaptermeta
    import figs_registry

    chapters = chaptermeta.CHAPTERS
    data = {"chapters": chapters, "toc_entries": []}
    return data


def build_all(pages_map, index_registry, only=None):
    """Parse every chapter's content file and return the chapter list."""
    import chaptermeta
    import figs_registry

    chapters = chaptermeta.CHAPTERS
    for ch in chapters:
        path = os.path.join(ROOT, ch["content"])
        figs = {k: v for k, v in figs_registry.FIGS.items()
                if k.startswith("c%02d_" % ch["n"])}
        ch["_prereq_answers"] = []
        answers = []
        story, _ = C.parse(path, ch, figs, pages_map, index_registry,
                           st.chapter_colour(ch["part"]), st.chapter_tint(ch["part"]),
                           answers)
        ch["_story"] = story
        ch["_sections"] = scan_sections(path)
        ch["_answers"] = answers
    return chapters


def revision_story(pages_map, index_registry):
    """Build the cumulative revision section from content/revision.txt."""
    from bookkit import style as st
    from bookkit import content as C
    path = os.path.join(ROOT, "content", "revision.txt")
    meta = {"n": 0, "part": 1, "title": "Cumulative revision"}
    answers = []
    story, _ = C.parse(path, meta, {}, pages_map, index_registry,
                       st.NAVY, st.NAVY_T, answers)
    return story, answers


def toc_entries(chapters, pages_map):
    """Structure of the table of contents."""
    from bookkit import style as st
    entries = []
    entries.append((0, "FRONT MATTER", "front:start"))
    for name, _ in _front_sections():
        entries.append((2, name, "front:" + name))
    for i, (numeral, pname, accent, tint) in enumerate(st.PART_COLOURS, 1):
        chs = [c for c in chapters if c["part"] == i]
        if not chs:
            continue
        entries.append((0, "PART %s · %s" % (numeral, pname), "part:%d" % i))
        for ch in chs:
            entries.append((1, "%d   %s" % (ch["n"], ch["title"]), "ch:%d" % ch["n"]))
            for num, title in scan_sections(os.path.join(ROOT, ch["content"])):
                if num:
                    entries.append((2, "%s   %s" % (num, title),
                                    "sec:%s:%s" % (ch["n"], num)))
                else:
                    entries.append((3, title, "special:%s:%s" % (ch["n"], title)))
    entries.append((0, "REFERENCE", "ref:start"))
    entries.append((2, "Cumulative revision", "ref:Cumulative revision"))
    rev_path = os.path.join(ROOT, "content", "revision.txt")
    if os.path.exists(rev_path):
        for num, title in scan_sections(rev_path):
            entries.append((3, "%s   %s" % (num, title), "sec:0:%s" % num))
    for name in ("Answers and worked solutions", "Formula bank",
                 "Glossary", "Index", "References and acknowledgements"):
        entries.append((2, name, "ref:" + name))
    return entries


def _front_sections():
    import frontmatter
    return frontmatter.SECTIONS


GLOSSARY = [
    ("Acute angle", "An angle smaller than 90°."),
    ("Alternate angles", "A pair of equal angles on opposite sides of a transversal between "
                         "parallel lines."),
    ("Angle", "The amount of turn between two straight lines that meet at a point, measured "
              "in degrees."),
    ("Area", "The amount of surface a shape covers, measured in square units."),
    ("Average", "A single value used to summarise a set of values; in this course the mean, "
                "median and mode."),
    ("Bar chart", "A display in which the height or length of each bar shows the frequency of "
                  "a category."),
    ("Base", "In a power, the number that is multiplied repeatedly, as in $2^{5}$."),
    ("Bidmas", "The agreed order of operations: brackets, indices, division and multiplication, "
               "addition and subtraction."),
    ("Capacity", "The amount a container can hold, usually measured in litres or millilitres."),
    ("Cardinality", "The number of elements in a set, written $n(A)$."),
    ("Categorical data", "Data that records a category or label rather than a number."),
    ("Circumference", "The perimeter of a circle, $C = 2\\pi r$."),
    ("Coefficient", "The number multiplying a variable in a term, as in $7x$."),
    ("Common factor", "A number that divides two or more numbers exactly."),
    ("Complement", "The elements of the universal set that are not in the set, written $A'$."),
    ("Composite number", "A whole number greater than 1 with more than two factors."),
    ("Congruent", "Exactly the same shape and size."),
    ("Constant", "A quantity that does not change."),
    ("Continuous data", "Numerical data that can take any value in a range, such as height."),
    ("Corresponding angles", "Angles in the same position at each intersection when a "
                             "transversal crosses parallel lines; they are equal."),
    ("Cross-section", "The shape you see when a solid is sliced parallel to its base."),
    ("Cube number", "A number of the form $n \\times n \\times n$, such as 27."),
    ("Cuboid", "A solid with six rectangular faces."),
    ("Decimal", "A number written using place value with tenths, hundredths and so on."),
    ("Denominator", "The number below the line in a fraction; it names the size of each part."),
    ("Diameter", "A straight line across a circle through its centre; $d = 2r$."),
    ("Difference", "The result of subtracting one number from another."),
    ("Discrete data", "Numerical data that can take only particular values, usually whole numbers."),
    ("Divisible", "A whole number $a$ is divisible by $b$ if $b$ divides $a$ with no remainder."),
    ("Equation", "A statement that two expressions are equal."),
    ("Equivalent fractions", "Fractions with the same value, such as $\\frac{1}{2}$ and $\\frac{3}{6}$."),
    ("Estimate", "An approximate answer obtained by rounding or by another deliberate "
                 "simplification."),
    ("Expanded form", "A number written as the sum of the values of its digits."),
    ("Exponent", "The number in a power that records how many copies of the base are "
                 "multiplied, as in $2^{5}$."),
    ("Expression", "A combination of numbers, variables and operations without an equals sign."),
    ("Factor", "A whole number that divides another exactly, with no remainder."),
    ("Factor pair", "Two factors that multiply to give a number, such as 4 and 9 for 36."),
    ("Factor tree", "A diagram that breaks a number into prime factors step by step."),
    ("Formula", "A rule written with symbols that relates quantities."),
    ("Frequency", "How often a value or category occurs."),
    ("Greater than", "The symbol $>$ means is greater than; $5 > 3$."),
    ("HCF", "Highest common factor: the largest number that divides two or more numbers exactly."),
    ("Histogram", "A display of continuous data grouped into equal class intervals, where the "
                  "area of each bar shows the frequency."),
    ("Hypotenuse", "The side opposite the right angle in a right-angled triangle."),
    ("Improper fraction", "A fraction whose numerator is greater than or equal to its "
                          "denominator, such as $\\frac{7}{4}$."),
    ("Index", "Another word for exponent."),
    ("Integer", "Any whole number, positive, negative or zero."),
    ("Intersection", "The elements that belong to both sets, written $A \\cap B$."),
    ("Inverse", "An operation that undoes another, such as addition and subtraction."),
    ("Irregular", "Not regular: sides or angles are not all equal."),
    ("LCM", "Lowest common multiple: the smallest number that two or more numbers divide into "
            "exactly."),
    ("Less than", "The symbol $<$ means is less than; $3 < 5$."),
    ("Like terms", "Terms with exactly the same variable part, such as $3x$ and $5x$."),
    ("Mean", "The sum of the values divided by the number of values."),
    ("Median", "The middle value of an ordered data set."),
    ("Mixed number", "A whole number together with a fraction, such as $2\\frac{1}{3}$."),
    ("Mode", "The value that occurs most often."),
    ("Multiple", "The result of multiplying a whole number by another whole number."),
    ("Natural number", "A counting number: 1, 2, 3, …"),
    ("Negative number", "A number less than zero."),
    ("Notation", "A agreed system for writing symbols and values."),
    ("Numerator", "The number above the line in a fraction; it counts the parts."),
    ("Obtuse angle", "An angle between 90° and 180°."),
    ("Origin", "The point where the $x$-axis and $y$-axis meet, $(0, 0)$."),
    ("Outlier", "A value that lies far from the rest of the data."),
    ("Parallel", "Lines in the same plane that never meet; the symbol is $\\parallel$."),
    ("Parallelogram", "A quadrilateral with two pairs of parallel sides."),
    ("Percentage", "A proportion expressed out of 100."),
    ("Perimeter", "The total distance around the outside of a shape."),
    ("Perpendicular", "At right angles; the symbol is $\\perp$."),
    ("Pi ($\\pi$)", "The ratio of the circumference of a circle to its diameter, "
                    "approximately 3.14159."),
    ("Place value", "The value a digit has because of its position in a number."),
    ("Polygon", "A closed shape made of straight sides."),
    ("Prime factorisation", "A number written as a product of prime factors."),
    ("Prime number", "A whole number greater than 1 with exactly two factors, 1 and itself."),
    ("Prism", "A solid with the same cross-section all along its length."),
    ("Product", "The result of a multiplication."),
    ("Proper fraction", "A fraction whose numerator is smaller than its denominator."),
    ("Proportion", "A relationship in which quantities keep the same ratio."),
    ("Quadrilateral", "A polygon with four sides."),
    ("Quotient", "The result of a division."),
    ("Range", "The largest value minus the smallest value in a data set."),
    ("Ratio", "A comparison of two quantities by division."),
    ("Rational number", "A number that can be written as a fraction of two integers."),
    ("Reciprocal", "The number you multiply by to get 1; the reciprocal of $\\frac{3}{4}$ is "
                   "$\\frac{4}{3}$."),
    ("Regular polygon", "A polygon with all sides and all angles equal."),
    ("Remainder", "What is left over after a division that is not exact."),
    ("Round", "Write a number to a required degree of accuracy."),
    ("Scale drawing", "A drawing in which every length is a fixed fraction of the real length."),
    ("Sector", "The region of a circle between two radii."),
    ("Set", "A well-defined collection of objects."),
    ("Simplifying", "Rewriting an expression or fraction in a shorter equivalent form."),
    ("Solution", "A value of the variable that makes an equation true."),
    ("Square number", "A number of the form $n \\times n$, such as 49."),
    ("Square root", "A value that, multiplied by itself, gives the number; $\\sqrt{49} = 7$."),
    ("Standard form of a number", "A number written with digits rather than in expanded form."),
    ("Subset", "A set whose elements all belong to another set, written $A \\subset B$."),
    ("Substitute", "Replace a variable with a number."),
    ("Surface area", "The total area of all the faces of a solid."),
    ("Term", "A part of an expression separated by addition or subtraction."),
    ("Transversal", "A line that crosses two or more other lines."),
    ("Trapezium", "A quadrilateral with exactly one pair of parallel sides."),
    ("Union", "The elements that belong to either set, written $A \\cup B$."),
    ("Universal set", "The set of all elements being considered, written $\\mathcal{U}$."),
    ("Variable", "A letter that stands for a number that can change."),
    ("Venn diagram", "A diagram using overlapping circles to show sets and their relationships."),
    ("Irrational number", "A number that cannot be written as a fraction of two integers, "
                          "such as $\\sqrt{2}$ or $\\pi$; its decimal never ends or repeats."),
    ("Real number", "Any number that has a position on the number line: every rational number "
                    "and every irrational number together."),
    ("Interior angle", "An angle inside a polygon, between two of its sides. The interior "
                       "angles of an $n$-sided polygon total $(n-2) \\times 180\\degree$."),
    ("Exterior angle", "The angle between one side of a polygon and the extension of the next "
                       "side. The exterior angles of a convex polygon total $360\\degree$."),
    ("Net", "A flat shape that folds into a solid; the area of the net is the surface area of "
            "the solid."),
    ("Recurring decimal", "A decimal in which a digit or block of digits repeats for ever, such "
                          "as $0.\\dot{3}$ or $0.\\overline{36}$; every recurring decimal is rational."),
    ("Terminating decimal", "A decimal with a finite number of digits after the point, such as "
                            "$0.375$; it equals a fraction whose denominator has no prime factors "
                            "other than 2 and 5."),
    ("Discount", "An amount taken off a marked price, usually quoted as a percentage of that price."),
    ("Tax (VAT)", "An amount added to a price by government, quoted as a percentage. To remove a "
                  "tax that is already included, divide by $1 + \\frac{\\text{rate}}{100}$."),
    ("Budget", "A plan for spending a fixed total, in which each item can be compared with the "
               "total as a percentage."),
    ("Vertex", "A corner of a shape, or the point where two lines meet."),
    ("Volume", "The amount of space a solid occupies, measured in cubic units."),
    ("Whole number", "Zero together with the natural numbers: 0, 1, 2, 3, …"),
]
