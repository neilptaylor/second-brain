---
name: editor-briefing
description: "Creates an Editor Briefing doc for a client editing session at Me & My Old Man, links it to the Drive editing folder and the matching recording (Riverside or Zoom), reformats the raw transcript into a clean Google Doc and .md file, proposes chapter titles from the transcript (fixed formula for a Child Briefing or Wrap Up, 3-4 house-style options for a Parent Session), fills in the music track for each chapter and logs each selected track against its chapter in the music tracking sheet, flips the session's Status/Onboarding fields in Airtable, and drafts the Gmail handoff to the assigned editor. Also handles interviewer prep: after the last child in a family is recorded, it builds an Interview Briefing for the parent's Session 1 from all children's transcripts; after a parent's Session 1, it builds a follow-up briefing for Session 2, and so on for later sessions. Use whenever Neil says \"brief the editor for [family/interviewee] session [n]\", \"create the briefing doc for [name]\", \"set up Ch[x]&[y] briefing\", or names a family + chapters + session number for handing a recording to an editor. Trigger even on terse asks like \"briefing for Jim Kumar S2\" — ask for missing pieces rather than skipping."
---

<!-- v1.7 — 2026-09-22: merged the forked Drive lineage back in. Gained Step 3b
(propose chapter titles, fixed formula for Child Briefing and Wrap Up, 3-4
house-style options for a Parent Session) plus references/chapter-title-style-examples.md,
and the rule to log every selected track in the "family - selected tracks" tab.
Both had been developed only in the Drive copy between 24 Aug and 16 Sep. -->
<!-- v1.6 — 2026-09-18: two fixes.
(1) All editor rates are quoted to Neil in GBP, always — never USD, even for
editing whose rate card is denominated in USD with a GBP equivalent
alongside. Fixed Abhi's rate card in references/editor-contacts.md to state
GBP-only figures pulled from his current rate doc, and added a hard rule in
Step 6 that the handoff email must always quote GBP regardless of how the
source rate card is denominated. Previously Abhi's rates defaulted to USD
with GBP only as a fallback "if that's what's been used in the thread" —
this caused a live handoff email to quote $25 instead of the correct £22.
(2) Reiterated and hardened the music-link step: the Music Library &
Selections sheet
(https://docs.google.com/spreadsheets/d/1DtURDPqUp1rbz6lAGOY_WrCVeoo9l_JcXWJZOQ2fBTg/edit)
must actually be opened and the real hyperlink extracted and used in the
briefing doc's Music section — this step was skipped on a live job (left as
"TBC (Neil to add link)" instead of being looked up), so the instruction now
spells out that leaving it TBC is only acceptable after a genuine attempt
(Chrome tools unavailable, or track truly not found in the sheet), not as a
default shortcut. -->

<!-- v1.5 — 2026-09-17: added an "Edits" line (Heading 3) as the final item
in the briefing doc template, below Stings & Outro - Timestamps, so the
editor has a dedicated place to drop the G Drive link to their edits (V1, V2,
Final, etc.) once they start delivering work back. Previously there was no
place in the doc for the editor's return-delivery link. -->

Neil records life-story sessions with clients, then hands the raw footage to an
editor. Sessions are recorded on either Riverside or Zoom, depending on the
setup. Each editing chunk covers one recorded session — typically 1hr for a
child session, 2hr for a parent life-story session, or 1–1.5hr for a family
wrap-up — and needs a short briefing doc so the editor knows which files to use,
what music to drop in, and how long the piece should run. This skill produces
that doc and does the bits of bookkeeping that go with it: linking the Drive
folder + recording (Riverside or Zoom), reformatting the transcript, proposing
the chapter titles, and updating the CRM row so the session shows as handed
off.

