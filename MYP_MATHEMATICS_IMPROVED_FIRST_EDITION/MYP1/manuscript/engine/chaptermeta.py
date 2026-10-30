"""Unit-planner metadata for the ten MYP1 chapters.

Concepts, global contexts, statements of inquiry and criteria follow the
framework already used in the first edition and have been rewritten for this
improved edition. Learning intentions and success criteria preserve the
mathematical scope of the original chapters.
"""

CHAPTERS = []


def ch(**kw):
    CHAPTERS.append(kw)
    return kw


ch(
    n=1, part=1,
    title="Number systems and place value",
    short="Number systems and place value",
    blurb="Ten digits are enough to write any number we can name. Their power comes "
          "from position: the same symbol can mean seven, seventy or seven thousandths.",
    inquiry="How does a digit's position change its value, and how can we describe that "
            "structure so precisely that comparisons and calculations become reliable?",
    opener_teaser="A museum label reads “about 12,000 objects”. A catalogue entry reads "
                  "“11,846 objects”. Both describe the same collection. This chapter asks "
                  "what each digit contributes, what zero is doing, and when “about” is the "
                  "more honest answer.",
    hours=12,
    concepts=[("KEY CONCEPT", "Form"), ("RELATED", "Quantity"),
              ("RELATED", "Representation"), ("GLOBAL CONTEXT", "Orientation in space and time")],
    concept_blocks=[
        ("KEY CONCEPT · FORM", "Form",
         "A number's written form is not a single symbol but an organised system of positions. "
         "Each position carries a value ten times the position to its right."),
        ("RELATED CONCEPT · QUANTITY", "Quantity",
         "Place value lets a small set of digits represent any magnitude. Rounding records an "
         "appropriate level of precision rather than every last unit."),
        ("RELATED CONCEPT · REPRESENTATION", "Representation",
         "A number may appear as words, digits, an expanded sum, a position on a number line "
         "or a rounded claim. Choosing the form is part of solving the problem."),
    ],
    context="Orientation in space and time",
    context_exploration="How different cultures have recorded quantity, and why the invention "
                        "of a place-value system with a zero changed what numbers could do.",
    factual="What is the value of a digit in a given position? How does multiplying or "
            "dividing by 10 change a number's digits?",
    conceptual="Why is zero essential in a place-value system, and how can one number have "
               "several equivalent representations?",
    debatable="When a number is reported as “about 2,000”, is the result more useful than "
              "the exact count?",
    criteria=[
        ("A · Knowing and understanding", "i, ii, iii",
         "Read, compare, round and rewrite integers and decimals; select sensible placements."),
        ("B · Investigating patterns", "i, ii, iii",
         "Investigate how counting possibilities grow with the number of digits; state and "
         "test a rule."),
        ("C · Communicating", "i, ii, iii, iv",
         "Move between words, digits, expanded form, number lines and rounded statements."),
        ("D · Applying mathematics", "i, ii, iii, iv, v",
         "Choose an appropriate accuracy for a public noticeboard and justify its effect on meaning."),
    ],
    atl_focus="Critical thinking",
    atl="In order for a student to test the claim that adding a zero always multiplies a "
        "number by 10, students must try the claim on a whole number, a decimal and a number "
        "ending in zero, and then revise the claim so that it survives every case.",
    soi="The position of a digit in a base-ten system encodes its value, so a small set of "
        "symbols can represent any magnitude when place and zero are used consistently.",
    soi_intro="Place-value systems are technologies of representation. They make large "
              "quantities manageable, comparisons quick and written calculation possible. The "
              "history of zero is not an optional curiosity: it explains why our written "
              "system can distinguish 305 from 35 and 3.05 without inventing a new symbol "
              "for every value.",
    intentions=[
        "Understand how natural numbers, whole numbers and integers are related.",
        "Know that the value of a digit depends on its place in a base-ten number.",
        "Write whole numbers and decimals in expanded form and return to standard form.",
        "Compare and order integers and decimals using place value and a number line.",
        "Round to a stated place and choose a reasonable level of accuracy in context.",
        "Estimate a result and explain whether the estimate is likely to be too high or too low.",
    ],
    success=[
        "I can classify a number as natural, whole, integer or rational.",
        "I can state the value of any digit in a whole number or decimal and explain the role of zero.",
        "I can write a number in expanded form and reconstruct it accurately.",
        "I can order positive and negative numbers and decimals and justify the order.",
        "I can round to the nearest stated unit or place and avoid an over-precise answer.",
        "I can estimate, compare the estimate with an exact calculation, and explain the difference.",
    ],
    prereq=[
        ("Write “four thousand and sixty” using digits.", "4,060"),
        ("Which is greater, $0.5$ or $0.45$? Explain in one sentence.", "$0.5$, because $0.50 > 0.45$"),
        ("Calculate $8 \\times 7$.", "56"),
        ("What is 100 more than 2,950?", "3,050"),
        ("Write $\\frac{7}{10}$ as a decimal.", "0.7"),
        ("Put $-2$, $0$ and $3$ in order from least to greatest.", "$-2 < 0 < 3$"),
    ],
    prereq_note="Answers are in the Chapter 1 answer section. If more than two are incorrect, "
                "review place value to thousands and simple fractions before continuing.",
    before="Counting, number bonds, place value to thousands and simple fractions of a whole.",
    this="Number families; decimal place value; integer ordering; expanded form; rounding "
         "and estimation.",
    later="Signed-number operations, powers and standard index form; scientific notation; "
          "absolute error.",
    pathway=[("CONTEXT", "Museum labels report collection size and years in different forms."),
             ("QUESTION", "What does each digit in a displayed number actually contribute?"),
             ("CONCEPT", "Base-ten place value, zero as placeholder, precision."),
             ("INVESTIGATION", "Count the possible numbers of different lengths."),
             ("COMMUNICATION", "Expanded form, number lines and justified rounding."),
             ("REFLECTION", "When does extra precision help, and when does it mislead?")],
    content="content/ch01.txt",
)

