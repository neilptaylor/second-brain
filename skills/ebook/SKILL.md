---
name: ebook
description: Builds the final "That's A Wrap" e-book (also called the ebook) for a Me & My Old Man family, the final handover document that delivers their chapters, mementos, download instructions and the referral ask. Landscape 16:9 PDF in the website's design (Lora, DM Sans, cream, terracotta), built as HTML and printed with headless Chrome so links stay live. Use when Neil says "ebook for [family]", "wrap e-book for [family]", "that's a wrap for [family]", "final handover doc", "handover e-book", or asks to replace the old Canva wrap deck. Distinct from client-handover (testimonials, refer page, consent), which runs alongside it.
---
<!-- v1.0 — 2026-09-25: created from the Griffiths build, replacing the Canva version (Marshes That's A Wrap.pdf, peach).
     v1.1 — 2026-09-25: locked as the reference after Neil's first-pass corrections on Griffiths. Added the memento title-card gallery slide, the Snapshot pricing rule, and the addressee rule.
     v2.0 — 2026-10-15: renamed from wrap-ebook to ebook. Added the Beards (5 Oct) refinements and the legacy folder layout used for the Normans. -->

# That's A Wrap e-book

The last thing a family receives. It hands over everything, tells them how to keep it, and asks them to pass the experience on.

Reference build: `assets/template.html` (Griffiths, 25 Sep 2026). Contact sheet: `assets/reference-griffiths-contact-sheet.png`. The old Canva version for comparison: `Shared drives/Families/Marshes/Marshes  That's A Wrap!.pdf`.

## Design (fixed, do not change the CSS)

Tokens are lifted from meandmyoldman.co.uk: cream `#f9f5f0`, tint `#f3e9e1`, ink `#1c1612`, muted `#6e635b`, terracotta `#b8624a` (not the old peach `#d4967e`). Headlines Lora 400 with one terracotta italic phrase, body DM Sans. Page 1600 x 900. Terracotta panels only on the cover, the thank you and the closing quote.

## Page order

1. Cover: terracotta panel, family name, "Vaughan's life story, in his own voice" style line, date. Group photo right.
2. Letter: "Dear [names]," short, names two or three real chapter-title moments. Photo right.
3. Chapters: numbered list, exact titles from the `04 Stories` filenames, link to that folder.
4. Artwork note (only if artwork was added after first listen, via album-artwork): "Every chapter now has its own cover", please download again. A background photo on this slide needs `background-size:contain;background-repeat:no-repeat` plus a fallback `background-color` (a fill colour from the palette, e.g. `#e8e1d8`) — `contain` alone tiles the image to fill the panel, which is a real bug, not a style choice. Never crop a person out of frame with `cover`; check every photo panel against the source image before calling a page done.
5. Mementos: exact titles from `05 Mementos` filenames, link to that folder. State the true count and how many are ready (e.g. "six of nine ready") rather than only listing what exists today, if Neil says more are still in progress.
6. Mementos gallery (only if there are Mementos videos): one clickable title-card per ready video, screengrab plus caption, each hyperlinked straight to the file so tapping the cover plays it. Grab the screengrabs with `scripts/mementos_titlecards.sh "<Mementos folder>" scratch/wrap-<family>/mementos` (needs `ffmpeg`) and get each file's Drive `viewUrl` via the Drive connector's `search_files` on the Mementos folder ID — link to `.../view`, not a raw download link.
7. Downloading: three steps (download, iPhone, Android/PC). Wording follows the Drive doc "How to Listen to Your Audio Documentary".
8. Mac to iPhone sync.
9. Sharing the folder, and the Spotify note.
10. Saving: everywhere, and in your wills.
11. Thank you. Signed Neil. Name every real name it's for — children and grandchildren by name, not just "whoever comes next" — and confirm the exact list and spelling with Neil rather than guessing from Drive filenames.
12. Pass it on: referral. Link meandmyoldman.co.uk/refer, the friend's 5% before end of 2026 and free call, "mention the [family]", and the Life Story Snapshot for the family, framed as a follow-up chapter or a start for one of the children. Read the live /refer page first, it owns the offer terms. **Snapshot length and price always come from `knowledge/offer/pricing.md`, never the live site** — confirmed 25 Sep 2026 the site (`/refer`) still shows the old "one hour, £400 free" copy while pricing.md has the current terms (1.5-hour session, £300, £750 standalone value). If the two disagree, flag it to Neil rather than silently picking one; a Lovable brief to fix the site is a separate deliverable (see below), not something this skill blocks on.
13. Closing quote on terracotta. Only include a title-page-style quote/name card (à la the Marsh build's "I'll think about it") if there's a real one-liner for this specific family — never invent or reuse one from another family.

## Addressee

Confirm the exact "Dear ..." list and the closing-page name list with Neil before drafting — don't infer who's included (e.g. a parent's spouse) from the folder or transcripts. Once confirmed, the same list should appear consistently on the letter page and the thank-you page.

## When the offer page is out of date

If building this surfaces a stale `/refer` page (wrong Snapshot price/length, wrong video-referral terms), write a short Lovable copy brief alongside the e-book: current live copy vs. the correct figures from `knowledge/offer/pricing.md`, with the exact section to change. Don't wait for this to be asked — flag it the same turn.

## Steps

1. Read `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` in full.
2. Ask Neil for anything not on disk: who to address (which parents and children), whether artwork was added, how many more mementos are coming.
3. List `Shared drives/Families/[Family]/04 Stories`, `05 Mementos`, `03 Photos/Photos selected`. Get the two folder IDs with the Drive connector's `search_files`.
4. Prep photos (fixes phone rotation):
   `python3 skills/ebook/scripts/prep_images.py "<family>/03 Photos/Photos selected" scratch/wrap-<family>/img`
5. Copy `assets/template.html` to `scratch/wrap-<family>/<family>-wrap.html`. Swap names, titles, links, photos (`img/chN.jpg`), date. Pick portrait photos for the 40% columns, group shots for the cover. Never invent a story detail; letter moments come from real chapter titles.
6. Render: `skills/ebook/scripts/render.sh scratch/wrap-<family>/<family>-wrap.html "scratch/wrap-<family>/<Family> That's A Wrap.pdf"`. Check every page as images (`pdftoppm -r 40`), watch for text overflow.
7. Copy the PDF to `Shared drives/Families/[Family]/`. Tell Neil the path and anything to check. Never send it to the family.


## Beards refinements (5 Oct 2026, on top of Griffiths)

- Letter names real chapter titles as a run ("From Barton Cottage and a trusty tricycle to Burton beer and the Stones...") and ends "I hope these last few months have been as reflective and as joyful for you as they have been for me." Adapt, never copy.
- Chapters page states the count ("in nine chapters") and links the Stories folder.
- Artwork slide wording: "Every chapter now has its own cover", then "if you downloaded them before, please download them again."
- Mementos: list page, then a tap-to-play gallery page. Count stated truthfully.
- Closing quote may be a real published quote with attribution (Beards used Frankl). Never a made-up family line.
- Refer link is per family: `meandmyoldman.co.uk/refer-[family]`. Confirm the page exists first, build it with client-handover if not.
- Every hyperlink in the PDF must be listed back to Neil at the end (folder links, each memento, refer page) so he can spot-check them.

## Legacy folder layout (the Normans, recorded 2025)

Early families do not follow `04 Stories` / `05 Mementos` / `03 Photos`. Always list the family folder first and map what is there. Normans:

| Job | Normans folder |
|---|---|
| Chapters | `02 Stories` (Ch1 to Ch12, Ch12 is Family Wrap Up & Reflections) |
| Mementos | `03 Mementos` |
| Photos | `01 Photos/Selected` only. Ignore the loose scans in `01 Photos`. |

Rules for legacy layouts:
- Use the folder the family actually has for the links. Say in the summary which folder maps to which page.
- Chapter titles come from the filenames, minus `ChN.` and `.mp3`. Some are very long (Normans' run to 10+ items). Show them in full on the chapters page, smaller type if needed, never trim a title.
- A Mementos folder may hold non-memento files (e.g. `Normans Testimonial.mp4`, `National Service Testimonial.mp3`, a mp3 and mp4 of the same story). Do not list testimonials as mementos. Where a story exists as both audio and video, ask Neil which to show before counting.
- Old chapters have no embedded artwork unless album-artwork was run. Ask before including the artwork slide.
- Photos in these families are scans of mixed quality. Run `prep_images.py` and check every panel at full size; use portraits only where the scan is sharp.
