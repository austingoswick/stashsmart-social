#!/usr/bin/env python3
"""Render a branded StashSmart social image (1080x1350 JPEG, Instagram 4:5).

Usage:
  python3 scripts/make_image.py spec.json out.jpg

spec.json fields:
  style    "fact" | "feature" | "hook"   (sets the color scheme)
  kicker   short label above the headline, e.g. "DID YOU KNOW?"
  headline the big text (keep it under ~12 words)
  body     optional supporting line (under ~25 words)
  source   optional source credit shown small at the bottom (use for facts)
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "fonts")
W, H = 1080, 1350
PAD = 96

# Brand palette
GREEN = (31, 107, 79)
DEEP = (18, 64, 48)
MINT = (232, 245, 236)
CREAM = (255, 250, 240)
ORANGE = (244, 163, 64)
INK = (24, 32, 28)
WHITE = (255, 255, 255)

SCHEMES = {
    "fact":    dict(bg=GREEN, fg=WHITE, kicker=ORANGE, body=(214, 236, 224), accent=ORANGE, foot=(190, 222, 205)),
    "feature": dict(bg=CREAM, fg=INK, kicker=GREEN, body=(70, 84, 76), accent=GREEN, foot=(110, 122, 115)),
    "hook":    dict(bg=ORANGE, fg=DEEP, kicker=WHITE, body=(70, 50, 20), accent=DEEP, foot=(110, 70, 20)),
}


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def wrap(draw, text, fnt, max_w):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def fit(draw, text, fname, max_w, max_h, start, minimum, spacing=1.12):
    size = start
    while size >= minimum:
        f = font(fname, size)
        lines = wrap(draw, text, f, max_w)
        h = len(lines) * size * spacing
        if h <= max_h:
            return f, lines, size
        size -= 4
    f = font(fname, minimum)
    return f, wrap(draw, text, f, max_w), minimum


def draw_logo(d, x, y, c, accent):
    # Simple mark: rounded jar with a check, then the wordmark.
    d.rounded_rectangle([x, y, x + 56, y + 64], radius=14, outline=c, width=6)
    d.rectangle([x + 10, y - 8, x + 46, y + 4], fill=c)
    d.line([(x + 14, y + 34), (x + 25, y + 46), (x + 43, y + 22)], fill=accent, width=7)
    d.text((x + 76, y + 6), "StashSmart", font=font("InterDisplay-ExtraBold.otf", 46), fill=c)


def render(spec, out):
    s = SCHEMES.get(spec.get("style", "feature"), SCHEMES["feature"])
    img = Image.new("RGB", (W, H), s["bg"])
    d = ImageDraw.Draw(img)

    # Decorative corner circle
    d.ellipse([W - 300, -220, W + 220, 300], fill=tuple(min(255, int(v * 0.92 + a * 0.08)) for v, a in zip(s["bg"], s["accent"])))

    draw_logo(d, PAD, PAD, s["fg"], s["accent"])

    y = 330
    kicker = spec.get("kicker", "").upper()
    if kicker:
        kf = font("Inter-SemiBold.otf", 38)
        d.text((PAD, y), kicker, font=kf, fill=s["kicker"])
        y += 70
        d.rectangle([PAD, y, PAD + 120, y + 8], fill=s["accent"])
        y += 56

    body = spec.get("body", "")
    body_h = 260 if body else 0
    hf, hlines, hs = fit(d, spec["headline"], "InterDisplay-ExtraBold.otf", W - 2 * PAD, 1040 - y - body_h, 124, 60)
    for ln in hlines:
        d.text((PAD, y), ln, font=hf, fill=s["fg"])
        y += int(hs * 1.12)

    if body:
        y += 40
        bf, blines, bs = fit(d, body, "Inter-Medium.otf", W - 2 * PAD, 1150 - y, 46, 30, 1.35)
        for ln in blines:
            d.text((PAD, y), ln, font=bf, fill=s["body"])
            y += int(bs * 1.35)

    # Footer
    ff = font("Inter-SemiBold.otf", 30)
    d.line([(PAD, H - 150), (W - PAD, H - 150)], fill=s["foot"], width=2)
    d.text((PAD, H - 118), "Coming soon  ·  @stashsmart.app", font=ff, fill=s["foot"])
    src = spec.get("source")
    if src:
        sf = font("Inter-Medium.otf", 24)
        txt = "Source: " + src
        tw = d.textlength(txt, font=sf)
        if tw > W - 2 * PAD - 520:
            sf = font("Inter-Medium.otf", 20)
            tw = d.textlength(txt, font=sf)
        d.text((W - PAD - tw, H - 112), txt, font=sf, fill=s["foot"])

    img.save(out, "JPEG", quality=90, optimize=True)


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        render(json.load(fh), sys.argv[2])
    print("wrote", sys.argv[2])
