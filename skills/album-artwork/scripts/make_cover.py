#!/usr/bin/env python3
"""
Build a designed album cover from a chosen chapter photo — title in
Marcellus over a darkened band, "A Me & My Old Man production" credit
bottom right in a solid backing plate. Used to replace Chapter 1's
artwork (which Apple Music displays as the album cover) with something
better than a bare, uncredited photo.

Usage:
    python3 make_cover.py \
        --image "/path/to/Ch09 photo.jpg" \
        --title "Vaughan Griffiths" \
        --subtitle "Life Stories of the Old Bear" \
        --out "/tmp/cover.jpg"

Fonts: needs Marcellus-Regular.ttf locally. If not already present at
~/Library/Fonts or the path given by --font, download it once from
Google Fonts (see SKILL.md).
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

CREAM = (249, 246, 241)
INK_SHADOW = (8, 9, 6)
INK_BG = (18, 15, 11)

DEFAULT_CREDIT = "A Me & My Old Man production"


def draw_text_with_shadow(draw_obj, xy, text, font, fill, shadow, align="left", anchor=None, shadow_offset=3):
    x, y = xy
    for dx, dy in [(shadow_offset, shadow_offset), (shadow_offset, 0), (0, shadow_offset), (-1, shadow_offset)]:
        draw_obj.text((x + dx, y + dy), text, font=font, fill=shadow, align=align, anchor=anchor)
    draw_obj.text((x, y), text, font=font, fill=fill, align=align, anchor=anchor)


def build_cover(image_path, title, subtitle, out_path, font_path, credit=DEFAULT_CREDIT, title_y=0.0217):
    img = Image.open(image_path).convert("RGB")
    w, h = img.size

    # Square crop, top-anchored: keeps a top foliage/sky band plus faces,
    # drops whatever's at the very bottom (feet, mugs, etc). If the source
    # photo is already square this is a no-op.
    side = min(w, h)
    img = img.crop((0, 0, side, side))
    w, h = img.size

    # Dark scrim across the top band so cream title text has real
    # contrast against busy photo texture (foliage, brick, sky).
    scrim_height = int(h * 0.217)  # matches the 260/1200 ratio tuned by eye
    scrim = Image.new("L", (w, scrim_height), 0)
    scrim_draw = ImageDraw.Draw(scrim)
    for i in range(scrim_height):
        alpha = int(205 * (1 - i / scrim_height) ** 1.15)
        scrim_draw.line([(0, i), (w, i)], fill=alpha)
    dark_layer = Image.new("RGB", (w, scrim_height), (6, 8, 5))
    img.paste(dark_layer, (0, 0), scrim)

    draw = ImageDraw.Draw(img)

    size1 = int(w * 0.07)   # 84/1200
    size2 = int(w * 0.038)  # 46/1200
    font1 = ImageFont.truetype(font_path, size1)
    font2 = ImageFont.truetype(font_path, size2)

    cx = w / 2
    y1 = int(h * title_y)  # default 26/1200 — keep tight to the top so it clears a head lower in frame
    draw_text_with_shadow(draw, (cx, y1), title, font1, CREAM, INK_SHADOW, align="center", anchor="ma", shadow_offset=3)

    y2 = y1 + size1 + int(h * 0.0167)
    if subtitle:
      draw_text_with_shadow(draw, (cx, y2), subtitle, font2, CREAM, INK_SHADOW, align="center", anchor="ma", shadow_offset=2)

    # Bottom-right line (production credit or a date); --credit "" skips it.
    # Production credit, bottom right, same serif as the title (not a
    # sans font) with a solid dark backing plate — a text shadow alone
    # doesn't stand out reliably over patio/plant/brick textures.
    if not credit:
        img.save(out_path, quality=95)
        return out_path
    credit_font = ImageFont.truetype(font_path, int(w * 0.025))
    margin = int(w * 0.0217)
    bbox = draw.textbbox((0, 0), credit, font=credit_font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    pad_x, pad_y = int(w * 0.015), int(w * 0.0083)
    box_right = w - margin
    box_bottom = h - margin
    box_left = box_right - text_w - pad_x * 2
    box_top = box_bottom - text_h - pad_y * 2

    backing = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    backing_draw = ImageDraw.Draw(backing)
    backing_draw.rounded_rectangle(
        [box_left, box_top, box_right, box_bottom],
        radius=max(4, int(w * 0.0067)),
        fill=(*INK_BG, 165),
    )
    img = Image.alpha_composite(img.convert("RGBA"), backing).convert("RGB")
    draw = ImageDraw.Draw(img)

    draw.text(
        (box_right - pad_x, box_bottom - pad_y),
        credit,
        font=credit_font,
        fill=CREAM,
        anchor="rb",
    )

    img.save(out_path, quality=95)
    return out_path


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--image", required=True, help="Chosen chapter photo to use as the cover base")
    parser.add_argument("--title", required=True, help="Client name / main title line")
    parser.add_argument("--subtitle", default="", help="Album subtitle line (omit for none)")
    parser.add_argument("--title-y", type=float, default=0.0217, help="Title top as a fraction of height (default 0.0217; raise to move down)")
    parser.add_argument("--out", required=True, help="Output JPEG path")
    parser.add_argument("--credit", default=DEFAULT_CREDIT, help=f"Bottom-right credit line (default: \"{DEFAULT_CREDIT}\")")
    parser.add_argument(
        "--font",
        default=str(Path.home() / "Library/Fonts/Marcellus-Regular.ttf"),
        help="Path to Marcellus-Regular.ttf (default: ~/Library/Fonts/Marcellus-Regular.ttf)",
    )
    args = parser.parse_args()

    if not Path(args.font).exists():
        raise SystemExit(
            f"Font not found at {args.font}. Download it once:\n"
            f'  curl -sL "https://github.com/google/fonts/raw/main/ofl/marcellus/Marcellus-Regular.ttf" '
            f'-o "{args.font}"'
        )

    out = build_cover(args.image, args.title, args.subtitle, args.out, args.font, args.credit, args.title_y)
    print(f"saved {out}")


if __name__ == "__main__":
    main()
