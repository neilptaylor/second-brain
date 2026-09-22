---
name: wrapup-brief-check
description: Tue/Thu 4pm: syncs Wrap Up session dates from Calendar for known families, checks for new homework responses (Sheet + Gmail), and updates briefing docs. New families are seeded by wrapup-date-watcher.
---

You are running an automated check for Me & My Old Man (MMOM). Check for new Wrap Up homework responses from Gmail and the Google Form, update the briefing docs in Google Drive, and create a Google Calendar reminder on the morning of each session (if it doesn't already exist).

Families enter this pipeline automatically: a separate scheduled task ("wrapup-date-watcher") scans Gmail twice a week for the "Family Wrap Up | [time] [date]" email Neil sends once a session is actually booked, and adds the family below under "Known families" directly from that email. You shouldn't need to go hunting through years of Gmail history for new families — if a family is missing and Neil confirms it's active, add them manually.

## Step 1: Sync session dates from Calendar (source of truth)

For each family listed under "Known families" below with a session date, search Google Calendar (list_events / search_events on connector 1cbe0d72-4187-49de-be4d-58fb3b395d3b) for their Wrap Up event to confirm the date/time is still correct. Reschedules happen (e.g. Salvesen moved from 17 Jun to ~24 Jun after a bad internet connection; Griffiths moved from 2 Sep to 15 Sep). If Calendar shows a different date/time than what's recorded here, that's the one to trust — update this file's entry via update_scheduled_task (taskId "wrapup-brief-check") before continuing, and flag the change in your final report. Don't RSVP or respond to any invite — read-only.

## Step 2: Check for new responses

### Google Form / Sheet
Sheet ID: 1NgxL3rw2tBXPwz-oIHqrZ-1W3DmmNnzHh-2fJbwXukc
Columns: Timestamp | Name | Role | Q1 (delighted/surprised) | Q2 (know more) | Q3 (experience) | Q4 (anything else) | Q5 (testimonial)
Match each row's name to a known family member to assign a family. Dedup key: form:[Timestamp]_[Name]

### Gmail replies
Search for emails TO neil@meandmyoldman.co.uk that are replies to Wrap Up / Homework Reminder threads, NOT from Neil, NOT system emails (Calendly, Zoom, Google Forms receipts, bounces).
Dedup key: email:[Gmail message ID]

## Step 3: Deduplication

Each family's briefing doc has a "PROCESSED RESPONSES (DO NOT EDIT)" block at the bottom. Read it. Skip any response whose key already appears there. After updating, append new keys to the block.

## Step 4: Check Drive for existing docs

Parent folder: 1bG1j428y4CVHr5X78NX6VIvOJmrnHVzF
Subfolder per family: [FAMILY NAME] Wrap Up Prep
Docs: "[FAMILY NAME] Wrap Up Prep — Briefing" and "[FAMILY NAME] Wrap Up Prep — For the Family"
If subfolder or docs don't exist yet for a new family, create them. Exception: if the family's session has already happened by the time they're activated (see Griffiths, Sep 2026), skip the "For the Family" doc — it's a pre-session agenda handout and has no use after the fact — but still build the Briefing doc for post-production reference, and skip Step 6 (morning-of event) since the date has passed.

## Step 5: If new responses found — update the docs

### Briefing doc (internal, "[FAMILY NAME] Wrap Up Prep — Briefing")

Structure per new response:
  **[FIRST NAME] ([ROLE])**
  *[One-sentence headline]*
  [Full answer]
  Key terms: **[bold 3–5 key words/phrases]**

Add under the relevant Q1–Q4 section. Append Q5 to the Testimonials section.
Update the "PROCESSED RESPONSES" dedup block.
Also update the header line "RESPONSES RECEIVED" and "STILL TO RESPOND" to reflect current state.

### Family-facing doc (shared with family, "[FAMILY NAME] Wrap Up Prep — For the Family")

Use this exact format and structure — do not use the old horizontal-line (─────) format:

```
Me & My Old Man

[Family Name] Family Wrap-Up
[Day] [Date] · [TIME]

Tonight's Plan

| 15 mins | Round the room — reflections on the recordings, what surprised you, what made you laugh |
| 40 mins | Dive into the stories we still want to hear — let it flow |
| 5 mins | Close & wrap |

What came through in your responses

— WHAT DELIGHTED / SURPRISED YOU?

  • [Name]: [synthesised bullet from their response]
  • [Name]: [synthesised bullet]
  • [Unnamed synthesised theme if shared across multiple people]

— WHAT DO YOU WANT TO KNOW MORE ABOUT?

  • [Name]: [bullet]

— HOW HAVE YOU FOUND THIS EXPERIENCE?

  • [Name]: [bullet]

— ANYTHING ELSE?

  • [Name]: [bullet]

See you at [TIME]! — Neil, Me & My Old Man
```

Rules for the family-facing doc:
- Agenda table always appears first, unchanged across families.
- Bullets are name-prefixed ("[First Name]: ...") when attributable to one person; unnamed for themes shared across multiple respondents.
- Keep bullets punchy and warm — first person voice stripped out, third-person observation.
- Do not include the raw Q5 testimonial text in this doc.
- Update synthesised bullets whenever a new response adds a meaningfully new theme.

## Step 6: Morning-of calendar event

For each active family, check whether a morning-of calendar event already exists by searching Google Calendar for events on the session date with the family name in the title. If none exists:
- Create a 30-min event at 08:00 CET (Europe/Paris) on the day of the session
- Title: "🎙️ [Family Name] Wrap Up — Session [Today/Tonight] [TIME]"
- Description: who responded, who's outstanding, links to both docs, 4–6 key themes from the briefing
- Reminders: popup at event start, email 60 minutes before

Only create this event once — skip if it already exists. Skip entirely if the session date has already passed by the time you're processing it (see Step 4 exception).

## Step 7: Alert Neil if new responses found

If new responses were processed, send a short email draft to neil@meandmyoldman.co.uk for each new respondent:
Subject: [Family Name] Wrap Up | New response from [First Name]
Body (3 lines):
[First Name] [Last Name] ([Role]) just sent their homework.
[X] of [Y] family members have responded.
Briefing updated → [Google Doc link]

If no new responses found, do nothing — no email, no noise.

## Known families (seeded automatically by wrapup-date-watcher — edit manually only if Neil tells you a family is missing or wrong)

### Salvesen
- Session: Wed 17 June 2026, 08:30 CET (rescheduled to ~24 Jun after connectivity issues — re-verify via Step 1)
- Members (4): Andrew (Dad), Angelica (Mum), Edo (Son), Hal (Son)
- Emails: AndrewSalvesen@findrack.co.uk, angelicasalvesen@gmail.com, edmundsalvesen@me.com, halsalvesen@hotmail.com
- Briefing doc ID: 1nCSSYjskFDzbQ-JdX6p9jshHpgaXofWdsPlJunAvnOc
- One-pager doc ID: 10JfSX6ANR_TOCzlVihYfxj3I9HKz2bu0cs_QGZ4meZU
- Morning event: already created ✓
- Status as of 2026-07-25: still 3/4 responded (Hal outstanding); session has passed, family is in post-production (editor Vuk Jankovic briefed).

### Cheyney
- Session: Tue 16 June 2026, 21:00 CET
- Members (4): Guy (Dad), Alex (Daughter), Lucy (Daughter), William (Son)
- Emails: gcglobal@btinternet.com (bounced), alexandra.cheyney@gmail.com, lucy@wildlulita.com, williamcheyney@yahoo.com
- Note: lucy@wildlulita.com = Lucy Cheyney (married name). Determine family from thread, not email.
- Briefing doc ID: 1qQG4jjdMyW_yrBV4QKwfkKyhKYS0usJcheOTWe3c-gw
- One-pager doc ID: 1vNeRKCfFh0_fbHS37V08ZiNZSDsK-NfW61CUhGIk9OQ
- Morning event: already created ✓
- Status as of 2026-07-25: still 2/4 responded (Guy, William outstanding); session has passed, family is in post-production.

### Griffiths
- Session: Tue 15 September 2026, 20:30 CEST/Europe-Oslo (rescheduled from originally booked Wed 2 Sep 2026, 11:30 UK — confirmed via Calendar 2026-09-20)
- Members (3 confirmed attendees of 6 possible spots): Vaughan Griffiths (Dad, info@corecollective.uk), Geoff Griffiths (Child, hello@geoffgriffiths.co.uk / geoffmarkgriffiths@gmail.com), Nicola Griffiths / Nicola Smith (Child, nicola@griffiths-psychology.co.uk)
- Briefing doc ID: 1OOxM0q9QDDRHP81ORVnekAsIQ6S9rbGei9SxYm8xVis
- One-pager doc: not created — session already happened by the time this family was activated (all 3 form responses landed 10–15 Sep, discovered by this task on 2026-09-20), so the pre-session "For the Family" agenda doc would serve no purpose. See Step 4 exception.
- Morning event: not created — session date had already passed when discovered. See Step 6.
- Status as of 2026-09-20: 3/3 confirmed attendees responded (Vaughan, Geoff, Nicola); session has passed, family is in post-production (Ch9 already briefed to editor Abhi Pawar per Gmail 16 Sep 2026).

### Taylor (watchlist — not yet active)
- Session: "1h30 Family Wrap Up & Reflections", currently booked Mon 24 Aug 2026, 18:00 UK / 19:00 CET (3 of 5 spots filled as of 2026-07-13 — date/attendees may still shift; re-verify via Step 1)
- Members expected (5 spots): Carl Taylor (carltaylor95xf@hotmail.co.uk), Jodie Taylor (hello@jodie-taylor.com), Maggie Taylor (mtaylor1958@hotmail.co.uk, mum), Phil Taylor (dad, email not yet seen), + 1 more
- Status: individual Child Session prep is ongoing (24hr/48hr Homework Reminder emails to Carl/Jodie). No Wrap Up homework (the 5-question sheet in Step 2) has been requested yet; expected ~48hrs before the 24 Aug session (~20-22 Aug 2026). NOTE: this booked date (24 Aug 2026) has now passed (today is 2026-09-20) with no Sheet/Gmail responses seen for this family and no "Family Wrap Up | [time] [date]" registration from wrapup-date-watcher — re-verify with Neil whether this session happened, was rescheduled, or fell through.
- Action: do NOT create briefing docs or calendar event yet. Once Wrap Up homework reminders start going out and/or responses land in the Step 2 sheet, treat as newly active — create the "Taylor Wrap Up Prep" folder/docs per Step 4 and follow the normal flow.

### Best (watchlist — onboarding call pending as of 2026-07-25)
- Status: Neil's next onboarding call is with the Best family. Their Wrap Up call isn't booked yet — expect the "Family Wrap Up | [time] [date]" booking email either within the same hour as the onboarding call or within ~24hrs after, which wrapup-date-watcher will pick up on its next twice-weekly run and register properly (with real session date, members, emails).
- Action: do NOT create briefing docs or calendar event yet — wait for wrapup-date-watcher to register this family with a real date. Re-check status with Neil if this stays stale much longer — the onboarding call may already have happened.

## Historical families (pre-dates this system — do not process)
Many other "Homework Reminder" / "Family Wrap Up" threads exist in Gmail going back to Jan 2025 (Marsh, Norman/Alison-Jill-Tim-David, Pinkham, Josephides, Smith, Bortner, and others) and their responses sit unprocessed in the Step 2 sheet. No Drive folders exist for any of them — only families explicitly listed above have ever been tracked. Do not backfill these — filter out any thread/response tied to a family surname other than one listed above unless Neil explicitly asks to onboard it.

## Known pipeline gap — Beard family (flagged 2026-09-20)
The Beard family (Richard Beard, dad; Daniel Beard, son) went through a full Wrap Up cycle — Sheet responses from Richard and Daniel (submitted twice) landed 15–16 Sep 2026, the Wrap Up call was recorded on Zoom 17 Sep 2026, and the session was already briefed to editor Abhi Pawar (Ch9) by 16-17 Sep — without ever being registered in this task's "Known families" list. wrapup-date-watcher never picked them up, likely because their Wrap Up call wasn't booked via the standard Calendly "Family Wrap Up | [time] [date]" flow this task watches for (it may have been arranged directly, outside Calendly).
Since their session has already happened and been fully handed to production, there's no retroactive value in building "Wrap Up Prep" docs or a morning-of reminder for them now. Do not add Beard to Known Families or backfill docs unless Neil says otherwise.
Action needed from Neil: none required, but worth knowing wrapup-date-watcher has a blind spot for Wrap Up calls booked outside the standard Calendly flow — future families booked the same way (direct Zoom/manual scheduling) will need to be added manually.

## Already processed (never reprocess these)
- form:14/06/2026 18:33:31_Andrew Salvesen
- form:14/06/2026 18:47:53_Angelica
- email:19eb160fb2402590 (Edo Salvesen)
- email:19ec4fa33b4855aa (Alex Cheyney, for all 3 children)
- form:14/06/2026 22:00:02_Lucy Cheyney
- form:15/06/2026 11:26:18_Angelica (Salvesen 2nd form entry — Q2 marriage addition; draft alert sent to Neil 2026-07-01)
- email:19ec09ddd2971104 (Lucy Cheyney email reply June 13 — clearer Q1 + Q4 guardedness; draft alert sent to Neil 2026-07-01)
- form:15/09/2026 20:25:56_Vaughan Griffiths
- form:14/09/2026 15:34:52_Geoff Griffiths
- form:10/09/2026 20:56:45_Nicola Smith (Griffiths)

## Notes
- Neil's email: neil@meandmyoldman.co.uk
- Drive parent folder: 1bG1j428y4CVHr5X78NX6VIvOJmrnHVzF
- Calendar timezone for morning events: Europe/Paris (CET/CEST)
- New-family discovery is handled entirely by the "wrapup-date-watcher" scheduled task (Mon/Thu Gmail scan for the booking email), not by this one — this task only maintains families already listed under "Known families" above. But see the Beard gap above: that discovery method has a blind spot for Wrap Up calls booked outside the standard Calendly flow.
