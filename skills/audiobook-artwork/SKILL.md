---
name: audiobook-artwork
description: >
  Import a family's chapter MP3s into Apple Music (desktop) and set
  metadata and per-chapter artwork automatically, instead of doing it by
  hand track-by-track. Use whenever Neil says "build the audiobook for
  [family]", "import [family]'s chapters", "add artwork to [family]'s
  audiobook", or references the "Adding Artwork to Final Audiobook
  Delivery" doc. Requires the chapter MP3s and matching photos to already
  be prepared and named per the ChNN convention below — this skill does
  not crop or select photos.
---
<!-- v1.0 — 2026-09-23: Built from "Adding Artwork to Final Audiobook Delivery" (Drive doc), replacing the manual Apple Music GUI workflow (Get Info -> Artwork tab, per track) with an AppleScript-driven import. -->

# Audiobook Artwork — Automated Apple Music Import

Automates steps 3-5 of the "Adding Artwork to Final Audiobook Delivery"
workflow: importing chapter MP3s into Apple Music, setting consistent
metadata, and embedding one artwork photo per chapter. Steps 1-2 (audio
mastering, photo cropping to square) and steps 6 onward (export, zip,
upload, testing) stay manual — see the source doc for those.

## Before you run this

Neil prepares the folder himself. It needs:

1. **Chapter MP3s**, one per chapter, named `ChNN [chapter name].mp3` —
   e.g. `Ch01 Steph & Mum.mp3`, `Ch02 The Move to Leeds.mp3`. The number
   drives track order and total track count.
2. **A matching image for every MP3**, same base name, same folder —
   `Ch01 Steph & Mum.jpg` (`.jpg`, `.jpeg` or `.png`, case-insensitive).
   Photos should already be cropped roughly square with faces centred —
   exact precision doesn't matter, "can you see the faces" is the bar.
3. **The client's name** (used as the Artist tag) and ideally the album
   title (defaults to `"[Client]'s Life Story"` if not given).

If any MP3 has no matching image, or a file doesn't start with `ChNN`,
the script reports it and skips that file rather than guessing.

## One-time setup (Neil only, first use)

Music.app automation needs macOS Automation permission granted to
whatever runs the script (Terminal, or Claude Code's shell). The first
run will trigger a system permission dialog — approve it. If it doesn't
prompt and instead silently fails, check **System Settings > Privacy &
Security > Automation** and enable access to Music for the relevant app.

## Running it

1. Confirm the folder path, client name, and (optionally) album title
   and year with Neil.
2. Dry run first, always — this only reports the pairing, it does not
   touch Music.app:

   ```bash
   python3 skills/audiobook-artwork/scripts/build_audiobook.py \
     --folder "/path/to/Family Folder/Audiobook" \
     --client "Judy Dickson" \
     --dry-run
   ```

3. Check the chapter <-> image pairing printed out. If anything looks
   wrong (missing image, wrong chapter matched), stop and get Neil to
   fix the folder rather than pushing on.
4. Run for real (same command, without `--dry-run`):

   ```bash
   python3 skills/audiobook-artwork/scripts/build_audiobook.py \
     --folder "/path/to/Family Folder/Audiobook" \
     --client "Judy Dickson" \
     --album "Judy Dickson's Life Story"
   ```

   This imports each MP3 into Music.app and sets, per track: title
   (from the filename), artist, album, genre (`Audiobook`), year, track
   number and track count, then embeds the matching photo as artwork.

5. Hand back to the source doc from step "5. Check your work" onward —
   verify in Music.app, then export and zip for delivery as normal.

## Notes

- This only ever adds tracks to the local Apple Music library — nothing
  is published or shared. Delete the imported tracks from Music.app
  after export, same as the manual workflow already does.
- Apostrophes: Music.app can mangle curly/straight apostrophes on import
  in the same way the source doc warns about for manual entry. Keep
  apostrophes out of chapter filenames where possible.
- If a track's artwork or metadata comes out wrong, fix it by hand in
  Get Info in Music.app rather than re-running the whole import — the
  script doesn't currently handle re-runs/updates, only fresh imports.
