---
name: audiobook-artwork
description: >
  End to end: import a family's chapter MP3s into Apple Music (desktop),
  set metadata and per-chapter artwork automatically, build a designed
  album cover, then deliver the finished files (no zip) and a generic
  client instructions doc into the family's own Stories Drive folder.
  Use whenever Neil says "build the audio documentary for [family]",
  "import [family]'s chapters", "add artwork to [family]'s audio
  documentary", "deliver [family]'s chapters", or references the "Adding
  Artwork to Final Audiobook Delivery" doc. Requires the chapter MP3s and
  matching photos to already be prepared and named per the ChNN
  convention below — this skill does not crop or select photos. Never
  call the output an "audiobook" in anything client-facing — Neil calls
  these "audio documentaries".
---
<!-- v1.0 — 2026-09-23: Built from "Adding Artwork to Final Audiobook Delivery" (Drive doc), replacing the manual Apple Music GUI workflow (Get Info -> Artwork tab, per track) with an AppleScript-driven import. -->
<!-- v1.1 — 2026-09-23: Added a designed cover step (make_cover.py). Apple Music shows Chapter 1's artwork as the album cover, so a bare uncropped chapter photo there looks unfinished — build a proper cover (title + subtitle in Marcellus over a scrim, "A Me & My Old Man production" credit bottom right in a backing plate) from a chosen chapter photo and set it as Ch1's artwork instead. Confirmed on the Griffiths build: title must sit tight to the top of the frame (clear of any head lower in the photo) and the credit needs a solid dark backing plate, not just a text shadow, to stand out on busy photo texture. Neil calls these "audio documentaries", never "audiobooks" — keep that word out of anything client-facing this skill produces or touches. -->
<!-- v1.2 — 2026-09-23: Fixed a real bug found on the Griffiths build — Music's AppleScript "set name of track" does not reliably flush the title into the file's ID3 tag before the command returns. Artist/album/genre/track-number/artwork all wrote correctly every time, but 9 of the 10 chapters had NO title tag at all on disk (would show blank on some phones/CarPlay). import_track.applescript now returns the track's on-disk path, and build_audiobook.py writes TIT2 directly with mutagen as a guaranteed backstop after every track. Needs `mutagen` (pip install mutagen — already present on this Mac). -->
<!-- v1.3 — 2026-09-23: Added the delivery step, approved on the Griffiths build. No export command needed and no zip: Music writes tags/artwork straight into the on-disk MP3 (get its path from each track's `location` property), so just copy those files directly into the family's own "04 Stories" Drive folder, replacing the untagged originals. Confirmed working through the Google Drive desktop mount at ~/Library/CloudStorage/GoogleDrive-.../Shared drives/Families/[Family]/04 Stories. Also added the generic client-facing instructions doc (references/family-instructions-template.html) — built as HTML per CLAUDE.md's Google Docs rule, uploaded via the first-party Drive connector's create_file (contentMimeType text/html) into the same Stories folder, sign-off included by default. Calls it an "audio documentary", never "audiobook" throughout. -->

# Audiobook Artwork — Automated Apple Music Import & Delivery

Automates most of the "Adding Artwork to Final Audiobook Delivery"
workflow: importing chapter MP3s into Apple Music, setting consistent
metadata, embedding one artwork photo per chapter, building a designed
album cover, copying the finished files into the family's Stories
folder, and adding a client instructions doc. Only steps 1-2 stay
manual — audio mastering and cropping photos roughly square in
PowerPoint — see the source doc for those.

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

5. **Build and set a designed cover for Chapter 1.** Apple Music displays
   whatever artwork is on the first track as the album cover, so a plain
   chapter photo there looks unfinished — replace it with a proper cover.

   a. Ask Neil which chapter's photo to use as the cover base (not
      necessarily Ch1's own photo — e.g. the Griffiths build used Ch9's).
   b. Build it:

      ```bash
      python3 skills/audiobook-artwork/scripts/make_cover.py \
        --image "/path/to/Chosen chapter photo.jpg" \
        --title "Client Name" \
        --subtitle "Album subtitle" \
        --out "/tmp/cover.jpg"
      ```

      Needs `~/Library/Fonts/Marcellus-Regular.ttf` — the script errors
      with a download command if it's missing (one-time, per Mac).
   c. **Always send the result to Neil and get a yes before setting it** —
      don't skip straight to applying it. He'll likely want to tweak
      title size/position or scrim strength; re-run with adjusted
      `--title`/`--subtitle` or edit the script's tuned constants
      (documented inline) rather than guessing at new numbers blind.
   d. Once approved, set it as Chapter 1's artwork:

      ```applescript
      tell application "Music"
        set t to first track of (every track of library playlist 1 whose name is "Ch1. ...")
        set artData to read (POSIX file "/tmp/cover.jpg") as picture
        set data of artwork 1 of t to artData
      end tell
      ```