There's a second, separate purpose bundled in here too: prepping Neil (as
interviewer, not editor) for upcoming sessions. Kids get interviewed first, and
what they say shapes the questions Neil should ask their parent. Once every
child in a family has been recorded, that's the moment to pull all the kids'
transcripts together into a single briefing for the parent's Session 1. And once
any parent session is done (S1, S2, S3, and so on), that transcript becomes the
basis for a follow-up briefing ahead of the next session, so Neil doesn't have
to remember everything that was covered or start the next session cold. Do
this automatically whenever it applies — don't wait to be asked separately,
since it's part of the same handoff moment as the editor briefing.

There's a third piece too: once the briefing doc and bookkeeping are done, the
handoff isn't complete until Neil actually has something to send the editor.
This skill drafts that Gmail handoff automatically as the final production
step, in each editor's own established style.

## Overview of steps

1. Find the Drive session folder
2. Create the editor briefing doc
3. Link the recording, download its transcript, and reformat it into a clean
   Google Doc and .md file saved in the session folder
3b. Propose chapter titles and write them into the doc
4. Update the Airtable Editor Pipeline
5. Check whether this triggers an interviewer briefing (last child session, or
   parent S1, S2, S3...) and build it if so
6. Draft the Gmail handoff to the assigned editor
7. Confirm with Neil

## Inputs needed

Before starting, make sure you have:

1. **Family name + interviewee** (e.g. "Kumar", "Jim Kumar")
2. **Session number and chapters** (e.g. "S1", "Ch3 & 4")
3. **Session date** in `YYYYMMDD` format — ask Neil if not given, don't guess
4. **Recording platform** — Riverside or Zoom. If not stated, ask; the lookup
   method in Step 3 differs between the two.
5. **Music track(s) per chapter** — Neil picks these by ear from the Music Library
   sheet, or sometimes hands you a direct Drive link to the track file itself —
   ask him for the track name(s) or link per chapter rather than choosing
   yourself. It's fine to leave a chapter as "TBC" if he doesn't have a pick yet
   — but once he HAS named a track, the link lookup in Step 3 is mandatory, not
   optional (see below).

If any of these are missing, ask — don't invent chapter numbers or dates.

## Step 1: Find the Drive session folder

The folder structure is:
`Editing / EDITOR [Editor Name] / Editing - [Family Name] / Ch[x]&[y] [Interviewee First] - S.[n]`

Search Drive for a folder matching `Ch[x]&[y] * S.[n]` under the relevant
`Editing - [Family]` parent. If there's no existing folder for this chapter/session
combination, check whether an adjacent one exists (e.g. `Ch1&2 ... S.1`) and create
the new one as a sibling, matching the naming convention exactly. Neil sometimes
names a child session folder descriptively (e.g. "Ch1. Sam & Mum") rather than
with the strict `S.[n]` suffix — if an existing folder for this session already
exists under a name like that, use it as-is rather than creating a duplicate in
the stricter naming pattern.

## Step 2: Create the briefing doc

Find an existing "Editor Briefing" doc in the same client folder (or a template
folder if Neil has designated one) to copy the structure from — don't invent a new
layout. The doc title follows this pattern:

```
YYYYMMDD [Interviewee Full Name] S[n] | Ch[x] & [y] | Editor Briefing
```

Example: `20260803 Jim Kumar S1 | Ch3 & 4 | Editor Briefing`

