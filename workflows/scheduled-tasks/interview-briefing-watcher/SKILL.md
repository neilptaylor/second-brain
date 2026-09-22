---
name: interview-briefing-watcher
description: Mon/Thu 7:30am: scans the Editor Pipeline Airtable for parent recording sessions due in the next 6 days, and builds the Interview Briefing for any that doesn't have one yet — from the children's transcripts + homework (S1) or the previous session's transcript (S2+). Catches what the editor-briefing skill's Step 5 misses, because that only fires as a side effect of an editor handoff.
---

You are running an automated pre-session check for Me & My Old Man (MMOM). Your job: make sure Neil never walks into a parent recording session without an Interview Briefing waiting for him.

## Why this task exists

The `editor-briefing` skill already knows how to build these (its Step 5). But that step only ever fires as a *side effect* of running an editor handoff for a session that has already been recorded. Nothing looks ahead at the calendar. In September 2026 that gap meant Phil Taylor's Session 1 briefing didn't exist until the morning of the session — his children were recorded back in July, before that Step 5 logic existed, and he'd never had an editor briefing run because he'd never been recorded.

This task closes that loop by working forwards from upcoming session dates instead of backwards from completed ones.

**Be quiet when there's nothing to do.** Most runs should end with no document created and no email drafted. Only act when a briefing is genuinely missing.

## Connectors

Airtable (`c689634b-…`), Google Drive (`04e9ba0e-…`), Gmail (`ffce937d-…`). If those IDs don't match this session, find them by name.

---

## Step 1: Find upcoming parent sessions

Airtable base **apprk3RUXdvZNJ8TF**, table **Editor Pipeline** (`tblWkRNY5rcvthBMs`).

Fields:
- `Family Name` (fldfvHJsC7EILNfpr) — surname, e.g. "Taylor"
- `First Name` (fldvMQG55QBjefTeB) — the interviewee, e.g. "Phil", "Maggie", "Carl & Dad", "Family"
- `Session Type` (fldO9gjgDbql5WTxC) — 1hr Child · 1hr Child Briefing · 2hr Parent S1 · 2hr Parents S2 · 2hr Parents S3 · 2hr Parents S4 · 2hr Parent Life Story Recording · Wrap Up · Other
- `Status` (fldvpwgWDhllOGcFI) — TBC · To Schedule · To Record · To Brief · To Edit · To Feedback · COMPLETE
- `Session Date` (fld45cYDJmVOHqsUN) — dateTime
- `Notes` (fldXvqZ69gzIsTUok)

Pull every row where **Session Date falls between today and today + 6 days** and **Session Type is a parent session** (any "2hr Parent…" value, including the unnumbered "2hr Parent Life Story Recording").

Skip rows whose Status is already past recording (`To Brief`, `To Edit`, `To Feedback`, `COMPLETE`) — those have happened. Act on `To Record`, `To Schedule`, and `TBC`.

If the row's Session Type is the unnumbered "2hr Parent Life Story Recording", work out which session number it is by sorting that person's parent rows by Session Date.

If there are no matching rows, stop here. Do nothing, send nothing.

## Step 2: Check whether a briefing already exists

For each candidate, search Drive for `title contains 'Interview Briefing' and title contains '[parent first name]'`.

Naming convention (matching the `editor-briefing` skill): `YYYYMMDD Interview Briefing [Parent Full Name]` for Session 1, and `YYYYMMDD Interview Briefing [Parent Full Name] S[n]` for Session 2 onwards. So an untitled-suffix doc covers S1.

**If a briefing for that person and session number already exists, skip it — never rebuild or overwrite one.** Docs may also have been created by hand or by the skill under a slightly different name, so read the titles properly rather than pattern-matching blindly. If you find something ambiguous, leave it alone and mention it in the Step 6 alert rather than creating a duplicate.

## Step 3: Work out which case applies

**Case A — the parent's Session 1.** Build from all of the children's transcripts and homework.

First confirm every child in the family has actually been recorded: pull all rows for that Family Name with Session Type `1hr Child` or `1hr Child Briefing` and check each is at `To Brief` or beyond. Cross-check against Drive — each child should have a session folder with a transcript in it. If Airtable and Drive disagree, or a child clearly hasn't been recorded, **do not build the briefing** — flag the mismatch in Step 6 instead so Neil can decide.

Note that children usually record twice, once about each parent. Only the sessions about *this* parent matter.

**Case B — Session 2, 3 or 4.** Build from the transcript of the parent's previous session, plus the briefing that was used going into it (read that first so you're not repeating ground already covered), plus anything the children flagged that still hasn't been reached.

## Step 4: Gather the sources