ch(
    n=2, part=1,
    title="Powers, expanded form and order of operations",
    short="Powers and order of operations",
    blurb="A power is a compressed instruction: it records how many copies of a factor to "
          "multiply. A shared order of operations keeps that compression unambiguous.",
    inquiry="When does a shorter notation make a calculation clearer, and what rules must "
            "everyone share before a compact expression can be read correctly?",
    opener_teaser="A phone advertises 64 GB of storage. A computer reports the same memory "
                  "as 59.6 GB. Both numbers are honest. This chapter explains why a power of "
                  "ten and a power of two can describe the same machine, and why the order in "
                  "which we apply operations changes the answer.",
    hours=14,
    concepts=[("KEY CONCEPT", "Form"), ("RELATED", "Simplification"),
              ("RELATED", "Quantity"), ("GLOBAL CONTEXT", "Scientific and technical innovation")],
    concept_blocks=[
        ("KEY CONCEPT · FORM", "Form",
         "A power has a precise form: a base and an exponent. Changing either part changes "
         "the number, and expanded form and index form are two ways of writing one quantity."),
        ("RELATED CONCEPT · SIMPLIFICATION", "Simplification",
         "Index notation shortens repeated multiplication, while an agreed order of operations "
         "makes a long expression readable in one consistent way."),
        ("RELATED CONCEPT · QUANTITY", "Quantity",
         "Powers of ten and powers of two describe and compare very large quantities such as "
         "storage capacity, distance and population."),
    ],
    context="Scientific and technical innovation",
    context_exploration="How compact notation and agreed calculation rules allow people and "
                        "machines to process quantities far beyond what can be written digit "
                        "by digit.",
    factual="What does $2^{10}$ mean? Which operation is performed first in $6 + 2 \\times 3$? "
            "What is the value of $10^{4}$?",
    conceptual="Why does an exponent of 1 leave the base unchanged? How can $2^{10}$ and "
               "$10^{3}$ be compared fairly? Why is a shared order of operations necessary?",
    debatable="Should a calculator be trusted to decide the meaning of an expression, or "
              "should the person writing it make the meaning visible?",
    criteria=[
        ("A · Knowing and understanding", "i, ii, iii",
         "Evaluate powers, roots and expressions using the agreed order."),
        ("B · Investigating patterns", "i, ii, iii",
         "Investigate doubling from paper folding; generalise the thickness after $n$ folds."),
        ("C · Communicating", "i, ii, iii, iv",
         "Translate between repeated multiplication, index form, expanded form and standard form."),
        ("D · Applying mathematics", "i, ii, iii, iv",
         "Interpret advertised and binary storage measures with justified assumptions."),
    ],
    atl_focus="Transfer",
    atl="In order for a student to decide whether $(a+b)^{2}$ is always $a^{2}+b^{2}$, students "
        "must transfer the substitution method from one pair of values to a second pair, "
        "compare the two results and decide whether a single counterexample settles the claim.",
    soi="Compressing repeated multiplication into a power, and agreeing the order in which "
        "operations apply, allows complex calculations to be recorded compactly and reproduced "
        "reliably.",
    soi_intro="A computer stores information in binary, so its capacity grows by powers of two, "
              "while storage is often advertised in powers of ten. The difference is small at "
              "first and large at scale. The same compact notation that describes a memory chip "
              "also describes the distance to a star.",
    intentions=[
        "Understand a power as repeated multiplication and identify its base and exponent.",
        "Know the place values represented by powers of ten and use them in expanded form.",
        "Recognise square and cube numbers and find square roots of perfect squares.",
        "Apply the order of operations, including brackets and indices.",
        "Substitute values into expressions and formulas containing powers.",
        "Compare quantities written as different powers and justify the comparison.",
    ],
    success=[
        "I can write repeated multiplication using an exponent and expand a power correctly.",
        "I can evaluate powers of whole numbers, including squares and cubes.",
        "I can write a whole number in expanded form using powers of ten and return to standard form.",
        "I can find square roots of perfect squares and explain what the root means.",
        "I can evaluate expressions using brackets, indices, multiplication, division, addition "
        "and subtraction in the agreed order.",
        "I can substitute a value into an expression with a power and explain the meaning of the result.",
    ],
    prereq=[
        ("Calculate $6 \\times 7$ and $9 \\times 9$.", "$42$ and $81$"),
        ("Write $4{,}000 + 500 + 30 + 6$ as a single number.", "4,536"),
        ("Calculate $12 + 3 \\times 4$.", "24"),
        ("Write $3 \\times 3 \\times 3$ as a product and evaluate it.", "27"),
        ("What is the area of a square with side 8 cm?", "64 cm²"),
        ("Insert brackets so that $2 + 4 \\times 3$ has the value 18.", "$(2 + 4) \\times 3$"),
    ],
    prereq_note="Answers are in the Chapter 2 answer section. If more than two are incorrect, "
                "review multiplication facts and the meaning of brackets before continuing.",
    before="Multiplication tables, place value, simple brackets and areas of squares and rectangles.",
    this="Index notation, powers of ten, squares, cubes and roots, order of operations, substitution.",
    later="Negative and fractional indices, standard form, algebraic expansion and sequences.",
    pathway=[("CONTEXT", "Storage, distance and population are reported in compact units."),
             ("QUESTION", "How can repeated multiplication be recorded without losing meaning?"),
             ("CONCEPT", "Base and exponent, powers of ten, inverse roots."),
             ("INVESTIGATION", "Model the thickness of folded paper as a power of two."),
             ("COMMUNICATION", "Move between expanded, index and standard forms."),
             ("REFLECTION", "When does compression clarify a quantity, and when does it hide it?")],
    content="content/ch02.txt",
)

