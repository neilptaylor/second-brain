---
name: mmom-carousel
description: Builds a branded LinkedIn carousel (1080x1350 slides, uploaded as a PDF document post) for Me & My Old Man by writing HTML from a fixed template and rendering it to PDF with headless Chrome. Use when Neil says "/carousel [topic]", "make a LinkedIn carousel about X", "build a carousel for X", or asks to turn a post, idea or story into carousel slides. Never uses Paper.
---
<!-- v2.0 — 2026-09-24. Rebuilt around MMOM_LI_Carousel_v1.pdf (HTML to PDF). Paper route retired. -->

# MMOM LinkedIn Carousel Builder (HTML to PDF)

## The reference wins

`references/MMOM_LI_Carousel_v1.pdf` is the house carousel. Contact sheet: `references/MMOM_LI_Carousel_v1_contact-sheet.png`. Look at it before every build.

It was built as HTML, each slide screenshotted, then stitched into a PDF. The PDF holds images, not live text, which is why the fonts never break. This skill does the same.

For carousels, the reference overrides everything else, including:
- `~/.claude/paper-skills/brand-tokens.md` (Marcellus/Inter, Paper token setup)
- `MMOM_Carousel-Design-Brief_v1.md` sections 1 to 4 (Marcellus, 120px margins, wordmark on first and last slide only)
- the Drive brand guidelines typography and colour pages (Marcellus/Inter, blush/slate palette)

The brief's section 5 slide ideas are still useful as copy starting points. Everything visual comes from the reference and `assets/template.html`.

Never build a carousel in Paper. See `knowledge/lessons.md`, 2026-09-24.

## The spec (lifted from the reference)

| | |
|---|---|
| Canvas | 1080 x 1350, every slide. 7 to 8 slides. |
| Background | Cream `#f9f6f1` |
| Headlines | Lora 600, near-black `#1c1814`. Hook 76px, other slides 66px. |
| Supporting lines | DM Sans 400, 32px, `#7a6e62`. One or two short lines. |
| Accent | Terracotta `#b8644b`. Big Lora numerals (150px), page count, one italic word. |
| Wordmark | "• ME & MY OLD MAN", small spaced caps, top left, every slide. |
| Page count | "01 / 08", Lora, terracotta, bottom right, every slide. |
| Margins | 88px left and right. Text left-aligned, block sits mid-slide. |

Slide order, as in the reference:
1. **Hook.** Neil's real moment in one line, a supporting line, a tease bottom left ("Here's exactly what I told him →").
2. **Numbered points.** Big terracotta number, one-line point, one or two quiet supporting lines. One idea per slide.
3. **Peach break.** At most one full-terracotta slide, cream type. Use it for the turn.
4. **Land.** The reframe, with one terracotta italic word ("Starting.").
5. **CTA.** Dark `#1c1814` slide, cream serif line, terracotta second line, `meandmyoldman.co.uk` bottom left.

The fonts are matched by eye to the reference's pixels (its PDF has no embedded fonts to read). If Neil names the real ones, update the template's link and this table.

## Step 1: Brief

Read `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` in full. Every word on every slide is Neil's voice. Use only what Neil gave you: a post, a story, a transcript. Never invent a story, a name or a number. If he gave only a topic, ask for the real moment behind it.

## Step 2: Plan, then build

Write the slide-by-slide copy as a short plan (slide number, headline, supporting line). Build straight away unless the angle is unclear.

## Step 3: Write the HTML

Copy `assets/template.html` to a working file in `scratch/`. Duplicate or delete `<section class="slide">` blocks to fit the plan. Don't change the CSS. Only the words, slide order and page counts change. Fix every "NN / 08" to the real total.

Check each slide: no widows (a single word alone on the last line), nothing longer than three lines of headline, no em dashes, British spelling, double quotes.

## Step 4: Render

```bash
python3 skills/mmom-carousel/scripts/render.py scratch/<file>.html "<out dir>" MMOM_LI_<post-slug>_v1
```

Needs Google Chrome installed and an internet connection (the fonts load from Google Fonts). The output is a PDF plus one PNG per slide. Open the PNGs and look at every one before handing back.

## Step 5: Save and hand back

Save to `Shared drives/Systems/01 Awareness/Linkedin 2026/03 Linkedin Assets 2026/` as `MMOM_LI_<post-slug>_v1.pdf`, PNGs alongside, and put the filename on the Notion row's Visual: line. Keep the working HTML in `scratch/` so tweaks are one edit and one re-render.

Tell Neil where the PDF is and flag anything you weren't sure of. Nothing else.
