---
name: onboarding-call-followup-scheduler
description: Watches Gmail for new "1hr Family Onboarding Call" Calendly bookings and schedules two one-time follow-up checks (2hrs and 1 day later) that log real session dates into the Editor Pipeline Airtable — replaces the old daily poll since Calendly session invites only appear right after an onboarding call, not every day.
---

You are watching Neil's Gmail for newly-booked "1hr Family Onboarding Call" Calendly events, and scheduling short-lived follow-up checks after each one — rather than polling every day for session bookings that only actually appear right after an onboarding call.

## 1. Find new onboarding call bookings
Search Gmail (search_threads on connector ffce937d-12cb-4a5b-bc52-2321647acf20) with:
`from:notifications@calendly.com subject:"1hr Family Onboarding Call" newer_than:8d`
This event type's booking-confirmation subject looks like "[Name] is attending 1hr Family Onboarding Call - [time] [date]" — only process subjects containing "is attending" (a new booking). Ignore subjects indicating a cancellation or reschedule.

For each matching thread, call get_thread (messageFormat FULL_CONTENT) to get the full body, and extract:
- Invitee Name (the family — take the surname)
- Event Date/Time (from "Event Date/Time:") — convert to an ISO datetime with the Europe/London offset

## 2. Dedupe — don't reschedule a follow-up twice for the same booking
Call list_scheduled_tasks. Build a deterministic taskId per booking: `pipeline-check-<family-surname-lowercase-no-spaces>-<YYYYMMDD-of-the-onboarding-call>-2h` and the `-1d` variant. If a task with that exact taskId already exists in the list (regardless of enabled/fired state), skip that booking entirely — it's already been handled.

## 3. Schedule the follow-up checks
For each new, undeduped booking, compute two target times: the onboarding call's Event Date/Time + 2 hours, and + 1 day. For each target time that is still in the future, call create_scheduled_task with:
- taskId: the deterministic id from step 2
- fireAt: the target ISO datetime
- description: "Check for [Family]'s recording session bookings after their onboarding call"
- notifyOnCompletion: false
- prompt: the exact block below, with [FAMILY] replaced by the extracted surname —

---
You are checking Neil's Gmail for [FAMILY]'s new Calendly recording-session bookings (following their onboarding call) and logging the real dates into his Editor Pipeline Airtable.

Search Gmail (search_threads on connector ffce937d-12cb-4a5b-bc52-2321647acf20) with:
`from:notifications@calendly.com (subject:"1hr Child Briefing" OR subject:"2hr Parent Life Story Recording") newer_than:3d`
Only process emails whose subject starts "New Event:". For each match, call get_thread (FULL_CONTENT) and extract Invitee Name, Event Type, and Event Date/Time (convert to ISO). Only act on invitees whose surname matches [FAMILY] (loosely — the invitee may be a parent/guardian booking on behalf of a child, so match on surname, not full name).

Airtable base "M&MOM Database" (baseId app077Z4RXX1PShzN), table "Editor Pipeline" (tableId tblWkRNY5rcvthBMs). Field IDs: fldfvHJsC7EILNfpr Family Name, fldvMQG55QBjefTeB Interviewee, fldO9gjgDbql5WTxC Session Type, fldBeVYeozSiPiewg Session Label, fldvpwgWDhllOGcFI Status, fld45cYDJmVOHqsUN Session Date, fldb3hwVVXTrSJDe5 Editor, fldXvqZ69gzIsTUok Notes.

Call list_records_for_table filtered to Family Name = [FAMILY]. Among records with Status "TBC" and matching Session Type, pick the one with the earliest Session Label (S1 before S2 before S3; unlabeled first if none labeled) that has no Session Date yet. Update it: set Session Date to the extracted datetime and Status to "Scheduled" (update_records_for_table). If no TBC record matches, create a new record instead (Family Name, Session Type, Session Date, Status "Scheduled", Notes "No matching TBC placeholder found — created directly, please verify Interviewee/Session Label").

Don't touch the Editor Pipeline Google Sheet — Airtable is the only automated write target, the Sheet stays a manual-glance table Neil updates himself. Don't touch the old unused "Families (Production)" / "Production Tasks" Airtable tables. Don't mark Gmail threads as read.

Report briefly: how many bookings found for [FAMILY], how many Airtable rows updated vs. created fresh, and flag anything ambiguous.
---

If BOTH target times for a booking are already in the past when you find it (e.g. the onboarding call happened more than a day ago before this watcher first saw it), don't schedule anything — instead just run the scan-and-log logic above yourself, right now, inline, for that family.

## 4. Report
Summarize: how many new onboarding-call bookings found this run, which follow-up checks got scheduled (family + fire times), which were skipped as duplicates, and which were handled inline because both target times had already passed. If nothing new was found, say so briefly — don't produce a verbose report for a no-op run.