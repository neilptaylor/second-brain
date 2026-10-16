---
name: mmom-visual
description: Builds a single branded visual (quote card, stat/myth callout, testimonial highlight, hand-lettered annotation graphic) for a standalone LinkedIn or Instagram post, directly inside Paper via the paper.design MCP. Use when Neil says "/visual [topic]", "make a quote card for X", "turn this into a graphic", or wants one image rather than a carousel.
---

# MMOM — Single Visual Builder (Paper MCP)

<!-- v1.2: 2026-10-15. Neil said the hand-lettered card (MMOM_LI_how-big-a-shag-is-it_v1.png) did not look like real handwriting. Cause: it was Caveat (Biro Script was not loaded in the HTML route), set in clean uniform CSS on a flat vignette, so it read as a font. Fix: hand-lettered notes now render through scripts/handwritten.py (Biro Script reduced, per-letter jitter, stroke wobble, ink bleed, paper grain). Paper is not used for these. -->
<!-- v1.1: a name at the end of Neil's brief on a hand-lettered note is the signature, render it as the attribution line -->

You build one branded image — not a multi-slide carousel — using the `paper` MCP tools, and export it ready to post.

**Companion skill:** `mmom-carousel` is for multi-slide LinkedIn document posts. Use this skill only for a single standalone image.

**Honest constraint:** Paper's MCP tools build with HTML/CSS on a canvas (`write_html`, artboards, design tokens) — there's no literal freehand pen/ink tool exposed. "Hand-drawn" here means handwriting webfonts (Caveat/Kalam), slight rotation, sketchy underline/circle SVG accents, and torn-paper/sticky-note styling — not actual freehand line art. If Neil wants literal sketch-style illustration, flag that this skill can't do that and KoralPaper (a separate, sketch-specific MCP tool) was the alternative considered for that.

---

## Step 0 — Confirm Paper is reachable

Call `get_guide` with topic `"paper-mcp-instructions"` first.

If any `paper` MCP tool call fails outright, STOP and tell Neil Paper Desktop needs to be open on his Mac — local-only connection (127.0.0.1).

---

## Step 1 — Get the brief

Read `~/.claude/paper-skills/brand-tokens.md` for colors/fonts, and Neil's [voice profile](/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My%20Drive/Mega%20Claude%20Cowork/About%20Me/VOICE_PROFILE_Neil_Taylor.md) — non-negotiable for any words on the graphic.

Work out which shape this is — ask Neil if it's not obvious from his prompt:

| Type | What it is | Typical source |
|---|---|---|
| Quote card | One verbatim line, large, attributed | A testimonial, a call transcript, his own line from a post |
| Stat / myth-buster | One number or misconception, corrected | Research, a claim he wants to counter |
| Hand-lettered annotation | A short phrase treated like a sticky note / margin note over a simple layout | A feeling, a one-liner, a callout |

Also confirm the **format**: LinkedIn single image is best at 1080×1350 (4:5) or 1080×1080 (square); Instagram feed post is 1080×1350 or 1080×1080. Default to 1080×1350 unless Neil says square.

---

**Signature rule:** if the brief ends with a name (e.g. "Neil"), that is the signature. On a hand-lettered note, render it as a "— Neil" attribution line in `var(--color-ink-soft)`. Never leave it off and never ask whether to add it.

---

## Step 2 — Set up the file

1. `get_basic_info` on the open file — reuse it if blank, otherwise `create_file` named `"[YYYY-MM-DD] Visual — [topic]"` and `open_file`.
2. `get_tokens` — `create_tokens` from `brand-tokens.md` if not already present.

---

## Step 3 — Build it

**Hand-lettered note: do not use Paper. Run the script.** It is the only route that reads as real handwriting rather than a font (a plain webfont in CSS always looks typed, and Paper is unreachable from Claude Code anyway).

```bash
python3 skills/mmom-visual/scripts/handwritten.py "<out dir>/MMOM_LI_<post-slug>_v1.png" "Line one." "Line two." "Line three." --sign Neil
```

One quoted argument per line of handwriting, `--sign Neil` for the signature (always, per the signature rule). Change `--seed` for a different hand. Open the PNG and look at it before handing back: the ink should vary in weight, letters should sit at slightly different angles and heights, lines should drift, and the paper should have grain and a lit falloff, not a flat fill. If it looks typed, something broke (check Biro Script reduced is in ~/Library/Fonts). Then skip to Step 4's save location. The Paper steps below are for quote cards and stat cards only.


1. `create_artboard` at the confirmed size, named `"Visual — [topic]"`.
2. `write_html` incrementally (`mode: "insert-children"`) — background treatment first, then the main text/quote, then any hand-lettered annotation layer, then a small MMOM mark. Build in pieces so progress is visible.
3. Typography: main statement in `"Marcellus", "Cormorant Garamond", serif` or `"Cormorant Garamond", "Marcellus", serif` (italic) for a quote; any hand-annotation or full hand-lettered note in `"Biro Script reduced", "Caveat", cursive` (Biro Script reduced is the primary hand font — check it resolves with `get_font_family_info` first and fall back to Caveat at `font-weight: 500` if not) with a small independent rotation per line (via the `rotate` style property, e.g. `-1.2deg`, `0.6deg`, `-0.4deg` — don't fold it into `transform`, see `brand-tokens.md`) so it reads as a hand actually moving across the page. **Write the literal font stack, not `var(--font-*)`** — the token reference silently fails to resolve in `font-family` and falls back to default sans (confirmed on live test 2026-08-11, see `brand-tokens.md`). Colors are fine via `var(--color-*)`. For a hand-lettered note specifically: use `var(--color-ink)` navy (not the brand peach), a warm vignette background instead of flat cream (`radial-gradient(ellipse at 50% 40%, #f3ecdd 0%, #e6dcc4 100%)`), and the wet-ink `text-shadow` bleed recipe in `brand-tokens.md` — this combination is what makes it read as genuinely handwritten rather than "a cursive font on a slide."
4. `get_screenshot` to check: no widows, legible contrast, nothing clipped at the artboard edge.
5. `finish_working_on_nodes` when done.

---

## Step 4 — Export

`export` the artboard as PNG, 2x scale for crispness on high-DPI phone screens. **This always writes to `~/Downloads` — confirmed on live test, there's no destination-path option** — then move the file into the Drive folder below as a separate filesystem step (Google Drive is mounted locally at `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/`).

**Save location — confirm with Neil, this is a proposed default:**
```
[Google Drive]/Content/Visuals/[YYYY-MM-DD] [Topic]/
```
Ask if this doesn't match how he organises content — don't invent a folder tree silently.

---

## Step 5 — Hand back

Tell Neil:
1. Paper file name/link
2. Where the PNG was saved
3. Which post it's meant to accompany, if that context exists (e.g. paired with a `linkedin-post` draft)
