#!/usr/bin/env python3
"""Render a StashSmart social image (1080x1350 JPEG, Instagram 4:5),
following StashSmart Brand Guidelines, Edition 02 (Nov 2026).

Usage:
  python3 scripts/make_image.py spec.json out.jpg

spec.json fields:
  style      "paper"  Paper ground, Ink type (default, most posts)
             "cyan"   Cyan 900 -> 500 feature-card gradient, reversed lockup
  kicker     short caption line, set in caps (e.g. "Did you know")
  highlight  optional big number, e.g. "$2,913.00". Set in marigold: use ONLY
             for money saved/wasted or something running out (one per post)
  headline   the main line (Semibold), sentence case, no exclamation marks
  body       optional supporting line (Regular)
  tip        optional italic line (tips, quotes)
  source     optional source credit for facts
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FONTS = os.path.join(ROOT, "fonts")
ICON = os.path.join(ROOT, "brand", "app-icon-512.png")
W, H = 1080, 1350
PAD = 96

# Brand Guidelines Ed. 02, section 04
PAPER = (0xF3, 0xF2, 0xF2)
SURFACE = (0xEA, 0xE9, 0xE9)
INK = (0x20, 0x1E, 0x1D)
MUTED = (0x5F, 0x5B, 0x59)
LINE = (0xD6, 0xD4, 0xD3)
CYAN_200 = (0xCB, 0xEE, 0xFF)
CYAN_500 = (0x00, 0x88, 0xB0)
CYAN_700 = (0x00, 0x67, 0x86)
CYAN_900 = (0x0A, 0x30, 0x3E)
MARIGOLD_500 = (0xF2, 0xB7, 0x05)
MARIGOLD_700 = (0x8A, 0x64, 0x00)
WHITE = (255, 255, 255)

SCHEMES = {
    "paper": dict(fg=INK, stash=INK, smart=CYAN_700, kicker=MUTED, body=INK, tip=MUTED,
                  money=MARIGOLD_700, foot=MUTED, rule=LINE),
    "cyan":  dict(fg=WHITE, stash=WHITE, smart=CYAN_200, kicker=CYAN_200, body=(0xE9, 0xF8, 0xFF),
                  tip=CYAN_200, money=MARIGOLD_500, foot=CYAN_200, rule=(0x38, 0xA6, 0xCF)),
}

REG = "SourceSerif4-Regular.otf"
SEMI = "SourceSerif4-Semibold.otf"
ITAL = "SourceSerif4-It.otf"
DISP = "SourceSerif4Display-Semibold.otf"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def wrap(d, text, f, max_w):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if d.textlength(trial, font=f) <= max_w:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit(d, text, fname, max_w, max_h, start, minimum, lh):
    size = start
    while size > minimum:
        f = font(fname, size)
        lines = wrap(d, text, f, max_w)
        if len(lines) * size * lh <= max_h:
            return f, lines, size
        size -= 2
    f = font(fname, minimum)
    return f, wrap(d, text, f, max_w), minimum


def background(style):
    if style == "cyan":
        # Feature-card gradient: Cyan 900 (top-left) -> Cyan 500 (bottom-right)
        img = Image.new("RGB", (W, H))
        px = img.load()
        for y in range(H):
            for x in range(W):
                t = (x / W * 0.35 + y / H * 0.65)
                px[x, y] = tuple(int(a + (b - a) * t) for a, b in zip(CYAN_900, CYAN_500))
        return img
    return Image.new("RGB", (W, H), PAPER)


def lockup(img, d, s, x, y):
    """Icon tile + wordmark. Tile ~1.4x the wordmark cap height, gap = 1/4 tile."""
    size = 46
    f_stash, f_smart = font(SEMI, size), font(ITAL, size)
    cap = f_stash.getbbox("S")[3] - f_stash.getbbox("S")[1]
    tile = int(round(cap * 1.4 * 1.6))  # a touch larger so the icon reads on a phone feed
    icon = Image.open(ICON).convert("RGB").resize((tile, tile), Image.LANCZOS)
    img.paste(icon, (x, y))
    tx = x + tile + tile // 4
    # vertically centre cap height on the tile
    top_offset = f_stash.getbbox("S")[1]
    ty = y + (tile - cap) // 2 - top_offset
    d.text((tx, ty), "Stash", font=f_stash, fill=s["stash"])
    tx += d.textlength("Stash", font=f_stash)
    d.text((tx, ty), "Smart", font=f_smart, fill=s["smart"])
    return y + tile


def render(spec, out):
    style = spec.get("style", "paper")
    s = SCHEMES.get(style, SCHEMES["paper"])
    img = background(style)
    d = ImageDraw.Draw(img)
    maxw = W - 2 * PAD

    y = lockup(img, d, s, PAD, PAD) + 150

    kicker = spec.get("kicker", "")
    if kicker:
        kf = font(SEMI, 30)
        x = PAD
        for ch in kicker.upper():  # letter-spaced caps (caption style)
            d.text((x, y), ch, font=kf, fill=s["kicker"])
            x += d.textlength(ch, font=kf) + 4
        y += 76

    hl = spec.get("highlight")
    if hl:
        hf, hlines, hs = fit(d, hl, DISP, maxw, 200, 170, 90, 1.05)
        for ln in hlines:
            d.text((PAD, y), ln, font=hf, fill=s["money"])
            y += int(hs * 1.05)
        y += 24

    body, tip = spec.get("body", ""), spec.get("tip", "")
    reserve = (210 if body else 0) + (90 if tip else 0)
    limit = H - 190 - reserve - y
    start = 92 if not hl else 72
    f, lines, sz = fit(d, spec["headline"], SEMI, maxw, limit, start, 52, 1.12)
    for ln in lines:
        d.text((PAD, y), ln, font=f, fill=s["fg"])
        y += int(sz * 1.12)

    if body:
        y += 34
        bf, blines, bs = fit(d, body, REG, maxw, H - 190 - (90 if tip else 0) - y, 44, 32, 1.4)
        for ln in blines:
            d.text((PAD, y), ln, font=bf, fill=s["body"])
            y += int(bs * 1.4)

    if tip:
        y += 24
        tf, tlines, ts = fit(d, tip, ITAL, maxw, H - 190 - y, 38, 28, 1.35)
        for ln in tlines:
            d.text((PAD, y), ln, font=tf, fill=s["tip"])
            y += int(ts * 1.35)

    # Footer: rule, then caption-style line
    d.line([(PAD, H - 150), (W - PAD, H - 150)], fill=s["rule"], width=2)
    ff = font(SEMI, 24)
    x = PAD
    for ch in "COMING SOON ON IPHONE  ·  @STASHSMART.APP":
        d.text((x, H - 112), ch, font=ff, fill=s["foot"])
        x += d.textlength(ch, font=ff) + 2
    src = spec.get("source")
    if src:
        sf = font(ITAL, 24)
        txt = "Source: " + src
        tw = d.textlength(txt, font=sf)
        if x + 40 + tw > W - PAD:
            d.text((W - PAD - tw, H - 76), txt, font=sf, fill=s["foot"])
        else:
            d.text((W - PAD - tw, H - 112), txt, font=sf, fill=s["foot"])

    img.save(out, "JPEG", quality=92, optimize=True)


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        render(json.load(fh), sys.argv[2])
    print("wrote", sys.argv[2])
