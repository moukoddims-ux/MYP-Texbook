"""Registry of original diagrams, keyed by chapter prefix."""
from bookkit import figures as F
from bookkit import style as st
from reportlab.lib.colors import HexColor

FIGS = {}
FIGS.update({
    "c01_places": (
        lambda: F.placevalue(["Thousands", "Hundreds", "Tens", "Ones", "Tenths",
                              "Hundredths", "Thousandths"],
                             ["3", "0", "4", "8", "3", "0", "7"],
                             highlight=3),
        "Place-value columns for 3,048.307. The decimal point marks the boundary between "
        "whole-number places and fractional places.", None),
    "c01_numline": (
        lambda: F.numline(-5, 5, marks=[(-4, "−4"), (3, "3")]),
        "On a horizontal number line, values increase from left to right. Negative numbers "
        "lie to the left of zero.", None),
    "c01_order": (
        lambda: F.numline(-9, 1, marks=[(-8, "−8"), (-3, "−3")], label_every=1),
        "−8 lies further left than −3, so −8 < −3 even though 8 is greater than 3.", None),
    "c01_round": (
        lambda: F.numline(3400, 3600, ticks=[3400, 3450, 3500, 3550, 3600],
                          marks=[(3486, "3,486")]),
        "3,486 is closer to 3,500 than to 3,400, so it rounds to 3,500 when rounded to the "
        "nearest hundred.", None),
    "c01_round10": (
        lambda: F.numline(0, 1000, ticks=[0, 250, 500, 750, 1000],
                          marks=[(486, "486")], label_every=1),
        "486 lies between 400 and 500, and closer to 500. Rounding to the nearest hundred "
        "gives 500.", None),
    "c01_digits": (
        lambda: F.digit_cards(),
        "Three-digit arrangements made from the cards 3, 0 and 5. Zero cannot take the "
        "leading place in a three-digit number.", None),
    "c01_dec": (
        lambda: F.fraction_bar(w=300, h=40, parts=10, shaded=3, col=st.TEAL,
                               labels=["0.1"] * 10, lab="0.3 means three tenths"),
        "A tenths strip: 0.3 is three of ten equal parts, so 0.3 = 3/10.", None),
})

FIGS.update({
    "c02_power": (
        lambda: F.power_repeat(2, 4),
        "2⁴ records four factors of 2. The base is 2; the exponent is 4.", None),
    "c02_square": (
        lambda: F.square_numbers(4),
        "A square number can be arranged as a square of dots: 4 × 4 = 16.", None),
    "c02_ops": (
        lambda: F.ops_priority(),
        "The agreed order of operations. Within one step, work from left to right.", None),
    "c02_fold": (
        lambda: F.paper_fold(),
        "Each fold doubles the number of layers, so the number of layers is a power of 2.", None),
    "c02_places": (
        lambda: F.placevalue(["10⁴", "10³", "10²", "10¹", "10⁰"],
                             ["3", "0", "4", "8", "6"], highlight=4),
        "Every place is a power of ten: 10⁰ = 1, 10¹ = 10, 10² = 100, 10³ = 1,000.", None),
})

FIGS.update({
    "c03_arrays": (
        lambda: F.factor_arrays(12),
        "The factor pairs of 12 as rectangles: 1 × 12, 2 × 6 and 3 × 4.", None),
    "c03_ray": (
        lambda: F.number_ray_factors(24),
        "Testing each number up to 24 to see whether it divides 24 exactly.", None),
    "c03_sieve": (
        lambda: F.sieve_grid(50),
        "A sieve of Eratosthenes for the numbers 1 to 50: each prime is shaded.", None),
    "c03_tree": (
        lambda: F.factor_tree(60),
        "A factor tree for 60. The primes at the ends of the branches give "
        "60 = 2 × 2 × 3 × 5.", None),
    "c03_venn": (
        lambda: F.common_factors_venn(),
        "The factors of 12 and 18. The overlap contains the common factors 1, 2, 3 and 6, "
        "so the highest common factor is 6.", None),
})

FIGS.update({
    "c04_wall": (
        lambda: F.fraction_wall(),
        "A fraction wall. Aligned bars show which fractions are equal and which are larger: "
        "each half-line matches a line on the bar below it.", None),
    "c04_equiv": (
        lambda: F.equiv_bars(),
        "Two thirds and four sixths cover exactly the same length of the bar, so they are "
        "equivalent fractions.", None),
    "c04_grid": (
        lambda: F.dec_grid(37),
        "A hundred square with 37 hundredths shaded. The same quantity is written 0.37, "
        "37/100 or 37%.", None),
    "c04_division": (
        lambda: F.long_division(3, 8),
        "Converting 3/8 to a decimal by division: the remainder is carried and the division "
        "continues past the decimal point, giving 0.375.", None),
})

FIGS.update({
    "c05_grid": (
        lambda: F.percent_grid(45),
        "45 of 100 squares shaded. A percentage is a fraction with denominator 100, so this is "
        "45%, or 0.45, or 45/100.", None),
    "c05_bar": (
        lambda: F.percent_bar(),
        "The same positions on a number line written as percentages, fractions and decimals.", None),
    "c05_discount": (
        lambda: F.discount_chain(),
        "A price reduced by 20% and then by a further 10% ends at 72% of the original price, "
        "not at 70%.", None),
})

