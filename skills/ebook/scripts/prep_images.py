#!/usr/bin/env python3
"""Copy chapter photos into a build folder, upright and web-sized.

Usage: prep_images.py "<family>/03 Photos/Photos selected" <build_dir>/img
Writes ch1.jpg, ch2.jpg ... keyed on the "ChN." prefix of each filename.
If the photos have no ChN prefix (legacy families, e.g. Normans), they are
written as p01.jpg, p02.jpg ... in filename order and the mapping is printed.
Phone photos often carry an EXIF rotation that Chrome and PIL treat
differently, so every image is physically rotated here before use.
"""
import pathlib, re, sys
from PIL import Image, ImageOps

src, out = map(pathlib.Path, sys.argv[1:3])
out.mkdir(parents=True, exist_ok=True)
files = [f for f in sorted(src.iterdir()) if f.suffix.lower() in (".jpg", ".jpeg", ".png")]
n = 0
for f in files:
    m = re.match(r"Ch(\d+)\.", f.name)
    if m:
        name = f"ch{m.group(1)}.jpg"
    else:
        n += 1
        name = f"p{n:02d}.jpg"
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    im.thumbnail((1800, 1800))
    im.save(out / name, quality=86)
    print(f"{name}  {im.size}  <- {f.name}")
