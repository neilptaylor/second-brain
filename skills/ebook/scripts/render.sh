#!/bin/bash
# Render the wrap e-book HTML to a landscape PDF with live links and embedded fonts.
# Usage: render.sh <book.html> <out.pdf>
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --no-pdf-header-footer --virtual-time-budget=8000 \
  --print-to-pdf="$2" "file://$(cd "$(dirname "$1")" && pwd)/$(basename "$1")" 2>/dev/null
echo "-> $2"
