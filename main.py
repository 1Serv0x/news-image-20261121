#!/usr/bin/env python3
"""The World in One Image -- 21 November 2026.

A one-page newspaper front page drawn entirely in code with Pillow.
No photos, no network calls, no copied assets: every pixel on the
page is drawn by the functions below. Run `python3 main.py` and it
writes entry.png (1024 x 1024) next to this file.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or HERE
OUT_PATH = os.path.join(OUT_DIR, "entry.png")

PAGE_W, PAGE_H = 1024, 1024
PAPER = (250, 246, 238)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (28, 52, 86)
TEAL = (14, 110, 110)
MUSTARD = (198, 142, 28)
GREY = (112, 112, 108)


def load_font(weight, size):
    base = "/usr/share/fonts/truetype/dejavu"
    tries = [
        os.path.join(base, "DejaVuSans-%s.ttf" % weight),
        os.path.join(base, "DejaVuSans%s.ttf" % weight),
        os.path.join(base, "DejaVuSans.ttf"),
    ]
    for path in tries:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def bold(size):
    return load_font("Bold", size)


def plain(size):
    return load_font("", size)


def wrap_text(draw, text, fnt, width):
    lines = []
    current = ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, gap=6):
    for line in wrap_text(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def headline(draw, x, y, text, size, width, fill=INK):
    return para(draw, x, y, text, bold(size), width, fill=fill, gap=2)


def kicker(draw, x, y, text, color=RED, size=17):
    fnt = bold(size)
    draw.text((x, y), text, font=fnt, fill=color)
    return y + size + 8


def rule(draw, x, y, width, fill=INK, px=2):
    draw.rectangle([x, y, x + width, y + px], fill=fill)
    return y + px


def globe_panel(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=NAVY)
    cx, cy = x + w // 2, y + h // 2 - 12
    for r, col in ((100, (58, 92, 130)), (76, (88, 128, 168)), (52, (150, 180, 205))):
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=3)
    draw.ellipse([cx - 112, cy - 112, cx + 112, cy + 112], outline=(235, 235, 230), width=2)
    draw.ellipse([cx - 138, cy - 34, cx + 138, cy + 34], outline=MUSTARD, width=4)
    for dx, dy in ((-58, -34), (48, -58), (78, 26), (-34, 58)):
        draw.ellipse([cx + dx - 7, cy + dy - 7, cx + dx + 7, cy + dy + 7], fill=RED)
    draw.text((x + 16, y + h - 34), "TALKS END WITHOUT A DEAL", font=bold(17), fill=(255, 255, 255))


def story_column(draw, x, y, w, color, tag, head, body):
    draw.rectangle([x, y, x + w, y + 6], fill=color)
    y += 16
    y = kicker(draw, x, y, tag, color=color, size=16)
    y = headline(draw, x, y, head, 25, w)
    y += 4
    y = para(draw, x, y, body, plain(16), w, fill=(52, 52, 50), gap=4)
    return y


def main():
    page = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    d = ImageDraw.Draw(page)
    d.rectangle([10, 10, PAGE_W - 11, PAGE_H - 11], outline=INK, width=2)

    # masthead band
    d.rectangle([10, 10, PAGE_W - 11, 118], fill=INK)
    d.text((PAGE_W // 2, 28), "THE WORLD IN ONE IMAGE", font=bold(52),
           fill=(255, 255, 255), anchor="ma")
    d.text((PAGE_W // 2, 88),
           "SATURDAY, 21 NOVEMBER 2026  -  ONE DAY, ONE PAGE, THE WHOLE WORLD",
           font=plain(16), fill=(210, 210, 205), anchor="ma")

    # lead story
    y = 142
    y = kicker(d, 48, y, "DIPLOMACY  -  GENEVA", color=RED, size=17)
    y = headline(d, 48, y, "US-IRAN TALKS STALL OVER URANIUM STOCKPILE", 40, 592)
    y += 8
    y = para(d, 48, y,
             "Negotiations stall as Tehran refuses terms Washington calls "
             "acceptable, and mediators warn they cannot rule out a return "
             "to conflict.", plain(19), 592, fill=(40, 40, 38), gap=6)
    y += 10
    y = para(d, 48, y,
             "President Trump said Iran wants an agreement but will not "
             "accept the US terms on its enriched uranium. Envoys left "
             "Geneva with no date set for the next round.",
             plain(16), 592, fill=(70, 70, 66), gap=5)
    globe_panel(d, 664, 142, 312, 238)

    # markets strip
    d.rectangle([28, 492, 996, 544], fill=INK)
    d.text((512, 512),
           "MARKETS  -  WALL STREET TUMBLES ON AI SELLOFF; S&P 500 AND DOW IN CORRECTION",
           font=bold(18), fill=(255, 255, 255), anchor="ma")

    # three stories across the page
    y0 = 574
    story_column(d, 48, y0, 288, RED, "YEMEN",
                 "STRIKES KILL 41 AS HOUTHI FIRE HITS SAUDI PLANTS",
                 "Saudi-attributed airstrikes kill 41 across Yemen, "
                 "including 11 children. The Houthis say they struck a "
                 "power plant and a port in south-western Saudi Arabia.")
    story_column(d, 368, y0, 288, NAVY, "EUROPE",
                 "EU AND BRITAIN CLINCH POST-BREXIT RESET DEAL",
                 "Brussels and London agree to ease agri-food trade, link "
                 "carbon markets, and let young people live, work or study "
                 "on either side.")
    story_column(d, 688, y0, 288, TEAL, "CLIMATE",
                 "COP31 DEADLOCKED OVER FOSSIL FUELS",
                 "Climate talks run into overtime as countries clash over "
                 "fossil fuels, with no deal in sight at the final stage.")

    # also-in-the-world strip
    y = 892
    rule(d, 48, y, 928, fill=GREY, px=1)
    y += 14
    y = kicker(d, 48, y, "ALSO IN THE WORLD", color=INK, size=16)
    para(d, 48, y,
         "6.8 quake shakes Peru as lawmakers flee congress  -  SpaceX "
         "Dragon leaves the space station  -  FBI probes a breach of its "
         "criminal database  -  India lead New Zealand by 118 in the "
         "first Test.",
         plain(16), 928, fill=(52, 52, 50), gap=5)

    # footer
    d.text((512, 978),
           "Drawn entirely in code from the day's reporting - no photos, no wire copy.",
           font=plain(14), fill=GREY, anchor="ma")

    page.save(OUT_PATH)
    print("wrote", OUT_PATH, page.size)


if __name__ == "__main__":
    main()
