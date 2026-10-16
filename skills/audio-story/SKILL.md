---
name: audio-story
description: >
  Builds a Me & My Old Man "audio story" video: a title card, a flowing
  waveform with synced captions, and an end card, all set to one narration or
  excerpt audio file. Uses HyperFrames. Trigger when Neil says "make an audio
  story for [family]", "waveform video", "turn this audio into a video with
  captions", or gives an audio file (with or without a transcript) and asks
  for a video/waveform version of it. Distinct from video-memento (photo
  slideshow, no captions) — an audio story has no photos, only a moving
  waveform and word-synced captions. Distinct from talking-head-recut and
  embedded-captions, which both start from video footage, not audio alone.
---
<!-- v1.0 — 2026-09-25: Created from the first build, Vaughan & Sue Griffiths "A Date, No Cake & A Proposal" (Love Letters, Coffee & Cake / famous no-proposal story), built as the audio-only companion to the existing video-memento of the same clip. Reused the memento's exact title/end-card style (cream #f6efe1, charcoal #2d2926, rust #bf5700, Playfair Display + Inter) for brand consistency across the two formats. -->
<!-- v1.1 — 2026-09-25: Neil rejected the first waveform treatment — a scrolling "conveyor belt" of bars sliding past a fixed centre playhead. Two corrections: (1) it read as constant motion with no felt link to the voice; (2) it was one flat block of solid rust, no shading. Replaced with a fixed mirrored equalizer (see "Building the waveform" below) — bars stay in place and spike up/down with real per-instant loudness, sit flat at true silence, and shade through a tan→rust colour tier by energy rather than one solid colour. Offered Neil 3 quick animated mockups (equalizer / breathing orb / radial pulse) before rebuilding, rather than guessing — he picked the equalizer. Worth doing that side-by-side step again for future style calls; it's cheap and avoids a second render/review cycle. -->
<!-- v1.2 — 2026-09-25: Same build, second correction pass — captions felt misaligned with the audio and too rushed. Two fixes: (1) one-line chunks (~7 words) were too short-lived; regrouped to ~13-word, two-line chunks so each caption holds long enough to actually read. (2) The real misalignment cause was trusting each chunk's own last-word `end` timestamp to decide the fade-out — Whisper's per-word end times bake in trailing silence and drift, so a caption could hang past or cut before the words actually being spoken. Fixed by holding each caption until the NEXT chunk's `start` time instead (minus a small gap) — anchoring every transition to a real, spoken timestamp rather than an unreliable `end` value. See "Getting a transcript" and "Sync pattern" below. -->
<!-- v1.3 — 2026-09-25: Same build, third correction pass — Neil said captions "don't match at all", and he was right: v1.2's fix was cosmetic, the real bug was structural. The story scene was positioned at data-start="5" (after the title card) and every caption/waveform time was offset by "+5" to land inside it — but the <audio> element itself was data-start="0", playing from the true start of the file the whole time. Global timeline time IS audio-file time whenever audio starts at 0; adding any extra offset for a later-starting visual scene silently desyncs anything timed off the transcript, by exactly that offset, for the ENTIRE rest of the file. Fixed by removing the offset entirely: story-scene now spans data-start="0" for the full audio duration (CSS opacity:0 by default so the title card can sit on top of it for the first few seconds without an extra positioning offset), and captions/waveform use the transcript's raw absolute times unmodified. Rule for next time: if a visual scene is delayed behind an intro card but the audio itself is NOT delayed (the intro plays over live audio, per the video-memento convention this skill inherited), never add the intro's duration to that scene's internal timings — anchor everything to raw audio-file time and only control visibility via the container's own opacity/fade, never via a time offset. -->
<!-- v1.4 — 2026-09-25: Same build, fourth correction pass — three separate notes: (1) transcription errors in the captions ("talk" for "talking", "Crips" for "Cripps", "dinner at home" for "dinner at Hall", "Dr Adam" for "Notre Dame", "calling off" for "cooling off"). Whisper output is a starting point, not ground truth — always proof-read the generated captions.json against the audio/a human transcript before locking timing, not just after Neil flags it. (2) A caption cue starting exactly ON its word's timestamp still reads as a beat late, because the fade-in (was 0.35s) plus the rise animation delays full legibility past the moment the word is heard. Added a small fixed LEAD (0.15s) subtracting from every cue's start, and shortened the fade durations (0.35s→0.22s in, 0.3s→0.2s out) — captions should anticipate slightly, not trail. (3) Neil wanted the end card brought forward from the tail of the file (224.5s, ~6s before the very end) to 3:38.5 (218.5s), right after the last spoken line — the ~16s of trailing audio after the transcript's last word doesn't need a full-length waveform scene sitting under it. When there's a long gap between the last transcribed word and the audio's true duration, ask whether the end card should come in near the last word instead of at a fixed offset from the file's end. -->