ch(
    n=3, part=1,
    title="Factors, multiples and primes",
    short="Factors, multiples and primes",
    blurb="Every whole number is built from smaller whole numbers. Learning to see that "
          "structure turns division, fair sharing and repeating schedules into questions with "
          "exact answers.",
    inquiry="When is a number best understood by what it is made of, and when does the way we "
            "group things decide whether a division is fair?",
    opener_teaser="A school has 84 Year 7 students, 60 Year 8 students and 48 Year 9 students. "
                  "It wants identical mixed teams with no student left out. The number of teams "
                  "is not a matter of opinion: it must divide all three totals. Arithmetic "
                  "decides what is possible before anyone negotiates.",
    hours=13,
    concepts=[("KEY CONCEPT", "Relationships"), ("RELATED", "System"),
              ("RELATED", "Representation"), ("GLOBAL CONTEXT", "Fairness and development")],
    concept_blocks=[
        ("KEY CONCEPT · RELATIONSHIPS", "Relationships",
         "Factors and multiples describe how whole numbers are connected: one number divides "
         "another exactly, or two numbers share a common structure."),
        ("RELATED CONCEPT · SYSTEM", "System",
         "The primes are building blocks: every whole number greater than 1 is assembled from "
         "them in exactly one way, apart from order."),
        ("RELATED CONCEPT · REPRESENTATION", "Representation",
         "Factor trees, index notation and Venn diagrams display the same factorisation in "
         "different forms."),
    ],
    context="Fairness and development",
    context_exploration="How number structure shapes fair division, shared timetables and the "
                        "allocation of resources.",
    factual="What is a factor of 36? What is a multiple of 7? Which numbers below 100 are prime?",
    conceptual="Why is 1 neither prime nor composite? Why is every prime factorisation unique? "
               "How are HCF and LCM related?",
    debatable="Is a number with many factors more useful than a prime number, or does usefulness "
              "depend entirely on the problem?",
    criteria=[
        ("A · Knowing and understanding", "i, ii, iii",
         "Find factors and multiples, apply divisibility tests, identify primes, calculate "
         "HCF and LCM."),
        ("B · Investigating patterns", "i, ii, iii",
         "Investigate how many factors a number has; generalise why squares have an odd number "
         "of factors."),
        ("C · Communicating", "i, ii, iii, iv",
         "Represent factorisations with trees, index notation and diagrams, using correct vocabulary."),
        ("D · Applying mathematics", "i, ii, iii, iv",
         "Solve grouping and scheduling problems, justify assumptions and evaluate the fairness "
         "of a plan."),
    ],
    atl_focus="Critical thinking",
    atl="In order for a student to judge the claim that every number with a 3 in it is divisible "
        "by 3, students must test it on numbers that support it and on numbers that refute it, "
        "then replace the claim with a test that looks at the digit sum.",
    soi="Whole numbers are built from factors in a structured way, and that structure makes it "
        "possible to divide quantities fairly, schedule repeating events and communicate precisely.",
    soi_intro="A school cannot make identical mixed teams from 84, 60 and 48 students unless the "
              "number of teams divides all three. Two bells ring together only at common "
              "multiples. Arithmetic decides what is possible before anyone negotiates.",
    intentions=[
        "Understand the relationship between factors and multiples, and list factor pairs systematically.",
        "Know the divisibility tests for 2, 3, 4, 5, 6, 8, 9 and 10 and explain how they work.",
        "Classify numbers as prime, composite or neither, and test whether a number is prime.",
        "Write any composite number as a product of primes using a factor tree or division.",
        "Find the highest common factor and lowest common multiple of two or three numbers.",
        "Choose and justify HCF or LCM in sharing and scheduling contexts.",
    ],
    success=[
        "I can list all factors of a number without missing any, using factor pairs.",
        "I can explain the difference between a factor and a multiple with examples.",
        "I can decide whether a number is divisible by 2, 3, 4, 5, 6, 8, 9 or 10 and give evidence.",
        "I can identify prime numbers and explain why 1 is excluded.",
        "I can write a prime factorisation in index form and reconstruct the number from it.",
        "I can calculate HCF and LCM and explain which one a context requires.",
    ],
    prereq=[
        ("Calculate $7 \\times 8$ and $9 \\times 6$.", "$56$ and $54$"),
        ("Divide 96 by 8.", "12"),
        ("List the first five multiples of 4.", "4, 8, 12, 16, 20"),
        ("Write 100 as a product of two equal factors.", "$10 \\times 10$"),
        ("Which is larger, $3^{3}$ or $4^{2}$?", "$3^{3} = 27$"),
        ("Is 56 in the 7 times table? Explain how you know.", "Yes, $7 \\times 8 = 56$"),
    ],
    prereq_note="Answers are in the Chapter 3 answer section. If more than two are incorrect, "
                "review multiplication and division facts before continuing.",
    before="Multiplication tables, division facts and simple fractions of amounts.",
    this="Factor pairs, divisibility, primes, prime factorisation, HCF and LCM.",
    later="Laws of indices, algebraic factorisation, number theory and cryptography.",
    pathway=[("CONTEXT", "Groups, timetables and shared resources must divide exactly."),
             ("QUESTION", "What smaller numbers build a given whole number?"),
             ("CONCEPT", "Factors, multiples, primes and common structure."),
             ("INVESTIGATION", "Count the factors of the numbers 1 to 30 and explain the pattern."),
             ("COMMUNICATION", "Represent factorisations as trees, index products and diagrams."),
             ("REFLECTION", "When does the largest common group produce the fairest result?")],
    content="content/ch03.txt",
)

ch(
    n=4, part=2,
    title="Fractions and decimals",
    short="Fractions and decimals",
    blurb="A fraction and a decimal can name the same point on a number line. Learning to move "
          "between forms makes it easier to compare quantities, calculate and judge how precise "
          "an answer really is.",
    inquiry="When two numbers look different but describe the same amount, how do we choose the "
            "form that is easiest to compare, calculate with or trust?",
    opener_teaser="A 3/8 inch drill bit and a 0.375 inch drill bit are the same size. A "
                  "laboratory that records one third of a litre as 0.33 litres has changed the "
                  "quantity slightly. In measurement, the form of a number carries information "
                  "about precision.",
    hours=16,
    concepts=[("KEY CONCEPT", "Relationships"), ("RELATED", "Equivalence"),
              ("RELATED", "Representation"), ("GLOBAL CONTEXT", "Scientific and technical innovation")],
    concept_blocks=[
        ("KEY CONCEPT · RELATIONSHIPS", "Relationships",
         "A fraction records a relationship between part and whole: the denominator sets the "
         "part size, the numerator counts parts."),
        ("RELATED CONCEPT · EQUIVALENCE", "Equivalence",
         "Different fractions and decimals can name the same number, so a calculation can be "
         "rewritten in a convenient form."),
        ("RELATED CONCEPT · REPRESENTATION", "Representation",
         "A number line, an area diagram, a fraction and a decimal make different features "
         "visible; the form should serve the task."),
    ],
    context="Scientific and technical innovation",
    context_exploration="Precision and measurement: how the way a quantity is recorded affects "
                        "comparison, calculation and trust in a result.",
    factual="What is an equivalent fraction? What does each digit after a decimal point "
            "represent? How can a fraction be written as a decimal?",
    conceptual="Why do different fractions name the same number? How does the form of a number "
               "influence the calculation you choose?",
    debatable="Is a fraction always a more exact record of a quantity than a decimal?",
    criteria=[
        ("A · Knowing and understanding", "i, ii, iii",
         "Generate equivalent fractions, order fractions, calculate with fractions and decimals, "
         "round decimals."),
        ("B · Investigating patterns", "i, ii",
         "Investigate which fractions produce terminating decimals and generalise from the "
         "prime factors of denominators."),
        ("C · Communicating", "i, ii, iii",
         "Explain equivalence and method choice, use number lines and diagrams, record results "
         "with suitable notation."),
        ("D · Applying mathematics", "i, ii, iii, iv",
         "Scale recipes, compare measurements, justify the choice of fraction or decimal and "
         "evaluate the effect of rounding."),
    ],
    atl_focus="Transfer",
    atl="In order for a student to decide whether a recipe scaled for 4 or for 15 should be "
        "recorded in fractions or decimals, students must transfer the same scaling method to "
        "an awkward quantity such as $\\frac{4}{9}$ of a cup and compare which record a cook and "
        "a supplier could act on.",
    soi="The same quantity can be represented in equivalent forms, and choosing an appropriate "
        "form improves the precision of comparison, calculation and communication.",
    soi_intro="A fraction and a decimal are two records of one point on the number line. "
              "Choosing between them is not a matter of taste: the choice decides what can be "
              "seen, what cancels neatly and how much precision the reader is being offered.",
    intentions=[
        "Understand equivalent fractions and write a fraction in simplest form.",
        "Compare and order fractions using common denominators, benchmarks or decimals.",
        "Add and subtract fractions, including mixed numbers.",
        "Multiply and divide fractions and interpret both operations.",
        "Know decimal place value to thousandths, and order, round and calculate with decimals.",
        "Convert between fractions and decimals and explain which decimals terminate.",
    ],
    success=[
        "I can generate equivalent fractions and simplify using a common factor.",
        "I can compare and order fractions with unlike denominators and justify my method.",
        "I can add and subtract fractions and mixed numbers, regrouping when needed.",
        "I can multiply and divide fractions, using the reciprocal correctly.",
        "I can read, order, round and calculate with decimals to thousandths.",
        "I can convert between fractions and decimals and explain which decimals terminate.",
    ],
    prereq=[
        ("Shade $\\frac{3}{4}$ of a rectangle divided into 8 equal parts.", "6 of the 8 parts"),
        ("Write 0.5 and 0.25 as fractions in simplest form.", "$\\frac{1}{2}$ and $\\frac{1}{4}$"),
        ("Find $\\frac{1}{2}$ of 20.", "10"),
        ("Which is larger, $\\frac{3}{4}$ or $\\frac{3}{8}$?", "$\\frac{3}{4}$"),
        ("Calculate $\\frac{1}{4} + \\frac{1}{4}$.", "$\\frac{1}{2}$"),
        ("Write “seven tenths” as a decimal and as a fraction.", "$0.7 = \\frac{7}{10}$"),
    ],
    prereq_note="Answers are in the Chapter 4 answer section. If more than two are incorrect, "
                "review simple equivalent fractions and decimal tenths before continuing.",
    before="Halves, quarters and tenths; simple fractions of shapes and amounts; decimal notation "
           "to hundredths.",
    this="Equivalence, ordering, the four operations with fractions, decimal place value and "
         "fraction–decimal links.",
    later="Percentages, ratio and proportion, rational expressions and algebraic fractions.",
    pathway=[("CONTEXT", "Recipes, measurements and shared quantities rarely arrive as whole numbers."),
             ("QUESTION", "How can different-looking numbers describe exactly the same amount?"),
             ("CONCEPT", "Equivalence, representation and precision."),
             ("INVESTIGATION", "Which fractions produce terminating decimals, and how can "
                               "denominators predict it?"),
             ("COMMUNICATION", "Number lines, fraction diagrams and decimal notation."),
             ("REFLECTION", "When is an exact fraction more useful than a rounded decimal?")],
    content="content/ch04.txt",
)

