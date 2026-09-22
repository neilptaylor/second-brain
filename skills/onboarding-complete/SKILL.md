---
name: "onboarding-complete"
description: "Runs the wrap-up after a family's 1hr Family Onboarding Call at Me & My Old Man. Drafts the \"everything you need to know\" welcome email (Gmail draft, never sent), builds the family's Google Drive folder structure, and logs their confirmed sessions in Airtable with real dates. Trigger when Neil says \"onboarding complete for [family]\", \"send the everything you need to know email for [family]\", \"wrap up onboarding for [family]\", or names a family that just had their onboarding call and wants the welcome email/folder/pipeline set up. Distinct from the `new-client` skill, which builds the *editor* folder tree before a client has even booked — this skill runs after the client-facing onboarding call, builds the *family's own* Drive folder (trees/guides/photos/stories/mementos), and produces the welcome email, not an editor briefing."
---

<![CDATA[<!-- v1.3 — 2026-08-13: fixed family folder location — must go directly in the Shared Drive root (0ALiqx6MMMJj3Uk9PVA), not a My Drive "Families" folder; added mandatory Content Manager / sharing-permissions flag to Step 6 since the Drive tool can't set permissions itself -->

---
name: "onboarding-complete"
---

# Onboarding Complete — Welcome Email, Family Folder & Pipeline Log

After Neil runs a family's 1hr Family Onboarding Call (booked via Calendly),
three things need to happen: the family gets a personal "everything you need
to know" email with their session times and homework links, they get a
shared Drive folder to hold their family tree/photos/stories, and their
confirmed sessions get logged into the Airtable Editor Pipeline with real
dates. This skill does all three from one trigger.

## Inputs needed

Before starting, confirm you have:

1. **Family surname** (e.g. "Griffiths", "Best")
2. Optionally the parent's/interviewee's first name if Neil gives it, to
   disambiguate if there are two families with the same surname

If the surname is ambiguous or not given, ask — don't guess which family
just onboarded.

## Step 1: Identify the family and their emails (Airtable is canonical)

Search the Airtable base **M&MOM Database** (`app077Z4RXX1PShzN`), table
**Full CRM**, view **Won - Recent**, for rows matching the family surname.
This is the fastest and most reliable source for names and emails — trust it
over Calendly invitee names, which can be stale (e.g. a daughter's maiden
name vs. married name).

Collect for every family member found:
- First name, last name (as recorded in Airtable — this is the name to use
  in the email and folder, not whatever name appears on the Calendly invite)
- Email address

If the family isn't in Airtable yet, or a member is clearly missing (e.g.
the onboarding call had 3 attendees but only 2 rows exist), fall back to
searching Gmail for the "1hr Family Onboarding Call" Calendly confirmation
thread for that surname to fill the gap — then flag to Neil that Airtable is
missing that person so he can add them.

Use whatever short first name/nickname Neil or the family actually use in
correspondence (e.g. "Liz" not "Elisabeth" if that's how she signs emails or
appears in Calendly) for the email greeting and body — Airtable is canonical
for matching the *record*, but the email should read the way Neil actually
talks to them. If unsure which form to use, default to the Calendly invitee
name since that's what the family sees on their own bookings.

## Step 2: Find all their sessions (Calendly)

Search Calendly (`meetings-list_events` / `list_calendly_skills` tools, or
the connector search) for every booking involving these family members —
match by attendee email from Step 1, not just name, since Calendly session
titles are generic ("1hr Family Onboarding Call", "2hr Parent Life Story
Recording", "1hr Family Wrap Up & Reflections", "The Handover"). Look across
the full booking history, not just upcoming — the sequence typically runs:

- Child Briefing(s) — one per child
- Parent Life Story Recording(s) — 2hr each, one per planned session (S1,
  S2, S3...)
- Family Wrap Up & Reflections
- The Handover

For each session found, get the date/time **converted into that attendee's
own local timezone** (Calendly's invitee details show each invitee's
timezone — use it; don't assume everyone is on Neil's UK time). If a session
isn't booked yet, list it as TBC rather than omitting it.

## Step 3: Draft the welcome email (Gmail draft only — never send)

Find a previous "everything you need to know" email in Gmail (search
`everything you need to know`) to copy the structure from — don't redesign
the layout. Create a **Gmail draft, addressed to all family members**,
following this exact shape. This is the corrected template (v1.3) — use it
verbatim, adapting only the bracketed placeholders. Pay close attention to
the exact wording around the homework links and "sit with them" line below —
these phrasings were proofread and corrected by Neil, don't paraphrase them:

```
Subject: The 'everything you need to know' email

Hi [First names, comma separated — e.g. "Colin, Liz & Dave"],

Great to meet you all the other day. I'm so excited to be making this happen!

Everything you need is in your Family Project Folder - [here](DRIVE_FOLDER_LINK)

1. Sessions. All UK times

- [Day DD Mon] [HH:MM–HH:MM] [Session type] | [Attendee name]
  (repeat per session from Step 2, one per line, chronological order)

2. Reflection Guides

- **[Child name(s), comma-separated if more than one]** look [here](CHILDREN_GUIDE_LINK). As you look through it you'll see a link to your homework - 10 questions. I'm popping this [here](GOOGLE_FORM_LINK) too for easy access. I need this 24hrs before we talk. You'll see reminders.
- **[Parent name]** - your folder is [here](PARENTS_GUIDE_LINK). Print off your Guides, sit with them, and take your time. Some people write pages. Some make a few scribbles. Some keep it all in their head. Whatever works. There is also a life chart and an audio version of the prompts. I also encourage you to get out the old photo albums and reach out to siblings and friends to piece together stories and memories—that's all part of the experience!

3. Simple Family tree—siblings, parents and grandparents with rough dates. A scribble on paper, a photo, an email — whatever's easiest. Drop it [here](TREES_FOLDER_LINK) before [first parent/interviewee name]'s first session.

4. Photos - as mentioned, please start to dust off those old albums, take a photo and upload it into the folder with clear labelling. "[Example] Cornwall 1965"..."[Example] and sister [name] 1970ish". [Upload here](PHOTOS_FOLDER_LINK).

5. Tech - wired headphones are the best basic option (not AirPods), so a heads-up to start digging them out of the drawer. If you want to step up the richness of the audio, you can pick up a decent USB microphone like [this Tonor one](TONOR_MIC_LINK) for £25. If you have a bit more budget, this is also [a trusted brand and decent choice](SENNHEISER_MIC_LINK).

Other than that, come as you are. Share what matters. That's it.

I'm your single point of contact for everything. For questions, excitement, or random memories that pop up at 11pm — my inbox is always open.

Can't wait to get started!

Thanks,
Neil
```

**Wording notes (from Neil's proofread, don't drift from these):**

- "As you look through it you'll see **a** link to your homework" — not
  "you'll see link to your homework."
- "I'm popping **this** here too for easy access" — not "I'm popping here
  too" (needs the object "this").
- "Print off your Guides, sit with them, **and** take your time" — not "sit
  with them, take your time" (needs the conjunction).
- "I need this 24hrs before we talk. **You'll see reminders.**" — not
  "You'll be reminders."

**Formatting rules for this email — non-negotiable:**

- **Bold the numbered section headers** ("1. Sessions.", "2. Reflection
  Guides", "3. Simple Family tree", "4. Photos", "5. Tech" — or at minimum
  bold each family member's name inline where they're addressed directly,
  e.g. "**Liz & Dave** look here", "**Colin** - your folder is here").
- **Every single link must be hyperlinked to a short word or phrase** — never
  paste a bare/raw URL as visible text, and never let Gmail's link-wrapping
  (`https://www.google.com/url?q=...`) show as the display text either. Link
  words like "here", "Upload here", "this Tonor one". This is a hard rule —
  it applies to Gmail exactly as it does to Google Docs (see cross-cutting
  hyperlink rule in `Lessons/lessons.md`, 2026-08-13).
- **Always include the "5. Tech" section** with the two mic links below,
  unless Neil says to drop it for a specific family:
  - Tonor USB mic (~£25): https://amazon.co.uk/TONOR-Microphone-Condenser-Recording-Podcasting/dp/B07W6ZZZWK
  - Sennheiser Profile USB mic (higher budget option): https://www.amazon.co.uk/Sennheiser-Profile-Microphone-Table-Stand/dp/B0BTPYCD86
  (Strip tracking params from Amazon URLs before inserting if you have a
  clean version to hand; otherwise the full link is fine since it's hidden
  behind hyperlinked text anyway.)
- **Google Form link for homework questions** — ask Neil for the current
  family's form link if you don't already have one on file; don't reuse a
  different family's form link.

Do not include Neil's old "Tayls / Neil / Teil / Nails" sign-off variant
unless Neil explicitly asks for it — that was a personal in-joke with one
specific family, not a standard sign-off. Default to "Thanks, Neil."

Remove any placeholder family-specific names/session labels that don't
apply (e.g. if there's only one child, don't leave a plural "children"
reference). Never leave a hyperlink pointing at nothing — if a guide/folder
doesn't exist yet, build it first (Step 4) before drafting the email so
every link resolves.

**Always save as a Gmail draft. Never send it yourself** — Neil reviews,
checks names/times, and sends it himself. Proofread the draft for small
grammar gaps before handing it back as final — missing articles ("a link"
not "link"), missing objects after verbs ("popping this here" not "popping
here"), missing conjunctions in short comma-joined clauses ("sit with them,
and take your time"), and verb mismatches (see/be) are the kind of slip that
slips through if you only check tone and not grammar.

## Step 4: Build the family's Drive folder

**Location: directly at the root of the Shared Drive with ID
`0ALiqx6MMMJj3Uk9PVA`.** This Shared Drive holds every family folder flat at
its top level — e.g. Griffiths, Blakes, Cheyneys, Taylors, McMullans,
Salvesens, Normans all sit directly there, no intermediate "Families"
subfolder. **Do NOT create or use a "Families" folder** — a folder with that
name exists in Neil's My Drive (`0AFnWiLtGFlyNUk9PVA`) but it is the WRONG
location; using it was a logged mistake (2026-08-13, Best family). Before
creating a new family folder, list the existing siblings at
`0ALiqx6MMMJj3Uk9PVA` first (search `parentId = '0ALiqx6MMMJj3Uk9PVA'`) to
confirm you're building in the same place as every other family, named
**[Surname]** (e.g. `Griffiths`, `Bests`).

Inside it, create exactly these five subfolders:

- `01 Trees` — empty
- `02 Guides` — contains two subfolders:
  - `01 Children` — **one single shared "Child Reflection Guide" file, used
    by ALL children in the family.** Do NOT duplicate or rename a copy per
    child (e.g. never create "Elisabeth - Child Reflection Guide" and
    "David - Child Reflection Guide" as separate files) — there is exactly
    one file here, titled "Child Reflection Guide" with no name prefix, and
    every child reads from it.
  - `02 Parents` — the parent reflection guide doc, the audio version of the
    prompts, and the life chart
  (Find these as a standard template set — search Drive for an existing
  family's `02 Guides` folder, e.g. Griffiths, to copy the subfolder
  structure and file set from. Don't invent the file list — match exactly
  what's in an existing family's `01 Children` and `02 Parents` subfolders.
  If none can be found, ask Neil where the master template set lives rather
  than guessing.)
- `03 Photos` — empty
- `04 Stories` — empty
- `05 Mementos` — empty

If Neil gives you a specific master folder to copy wholesale (e.g. pastes a
Drive link and says "copy this over and call it [Surname]"), note that the
Drive connector's `copy_file` tool only duplicates single files, not folder
trees — it will error on a folder ID. Build the structure manually instead:
create the top-level folder (at the Shared Drive root per above), the five
subfolders, and copy each file individually into the right destination,
matching the master's layout exactly.

**Share the top-level `[Surname]` folder** with **Content Manager** access
(this Shared Drive uses Content Manager as the standard collaborator role,
not "Anyone with the link") so the family can upload their own photos and
family tree docs into it. **The connected Drive MCP tool cannot set sharing
permissions** — it only has a read-only `get_file_permissions` call, no
write/create-permission call. This means Step 4 can never fully finish the
sharing step itself: **always flag in Step 6** that Neil needs to manually
add the family as Content Manager (or set General access → Anyone with the
link → Editor, whichever fits) — don't let this slip as a one-off aside,
treat it as a required checklist item every single run.

Copy the shareable link to the top-level folder — this is what goes in the
email's "Family Project Folder" hyperlink (Step 3).

## Step 5: Log confirmed sessions in Airtable

Base **M&MOM Database** (`app077Z4RXX1PShzN`), table **Editor Pipeline**
(`tblWkRNY5rcvthBMs`). Find the existing rows for this family (created
earlier by the `new-client` skill, likely still showing `TBC` dates) and
update the **Session Date** field with the real, confirmed date/time from
Step 2, matching each row to the right session by session type and
attendee/interviewee name.

If a session type Neil booked doesn't already have a placeholder row (e.g.
a Wrap Up now scheduled that wasn't logged before), create one — same field
IDs as documented in `new-client`:
- `fldfvHJsC7EILNfpr` Family Name
- `fldvMQG55QBjefTeB` Interviewee
- `fldO9gjgDbql5WTxC` Session Type
- `fldBeVYeozSiPiewg` Session Label (S1/S2/S3, blank for children)
- `fldvpwgWDhllOGcFI` Status — set to "To Schedule" or "To Record" as
  appropriate now a real date exists (no longer "TBC")
- `fldb3hwVVXTrSJDe5` Editor

If you can't confidently match a Calendly session to an Airtable row, don't
guess — flag it to Neil in the summary (Step 6) rather than creating a
duplicate or overwriting the wrong row.

## Step 6: Confirm with Neil

Summarize in a few short lines: the Gmail draft created (recipients,
subject — note it's a draft, not sent), the Drive folder link (confirm it's
at the Shared Drive root, not a "Families" subfolder), what's in `02
Guides` (or what's missing/TBC), and which Airtable rows got real dates vs.
any sessions you couldn't confidently match.

**Always explicitly flag, every run, without being asked:** that Neil needs
to manually set Content Manager (or equivalent edit) access on the new
family folder, since the Drive tool can't do this. Also flag anything else
that needed guessing (missing Airtable row, ambiguous guide template,
timezone uncertainty) so Neil can spot-check before the email goes out.
]]>
