---
name: handover-reminder-watcher
description: Daily: finds Calendly "The Handover 30mins" bookings ~48hrs out and drafts a priming reminder email in Gmail (never sends).
---

You are checking for Me & My Old Man (MMOM) handover calls coming up in roughly 48 hours, and drafting (never sending) a short priming email so the family arrives at the call ready.

Context: Neil books "The Handover 30mins" event (Calendly event type https://api.calendly.com/event_types/44f9086d-8936-4340-bb90-bd1c9e628e2d, slug thehandover-30min) with each family right at the start of their project — often 8-12 weeks before it actually happens. Because it's booked so far ahead, nobody reads the Calendly description by the time the call comes round. This task's job is a short reminder 48 hours before, so the family has thought ahead about (a) what each family member is comfortable sharing for consent, and (b) who else in their life might enjoy the same experience — NOT a form to fill in beforehand, just a heads-up so the live call moves faster.

## Step 1: Find upcoming Handover bookings

Call `meetings-list_events` on the Calendly connector (a0a8a416-4d7c-4f66-9323-904a97c35f78), filtering to event_type = "https://api.calendly.com/event_types/44f9086d-8936-4340-bb90-bd1c9e628e2d", status = active, min_start_time = now, max_start_time = now + 4 days (covers the 48hr window with slack for run-time drift).

For each event, compute hours until start. Keep events where start time is between 36 and 60 hours from now — this is the "due for a reminder" window given the task runs once daily.

## Step 2: Dedup

This file has a "## Sent log" section below. Each entry is `[Calendly event URI] — reminder drafted [date]`. Skip any event already logged there.

## Step 3: Get attendee details

For each new event due, call `meetings-list_event_invitees` to get names and emails. Extract the family surname from the invitee names or the event's own name/location field.

## Step 4: Draft the email

Use the Gmail connector (ffce937d-12cb-4a5b-bc52-2321647acf20), `create_draft`. To: the invitee email(s). Subject: "Excited for [Day] — quick heads up". Body (adapt names/date, keep the structure and tone, British English, no em dashes):

---
Hi [first names, comma separated],

Looking forward to our handover call on [day + date + time]. Wanted to give you a quick heads up on what we'll cover, so you can come ready:

1. The walkthrough — I'll show you everything: the audio documentary, the artwork, the "It's a Wrap" ebook. How to access it, download it, keep it safe.
2. A few quick questions about what you're comfortable sharing — nothing to prepare, just have a think as a family beforehand about what feels right to you.
3. A favour to ask — if this has meant something to you, I'll ask who else in your life might want the same experience.

Nothing to do beforehand except show up. See you then.

Neil
---

Do NOT send the draft. Drafting only — Neil reviews and sends himself, per standing instruction that client-facing sends always need his yes.

## Step 5: Log and report

Append `[event URI] — reminder drafted [today's date]` to the Sent log below via `update_scheduled_task` (taskId "handover-reminder-watcher"), reproducing the rest of this file exactly. Report which families got a new draft this run (name + call date), and which were already logged / skipped. If nothing due, say so briefly, no verbose no-op report.

## Sent log

(none yet)
