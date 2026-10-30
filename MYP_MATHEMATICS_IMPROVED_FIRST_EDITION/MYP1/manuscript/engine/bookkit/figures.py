"""Original vector diagrams for the improved edition.

Every diagram is drawn from code (no third-party artwork), so the book can
state clearly that all figures are original to this edition.
"""
import math

from reportlab.graphics.shapes import (Circle, Drawing, Group, Line, Polygon,
                                       Rect, String, Wedge)
from reportlab.lib import colors
from reportlab.lib.colors import HexColor

INK = HexColor("#17222B")
SOFT = HexColor("#7C8B95")
BAND = HexColor("#0E6E76")
BAND2 = HexColor("#B4701A")
BAND3 = HexColor("#4A3F87")
BAND4 = HexColor("#2F6B3E")
BAND5 = HexColor("#7A2E52")
LIGHT = HexColor("#D9E6E8")
LIGHT2 = HexColor("#F3E3C8")
GRID = HexColor("#DDE4E9")
WHITE = colors.white


def _t(g, x, y, txt, size=8, col=INK, anchor="middle", bold=False):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    fname = "Sans-Bold" if bold else "Sans"
    s = String(x, y, txt, fontName=fname, fontSize=size, fillColor=col)
    w = stringWidth(txt, fname, size)
    if anchor == "middle":
        s.x = x - w / 2.0
    elif anchor == "right":
        s.x = x - w
    s.textAnchor = "start"
    g.add(s)
    return s


def _arrow(g, x1, y1, x2, y2, col=INK, w=0.9, head=4.0):
    g.add(Line(x1, y1, x2, y2, strokeColor=col, strokeWidth=w))
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (+1, -1):
        g.add(Line(x2, y2,
                   x2 - head * math.cos(ang - s * 0.42),
                   y2 - head * math.sin(ang - s * 0.42),
                   strokeColor=col, strokeWidth=w))


def _drawing(w, h):
    d = Drawing(w, h)
    d.hAlign = "CENTER"
    return d


# ------------------------------------------------------------------ 1. number line
def numline(lo=-5, hi=5, w=330, h=54, ticks=None, marks=(), label_every=1,
            col=BAND, caption_labels=None):
    d = _drawing(w, h)
    g = Group()
    y = h * 0.46
    pad = 18
    g.add(Line(pad, y, w - pad, y, strokeColor=INK, strokeWidth=1.1))
    _arrow(g, w - pad - 8, y, w - pad, y, INK, 1.1, 4.5)
    _arrow(g, pad + 8, y, pad, y, INK, 1.1, 4.5)
    ticks = ticks if ticks is not None else list(range(lo, hi + 1))
    span = (w - 2 * pad - 6)
    step = span / max(1, (hi - lo))

    def X(v):
        return pad + 3 + (v - lo) * step

    for t in ticks:
        g.add(Line(X(t), y - 3.2, X(t), y + 3.2, strokeColor=INK, strokeWidth=0.8))
        if label_every and (t - lo) % label_every == 0:
            _t(g, X(t), y - 12.5, str(t).replace("-", "−"), 7.2, INK)
    for v, lab in marks:
        g.add(Circle(X(v), y, 3.1, fillColor=col, strokeColor=col))
        _t(g, X(v), y + 7.5, lab, 7.4, col, bold=True)
    if caption_labels:
        for v, lab in caption_labels:
            _t(g, X(v), y - 22, lab, 6.6, SOFT)
    d.add(g)
    return d


# ------------------------------------------------------------------ 2. place value grid
def placevalue(headers, digits, highlight=None, w=None, h=52, col=BAND):
    n = len(headers)
    cw = 48 if w is None else w / n
    d = _drawing(cw * n, h)
    g = Group()
    for i, (hd, dg) in enumerate(zip(headers, digits)):
        x = i * cw
        fill = HexColor("#E7F1F1") if highlight == i else WHITE
        g.add(Rect(x, 16, cw, h - 26, fillColor=fill, strokeColor=INK, strokeWidth=0.6))
        _t(g, x + cw / 2, h - 7, hd, 5.9, SOFT, bold=True)
        _t(g, x + cw / 2, 24, dg, 12.5, col if highlight == i else INK, bold=True)
    d.add(g)
    return d


# ------------------------------------------------------------------ 3. bar chart
def bars(cats, vals, w=300, h=130, ymax=None, col=BAND, ylab="", gap=0.28,
         value_labels=True, horizontal=False, unit=""):
    d = _drawing(w, h)
    g = Group()
    ymax = ymax or max(vals) * 1.15
    if horizontal:
        left, right, top, bot = 62, 12, 10, 26
        bh = (h - top - bot) / len(vals)
        for i, (c, v) in enumerate(zip(cats, vals)):
            bwd = (w - left - right) * v / ymax
            y = h - top - (i + 1) * bh + bh * 0.18
            g.add(Rect(left, y, bwd, bh * 0.64, fillColor=col, strokeColor=None))
            _t(g, left - 4, y + bh * 0.2, c, 6.8, INK, "right")
            if value_labels:
                _t(g, left + bwd + 3, y + bh * 0.2, f"{v}{unit}", 6.8, col, "left")
        g.add(Line(left, h - top - len(vals) * bh, left, h - top, strokeColor=INK, strokeWidth=0.8))
    else:
        left, right, top, bot = 34, 10, 12, 26
        bw = (w - left - right) / len(vals)
        for i, (c, v) in enumerate(zip(cats, vals)):
            bh = (h - top - bot) * v / ymax
            x = left + i * bw + bw * gap / 2
            g.add(Rect(x, bot, bw * (1 - gap), bh, fillColor=col, strokeColor=None))
            if value_labels:
                _t(g, x + bw * (1 - gap) / 2, bot + bh + 3, f"{v}", 6.6, col, bold=True)
            _t(g, x + bw * (1 - gap) / 2, bot - 10, c, 6.6, INK)
        g.add(Line(left, bot, w - right, bot, strokeColor=INK, strokeWidth=0.8))
        g.add(Line(left, bot, left, h - top, strokeColor=INK, strokeWidth=0.8))
        for frac in (0.25, 0.5, 0.75, 1.0):
            yy = bot + (h - top - bot) * frac
            g.add(Line(left, yy, w - right, yy, strokeColor=GRID, strokeWidth=0.4))
            _t(g, left - 3, yy - 2, f"{ymax*frac:.0f}", 6.0, SOFT, "right")
        if ylab:
            _t(g, 8, h / 2, ylab, 6.4, SOFT)
    d.add(g)
    return d


# ------------------------------------------------------------------ 4. pie chart
def pie(labels, vals, w=250, h=140, colours=None, show_pct=True):
    d = _drawing(w, h)
    g = Group()
    total = float(sum(vals))
    colours = colours or [BAND, BAND2, BAND3, BAND4, BAND5, SOFT]
    cx, cy, r = h * 0.52, h * 0.5, h * 0.40
    start = 90
    for i, v in enumerate(vals):
        ext = -360.0 * v / total
        g.add(Wedge(cx, cy, r, start, start + ext, fillColor=colours[i % len(colours)],
                    strokeColor=WHITE, strokeWidth=1.0))
        mid = math.radians(start + ext / 2)
        if v / total > 0.07:
            _t(g, cx + 0.58 * r * math.cos(mid), cy + 0.58 * r * math.sin(mid),
               f"{100*v/total:.0f}%" if show_pct else str(v), 6.4, WHITE, bold=True)
        start += ext
    for i, lab in enumerate(labels):
        yy = h - 12 - i * 13
        g.add(Rect(h * 1.06, yy - 1, 7, 7, fillColor=colours[i % len(colours)],
                   strokeColor=None))
        _t(g, h * 1.06 + 10, yy, lab, 6.8, INK, "left")
    d.add(g)
    return d


# ------------------------------------------------------------------ 5. dot plot
def dotplot(vals, lo, hi, w=320, h=62, col=BAND):
    d = _drawing(w, h)
    g = Group()
    pad = 16
    y = 18
    g.add(Line(pad, y, w - pad, y, strokeColor=INK, strokeWidth=0.8))
    step = (w - 2 * pad) / max(1, (hi - lo))
    for v in range(lo, hi + 1):
        g.add(Line(pad + (v - lo) * step, y - 2.5, pad + (v - lo) * step, y + 2.5,
                   strokeColor=INK, strokeWidth=0.6))
        _t(g, pad + (v - lo) * step, y - 9, str(v), 6.6, INK)
    counts = {}
    for v in vals:
        counts[v] = counts.get(v, 0) + 1
        g.add(Circle(pad + (v - lo) * step, y + 5 + 6.0 * (counts[v] - 1), 2.6,
                     fillColor=col, strokeColor=col))
    d.add(g)
    return d


