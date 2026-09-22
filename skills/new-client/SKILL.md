---
name: new-client
description: >
  Set up the Google Drive editing folder structure for a new Me & My Old Man
  family client. Trigger this whenever Neil says "/new client", "new client",
  "set up a new family", "create the editing folder for [family name]", or
  names a family and starts listing children/parents/editor for a project —
  even if he doesn't use the exact phrase "new client". This is a fixed,
  mechanical folder-creation workflow (not a writing task), so use it any
  time the ask is about creating the Drive structure for a family, not about
  drafting content for one.
---
<!-- v1.1 — 2026-07-24: Bronze tier is dad/mum-only, 3 folders total (S.1/S.2/S.3), never a 4th Wrap Up folder. Confirmed after the Kumar (Bronze) build initially added a Wrap Up chapter in error. -->
<!-- v1.2 — 2026-07-24: Added Airtable Editor Pipeline logging step so upcoming sessions are tracked (TBC) from the moment a client closes, ahead of real dates. -->
<!-- v1.3 — 2026-08-24: Added Music Selection Tracker Google Sheet logging step, so intro/outro picks are tracked per chapter and don't get duplicated within a family. -->
<!-- v1.4 — 2026-09-22: Retranslated from Bronze/Silver/Gold to the A to D option ladder. Option A is the only one with no Wrap Up. B gets a buyer chapter, C gets one shared children chapter. -->
<!-- v1.5 — 2026-09-22: Added Family Hours & Countries Tracker logging step, and a step to refresh knowledge/offer/business-stats.md from it. business-stats.md is now the single source of truth every content skill reads its families/hours/countries figure from, so it must be kept current the moment a new client is won. -->

# New Client — Editing Folder Setup

Builds the standard Google Drive folder tree for a new family under
`Shared Drive > Editing > Editor [Name]`, ready for editors to receive
briefings and drop edits.

## Before you start: gather the details

Never guess at family structure — always confirm with Neil first if any of
this is missing or ambiguous:

1. **Family surname** (used in the top folder name: `Editing - [Surname]`)
2. **Editor** — one of Vuk, Jodie, Abhi, Neil, or TBC if not yet assigned
3. **Option** — A, B, C or D. This determines the folder count (see below),
   so always confirm it. These are the internal labels; families see Hero
   Story (A and B), Family Documentary (C) and Full Chorus (D). See
   `knowledge/offer/pricing.md`.
4. **Children** — full list of first names, in the order chapters should run.
   Option A has no children chapters at all. Option B has one, for the
   buying child only. Confirm which before skipping this step.
5. **Parent(s)** — name(s), and whether each is "The Old Man" or "Mum" (use
   whichever term matches how Neil refers to them — check his phrasing)
6. **Number of parent sessions** — parents are normally recorded across 3
   sessions (S.1, S.2, S.3), each covering 2 chapters. Confirm this is still
   3 for this family; some families may differ.
7. Whether the briefing doc content should come from the standard template
   (ask if unsure where that lives) or something Neil supplies directly.

Ask concise, single questions rather than assuming — getting the chapter
sequence wrong means renumbering every folder and doc afterwards.

## Option rules — folder count (read before building)

The option decides how the children are recorded, which decides the chapter
count. Confirm the option before creating anything.

| Option | Children chapters | Wrap Up | Total folders |
|---|---|---|---|
| A — solo, no child interview | none | no | 3 |
| B — solo, buyer interviewed | 1, the buying child | yes | 5 |
| C — children batched, one session | 1, all children together | yes | 5 |
| D — children individually | one per child | yes | 4 + one per child |

- **Option A** is the only option with no Wrap Up. Exactly 3 chapter folders:
  Ch1&2 (S.1), Ch3&4 (S.2), Ch5&6 (S.3). Never create a 4th folder for A.
- **Option B** opens with one child chapter for the buying child, then the
  parent pairs, then the Wrap Up.
- **Option C** opens with one shared chapter covering all the children in a
  single session, named `Ch1. Us & [The Old Man / Mum]`, then the parent
  pairs, then the Wrap Up.
- **Option D** gives each child their own chapter, then the parent pairs,
  then the Wrap Up.

If the option is ambiguous, ask before creating any folders. The gap between
A and D is three folders or more, and renumbering afterwards means renaming
every folder and every briefing doc inside it.

## Folder and chapter logic

The chapter numbering is sequential and follows this fixed order:

1. **One chapter per child**, in the order given, each titled:
   `ChN. [FirstName] & [The Old Man / Mum]`
   (N starts at 1 and increments per child — 2 kids means Ch1 and Ch2, 3 kids
   means Ch1, Ch2, Ch3, etc.)

   This is the Option D shape. **Option A skips this step entirely.**
   **Option B** creates exactly one chapter here, for the buying child.
   **Option C** creates exactly one shared chapter for all the children
   together, named `Ch1. Us & [The Old Man / Mum]` rather than naming one
   child.