ch(
    n=5, part=2,
    title="Percentages and applications",
    short="Percentages and applications",
    blurb="A percentage compares a quantity with 100. Once a price, a budget or a change is "
          "written on that scale, very different quantities can be judged side by side — "
          "provided we ask what the percentage is of.",
    inquiry="When a shop advertises “20% off”, what exactly is being reduced, and how can a "
            "buyer tell whether the offer is genuinely good?",
    opener_teaser="A 30% discount on a 20-unit item saves 6 units; the same 30% on a 200-unit "
                  "item saves 60. The percentage is identical, but the effect on a household is "
                  "not. Reading the base is part of reading the offer honestly.",
    hours=14,
    concepts=[("KEY CONCEPT", "Change"), ("RELATED", "Quantity"),
              ("RELATED", "Proportion"), ("GLOBAL CONTEXT", "Fairness and development")],
    concept_blocks=[
        ("KEY CONCEPT · CHANGE", "Change",
         "A percentage describes a change or a part relative to a base; the same absolute "
         "change is a different percentage when the base changes."),
        ("RELATED CONCEPT · QUANTITY", "Quantity",
         "A percentage is not an amount until it is applied to something. 20% of 50 and 20% "
         "of 80 are the same proportion but not the same money."),
        ("RELATED CONCEPT · PROPORTION", "Proportion",
         "Percentages compare a part with a whole scaled to 100, linking fractions, decimals "
         "and ratio."),
    ],
    context="Fairness and development",
    context_exploration="Financial decisions and access: how percentage claims in prices, taxes "
                        "and budgets shape what people can afford, and whether an offer is fair.",
    factual="What does per cent mean? How do you convert between percentages, fractions and "
            "decimals? How do you find a percentage of a quantity?",
    conceptual="How can the same percentage produce different amounts, and why do successive "
               "changes not add?",
    debatable="Is a larger percentage discount always the better deal? Should a budget be judged "
              "by its percentages or by its amounts?",
    criteria=[
        ("A · Knowing and understanding", "i, ii, iii",
         "Convert between forms, calculate a percentage of a quantity, increase and decrease "
         "amounts, calculate discounts and taxes."),
        ("B · Investigating patterns", "i, ii",
         "Investigate successive percentage changes, record multipliers and generalise an "
         "equivalent single change."),
        ("C · Communicating", "i, ii, iii",
         "Explain the choice of base and method, represent percentages with grids and bars, "
         "justify a financial claim."),
        ("D · Applying mathematics", "i, ii, iii, iv",
         "Price a stall, compare offers, build a budget, evaluate rounding and recommend a "
         "course of action."),
    ],
    atl_focus="Critical thinking",
    atl="In order for a student to compare “20% off, then an extra 10% at the till” with “30% "
        "off”, students must decide on a method before calculating, test it on two different "
        "prices and explain why the two claims are not the same.",
    soi="Percentages express change and comparison on a common scale of 100, and interpreting "
        "the base and the multiplier determines whether a financial claim is understood or misleading.",
    soi_intro="The word itself is the definition: per centum, by the hundred. A percentage is a "
              "fraction with a denominator of 100. That single idea connects a discount, a tax "
              "rate, a survey result and a test score — and it is the idea that makes it possible "
              "to compare quantities of very different sizes.",
    intentions=[
        "Understand per cent as a proportion of 100 and convert between percentages, fractions "
        "and decimals.",
        "Find a percentage of a quantity using benchmarks and multipliers.",
        "Increase and decrease quantities by a percentage and explain the multiplier.",
        "Use percentages in discounts, sale prices, taxes and budgets.",
        "Compare offers and justify a financial decision with evidence.",
        "Investigate what happens when two percentage changes are applied one after the other.",
    ],
    success=[
        "I can convert between percentages, fractions and decimals.",
        "I can find a percentage of a quantity and choose an efficient method.",
        "I can increase or decrease a quantity by a percentage using a multiplier.",
        "I can calculate a discount, a sale price and a price including tax.",
        "I can build and interpret a simple budget using percentages.",
        "I can compare two offers and explain which is better and why.",
    ],
    prereq=[
        ("Write $\\frac{3}{4}$ as a decimal.", "0.75"),
        ("Find $\\frac{1}{10}$ of 80.", "8"),
        ("Calculate $0.2 \\times 150$.", "30"),
        ("Write $\\frac{45}{100}$ in simplest form.", "$\\frac{9}{20}$"),
        ("Increase 50 by 10.", "60"),
        ("Which is larger, 0.6 or 0.06?", "0.6"),
    ],
    prereq_note="Answers are in the Chapter 5 answer section. If more than two are incorrect, "
                "review fraction–decimal conversion and finding a fraction of an amount before "
                "continuing.",
    before="Fractions and decimals; finding a fraction of an amount; simple money calculations "
           "and comparisons.",
    this="Percent as per hundred, conversions, percentage of a quantity, increase and decrease, "
         "discounts, tax and budgets.",
    later="Ratio and proportion, repeated and compound change, interest, and percentages in "
          "statistics.",
    pathway=[("CONTEXT", "Offers, taxes and household budgets are written as percentages of something."),
             ("QUESTION", "What is the percentage of, and does the claim tell the whole story?"),
             ("CONCEPT", "Change, quantity and proportion."),
             ("INVESTIGATION", "Do two successive discounts add up to one larger discount?"),
             ("COMMUNICATION", "Hundred grids, bar models, multipliers and clear financial statements."),
             ("REFLECTION", "When is a percentage the honest way to describe a change?")],
    content="content/ch05.txt",
)