6. Check the chapters in Music.app — play a few seconds of a couple of
   tracks, confirm artwork shows, titles look right.

7. **Deliver the files — no export, no zip.** Music writes the metadata
   and artwork directly into the on-disk MP3, so just copy those files
   straight into the family's own Stories folder.

   a. Get each track's real file path (its `location` property must be
      read inside the `tell application "Music"` block, then coerced to
      a POSIX path outside it — coercing inside the tell block fails,
      see `import_track.applescript` for the working pattern):

      ```applescript
      tell application "Music"
        set t to (every track of library playlist 1 whose album is "Album Title")
        repeat with x in t
          set trackLoc to location of x
          -- collect (name of x) and (POSIX path of trackLoc) per track
        end repeat
      end tell
      ```

   b. Find the family's Stories folder on the Drive-mounted path:
      `~/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/Shared drives/Families/[Family]/04 Stories`
   c. Copy each track's file into that folder, named `[Chapter title].mp3`
      (overwriting the untagged originals that are already there from
      the source audio). Loose files, never a zip — most phones won't
      auto-unzip or show a zip's contents as playable tracks, and Neil
      wants zero extra steps for the family.
   d. Once copied, spot-check at least one file's tags with mutagen
      before calling it done — Music's own UI and the AppleScript layer
      can both report success while the on-disk file is still wrong
      (see the v1.2 title-tag bug). Check title, artist, track number,
      and that an APIC (artwork) frame is actually present.

8. **Add the client instructions doc**, generic and reusable — don't
   write from scratch each time, copy the content from
   `references/family-instructions-template.html` (it already has
   Neil's sign-off) and upload it as a Google Doc directly into the same
   Stories folder using the first-party Drive connector:

   ```
   create_file(
     title: "How to Listen to Your Audio Documentary",
     parentId: "<Stories folder's Drive ID>",
     textContent: "<the template's HTML>",
     contentMimeType: "text/html"
   )
   ```

   Always verify in the browser afterward that it rendered as real Doc
   formatting (headings/bold/bullets), not literal `<h1>`/`<b>` text —
   `read_file_content` on a Drive doc can't be used to check this, it
   always returns a flattened plain-text view regardless of styling.

   Keep the doc itself generic (no family name in the body) — Neil's
   preference, confirmed on the Griffiths build. Never use the word
   "audiobook" anywhere in it; these are "audio documentaries".

9. Clean up: delete the imported tracks from Music.app's library once
   delivery is confirmed — this skill only ever used it as a tagging
   tool, nothing should stay published there long-term.

## Notes

- Apostrophes: Music.app can mangle curly/straight apostrophes on import
  in the same way the source doc warns about for manual entry. Keep
  apostrophes out of chapter filenames where possible.
- If a track's artwork or metadata comes out wrong, fix it by hand in
  Get Info in Music.app rather than re-running the whole import — the
  script doesn't currently handle re-runs/updates, only fresh imports.
