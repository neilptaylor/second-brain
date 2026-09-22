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

# New Client — Editing Folder Setup

Builds the standard Google Drive folder tree for a new family under
`Shared Drive > Editing > Editor [Name]`, ready for editors to receive
briefings and drop edits.

## Before you start: gather the details

Never guess at family structure — always confirm with Neil first if any of
this is missing or ambiguous:

1. **Family surname** (used in the top folder name: `Editing - [Surname]`)
2. **Editor** — one of Vuk, Jodie, Abhi, Neil, or TBC if not yet assigned
3. **Children** — full list of first names, in the order chapters should run
4. **Parent(s)** — name(s), and whether each is "The Old Man" or "Mum" (use
   whichever term matches how Neil refers to them — check his phrasing)
5. **Number of parent sessions** — parents are normally recorded across 3
   sessions (S.1, S.2, S.3), each covering 2 chapters. Confirm this is still
   3 for this family; some families may differ.
6. Whether the briefing doc content should come from the standard template
   (ask if unsure where that lives) or something Neil supplies directly.

Ask concise, single questions rather than assuming — getting the chapter
sequence wrong means renumbering every folder and doc afterwards.

## Folder and chapter logic

The chapter numbering is sequential and follows this fixed order:

1. **One chapter per child**, in the order given, each titled:
   `ChN. [FirstName] & [The Old Man / Mum]`
   (N starts at 1 and increments per child — 2 kids means Ch1 and Ch2, 3 kids
   means Ch1, Ch2, Ch3, etc.)

2. **Three chapter-pairs for the parent**, continuing the sequence
   immediately after the children, each covering 2 chapters and one session:
   `ChX & Y [ParentFirstName]` — e.g. if children took Ch1-2, the parent
   pairs are Ch3&4, Ch5&6, Ch7&8. These map to sessions S.1, S.2, S.3 in
   that order.

   If there are two parents (e.g. Mum and Dad), ask Neil whether each
   parent gets their own set of three chapter-pairs, or whether they share
   the sequence — don't assume.

3. **One final "Wrap Up" chapter**, numbered to continue the sequence
   immediately after the last parent chapter: `ChZ Wrap Up`.

## What to create, in order

1. **Locate the editor folder**: search Drive for `title = 'Editor [Name]'`
   (or `'EDITOR [Name]'` — check the actual casing used in Drive) under the
   Shared Drive Editing root. If Neil hasn't said which editor yet, use
   `Editor TBC`.

2. **Create the family folder** inside that editor folder:
   `Editing [- Surname]` — e.g. `Editing - Griffith`.

3. **Create each chapter folder** inside the family folder, using the
   naming logic above.

4. **Inside every chapter folder**, create three subfolders:
   `Neil Internal`, `Edits`, `Video`.

5. **Duplicate the briefing doc template as a Gdoc into each chapter
   folder** (not into the subfolders — it sits alongside them). Rename each
   copy following this convention:
   - Children: `ChN [FirstName] - Editor Briefing`
   - Parent chapters: `ChX&Y [ParentFirstName] - S.[1/2/3] | Editor Briefing`
   - Wrap Up: `ChZ Wrap Up - Editor Briefing`

   If a template file can't be found or read, ask Neil to point you to it or
   paste the content rather than inventing placeholder text — the briefing
   doc structure (titles, music, commentary, stings) is specific and used
   by editors downstream.

## After building

List back the full folder tree you created (chapter names, subfolder names,
doc names) so Neil can quickly eyeball it against what he asked for — this
catches naming mistakes before an editor starts working from a wrong folder.
Share the link to the top-level family folder.

## Notes on care

Getting names, spelling, and chapter numbers exactly right matters more than
speed here — these folders get used by editors for weeks and a wrong name
(e.g. "Geoff" vs "Jeff") causes confusion downstream. When in doubt about a
spelling or a detail Neil mentioned casually, read it back to confirm before
creating dozens of files around it.