The body structure (copy this shape, don't redesign it):

```
[Doc title as Title style]

Link to files in G Drive Folder - here (hyperlinked to the Step 1 folder)

Link to Recording - here (hyperlinked to the Riverside/Zoom link, see Step 3)

Transcript (Google Doc) - here / Transcript (.md) - here (hyperlinked to the
Step 3a reformatted transcript files)

Titles [Heading 3]
Ch[x] TBC
Ch[y] TBC

Loom Briefing / Commentary [Heading 3]
xx

Music [Heading 3]
Ch[x] - [track name, hyperlinked — see Step 3 for how to get the real URL]
Ch[y] - [track name, hyperlinked — see Step 3 for how to get the real URL]

Duration [Heading 3]
xx

COMMENTARY & STINGS FROM EDITOR [Heading 3]

Commentary [Heading 3]

Stings & Outro - Timestamps [Heading 3]
- Xx
- xx

Edits [Heading 3]
Please drop the G Drive link to your edits here (V1, V2, Final, etc.)
```

The final "Edits" heading is where the assigned editor drops the G Drive link
to their delivered cuts as they come in — leave the line under it as a plain
instruction (not a placeholder link) since there's nothing to link yet when the
doc is first created; the editor fills this in themselves once they have
something to share.

Create this as a Google Doc directly in the session's Drive folder (or its parent
client folder, matching where the existing briefing docs live). Don't upload plain
text — plain text loses the Title/Heading 3 styling and produces dead-text links
instead of real hyperlinks. Instead, build the body as HTML (real `<h1>` for the
doc title, `<h3>` for each subtitle, `<a href="...">` for every link) and upload it
via the Drive file-creation tool with `contentMimeType: "text/html"` and
`mimeType: "application/vnd.google-apps.document"` — Drive converts this into a
native Google Doc with working Title/Heading 3 styles and live hyperlinks. Verify
after creating by reading the file back and checking for `# **title**`, `### **heading**`,
and `[text](url)` markdown in the result, which confirms the styles/links landed
correctly rather than as literal text.

## Step 3: Link the recording and download its transcript

**Before assuming any asset needs pulling from Zoom or Riverside, check the
session's Drive folder first.** Neil often uploads recordings, separate audio
tracks, or transcripts manually ahead of asking — don't flag Zoom login or
Riverside browser access as a blocker until you've confirmed the file isn't
already sitting in Drive. Note that Neil sometimes drops separate raw audio
tracks (e.g. `riverside_<name>_raw-audio_...wav`) into a generic Drive
"Downloads" folder rather than the session folder itself — check there too if
he mentions separate tracks being available, and link to them from wherever
they actually are rather than moving them.

**If Zoom:** use the Zoom connector directly — no browser needed. Use
`recordings_list` (or `search_meetings` / `ask` if you need to find the meeting
by name/date first) to find the session recording, then `get_meeting_assets` to
get the cloud recording's play URL. Match by date and interviewee name if there
are multiple candidates. Drop the play URL straight into the doc. Then pull the
transcript with `get_meeting_assets` / `get_recording_resource` (`types=transcript`).
Note: `get_meeting_assets` / `get_recording_resource` responses can be very large
(hundreds of KB) and may get saved to a local file rather than returned inline —
if so, use bash/jq to extract just the play_url and the transcript timeline array
rather than reading the whole payload into context.

**If Riverside:** there's no API/MCP access to Riverside, so this has to go
through the browser. Use the Claude in Chrome tools to navigate to
riverside.com, find the project (names follow the pattern `[First] [Last] S.[n]`,
e.g. "Vaughan Griffiths S.1") via the search box (Cmd/Ctrl+K), and copy its
project URL and duration from the search result / project page. Riverside
projects also have a "Transcript" export (visible on the project page) if a
transcript isn't already sitting in Drive — download or copy that transcript
too. If Chrome tools aren't available in this session, ask Neil to paste the
Riverside project URL and transcript instead, or leave the recording line as a
placeholder (`Link to Recording - TBC`) and tell him those are the things he
needs to drop in himself. Don't guess a URL either way.

You need this transcript regardless of whether Step 5 ends up applying — it
costs little to grab it now and saves a second trip back into Riverside/Zoom
later.

**Music track links — THIS IS A REQUIRED LOOKUP, NOT AN OPTIONAL NICE-TO-HAVE:**
Whenever Neil has named a track (by song name, or artist + song), the skill
must go and find its real hyperlink and put that hyperlink in the briefing
doc's Music section — do not write the track name as plain unlinked text, and
do not default to "link TBC" just because the lookup takes browser steps.
"TBC" is only acceptable when Chrome tooling is genuinely unavailable in this
session, or the track truly cannot be found in the sheet after a real search
— not as a shortcut to save time.

