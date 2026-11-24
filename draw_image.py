#!/usr/bin/env python3
"""Draw the 23 Nov 2026 news front page as a 1024x1024 PNG (PIL, no network).

Layout differs from the 24 Nov entry: a dark navy masthead band with a gold
date, a full-width lead card, a three-column row, then a full-width bottom
card, so the two entries are not near-duplicates.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W = H = 1024
BG = (245, 240, 228)      # newsprint cream
NAVY = (18, 32, 62)
GOLD = (212, 175, 55)
INK = (24, 24, 24)
BODY = (58, 56, 50)
MUTED = (110, 108, 100)
RULE = (198, 188, 166)
CARD = (255, 253, 247)
RED = (178, 34, 34)
BLUE = (30, 64, 175)
TEAL = (13, 110, 110)
ORANGE = (194, 65, 12)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    # Pure pixel-width word wrap: build each line by measured width so no
    # line is ever split mid-word or broken awkwardly by a character count.
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split():
            trial = f"{cur} {w}".strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
M = 44  # margin

# ---- Navy masthead band ----
d.rectangle([0, 0, W, 168], fill=NAVY)
d.text((M, 22), "THE WORLD IN ONE DAY", font=font(FB, 52), fill=(255, 255, 255))
d.text((M, 88), "Monday 23 November 2026", font=font(FB, 40), fill=GOLD)
d.text((M, 136), "Five stories that shaped the world today  •  One page, one day",
       font=font(SR, 20), fill=(200, 205, 220))

# ---- Lead story: full-width card ----
y = 190
d.rounded_rectangle([M, y, W - M, y + 210], radius=10, fill=CARD, outline=RULE, width=2)
d.rectangle([M, y, M + 10, y + 210], fill=RED)
d.text((M + 28, y + 14), "UKRAINE  —  OFF LIBYA", font=font(SB, 23), fill=RED)
d.text((M + 28, y + 48), "Ukraine sinks Russian warship off Libya",
       font=font(FB, 33), fill=INK)
lead = ("President Zelenskyy confirmed on Monday that Ukrainian naval drones sank "
        "the Russian corvette Merkury off Libya and hit a second ship, the dry "
        "cargo vessel Angara.")
for i, line in enumerate(wrap(d, lead, font(SR, 22), W - 2 * M - 56)):
    d.text((M + 28, y + 98 + i * 29), line, font=font(SR, 22), fill=BODY)

# ---- Three-column row ----
stories = [
    ("MARKETS", BLUE, "Nvidia brings back Jensen Huang",
     "Nvidia reinstated Jensen Huang as chief executive on Monday. "
     "Shares jumped 31%, their best day since 2003."),
    ("EUROPE", TEAL, "NATO sends radar plane to Poland",
     "NATO will send an AWACS early-warning aircraft to Poland after three "
     "Russian missiles landed there on Friday, Poland's deputy defence "
     "minister said on Monday."),
    ("UNITED STATES", INK, "Trump orders faster federal executions",
     "Trump attacked Newsom's commutation of 548 death sentences and ordered "
     "faster federal executions."),
]
gy = 420
ch = 290
gap = 20
cw = (W - 2 * M - 2 * gap) // 3
for i, (tag, color, head, body) in enumerate(stories):
    x = M + i * (cw + gap)
    d.rounded_rectangle([x, gy, x + cw, gy + ch], radius=10, fill=CARD, outline=RULE, width=2)
    d.rectangle([x + 20, gy + 18, x + 28, gy + 38], fill=color)
    d.text((x + 38, gy + 14), tag, font=font(SB, 19), fill=color)
    lines = wrap(d, head, font(FB, 24), cw - 40)
    for j, line in enumerate(lines):
        d.text((x + 20, gy + 50 + j * 31), line, font=font(FB, 24), fill=INK)
    by = gy + 50 + len(lines) * 31 + 8
    for j, line in enumerate(wrap(d, body, font(SR, 19), cw - 40)):
        d.text((x + 20, by + j * 25), line, font=font(SR, 19), fill=BODY)

# ---- Bottom story: full-width card ----
y = 730
d.rounded_rectangle([M, y, W - M, y + 160], radius=10, fill=CARD, outline=RULE, width=2)
d.rectangle([M, y, M + 10, y + 160], fill=ORANGE)
d.text((M + 28, y + 14), "INDONESIA", font=font(SB, 23), fill=ORANGE)
d.text((M + 28, y + 48), "24 dead in Indonesia factory fire",
       font=font(FB, 33), fill=INK)
body = ("Indonesia confirmed on Monday that 24 people died in a fire at a candy "
        "factory in Banten. About 30 workers are still missing.")
for i, line in enumerate(wrap(d, body, font(SR, 22), W - 2 * M - 56)):
    d.text((M + 28, y + 98 + i * 29), line, font=font(SR, 22), fill=BODY)

# ---- Footer ----
fy = 908
d.line([(M, fy), (W - M, fy)], fill=RULE, width=2)
d.text((M, fy + 12), "Sources: Reuters, Al Jazeera, Ukrinform, Ukrainska Pravda — reported 23 Nov 2026",
       font=font(SR, 18), fill=MUTED)
d.text((M, fy + 38), "All five stories happened or were first reported on Monday 23 November 2026.",
       font=font(SR, 18), fill=MUTED)

img.save("/home/hatch/workspace/makefun/news-image-20261123/entry/entry.png", optimize=True)
print("saved")
