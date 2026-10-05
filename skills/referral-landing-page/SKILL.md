---
name: referral-page
description: Builds or updates a family's forwardable /refer-[family] referral landing page for Me & My Old Man — scans their Drive session transcripts for approved-worthy stories and testimonials, drafts the consent HTML for family sign-off, and once approved, hands the copy deck + build brief to Lovable to publish. Trigger when Neil says "build the referral page for [family]", "refer page for [family]", "/refer-[family]", or after a client-handover call where a family consented to testimonials/stories being used. Distinct from client-handover, which runs the call itself and captures consent — this skill turns that consent into the actual page.
---

<!-- v1.0 — 2026-09-25: built from Neil's existing Marsh/Pinkham/Normans/Mcmullan referral pages, which were hand-built one at a time. This skill systemises that same process. -->

## What this builds

A single forwardable page per family, `meandmyoldman.co.uk/refer-[family]` (published via a dedicated, noindexed Lovable project, never the main site), built entirely from that family's own approved stories and testimonials. Never generic copy. The whole point is a friend or relative reading it thinks "these guys really got to know this family."

**This only runs for a family who consented on their handover call** (see `client-handover` skill). Never build or send anything using a story, quote, or clip nobody signed off — check the family's Consent & Referral Tracker doc before pulling anything.

## Canonical references — read these fresh every time, don't work from memory of them

- **Master build brief** (design system, section-by-section copy spec, per-family data model): Google Doc `1Sab8S9V-CCDoXlDRDZiLGDPW2gl_QFSZHvCQ3HcCzUU`, "refer-[family] — Build Brief & Copy Deck v2"
- **Hosting/indexing setup**: Google Doc/`.md` `1KSmMtwpVd7magVhBX28SSPhJ0YVc9DHs`, "HOSTING — refer pages in Lovable (keep them hidden)"
- **Canonical reference builds (match these exactly for layout/type/spacing)**: `refer-marsh.html` (Drive `1XNKwPBB5jOd6O3zcFb91FO18JIPKJDyz`, video hero) and `refer-pinkham.html` (Drive `16EuPeGCLYusAD2yK8byYbLWoxuuD57Y_`, audio waveform hero). If the brief and these files ever disagree, the files win.
- **All families' folders live under**: Drive folder `1pty6Q4_2yNWC57bttJkOR6u0vBelgiaa` ("05 Referral Landing Pages" — or wherever it currently sits, confirm with Neil if moved), one `[Family] HTML & LP` subfolder per family.

Read the brief and hosting doc fresh each run — they are the source of truth, not this file. If Neil has revised the offer terms (currently 5% off, book before end of year — check this against `knowledge/offer/pricing.md` too, since pricing terms can move independently), the brief's copy wins on wording but pricing.md wins on any number.

## Step 1: Find the family's transcripts

Family session material lives under the `Editing - [Family]` Drive tree (same parent editor-briefing works from). Search for:

- **Parent session folders** (`Ch[x]&[y] * S.[n]` under the parent's own chapter set) — this is where the **stories** live: the specific, concrete, textured details (a place, an object, a turn of phrase) that go in the hero headline detail and the "What it is" section's one-clause specific-detail line. Read the reformatted transcript `.md` file in each folder — these already carry speaker + timestamp per line, from the editor-briefing skill's Step 3a reformat.
- **Child briefing folders** — this is where **testimonials about the service itself** tend to surface, since the buying child is usually the one reflecting on why they did it.
- **Family Wrap Up folder/session** — this is where **most testimonials** live; the wrap-up call is explicitly a reflection on the whole experience. Also check the "[FAMILY NAME] Wrap Up Prep" doc under Drive folder `1bG1j428y4CVHr5X78NX6VIvOJmrnHVzF` if `wrapup-brief-check` has already logged Q1-Q5 homework responses for this family — those are pre-extracted testimonial material, often faster than re-scanning the raw transcript.

If a family's transcripts aren't reformatted yet (no `.md`/Doc in the session folder), that's a gap in the editor-briefing pipeline for that session — flag it to Neil rather than reading a raw, unstamped transcript by hand.

## Step 2: Pull candidate material, with timestamps

For each transcript, pull:
- 1-2 candidate **stories** per parent (concrete, specific, a real moment — not a summary) with the timestamp and speaker
- 2-5 candidate **testimonial quotes** per family member who consented, with timestamp and speaker, verbatim (strip filler words only, never reword)

Cross-check every name against the family's Consent & Referral Tracker doc (from `client-handover`). Anyone who didn't consent, or wasn't asked, gets nothing on the page — no quote, no clip, no name in a caption. This is not optional; see the Pinkham build, where a non-consenting parent was fully excluded.

## Step 3: Build the per-family data model and draft the page

Fill the data model from section 4 of the master build brief (family_name, possessive, month_year, project_shape, hero_headline_tail, hero_clip, hero_quote, what_it_is_detail, quotes[], why_now_quote, extra_clips[]).

Build the HTML page matching `refer-marsh.html` / `refer-pinkham.html` exactly for design (tokens, type, components) — video hero if the strongest consented clip is video, audio waveform hero if it's audio. Save it to the family's `[Family] HTML & LP` Drive subfolder as `refer-[family].html`, and the matching Lovable copy deck as `refer-[family]-lovable-copy-deck.md` (same folder), per the existing Marsh/Pinkham naming convention.

Any media clip referenced must be a Drive file shared "anyone with the link" — check/set this before the page can render.

## Step 4: Consent sign-off — mandatory gate before anything goes live

Send Neil (not the family directly — he sends it) the built `refer-[family].html` for the family's approval, with the private-preview bar left in place ("Private preview for the [Family] family · not published · not indexed"). **No page goes live without the family approving this exact draft.** One family previously asked theirs taken down because video use hadn't been discussed with them first — that is the failure mode this gate exists to prevent.

## Step 5: Hand to Lovable, once approved

Only after family approval: hand the copy deck + brief to the **MMOM Referral Pages** Lovable project (one shared project, one route per family — never a new project per family) via `send_message` / `create_project` on the Lovable connector. Confirm all four noindex steps are in place (they're project-wide, so only need checking on the very first family, per the hosting doc) and that the Drive audio/video files are still shared correctly. Test both the family's live route and the bare root (should 404/blank) before sending Neil the final link. Never publish the URL anywhere public — email/message directly to the family only.

## Step 6: Report

Tell Neil: which page was built, where the HTML/copy-deck landed in Drive, what needs his review before it can go to Lovable (the consent HTML), and any consent gaps found (someone whose material was strong but who wasn't asked, or said no).

## Feedback loop

If Neil corrects the copy, the design, the consent gate, or anything about how a page turned out, log it in `knowledge/lessons.md` the same turn and fold the fix back into this SKILL.md, per the CLAUDE.md skill feedback loop. Bump the version comment.
