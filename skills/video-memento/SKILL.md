---
name: video-memento
description: >
  Builds a Me & My Old Man "memento" video: a title card, a Ken Burns
  slideshow of family photos, and an end card, all set to one narration or
  excerpt audio file. Uses HyperFrames. Trigger when Neil says "make a
  memento for [family]", "video memento", "turn this audio into a memento",
  or gives an audio excerpt plus family photos and asks for a video/slideshow
  version of it. Distinct from talking-head-recut (existing footage with
  overlays) and embedded-captions (existing footage with captions) — a
  memento has no source footage, only stills and audio.
---
<!-- v1.0 — 2026-09-25: Created from the first build, Vaughan Griffiths "The Privilege of Parenting", styled directly off the Saturday Buns & Routines reference card (Normans Mementos). -->
<!-- v1.1 — 2026-09-25: Corrections from the Griffiths build review. (1) "Start with 1, 2, 3" meant those photos open the slideshow, not that the slideshow is only those photos — use every photo in the named folder unless Neil caps the count. (2) Deliver a WhatsApp-shareable file alongside (or instead of) the full-quality render; the raw HyperFrames render is 100-200MB+ and unshareable. (3) Title-card meta line must give the real recording month from the session, and must not repeat "Me & My Old Man" a second time (the kicker already says it) — drop any "A Me & My Old Man Recording" style line entirely. -->
<!-- v1.2 — 2026-09-25: Second correction pass, same Griffiths build. (1) Fixed generic aspect-ratio "buckets" (landscape/portrait/wide boxes) crop real content — faces, chins, heads lost at the frame edge on several photos. Size each photo's frame to ITS OWN aspect ratio instead; see "Photo frame sizing" below. (2) A photo can be rotated even when the user didn't flag it — always eyeball every photo before locking the sequence, not just the ones named as sideways. (3) When Neil says "remove photo X, end on the previous one instead", the fix is to drop it from the source list and let the timing regenerate (previous photo's scene now runs to the end) — don't just delete the scene and leave a gap or truncate the audio. -->
<!-- Also, process note: compress to the WhatsApp-shareable file and confirm its size BEFORE deleting the raw render — if the compressed pass needs a re-run (still over target size), you need the raw source again and re-rendering costs 1-2 minutes. -->
<!-- v1.3 — 2026-09-25: Third pass, same Griffiths build. v1.2's fix (size each frame to its own aspect ratio) was necessary but not sufficient — three photos still cropped heads because their EXIF Orientation tag didn't match their stored pixel dimensions (sips reports raw dimensions, ignoring the tag; the browser HyperFrames renders in honours it). Added a mandatory `ImageOps.exif_transpose` normalization pass, run before any dimension is read — see "Sourcing assets" below. Also tightened the WhatsApp compression target to CRF 26 / maxrate 620k, landing ~13-14MB with clear margin under the ~16MB ceiling rather than cutting it close at 16MB. -->
<!-- v1.4 — 2026-09-25: Repeat failure on a SECOND, separate memento build (Vaughan Griffiths "A Date, No Cake & A Proposal") — the v1.3 EXIF fix was documented but sat inside "Sourcing assets" as one bullet among several, and got skipped entirely: dimensions were read with bare `sips -g pixelWidth -g pixelHeight`, and 4 of 49 photos (all phone shots with EXIF orientation 6) got landscape-shaped boxes for portrait images, cropping heads/torsos at the frame edge in the delivered video. Moved the EXIF-normalization pass out of "Sourcing assets" and into "Before building" as a numbered, mandatory step — a bullet buried in a longer list is too easy to skim past under momentum; a numbered pre-flight step is not. -->



# Video Memento

A memento turns one audio excerpt (a chapter clip, a wrap-up soundbite, a
standalone story) into a shareable video: title card → Ken Burns slideshow of
real family photos → end card. No talking-head footage, no captions synced to
speech — the audio plays under stills.

## Trigger

Neil hands over: an audio file (mp3/wav), a folder or short list of photos,
and a title. He may also point to a past memento as the style reference. Ask
for whichever of these is missing before building — never invent a title,
caption, or date.

**"Start with 1, 2, 3" means opening order, not the photo list.** When Neil
names specific photos and then says "use the others" (or points at a folder
and names only the first few), the slideshow uses every photo in that folder
— the named ones just go first, in the order given. List the folder and
confirm the total count before building rather than assuming the named
photos are the whole set. If there's no signal at all for ordering the rest,
folder/filename order is a reasonable default; say so rather than silently
picking one.

## Before building

1. **Read the family's facts.** Never caption a photo with an invented year,
   age, or description. If Neil hasn't supplied captions, ship the slideshow
   without them rather than guessing.
2. **Find the style reference.** MMOM mementos live in Drive under
   `Shared drives/Editing/EDITOR Neil/<Family> Mementos/`. A finished one
   (`FINAL/*.mp4`) is the fastest way to pull exact title-card and end-card
   styling — extract frames with ffmpeg rather than guessing at colours/fonts:
   ```bash
   ffmpeg -y -ss 2 -i "<reference>.mp4" -frames:v 1 /tmp/title.png
   ffmpeg -y -sseof -3 -i "<reference>.mp4" -frames:v 1 /tmp/end.png
   ```
   Read the frames back before writing any CSS. The house style seen so far:
   cream background (`#f6efe1`), charcoal text (`#2d2926`), rust accent
   (`#bf5700`), serif display face for the title/end lines (Playfair Display),
   tracked-uppercase sans kicker/meta (Inter), photos in a white
   polaroid-style frame with a soft drop shadow.
3. **Confirm aspect and run-shape** with the user (vertical 9:16 for
   social/mobile, 16:9 landscape for the audio-documentary delivery format;
   one-shot build vs. storyboard first) — this is a `/general-video` route
   inside HyperFrames; follow its intent layer rather than skipping straight
   to code on a fresh project.
4. **Normalize EXIF orientation on every photo, before reading a single
   dimension.** Non-negotiable, not a "sourcing" nicety — do this as its own
   pass immediately after copying photos into `assets/photos/`, before any
   frame-sizing code runs. `sips -g pixelWidth -g pixelHeight` (and several
   other tools) report the *raw* sensor dimensions and ignore the EXIF
   `Orientation` tag; the browser HyperFrames renders in honours that tag.
   Reading a landscape-tagged phone photo as landscape sizes its frame for
   the wrong aspect ratio, and `object-fit: cover` then crops the actual
   (correctly-rotated) portrait image hard at top and bottom — heads,
   torsos, whatever was near the edge. This has now caused cropped photos
   in the delivered video on two separate builds (3 photos, then 4 photos)
   because the fix lived as a bullet inside "Sourcing assets" and got
   skimmed past. Run this before every build, no exceptions, on the whole
   folder in one pass:
   ```python
   from PIL import Image, ImageOps
   import glob
   for path in glob.glob("assets/photos/*"):
       img = Image.open(path)
       if img.getexif().get(274, 1) != 1:      # 274 = Orientation tag
           ImageOps.exif_transpose(img).save(path, quality=95)
   ```
   Only read pixel dimensions for frame-sizing *after* this pass has run —
   a photo that was 4000x3000 with orientation 6 becomes a genuinely
   portrait 3000x4000 file once corrected, and the frame sizing must use
   that corrected value, not the raw one.

## Sourcing assets

- Photos are usually only linked via a Drive folder URL. Check first whether
  the folder is mirrored locally under
  `~/Library/CloudStorage/GoogleDrive-<account>/`
  — `find … -iname "*<folder name>*"` — before falling back to the Drive
  connector.
- Rotate with `sips -r -90` (left) / `sips -r 90` (right) for any photo the
  user flags as sideways *after* the EXIF-normalization pass above has run
  and the photo is still genuinely sideways (not an EXIF tag mismatch);
  always view the result afterwards to confirm the subject is upright the
  right way round, not just landscape.
- **View every photo before locking the sequence, not just the ones the user
  flags.** A Griffiths build shipped with one photo still sideways because
  only the two the user named up front got checked. Read each photo file
  back (or at minimum skim thumbnails) as part of assembly — catching a
  rotated or mis-cropped photo before render is a one-line fix; catching it
  after is a full re-render.
- Fonts: download the exact static weights needed from Google Fonts
  (`fonts.googleapis.com/css2?family=…`) straight to `assets/fonts/*.woff2`
  and self-host via `@font-face` — do not link a live Google Fonts stylesheet
  from the composition (render must stay deterministic/offline-safe).

## Build pattern (HyperFrames)

Scaffold with `npx hyperframes init`, then a single-file `index.html`
composition (no sub-compositions needed for 5 scenes; lint's
`nested_structure_needs_subcomposition` warning is fine to leave for a
one-off memento):

- **Timeline:** title card (~6s) → one scene per photo, audio duration minus
  title split evenly across photos → end card (~6s, starts as the audio
  finishes or slightly before).
- **Audio:** one `<audio>` element, `data-start="0"`, duration = exact file
  length (`ffprobe -show_entries format=duration`), `data-fade-out` of ~1s.
- **Photo frame sizing — fit each photo's OWN aspect ratio, never a generic
  bucket.** The first Griffiths build sorted photos into fixed
  landscape/portrait/wide boxes (e.g. a 4:3 box for every landscape photo)
  and let `object-fit: cover` crop whatever didn't match — this silently ate
  chins, foreheads, and half a face on several real photos. Instead, read
  each photo's actual pixel dimensions and size its `.crop` box to that exact
  ratio, capped to a max width/height that fits the stage
  (e.g. `MAX_W=940, MAX_H=1480` in a 1080x1920 comp):
  ```python
  def fit(w, h, MAX_W=940, MAX_H=1480):
      r = w / h
      box_w = MAX_W
      box_h = box_w / r
      if box_h > MAX_H:
          box_h = MAX_H
          box_w = box_h * r
      return round(box_w), round(box_h)
  ```
  With the box ratio equal to the image ratio, `object-fit: cover` crops
  nothing at rest — the whole photo is visible. This means every scene has
  a different frame size (that's fine and expected; it's what "not cropped"
  looks like against a fixed-size cream stage).
- **Ken Burns stays gentle for exactly this reason.** Once the frame shows
  the whole photo, any zoom crops real content, so keep it small: `scale`
  1.0→~1.05 (not 1.14) with `xPercent`/`yPercent` drift under ±1, `ease:
  "none"`, duration = the scene's full on-screen time. Vary start/end scale
  and drift direction per photo so consecutive scenes don't feel identical,
  but never start a scene already zoomed in past ~1.05 — that's the amount
  that clipped faces last time. Mark the `.crop` container
  `data-layout-allow-overflow` since the zoom is meant to overflow it by that
  small margin.
- **Photo frame:** white padded box (`background:#fff; padding:~22px`),
  soft multi-layer `box-shadow`, on the cream stage background — this is what
  reads as "physical photo" rather than a flat image.
- **Title/end card copy:** kicker "ME & MY OLD MAN" → rust rule →
  serif headline → sans subtitle/byline → one meta line giving the real
  recording month and year Neil supplied (e.g. "Recorded August 2026"). Never
  add a second brand mention such as "A Me & My Old Man Recording" on top of
  the kicker — it's already said once, repeating it reads as filler. End card
  is fixed brand copy ("Stories That Matter. With People You Love." +
  `meandmyoldman.co.uk`) unless Neil says otherwise.
- **Photo count scales the per-scene duration**, not the format: with N
  photos and a title/end card of a few seconds each, give each photo
  `(audio_duration - title - end) / N` seconds. Above ~15-20 photos this
  runs a few seconds per photo — expected for a fuller family archive, not a
  bug; just shorten the per-scene cross-fade (`min(0.45, dur * 0.15)`) so
  quick scenes don't fade before they've held.

## Checks before render

```bash
npm run check     # lint + runtime + layout + motion + contrast
npx hyperframes preview --background   # then review key frames in the Browser pane
npx hyperframes preview --stop
npm run render
```

Scrub the title card, at least one photo scene mid-zoom, and the end card in
Studio before rendering — confirm text isn't clipped and the Ken Burns zoom
doesn't reveal the crop edge (the layout check's `container_overflow` info
lines are expected here; only worry if the *image* runs out of coverage,
which shows as a blank/transparent sliver).