ch(
    n=6, part=3,
    title="Patterns, expressions and equations",
    short="Patterns, expressions and equations",
    blurb="Algebra begins by noticing what stays the same while something else changes. A "
          "pattern can be shown in shapes, written in a table, described in words and compressed "
          "into a rule — and an equation lets us work backwards from a result to the unknown.",
    inquiry="A tiled border grows by the same number of tiles at every step. How can you predict "
            "the hundredth stage without drawing it, and how can you find which stage uses "
            "exactly 100 tiles?",
    opener_teaser="A square pond of side $n$ metres needs a one-slab border counted by "
                  "$4n + 4$. The rule lets a builder order slabs without drawing the plan; an "
                  "equation reverses the count when the delivery contains only 96 slabs.",
    hours=16,
    concepts=[("KEY CONCEPT", "Relationships"), ("RELATED", "Patterns"),
              ("RELATED", "Equivalence"), ("GLOBAL CONTEXT", "Scientific and technical innovation")],
    concept_blocks=[
        ("KEY CONCEPT · RELATIONSHIPS", "Relationships",
         "A pattern relates a position to a value. An equation states that two expressions "
         "name the same number, so a solution can be checked by substitution."),
        ("RELATED CONCEPT · PATTERNS", "Patterns",
         "Regular change can be described, continued and predicted. The step and the starting "
         "value together determine the rule."),
        ("RELATED CONCEPT · EQUIVALENCE", "Equivalence",
         "Expressions may look different and still be equal for every value of the variable. "
         "Collecting like terms and expanding rewrite an expression without changing its value."),
    ],
    context="Scientific and technical innovation",
    context_exploration="How systems and patterns work: using rules to model growth, cost and "
                        "design in construction.",
    factual="What is a variable, a term and a coefficient? How do you substitute a value? What "
            "separates an expression from an equation?",
    conceptual="How can different-looking expressions always be equal, and what does it mean to "
               "solve an equation?",
    debatable="Is a rule guessed from several terms trustworthy? When is a formula more useful "
              "than a table of values?",
    criteria=[
        ("A · Knowing and understanding", "i, ii, iii",
         "Continue and generalise sequences, write and simplify expressions, substitute values, "
         "solve one- and two-step equations."),
        ("B · Investigating patterns", "i, ii",
         "Investigate a matchstick chain, record counts in a table, justify the general rule and "
         "test it against a claim."),
        ("C · Communicating", "i, ii, iii",
         "Move between diagram, table, words and symbols; explain each step in a solution; "
         "justify that two expressions are equivalent."),
        ("D · Applying mathematics", "i, ii, iii, iv",
         "Model a courtyard border and a service charge, solve design equations, evaluate a "
         "budget and recommend a size."),
    ],
    atl_focus="Critical thinking",
    atl="In order for a student to explain the sequence 4, 7, 10, 13 in two different ways, "
        "students must compare “add 3 each time” with $3n + 1$, use both descriptions to find "
        "the 40th term and state what each description can and cannot predict.",
    soi="Patterns follow algebraic rules, and equivalent expressions and equations let us "
        "predict later stages and recover unknown values.",
    soi_intro="Algebra begins with a question that arithmetic cannot answer comfortably: what "
              "stays the same while something else changes? Once that is written as a rule, a "
              "table of twenty cases becomes one line, and a question about the hundredth case "
              "becomes a calculation.",
    intentions=[
        "Understand how a sequence is built from a position and a rule, and distinguish "
        "term-to-term from position-to-term descriptions.",
        "Write, interpret and substitute into algebraic expressions.",
        "Collect like terms and expand a single bracket.",
        "Form and solve one- and two-step equations, and check the solution.",
        "Use a formula that links quantities in a context.",
        "Investigate a growing matchstick pattern and justify a general rule.",
    ],
    success=[
        "I can continue a sequence and explain the rule in words.",
        "I can find a position-to-term rule and use it for a distant term.",
        "I can write and evaluate expressions, including with negative values.",
        "I can simplify expressions by collecting like terms and expanding brackets.",
        "I can solve linear equations and check my answer by substitution.",
        "I can form an equation from a context and interpret the solution.",
    ],
    prereq=[
        ("Calculate $6 \\times 7$.", "42"),
        ("Calculate $20 - 3 \\times 4$.", "8"),
        ("Write $5 + 5 + 5 + 5$ as a multiplication.", "$4 \\times 5$"),
        ("Find the next two terms of 2, 5, 8, 11, …", "14, 17"),
        ("Calculate $3 \\times 4 + 2$.", "14"),
        ("Solve $6 + \\square = 15$.", "$\\square = 9$"),
    ],
    prereq_note="Answers are in the Chapter 6 answer section. If more than two are incorrect, "
                "review multiplication facts, order of operations and simple missing-number "
                "sentences before continuing.",
    before="Number patterns, missing-number sentences, multiplication facts and the order of operations.",
    this="Sequences and rules, expressions, substitution, simplifying, expanding, equations and "
         "formulas.",
    later="Linear graphs, simultaneous equations, inequalities, quadratic expressions and "
          "algebraic proof.",
    pathway=[("CONTEXT", "Borders, chains and service charges grow by a regular rule."),
             ("QUESTION", "How can one rule describe every stage, and how can we reverse it?"),
             ("CONCEPT", "Relationships, pattern and equivalence."),
             ("INVESTIGATION", "How many matches make a chain of $n$ squares?"),
             ("COMMUNICATION", "Diagrams, tables, words, expressions and balanced equations."),
             ("REFLECTION", "When does a pattern count as explained rather than merely continued?")],
    content="content/ch06.txt",
)

