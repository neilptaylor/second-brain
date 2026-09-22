---
name: wrapup-date-watcher
description: Twice a week (Mon/Thu), scans Gmail for the "Family Wrap Up | [time] [date]" email Neil sends once a session is actually booked, and registers any new family directly into wrapup-brief-check's Known Families list.
---

You are checking Neil's Gmail, twice a week, for the moment a family's Wrap Up call gets booked — this is how new families enter the "wrapup-brief-check" pipeline.

Context: Neil runs an onboarding call with each new family, then books their Wrap Up call himself (sometimes that same hour, sometimes within ~24hrs) and sends the calendar invite/confirmation. The actual Wrap Up session then happens 6-12 weeks later. Because the lead time is so long, checking twice a week is plenty — no need to watch onboarding calls or run daily.

## 1. Find new "Family Wrap Up" booking emails
Search Gmail (search_threads on connector ffce937d-12cb-4a5b-bc52-2321647acf20) with:
`subject:"Family Wrap Up" newer_than:5d`
This catches both directions (Neil sending the announcement, or a calendar invite whose subject embeds the event title). Only process threads whose subject does NOT also contain "Reminder" — reminder emails ("24hr/48hr Homework Reminder | ...") are a later, separate nudge, not the original booking. The real signal looks like "Family Wrap Up | 0830 Wed 17 June" — an event confirmation Neil sends himself once the call is actually booked.

For each matching thread, call get_thread (messageFormat FULL_CONTENT) and extract:
- Family surname — from the toRecipients' names/addresses, or the salutation in the body (e.g. "Team Salvesen," / "Hello family,")
- Session date/time — parse from the subject (format is usually "Family Wrap Up | [HHMM 24hr] [Day] [D Month]") or, if ambiguous, from the body/calendar details. Note the timezone if stated.
- Every attendee email you can find in the thread (to/cc)

## 2. Register in wrapup-brief-check
Call list_scheduled_tasks to get the current content for taskId "wrapup-brief-check" (read the file at the path it returns). If this family is NOT already listed under "Known families" or "Historical families" in that file, call update_scheduled_task on taskId "wrapup-brief-check" with a prompt equal to the CURRENT full prompt content plus one new entry inserted under "## Known families" (same position/format as the existing entries), using this shape:

### [FAMILY]
- Session: [date], [time + timezone]
- Members: [whatever you found — names/roles/emails, or "not yet confirmed — check Gmail thread [id]"]
- Briefing doc ID: (not yet created — wrapup-brief-check will create it on first response)
- One-pager doc ID: (not yet created — wrapup-brief-check will create it on first response)
- Morning event: not yet created
- Status: newly registered [today's date] by wrapup-date-watcher, from booking email.

This must be a surgical edit — reproduce every other line of the file exactly as it was, do not reword or remove anything else, do not touch "Historical families" / "Already processed" / "Notes".

If the family IS already listed, skip it (already registered) — but if their recorded session date differs from what this email says, update just that family's "Session:" line (same surgical-edit rule) and note the correction in your report.

## 3. Report
Summarize: how many "Family Wrap Up" booking emails found this run, which families were newly registered (with date), which were already known, and any date corrections made. If nothing new, say so briefly — don't produce a verbose report for a no-op run.