The sheet is **Music Library & Selections**:
https://docs.google.com/spreadsheets/d/1DtURDPqUp1rbz6lAGOY_WrCVeoo9l_JcXWJZOQ2fBTg/edit
It has a "Song (hyperlinked)" column where each track filename is a rich-text
hyperlink to the actual Drive (or YouTube) file — but that underlying URL does
NOT show up in any Drive-read export (plain text read, or `gviz`/CSV export all
strip cell-level hyperlinks and return just the filename). To get the real URL:

1. Open the sheet above in Claude in Chrome.
2. Navigate to (or confirm you're on) the "Music Library" tab.
3. Locate the track's row — the Name Box (e.g. typing `B84` and Enter) is much
   faster than scrolling or Ctrl+F. Ctrl+F does not open Sheets' native
   find-in-sheet from these tools, it types into whatever cell is currently
   selected, so avoid it; instead use the sheet's own on-screen filter/search
   UI or scroll/Name-Box navigation to locate the artist/song.
4. Click the cell in the "Song (hyperlinked)" column to pop up its link chip.
5. Use `find` (natural-language element search) on the page to pull the full
   un-truncated href out of the popup — don't rely on any truncated/visible
   text, the popup can clip long Drive URLs.
6. Copy that Drive/YouTube URL into the briefing doc's Music section as the
   hyperlink target for the track name (e.g. `Ch8 - <a href="...">Come
   Together - The Beatles</a>`).

Alternatively, Neil sometimes hands you a direct Drive link to the music file
itself (e.g. an mp3 he's already placed in Drive) — use that directly, no
sheet lookup needed in that case.

If Chrome tooling isn't available in this session AND no direct link was
given, that's the one legitimate reason to leave it as "TBC" — ask Neil to
paste the URL directly rather than guessing or linking to the sheet itself,
and say plainly in Step 7 that this is why the music link is still open.

**Logging selected tracks:** every time a music track is chosen for a chapter
(whether picked from the Music Library sheet or handed to you directly by
Neil as a Drive/YouTube link), log it in the "family - selected tracks" tab of
https://docs.google.com/spreadsheets/d/1DtURDPqUp1rbz6lAGOY_WrCVeoo9l_JcXWJZOQ2fBTg/edit?gid=0#gid=0 —
list the track against the respective chapter (family/interviewee, chapter
number, track name/link). Do this for every session briefed, not just when
Neil explicitly asks.

Before typing into any cell in the Music Library sheet via browser automation,
verify the Name Box shows the intended cell and the formula bar shows the
expected pre-edit content — a misdirected click/type sequence can silently
overwrite the wrong cell. Re-read the cell after any edit to confirm it landed
correctly; don't assume an undo worked without checking.

## Step 3a: Reformat the transcript into a clean Google Doc and .md file

Raw transcripts (whether pulled from Zoom, Riverside, or a .txt file Neil has
already dropped in the session folder) come as a wall of `Speaker (mm:ss.mmm)`
headers followed by unbroken paragraph text. Always clean this up into two
files, saved in the session folder alongside the recording link:

1. **A `.md` file** named `[Interviewee] Ch[x] Transcript.md` — speaker names in
   markdown bold (`**Speaker**`) with the timestamp alongside, a blank line,
   then the turn's text as a paragraph. Add a one-line H1 title and a short
   context line (who's interviewing whom, platform, date, duration) at the top.
   Upload via the Drive file-creation tool with `contentMimeType: "text/markdown"`
   and `disableConversionToGoogleType: true` so it stays a real .md file rather
   than being converted.
2. **A native Google Doc** with the same content and title (no `.md` extension),
   built the same way as the briefing doc: upload markdown content via
   `contentMimeType: "text/markdown"` (conversion enabled, i.e. omit
   `disableConversionToGoogleType`) so Drive auto-converts it into a proper
   Google Doc with heading/bold formatting intact — this is far more reliable
   for a long transcript than hand-building HTML paragraph by paragraph.

When decoding transcript content pulled via a Drive read tool, check whether
the returned content is base64-encoded before treating it as plain text —
some large text-file reads come back base64-wrapped, and writing that
undecoded produces a garbled file.

Always paste the FULL transcript content into both files — never truncate,
summarize, or leave a placeholder note pointing at "the other file" partway
through. Verify each file after creating it by reading back its size/content
snippet; a suspiciously small result (a few dozen bytes on a file that should
be tens of thousands) means the upload didn't actually carry the content and
needs to be redone.

Link both files from the editor briefing doc's top section (see Step 2's body
structure) so the editor can open whichever format they prefer.

## Step 3b: Propose chapter titles

Every briefing carries a chapter title proposal in its Titles section — for a
Child Briefing or a Wrap Up session this is a fixed formula, for a Parent
Session it's a set of creative options pulled from the transcript for Neil to
choose between.

If Step 3 couldn't get a transcript (Riverside without Chrome access, and Neil
hasn't supplied one manually), skip this step for a Parent Session (leave the
Titles section in the doc as "TBC", flag it in Step 7) — but a Child Briefing or
Wrap Up title doesn't need the transcript at all, since it's a fixed formula;
fill those in regardless.

**Child Briefing** — apply this fixed formula directly, no creative proposals
needed:

```
Ch[x]. [Child First Name] & The Old Man
```

Use "& The Old Man" when the project is about Dad, "& Mum" when it's about Mum
(see Inputs needed — confirm which if it isn't already obvious). This single
line goes straight into the Titles section of the doc created in Step 2,
replacing "TBC" — it's
not a set of options, since there's only one child and one answer.

**Wrap Up session** — this is always the family's final chapter, closing out
after every child and the parent have been recorded. Apply this fixed formula,
no creative proposals needed:

```
Ch[x]. Wrap Up & Reflections
```

Neil has also used "Family Wrap Up & Reflections" for this same chapter in past
briefings — either wording is fine; default to the plainer "Wrap Up &
Reflections" unless Neil says otherwise for a given family. Like the Child
Briefing case, this is a single fixed line straight into the doc's Titles
section, not a set of options.

**Parent Session** — parent sessions run ~2hrs and the editor splits them into
2 chapters of roughly an hour each; the exact cut point isn't finalised until
they edit, so treat the transcript as one continuous conversation and propose
titles for a natural first-half / second-half split, using whichever two
chapter numbers apply to this session (e.g. "Ch3" and "Ch4"). For **each** of
the two chapters, propose **3-4 title options** in Neil's house style. Read
`references/chapter-title-style-examples.md` in full before generating — it
has the complete rule set and real worked examples from Neil's own
"Audiobook Chapter Title Creator" project; the summary below is not a
substitute:

- Format: a comma-separated string of short beats, ending "& [Last Beat]" —
  a short word/phrase + short word/phrase + ampersand rhythm on the final pair
- 10 words max per title
- Beats run in chronological order of when they came up in the transcript
- Cover the full chapter: aim for a beat from the beginning, middle, and end,
  but let the strongest story in the chapter decide the actual weighting —
  don't force even spacing across the three
- 1-2 alliterative pairs read well; don't force alliteration throughout
- Verbatim words/phrases from the transcript are great (they carry the
  interviewee's own voice) but use them sparingly: at most 1 verbatim phrase
  across the whole set of titles proposed in this briefing, never more than 2
  in any single title
- Under each option, add a one-line reasoning note — succinctly, what story
  each beat refers to, so Neil can pick without re-reading the transcript

Take your time on this — read the full transcript before drafting, don't
skim for keywords.

Write the chosen titles (or the options, for a Parent Session) into the
Titles section of the briefing doc created in Step 2, replacing the `Ch[x]
TBC` placeholders.


## Step 4: Update the Airtable Editor Pipeline

Base: **M&MOM Database**, table: **Editor Pipeline**. Find the row matching the
family name + interviewee + session type (e.g. Family Name = "Kumar", Interviewee =
"Jim", Session Type matching the chapters/session you're briefing).

Update:
- **Status** → `To Edit` (it was previously `To Schedule`, `To Record`, etc. —
  moving to "To Edit" reflects that the editor now has what they need). When
  writing to this field via the Airtable update tool, pass the option's plain
  name as a string (e.g. `"To Edit"`), not an `{id: ...}` object — the field
  update fails to parse otherwise.
- **Onboarding** → `TBC` if it's currently blank (this field tracks onboarding
  status separately and defaults to TBC once a session enters the pipeline)

If you can't find a matching row, don't create one blind — tell Neil so he can
check the family/session naming in Airtable. Note: Airtable's Session Type field
uses generic labels like "2hr Parent S1/S2/S3", not chapter numbers — a session
Neil describes by chapter (e.g. "Ch3&4") may map to "2hr Parent S1" in Airtable.
If the Drive folder naming and Airtable session dates/types don't obviously agree
with what Neil described (e.g. the row's logged Session Date is a different day
than the actual recording), don't block on it — update the row that matches on
family + interviewee + session type, and flag the date mismatch to Neil in
Step 7 rather than guessing which row to update or skipping the update entirely.

## Step 5: Check for an interviewer briefing

This step only produces a document in two situations: the session you just
briefed was the **last child in the family** to be recorded, or it was **any
parent session that isn't their last** (S1, S2, S3, and so on — not just S1).
Work out which (if either) applies, then build the matching briefing
automatically — don't ask Neil first, just do it and tell him in Step 7. If
Neil tells you a separate Interview Briefing for this exact session was
already created independently (e.g. earlier the same day), skip this step —
don't duplicate it. If Neil explicitly says not to build it yet (e.g. because
another child hasn't been interviewed yet even though Airtable/Drive suggest
this is the last one), skip it and say so plainly in Step 7 — don't second-guess him.

### Case A: This was the last child session in the family

Check both places, since either alone can be stale:

- **Airtable**: pull every Editor Pipeline row with the same Family Name. Look
  at the children (Parent/Child or Session Type will tell you who's a child vs
  a parent) and check whether all of them now have a session recorded/briefed
  (Status of `To Edit` or further along, not still `To Schedule`/`To Record`).
- **Drive**: check the `Editing - [Family]` folder for a session folder + editor
  briefing doc for each child. If a child has no folder yet, they haven't been
  recorded, so this isn't the last one.

Only proceed if both checks agree every child is done. If they disagree (e.g.
Airtable shows a child still "To Record" but there's a Drive folder for them, or
vice versa), don't guess — flag the mismatch to Neil in Step 6 instead of
building the briefing.

If this genuinely is the last child session:

1. Gather the transcripts for **every child's** session in this family (you
   should already have this one from Step 3; find the others in their
   respective session folders — download them the same way if they weren't
   already saved there).
2. Read through all of them and pull out, in chronological order of the
   **parent's life** (not the order kids mentioned things):
   - Key life stages the children shared stories or memories about
   - Things the children said they want to know about the parent's life —
     tag each bullet with which child said it, e.g. `(Priya)`
   - Verbatim questions the children asked or said they'd want asked — quote
     these directly, don't paraphrase, and tag with the child's name
3. Create a Google Doc titled `YYYYMMDD Interview Briefing [Parent Full Name]`
   (use today's date) and save it in the **parent's Session 1** Drive folder —
   create that folder now if it doesn't exist yet, following the same naming
   convention as the child folders.
4. Structure the doc with three sections matching the bullets above: "Key Life
   Stages", "Things The Kids Want To Know", "Questions From The Kids".

### Case B: This was any parent session (S1, S2, S3...) that isn't their last

This applies after every parent session except the final one in the family's
plan — not just S1→S2. Work out the next session number as this session's
number + 1.

1. Take this session's transcript from Step 3.
2. Write a follow-up briefing for the next session that builds on whatever
   Interview Briefing already exists for *this* session (read it first so
   you're not repeating ground already flagged — e.g. before writing the S3
   briefing, read the S2 briefing that was used going into this recording)
   covering, in bullets:
   - Key stories the parent shared in this session
   - Where the conversation left off / what was cut short by time
   - 3 suggested "rewind" questions — things to circle back to that deserve
     more depth
   - Areas the children flagged interest in (from the original Case A
     briefing, if one exists) that still haven't been reached
3. Create a Google Doc titled `YYYYMMDD Interview Briefing [Parent Full Name]
   S[next]` and save it in the **parent's next-session** Drive folder — create
   that folder now if it doesn't exist yet, checking first whether it already
   exists under a name you haven't matched yet (e.g. `Ch7 & 8 [Name]` might
   already exist as the S3 folder even without an explicit "S.3" suffix) so
   you don't create a duplicate.

## Step 6: Draft the Gmail handoff to the assigned editor

This step always runs — don't ask Neil first, just draft it and mention it in
Step 7. Read `references/editor-contacts.md` for the recipient address and
email style rules, matched against the `Editor` value on the Airtable row you
updated in Step 4.

1. Resolve the editor's real email address from `editor-contacts.md`. If the
   name isn't listed there, search recent Gmail thread history for that
   editor's name in past briefing-handoff subject lines to find their address
   — don't guess an address from a name pattern. Watch for name collisions:
   Neil has both editors and unrelated clients/interviewees who can share a
   first name (e.g. an editor "Jody" vs. a client "Jodie Taylor"), confirm
   the address by checking it against actual past briefing threads to that
   exact address before using it.
2. Follow that editor's saved style exactly, including whether a rate and/or
   deadline should be quoted. Link the Step 2 briefing doc using "here" or
   "is here" as the link text, matching Neil's established pattern — don't
   restate the full briefing content in the email body.
3. **All editor rates are always quoted in GBP (£) — never USD, and never any
   other currency, regardless of how the editor's own rate card is
   denominated.** Some rate cards (e.g. Abhi's) are written primarily in USD
   with a GBP equivalent alongside — always use the GBP figure from those
   cards, never the USD one. If a rate card only lists USD with no GBP
   equivalent given, don't guess a conversion — flag this to Neil in Step 7
   and ask him to confirm the GBP figure before it's used again.
4. **Build the email as real HTML with a genuine hyperlink — never plain
   text with a raw URL pasted in.** Call `create_draft` (and `update_draft`
   if revising) with the `htmlBody` field, and put the doc link on an actual
   `<a href="...">here</a>` tag around the word "here"/"is here" — e.g.
   `<p>Colin Best S1 - Ch3 &amp; 4 briefing is <a href="https://docs.google.com/document/d/...">here</a>.</p>`.
   Do **not** use the plain-text `body` field for the message content: Gmail's
   compose UI will auto-linkify a bare URL dropped in plain text into a long
   wrapped `https://www.google.com/url?q=...` redirect link, which is exactly
   the broken look Neil doesn't want. If a tool only accepts a single `body`
   field, write real `<a href="...">text</a>` markup into it rather than a
   plain-text link. Never paste a raw or wrapped URL into the visible email
   text — the URL only ever belongs inside an `href`.
5. Create the email as a **Gmail draft only** — never send it. Neil reviews
   and sends himself.
6. If the assigned editor has no saved style in `editor-contacts.md` and no
   usable history in Gmail, draft a minimal version (greeting, doc link,
   "Please confirm receipt.", sign-off) and flag in Step 7 that this editor
   has no saved style yet, so Neil can confirm and it can be added.

## Step 7: Confirm with Neil

Summarize what was created/updated: the doc link, the Drive folder link, the
transcript Google Doc + .md links, whether the recording link needs to be
added by hand (Riverside without Chrome access), the music tracks used (or
left TBC), the Airtable status change (and any date/naming mismatch flagged),
the Gmail draft created (recipient + subject), and — if applicable — the
interviewer briefing you built (or the mismatch you flagged, or that Neil
asked to hold it back). Keep this short — a few lines, not a report.