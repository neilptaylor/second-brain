---
name: wrap-up-memento
description: Builds a Me & My Old Man "wrap up behind the scenes" clip — an existing multi-person call recording (Riverside/Zoom grid) played untouched, with a centred title box overlay near the top and the brand end card appended after. Distinct from video-memento (title card + Ken Burns photo slideshow over one audio excerpt) and waveform-memento (audio-only story with waveform + captions). Use when Neil gives a wrap-up/behind-the-scenes call recording and asks for a title box added, referencing a prior clip's style, or says "wrap up clip" / "BTS clip".
---

<!-- v1.0 — 2026-09-25 -->

# Wrap-Up Memento

A **wrap up behind the scenes** clip is real call footage (usually a 2-3 way Riverside/Zoom
grid, portrait 1080x1920) that plays in full, unedited, with two brand overlays added:
a **title box** near the start naming the moment, and the standard **end card** after the
clip finishes. It is NOT a photo slideshow (`video-memento`) and NOT an audio-only piece
with a waveform (`waveform-memento`) — the source video itself is the content.

## Build steps

1. Re-encode the source with dense keyframes so HyperFrames can seek it cleanly:
   `ffmpeg -i "$SRC" -c:v libx264 -crf 18 -g <fps> -keyint_min <fps> -pix_fmt yuv420p -movflags +faststart -c:a aac assets/video/<name>.mp4`
2. Mount the video as an **untimed wrapper** with a `<video>` child that carries its own
   `data-start`/`data-duration` — never put `data-start` on both the wrapper and the video
   (HyperFrames lint: `video_nested_in_timed_element`, and it desyncs visibility from the
   frame extractor). Mirror the same source into a separate `<audio data-track-index="10">`
   so the muted visual track still has sound.
3. **Title box placement — find the face-free band before picking coordinates.** Multi-tile
   call grids (2-up, 3-up) stack faces through almost the whole frame. Don't guess a centred
   position — pull 2-3 frames from the actual clip with `ffmpeg -ss <t> -frames:v 1` at
   different timestamps, look at them, and find the one horizontal band that stays empty
   (wall/ceiling) across all sampled frames — typically the gap between two stacked tiles,
   above where heads start. Anchor the box there, not at literal vertical centre.
4. Use `npx hyperframes snapshot . --at <t>` to confirm the box clears every face before
   rendering the full clip.
5. Append the brand end card as its own scene starting exactly at the source clip's real
   duration (from `ffprobe`, not assumed).

## Brand execution (confirmed, don't reinvent)

**Title box** — Playfair Display italic, semi-opaque cream card floating over the live
video:
```css
.title-box { background: rgba(246, 239, 225, 0.94); border-radius: 6px; box-shadow: 0 18px 46px rgba(20,15,8,0.32); padding: 30px 46px; text-align: center; }
.title-box .title-text { font-family: "Playfair Display", serif; font-weight: 600; font-style: italic; font-size: 52px; line-height: 1.2; color: #2d2926; }
```
Fade/rise in (~0.5s), hold, fade/rise out (~0.4s) before any burned-in captions in the
source footage reach the same words the title box already named — check the source's own
captions timing so the two never compete on screen at once.

**End card** — same house card as `video-memento` (cream `#f6efe1` / charcoal `#2d2926` /
rust accent `#bf5700`, Playfair Display + Inter tracked-caps kicker):
```html
<div class="card">
  <div class="kicker">Me &amp; My Old Man</div>
  <div class="rule"></div>
  <div class="end-line">Stories That Matter.<br />With People You Love.</div>
  <div class="end-aside">Especially the funny ones.</div>
  <div class="end-url">meandmyoldman.co.uk</div>
</div>
```
```css
.end-aside { font-family: "Playfair Display", serif; font-weight: 400; font-style: italic; font-size: 34px; color: #bf5700; margin-top: 22px; transform: rotate(-3deg); display: inline-block; }
```
**Confirmed by Neil (2026-09-25): keep the `.end-aside` line and its execution exactly as
above** — italic, rust-coloured, slightly rotated like a stamp, sitting just under the main
two lines. Animate it in with a small overshoot (`back.out(1.7)`) from a steeper rotation
so it reads as "slapped on screen": `rotate: -8 → -3` alongside the fade/rise. Use this
`.end-aside` treatment as the default whenever a wrap-up or memento end card needs a
secondary line in a different register from the main tagline — don't invent a new
treatment per project.

## Known-good reference

`videos/griffiths-shower-story-wrap-up/` — first build of this format (Judith / shower
story clip, 3-up Riverside grid, title box in the gap between the top and middle tiles).
