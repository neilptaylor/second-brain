---
name: editor-pipeline-session-logger
description: Logs new Calendly 1hr Child Briefing / 2hr Parent Life Story Recording bookings into the Editor Pipeline Airtable, filling in real dates on the TBC placeholder rows the new-client skill created.
---

You are checking Neil's Gmail for new Calendly recording-session bookings and logging the real dates into his Editor Pipeline Airtable.

## 1. Find matching emails
Search Gmail (search_threads on connector ffce937d-12cb-4a5b-bc52-2321647acf20) with:
`from:notifications@calendly.com (subject:"1hr Child Briefing" OR subject:"2hr Parent Life Story Recording") newer_than:1d`
Only process emails whose subject starts "New Event:" — ignore "Canceled:" and "Updated:" subjects (those are reschedules/cancellations, not new bookings; leave them for Neil to handle manually since this task doesn't yet handle rescheduling).

For each matching thread, call get_thread (messageFormat FULL_CONTENT) to get the full body.

## 2. Extract from the email body
- Invitee Name (from "Invitee:") — the last word/token is normally the family surname, e.g. "Geoff Griffiths" → family "Griffiths". Use judgement for multi-word surnames.
- Event Type: "1hr Child Briefing" or "2hr Parent Life Story Recording" (from "Event Type:")
- Event Date/Time (from "Event Date/Time:", e.g. "11:00 - Friday, 14 August 2026") — convert to an ISO datetime

Note: for "1hr Child Briefing" events the invitee is often a parent/guardian booking on behalf of a child, not the child themselves — don't assume the invitee name is the interviewee.

## 3. Match to an existing Airtable pipeline row (fill in, don't duplicate)
Airtable base "M&MOM Database" (baseId app077Z4RXX1PShzN), table "Editor Pipeline" (tableId tblWkRNY5rcvthBMs). Field IDs:
- fldfvHJsC7EILNfpr Family Name
- fldvMQG55QBjefTeB Interviewee
- fldO9gjgDbql5WTxC Session Type ("1hr Child Briefing" / "2hr Parent Life Story Recording" / "Wrap Up" / "Other")
- fldBeVYeozSiPiewg Session Label (S1/S2/S3, blank for children)
- fldvpwgWDhllOGcFI Status (TBC / Scheduled / Recorded / Cancelled)
- fld45cYDJmVOHqsUN Session Date (dateTime)
- fldb3hwVVXTrSJDe5 Editor
- fldXvqZ69gzIsTUok Notes

Call list_records_for_table filtered to Family Name = the extracted surname. Among the results, find records with Status = "TBC" and matching Session Type. If more than one (e.g. S1/S2/S3 all still TBC), pick the one with the earliest Session Label (S1 before S2 before S3; blank/unlabeled first if none are labeled). Update that record: set Session Date to the extracted datetime and Status to "Scheduled" (use update_records_for_table).

If no TBC record matches (family not pre-logged by the new-client skill, or all placeholders already filled), create a new record instead: Family Name, Session Type, Session Date, Status "Scheduled", and a Notes value of "No matching TBC placeholder found — created directly from Calendly booking, please verify Interviewee/Session Label." Leave Interviewee and Session Label blank in this case rather than guessing.

## 4. Report
Summarize what was processed this run: how many matching emails found, how many existing TBC rows updated (family + session type + record ID), how many new rows created because no placeholder matched (flag these clearly since they need Neil's review), and how many were skipped as duplicates/already-scheduled. If no matching emails were found this run, just say so briefly — don't produce a verbose report for a no-op run.

## Notes
- Don't mark emails as read or otherwise modify the Gmail thread — there are no label-write permissions available to this task (same constraint as discovery-session-crm-logger).
- The Editor Pipeline Google Sheet is no longer the target for this automation — Airtable is now the source of truth for upcoming session dates, per Neil's decision on 2026-07-24. Do not attempt to write to the Google Sheet.
- There is also an old, unused "Families (Production)" / "Production Tasks" system in the same Airtable base. Neil doesn't use it (built by a prior Claude session, doesn't match his workflow) — ignore it entirely, do not read from or write to it.