# Audio Story

An audio story turns one audio excerpt (a chapter clip, a wrap-up soundbite,
a standalone story) into a shareable video with no photos at all: title card
→ a flowing waveform with synced captions → end card. Same house style as
`video-memento`, different visual body — a waveform that moves to the voice
instead of a Ken Burns slideshow.

## Trigger

Neil hands over an audio file (mp3/wav) and a title. He may also give a
transcript (txt/doc) — if he doesn't, extract the voiceover and generate
captions yourself (see "Getting a transcript" below). He may point to a past
audio story or memento as the style reference. Never invent a title, caption,
or date — ask if missing.

## Before building

1. **Read the family's facts.** Never caption with an invented year, age, or
   description.
2. **Find the style reference.** If this family already has a `video-memento`
   built, reuse its exact title-card and end-card CSS values (colours, fonts,
   copy structure) rather than re-deriving them — read its `index.html`
   directly. Otherwise pull frames from a finished memento the same way
   `video-memento` does (`ffmpeg -ss 2 -i ref.mp4 -frames:v 1 title.png`).
   House style: cream background (`#f6efe1`), charcoal text (`#2d2926`), rust
   accent (`#bf5700`), serif display face for title/end lines (Playfair
   Display), tracked-uppercase sans kicker/meta (Inter).
3. **Confirm aspect** with Neil (vertical 9:16 default, matching the memento
   format) — this is a `/general-video` route inside HyperFrames.

## Getting a transcript

- If Neil supplies a transcript file, use it for wording and story context,
  but **do not trust its timestamps** if it's a transcript of a raw source
  recording rather than the exact delivered audio file — an edited excerpt
  is very often re-cut from the raw interview and the timings won't line up.
  Check the transcript's total duration against `ffprobe`'s duration for the
  actual mp3; if they differ, the transcript is describing different audio.
- **Always generate word-level timestamps from the actual audio file itself**
  with `npx hyperframes transcribe <audio>.mp3 --output assets/transcript.json`
  — this is what drives caption sync, regardless of whether Neil also gave a
  transcript. A supplied transcript is useful for spelling/wording checks
  (correct a name Whisper mis-heard) but the timing must come from the real
  file.
- **Group words into two-line caption chunks (~12-13 words / ~75-80 chars,
  breaking on sentence punctuation), not one-liners.** A one-line-per-chunk
  (~6-7 words) build shipped first and felt rushed — chunks changed faster
  than they could be read. Split the chunk's text into two roughly-even
  lines at the nearest space to the midpoint.
- **Never trust a chunk's own last-word `end` timestamp to decide when it
  fades out.** Whisper's per-word `end` times bake in trailing silence and
  drift from what's actually being said — using it caused a visible
  misalignment between captions and audio on the first pass. Instead, hold
  each caption until the *next* chunk's `start` time (minus a small ~0.1s
  gap) — every transition then anchors to a real, spoken timestamp instead
  of a timestamp that can silently include dead air.

## Building the waveform

There is no ready-made waveform block in the HyperFrames catalog (checked
`npx hyperframes catalog` — `oscilloscope-trace` is a decorative CRT effect,
not amplitude-driven). Build one from the real audio. **A scrolling
"conveyor belt" waveform (bars sliding past a fixed playhead) was tried and
rejected** — it reads as constant motion disconnected from the voice, and as
one flat block of colour. The working pattern is a fixed mirrored equalizer:

1. **Decode PCM and compute an RMS envelope** over a tight ~1/30s window —
   tight enough to feel responsive to individual syllables, not just
   sentence-level swells:
   ```bash
   ffmpeg -v error -i audio.mp3 -ac 1 -ar 24000 -f s16le -
   ```
   then in Python, RMS per window, normalize to 0..1 against the file's own
   max, **noise-gate it** (anything below ~6% of peak snaps to exactly 0 —
   true silence must read as flat, not idly wobbling), then apply a punchy
   curve (`x ** 1.5`) so real energy pops and mid-level noise stays
   suppressed. This is what makes the motion feel *sensitive to the voice*
   rather than constant — the single biggest note from the first build.
2. **Sample at ~30/second**, light 2-point smoothing only (a heavier smooth
   re-introduces the "always moving" problem). Store as a small JSON file
   (`assets/waveform-track.json`), not inlined in the HTML.