# ------------------------------------------------------------------ 6. histogram
def hist(bins, freqs, w=320, h=110, col=BAND, xlab=""):
    d = _drawing(w, h)
    g = Group()
    left, right, top, bot = 28, 8, 12, 24
    ymax = max(freqs) * 1.2
    bw = (w - left - right) / len(freqs)
    for i, f in enumerate(freqs):
        bh = (h - top - bot) * f / ymax
        g.add(Rect(left + i * bw, bot, bw - 0.8, bh, fillColor=col, strokeColor=WHITE,
                   strokeWidth=0.8))
        _t(g, left + i * bw + bw / 2, bot + bh + 3, str(f), 6.2, col, bold=True)
    for i, b in enumerate(bins):
        _t(g, left + i * bw, bot - 8, str(b), 6.0, INK)
    _t(g, left + (w - left - right), bot - 16, xlab, 6.2, SOFT, "right")
    g.add(Line(left, bot, w - right, bot, strokeColor=INK, strokeWidth=0.8))
    g.add(Line(left, bot, left, h - top, strokeColor=INK, strokeWidth=0.8))
    d.add(g)
    return d


# ------------------------------------------------------------------ 7. coordinate grid
def grid(points=(), lines=(), w=230, h=210, xr=(-5, 5), yr=(-4, 6), cell=None,
         labels=True, shade=None):
    d = _drawing(w, h)
    g = Group()
    pad = 14
    cw = (w - 2 * pad) / (xr[1] - xr[0])
    ch = (h - 2 * pad) / (yr[1] - yr[0])

    def X(x):
        return pad + (x - xr[0]) * cw

    def Y(y):
        return pad + (y - yr[0]) * ch

    if shade:
        x0, y0, x1, y1 = shade
        g.add(Rect(X(x0), Y(y0), (x1 - x0) * cw, (y1 - y0) * ch,
                   fillColor=HexColor("#E7F1F1"), strokeColor=None))
    for x in range(xr[0], xr[1] + 1):
        g.add(Line(X(x), Y(yr[0]), X(x), Y(yr[1]), strokeColor=GRID, strokeWidth=0.4))
    for y in range(yr[0], yr[1] + 1):
        g.add(Line(X(xr[0]), Y(y), X(xr[1]), Y(y), strokeColor=GRID, strokeWidth=0.4))
    g.add(Line(X(xr[0]), Y(0), X(xr[1]), Y(0), strokeColor=INK, strokeWidth=0.9))
    g.add(Line(X(0), Y(yr[0]), X(0), Y(yr[1]), strokeColor=INK, strokeWidth=0.9))
    if labels:
        for x in range(xr[0], xr[1] + 1):
            if x:
                _t(g, X(x), Y(0) - 8, str(x).replace("-", "−"), 5.6, SOFT)
        for y in range(yr[0], yr[1] + 1):
            if y:
                _t(g, X(0) - 5, Y(y) - 2, str(y).replace("-", "−"), 5.6, SOFT, "right")
    for ln in lines:
        (x1, y1), (x2, y2) = ln
        g.add(Line(X(x1), Y(y1), X(x2), Y(y2), strokeColor=BAND, strokeWidth=1.3))
    for p in points:
        x, y = p[0], p[1]
        g.add(Circle(X(x), Y(y), 2.6, fillColor=BAND2, strokeColor=WHITE, strokeWidth=0.5))
        if len(p) > 2:
            _t(g, X(x) + 4, Y(y) + 3, p[2], 6.4, BAND2, "left", bold=True)
    if labels:
        _t(g, X(xr[1]) - 3, Y(0) - 9, "x", 7, INK, "right")
        _t(g, X(0) - 6, Y(yr[1]) - 2, "y", 7, INK, "right")
    d.add(g)
    return d


# ------------------------------------------------------------------ 8. angle diagrams
def angle_on_line(w=200, h=90, a=125, b=55, la="a", lb="b"):
    d = _drawing(w, h)
    g = Group()
    y = 22
    g.add(Line(16, y, w - 16, y, strokeColor=INK, strokeWidth=1.1))
    cx = w * 0.45
    L = h - 26
    g.add(Line(cx, y, cx + L * math.cos(math.radians(a)), y + L * math.sin(math.radians(a)),
               strokeColor=INK, strokeWidth=1.0))
    g.add(Wedge(cx, y, 15, 0, a, fillColor=LIGHT, strokeColor=None))
    _t(g, cx + 24, y + 12, f"{la}", 7.6, BAND, bold=True)
    _t(g, cx - 26, y + 12, f"{lb}", 7.6, BAND, bold=True)
    d.add(g)
    return d


def angle_point(w=180, h=110, angles=(0, 65, 140, 230), labs=("x", "y", "z", "w")):
    d = _drawing(w, h)
    g = Group()
    cx, cy, L = w / 2, h / 2, min(w, h) * 0.42
    for i, a in enumerate(angles):
        g.add(Line(cx, cy, cx + L * math.cos(math.radians(a)), cy + L * math.sin(math.radians(a)),
                   strokeColor=INK, strokeWidth=1.0))
        mid = math.radians((a + angles[(i + 1) % len(angles)]) / 2 + (0 if i < len(angles) - 1 else 0))
    for i, a in enumerate(angles):
        nxt = angles[i + 1] if i + 1 < len(angles) else angles[0] + 360
        mid = math.radians((a + nxt) / 2)
        _t(g, cx + 0.55 * L * math.cos(mid), cy + 0.55 * L * math.sin(mid), labs[i], 7.4, BAND, bold=True)
    g.add(Circle(cx, cy, 1.6, fillColor=INK, strokeColor=INK))
    d.add(g)
    return d


def parallel_lines(w=250, h=120, labs=("a", "b", "c", "d")):
    d = _drawing(w, h)
    g = Group()
    y1, y2 = h * 0.66, h * 0.30
    g.add(Line(14, y1, w - 14, y1, strokeColor=INK, strokeWidth=1.0))
    g.add(Line(14, y2, w - 14, y2, strokeColor=INK, strokeWidth=1.0))
    x0, x1 = w * 0.30, w * 0.62
    g.add(Line(x0, 8, x1, h - 8, strokeColor=BAND, strokeWidth=1.1))
    _t(g, w - 16, y1 + 4, "l", 7, SOFT, "right")
    _t(g, w - 16, y2 + 4, "m", 7, SOFT, "right")
    _t(g, x1 + 4, h - 14, "t", 7, SOFT, "left")
    _t(g, x0 - 12, y1 + 4, labs[0], 7.2, BAND, bold=True)
    _t(g, x0 + 10, y1 + 4, labs[1], 7.2, BAND, bold=True)
    _t(g, x1 - 14, y2 + 4, labs[2], 7.2, BAND, bold=True)
    _t(g, x1 + 8, y2 + 4, labs[3], 7.2, BAND, bold=True)
    d.add(g)
    return d


def triangle(w=210, h=120, sides=("a", "b", "c"), angles=None, apex=62, col=BAND,
             marks=None, right=False, base_lab=None, height=None):
    d = _drawing(w, h)
    g = Group()
    if right:
        pts = [(24, 18), (24, h - 16), (w - 24, 18)]
    else:
        bx1, bx2, by = 24, w - 24, 18
        apex_x = bx1 + (bx2 - bx1) * 0.45
        pts = [(bx1, by), (bx2, by), (apex_x, h - 16)]
    g.add(Polygon(pts, fillColor=HexColor("#F4F8F9"), strokeColor=INK, strokeWidth=1.0))
    if right:
        g.add(Rect(24, 18, 9, 9, fillColor=None, strokeColor=BAND, strokeWidth=0.8))
    if angles:
        for (px, py), a, lab in zip(pts, angles, ("A", "B", "C")):
            _t(g, px, py + (-8 if py > h / 2 else 4), lab, 6.6, SOFT)
        for (px, py), a, lab in zip(pts, angles, sides):
            if lab:
                ang = math.degrees(math.atan2(py - h / 2, px - w / 2)) + 180
                _t(g, px + 12 * math.cos(math.radians(ang)), py + 10 * math.sin(math.radians(ang)),
                   lab, 7.0, BAND, bold=True)
    d.add(g)
    return d


def angle_pair(w=300, h=100, mode="corresponding"):
    return parallel_lines(w, h)


