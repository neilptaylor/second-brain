---
name: mmom-carousel
description: Builds a branded LinkedIn carousel (multi-slide 1080x1350 artboards) for Me & My Old Man directly inside Paper via the paper.design MCP. Use when Neil says "/carousel [topic]", "make a LinkedIn carousel about X", "build a carousel for X", or asks to turn a post/idea/story into carousel slides. Produces an editable Paper file plus exported PDF/PNGs ready to upload as a LinkedIn document post.
---

# MMOM — LinkedIn Carousel Builder (Paper MCP)

You build a multi-slide LinkedIn carousel as a real, editable design in Paper — not a mockup — using the `paper` MCP tools, and export it ready to post.

**Companion skill:** `mmom-visual` is for single-image posts. Use this skill only when the ask is a multi-slide carousel.

---

## Step 0 — Confirm Paper is reachable

Call `get_guide` with topic `"paper-mcp-instructions"` first — Paper's own tools recommend this for best results and it may cover conventions not documented here.

If any `paper` MCP tool call fails outright (not just an empty result), STOP and tell Neil: Paper Desktop needs to be open with a file loaded on his Mac for this to work — it's a local-only connection (127.0.0.1), it won't work if the app isn't running.

---

## Step 1 — Get the brief

Read `~/.claude/paper-skills/brand-tokens.md` for colors/fonts, and Neil's [voice profile](/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My%20Drive/Mega%20Claude%20Cowork/About%20Me/VOICE_PROFILE_Neil_Taylor.md) for tone and banned words — non-negotiable per his CLAUDE.md, applies to every word on every slide.

From Neil's prompt, work out:
- **Topic** — what the carousel is about
- **Source material** — did he paste a post draft, a transcript, a story, or just a topic to develop from scratch? Use whatever he gave you; don't invent client stories.
- **Slide count** — default 6–8 unless he specifies. Carousels that run long lose completion rate; don't pad.

If the topic alone was given with no angle, draft the story arc yourself using his voice profile and the `mmom-sales-strategist`/`linkedin-post` skills' framing logic (hook → tension → insight → proof → CTA), then state it back to him before building (see Step 2).

---

## Step 2 — Plan the arc, then confirm before building

Output a short plan, don't skip this:

```
CAROUSEL PLAN — [topic]
Slide 1 (hook):     [headline]
Slide 2–N (body):   [one line per slide — the idea/story beat it carries]
Slide N (CTA):      [what you want the reader to do]
```

Proceed straight to building — no need to wait for approval unless the topic itself was ambiguous.

---

## Step 3 — Set up the file

1. `get_basic_info` on the currently open file. If it's a blank/scratch file, use it. If Neil has something else open, call `create_file` with name `"[YYYY-MM-DD] Carousel — [topic]"` and `open_file` it.
2. `get_tokens` — if MMOM tokens aren't already defined, `create_tokens` using the payload in `brand-tokens.md`.

---

## Step 4 — Build each slide

For each slide, in order:

1. `create_artboard` — 1080×1350 (LinkedIn carousel native size, 4:5). Name it `"Slide N — [short label]"`.
2. `write_html` incrementally into that artboard (`mode: "insert-children"`) — build it in pieces (header/eyebrow, then headline, then body, then footer/page-number) so progress is visible, per Paper's own guidance. **Colors**: use the brand tokens via `var(--color-peach)` etc. (confirmed working), not hardcoded hex. **Fonts**: write the literal stack (e.g. `font-family: "Marcellus", "Cormorant Garamond", serif;`) — `var(--font-*)` silently fails to resolve in `font-family` and falls back to default sans, confirmed on live test 2026-08-11. See `brand-tokens.md` for the exact stacks. If a slide uses a hand-lettered annotation, the primary hand font is now `"Biro Script reduced"` (fall back to `"Caveat"` at weight 500 if it doesn't resolve) — see `brand-tokens.md`'s full genuinely-handwritten recipe (ink color, vignette background, per-line rotation, wet-ink bleed shadow).
3. Slide 1 gets the strongest visual weight — big serif headline (`"Marcellus", "Cormorant Garamond", serif`), short. Middle slides carry one idea each — don't cram. Last slide is the CTA slide: clear next step, and if it's a call-to-action to book, use the [Calendly link](use reference_calendly memory) — check that memory for the current URL rather than hardcoding it here since it can change.
4. Keep a consistent footer treatment across slides (page number, small MMOM wordmark/name) — build it once on slide 1, then `duplicate_nodes` the footer group onto each subsequent artboard rather than rewriting it each time.
5. After each slide, `get_screenshot` it and sanity-check: no widows (single word alone on a line — same rule as proposals), text not clipped, contrast readable.
6. `finish_working_on_nodes` when the whole carousel is done.

---

## Step 5 — Export

1. `export_combined_pdf` across all slide artboards, in order — this is the file to upload as a LinkedIn "document" post (LinkedIn carousels are PDF uploads, not separate images).
2. Also `export` each artboard individually as PNG, in case Neil wants to repost as an Instagram carousel instead.
3. **`export` always writes to `~/Downloads` on Neil's Mac — confirmed on live test, there's no destination-path option.** Move the exported file(s) from Downloads into the target Drive folder as a separate filesystem step (Google Drive is mounted locally at `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/`).

**Save location — confirm with Neil, this is a proposed default, not a known-correct path:**
```
[Google Drive]/Content/LinkedIn Carousels/[YYYY-MM-DD] [Topic]/
```
If that folder structure doesn't already exist or doesn't match how Neil organises content, ask him where these should live before finalizing — don't silently invent a new folder tree.

---

## Step 6 — Hand back

Tell Neil:
1. Paper file name/link (so he can open and tweak it directly in Paper — that's the point of this over a flat export)
2. Where the PDF + PNGs were saved
3. One line on the arc you used and why
4. Flag anything you weren't sure about (a claim you couldn't verify, a beat you invented because the brief didn't specify it)
