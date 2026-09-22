---
name: fathom-transcript-filer
description: Check Gmail for new Fathom call recap emails and file BOTH the summary (Google Doc) and the full transcript (Markdown) into the matching Google Drive Sales Call folder.
---

You are running an automated task. Follow these steps exactly with no user interaction. Do not ask questions. Take the write actions described below (they are the point of the task).

## What this task must produce, per call
For every new Fathom call, TWO files land in the client's Sales Call subfolder:
1. `Fathom Summary — [Full Name] — [YYYY-MM-DD]`  -> Google Doc, structured summary
2. `Fathom Transcript — [Full Name] — [YYYY-MM-DD].md`  -> Markdown file, FULL verbatim transcript

Historically this task only produced file 1. File 2 is mandatory now — the recap email never contains the transcript, so it MUST be pulled from the Fathom MCP.

## STEP 1 — Find new Fathom recaps in Gmail
`mcp__ffce937d-12cb-4a5b-bc52-2321647acf20__search_threads` with query:
`from:no-reply@fathom.video subject:Recap newer_than:3d`
Collect thread IDs + subjects.

## STEP 2 — For each thread
a) `get_thread` (messageFormat FULL_CONTENT) for the full body.
b) Participant name = the person who is NOT Neil Taylor (from the "X and Neil Taylor" line or the meeting title).
c) Meeting date (subject or body) -> `YYYY-MM-DD`.
d) Grab the Fathom call URL from the email body — the "View recording" / "View Meeting" link, form `https://fathom.video/calls/<id>` (may carry `?tab=summary`).

## STEP 3 — Resolve the Fathom recording
- `mcp__a4f71cf3-69f5-41f4-896f-163dcdd00adc__get_recording_by_url` with the URL from 2d -> gives `recording_id`.
- If there is no usable URL in the email, use `mcp__a4f71cf3-69f5-41f4-896f-163dcdd00adc__search_meetings` (query = participant name, recorded_by = "anyone"), or `list_meetings` filtered to the date, and match on participant name + date.
- If you still cannot resolve it, continue with the summary only and flag it in STEP 6.

## STEP 4 — Find the matching Drive folder
- Sales Call parent folder ID: `1ba_mqJkb95u7l8aI2UMcGN4cGkuc1MF3`
- `mcp__04e9ba0e-2617-42ef-ae1a-45896d238f63__search_files` for a subfolder whose name contains the participant's first AND last name (titles look like `20260903 Matt Roberts`).
- If none exists: use `Unnamed Fathom Transcripts` inside the parent folder (create it, mimeType `application/vnd.google-apps.folder`, if missing).

## STEP 5 — File the two files (dedupe first)
Search the target folder for existing files whose name starts with `Fathom Summary` / `Fathom Transcript` AND contains this call's date. Create only the ones that are missing.

5a — Summary (Google Doc)
Build the summary from the recap email body with these sections: Meeting Purpose, Key Takeaways (3-5 bullets), Action Items (split Neil's vs client's), Topics Discussed, Next Steps.
`create_file`:
- title: `Fathom Summary — [Full Name] — [YYYY-MM-DD]`
- parentId: the folder from STEP 4
- contentMimeType: `text/markdown`  (let Drive convert to a Doc)
- textContent: the structured summary

5b — Transcript (Markdown file) — DO NOT SKIP
`mcp__a4f71cf3-69f5-41f4-896f-163dcdd00adc__get_meeting_transcript` with the `recording_id` from STEP 3 (pass `url` too, for timestamped links).
`create_file`:
- title: `Fathom Transcript — [Full Name] — [YYYY-MM-DD].md`
- parentId: the folder from STEP 4
- contentMimeType: `text/markdown`
- disableConversionToGoogleType: `true`   (keep it as a real .md file, not a Doc)
- textContent: a short header (participant, date, meeting title, recording URL) then the full transcript exactly as returned — no trimming, no summarising.

If STEP 3 failed, skip 5b and note it.

## STEP 6 — Report
Print, per call: participant, folder used, and which of {summary, transcript} were created / skipped-already-there / could-not-produce (with reason).
If a folder was missing, run:
`osascript -e 'display notification "No client folder for [name]" with title "Fathom filer" sound name "Glass"'`
If a transcript could not be resolved, run:
`osascript -e 'display notification "Transcript missing for [name]" with title "Fathom filer" sound name "Glass"'`

## Notes
- Neil's email: neil@meandmyoldman.co.uk
- Sales Call parent folder ID: `1ba_mqJkb95u7l8aI2UMcGN4cGkuc1MF3`
- Client subfolders are created by the `discovery-session-crm-logger` task (Mon/Wed) from the Calendly booking, so for a booked discovery call the folder should already exist by the time the recap email arrives.
- Idempotent: safe to run repeatedly — the date-based dedupe in STEP 5 prevents duplicates.
- Use the real current date at run time for dedupe, never a hardcoded value.