# ------------------------------------------------------------------ 9. rectangles / area
def rect_dim(w=200, h=110, wl="6 cm", hl="4 cm", col=BAND, shaded=False, grid_units=None):
    d = _drawing(w, h)
    g = Group()
    x0, y0 = 26, 24
    rw, rh = w - 52, h - 44
    g.add(Rect(x0, y0, rw, rh, fillColor=(HexColor("#E7F1F1") if shaded else HexColor("#FBFCFC")),
               strokeColor=INK, strokeWidth=1.0))
    if grid_units:
        for i in range(1, grid_units):
            g.add(Line(x0 + rw * i / grid_units, y0, x0 + rw * i / grid_units, y0 + rh,
                       strokeColor=GRID, strokeWidth=0.5))
    _t(g, x0 + rw / 2, y0 - 9, wl, 7.2, col, bold=True)
    _t(g, x0 - 4, y0 + rh / 2 - 3, hl, 7.2, col, "right", bold=True)
    d.add(g)
    return d


def composite_shape(w=250, h=150):
    d = _drawing(w, h)
    g = Group()
    pts = [20, 20, 150, 20, 150, 90, 230, 90, 230, 130, 20, 130]
    g.add(Polygon(pts, fillColor=HexColor("#EFF6F6"), strokeColor=INK, strokeWidth=1.0))
    g.add(Line(150, 20, 150, 130, strokeColor=SOFT, strokeWidth=0.6))
    _t(g, 85, 12, "12 m", 7, BAND, bold=True)
    _t(g, 190, 134, "6 m", 7, BAND, bold=True)
    _t(g, 236, 105, "4 m", 7, BAND, "left", bold=True)
    _t(g, 14, 75, "9 m", 7, BAND, "right", bold=True)
    d.add(g)
    return d


def circle_parts(w=300, h=140, show_r=True, show_d=True, show_circ=True, shade=False,
                 deg=70):
    d = _drawing(w, h)
    g = Group()
    cx, cy, r = 70, h / 2, min(h / 2 - 14, 52)
    if shade:
        g.add(Wedge(cx, cy, r, 0, deg, fillColor=LIGHT, strokeColor=INK, strokeWidth=0.9))
        g.add(Circle(cx, cy, r, fillColor=None, strokeColor=INK, strokeWidth=1.0))
    else:
        g.add(Circle(cx, cy, r, fillColor=HexColor("#FAFCFC"), strokeColor=INK, strokeWidth=1.0))
    if show_r:
        g.add(Line(cx, cy, cx + r * math.cos(math.radians(30)), cy + r * math.sin(math.radians(30)),
                   strokeColor=BAND, strokeWidth=1.0))
        _t(g, cx + r * 0.5 * math.cos(math.radians(30)) + 4, cy + r * 0.5 * math.sin(math.radians(30)) + 4,
           "r", 7.4, BAND, "left", bold=True)
    if show_d:
        g.add(Line(cx - r, cy, cx + r, cy, strokeColor=BAND2, strokeWidth=1.0))
        _t(g, cx, cy - 9, "d = 2r", 6.8, BAND2)
    g.add(Circle(cx, cy, 1.4, fillColor=INK, strokeColor=INK))
    if show_circ:
        _t(g, cx + r + 26, cy + r - 8, "C = 2πr", 7.6, BAND)
        _t(g, cx + r + 26, cy + 2, "A = πr²", 7.6, BAND)
    d.add(g)
    return d


# ------------------------------------------------------------------ 10. solids and nets
def prism(w=220, h=140, labels=("l", "w", "h"), vals=None):
    d = _drawing(w, h)
    g = Group()
    ox, oy = 34, 26
    dx, dy = 62, 34
    bw, bh = 96, 62
    face = [ox, oy, ox + bw, oy, ox + bw, oy + bh, ox, oy + bh]
    top = [ox, oy + bh, ox + dx, oy + bh + dy, ox + bw + dx, oy + bh + dy, ox + bw, oy + bh]
    side = [ox + bw, oy, ox + bw + dx, oy + dy, ox + bw + dx, oy + bh + dy, ox + bw, oy + bh]
    g.add(Polygon(face, fillColor=HexColor("#EFF6F6"), strokeColor=INK, strokeWidth=0.9))
    g.add(Polygon(top, fillColor=HexColor("#DDEBEC"), strokeColor=INK, strokeWidth=0.9))
    g.add(Polygon(side, fillColor=HexColor("#E7F1F1"), strokeColor=INK, strokeWidth=0.9))
    vals = vals or ("l", "w", "h")
    _t(g, ox + bw / 2, oy - 9, vals[0], 7.2, BAND, bold=True)
    _t(g, ox + bw + dx / 2 + 5, oy + dy / 2 - 6, vals[1], 7.2, BAND, bold=True)
    _t(g, ox - 5, oy + bh / 2, vals[2], 7.2, BAND, "right", bold=True)
    d.add(g)
    return d


def net_cuboid(w=240, h=150, dims=("l", "w", "h")):
    d = _drawing(w, h)
    g = Group()
    u, v = 22, 20
    x0, y0 = 30, 34
    # cross net: top column, middle row of 4, bottom
    cells = [(1, 2), (0, 1), (1, 1), (2, 1), (3, 1), (1, 0)]
    for (cx, cy) in cells:
        g.add(Rect(x0 + cx * u * 1.6, y0 + cy * v * 1.9, u * 1.6, v * 1.9,
                   fillColor=HexColor("#F2F8F8"), strokeColor=INK, strokeWidth=0.8))
    cw_, chh = u * 1.6, v * 1.9
    _t(g, x0 + 1.5 * cw_, y0 + 3 * chh + 8, "surface area = 2(lw + lh + wh)", 6.6, SOFT)
    _t(g, x0 + 0.5 * cw_, y0 + 1.5 * chh, dims[0], 7.0, BAND, bold=True)
    _t(g, x0 + 2.5 * cw_, y0 + 1.5 * chh, dims[0], 7.0, BAND, bold=True)
    _t(g, x0 + 1.5 * cw_, y0 + 1.5 * chh, dims[1], 7.0, BAND2, bold=True)
    _t(g, x0 + 1.5 * cw_, y0 + 0.5 * chh, dims[1], 7.0, BAND2, bold=True)
    _t(g, x0 + 3.5 * cw_, y0 + 1.5 * chh, dims[2], 7.0, INK, bold=True)
    _t(g, x0 + 1.5 * cw_, y0 + 2.5 * chh, dims[2], 7.0, INK, bold=True)
    d.add(g)
    return d


def cylinder(w=190, h=140, r_lab="r", h_lab="h"):
    d = _drawing(w, h)
    g = Group()
    cx, cy = w / 2, h / 2
    rx, ry = 40, 12
    top = cy + 30
    g.add(Polygon([cx - rx, cy - 30, cx + rx, cy - 30, cx + rx, cy + 30, cx - rx, cy + 30],
                  fillColor=HexColor("#EFF6F6"), strokeColor=None))
    g.add(Line(cx - rx, cy - 30, cx - rx, cy + 30, strokeColor=INK, strokeWidth=0.9))
    g.add(Line(cx + rx, cy - 30, cx + rx, cy + 30, strokeColor=INK, strokeWidth=0.9))
    g.add(Wedge(cx, cy + 30, rx, 0, 180, fillColor=HexColor("#DDEBEC"), strokeColor=INK, strokeWidth=0.9))
    g.add(Wedge(cx, cy - 30, rx, 180, 360, fillColor=None, strokeColor=INK, strokeWidth=0.9))
    g.add(Line(cx, cy + 30, cx + rx, cy + 30, strokeColor=BAND, strokeWidth=0.9))
    _t(g, cx + rx / 2, cy + 34, r_lab, 7.2, BAND, bold=True)
    _t(g, cx + rx + 6, cy, h_lab, 7.2, BAND, "left", bold=True)
    d.add(g)
    return d


# ------------------------------------------------------------------ 11. sets
def venn2(w=250, h=130, a_lab="A", b_lab="B", counts=(None, None, None, None),
          region_labs=None, shade=None, uni="U"):
    d = _drawing(w, h)
    g = Group()
    g.add(Rect(6, 6, w - 12, h - 12, fillColor=HexColor("#FBFCFC"), strokeColor=SOFT, strokeWidth=0.7))
    cx, cy = w / 2, h / 2 - 4
    r = min(h, w) * 0.30
    g.add(Circle(cx - r * 0.62, cy, r, fillColor=HexColor("#E7F1F1"), strokeColor=BAND, strokeWidth=1.0))
    g.add(Circle(cx + r * 0.62, cy, r, fillColor=HexColor("#FBF0DF"), strokeColor=BAND2, strokeWidth=1.0))
    _t(g, cx - r * 1.15, cy + r - 4, a_lab, 8, BAND, bold=True)
    _t(g, cx + r * 1.15, cy + r - 4, b_lab, 8, BAND2, bold=True)
    _t(g, 12, h - 16, uni, 7.4, SOFT, bold=True)
    if counts:
        xs = [cx - r * 0.95, cx, cx + r * 0.95, w - 30]
        ys = [cy, cy, cy, 24]
        for (x, y, c) in zip(xs, ys, counts):
            if c is not None:
                _t(g, x, y - 3, str(c), 8.4, INK, bold=True)
    if region_labs:
        for (x, y, t) in region_labs:
            _t(g, x, y, t, 7.0, INK)
    d.add(g)
    return d


