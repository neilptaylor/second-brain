#!/usr/bin/env python3
"""Render an MMOM carousel HTML file to a LinkedIn-ready PDF plus per-slide PNGs.

Same method as the reference MMOM_LI_Carousel_v1.pdf: each 1080x1350 slide is
screenshotted in headless Chrome (at 2x, then downsampled), and the images are
stitched into a PDF. Fonts are baked into pixels, so nothing can fall back.

Usage: render.py carousel.html OUT_DIR NAME
  -> OUT_DIR/NAME.pdf and OUT_DIR/NAME_png/NAME_01.png ...
"""
import pathlib, re, subprocess, sys, tempfile
from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1080, 1350


def main(html, out_dir, name):
    html = pathlib.Path(html).resolve()
    out = pathlib.Path(out_dir); png_dir = out / f"{name}_png"
    png_dir.mkdir(parents=True, exist_ok=True)
    n = len(re.findall(r'<section class="slide', html.read_text()))
    if not n:
        sys.exit("No <section class=\"slide\"> found.")
    pages = []
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(1, n + 1):
            shot = pathlib.Path(tmp) / f"{i}.png"
            subprocess.run([CHROME, "--headless=new", "--hide-scrollbars",
                            "--force-device-scale-factor=2", f"--window-size={W},{H}",
                            "--virtual-time-budget=6000",  # lets web fonts load
                            f"--screenshot={shot}", f"{html.as_uri()}?s={i}"],
                           check=True, capture_output=True)
            img = Image.open(shot).convert("RGB").crop((0, 0, W * 2, H * 2)).resize((W, H), Image.LANCZOS)
            img.save(png_dir / f"{name}_{i:02d}.png")
            pages.append(img)
    pdf = out / f"{name}.pdf"
    pages[0].save(pdf, save_all=True, append_images=pages[1:], resolution=72, quality=92)
    print(f"{n} slides -> {pdf}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
