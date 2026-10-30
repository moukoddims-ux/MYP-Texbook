"""Minimal TeX-like maths to ReportLab inline-markup converter.

Content files use $...$ for mathematics.  The converter supports the subset
that a Year 1 coursebook needs: fractions, powers, roots, comparisons and the
usual symbols, plus automatic italicising of algebraic letters.
"""
import re

GREEK = {
    r"\alpha": "α", r"\beta": "β", r"\gamma": "γ", r"\delta": "δ",
    r"\theta": "θ", r"\pi": "π", r"\lambda": "λ", r"\mu": "μ",
    r"\Sigma": "Σ", r"\Delta": "Δ", r"\Omega": "Ω",
}

SYMBOLS = {
    r"\times": "×", r"\div": "÷", r"\pm": "±", r"\mp": "∓", r"\cdot": "·",
    r"\le": "≤", r"\leq": "≤", r"\ge": "≥", r"\geq": "≥", r"\ne": "≠",
    r"\neq": "≠", r"\approx": "≈", r"\equiv": "≡", r"\propto": "∝",
    r"\to": "→", r"\rightarrow": "→", r"\Rightarrow": "⇒",
    r"\leftarrow": "←", r"\leftrightarrow": "↔", r"\iff": "⇔",
    r"\angle": "∠", r"\triangle": "△", r"\parallel": "∥", r"\perp": "⊥",
    r"\in": "∈", r"\notin": "∉", r"\subset": "⊂", r"\subseteq": "⊆",
    r"\cup": "∪", r"\cap": "∩", r"\emptyset": "∅", r"\varnothing": "∅", r"\square": "□", r"\Box": "□",
    r"\degree": "°", r"\circ": "∘", r"\infty": "∞", r"\therefore": "∴",
    r"\because": "∵", r"\prime": "′", r"\ldots": "…", r"\dots": "…",
    r"\sum": "Σ", r"\sqrt2": "√2", r"\lt": "<", r"\gt": ">",
    r"\colon": ":", r"\ast": "∗", r"\star": "⋆", r"\bullet": "•",
    r"\lvert": "|", r"\rvert": "|", r"\{": "{", r"\}": "}",
    r"\quad": "\u2002\u2002", r"\ ": " ",
}

# words that must stay upright inside mathematics
UPRIGHT = {
    "cm", "mm", "km", "kg", "mg", "ml", "mL", "km/h", "m/s", "min", "max",
    "sin", "cos", "tan", "°C", "°F", "m²", "cm²", "m³", "cm³", "L", "h", "g",
    "HCF", "LCM", "and", "or", "of", "to", "per", "so", "cm2", "cm3", "m2",
    "m3", "km2", "mm2", "kg/m³",
}


BLACKBOARD = {"N": "ℕ", "Z": "ℤ", "Q": "ℚ", "R": "ℝ", "C": "ℂ"}


def _fontified(ch, font="Sans"):
    return f'{TOK_L}font name="{font}"{TOK_R}{ch}{TOK_L}/font{TOK_R}'


def _apply_symbols(s):
    def mathbb(m):
        return _fontified(BLACKBOARD.get(m.group(1), m.group(1)))

    s = re.sub(r"\\mathbb\{([A-Za-z])\}", mathbb, s)
    s = re.sub(r"\\overline\{([^{}]*)\}", lambda m: m.group(1) * 2 + "\u2026", s)
    s = re.sub(r"\\dot\{([^{}]*)\}", lambda m: m.group(1) * 3 + "\u2026", s)
    s = re.sub(r"\\text\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\mathcal\{([A-Za-z])\}", r"\1", s)
    s = re.sub(r"\\sqrt\{([^{}]*)\}", r"√\1", s)
    s = re.sub(r"\\sqrt(\d)", r"√\1", s)
    s = s.replace(r"\%", "%").replace(r"\$", "$").replace(r"\&", "&")
    s = s.replace(r"\_", "_").replace(r"\#", "#")
    # longest keys first so that \le does not eat \leq
    for k in sorted(list(GREEK) + list(SYMBOLS), key=len, reverse=True):
        s = s.replace(k, GREEK.get(k, SYMBOLS.get(k, "")))
    s = s.replace("∅", _fontified("∅"))
    return s