def venn3(w=260, h=150):
    d = _drawing(w, h)
    g = Group()
    cx, cy = w / 2, h / 2
    r = min(h, w) * 0.27
    for ang, colr, tint in ((90, BAND, "#E7F1F1"), (210, BAND2, "#FBF0DF"), (330, BAND3, "#ECEAF7")):
        x = cx + r * 0.52 * math.cos(math.radians(ang))
        y = cy + r * 0.52 * math.sin(math.radians(ang))
        g.add(Circle(x, y, r, fillColor=None, strokeColor=colr, strokeWidth=1.0))
    g.add(Rect(6, 6, w - 12, h - 12, fillColor=None, strokeColor=SOFT, strokeWidth=0.7))
    d.add(g)
    return d


# ------------------------------------------------------------------ 12. fractions
def fraction_bar(w=260, h=34, parts=4, shaded=1, col=BAND, labels=None, lab=""):
    d = _drawing(w, h)
    g = Group()
    y0 = 14
    bh = h - 22
    cw = w / parts
    for i in range(parts):
        g.add(Rect(i * cw, y0, cw, bh,
                   fillColor=(col if i < shaded else WHITE), strokeColor=INK, strokeWidth=0.7))
    if labels:
        for i, lb in enumerate(labels[:parts]):
            _t(g, i * cw + cw / 2, y0 + bh / 2 - 2.5, lb, 6.6, WHITE if i < shaded else INK)
    if lab:
        _t(g, 0, 2, lab, 6.8, SOFT, "left")
    d.add(g)
    return d


def square_grid(w=120, h=120, n=10, shaded=25, col=BAND):
    d = _drawing(w, h)
    g = Group()
    cell = w / n
    for i in range(n):
        for j in range(n):
            k = j * n + i
            g.add(Rect(i * cell, h - (j + 1) * cell, cell, cell,
                       fillColor=(col if k < shaded else WHITE), strokeColor=GRID, strokeWidth=0.3))
    g.add(Rect(0, 0, w, h, fillColor=None, strokeColor=INK, strokeWidth=0.8))
    d.add(g)
    return d


def percent_grid(w=120, h=120, shaded=25, col=BAND):
    return square_grid(w, h, 10, shaded, col)


# ------------------------------------------------------------------ 13. patterns
def matchstick(n=3, w=250, h=100):
    """n squares in a row, drawn as matchsticks."""
    d = _drawing(w, h)
    g = Group()
    s = min(34, (w - 40) / max(1, n))
    x0, y0 = 24, 26
    for k in range(n):
        x = x0 + k * s
        for (a, b, c, e) in [(x, y0, x, y0 + s), (x, y0 + s, x + s, y0 + s),
                             (x + s, y0, x + s, y0 + s), (x, y0, x + s, y0)]:
            g.add(Line(a, b, c, e, strokeColor=BAND, strokeWidth=1.6, strokeLineCap=1))
        g.add(Circle(x, y0, 2.0, fillColor=INK, strokeColor=INK))
    _t(g, x0, 12, f"stage {n}", 6.8, SOFT, "left")
    d.add(g)
    return d


def tile_pattern(stages=(1, 2, 3), w=300, h=90):
    d = _drawing(w, h)
    g = Group()
    s = 20
    x = 16
    for st in stages:
        for row in range(2):
            for k in range(st + 1):
                g.add(Rect(x + k * s, 20 + row * s, s, s, fillColor=HexColor("#E7F1F1"),
                           strokeColor=BAND, strokeWidth=0.6))
        _t(g, x + (st + 1) * s / 2, 10, f"{st}", 6.8, SOFT)
        x += (st + 1) * s + 22
    d.add(g)
    return d


# ------------------------------------------------------------------ 14. balance
def balance(w=280, h=108, left="2x + 3", right="11"):
    d = _drawing(w, h)
    g = Group()
    cx, cy = w / 2, 66
    g.add(Line(cx, 26, cx, cy, strokeColor=INK, strokeWidth=1.4))
    g.add(Line(cx - 96, cy, cx + 96, cy, strokeColor=INK, strokeWidth=1.6))
    g.add(Circle(cx, cy, 3.4, fillColor=INK, strokeColor=INK))
    for sgn in (-1, 1):
        px = cx + sgn * 82
        g.add(Line(px, cy, px, cy - 16, strokeColor=INK, strokeWidth=0.8))
        g.add(Line(px - 30, cy - 16, px + 30, cy - 16, strokeColor=INK, strokeWidth=1.0))
        g.add(Polygon([px - 30, cy - 16, px + 30, cy - 16, px + 24, cy - 26,
                       px - 24, cy - 26], fillColor=LIGHT, strokeColor=INK, strokeWidth=0.8))
        _t(g, px, cy - 35, left if sgn < 0 else right, 7.6,
           BAND if sgn < 0 else BAND2, bold=True)
    g.add(Polygon([cx - 20, 26, cx + 20, 26, cx + 12, 18, cx - 12, 18],
                  fillColor=HexColor("#DDE4E9"), strokeColor=INK, strokeWidth=0.8))
    _t(g, w - 8, 6, "both sides must stay equal", 6.2, SOFT, "right")
    d.add(g)
    return d


# ------------------------------------------------------------------ 15. angle / construction
def compass_arc(w=200, h=140, r=46):
    d = _drawing(w, h)
    g = Group()
    cx, cy = 40, h / 2
    g.add(Line(cx, cy, cx + w * 0.6, cy, strokeColor=INK, strokeWidth=1.0))
    g.add(Line(cx, cy, cx + w * 0.6 * math.cos(math.radians(50)),
               cy + w * 0.6 * math.sin(math.radians(50)), strokeColor=INK, strokeWidth=1.0))
    g.add(Wedge(cx, cy, r, 0, 50, fillColor=LIGHT, strokeColor=BAND, strokeWidth=0.6))
    _t(g, cx + r * 0.75, cy + r * 0.35, "50°", 7.2, BAND, bold=True)
    g.add(Circle(cx, cy, 1.6, fillColor=INK, strokeColor=INK))
    d.add(g)
    return d


def polygon(n=5, w=180, h=140, lab=True):
    d = _drawing(w, h)
    g = Group()
    cx, cy, r = w / 2, h / 2, min(w, h) * 0.42
    pts = [(cx + r * math.cos(math.radians(90 + 360 * i / n)),
            cy + r * math.sin(math.radians(90 + 360 * i / n))) for i in range(n)]
    g.add(Polygon(pts, fillColor=HexColor("#F4F8F9"), strokeColor=INK, strokeWidth=1.0))
    if lab:
        for i, p in enumerate(pts):
            g.add(String(p[0] + (4 if p[0] >= cx else -10), p[1] + (4 if p[1] >= cy else -8),
                         "ABCDEFG"[i], fontName="Sans", fontSize=6.6, fillColor=SOFT))
    d.add(g)
    return d


def reflection_diagram(w=220, h=110):
    d = _drawing(w, h)
    g = Group()
    g.add(Line(w / 2, 8, w / 2, h - 8, strokeColor=BAND2, strokeWidth=1.0, strokeDashArray=[3, 3]))
    a = [(30, 20), (70, 20), (70, 70), (30, 70)]
    g.add(Polygon(a, fillColor=HexColor("#E7F1F1"), strokeColor=BAND, strokeWidth=0.9))
    b = [(w - x, y) for (x, y) in a]
    g.add(Polygon(b, fillColor=HexColor("#FBF0DF"), strokeColor=BAND2, strokeWidth=0.9))
    _t(g, w / 2, h - 4, "mirror line", 6.4, BAND2)
    d.add(g)
    return d


