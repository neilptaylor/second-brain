#!/bin/bash
# Extract a title-card screengrab from each memento video for a hyperlinked gallery slide.
# Usage: mementos_titlecards.sh "<Mementos folder>" <out_dir>
set -e
SRC="$1"; OUT="$2"
mkdir -p "$OUT"
for f in "$SRC"/*.mp4; do
  base=$(basename "$f" .mp4)
  slug=$(echo "$base" | tr -cd '[:alnum:]' | cut -c1-24)
  ffmpeg -y -ss 1 -i "$f" -frames:v 1 -q:v 3 "$OUT/$slug.jpg" 2>/dev/null
  python3 -c "
from PIL import Image, ImageOps
im = ImageOps.exif_transpose(Image.open('$OUT/$slug.jpg')).convert('RGB')
im.thumbnail((900,900))
im.save('$OUT/$slug.jpg', quality=85)
"
  echo "$base -> $slug.jpg"
done