2. **Three chapter-pairs for the parent**, continuing the sequence
   immediately after the children (or starting at Ch1 for Option A), each
   covering 2 chapters and one session: `ChX & Y [ParentFirstName]` — e.g.
   if children took Ch1-2, the parent pairs are Ch3&4, Ch5&6, Ch7&8. These
   map to sessions S.1, S.2, S.3 in that order.

   If there are two parents (e.g. Mum and Dad), ask Neil whether each
   parent gets their own set of three chapter-pairs, or whether they share
   the sequence — don't assume.

3. **One final "Wrap Up" chapter** — **every option except A.** Numbered to
   continue the sequence immediately after the last parent chapter:
   `ChZ Wrap Up`. **Do not create this folder for Option A projects.**

## What to create, in order

1. **Locate the editor folder**: search Drive for `title = 'Editor [Name]'`
   (or `'EDITOR [Name]'` — check the actual casing used in Drive) under the
   Shared Drive Editing root. If Neil hasn't said which editor yet, use
   `Editor TBC`.

2. **Create the family folder** inside that editor folder:
   `Editing [- Surname]` — e.g. `Editing - Griffith`.

3. **Create each chapter folder** inside the family folder, using the
   naming logic above. For Option A, this means exactly 3 folders — stop
   there.

4. **Inside every chapter folder**, create three subfolders:
   `Neil Internal`, `Edits`, `Video`.

5. **Duplicate the briefing doc template as a Gdoc into each chapter
   folder** (not into the subfolders — it sits alongside them). Rename each
   copy following this convention:
   - Children: `ChN [FirstName] - Editor Briefing`
   - Parent chapters: `ChX&Y [ParentFirstName] - S.[1/2/3] | Editor Briefing`
   - Wrap Up (every option except A): `ChZ Wrap Up - Editor Briefing`

   If a template file can't be found or read, ask Neil to point you to it or
   paste the content rather than inventing placeholder text — the briefing
   doc structure (titles, music, commentary, stings) is specific and used
   by editors downstream.

## Log the pipeline (Airtable)

After building the Drive structure, log placeholder entries so upcoming
sessions are tracked before real dates exist. Base "M&MOM Database"
(`app077Z4RXX1PShzN`), table "Editor Pipeline" (`tblWkRNY5rcvthBMs`). Use
`create_records_for_table` with these field IDs:
- `fldfvHJsC7EILNfpr` Family Name (the surname)
- `fldvMQG55QBjefTeB` Interviewee (first name)
- `fldO9gjgDbql5WTxC` Session Type — "1hr Child Briefing" or "2hr Parent
  Life Story Recording"
- `fldBeVYeozSiPiewg` Session Label — blank for children, "S1"/"S2"/"S3"
  for each parent session
- `fldvpwgWDhllOGcFI` Status — always "TBC" at this stage
- `fldb3hwVVXTrSJDe5` Editor — the assigned editor, or "TBC" if not yet
  decided

Create one record per child chapter (Session Type "1hr Child Briefing") —
**skip this entirely for Option A**, and for Option C create a single record
for the batched session rather than one per child, same as the folder logic
above — and one record
per parent session confirmed with Neil (Session Type "2hr Parent Life Story
Recording", one row per S.1/S.2/S.3 etc. — match however many sessions Neil
confirmed for that parent, not always 3). Don't create a Wrap Up record
here — that gets logged later, closer to when it's actually being
scheduled, and never at all for Option A.

Real dates get filled in automatically later, triggered off Neil's
calendar once the family's onboarding call happens (see the
`onboarding-call-followup-scheduler` scheduled task) — you don't need to
chase dates now.

This Airtable table is a reliability backstop — it captures every session
even if the step below can't run (e.g. no browser available). It is not
what Neil looks at day to day.

## Also log it in the Production Tracker Google Sheet

Neil works from a Google Sheet, not Airtable, day to day. Since this skill
runs in an attended session, also add the same rows directly to the
Sheet via the browser (claude-in-chrome tools):
`https://docs.google.com/spreadsheets/d/1LRQVumMLuagg2IUaIBDdwi9Kw4ufNrLhS983M9oto3g/edit`
("Pipeline" tab). Columns in order: Family, Interviewee, Session Type,
Session Label, Editor, Status, Session Date, Notes — same values as the
Airtable rows above. Click the first empty row below the existing data
(Ctrl+/Cmd+Down from A1 to jump to the last filled row, then move down
one) and type each row's values across the columns. Leave Session Date
blank (TBC). If the browser isn't available in this session, skip this
step — the Airtable record is still there as a backstop, and it can be
added to the Sheet later.

## Also log it in the Music Selection Tracker Google Sheet