ch(
    n=7, part=4,
    title="Lines, angles, triangles and constructions",
    short="Lines, angles and constructions",
    blurb="A single straight line contains 180°, and a full turn contains 360°. From those two "
          "facts, and one statement about parallel lines, an entire system of shape reasoning "
          "follows. Constructions turn that reasoning into a repeatable physical procedure.",
    inquiry="A workshop needs a triangular roof truss with equal slopes and a horizontal collar "
            "beam. Which angles must the carpenter set, how can the shape be checked without "
            "measuring every angle, and how can a full-size template be reproduced exactly?",
    opener_teaser="A roof truss is a triangle of timbers. Equal base angles make the slopes "
                  "symmetrical; a parallel collar creates equal angles; a perpendicular from the "
                  "apex locates the centre. None of these facts needs measuring if the geometry "
                  "is right.",
    hours=16,
    concepts=[("KEY CONCEPT", "Relationships"), ("RELATED", "Space"),
              ("RELATED", "Measurement"), ("GLOBAL CONTEXT", "Orientation in space and time")],
    concept_blocks=[
        ("KEY CONCEPT · RELATIONSHIPS", "Relationships",
         "Angles are related by position: on a line, at a point, between parallel lines, in "
         "triangles and in polygons."),
        ("RELATED CONCEPT · SPACE", "Space",
         "Lines, angles and shapes describe how parts of a structure fit together. A "
         "construction locates a point using distance, not guesswork."),
        ("RELATED CONCEPT · MEASUREMENT", "Measurement",
         "Degrees measure turn. A construction enforces an exact relationship by repeating a "
         "radius; a measuring instrument only approximates."),
    ],
    context="Orientation in space and time",
    context_exploration="How spatial relationships and precise construction allow structures to "
                        "be designed, checked and reproduced.",
    factual="What is an angle, and how is it measured? Which angle facts hold on a line, at a "
            "point and between parallel lines?",
    conceptual="Why is the angle sum of a triangle fixed even when the triangle changes? How "
               "does a construction guarantee a result that measurement can only approximate?",
    debatable="When is an exact construction more trustworthy than a careful measurement? Should "
              "a design follow the standard construction or adapt to the materials available?",
    criteria=[
        ("A · Knowing and understanding", "i, ii, iii",
         "Apply angle facts on lines, at points, between parallel lines, in triangles and in "
         "polygons; classify triangles; describe constructions accurately."),
        ("B · Investigating patterns", "i, ii",
         "Test sets of three lengths, record whether a triangle is possible, conjecture and "
         "justify the triangle inequality."),
        ("C · Communicating", "i, ii, iii",
         "Name angles and lines correctly, label diagrams, and write reasoned angle chains and "
         "construction steps."),
        ("D · Applying mathematics", "i, ii, iii, iv",
         "Design and check a roof truss, use scale and construction constraints, and evaluate a "
         "template."),
    ],
    atl_focus="Thinking skills",
    atl="In order for a student to explain why two measured angle sums of 179° and 181° do not "
        "refute the triangle angle sum, students must distinguish a measurement from a "
        "deduction and name one procedure that would reduce the variation.",
    soi="Spatial relationships obey angle and shape rules, and precise constructions let those "
        "rules be checked and reproduced in real structures.",
    soi_intro="One fact generates a system. If a straight line holds 180°, then angles at a "
              "point hold 360°, a triangle holds 180°, and every polygon angle sum follows. "
              "Geometry is the study of what must be true, not what happens to look true in one "
              "drawing.",
    intentions=[
        "Understand how angles are named and measured, and why angle facts on a line and at a "
        "point must be true.",
        "Calculate angles between parallel lines, in triangles and in polygons, giving a reason "
        "at each step.",
        "Classify triangles by sides and angles and use the exterior angle relationship.",
        "Construct a perpendicular bisector, an angle bisector and a triangle from three side lengths.",
        "Know the triangle inequality and use it to decide whether a construction is possible.",
        "Investigate which triples of lengths form a triangle and justify the general condition.",
    ],
    success=[
        "I can name and classify an angle using correct notation.",
        "I can find missing angles on a straight line, at a point and between parallel lines, "
        "with reasons.",
        "I can use the triangle and polygon angle sums to solve problems.",
        "I can explain why a construction produces the required point or line.",
        "I can decide whether three lengths can form a triangle.",
        "I can produce a clear scale drawing and evaluate its accuracy.",
    ],
    prereq=[
        ("Solve $x + 40 = 180$.", "$x = 140$"),
        ("Calculate $180 - 65$.", "115"),
        ("Solve $3x = 180$.", "$x = 60$"),
        ("Name a triangle with two equal sides.", "Isosceles"),
        ("How many degrees are in a quarter turn?", "90°"),
        ("Calculate $2 \\times (180 - 70)$.", "220"),
    ],
    prereq_note="Answers are in the Chapter 7 answer section. If more than two are incorrect, "
                "review angle measurement, solving one-step equations and the names of common "
                "triangles before continuing.",
    before="Recognising and measuring angles with a protractor; naming triangles and "
           "quadrilaterals; simple angle sums.",
    this="Angle facts with reasons; parallel lines; triangle and polygon sums; ruler-and-compass "
         "constructions; triangle inequality.",
    later="Congruence and similarity, Pythagoras' theorem, circle theorems, trigonometric ratios "
          "and geometric proof.",
    pathway=[("CONTEXT", "Roofs, ramps and frames are built from straight lines and triangles."),
             ("QUESTION", "Which angles are forced once one angle is known, and when can a shape "
                          "be built at all?"),
             ("CONCEPT", "Relationships, space and measurement."),
             ("INVESTIGATION", "Which triples of lengths can make a triangle?"),
             ("COMMUNICATION", "Labelled diagrams, angle chains with reasons, and construction "
                               "instructions."),
             ("REFLECTION", "When does a drawing prove a relationship, and when does it only "
                            "suggest one?")],
    content="content/ch07.txt",
)

ch(
    n=8, part=4,
    title="Sets and classification",
    short="Sets and classification",
    blurb="A set is a collection described by a rule. Once the rule is precise, belonging can "
          "be tested, overlap can be counted and a decision can be defended. Sets give "
          "classification a language and a diagram.",
    inquiry="A community centre offers two activity programmes. Some members use only one, some "
            "use both and some use neither. How can the centre record this fairly, count each "
            "group without double-counting, and decide what a combined membership should include?",
    opener_teaser="A centre must know how many members use each programme, how many use both and "
                  "how many use neither. Counting the overlap twice would overstate demand; "
                  "ignoring it would understate it. Both errors cost money and both are avoidable.",
    hours=14,
    concepts=[("KEY CONCEPT", "Form"), ("RELATED", "Representation"),
              ("RELATED", "Systems"), ("GLOBAL CONTEXT", "Fairness and development")],
    concept_blocks=[
        ("KEY CONCEPT · FORM", "Form",
         "A set is defined by the property its elements share. The form of the definition "
         "determines which objects belong and which do not."),
        ("RELATED CONCEPT · REPRESENTATION", "Representation",
         "Roster notation, set-builder notation and Venn diagrams represent the same collection "
         "in different ways. Each makes a different feature visible."),
        ("RELATED CONCEPT · SYSTEMS", "Systems",
         "Number sets form a nested system. Each larger set contains the smaller ones and adds "
         "new possibilities."),
    ],
    context="Fairness and development",
    context_exploration="How clear classification and accurate counting support fair access to "
                        "shared resources.",
    factual="What is a set, and how are its elements and subsets written? What do union, "
            "intersection and complement mean?",
    conceptual="How can one collection be represented by a list, a rule and a diagram? Why does "
               "the overlap need special treatment when groups are combined?",
    debatable="When does a classification system help a decision, and when does it exclude "
              "people unfairly? Should a shared service be priced by use or by membership?",
    criteria=[
        ("A · Knowing and understanding", "i, ii, iii",
         "Use set notation, identify subsets, classify numbers and calculate counts from Venn "
         "diagrams."),
        ("B · Investigating patterns", "i, ii",
         "Investigate how overlap constrains the possible counts in a survey, and generalise "
         "the addition rule."),
        ("C · Communicating", "i, ii, iii",
         "Represent sets by roster, rule and diagram; label a universal set; justify a count in words."),
        ("D · Applying mathematics", "i, ii, iii, iv",
         "Audit a membership scheme, interpret survey data transparently, and evaluate a "
         "classification guide."),
    ],
    atl_focus="Thinking skills",
    atl="In order for a student to explain how two students can count 42 and 28 uses from the "
        "same 30 classmates, students must distinguish a count of uses from a count of people "
        "and name the information missing from the total.",
    soi="Precise classification reveals relationships between groups, and accurate set reasoning "
        "supports fair decisions about shared resources.",
    soi_intro="Classification is a mathematical act. The moment a centre writes “member of the "
              "music programme”, it has defined a set, and every later count depends on how "
              "carefully that definition was written. Sets make the definition visible and the "
              "counting checkable.",
    intentions=[
        "Understand sets as collections defined by a property, and use element and subset "
        "notation correctly.",
        "Represent a set by roster, set-builder notation and a Venn diagram.",
        "Find unions, intersections, complements and differences of sets.",
        "Know how the number sets $\\mathbb{N}$, $\\mathbb{Z}$, $\\mathbb{Q}$ and $\\mathbb{R}$ are related.",
        "Use the addition rule to count overlapping groups without double-counting.",
        "Investigate how the overlap between two groups is constrained by the total surveyed.",
    ],
    success=[
        "I can list the elements of a set and state its cardinality.",
        "I can decide whether one set is a subset of another.",
        "I can read and draw a two-set Venn diagram with a universal set.",
        "I can calculate $n(A \\cup B)$, $n(A \\cap B)$ and $n(A')$.",
        "I can classify a number into the correct number sets.",
        "I can solve a two-group survey problem and explain each count.",
    ],
    prereq=[
        ("List the first five even numbers greater than zero.", "2, 4, 6, 8, 10"),
        ("Write 0.75 as a fraction in its simplest form.", "$\\frac{3}{4}$"),
        ("Calculate $18 + 14 - 6$.", "26"),
        ("Which is greater, $-4$ or $-9$?", "−4"),
        ("Write two multiples of 3 that are less than 10.", "3 and 6 (or 9)"),
        ("Calculate $10 - 3 - 2$.", "5"),
    ],
    prereq_note="Answers are in the Chapter 8 answer section. If more than two are incorrect, "
                "review factors and multiples, fraction equivalence and subtraction with "
                "compensation before continuing.",
    before="Sorting objects by one or two properties; using tables and simple lists; recognising "
           "odd, even, prime and square numbers.",
    this="Set notation and subsets; Venn diagrams; union, intersection and complement; number "
         "sets; two-group survey reasoning.",
    later="Three-set Venn diagrams, set algebra, logic and truth tables, probability using sets, "
          "and functions defined on number sets.",
    pathway=[("CONTEXT", "A community centre records who uses which activity programme."),
             ("QUESTION", "How can overlapping groups be counted once each, and what does "
                          "“neither” mean?"),
             ("CONCEPT", "Form, representation and systems."),
             ("INVESTIGATION", "How much overlap is possible when two totals and the overall "
                               "total are known?"),
             ("COMMUNICATION", "Roster lists, set-builder rules, labelled Venn diagrams and "
                               "count statements."),
             ("REFLECTION", "When does a neat classification clarify a decision, and when does "
                            "it hide an exception?")],
    content="content/ch08.txt",
)

