# MMOM brand tokens for Paper

Shared reference for the `mmom-carousel` and `mmom-visual` skills. Pulled directly from `~/.claude/proposal-system/proposal-light.css` — the same light/cream system used in proposals — so carousels, visuals, and proposals all look like one brand.

Always read [Neil's voice profile](/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My%20Drive/Mega%20Claude%20Cowork/About%20Me/VOICE_PROFILE_Neil_Taylor.md) before writing any copy that goes on a slide — banned words, tone, "we" not "you", etc. all apply here exactly as they do in proposals and posts.

## Colors

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#f9f6f1` | Base background (cream, not white) |
| `--bg-2` | `#f0ebe3` | Secondary panel background |
| `--bg-3` | `#e8e1d8` | Tertiary / card background |
| `--cream` | `#1c1814` | Primary text (near-black, warm) |
| `--cream-2` | `#3a3228` | Body text |
| `--muted` | `#7a6e62` | Secondary text, captions |
| `--muted-soft` | `#9e9185` | Tertiary text, timestamps |
| `--peach` | `#b8674e` | Accent — headings, dividers, CTA |
| `--peach-light` | `#c9856a` | Accent hover / lighter variant |
| `--peach-deep` | `#a05540` | Accent pressed / darker variant |
| `--peach-tint` | `#f5e8e3` | Accent background tint |
| `--hair` | `rgba(28,24,20,0.10)` | Hairline dividers |
| `--hair-peach` | `rgba(184,103,78,0.45)` | Peach-tinted hairline |
| `--ink` | `#1e2a4a` | Handwriting ink color (biro navy) — use ONLY for hand-lettered notes, never for print type |
| `--ink-soft` | `#2f3c60` | Handwriting ink, lighter — attribution lines under a hand-lettered note |

## Fonts

| Token | Stack | Use |
|---|---|---|
| `--serif` | `"Marcellus", "Cormorant Garamond", serif` | Headlines |
| `--italic` | `"Cormorant Garamond", "Marcellus", serif` | Lead lines, pull quotes |
| `--sans` | `"Inter", "Helvetica Neue", Arial, sans-serif` | Body, labels, captions |
| `--hand` | `"Biro Script reduced", "Caveat", cursive` | Hand-written annotations (visuals skill) — Paper's MCP tools are HTML/CSS, not freehand ink, so "hand-drawn" is achieved through handwriting webfonts, slight rotation, ink-bleed shadow, and a vignette background, not literal pen strokes |

## Setting these up in a Paper file (once per file)

Call `create_tokens` early in both skills so `write_html` colors can reference `var(--color-peach)` etc. **Token names need the leading `--`, and font tokens use `type: "fontFamily"` (not `"font"`)** — confirmed against the real tool schema:

```json
[
  {"type": "color", "name": "--color-bg", "value": "#f9f6f1"},
  {"type": "color", "name": "--color-bg-2", "value": "#f0ebe3"},
  {"type": "color", "name": "--color-bg-3", "value": "#e8e1d8"},
  {"type": "color", "name": "--color-cream", "value": "#1c1814"},
  {"type": "color", "name": "--color-cream-2", "value": "#3a3228"},
  {"type": "color", "name": "--color-muted", "value": "#7a6e62"},
  {"type": "color", "name": "--color-muted-soft", "value": "#9e9185"},
  {"type": "color", "name": "--color-hair", "value": "rgba(28,24,20,0.10)"},
  {"type": "color", "name": "--color-peach", "value": "#b8674e"},
  {"type": "color", "name": "--color-peach-light", "value": "#c9856a"},
  {"type": "color", "name": "--color-peach-deep", "value": "#a05540"},
  {"type": "color", "name": "--color-peach-tint", "value": "#f5e8e3"},
  {"type": "color", "name": "--color-hair-peach", "value": "rgba(184,103,78,0.45)"},
  {"type": "color", "name": "--color-ink", "value": "#1e2a4a"},
  {"type": "color", "name": "--color-ink-soft", "value": "#2f3c60"},
  {"type": "fontFamily", "name": "--font-serif", "value": "\"Marcellus\", \"Cormorant Garamond\", serif"},
  {"type": "fontFamily", "name": "--font-italic", "value": "\"Cormorant Garamond\", \"Marcellus\", serif"},
  {"type": "fontFamily", "name": "--font-sans", "value": "\"Inter\", \"Helvetica Neue\", Arial, sans-serif"},
  {"type": "fontFamily", "name": "--font-hand", "value": "\"Caveat\", \"Kalam\", cursive"}
]
```

Check with `get_tokens` first — if a file already has these (e.g. reused from a previous carousel), skip re-creating them.

**Critical: `var(--font-*)` does NOT resolve in `write_html`/`update_styles` `font-family` — write the literal stack instead.** Confirmed by live test on 2026-08-11: `font-family: var(--color-peach)`-style references work fine for colors (render correctly), but `font-family: var(--font-hand)` silently falls back to a default sans instead of Caveat, even though the token is defined correctly and `get_computed_styles` shows the literal unresolved `"var(--font-serif)"` string sitting in the `fontFamily` property. Fix: always write the actual font stack in the HTML/style, e.g. `font-family: "Marcellus", "Cormorant Garamond", serif;` — never `font-family: var(--font-serif);`. Keep the `--font-*` tokens in the file anyway (useful as a documented reference visible via `get_tokens`, and other tools may read them), just don't rely on them for rendering.

**Export lands in `~/Downloads`, not a Drive folder — you must move it.** `export` has no destination-path parameter; it always writes to `~/Downloads/[artboard name]@[scale].png` on Neil's Mac. Since Google Drive is mounted locally at `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/`, the skill's export step must `mv` the file from Downloads into the target Drive folder as a separate step after calling `export` — Paper itself can't save there directly.

## Confirmed on first live run (2026-08-11)

- `create_tokens` payload shape — see corrected JSON above (was wrong in the original draft: missing `--` prefix, `"font"` instead of `"fontFamily"`)
- Google Fonts "Caveat"/"Kalam" (and Marcellus/Cormorant Garamond/Inter) all resolve automatically via `get_font_family_info` — no manual embedding needed
- **Output save location — confirmed, was wrong in the original draft.** Neil's actual convention (seen in `Claude Outputs/Content/` — real files there, not a guess) is flat files directly in `[Drive]/Mega Claude Cowork/Claude Outputs/Content/`, named `MAMO_<Type>_<Topic>_v<N>.<ext>` (e.g. `MAMO_LinkedIn-Post_ChildQuestions_v2.md`, `MAMO_7-Questions-Carousel_v1.md`). Both skills now save exports there as `MAMO_Visual_<Topic>_v<N>.png` / `MAMO_Carousel_<Topic>_v<N>.pdf` — NOT the nested dated subfolders (`Content/Visuals/[date] [topic]/`) originally proposed, which don't exist in Neil's real Drive.

## Genuinely-handwritten technique (confirmed on live run 2026-08-11, spec'd from Steve's reference image)

The brief was explicit: text needs to read as if Neil actually wrote it on paper — not "a cursive webfont on a flat background." Tested 9 Google Fonts side by side (Caveat, Kalam, Shadows Into Light, Homemade Apple, Reenie Beanie, Nanum Pen Script, Just Another Hand, Annie Use Your Telescope, La Belle Aurore) against Steve's reference photo. Caveat at `font-weight: 500` was the closest Google Font match.

**Then Neil installed a real biro font and it's now the primary choice.** Steve's tip ("download a free biro font online and get Paper to leverage it") led to "Biro Script reduced" (ingoFonts, `~/Library/Fonts/Biro_Script_reduced.otf`) — licensed for use on up to 5 of Neil's own computers, output (finished designs/images) is unrestricted, only the font file itself can't be redistributed. Side-by-side test on 2026-08-11 confirmed it beats Caveat decisively: it has genuine pen-pressure variation and irregular stroke width baked into the letterforms themselves, not simulated via CSS. **Use `"Biro Script reduced"` as the primary hand font; fall back to `"Caveat"` at weight 500 only if Paper can't find it** (e.g. a different machine where the font isn't installed — check with `get_font_family_info` first and fall back silently, don't error out).

Full recipe — all elements matter together, not just the font:
1. **Font**: `font-family: "Biro Script reduced", "Caveat", cursive;` — literal stack, never `var(--font-hand)` (see the resolution bug above). No need to set `font-weight` on Biro Script reduced (it only has one weight); use `font-weight: 500` when falling back to Caveat. Size 56–64px for a primary note on a 1080-wide artboard.
2. **Ink color**: `var(--color-ink)` (`#1e2a4a`, a navy biro, not black and not the brand peach) for the main lines; `var(--color-ink-soft)` at reduced size for an attribution line.
3. **Background**: a warm vignette, not a flat fill — `background-image: radial-gradient(ellipse at 50% 40%, #f3ecdd 0%, #e6dcc4 100%)`. Flat cream reads as a slide; the vignette reads as a photographed page.
4. **Per-line imperfection**: rotate each line independently by a small, different amount (e.g. `rotate: -1.2deg`, `0.6deg`, `-0.4deg` — set via the `rotate` style property, not folded into a `transform` string, since `update_styles` additively merges `transform`-authored rotate onto the existing one rather than replacing it — confirmed by a doubled-rotation bug on live test). A uniform rotation on the whole block reads as a design choice; independent per-line rotation reads as a hand actually moving across the page.
5. **Optional grain**: a low-opacity (~0.05) SVG `feTurbulence` noise overlay, `mix-blend-mode: multiply`, absolutely positioned full-bleed, adds paper texture. Subtle — don't push past ~0.06 opacity or it reads as a filter, not paper.
6. **Wet-ink bleed — the detail that actually sells it.** A crisp vector stroke reads as a font no matter how good the letterforms are. Add `text-shadow` layers in the ink color to simulate ink feathering into paper fiber before it's dry: `text-shadow: 0 0 0.6px rgba(30,42,74,0.6), 0 0 2.5px rgba(30,42,74,0.22), 0 0 5px rgba(30,42,74,0.08);` (three stacked shadows — tight/dense, mid soft glow, wide faint halo — using the ink color at decreasing opacity as radius increases). Scale opacity down proportionally for the lighter `--color-ink-soft` attribution line. Confirmed on live test 2026-08-11, directly requested by Neil after seeing the first pass ("I want... you can see the ink hasn't quite set on the page, like Steve's") — do this by default on every hand-lettered piece, don't treat it as optional polish.

**Style-authoring pitfall**: `write_html`/`update_styles` do NOT ban `margin`, but Paper's own guide discourages it in favor of `gap`/`padding` for layout. For a one-off organic offset on a single hand-lettered line (not a repeated layout), a small `margin-left` is fine and renders correctly — reserve `gap`/`padding` for actual multi-child layout structure.