def number_line_frac(w=330, h=70, ticks=("0", "1/4", "1/2", "3/4", "1"), marks=()):
    d = _drawing(w, h)
    g = Group()
    y = h * 0.55
    g.add(Line(18, y, w - 18, y, strokeColor=INK, strokeWidth=1.0))
    n = len(ticks) - 1
    for i, t in enumerate(ticks):
        x = 18 + (w - 36) * i / n
        g.add(Line(x, y - 4, x, y + 4, strokeColor=INK, strokeWidth=0.8))
        if "/" in t:
            a, b = t.split("/")
            _t(g, x, y - 11, a, 6.4, INK)
            _t(g, x, y - 18, b, 6.4, INK)
            g.add(Line(x - 4, y - 13.5, x + 4, y - 13.5, strokeColor=INK, strokeWidth=0.5))
        else:
            _t(g, x, y - 11, t, 6.8, INK)
    for v, lab in marks:
        x = 18 + (w - 36) * v
        g.add(Circle(x, y, 3.0, fillColor=BAND, strokeColor=BAND))
        _t(g, x, y + 7, lab, 6.8, BAND, bold=True)
    d.add(g)
    return d


def survey_table_figure(w=300, h=110):
    d = _drawing(w, h)
    g = Group()
    rows = [["Programme", "Members"], ["Music", "48"], ["Sport", "63"], ["Both", "?"], ["Neither", "?"]]
    cw, rh = w / 2, (h - 10) / len(rows)
    for i, r in enumerate(rows):
        for j, c in enumerate(r):
            g.add(Rect(j * cw, h - 6 - (i + 1) * rh, cw, rh,
                       fillColor=(HexColor("#E7F1F1") if i == 0 else WHITE),
                       strokeColor=GRID, strokeWidth=0.5))
            _t(g, j * cw + 6, h - 6 - (i + 1) * rh + rh / 2 - 2.4, c, 7.0,
               BAND if i == 0 else INK, "left", bold=(i == 0))
    d.add(g)
    return d


def scatter(w=230, h=140, pts=((1, 2), (2, 3), (3, 5), (4, 4), (5, 6), (6, 8))):
    d = _drawing(w, h)
    g = Group()
    left, bot, top, right = 24, 20, 10, 10
    g.add(Line(left, bot, w - right, bot, strokeColor=INK, strokeWidth=0.8))
    g.add(Line(left, bot, left, h - top, strokeColor=INK, strokeWidth=0.8))
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    for x in range(0, max(xs) + 1):
        px = left + (w - left - right) * x / max(xs)
        _t(g, px, bot - 8, str(x), 6.0, SOFT)
    for y in range(0, max(ys) + 1):
        py = bot + (h - top - bot) * y / max(ys)
        _t(g, left - 4, py - 2, str(y), 6.0, SOFT, "right")
    for (x, y) in pts:
        px = left + (w - left - right) * x / max(xs)
        py = bot + (h - top - bot) * y / max(ys)
        g.add(Circle(px, py, 2.4, fillColor=BAND, strokeColor=BAND))
    d.add(g)
    return d


def two_way_table(w=280, h=100, header=("", "Library", "No library", "Total"),
                  rows=(("Sport", "18", "22", "40"), ("No sport", "12", "8", "20"),
                        ("Total", "30", "30", "60"))):
    d = _drawing(w, h)
    g = Group()
    ncol = len(header)
    cw = w / ncol
    rh = h / (len(rows) + 1)
    def draw_row(i, cells, head=False):
        for j, c in enumerate(cells):
            g.add(Rect(j * cw, h - (i + 1) * rh, cw, rh,
                       fillColor=(HexColor("#E7F1F1") if head else WHITE),
                       strokeColor=GRID, strokeWidth=0.5))
            _t(g, j * cw + cw / 2, h - (i + 1) * rh + rh / 2 - 2.4, c, 6.8,
               BAND if head else INK, bold=head)
    draw_row(0, header, True)
    for i, r in enumerate(rows):
        draw_row(i + 1, r)
    d.add(g)
    return d


def digit_cards(cards=("3", "0", "5"), w=300, h=70, accent=BAND, examples=("305", "350", "503")):
    d = _drawing(w, h)
    g = Group()
    cw, ch = 38, 50
    x0, y0 = 10, 12
    for i, cdigit in enumerate(cards):
        x = x0 + i * (cw + 8)
        g.add(Rect(x, y0, cw, ch, rx=4, ry=4, fillColor=HexColor("#F2F7F8"),
                   strokeColor=accent, strokeWidth=1.1))
        _t(g, x + cw / 2, y0 + 15, cdigit, 20, accent, bold=True)
    x1 = x0 + 3 * (cw + 8) + 12
    g.add(Line(x1, y0 + ch / 2, x1 + 26, y0 + ch / 2, strokeColor=INK, strokeWidth=0.8))
    _arrow(g, x1 + 20, y0 + ch / 2, x1 + 30, y0 + ch / 2, INK, 0.8, 4)
    for i, ex in enumerate(examples):
        _t(g, x1 + 40 + i * 40, y0 + ch / 2 - 3, ex, 9.2, INK, "left", bold=True)
    _t(g, x0, 2, "three digit cards", 6.4, SOFT, "left")
    _t(g, x1 + 40, 2, "some three-digit numbers", 6.4, SOFT, "left")
    d.add(g)
    return d