ch(
    n=9, part=4,
    title="Perimeter, area, surface area and volume",
    short="Perimeter, area and volume",
    blurb="A boundary has length, a surface has area and a solid encloses space. Each quantity "
          "needs its own formula, its own unit and its own check. Measuring well is therefore as "
          "much about choosing the right question as about calculating accurately.",
    inquiry="A community centre is redesigning its courtyard. It must buy turf for the lawn, "
            "paving for a semicircular stage, fencing for the boundary, soil for three raised "
            "beds and paint for their outsides. Which measurements does each purchase require, "
            "and how can the centre avoid paying for material it does not need?",
    opener_teaser="A courtyard, a carton and a water tank raise the same question: how much "
                  "material is needed for the surface, and how much space is available inside? "
                  "Accurate measurement reduces waste; the wrong quantity wastes money as well.",
    hours=16,
    concepts=[("KEY CONCEPT", "Form"), ("RELATED", "Measurement"),
              ("RELATED", "Space"), ("GLOBAL CONTEXT", "Globalization and sustainability")],
    concept_blocks=[
        ("KEY CONCEPT · FORM", "Form",
         "The shape of an object determines which measurements are needed and how they "
         "combine. A rectangle, a prism and a composite courtyard each have a different form."),
        ("RELATED CONCEPT · MEASUREMENT", "Measurement",
         "Length, area and volume are different quantities; the unit records which one has "
         "been measured."),
        ("RELATED CONCEPT · SPACE", "Space",
         "Decomposing a shape into familiar parts turns an unfamiliar space into a calculation "
         "that can be checked."),
    ],
    context="Globalization and sustainability",
    context_exploration="How measurement supports responsible decisions about materials, "
                        "packaging, land and water.",
    factual="What is the difference between perimeter, area, surface area and volume? Which "
            "units are appropriate for each?",
    conceptual="Why does doubling every dimension multiply volume by eight but surface area by "
               "only four? How does decomposition simplify an unfamiliar shape?",
    debatable="Should packaging use the least material even when the result is less attractive? "
              "Who pays for unnecessary packaging — buyer, seller or environment?",
    criteria=[
        ("A · Knowing and understanding", "i, ii, iii",
         "Select and use measurement formulas; convert units correctly; classify measurements "
         "by dimension."),
        ("B · Investigating patterns", "i, ii",
         "Compare the surface areas of cuboids with the same volume, record the pattern and "
         "justify a conjecture."),
        ("C · Communicating", "i, ii, iii",
         "Label diagrams with dimensions and units, show the decomposition of composite shapes, "
         "and explain each step of a calculation."),
        ("D · Applying mathematics", "i, ii, iii, iv",
         "Cost a courtyard project, decide quantities of turf, soil and paint, and evaluate a "
         "storage-crate design."),
    ],
    atl_focus="Research skills",
    atl="In order for a student to compare two paint tins fairly, students must find the "
        "coverage, the number of coats, the price per litre and the area to be covered, then "
        "justify the comparison with the quantities rather than the price alone.",
    soi="Form determines how length, area and volume are measured, and measuring accurately "
        "supports responsible use of materials and space.",
    soi_intro="A boundary is one-dimensional, a surface is two-dimensional and a solid is "
              "three-dimensional. That single sentence explains why fencing is bought in metres, "
              "turf in square metres and soil in cubic metres — and why using the wrong unit is "
              "not a small slip but a different question.",
    intentions=[
        "Understand why perimeter, area, surface area and volume are different quantities with "
        "different units.",
        "Calculate the perimeter and area of rectangles, triangles, parallelograms, trapeziums "
        "and circles.",
        "Break a composite shape into familiar parts and combine the results.",
        "Draw and interpret nets, and calculate the surface area of cuboids and triangular prisms.",
        "Calculate the volume of prisms and convert between cubic units, millilitres and litres.",
        "Investigate how the shape of a cuboid affects its surface area when the volume is fixed.",
    ],
    success=[
        "I can name the quantity being measured and state its unit.",
        "I can choose the correct formula and substitute the perpendicular dimensions.",
        "I can decompose a composite shape and account for every boundary edge.",
        "I can calculate surface area from a net or from a formula.",
        "I can calculate volume and convert capacity units accurately.",
        "I can evaluate a measurement-based design against a budget and a constraint.",
    ],
    prereq=[
        ("Calculate $14 \\times 6$.", "84"),
        ("Convert 2.4 m to centimetres.", "240 cm"),
        ("Calculate $0.5 \\times 10 \\times 7$.", "35"),
        ("Calculate $3.14 \\times 4$.", "12.56"),
        ("Calculate $3^{2} + 4^{2}$.", "25"),
        ("Calculate $1000 \\div 8$.", "125"),
    ],
    prereq_note="Answers are in the Chapter 9 answer section. If more than two are incorrect, "
                "review multiplication of decimals, metric length conversions and the meaning of "
                "square units before continuing.",
    before="Perimeter and area of rectangles and squares; naming common 2D and 3D shapes; simple "
           "metric conversions.",
    this="Area of triangles, parallelograms, trapeziums and circles; composite shapes; nets and "
         "surface area of prisms; volume and capacity.",
    later="Arc length and sector area, cylinders, cones and spheres, Pythagoras' theorem, "
          "similarity and scaling, and optimisation.",
    pathway=[("CONTEXT", "Gardens, packaging and water tanks are sized before they are built or bought."),
             ("QUESTION", "Which measurement does each decision require, and which unit makes it "
                          "meaningful?"),
             ("CONCEPT", "Form, measurement and space."),
             ("INVESTIGATION", "Which cuboid uses the least material for a fixed volume?"),
             ("COMMUNICATION", "Labelled nets, dimensioned diagrams and calculations that carry units."),
             ("REFLECTION", "When is an estimate sufficient, and when must a measurement be exact?")],
    content="content/ch09.txt",
)

