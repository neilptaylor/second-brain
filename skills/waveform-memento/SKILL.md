---
name: waveform-memento
description: >
  Builds a Me & My Old Man "waveform memento": a title card, a live audio
  waveform/EQ visualisation with burned-in word-timed captions, and an end
  card, all set to one narration or excerpt audio file, with no photos or
  footage. Uses HyperFrames. Trigger when Neil says "waveform memento",
  "make a waveform video for [family]", or asks for an audio excerpt turned
  into a captioned waveform video rather than a photo slideshow. Distinct
  from video-memento (Ken Burns photo slideshow) — this format has no
  stills, just a reactive waveform and captions against the audio.
---
<!-- v1.0 — 2026-09-25: Created from the first build, Vaughan Griffiths "Bottle Tops & Bomb Shelters", styled off the existing griffiths-no-proposal-audio-story HyperFrames project. Encodes four correction passes from that one build: waveform colour must stay inside the brand palette, captions must be a hard 2-line cap by character width not word count, end-card/fade timing must be re-derived per file (never copied from a reference project), the HyperFrames render pipeline itself has a known audio-mux desync bug past ~100s requiring a manual remux fix, and final caption/fade timing should follow the client's own ear-timed cues over raw whisper timestamps. -->
<!-- v1.1 — 2026-09-25: Added a standard music-bed step, missing from v1.0 (the Griffiths "Facing Death, Choosing Life" build had no music at all until Neil asked for one, and no prior waveform-memento build had one on disk to copy from). The org's music stings live locally at ~/Downloads/MMOM_New_Stings/ (synced from a Drive folder) — 29 short piano/guitar/harp cues, 18-40s each, meant as loop material. `media-use`/HeyGen needs an interactive OAuth login this skill's usual non-interactive session can't do, so the stings folder is the first place to check, not the catalog. -->
<!-- v1.2 — 2026-09-25: "Restless Painter & Savvy Entrepreneur" build still read as orange and started animating over silence, even though the colour lerp code already used only the two brand tokens. Root cause was upstream: RMS taken across room-tone/silence before speech onset read as mid-amplitude motion once normalized against the file's peak, and a *linear* amplitude→colour lerp already looks rust-orange by t=0.3, which is where most real speech energy sits. Added: a noise-gate floor on the RMS envelope before the 0.6 power curve, a hard-zero before the transcript's real speech-onset (title card holds opaque until just before it, not a fixed ~5s), and a separate steeper gamma (^1.6) on amplitude specifically for the colour lerp, distinct from the height/motion curve. Using only the two brand tokens is necessary but not sufficient — the amplitude curve feeding the lerp needs checking too. -->
<!-- v1.3 — 2026-09-28: Josephides "Poor Lizards" build (a punchline-ending story) surfaced two corrections. (1) The opening title card showed "Poor Lizards" up front, spoiling the line the speaker lands the clip on — added the "Title reveal" section: when the story's own last line is also the title, withhold it from the opening card and reveal it inside the end card right after he actually says it. (2) Neil reported the music "fades out too soon" and "some other track starts playing." Root cause of the second: the standard 2-3s crossfade loop only blends the seam, not the ~18-21s of raw, un-blended repetition after it — that raw restart of the sting's own intro landed right under the swell/end-card and read as a second track kicking in. Fixed by loading crossfade to ~50% of the clip length (10-12s) so no point in the loop is ever a cold restart. Root cause of the first: the fade-to-zero envelope ramped down across the entire end-card hold, so the music was audibly leaving well before the card finished its job — fixed by holding at swell level through the end card and only fading in the final ~2s of the video. -->
<!-- v1.4 — 2026-09-28: Second review pass, same Josephides build. Neil corrected the v1.3 fixes further: (1) music STILL stopped abruptly (at 1:59, exactly where the narration's own fade-out ends) — root cause was a genuine ffmpeg bug, not a design error: a 5-level nested `if(lt(t,...),...)` expression passed to `volume=eval=frame:volume='...'` silently fails to evaluate past the first couple of branches on a file of this length, producing a near-flat, quiet output despite reading back with no error — confirmed by testing 2-3 level nesting (works), then the full 5-level expression (flat/broken), with numeric proof via `volumedetect` at fixed timestamps. (2) He wanted "Poor Lizards" appearing fully on its own, not sharing the frame with the end card's kicker/rule that had already faded in. (3) He wanted the end-card's typographic treatment applied to the title card too, with the WEBSITE on the title card and the RECORDING DATE moved to the end card (reversed from his own first phrasing mid-message — the later instruction in a self-corrected message wins). | RULE: (1) Never build a multi-branch time-based gain envelope as one large nested `if()` expression in ffmpeg's `volume` filter — build it as separate segments instead: extract each time range to its own file first with a plain `-ss/-t` cut (`-c copy`, so the filter's own `t` starts at 0 for that segment), apply a SIMPLE (≤2-level) volume expression or constant to each segment separately, then join with the concat demuxer (`-f concat -c copy`). Verify each segment's loudness with `volumedetect` (using a WIDE, multi-second window — a short 0.3-0.5s window on real music reads as erratic/misleading because it catches individual note attacks and silences between them, not the macro envelope) before concatenating, and re-verify the joined file the same way. (2) A "solo reveal" title (the punchline text with nothing else on screen — no kicker, no rule) needs its own dedicated timed `.clip` between the story and the end card, not a title element nested inside the end-card's own div where the end card's other chrome (kicker/rule) is already visible. (3) When Neil's own message self-corrects mid-stream ("do X — actually no, Y instead"), the later statement is the instruction; don't average or half-apply both. -->
<!-- v1.5 — 2026-09-28: Third review pass, same Josephides build — Neil reversed v1.3's whole "withhold the title" premise. He wants the title card back to the STANDARD front-loaded layout (title text + subtitle + date, upfront, even when the closing line is the punchline) — the "spoiler" framing in v1.3 was this skill's own assumption, not something he'd asked for. Separately, the mid-video "Poor Lizards" moment should be a CAPTION-styled callback (same size/font as the running captions, sentence case, "Poor lizards.") on a blank beat, not a second big title screen — his exact words: "I wanted it on its own as a caption. Not as a title!!". And the end card reverts fully to the original (tagline + website); the date/website swap from v1.4 is undone — date stays on the title card, website stays on the end card. | RULE: Rewrote the "Title reveal" section as "Title card and the punchline moment" — default is now the plain, standard title card (no withholding), and a punchline callback (when wanted) is explicitly a `.caption-line`-styled element, never `.title-main`. Cross-cutting: when a stylistic pattern gets added to a skill off a single build's outcome, treat it as provisional until confirmed on a second pass — Neil approving the render once is not the same as him confirming he wants that pattern as the new default going forward. -->
<!-- v1.6 — 2026-09-28: Fourth review pass, same Josephides build. Even after v1.5's caption-styled callback and the v1.4 crossfade fix, Neil still heard "that new track that comes in" — the swell into the end card was itself the problem, not just the loop-restart artifact. He asked to cut the caption callback entirely and have the end card "coming on in silence." | RULE: Cut the reveal-caption clip and the music-bed swell for this build; bed now fades to TRUE silence together with the narration by the point the story ends, and the end card runs with no audio under it at all. Added to "Music bed": if Neil flags "another track" a SECOND time after the crossfade-loop fix, stop re-tuning the swell/crossfade parameters and switch to a flat fade-to-silence bed instead — a swell into the end card is the default, but it is not worth defending after two rounds of the same complaint. Cross-cutting: when the same class of complaint ("something audibly changes near the end") survives a targeted technical fix, consider that the FEATURE itself (not just its implementation) may be what's unwanted, rather than continuing to patch the implementation. -->
<!-- v1.7 — 2026-10-02: Beard "Six Brothers Go & One Left Behind" build. Neil, who normally edits the music fades himself, handed over the fades as a brief for the first time and asked for the brief plus this build to be kept as the worked example. Added the "Brief-driven music arc" section, the arc mixer at references/music-arc-mix.py (numpy, builds the whole gain envelope in code, so no nested ffmpeg `if()` and no concat segments), and the title card now carries a "Recorded in [Month Year]" meta line again (confirm the date with Neil, never invent it). | RULE: when Neil supplies a music brief like the one below, follow it literally and use the arc mixer; the default music bed section applies only when he gives no brief. -->

## Speech onset, noise floor, and colour gamma — check these even when the colour code looks right

Two upstream problems can make a technically-correct 2-token waveform still
read wrong, and both surfaced on the same build:

1. **Silence/room-tone before the subject starts talking reads as motion.**
   RMS is normalized against the *whole file's* peak, so quiet lead-in audio
   (breathing, room tone, a mic bump) can land at 0.2-0.5 normalized
   amplitude — enough to visibly move bars and tint them before anyone is
   actually speaking. Whisper can also hallucinate a word at ~0.00s during
   that silence; don't trust word index 0 as the real speech start without
   checking it against the rest of the transcript's timing gap.
   - Find the **real** speech-onset timestamp (the first word after any
     multi-second gap from t=0, not necessarily word index 0 in the
     transcript).
   - Noise-gate the RMS envelope before the existing 0.6 power curve:
     `gated = max(0, normalized - FLOOR) / (1 - FLOOR)`, `FLOOR ≈ 0.15-0.16`
     of the file's own peak (tune per file — check the envelope's values in
     the first several seconds before committing to a number).
   - Hard-zero the envelope for every frame before the real speech-onset
     time, regardless of what the gate leaves behind.
   - Hold the title card **opaque until just before speech onset**, not a
     fixed ~5s — extend `data-duration` on the title card and shift the
     story-scene/eq/caption entrance to land right as speech starts. The
     waveform and captions must never appear over dead air.

2. **A linear amplitude→colour lerp reads as orange well before "peak."**
   Speech energy for a typical clip sits mostly in the 0.2-0.5 normalized
   amplitude band. Lerping muted→rust linearly by that same amplitude
   already produces a visibly rust/orange mix by t≈0.3, so most of the
   waveform reads orange even though the code is only using the two approved
   tokens — this is the failure mode to check for specifically when Neil says
   "orange again" but a code read shows the tokens are correct.
   - Apply a **separate, steeper gamma to the colour mix only** (leave the
     bar-height/motion amplitude alone): `t = Math.pow(amp, 1.6)` (tune per
     file by eye — check a mid-story still, not just the numbers). This
     keeps mid amplitudes closer to resting grey and reserves the rust
     accent for genuine peaks.

## Trigger

Neil hands over: an audio file (mp3/wav), a family name, and a title (or
enough to derive one). No photos are involved — this is the format for when
he explicitly wants a waveform/EQ visual with captions, not a Ken Burns
slideshow (`video-memento` handles that). Ask which format he wants if it's
ambiguous.

## Before building

1. **Find a prior waveform-memento project to copy the structure from.**
   Check `videos/*/index.html` for an existing composition with a
   `story-scene` / `#eq` / `caption-wrap` pattern (e.g.
   `videos/griffiths-no-proposal-audio-story/`). Copy its `index.html`,
   `package.json`, `AGENTS.md`/`CLAUDE.md`, and `assets/fonts/` wholesale as
   the starting point — don't rebuild the GSAP/HTML structure from scratch.
2. **Transcribe the audio locally** with whisper.cpp for word-level
   timestamps (a proper model, not the tiny test model that ships with
   homebrew's whisper-cpp):
   ```bash
   ffmpeg -y -i "<source>.mp3" -ar 16000 -ac 1 -c:a pcm_s16le audio.wav
   whisper-cli -m <path-to-ggml-small.en.bin-or-better> -f audio.wav \
     -oj -ojf -osrt -of transcript -sow
   ```
   If no real model is on disk, download one first
   (`ggml-small.en.bin` from `huggingface.co/ggerganov/whisper.cpp` is
   sufficient). Tell Neil plainly that this is a machine transcript and
   should be checked before anything client-facing goes out — don't present
   it as verified.
3. **Merge whisper.cpp's sub-word tokens back into real words** before
   using them for anything. Tokens without a leading space are continuations
   of the previous token (`"se"`, `"ag"`, `"ull"` → `"seagull"`); merging on
   leading-space is required or names and compound words come out mangled.

## Generating the two data assets

**`waveform-track.json`** — a 30fps RMS amplitude envelope of the whole
file, used to drive the EQ bars:
```python
# decode to mono PCM at 48kHz, take per-frame RMS at composition fps,
# normalize to 0..1 against the file's own peak, apply a gentle **0.6
# power curve for a natural level-meter feel. rate=fps, matches waveDriver.
```
Output shape: `{"rate": 30, "duration": <seconds>, "peaks": [0..1, ...]}`.

**`captions.json`** — two-line caption chunks, **wrapped by character
count, never by word count.** Greedily wrap words into lines capped at
**~34 characters** (fits Playfair Display 46px in a 900px-wide caption box
at this composition's dimensions — recompute the cap if font size or box
width differ), then group **exactly 2 wrapped lines per on-screen caption,
never 3.** A word-count target (e.g. "~13 words per chunk") reliably
produces 3-line wraps on longer words and got caught by Neil on the first
build here — character-count wrapping is the only reliable method.
```python
MAX_CHARS = 34
# greedy-wrap words into lines <= MAX_CHARS, then pair every 2 lines into
# one caption entry: {"line1", "line2", "start": <first word start>,
# "end": <last word end>}
```

## Build pattern (HyperFrames)

Reuse the copied reference project's structure: title card (~5s, opaque,
sits on top of the audio which starts at absolute `data-start="0"`) → a
`story-scene` clip holding a fixed mirrored EQ (`#eq`, N bars, each with a
small per-bar deterministic time-offset and gain via a `sin`-hash, **no
`Math.random()`**) and a `caption-wrap` → an end card.

**Waveform colour must interpolate between only the two defined brand
tokens** — `--muted` (#8c857c, resting) and `--accent` (#bf5700, peak) —
**never invented intermediate warm/sand/tan tones.** A tiered palette with
extra named colours in between reads as generic orange rather than the
actual brand, and Neil will catch it immediately. Interpolate linearly by
RGB between the two tokens as a function of amplitude:
```js
const REST_RGB = [140, 133, 124]; // var(--muted)
const PEAK_RGB = [191, 87, 0];    // var(--accent)
// lerp per-channel by clamped amplitude, return rgb(...)
```

**Every absolute timestamp in the timeline must be re-derived from THIS
audio file, never copied as a literal number from the reference project.**
The first build here hard-copied `101.2s` / `101.5s` end-card timing from a
230s reference file onto a 113s file, cutting the story off mid-sentence.
Before writing any timeline numbers:
- Read `captions.json`'s **final entry's `end`** — that is the real point
  the story content finishes.
- Set the story-scene fade-out at (last caption end + ~0.5-0.8s buffer),
  the end-card `data-start` just after that, and the stage's total
  `data-duration` to comfortably cover the end card's full hold.
- Sanity-check the chosen fade point against `captions.json`'s last entry
  in a print statement or by eye **before** rendering, not after Neil
  catches it in playback.

**If Neil later gives exact ear-timed cues** ("he says X at 1:42", "end
card should start at 1:48") **from watching the actual delivered video,
those cues override the whisper timestamps** for final polish — whisper's
word timing can land a couple of seconds later than what's actually heard,
especially near the end of a clip. Retime the relevant caption(s)
`start`/`end` to match his cues directly rather than re-deriving from the
transcript.

**A synchronised fade (audio fading out while the end-card title finishes
its own entrance) is driven off two shared anchor points, not tuned
per-element.** Given a start time S and an end time E Neil specifies (e.g.
"end card starts at 1:48, music fades slowly until 1:53"):
- Set the `<audio>` element's `data-fade-out` to exactly `E - S`, so the
  fade-out window is `[S, E]`.
- Stagger the end-card's visual entrance elements (kicker/container, title
  line, url) so the **last** one's tween finishes at `E`, not sooner —
  spread their start times across `[S, E]` rather than firing them all at
  once with short durations.

## Title card and the punchline moment — default to the standard layout

**Default is the standard front-loaded title card** — kicker, rule, big
`.title-main` title text (the family/story's actual title, even when
that title is also the story's closing line — e.g. "Poor Lizards"),
subtitle ("An excerpt from [Name]'s Life Story."), meta ("Recorded in
[Month Year]"). Do NOT withhold the title from the opening card by
default, even when the closing line is a punchline. An earlier version of
this skill tried withholding it and revealing it as a big standalone
title card later — Neil tried it and reversed the decision; don't
reintroduce that pattern without him asking for it specifically.

**If Neil DOES want the punchline called back at the moment he says it**,
that's a **caption-styled callback, not a second title card**:
- Its own dedicated timed `.clip`, sitting between the story scene and
  the end card, with nothing else on screen (no kicker, no waveform).
- Text styled and positioned EXACTLY like the running captions —
  `.caption-line`'s font (Playfair Display, 46px, weight 500), same
  general vertical position — not `.title-main`'s 84px title size. It
  should read as if it's the story's last caption on a blank beat, not as
  a new title screen. Use sentence case with the natural punctuation he
  actually said ("Poor lizards.") rather than title case.
- Brief hold (~2.5-3s) is enough; it's a beat, not a scene.
- The end card that follows is the standard one — kicker, rule, tagline,
  **website** — unchanged. Don't move the recording date onto the end
  card or the website onto the title card; date lives on the title card
  (in its meta line), website lives on the end card, as in every other
  waveform-memento.

## Music bed (default, not on-request)

Every waveform-memento carries a very light instrumental bed under the narration unless Neil says otherwise — a bare waveform reads cold against this content. Add it as a standard build step, before checks:

1. **Source it locally first.** Check `~/Downloads/MMOM_New_Stings/` for a calm, non-percussive piano/strings/harp sting matching the piece's tone (the filenames describe mood — "Nostalgic", "pensive", "calm lullaby" etc.). Only fall back to `media-use` (`resolve --type bgm`) if nothing there fits or Neil wants something specific it doesn't have — that path needs `heygen auth login --oauth`, which a non-interactive session cannot run, so flag it to Neil rather than stalling silently.
2. **These stings are short (18-40s), not full-length beds — loop with a LARGE crossfade (10-12s, roughly half the clip), never a short one.** A short crossfade (2-3s) avoids an audible hard seam but does NOT stop each new repetition sounding like a fresh, unblended restart of the piece once the brief overlap ends — the sting's own intro/build plays through again at full, un-blended strength for most of its length. On a ~2-minute video this restart reliably lands right under the swell/end-card, at which point it reads as **a second, different track kicking in** — this is the single most likely cause if Neil says "another track starts playing" even though there's only ever one file in the mix. A crossfade of ~50% of the clip's own length keeps every point in the bed a blend of at least two overlapping instances, so there's no raw, cold restart anywhere in the timeline:
   ```bash
   ffmpeg -y -i sting.wav -i sting.wav -filter_complex "[0][1]acrossfade=d=12:c1=tri:c2=tri" loop2.wav
   # repeat, feeding loop2.wav back in as the first input, until the result comfortably
   # exceeds the story's own duration, then trim to exact length with -t
   ```
3. **If Neil flags "another track kicks in" a SECOND time after the crossfade fix in step 2, stop tuning the swell — drop it entirely.** The swell/crescendo pattern below is the default, but on the Josephides build it kept triggering the "new track" complaint even after fixing the crossfade loop. After several rounds, what he actually wanted was simpler: no swell at all — the bed stays quiet and flat under the narration and fades to TRUE SILENCE together with the narration by the point the story ends, and the end card comes on over silence with no music under it. If a second complaint about the ending's music comes in, don't keep re-tuning the envelope — switch to this flat-fade-to-silence pattern instead of iterating further on the swell.
4. **Otherwise (default): keep it very quiet under narration, swell once, then hold through the end card and only fade in its final couple of seconds — not across the whole end-card hold.** Fading the bed down over the entire end-card duration reads as the music leaving before the card has finished doing its job ("fades out too soon"), even though it technically reaches zero exactly on the last frame.
   - Resting level under narration: around **-22dB (≈0.08 linear)**.
   - A gentle crescendo only in the **last 5-8s of the story content** (never earlier — a swell mid-story competes with the words), rising to around **-13dB (≈0.22 linear)**.
   - **Hold at that swell level through the end card** — don't start ramping down the moment the end card appears.
   - Fade to true zero only in the **final ~2s of the video**, so the bed is still audibly present while the end-card title/tagline are on screen and only leaves right at the very last beat.

   **Build this as separate segments joined by the concat demuxer — never as one large nested `if()` expression in `volume=eval=frame`.** A ≥4-level nested `if(lt(t,...),...)` expression silently fails to evaluate correctly on a file this long: it produces near-flat, quiet output for the whole file (no error, no warning — `ffmpeg`'s own stderr looks clean), which is exactly what "the music fades out too soon" or "never really swells" looks like when Neil hears it. Confirmed on the Josephides build: a 2-3 level nested expression works fine, a 5-level one doesn't. Extract each time range to its own file FIRST (so the filter's own `t` starts at 0 for that segment, not the source file's absolute time), apply a single constant or simple 1-clause ramp per segment, then concatenate:
   ```bash
   # 1. cut each range to its own file (plain seek, no filter yet)
   ffmpeg -y -i bed_looped.wav -ss 0    -t 2     -c copy raw1.wav   # ramp in
   ffmpeg -y -i bed_looped.wav -ss 2    -t 110.1 -c copy raw2.wav   # rest
   ffmpeg -y -i bed_looped.wav -ss 112.1 -t 6    -c copy raw3.wav   # swell ramp
   ffmpeg -y -i bed_looped.wav -ss 118.1 -t 8.9  -c copy raw4.wav   # hold through end card
   ffmpeg -y -i bed_looped.wav -ss 127.0 -t 2    -c copy raw5.wav   # fade to zero

   # 2. apply a SIMPLE (single-clause, no nesting) gain to each segment on its own —
   #    t is now local to that segment (0..segment length), so the maths are trivial
   ffmpeg -y -i raw1.wav -af "volume=eval=frame:volume='(t/2)*0.08'"        s1.wav
   ffmpeg -y -i raw2.wav -af "volume=0.08"                                   s2.wav
   ffmpeg -y -i raw3.wav -af "volume=eval=frame:volume='0.08+0.14*(t/6)'"   s3.wav
   ffmpeg -y -i raw4.wav -af "volume=0.22"                                   s4.wav
   ffmpeg -y -i raw5.wav -af "volume=eval=frame:volume='0.22*(1-(t/2))'"    s5.wav

   # 3. join — no re-encode, no gain re-application
   printf "file 's1.wav'\nfile 's2.wav'\nfile 's3.wav'\nfile 's4.wav'\nfile 's5.wav'\n" > list.txt
   ffmpeg -y -f concat -safe 0 -i list.txt -c copy bed_final.wav
   ```
   **Verify with `volumedetect` using a WIDE window (2-3s+), never a short one (0.3-0.5s).** A short window on real music (piano, guitar) reads as erratic and misleading — it catches individual note attacks and the silence between them, not the macro envelope, and can look "broken" even when the envelope is correct. Sample every ~1-2 minutes across the full bed and confirm a smooth, monotonic trend (quiet → swell → hold → fade), not the segment boundaries themselves.
4. **Mix after the render's audio is already resynced, not before.** Build the bed alongside the clean narration `.wav`, mix them with `amix` (compensate for its default `1/N` gain drop with a matching `volume=N` after), and only then remux onto the video track — running the mix before the known desync-fix step would just bake the drift into the music too.
5. **Re-run the standard verify-transcription check** on the finished mix — the extra track shouldn't move any word's timing, but confirm it, not assume it.

## Brief-driven music arc (when Neil gives fade guidance)

Normally Neil edits the fades himself. When he hands over the audio and the music sting and says "I want you to execute this", this section replaces the default music bed. Inputs: the narration .wav, one music sting .wav (from the Drive folder "Music & Stings/Stings 2024-26/09 Memento Stings"), a title, the family and the recording month. Ask for the recording month if he has not given it. Never invent it.

**His brief, verbatim (Beard build, 2 Oct 2026):**

> * 0:01" titles come on screen, at same time intro music slowly fades in for 3-5"
> * As the title fades out from the screen, fade out the music, and fade in the Voice over alongside the Waveform and captions to match
> * From this point on until the end, we just hear the voiceover
> * Then approx 10" before the end, slowly fade in the music again cueing to the listener very smoothly that this is almost the end of the clip. 
> * Gradually build the music - never ever make it fight with the VO, it's only there to enhance
> * 1" after the last word, the music can crescendo again smoothly
> * End card for 3-5" and then fade out music and end card in sync

**How it was executed (all times are video time, D = voiceover start):**

| Moment | Time | What happens |
|---|---|---|
| Title in | 1.0s | Card fades in, kicker, rule, title, subtitle, meta staggered to ~3.4s |
| Intro music | 0.8s to 4.4s | Sting from its start, smoothstep fade in to 0.75 gain (3.6s, inside the 3-5s ask) |
| Title out / music out | 5.0s to 6.3s | Card fades 5.0 to 5.8, music fades 4.9 to 6.3 |
| VO in | D = 5.8s | 0.4s fade in on the voice, waveform and captions fade in with it (5.6s) |
| VO only | D to 10s before end | Nothing else under the voice |
| Music returns | last word minus ~10s | Sting restarted from its beginning, smoothstep build from 0 to 0.10 gain, about 11 dB below the voice at its loudest, never competing |
| Crescendo | last word + 1.0s | Smoothstep from 0.10 to 0.80 over 2.4s |
| End card | last word + ~0.7s | Story scene fades out, end card fades in, held about 4s |
| Out together | 2.0s fade | Music and end card fade to zero over the same 2.0s, ending on the final frame |

Beard numbers: voiceover 91.96s (last word ends 91.6s), D = 5.8, last word at 97.4s, music returns 87.0s, crescendo 98.4s, end card 98.0s, fade out 102.4s to 104.4s, total 104.4s. Re-derive every one of these from the new file's own last-word time, never copy them.

**Mechanics that matter:**
- The waveform and captions run on audio time + D. Pad the narration inside the mix at D, not by editing the source file. `waveform-track.json` and `captions.json` stay in audio time; the HTML timeline adds D.
- The waveform track needs no speech-onset zeroing when the voice starts at 0.04s, but still apply the noise gate (FLOOR 0.15) and the 1.6 colour gamma.
- Build the whole mix in `references/music-arc-mix.py` (numpy: one smoothstep gain curve per music instance, voice laid in at D, music instances summed on top, peak-normalised). Set a venv with numpy first (`python3 -m venv /private/tmp/claude-502/venv && pip install numpy`); the system python has none. Save the result as `mix.wav`, make `mix.mp3` for the composition's `<audio>`, and use `mix.wav` for the remux.
- A short sting (the Beard one is 22.6s) is used twice from its own beginning, once for the intro and once for the outro, rather than looped. Check the sting is long enough for the outro (return time to end of video, about 17s here). If not, loop with the large crossfade from the Music bed section.
- Verify with `volumedetect` in 2s windows: intro near -24 dB mean, voice-only about -20 dB, final crescendo near -20 dB, last 2s dropping to about -29 dB and then silent.
- Run the normal render, then the manual remux from the Known render bug section, using `mix.wav` as the audio. This build was 104s, past the drift threshold, so the remux is mandatory.

**Title card on this variant:** kicker, rule, title (two lines if long: "Six Brothers Go<br />& One Left Behind"), subtitle "An excerpt from [Full name]'s Life Story.", and the meta line "Recorded in [Month Year]". Neil gave the full name and month when asked, so ask for them rather than guessing from the Drive folder name.

**Worked example:** `videos/beard-six-brothers-one-left-behind/` (index.html, work/mix.py, renders/). Source files were `EDITOR Neil/Beards Mementos/Six Brothers Go & One Left Behind.wav` and `Music & Stings/Stings 2024-26/09 Memento Stings/best - journey steel guitar - start fade out at 12s .wav`. The machine transcript fix "Bellson" to "Belsen" is the kind of proper-noun slip to check on any war or place name.

## Checks before render

```bash
npm run check     # lint + runtime + layout + motion + contrast
```
The three `nested_structure_needs_subcomposition` warnings (title-card,
story-scene, end-card) and the `.end-url` contrast warning are expected —
they're the same house-style tradeoffs as `video-memento` and not worth
fixing for a one-off. Scrub the title card, a mid-waveform frame, and the
end card by extracting stills with ffmpeg and reading them back — confirm
captions are genuinely 2 lines, not wrapping to 3, and the waveform reads
as brand colours, not orange.

## Known render bug: audio desyncs past ~100s — verify and fix every time

**The HyperFrames render pipeline itself has a bug where the baked-in audio
track can drift out of sync with the (frame-accurate) video track on
compositions past roughly 100 seconds.** This is not a composition timing
error — the captions/waveform stay locked to composition time throughout;
only the muxed audio drifts, increasingly, reaching several seconds of
offset by the end of a ~113s clip in the build that surfaced this. Ruled
out as causes: `--workers 1`, re-encoding the source MP3 to remove
ID3/VBR ambiguity, converting the source to WAV. None of those changed it.

**Verify every render of a story past ~90-100s before sending it**, using
word-level re-transcription, not an amplitude/energy correlation script —
an RMS-envelope cross-correlation approach gives false drift readings near
a clip's low-energy tail (self-test it against identical audio before
trusting it, if you build one at all):
```bash
ffmpeg -y -i render.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le render_audio.wav
whisper-cli -m <model> -f render_audio.wav -oj -ojf -of render_transcript -sow
# compare segment timestamps/text against the source transcript's — a
# genuine desync shows as compressed real-word timing past a point, not
# just a numeric offset
```

**If desync is confirmed, do not just re-render — go straight to a manual
remux.** The video track is trustworthy; only the audio needs replacing:
```bash
ffmpeg -y -i render.mp4 -an -c:v copy video_only.mp4
ffmpeg -y -i video_only.mp4 -i "<clean source audio>" \
  -filter_complex "[1:a]afade=t=out:st=<fade-start>:d=<fade-duration>,apad[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest \
  render_resync.mp4
```
Re-verify with the same re-transcription check before sending. Treat this
remux as the standard step for any waveform-memento render whose story
runs past ~90s, not a one-off fallback — check first, remux if needed, on
every render.

## Delivery

Same as `video-memento`: compress to a WhatsApp-shareable file
(`-crf 26 -maxrate 620k`, lands ~13-14MB) and send that by default,
alongside the full-quality render. See `video-memento`'s SKILL.md
"Delivery" section for the exact ffmpeg command — identical here.