Neil tracks which intro/outro track has been chosen for each chapter so he
doesn't reuse the same piece of music twice within one family's audio
documentary. Once the Airtable Editor Pipeline rows above exist (correct
family surname and interviewee first name), add matching rows to the
Music Selection Tracker Sheet:
`https://docs.google.com/spreadsheets/d/1DtURDPqUp1rbz6lAGOY_WrCVeoo9l_JcXWJZOQ2fBTg/edit`
— the **"Family - Selected Tracks"** tab specifically (not "Music Library",
which is the master track catalogue and shouldn't be touched here).

Columns, in order: `Last Name` | `First Name` | `Chapter` | `Track` | `Status`.

Rows are per individual chapter, not per folder/session-pair — split each
parent chapter-pair into its two chapter rows:
- **Children**: one row per child chapter — `Last Name` = surname,
  `First Name` = child's first name, `Chapter` = `ChN` (e.g. `Ch1`),
  matching that child's chapter number from the folder logic above. Skip
  for Option A. For Option C, one row for the shared chapter with
  `First Name` = `Us`.
- **Parent sessions**: two rows per session, one per chapter in the pair —
  `Last Name` = surname, `First Name` = parent's first name, `Chapter` =
  `ChN. [Old Man/Mum]` using whichever term Neil used for that parent (e.g.
  a `Ch3&4` session folder becomes two rows: `Ch3. Dad` and `Ch4. Dad`).
- **Wrap Up**: skip for now, same as the Airtable step above — it gets
  logged later, closer to when it's actually scheduled, and never for
  Option A.

For every new row, set `Track` to `tbc` and leave `Status` blank — don't
invent a track or mark a status. Before adding rows, scan the sheet for
this family's existing `Last Name` entries so you don't create a duplicate
row for a chapter that's already logged.

Use the claude-in-chrome browser tools to edit this Sheet, same as the
Production Tracker step above. If the browser isn't available in this
session, skip this step and flag it clearly so Neil (or a later run) can
add the rows once a browser is available.

## Also log it in the Family Hours & Countries Tracker Google Sheet

Neil tracks total families, hours and countries served in this Sheet, and
it's the source data behind every "X families / Y hours / Z countries"
figure used in his bios and content:
`https://docs.google.com/spreadsheets/d/1njqBD96T5MLP4GGAK5_PTS-dAM6wX0peIF3AWOOhZA0/edit`.
Columns, in order: `#` | `Family` | `Child` (hours) | `Parent` (hours) |
`Wrap Ups` (hours) | `Countries` | `Country #`.

Add one new row for this family:
- **#** — next sequential number after the last filled row.
- **Family** — the surname.
- **Child / Parent / Wrap Ups** — hours for each, following the pattern of
  existing rows for the same option (A/B/C/D). If it isn't obvious from the
  option and session count, ask Neil for the hours rather than guessing —
  these numbers roll up into the headline stats everyone else quotes.
- **Countries** — only fill in if this family is based outside the UK. If
  Neil hasn't said where the family is based when invoking this skill, ask.
  Leave blank for UK families.
- **Country #** — put `1` only if this is a country not already listed
  elsewhere in the Countries column (i.e. it adds a new country to the
  total, not a repeat). Scan the existing Countries column first. Leave
  blank for UK families or repeat countries.

Use the claude-in-chrome browser tools to edit this Sheet, same as the
Production Tracker step above. If the browser isn't available in this
session, skip this step and flag it clearly — the stats refresh below
depends on it, so do it as soon as a browser is available.

## Refresh knowledge/offer/business-stats.md

`knowledge/offer/business-stats.md` is the single source of truth every
content skill (linkedin-post, newsletter, mmom-podcast-pr,
mmom-sales-strategist, instagram, and others) reads its families/hours/
countries figure from. It must be updated the same session a new client is
won, using the tracker sheet you just updated:

1. Read the tracker sheet's totals row (Sub-Total Hrs / Total, and the
   Country # sum).
2. **Families** — exact count of families logged in the tracker (no
   rounding).
3. **Hours** — sum of the Child + Parent + Wrap Ups totals, rounded DOWN to
   the nearest 10. Never round up, never use the raw total.
4. **Countries** — exact count of flagged (`1`) entries in the Country #
   column (no rounding).
5. Edit `knowledge/offer/business-stats.md`: update the three numbers, the
   "Current numbers (as of ...)" date, and the worked examples under "How
   to phrase it in copy" so they still read correctly with the new figures.

Do this even if the Sheet step above had to be skipped for lack of a
browser — in that case, compute the new totals from what you just logged
in Airtable/the Production Tracker instead, and flag that the Sheet itself
still needs the row added later.

## After building

List back the full folder tree you created (chapter names, subfolder names,
doc names) AND the pipeline rows you logged (Airtable and, if you managed
it, the Production Tracker Sheet, the Music Selection Tracker Sheet, and
the Family Hours & Countries Tracker), plus the new families/hours/
countries figures now in `business-stats.md`, so Neil can quickly eyeball
all of it against what he asked for — this catches naming mistakes before
an editor starts working from a wrong folder. For Option A, explicitly
confirm only 3 chapter folders were created (no Wrap Up). For every other
option, confirm the Wrap Up folder exists.
Share the link to the top-level family folder.

## Notes on care

Getting names, spelling, and chapter numbers exactly right matters more than
speed here — these folders get used by editors for weeks and a wrong name
(e.g. "Geoff" vs "Jeff") causes confusion downstream. When in doubt about a
spelling or a detail Neil mentioned casually, read it back to confirm before
creating dozens of files around it.