FIGS.update({
    "c06_match": (
        lambda: F.matchstick(4),
        "The first four stages of the matchstick chain. Each new square shares one match, so "
        "the number of matches grows by 3 at every stage.", None),
    "c06_machine": (
        lambda: F.function_machine(),
        "A two-step function machine. The input 5 is multiplied by 3 and then increased by 2, "
        "giving 17. Reading the machine backwards recovers the input.", None),
    "c06_balance": (
        lambda: F.balance(left="3x + 4", right="19"),
        "An equation is a balance. Whatever is done to one side must be done to the other, so "
        "the two sides stay equal.", None),
    "c06_steps": (
        lambda: F.equation_steps(),
        "The same equation solved in two inverse operations, with the reason for each step "
        "recorded beside it.", None),
})

FIGS.update({
    "c07_types": (
        lambda: F.angle_types(),
        "Angles are classified by size: acute, right, obtuse and reflex.", None),
    "c07_angles": (
        lambda: F.angle_on_line(240, 100, 125, 55),
        "Two angles on a straight line. However the line is divided, the two angles add to 180°.", None),
    "c07_parallel": (
        lambda: F.angle_pair(mode="corresponding"),
        "A transversal crossing two parallel lines makes eight angles. Corresponding angles are "
        "equal, and alternate angles are equal.", None),
    "c07_sum": (
        lambda: F.triangle_sum(),
        "The three angles of any triangle add to 180°. The dashed line through the apex, parallel "
        "to the base, shows why: the three angles fit on a straight line.", None),
    "c07_bisector": (
        lambda: F.perpendicular_bisector(),
        "Constructing the perpendicular bisector of AB with compasses: equal arcs from A and "
        "from B meet at two points, and the line through them is perpendicular to AB.", None),
})

FIGS.update({
    "c08_venn": (
        lambda: F.venn_regions(),
        "The four regions of a two-set Venn diagram: in A only, in both, in B only, and outside "
        "both but inside the universal set.", None),
    "c08_tree": (
        lambda: F.classification_tree(),
        "A classification tree for whole numbers. Each branch divides a group into parts that do "
        "not overlap, so every number ends in exactly one final category.", None),
    "c08_survey": (
        lambda: F.venn2(300, 140, "\u201cwalks\u201d", "\u201ccycles\u201d", counts=(14, 9, 12, 15)),
        "A survey of 50 students. 14 walk only, 9 both walk and cycle, 12 cycle only and 15 do "
        "neither, so 23 walk and 21 cycle.", None),
})

FIGS.update({
    "c09_triangle": (
        lambda: F.triangle_area(),
        "The height of a triangle is measured perpendicular to the base, not along a side. "
        "The area is half the area of the rectangle with the same base and height.", None),
    "c09_compound": (
        lambda: F.compound_rect(),
        "A compound shape can be split into rectangles, or treated as a large rectangle with a "
        "piece removed. Both methods give the same area.", None),
    "c09_net": (
        lambda: F.net_cuboid(260, 160, ("6 cm", "4 cm", "3 cm")),
        "The net of a cuboid. The surface area is the total area of all six rectangles, and "
        "opposite faces are equal.", None),
    "c09_prism": (
        lambda: F.prism(230, 150, ("l", "w", "h"), ("6 cm", "4 cm", "3 cm")),
        "A cuboid with its three dimensions marked. Volume is length × width × height, and "
        "capacity is measured in litres.", None),
    "c09_units": (
        lambda: F.unit_ladder(),
        "Converting units for length, area and volume: area uses the square of the length factor, "
        "and volume its cube.", None),
})

FIGS.update({
    "c10_bar": (
        lambda: F.bars(["A", "B", "C", "D"], [12, 9, 15, 6], 300, 130, ylab="students"),
        "A bar chart of four categories. The bars are separate because the categories are "
        "labels, not numbers on a continuous scale.", None),
    "c10_hist": (
        lambda: F.hist(["0-", "10-", "20-", "30-", "40-"], [4, 9, 14, 8, 5],
                       320, 120, xlab="time in minutes"),
        "A histogram of grouped data. The bars touch because the groups are intervals on a "
        "continuous scale.", None),
    "c10_freq": (
        lambda: F.frequency_table(),
        "A frequency table records how often each value occurs; the frequencies add to the "
        "number of students surveyed.", None),
    "c10_mislead": (
        lambda: F.misleading_bars(),
        "The same counts drawn on two different scales. The second chart makes small differences "
        "look dramatic, because its axis does not start at zero.", None),
    "c10_dot": (
        lambda: F.dotplot([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6], 1, 6, 320, 70),
        "A dot plot of 13 values. Each dot is one student's result, and repeated values stack "
        "vertically, so the shape of the data is visible.", None),
    "c07_polygon": (
        lambda: F.polygon_diagonals(6),
        "A hexagon split into triangles from one vertex. The diagonals divide it into four "
        "triangles, so its interior angles total 4 × 180° = 720°.",
        None),
    "c09_circle": (
        lambda: F.circle_parts(shade=True, deg=120),
        "The parts of a circle: radius r, diameter d = 2r, circumference C = 2πr and area "
        "A = πr². The shaded sector is a fraction of the whole circle.",
        None),
})