def power_repeat(base=2, exp=4, w=300, h=64, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    y0 = 26
    _t(g, 12, y0 + 6, str(base), 16, accent, "left", bold=True)
    _t(g, 26, y0 + 16, str(exp), 9, accent, "left", bold=True)
    _t(g, 40, y0 + 6, "=", 13, INK, "left")
    x = 56
    for i in range(exp):
        _t(g, x, y0 + 6, str(base), 13, INK, "left")
        x += 12
        if i < exp - 1:
            _t(g, x, y0 + 6, "×", 11, SOFT, "left")
            x += 12
    _t(g, 2, 8, f"{base} is the base; {exp} is the exponent (the number of factors)", 6.4, SOFT, "left")
    d.add(g)
    return d


def square_numbers(n=4, w=230, h=120, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    cell = min(20, (h - 26) / max(1, n))
    x0, y0 = 12, 22
    for i in range(n):
        for j in range(n):
            g.add(Rect(x0 + i * cell, y0 + j * cell, cell, cell,
                       fillColor=HexColor("#E7F1F1"), strokeColor=WHITE, strokeWidth=0.8))
    g.add(Rect(x0, y0, n * cell, n * cell, fillColor=None, strokeColor=accent, strokeWidth=1.0))
    _t(g, x0 + n * cell + 14, y0 + n * cell - 10, f"{n} × {n} = {n*n}", 10, accent, "left", bold=True)
    _t(g, x0 + n * cell + 14, y0 + n * cell - 24, f"{n}² = {n*n}", 10, INK, "left", bold=True)
    _t(g, x0 + n * cell + 14, y0 + n * cell - 40, "a square number", 6.6, SOFT, "left")
    d.add(g)
    return d


def ops_priority(w=310, h=86):
    d = _drawing(w, h)
    g = Group()
    steps = [("1  Brackets", BAND), ("2  Indices", BAND3), ("3  × and ÷", BAND2),
             ("4  + and −", BAND4)]
    bw = (w - 24) / 4
    for i, (lab, col) in enumerate(steps):
        x = 12 + i * bw
        g.add(Rect(x, 26, bw - 6, 34, rx=3, ry=3, fillColor=col, strokeColor=None))
        _t(g, x + (bw - 6) / 2, 40, lab, 7.4, WHITE, bold=True)
        if i < 3:
            _t(g, x + bw - 4, 40, "›", 11, SOFT)
    _t(g, 12, 10, "work left to right within the same step", 6.6, SOFT, "left")
    d.add(g)
    return d


def paper_fold(folds=(0, 1, 2, 3), w=300, h=70):
    d = _drawing(w, h)
    g = Group()
    x = 10
    for f in folds:
        hh = 3 + f * 4
        g.add(Rect(x, 34 - hh / 2, 34, hh, fillColor=HexColor("#E7F1F1"), strokeColor=BAND,
                   strokeWidth=0.8))
        _t(g, x + 17, 18, f"{f} fold" + ("" if f == 1 else "s"), 6.2, SOFT)
        x += 62
    d.add(g)
    return d


def factor_arrays(n=12, w=250, h=110, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    pairs = [(a, n // a) for a in range(1, int(n ** 0.5) + 1) if n % a == 0]
    x = 12
    cell = 7
    for (a, b) in pairs:
        bw, bh = a * cell, b * cell
        g.add(Rect(x, 30, bw, bh, fillColor=HexColor("#E7F1F1"), strokeColor=accent, strokeWidth=0.7))
        _t(g, x + bw / 2, 16, f"{a} × {b}", 6.4, INK)
        x += bw + 16
    _t(g, 12, 8, f"rectangles for {n}: {len(pairs)} factor pairs", 6.2, SOFT, "left")
    d.add(g)
    return d


def sieve_grid(n=50, w=280, h=148, accent=BAND, primes=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)):
    d = _drawing(w, h)
    g = Group()
    cols = 10
    cell = (w - 10) / cols
    rh = (h - 26) / ((n + cols - 1) // cols)
    for k in range(1, n + 1):
        i, j = (k - 1) % cols, (k - 1) // cols
        x, y = 5 + i * cell, h - 26 - (j + 1) * rh
        is_p = k in primes
        g.add(Rect(x, y, cell - 1.2, rh - 1.2,
                   fillColor=(HexColor("#DCEBEC") if is_p else WHITE),
                   strokeColor=(accent if is_p else GRID), strokeWidth=(0.8 if is_p else 0.4)))
        _t(g, x + (cell - 1.2) / 2, y + rh / 2 - 3, str(k), 7.0,
           accent if is_p else SOFT, bold=is_p)
    _t(g, 5, h - 9, "numbers 1–50; the primes are shaded", 6.2, SOFT, "left")
    d.add(g)
    return d


def factor_tree(n=60, w=230, h=120, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    cx, cy = w / 2, h - 22

    def node(x, y, v, col=INK, fill=HexColor("#F2F7F8")):
        g.add(Circle(x, y, 11, fillColor=fill, strokeColor=col, strokeWidth=0.8))
        _t(g, x, y - 3, str(v), 8, col, bold=True)

    node(cx, cy, n, accent, HexColor("#E7F1F1"))
    g.add(Line(cx, cy - 11, cx - 34, cy - 40, strokeColor=SOFT, strokeWidth=0.7))
    g.add(Line(cx, cy - 11, cx + 34, cy - 40, strokeColor=SOFT, strokeWidth=0.7))
    node(cx - 40, cy - 48, 6)
    node(cx + 40, cy - 48, 10)
    g.add(Line(cx - 40, cy - 59, cx - 40, cy - 80, strokeColor=SOFT, strokeWidth=0.7))
    g.add(Line(cx - 40, cy - 59, cx - 70, cy - 80, strokeColor=SOFT, strokeWidth=0.7))
    node(cx - 40, cy - 88, 2)
    node(cx - 74, cy - 88, 3)
    g.add(Line(cx + 40, cy - 59, cx + 40, cy - 80, strokeColor=SOFT, strokeWidth=0.7))
    g.add(Line(cx + 40, cy - 59, cx + 70, cy - 80, strokeColor=SOFT, strokeWidth=0.7))
    node(cx + 40, cy - 88, 2)
    node(cx + 74, cy - 88, 5)
    d.add(g)
    return d


def common_factors_venn(w=250, h=120):
    return venn2(w, h, a_lab="factors of 12", b_lab="factors of 18",
                 counts=(None, None, None, None))


def number_ray_factors(w=280, h=90, n=24):
    d = _drawing(w, h)
    g = Group()
    y = 40
    g.add(Line(14, y, w - 14, y, strokeColor=INK, strokeWidth=0.8))
    for k in range(1, n + 1):
        x = 14 + (w - 28) * (k - 1) / (n - 1)
        is_f = n % k == 0
        if is_f:
            g.add(Circle(x, y, 3, fillColor=BAND, strokeColor=BAND))
            _t(g, x, y + 10, str(k), 7, BAND, bold=True)
        else:
            g.add(Line(x, y - 2, x, y + 2, strokeColor=GRID, strokeWidth=0.5))
    _t(g, 14, 14, f"the factors of {n} are the positions where the divisions are exact", 6.2, SOFT, "left")
    d.add(g)
    return d


def fraction_wall(rows=("1/2", "1/3", "1/4", "1/5", "1/6"), w=300, h=118, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    rh = (h - 14) / len(rows)
    barw = w - 46
    for k, lab in enumerate(rows):
        num, den = [int(x) for x in lab.split("/")]
        y = h - 10 - (k + 1) * rh
        g.add(Rect(34, y, barw, rh - 5, fillColor=WHITE, strokeColor=GRID, strokeWidth=0.5))
        cw = barw / den
        for j in range(num):
            g.add(Rect(34 + j * cw, y, cw, rh - 5, fillColor=HexColor("#DCEBEC"),
                       strokeColor=accent, strokeWidth=0.6))
        for j in range(1, den):
            g.add(Line(34 + j * cw, y, 34 + j * cw, y + rh - 5, strokeColor=GRID, strokeWidth=0.4))
        _t(g, 28, y + (rh - 5) / 2 - 2.6, lab, 6.8, INK, "right")
    g.add(Line(34, h - 6, 34 + barw, h - 6, strokeColor=accent, strokeWidth=0.8))
    _t(g, 34, h - 3, "0", 6.2, SOFT, "left")
    _t(g, 34 + barw, h - 3, "1", 6.2, SOFT, "right")
    d.add(g)
    return d


def equiv_bars(w=300, h=96, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    barw, bh = 220, 22
    specs = [("2/3", 3, 2, h - 34), ("4/6", 6, 4, h - 68)]
    for lab, den, num, y in specs:
        g.add(Rect(60, y, barw, bh, fillColor=WHITE, strokeColor=GRID, strokeWidth=0.5))
        cw = barw / den
        for j in range(num):
            g.add(Rect(60 + j * cw, y, cw, bh, fillColor=HexColor("#DCEBEC"),
                       strokeColor=accent, strokeWidth=0.6))
        for j in range(1, den):
            g.add(Line(60 + j * cw, y, 60 + j * cw, y + bh, strokeColor=GRID, strokeWidth=0.4))
        _t(g, 54, y + bh / 2 - 2.6, lab, 7, INK, "right")
    g.add(Line(60, 12, 60, h - 8, strokeColor=accent, strokeWidth=0.5, strokeDashArray=[1, 2]))
    _t(g, 60, 4, "0", 6.2, SOFT, "middle")
    _t(g, 60 + barw, 4, "1", 6.2, SOFT, "middle")
    d.add(g)
    return d


def dec_grid(w=150, h=150, shaded=37, col=BAND):
    d = _drawing(w, h)
    g = Group()
    cen = 8
    cw = (w - 22) / 10
    ch = (h - 30) / 10
    filled = shaded
    for r in range(10):
        for c in range(10):
            x = 11 + c * cw
            y = h - 20 - (r + 1) * ch
            g.add(Rect(x, y, cw, ch, fillColor=(HexColor("#DCEBEC") if filled > 0 else WHITE),
                       strokeColor=GRID, strokeWidth=0.35))
            filled -= 1
    _t(g, w / 2, 3, "%d hundredths shaded = %s" % (shaded, ("%.2f" % (shaded / 100.0))), 6.6, INK)
    d.add(g)
    return d


def long_division(num=3, den=8, w=170, h=92, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    _t(g, 26, h - 18, str(den), 9, INK, "right", True)
    g.add(Line(30, h - 26, w - 30, h - 26, strokeColor=INK, strokeWidth=0.9))
    g.add(Line(30, h - 26, 30, 8, strokeColor=INK, strokeWidth=0.9))
    _t(g, 40, h - 20, "%d.000" % num, 9, INK, "left", True)
    rows = ["0.  3  7  5", "", "", ""]
    _t(g, 40, h - 40, "0 . 3 7 5", 9, accent, "left", True)
    _t(g, 40, h - 56, "30", 8, INK, "left")
    _t(g, 40, h - 70, "60", 8, INK, "left")
    _t(g, 52, h - 84, "40", 8, INK, "left")
    d.add(g)
    return d


def percent_bar(w=300, h=96, vals=(("0%", 0.0), ("25%", 0.25), ("50%", 0.5), ("75%", 0.75), ("100%", 1.0)), accent=BAND):
    d = _drawing(w, h)
    g = Group()
    x0, bw, y = 24, w - 44, h - 52
    g.add(Rect(x0, y, bw, 20, fillColor=WHITE, strokeColor=GRID, strokeWidth=0.6))
    for k in range(5):
        g.add(Rect(x0 + bw * k / 4, y, bw / 4, 20,
                   fillColor=HexColor("#DCEBEC") if k < 2 else WHITE,
                   strokeColor=accent, strokeWidth=0.5))
    for lab, f in vals:
        x = x0 + bw * f
        g.add(Line(x, y - 3, x, y + 23, strokeColor=accent, strokeWidth=0.7))
        _t(g, x, y - 11, lab, 6.8, INK)
        _t(g, x, y + 30, ["0", "1/4", "1/2", "3/4", "1"][int(round(f * 4))], 7.2, BAND, bold=True)
    _t(g, x0, 6, "percentages, fractions and decimals name the same positions", 6.2, SOFT, "left")
    d.add(g)
    return d


def percent_grid(w=140, h=150, shaded=45, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    cw = (w - 20) / 10
    ch = (h - 34) / 10
    filled = shaded
    for r in range(10):
        for c in range(10):
            x = 10 + c * cw
            y = h - 24 - (r + 1) * ch
            g.add(Rect(x, y, cw, ch, fillColor=(HexColor("#DCEBEC") if filled > 0 else WHITE),
                       strokeColor=GRID, strokeWidth=0.35))
            filled -= 1
    _t(g, w / 2, h - 14, "one whole square = 100%", 6.6, INK)
    _t(g, w / 2, 5, "%d squares shaded = %d%% = 0.%02d" % (shaded, shaded, shaded), 6.6, accent)
    d.add(g)
    return d


def discount_chain(w=300, h=104, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    barw, bh = 190, 18
    x, y1, y2 = 66, h - 40, h - 74
    for y, frac, lab in ((y1, 0.8, "after 20% off"), (y2, 0.72, "after a further 10%")):
        g.add(Rect(x, y, barw, bh, fillColor=HexColor("#E7F1F1"), strokeColor=accent, strokeWidth=0.5))
        g.add(Rect(x, y, barw * frac, bh, fillColor=HexColor("#DCEBEC"), strokeColor=accent, strokeWidth=0.6))
        _t(g, x - 6, y + bh / 2 - 2.6, lab, 6.4, INK, "right")
        _t(g, x + barw * frac + 6, y + bh / 2 - 2.6, "%.0f%%" % (frac * 100), 6.6, accent, "left", True)
    _t(g, x, 10, "two successive reductions do not add up to 30%", 6.4, SOFT, "left")
    d.add(g)
    return d


def function_machine(inp="5", ops=("× 3", "+ 2"), out="17", w=280, h=90, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    bx, bw, bh, y = 66, 74, 34, h / 2 - 8
    g.add(Rect(bx, y, bw, bh, fillColor=HexColor("#E7F1F1"), strokeColor=accent, strokeWidth=0.8))
    _t(g, bx + bw / 2, y + bh / 2 - 3, ops[0], 8.4, INK)
    bx2 = bx + bw + 34
    g.add(Rect(bx2, y, bw, bh, fillColor=HexColor("#E7F1F1"), strokeColor=accent, strokeWidth=0.8))
    _t(g, bx2 + bw / 2, y + bh / 2 - 3, ops[1], 8.4, INK)
    _arrow(g, bx - 22, y + bh / 2, bx - 2, y + bh / 2)
    _arrow(g, bx + bw + 2, y + bh / 2, bx2 - 2, y + bh / 2)
    _arrow(g, bx2 + bw + 2, y + bh / 2, bx2 + bw + 24, y + bh / 2)
    _t(g, bx - 30, y + bh / 2 - 3, inp, 9.2, accent, bold=True)
    _t(g, bx2 + bw + 32, y + bh / 2 - 3, out, 9.2, accent, bold=True)
    _t(g, w / 2, 8, "each machine applies one operation; together they give the rule", 6.2, SOFT)
    d.add(g)
    return d


def equation_steps(w=290, h=100, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    rows = [("3x + 4 = 19", ""), ("3x = 15", "subtract 4 from both sides"),
            ("x = 5", "divide both sides by 3")]
    y = h - 22
    for eq, why in rows:
        g.add(Rect(20, y - 6, 118, 18, fillColor=WHITE, strokeColor=GRID, strokeWidth=0.4))
        _t(g, 26, y, eq, 8.4, accent, "left", True)
        if why:
            _t(g, 146, y, why, 6.6, SOFT, "left")
        y -= 26
    g.add(Line(14, y + 12, w - 14, y + 12, strokeColor=GRID, strokeWidth=0.4))
    d.add(g)
    return d


def angle_types(w=320, h=90, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    specs = [(30, "acute", "< 90°"), (90, "right", "= 90°"), (135, "obtuse", "> 90°"), (250, "reflex", "> 180°")]
    step = w / len(specs)
    for k, (deg, name, note) in enumerate(specs):
        cx, cy = step * (k + 0.5), 42
        r = 22
        g.add(Line(cx, cy, cx + r * 1.35, cy, strokeColor=INK, strokeWidth=1.0))
        g.add(Line(cx, cy, cx + r * 1.35 * math.cos(math.radians(deg)),
                   cy + r * 1.35 * math.sin(math.radians(deg)), strokeColor=INK, strokeWidth=1.0))
        col = accent if k != 3 else BAND2
        if deg < 180:
            g.add(Wedge(cx, cy, r * 0.55, 0, deg, fillColor=HexColor("#DCEBEC"),
                        strokeColor=col, strokeWidth=0.6))
        else:
            g.add(Wedge(cx, cy, r * 0.55, 0, deg, fillColor=HexColor("#FBF0DF"),
                        strokeColor=col, strokeWidth=0.6))
            g.add(Rect(cx, cy, 3.2, 3.2, fillColor=INK, strokeColor=INK))
        _t(g, cx + 8, cy - 14, name, 6.8, col, bold=True)
        _t(g, cx + 8, cy - 23, note, 6.0, SOFT)
    _t(g, 4, h - 8, "angles are measured in degrees, anticlockwise from a fixed arm", 6.2, SOFT, "left")
    d.add(g)
    return d


def triangle_sum(w=250, h=140, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    A = (30, 26)
    B = (210, 26)
    C = (120, 108)
    g.add(Polygon([A[0], A[1], B[0], B[1], C[0], C[1]], fillColor=HexColor("#EFF6F6"),
                  strokeColor=INK, strokeWidth=1.0))
    g.add(Line(30, 108, 210, 108, strokeColor=accent, strokeWidth=0.9,
               strokeDashArray=[3, 2]))
    for pt, lab, col in ((A, "a", BAND), (B, "b", BAND), (C, "c", BAND)):
        g.add(Circle(pt[0], pt[1], 2.2, fillColor=col, strokeColor=col))
    _t(g, 22, 20, "a", 8.4, BAND, bold=True)
    _t(g, 214, 20, "b", 8.4, BAND, bold=True)
    _t(g, 120, 116, "c", 8.4, BAND, bold=True)
    _t(g, 120, 118, "", 6, SOFT)
    _t(g, w / 2, 6, "a + b + c = 180°", 8.2, accent)
    d.add(g)
    return d


def perpendicular_bisector(w=230, h=140, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    A, B = (46, 92), (186, 52)
    g.add(Line(A[0], A[1], B[0], B[1], strokeColor=INK, strokeWidth=1.2))
    r = math.hypot(B[0] - A[0], B[1] - A[1])
    for centre in (A, B):
        g.add(Circle(centre[0], centre[1], r, strokeColor=accent, strokeWidth=0.7,
                     fillColor=None))
    mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
    dx, dy = B[0] - A[0], B[1] - A[1]
    g.add(Line(mx - dy * 0.55, my + dx * 0.55, mx + dy * 0.55, my - dx * 0.55,
               strokeColor=BAND2, strokeWidth=1.0))
    g.add(Circle(A[0], A[1], 2.0, fillColor=INK, strokeColor=INK))
    g.add(Circle(B[0], B[1], 2.0, fillColor=INK, strokeColor=INK))
    _t(g, A[0] - 8, A[1] + 4, "A", 8, INK, bold=True)
    _t(g, B[0] + 8, B[1] + 4, "B", 8, INK, bold=True)
    _t(g, w - 6, 8, "equal arcs from A and from B", 6.2, SOFT, "right")
    d.add(g)
    return d


def venn_regions(w=290, h=150, a="A", b="B", inner=("A only", "both", "B only"), accent=BAND):
    d = _drawing(w, h)
    g = Group()
    g.add(Rect(6, 6, w - 12, h - 12, fillColor=HexColor("#FBFCFC"),
               strokeColor=SOFT, strokeWidth=0.7))
    cx, cy = w / 2, h / 2 - 2
    r = min(h, w) * 0.30
    g.add(Circle(cx - r * 0.62, cy, r, fillColor=HexColor("#E7F1F1"),
                 strokeColor=BAND, strokeWidth=1.0))
    g.add(Circle(cx + r * 0.62, cy, r, fillColor=HexColor("#FBF0DF"),
                 strokeColor=BAND2, strokeWidth=1.0))
    _t(g, cx - r * 1.15, cy + r - 4, a, 8, BAND, bold=True)
    _t(g, cx + r * 1.15, cy + r - 4, b, 8, BAND2, bold=True)
    _t(g, 12, h - 16, "U", 7.4, SOFT, bold=True)
    _t(g, w * 0.34, h * 0.55, inner[0], 6.6, INK)
    _t(g, w * 0.5, h * 0.55, inner[1], 6.6, INK, bold=True)
    _t(g, w * 0.66, h * 0.55, inner[2], 6.6, INK)
    _t(g, w * 0.5, 12, "outside both sets", 6.2, SOFT)
    d.add(g)
    return d


def classification_tree(w=290, h=140, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    root = (w / 2, h - 16)
    g.add(Rect(root[0] - 32, root[1] - 8, 64, 18, fillColor=HexColor("#E7F1F1"),
               strokeColor=accent, strokeWidth=0.8))
    _t(g, root[0], root[1], "whole numbers", 7.0, accent, bold=True)
    kids = [(w * 0.25, "even"), (w * 0.75, "odd")]
    for x, lab in kids:
        g.add(Line(root[0], root[1] - 8, x, h - 56, strokeColor=SOFT, strokeWidth=0.7))
        g.add(Rect(x - 22, h - 66, 44, 16, fillColor=WHITE, strokeColor=accent, strokeWidth=0.7))
        _t(g, x, h - 62, lab, 6.8, INK)
    leaves = [(w * 0.13, "multiple of 4"), (w * 0.37, "not a multiple of 4"),
              (w * 0.63, "prime"), (w * 0.87, "composite")]
    for i, (x, lab) in enumerate(leaves):
        px = kids[i // 2][0]
        g.add(Line(px, h - 66, x, h - 96, strokeColor=SOFT, strokeWidth=0.7))
        g.add(Rect(x - 30, h - 106, 60, 14, fillColor=WHITE, strokeColor=GRID, strokeWidth=0.6))
        _t(g, x, h - 102, lab, 6.0, SOFT)
    _t(g, 6, 8, "every branch divides the previous group into two non-overlapping parts", 6.0, SOFT, "left")
    d.add(g)
    return d


def triangle_area(w=240, h=120, base=160, height=64, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    x0 = (w - base) / 2
    y0 = 22
    apex = (x0 + base * 0.34, y0 + height)
    g.add(Polygon([x0, y0, x0 + base, y0, apex[0], apex[1]], fillColor=HexColor("#EFF6F6"),
                  strokeColor=INK, strokeWidth=1.0))
    g.add(Line(apex[0], apex[1], apex[0], y0, strokeColor=accent, strokeWidth=0.9,
               strokeDashArray=[3, 2]))
    g.add(Rect(apex[0], y0, 4.5, 4.5, fillColor=None, strokeColor=accent, strokeWidth=0.6))
    _t(g, x0 + base / 2, y0 - 10, "base", 7.4, INK)
    _t(g, apex[0] + 5, y0 + height / 2, "height", 7.0, accent, "left", True)
    _t(g, w / 2, h - 8, "area = ½ × base × height", 7.6, accent)
    d.add(g)
    return d


def compound_rect(w=260, h=140, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    ox, oy = 40, 24
    # L-shape: 8 by 5 with a 3 by 2 bite
    g.add(Polygon([ox, oy, ox + 160, oy, ox + 160, oy + 100, ox + 60, oy + 100,
                   ox + 60, oy + 40, ox, oy + 40],
                  fillColor=HexColor("#EFF6F6"), strokeColor=INK, strokeWidth=1.0))
    g.add(Line(ox + 60, oy + 100, ox + 60, oy + 40, strokeColor=accent, strokeWidth=0.7,
               strokeDashArray=[3, 2]))
    g.add(Line(ox, oy + 40, ox + 160, oy + 40, strokeColor=accent, strokeWidth=0.7,
               strokeDashArray=[3, 2]))
    _t(g, ox + 80, oy - 10, "10 cm", 7.0, INK)
    _t(g, ox - 12, oy + 50, "6 cm", 7.0, INK, "right")
    _t(g, ox + 170, oy + 70, "4 cm", 7.0, INK, "left")
    _t(g, ox + 30, oy + 71, "2 cm", 6.6, accent)
    _t(g, w - 6, 8, "split the shape into rectangles, or subtract the missing part", 6.0, SOFT, "right")
    d.add(g)
    return d


def unit_ladder(w=250, h=110, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    rows = [("length", "1 cm = 10 mm", "× 10"),
            ("area", "1 cm² = 100 mm²", "× 100"),
            ("volume", "1 cm³ = 1,000 mm³", "× 1,000")]
    y = h - 26
    for kind, fact, mult in rows:
        g.add(Rect(14, y - 6, 66, 18, fillColor=HexColor("#E7F1F1"), strokeColor=accent,
                   strokeWidth=0.6))
        _t(g, 47, y, kind, 7.0, accent, bold=True)
        _t(g, 90, y, fact, 7.0, INK, "left")
        _t(g, w - 16, y, mult, 7.0, SOFT, "right")
        y -= 30
    d.add(g)
    return d


def misleading_bars(w=300, h=120, accent=BAND, accent2=BAND2):
    d = _drawing(w, h)
    g = Group()
    sets = [((40, 44, 46), accent, "axis from 0"), ((10, 22, 34), accent2, "axis from 35")]
    for k, (vals, col, note) in enumerate(sets):
        x0 = 18 + k * (w / 2)
        base = 24
        bw = 18
        for j, v in enumerate(vals):
            g.add(Rect(x0 + j * (bw + 8), base, bw, v, fillColor=HexColor("#DCEBEC"),
                       strokeColor=col, strokeWidth=0.8))
        g.add(Line(x0 - 4, base, x0 + 3 * (bw + 8), base, strokeColor=INK, strokeWidth=0.9))
        _t(g, x0 + 1.5 * (bw + 8), base - 10, note, 6.2, col)
    _t(g, w / 2, h - 10, "the same three counts, drawn on two different vertical scales", 6.2, SOFT)
    d.add(g)
    return d


def frequency_table(w=280, h=118, accent=BAND):
    d = _drawing(w, h)
    g = Group()
    rows = [("0", "4"), ("1", "9"), ("2", "12"), ("3", "7"), ("4", "3")]
    cw, rh = 70, 16
    x0, y0 = 60, h - 26
    for j, head in enumerate(("number of pets", "frequency")):
        g.add(Rect(x0 + j * 110, y0, 110, rh, fillColor=accent, strokeColor=accent,
                   strokeWidth=0.4))
        _t(g, x0 + j * 110 + 55, y0 + 5, head, 6.4, WHITE, bold=True)
    for i, (v, f) in enumerate(rows):
        y = y0 - (i + 1) * rh
        for j, cell in enumerate((v, f)):
            g.add(Rect(x0 + j * 110, y, 110, rh, fillColor=WHITE, strokeColor=GRID,
                       strokeWidth=0.4))
            _t(g, x0 + j * 110 + 55, y + 5, cell, 6.8, INK)
    _t(g, x0 + 240, y0 - 6 * rh + 3, "total 35", 6.6, SOFT, "right")
    d.add(g)
    return d

def polygon_diagonals(n=6, w=250, h=150, accent=BAND):
    """Regular n-gon with all diagonals from one vertex, showing n-2 triangles."""
    d = _drawing(w, h)
    g = Group()
    cx, cy, r = w / 2 + 6, h / 2, min(w, h) * 0.40
    pts = [(cx + r * math.cos(math.radians(90 + 360 * i / n)),
            cy + r * math.sin(math.radians(90 + 360 * i / n))) for i in range(n)]
    flat = [c for p in pts for c in p]
    g.add(Polygon(flat, fillColor=HexColor("#F4F8F9"), strokeColor=INK, strokeWidth=1.0))
    for i in range(2, n - 1):
        g.add(Line(pts[0][0], pts[0][1], pts[i][0], pts[i][1],
                   strokeColor=accent, strokeWidth=0.8, strokeDashArray=[2.2, 1.8]))
    for i, p in enumerate(pts):
        g.add(String(p[0] + (4 if p[0] >= cx else -10), p[1] + (4 if p[1] >= cy else -8),
                     "ABCDEFGH"[i], fontName="Sans", fontSize=6.6, fillColor=SOFT))
    _t(g, 8, 10, "%d sides, %d triangles" % (n, n - 2), 7.0, accent, "left", bold=True)
    d.add(g)
    return d
