#!/usr/bin/env python3
"""Render a hand-lettered note (1080x1350 PNG) that reads as pen on real paper.

Why this exists: a handwriting webfont set in clean CSS reads as a font. This
script adds what a real hand does: per-letter jitter in angle, baseline and size,
uneven word gaps, a slight drift in line angle, stroke wobble (SVG displacement),
ink bleed, and paper with grain, fibres and a lit-from-above falloff.

Usage: handwritten.py OUT.png "Line one." "Line two." [--sign "Neil"] [--seed 7]
Font: Biro Script reduced (~/Library/Fonts). Falls back to Caveat via Google Fonts.
"""
import argparse, html, pathlib, random, subprocess, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FONT = pathlib.Path.home() / "Library/Fonts/Biro_Script_reduced.otf"


def letters(text, rnd, size):
    out = []
    for word in text.split(" "):
        spans = []
        for ch in word:
            rot = rnd.uniform(-2.6, 2.6)
            dy = rnd.uniform(-4, 4)
            sc = rnd.uniform(0.94, 1.06)
            sp = rnd.uniform(-1.5, 2.5)
            spans.append(
                f'<i style="transform:translateY({dy:.1f}px) rotate({rot:.1f}deg) scale({sc:.3f});'
                f'margin-right:{sp:.1f}px">{html.escape(ch)}</i>')
        out.append(f'<b class="w" style="margin-right:{rnd.uniform(0.18, 0.42):.2f}em">{"".join(spans)}</b>')
    return "".join(out)


def build(lines, sign, seed):
    rnd = random.Random(seed)
    body = ""
    drift = rnd.uniform(-0.6, 0.6)
    for n, line in enumerate(lines):
        ang = drift + rnd.uniform(-0.9, 0.9)
        indent = rnd.uniform(-8, 22)
        body += (f'<div class="ln" style="rotate:{ang:.2f}deg;margin-left:{indent:.0f}px">'
                 f'{letters(line, rnd, 92)}</div>')
    if sign:
        body += (f'<div class="ln sig" style="rotate:{rnd.uniform(-2.5, -0.5):.2f}deg;margin-left:{rnd.uniform(10, 40):.0f}px">'
                 f'{letters("— " + sign, rnd, 64)}</div>')
    fontface = (f'@font-face{{font-family:"BiroHand";src:url("{FONT.as_uri()}")}}'
                if FONT.exists() else '@import url("https://fonts.googleapis.com/css2?family=Caveat:wght@500&display=block");')
    family = '"BiroHand","Caveat",cursive'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{fontface}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;background:#d9cfb8}}
.paper{{position:absolute;inset:0;
  background:
   radial-gradient(ellipse 120% 90% at 46% 38%, #f6f0e2 0%, #eee4cf 55%, #dccfb0 100%);}}
.grain{{position:absolute;inset:0;mix-blend-mode:multiply;opacity:.55}}
.fibre{{position:absolute;inset:0;mix-blend-mode:multiply;opacity:.12}}
.fold{{position:absolute;inset:0;background:linear-gradient(180deg,transparent 48%,rgba(120,95,55,.10) 49.6%,rgba(255,250,235,.25) 50.4%,transparent 52%)}}
.edge{{position:absolute;inset:0;box-shadow:inset 0 0 160px rgba(110,85,45,.28)}}
.text{{position:absolute;left:112px;top:400px;width:860px;color:#16214a;font-family:{family};
  font-size:108px;line-height:1.25;filter:url(#wobble)}}
.ln{{white-space:nowrap;transform-origin:left center;margin-bottom:6px}}
.sig{{font-size:64px;color:#2a3868;margin-top:26px}}
.w{{display:inline-block;font-weight:400}}
i{{display:inline-block;font-style:normal;
  text-shadow:0 0 .7px rgba(27,39,80,.75),0 0 2.4px rgba(27,39,80,.28),0 0 5px rgba(27,39,80,.10)}}
</style></head><body>
<svg width="0" height="0" style="position:absolute"><defs>
 <filter id="wobble" x="-5%" y="-5%" width="110%" height="110%">
  <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="{seed}" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3.2" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="{seed+3}" result="t"/>
  <feColorMatrix in="t" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -0.9 1.3" result="ta"/>
  <feComposite in="d" in2="ta" operator="in"/>
 </filter>
 <filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="3" seed="{seed}"/>
  <feColorMatrix type="matrix" values="0 0 0 0 .45  0 0 0 0 .38  0 0 0 0 .27  0 0 0 .5 0"/></filter>
 <filter id="f"><feTurbulence type="fractalNoise" baseFrequency=".012 .22" numOctaves="2" seed="{seed+9}"/>
  <feColorMatrix type="matrix" values="0 0 0 0 .5  0 0 0 0 .42  0 0 0 0 .3  0 0 0 .35 -.05"/></filter>
</defs></svg>
<div class="paper"></div>
<svg class="grain" width="1080" height="1350"><rect width="100%" height="100%" filter="url(#g)"/></svg>
<svg class="fibre" width="1080" height="1350"><rect width="100%" height="100%" filter="url(#f)"/></svg>
<div class="edge"></div>
<div class="text">{body}</div>
</body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("lines", nargs="+")
    ap.add_argument("--sign", default=""); ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as t:
        f = pathlib.Path(t) / "n.html"; f.write_text(build(a.lines, a.sign, a.seed))
        subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--force-device-scale-factor=2",
                        "--window-size=1080,1350", "--virtual-time-budget=6000",
                        f"--screenshot={t}/s.png", f.as_uri()], check=True, capture_output=True)
        from PIL import Image
        Image.open(f"{t}/s.png").convert("RGB").crop((0, 0, 2160, 2700)).resize((1080, 1350), Image.LANCZOS).save(a.out)
    print(a.out)


if __name__ == "__main__":
    main()
