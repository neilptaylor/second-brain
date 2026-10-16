# Handover: Calendly slots for Brownie, 7 Oct 2026

## The ask

Neil wants to send Brownie two Thursday slots and two Friday slots on the 20min discovery call, in Berlin time (CEST, Neil's Calendly timezone):

- Thursday 8 Oct: 16:00 and 16:30
- Friday 9 Oct: 17:00 and 17:30

He opened the hours up, but they do not show on the public link for "20min Family Story Discovery Session": https://calendly.com/meandmyoldman/20min-family-story-discovery-session

Event type URI: `https://api.calendly.com/event_types/bc521e38-0948-4bf3-9579-235aa7a14bb5`
User URI: `https://api.calendly.com/users/8898a933-2d57-4c13-82bc-2d44df737361`

## What we found

- That event type uses its own schedule, not "Working hours (default)". Its weekly hours were Thursday 12:00 to 16:30 and Friday 10:00 to 12:00, with no 8 or 9 Oct date rows.
- Neil's exceptions are on "Working hours (default)": Oct 8 12:00 to 18:00, Oct 9 10:00 to 12:00 and 14:00 to 18:30. That schedule is only active on 6 event types, so they never reached this one.
- Friday is now sorted (Neil's words). Thursday is not.
- Meeting limits: none set (Scheduling settings > Advanced availability). Ruled out.
- Orange Google Calendar events do not block Calendly. Only blue ones do. Ruled out.
- Thursday busy times from the API were only 13:30 to 15:00 Berlin, so the calendar is not what hides 16:00 to 18:00.
- When I read the slots earlier, Thursday showed nothing at all, while Friday showed 10:20 and 10:40 Berlin. That fits a minimum scheduling notice of about 24 hours: Thursday 16:00 is roughly 20 hours away, Friday 10:20 is roughly 38 hours away.
- Friday 17:00 may stay hidden: a Calendly meeting at 16:00 to 16:45 Berlin has a buffer to about 17:15. 17:30 should be fine.

## Most likely fix (not yet done)

Open the event type in Calendly > Availability (or Scheduling > "Date range / minimum notice") and reduce the minimum scheduling notice to a couple of hours, or switch the event type to "Working hours (default)". Neil is checking the notice setting.

## Left over

- A single-use share link I created (https://calendly.com/d/dtfb-3dj-r68) shows "No times in October". It does not work. Do not send it.
- A second share link attempt was never created (the safety check errored). Nothing else was changed in Calendly.
- Once the notice is fixed: read available times for the event type for 8 and 9 Oct with `event_types-list_event_type_available_times`, and send Neil the per-slot `scheduling_url` links for Brownie. Those direct links are the "invite" he asked for.

## Why my Calendly calls were failing

Not Calendly. The error was "auto mode classifier gave no verdict": the permission check that approves each tool call timed out on its side. It is transient. The earlier calls in this session worked, so a fresh session should be fine.