def _split_top(s, sep="+"):
    """Split on a separator that is not inside braces."""
    depth = 0
    out, cur = [], ""
    for ch in s:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out


FRAC = re.compile(r"\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}")


TOK_L = "\x01"
TOK_R = "\x02"


def _frac(a, b, size=-1.5):
    """Stacked-fraction look using the fraction slash and raised/lowered text."""
    L, R = TOK_L, TOK_R
    return (f'{L}super{R}{L}font size="{size}"{R}{a}{L}/font{R}{L}/super{R}\u2044'
            f'{L}sub{R}{L}font size="{size}"{R}{b}{L}/font{R}{L}/sub{R}')


def _fractions(s):
    while True:
        m = FRAC.search(s)
        if not m:
            break
        s = s[:m.start()] + _frac(m.group(1), m.group(2)) + s[m.end():]

    def repl(m):
        a, b = m.group(1), m.group(2)
        return _frac(a, b, 0.6)

    s = re.sub(r"(?<![\w.\\])(\d+(?:\.\d+)?|[a-zA-Z])\s?/\s?"
               r"(\d+(?:\.\d+)?|[a-zA-Z])(?![\w.\\])", repl, s)
    return s


def _scripts(s):
    L, R = TOK_L, TOK_R

    def sup_repl(m):
        body = m.group(1) if m.group(1) is not None else m.group(2)
        return f'{L}super{R}{L}font size="-1.2"{R}{body}{L}/font{R}{L}/super{R}'

    def sub_repl(m):
        body = m.group(1) if m.group(1) is not None else m.group(2)
        return f'{L}sub{R}{L}font size="-1.2"{R}{body}{L}/font{R}{L}/sub{R}'

    s = re.sub(r"\^\{([^{}]*)\}|\^(\w)", sup_repl, s)
    s = re.sub(r"_\{([^{}]*)\}|_(\w)", sub_repl, s)
    return s


def _italicise(s):
    """Italicise runs of Latin letters that are not measurement units."""
    L, R = TOK_L, TOK_R
    unit_pat = r"(\b(?:%s)\b)" % "|".join(
        sorted([re.escape(u) for u in UPRIGHT], key=len, reverse=True))
    letters = re.compile(r"[A-Za-z\u03b1-\u03c9\u0391-\u03a9]+")

    def italic_run(m):
        return f"{L}i{R}{m.group(0)}{L}/i{R}"

    out = []
    for token in re.split(f"({L}[^{R}]*{R}|&[a-zA-Z]+;)", s):
        if token.startswith("&"):
            out.append(token)
            continue
        if token.startswith(L):
            out.append(token)
            continue
        pieces = re.split(unit_pat, token)
        for piece in pieces:
            if not piece:
                continue
            if piece in UPRIGHT:
                out.append(piece)
            else:
                out.append(letters.sub(italic_run, piece))
    return "".join(out)


def mathify(expr):
    """Convert a single $...$ expression into ReportLab inline markup."""
    s = expr.strip()
    while "\\\\" in s:          # tolerate doubled backslashes from source files
        s = s.replace("\\\\", "\\")
    s = _apply_symbols(s)
    s = _fractions(s)
    s = _scripts(s)
    s = re.sub(r"\\([A-Za-z]+)", r"\1", s)
    s = s.replace("{", "").replace("}", "")
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = _italicise(s)
    s = s.replace(TOK_L, "<").replace(TOK_R, ">")
    return s


INLINE = re.compile(r"\$(.+?)\$", re.S)


def rich(text):
    """Convert **bold**, *italic*, =underline= and $maths$ in running text."""
    parts = []
    pos = 0
    for m in INLINE.finditer(text):
        chunk = text[pos:m.start()]
        parts.append(_plain(chunk))
        parts.append(mathify(m.group(1)))
        pos = m.end()
    parts.append(_plain(text[pos:]))
    return "".join(parts)


def _plain(chunk):
    chunk = chunk.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    chunk = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", chunk)
    chunk = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", chunk)
    chunk = re.sub(r"(?<![\w\d])-(?=\d)", "\u2212", chunk)
    return chunk