**Transcripts** live in the session folders under the Editing shared drive. Structure is `[Family] - [Editor]` (e.g. "Taylors - Jodie", `1WeH_F2PtCNq5ZnzGXIuAXNdbbxzz9Ypi`) → a folder per parent (e.g. "Phil Taylor") → chapter folders (e.g. "Ch3 & 4 Phil Taylor", "Ch2 Jodie & The Old Man"). Naming is inconsistent between families — search by family and person name rather than assuming a fixed path.

Two file-handling traps, both of which will otherwise blow your context:
- **.vtt transcripts** aren't readable via `read_file_content`. Use `download_file_content`, then base64-decode and collapse the cue blocks into speaker lines with a short Python script before reading.
- Large reads get persisted to a file rather than returned inline. When that happens, extract what you need with `jq` or Python rather than trying to read the whole payload.

**Children's homework** is in the **Child Primer_Homework (Responses)** sheet, `1WSC3YBarKi3_CrHQW3o07i-9FBjCr6-zVlAoaed_wWY`. The sheet is large — read it, then grep the persisted file for the family surname rather than pulling it all into context. The name column identifies which parent the response is about, in free text, e.g. "jodie taylor - Dad" or "Carl Taylor-Son      Phil Taylor". Match on that, not on position.

Homework answers are often written then struck through — struck-through text still counts as what the child said, but an un-struck line is usually the one they landed on. Worth noting the difference.

## Step 5: Build the doc

Load the `editor-briefing` skill and follow its Step 5 for the matching case — that's the source of truth for structure, and keeping to it means the two systems stay in step. If the skill can't be loaded, fall back to the shape of the existing examples.

Reference docs, in order of usefulness:
- **Phil Taylor S1** (Case A, the fullest example): `10S-bR6PTNBB_HHsRy1ACpCXD2N6UVsz28Rq2CSmtVt0`
- **Maggie Taylor S2** (Case A material, children's input): `1_HxVm4FEGMO1W-h60PBO1jXV_8LvDqbBCSP8171FpU4`
- **Maggie Taylor S3** (Case B, follow-on from a parent session): `1iDXrvGS_gM6tUrzGtBT6F-FuZ0eROmWeoBcDzK6tnNo`

What makes these work, and what to preserve:
- **Sensitivities go first**, before anything else, if the children flagged any. What to avoid, what's safe, and why.
- **Life stages in order of the parent's life**, not the order the children mentioned them. Flag clearly that it's second-hand and may be wrong — it's a prompt list, not a fact sheet.
- **Tag every want-to-know with the child who said it.**
- **Quote questions verbatim.** Don't paraphrase them into neatness; the children's own wording is the point.
- **Name the gaps.** The most useful line in a briefing is usually "neither child knows X."
- Where two children's accounts conflict, say so and mark it as something to pin down.
- Finish with a suggested session arc and a few craft notes.

Write it as HTML (`<h1>` for the title, `<h3>` for section headings, real `<a href>` for any links) and upload via the Drive file-creation tool with `contentMimeType: "text/html"` and `mimeType: "application/vnd.google-apps.document"`. That converts to a native Google Doc with working Title/Heading 3 styles. Plain text does not — it produces dead text and no styling.

**Do not use `<hr>` tags.** They don't convert, and leak into the following heading as a literal "-----".

Read the doc back afterwards to confirm the styles landed (you should see `# **title**` and `### **heading**` in the result).

Save it into the parent's folder for **that** session. If the folder doesn't exist yet, check carefully for one under a name you haven't matched (e.g. "Ch7 & 8 Phil Taylor" may be the S3 folder with no explicit "S.3" in the name) before creating a new one.

## Step 6: Alert Neil

Create a **Gmail draft** to neil@meandmyoldman.co.uk. Never send.

Subject: `[Family] | Interview Briefing ready for [Parent] S[n]`

Body, short — four lines:
```
[Parent]'s Session [n] is [day] [date] at [time].
Briefing built from [what you used].
The one thing to know going in: [single sharpest point from the doc].
→ [link to the doc]
```

Build the link as a real `<a href="…">` in `htmlBody`. Never paste a bare URL into the visible text — Gmail turns it into a long wrapped `google.com/url?q=` redirect, which is exactly the look Neil doesn't want.

If you found a mismatch in Step 3 rather than building anything, draft that instead: which family, what disagrees, and what you'd need in order to proceed.

## Guard rails

- **Never send email.** Drafts only.
- **Never overwrite or rebuild an existing briefing.** If in doubt, skip and flag.
- **Don't change Airtable.** This task is read-only there — status changes belong to the editor-briefing skill after a session is recorded.
- **Don't RSVP to or modify any calendar event.**
- If a family's transcripts are missing entirely, say so in the alert rather than building a thin briefing from homework alone.
- Nothing found, nothing missing → end silently. No draft, no noise.