3. **Render as a fixed row of `<div>` bars** (12-16 bars is plenty), one
   flex row, `align-items: center`, each bar's `height` set directly per
   frame — because the row is vertically centred, a bar's own height growing
   mirrors it symmetrically up/down from the baseline for free, no extra
   canvas or transform math needed.
4. **Give each bar a small deterministic personality** so the row reads as
   an equalizer (different bands) rather than one pulsing block: a fixed
   per-bar time offset (±0.1s, sampling the envelope very slightly
   early/late) and a fixed per-bar gain multiplier. Derive both from a
   stable hash of the bar's index (e.g. `Math.sin(i * 12.9898) * 43758.5453`,
   fractional part) — **never `Math.random()`**, the project's determinism
   rule bans it; the render must produce identical output on every pass.
5. **Shade by energy, not one solid colour.** Neil's second correction on
   the first build: don't paint every bar the same brand rust. Tier the bar
   colour by its own current amplitude — quiet bars sit in a soft muted tan,
   loud ones deepen through mid rust to the full brand accent at peak. This
   reads as "different shadings" and ties colour to loudness, which is
   meaningful rather than decorative.
6. **No playhead line, no scroll.** Bars stay in their fixed positions for
   the whole scene; only their height and colour change per frame.

## Sync pattern (HyperFrames)

One `gsap.timeline({ paused: true })`, registered under
`window.__timelines[<composition-id>]`, same as every HyperFrames comp:

- **Waveform:** a single linear tween on a dummy object (`{t: 0}`) running
  the length of the story scene, `ease: "none"`, with an `onUpdate` that
  reads that elapsed time, looks up each bar's own offset/gain, and sets
  its `height`/`background` directly. One tween drives every bar — don't
  give each bar its own GSAP tween, the per-bar variation comes from the
  fixed offset/gain hash, not from separate animations.
- **Captions:** one `fromTo`/`to` pair per caption chunk timed directly off
  the real `start`/`end` from the transcript JSON (offset by the story
  scene's start time on the master timeline). Fade + small rise in, hold,
  fade + small rise out.
- **Caption exit kill (mandatory — `npm run check` fails without it):** after
  every caption's exit `tl.to(el, { opacity: 0, ... })`, add
  `tl.set(el, { opacity: 0, visibility: "hidden" }, holdEnd)` as a
  deterministic kill, and `tl.set(el, { visibility: "visible" }, start)`
  before its entrance tween. This is HyperFrames' own lint rule
  (`caption_exit_missing_hard_kill`) — word-level/caption tweens can leave
  text stuck on screen without a hard kill at the end of the exit.
- **Fetch data before building the timeline**, same pattern as
  `document.fonts.ready` in `video-memento`: `await` the waveform and
  caption JSON fetches inside an async IIFE, build all the DOM/canvas setup,
  *then* build and register the GSAP timeline. Building before the data
  arrives races the render engine's first seek.

## Title/end card copy

Same conventions as `video-memento`: kicker "ME & MY OLD MAN" → rust rule →
serif headline → sans subtitle/byline → one meta line with the real
recording month Neil supplied. End card is the fixed brand line ("Stories
That Matter. With People You Love." + `meandmyoldman.co.uk`) unless told
otherwise. If a memento of the same clip already exists, reuse its exact
title/subtitle/meta text so the two deliverables read as a matched pair.

## Checks before render

```bash
npm run check      # lint + runtime + layout + motion + contrast — must pass with 0 errors
npx hyperframes snapshot --at <a few key timestamps> -o /tmp/snap
```
Read back the contact sheet before rendering. Confirm: title/end card match
the memento's style, waveform bars are legible against the cream background
(this failed contrast check on the first build at 85% opacity muted grey —
kicker/meta text needs full opacity `--text-soft`, not a faded `--muted`),
and a couple of caption frames mid-story for wording/timing sanity.

`content_overlap` info-lines during caption cross-fades are expected and
fine to leave — two captions briefly sharing the frame during a 0.3-0.35s
transition is not the same as unreadable overlap.

## Delivery

Same as `video-memento`: render lands in `renders/`, always produce a
WhatsApp-shareable compressed copy before sending, and don't delete the raw
render until the compressed file's size is confirmed under ~15MB:
```bash
ffmpeg -y -i "<raw render>.mp4" -vf "scale=1080:1920:flags=lanczos" \
  -c:v libx264 -preset slow -crf 26 -maxrate 620k -bufsize 1240k \
  -c:a aac -b:a 112k \
  "<slug>_whatsapp.mp4"
```
Send the compressed file to Neil by default; keep the raw in `renders/`.
