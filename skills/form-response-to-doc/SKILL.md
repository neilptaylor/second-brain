---
name: form-response-to-doc
description: Turn new Child Reflection Guide form responses into formatted Google Docs filed in the right family's editor folder. Use this whenever Neil asks to process new form responses, check for new briefing submissions, catch up the family briefing docs, or run the "form to doc" / "briefing doc" skill — including phrases like "any new responses come in?", "turn the latest submissions into docs", or a specific person's name plus "form"/"submission"/"briefing". Manual trigger only — never run automatically without Neil asking.
---

# Form Response to Doc

Turns rows from the Child Reflection Guide response sheet into a formatted Google
Doc per response, filed into the right family's session folder inside the
Editing shared drive. This is a manual, on-demand skill — only run it when Neil
asks.

## Why this works the way it does

The response sheet has no "processed" flag and no dedicated "family surname" or
"editor" column — column B is free text like `"Carl Taylor-Son Phil Taylor"` or
`"Carl Taylor- Son   Maggie Taylor."`, and formatting is inconsistent between
respondents. There's also no Drive tool available in this session that can write
back to an existing Sheet or Doc (only create new files, copy, and read). Two
things follow from that:

1. **Family surname and which-parent must be parsed loosely**, not looked up in
   a field.
2. **"Already processed" is determined by checking whether a matching doc
   already exists**, not by a marker in the sheet. Before creating a doc, always
   search the target subfolder for one already titled the same way, and skip
   the row if it's there. This makes reruns safe — you can run this skill as
   often as you like and it will only ever create docs for genuinely new rows.

There's also no tool available to move, rename, or delete a Drive file once
created — only create and copy. So getting the destination folder right
*before* creating the doc matters more than usual: if you get it wrong,
fixing it means creating a corrected copy elsewhere and asking Neil to trash
the original by hand, since you can't do that yourself.

## Step 1: Find the response sheet

The known sheet is **`Child Primer_Homework (Responses)`**
(file ID `1WSC3YBarKi3_CrHQW3o07i-9FBjCr6-zVlAoaed_wWY`). Try that ID first with
`get_file_metadata` to confirm it still resolves. If it's gone or Neil mentions
a different form, use `search_files` for the sheet name matching the form (Forms
auto-name the response sheet `<Form Name> (Responses)`), or ask Neil to paste
the Google Form or Sheet link.

Don't confuse this with the **`Welcome Form (Responses)`** sheet
(`1HDikByjenngUsguhJ3M3xcloLzL-VXqnh3BN-O0q0do`) — that's a separate intake form
(who's participating, contact details) and isn't in scope for this skill.

Read the sheet with `download_file_content` using `exportMimeType: text/csv` —
CSV parses far more reliably than the natural-language `read_file_content`
output for a wide, many-column sheet like this one.

## Step 2: Parse each row

Columns (as of last check — re-verify headers if the sheet has changed):

| Col | Header |
|---|---|
| A | Timestamp |
| B | "What is your first name and family name... Please also state which parent." |
| C–K, M–P | The reflection questions themselves |
| L | Email address |

For each row, extract:

- **Submission date** — from column A, format as `D Month YYYY` (e.g. `11 July
  2026`) for the doc title.
- **Respondent's name, family surname, and which parent** — from column B.
  This field is free text and inconsistent, so parse by judgment rather than a
  fixed pattern: look for a surname shared between the respondent and a named
  parent, and look for words/names indicating which parent — "Mum", "Mom",
  "Mother", or a female first name mean the response is about the mother;
  "Dad", "Father", "Old Man", or a male first name mean the father. If column B
  is too ambiguous to confidently determine the surname or which parent, stop
  and ask Neil rather than guessing — filing a doc in the wrong family's folder
  is worse than pausing to check.
- **Question/answer pairs** — every other column is a question (the column
  header) paired with that row's answer (the cell value). Skip any pair where
  the answer is blank. Keep answers verbatim, including typos — these are
  personal reflections, not copy to be cleaned up.

## Step 3: Find the family folder

**Family session folders are not confined to one known shared drive, and
editor names in a folder's path don't mean "skip it."** Family folders (e.g.
`Taylors - Jodie`) can live directly, or nested one level under an editor's
own top-level folder (e.g. `EDITOR Vuk / Taylors - Jodie`) — Neil's editors
each keep their assigned families' folders under their own name. There can
also be more than one folder with a similar name in different shared drives
that *isn't* the right one — e.g. a generic family-info folder with a
`Plans/Trees/Guides/Photos/Stories` structure unrelated to editing sessions.

So: use `search_files` for the family surname across all of Drive (try both
singular and plural/possessive forms Drive tends to use, e.g. "Taylor" and
"Taylors" — don't scope the search to a single hardcoded folder ID, since the
right family folder may be nested under any editor). Judge candidates **by
their internal structure, not by what folder they sit under**: the right one
contains chapter-style subfolders named like `Ch1 ...`, `Ch2 ...` etc. If
more than one folder matches that shape, or none does, stop and ask Neil
which one to use rather than guessing.

Inside the matched family folder, find the subfolder for the correct parent —
named along the lines of `Ch1 ... & Mum` / `Ch1 ... & The Old Man` (or `&
Dad`). Match on "Mum" vs "Dad"/"Old Man"/"Father" in the subfolder name,
consistent with which parent you determined in Step 2. If no subfolder clearly
matches, stop and ask rather than creating one or guessing.

Inside that Ch-folder, file into its **`00 Neil Internal`** subfolder if one
exists (siblings like `01 Audio Files`, `02 Video Files`, `03 Edits`, `04
Final Approved Versions` are not for this doc). If there's no `00 Neil
Internal` subfolder, use the Ch-folder itself.

## Step 4: Check for an existing doc (the dedup step)

Build the target title: `[Family Surname] ([Respondent First Name]) — [Submission Date]`
(e.g. `Taylor (Carl) — 11 July 2026`). Including the respondent's first name
matters — two siblings can submit about the same parent on the same day, and
without it their doc titles would collide.

Search the matched destination folder for a doc already titled this. If
found, skip this row — it's already been processed — and move to the next
one. Don't create a duplicate.

## Step 5: Create the doc

Use `create_file` with:
- `title`: the target title from Step 4
- `parentId`: the matched subfolder's ID
- `contentMimeType`: `text/html`
- `textContent`: HTML built as below (leave `disableConversionToGoogleType`
  unset/false so Drive converts it into a native Google Doc)

HTML structure — question bold, answer plain, a blank paragraph between pairs:

```html
<p><b>Question text here?</b></p>
<p>Answer text here.</p>
<p></p>
<p><b>Next question?</b></p>
<p>Next answer.</p>
<p></p>
```

Put the respondent's name and email at the top of the doc (before the first
Q&A pair) so the editor has contact context at a glance:

```html
<p><b>Submitted by:</b> [Respondent Name] ([email])</p>
<p><b>Date:</b> [Submission Date]</p>
<p></p>
```

## Step 6: Report back

For each row processed, report:

- Family name
- Doc title
- Doc URL (`https://docs.google.com/document/d/<fileId>/edit`, from the
  `create_file` response)
- Folder path it was saved in (family folder → subfolder)

For each row skipped (doc already existed), report the family name and that it
was already processed — don't silently skip without mentioning it, so Neil can
see the run covered every row.

If more than ~5 new docs would be created in one run, list what you're about
to do and confirm with Neil before creating them — a big backlog usually means
something upstream changed and is worth a sanity check first, rather than
silently bulk-creating a dozen docs.