ch(
    n=10, part=5,
    title="Data, tables and graphs",
    short="Data, tables and graphs",
    blurb="A table can organise a crowd of responses into a pattern. A graph can make that "
          "pattern visible at a glance. But every display is a set of choices, and those choices "
          "decide what a reader notices, what they overlook and what they are willing to believe.",
    inquiry="A school surveys 200 students about where they eat lunch. The newsletter reports "
            "that “most students buy school lunch”, while a second article claims that “off-site "
            "eating is out of control”. Both use the same survey. Which tables and graphs would "
            "let you check each claim, and what could a careless display hide?",
    opener_teaser="The same survey can support two opposite headlines. One number is not a "
                  "finding until the question, the group and the display are known. This "
                  "chapter teaches you to read the choices behind the chart.",
    hours=16,
    concepts=[("KEY CONCEPT", "Relationships"), ("RELATED", "Representation"),
              ("RELATED", "Patterns"), ("GLOBAL CONTEXT", "Fairness and development")],
    concept_blocks=[
        ("KEY CONCEPT · RELATIONSHIPS", "Relationships",
         "A data set records how individuals vary. Tables, graphs and averages are ways of "
         "showing relationships between a variable and its frequency, or between two variables."),
        ("RELATED CONCEPT · REPRESENTATION", "Representation",
         "Every table or graph models the data and can reveal or distort a pattern through its "
         "scale and labels."),
        ("RELATED CONCEPT · PATTERNS", "Patterns",
         "Trends, clusters and outliers are patterns; describing them needs evidence, not first "
         "impressions."),
    ],
    context="Fairness and development",
    context_exploration="How data displays inform decisions about shared resources, and how a "
                        "misleading display can make a claim seem stronger than the evidence.",
    factual="What are the main types of data? How is a frequency table built, and how is a "
            "sector angle calculated?",
    conceptual="How does the choice of representation reveal or conceal a pattern? When does one "
               "average represent a group fairly?",
    debatable="Is a graph that is technically accurate but visually exaggerated misleading? Who "
              "is responsible for the interpretation — the creator or the reader?",
    criteria=[
        ("A · Knowing and understanding", "i, ii",
         "Classify data, construct frequency and two-way tables, calculate averages and sector "
         "angles accurately."),
        ("B · Investigating patterns", "i, ii",
         "Compare how different class intervals change a histogram, describe the pattern and "
         "justify a choice."),
        ("C · Communicating", "i, ii, iii",
         "Label axes and units, choose an appropriate display, and explain a trend or a "
         "misleading feature precisely."),
        ("D · Applying mathematics", "i, ii, iii, iv",
         "Analyse survey data, cost a canteen decision, and evaluate a public claim against the "
         "evidence behind it."),
    ],
    atl_focus="Critical thinking",
    atl="In order for a student to question the claim that a new phone has “twice the battery "
        "life”, students must identify the test conditions, the axis scale and the baseline, "
        "then state which feature of the graph could exaggerate the difference.",
    soi="Data becomes evidence when it is represented accurately; the choice of table, graph or "
        "average shapes the conclusion a reader can draw.",
    soi_intro="A frequency table is a decision about categories; a graph is a decision about "
              "scale; an average is a decision about summary. None of these decisions is "
              "neutral, and each can be checked. Statistical literacy begins with asking who "
              "chose and why.",
    intentions=[
        "Understand the difference between categorical and numerical data, and between discrete "
        "and continuous measurements.",
        "Organise data in frequency tables and two-way tables.",
        "Construct and interpret bar charts, pie charts, dot plots, histograms and time-series "
        "graphs.",
        "Calculate and compare the mean, median, mode and range.",
        "Describe a trend and calculate a percentage change.",
        "Investigate how the choice of class interval changes the picture a histogram gives.",
    ],
    success=[
        "I can classify a variable and justify the classification.",
        "I can build a table with correct totals and relative frequencies.",
        "I can calculate sector angles and draw a labelled pie chart.",
        "I can choose an average and explain why it suits the data.",
        "I can describe a trend using values from a graph.",
        "I can identify how an axis, interval or missing context misleads.",
    ],
    prereq=[
        ("Calculate 25% of 80.", "20"),
        ("Write $\\frac{3}{8}$ as a decimal and a percentage.", "0.375 and 37.5%"),
        ("Calculate $360 \\div 8$.", "45"),
        ("Find the mean of 4, 7 and 13.", "8"),
        ("List these numbers in order: 12, 5, 9, 5, 14.", "5, 5, 9, 12, 14"),
        ("Calculate the difference between 186 and 104.", "82"),
    ],
    prereq_note="Answers are in the Chapter 10 answer section. If more than two are incorrect, "
                "review fractions, percentages and the idea of an average before continuing.",
    before="Tally charts, simple bar charts, reading tables, and finding the mean of a small set "
           "of numbers.",
    this="Data types; frequency and two-way tables; bar charts, pie charts, dot plots and "
         "histograms; averages and range; trends and misleading graphs.",
    later="Scatter graphs and correlation, sampling and bias, probability from data, cumulative "
          "frequency and statistical inference.",
    pathway=[("CONTEXT", "Schools and news outlets use surveys to make claims about groups of people."),
             ("QUESTION", "Which display communicates each claim honestly, and which display "
                          "exaggerates it?"),
             ("CONCEPT", "Relationships, representation and pattern."),
             ("INVESTIGATION", "How does the width of a class interval change the shape of a "
                               "histogram?"),
             ("COMMUNICATION", "Labelled axes, stated totals and a caption that names the pattern."),
             ("REFLECTION", "When is an average a fair summary, and when does it hide the people "
                            "behind the number?")],
    content="content/ch10.txt",
)