## Delivery

Rendered files land in `renders/` inside the project folder under
`videos/<slug>/`. The raw HyperFrames render is large (100-200MB+ for a
2-3 minute vertical video with many scenes) — too big for WhatsApp and over
the 30 MB remote-file-share limit. **Always produce a compressed, WhatsApp-
shareable copy as a standard step, not just on request:**

```bash
ffmpeg -y -i "<raw render>.mp4" -vf "scale=1080:1920:flags=lanczos" \
  -c:v libx264 -preset slow -crf 26 -maxrate 620k -bufsize 1240k \
  -c:a aac -b:a 112k \
  "<slug>_whatsapp.mp4"
```

This keeps full 1080x1920 resolution and lands around 13-14MB for a typical
2-3 minute memento — clear margin under WhatsApp's ~16MB video-message
ceiling, not right up against it (an earlier pass at `-crf 24 -maxrate 900k`
landed at 16.0MB, borderline enough to risk WhatsApp's own re-compression
kicking in). Title cards and Ken-Burns-on-stills are low-motion, so this
compresses hard without visible banding on text. Check the output size and
tighten further (`-maxrate 500k`, or scale to `720:1280`) if a particular
memento still lands over ~15MB — more scenes/cuts per minute means less
static-frame reuse and a bigger file at the same settings. Verify a frame
from the compressed file (`ffmpeg -ss … -frames:v 1`) before sending —
confirm title-card text is still sharp. Delete the raw render's two-pass log
files (`ffmpeg2pass-0.log*`) if a two-pass attempt was made; a single
CRF+maxrate pass is simpler and has proven reliable here (two-pass failed
with a libx264 encoder error on this machine, root cause not chased down —
CRF is the working path, use it first).

Send the compressed file to Neil by default. Keep the raw high-quality
render in `renders/` too in case he wants to re-derive a different cut, but
don't lead with it or describe it as desktop-app-only without also handing
over the shareable version. **Don't delete the raw render until the
compressed file's size is confirmed acceptable** — a compression pass
sometimes needs a second attempt at a lower `maxrate`, and that only needs
the raw source, not a full 1-2 minute re-render, if it's still on disk.
