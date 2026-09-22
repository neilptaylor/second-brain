---
name: client-onboarding-complete
description: >
  Draft the welcome email to send to a family after the onboarding call,
  with session times populated from Calendly/Gmail. Pulls times from Neil's
  calendar, converts to family's timezone, links to their Family Project
  Folder (created by client-folder-setup), and links to specific guides
  folders. In Neil's voice. Runs AFTER the onboarding call, once session
  times are locked.
---

# Client Onboarding Complete — Welcome Email

Drafts the welcome email to send to a family after Neil's onboarding call with
them. This email introduces the Family Project Folder, confirms all upcoming
session times, and links to the guides families need to review.

**Timing:** Run this after the onboarding call. Neil will tell you "send the
onboarding email for [Family]" once the calendar is updated with session times.

**Output:** A draft Gdoc (not sent yet) that Neil reviews, tweaks, then copies
to Gmail to send to the family.

## Before you start: confirm these details

1. **Family surname** — exact spelling
2. **All family members' names** who are involved (everyone who recorded a
   child session, everyone in the parent sessions). You'll greet them all by
   first name in the opening.
3. **Family email addresses** — who the email is going to (usually the primary
   contact + partner if applicable)
4. **Family timezone** — ask Neil directly ("What timezone are they in?") — you
   need this to convert session times. Common: "US Eastern," "UK," "US
   Pacific." If they're in UK, times stay in GMT/BST; if US, convert.
5. **The Family Project Folder link** — the shareable link from client-folder-
   setup. If Neil hasn't run that skill yet, ask him to confirm the folder
   location first.
6. **Which guides exist** — Neil will tell you which reflection guides are
   already in the folder. For most families this is:
   - One child reflection guide per child (PDF)
   - One parent reflection guide (PDF)
   - One audio version of parent guide (MP3)
   - One family life chart (PDF, Silver/Gold only)
   If any are missing, leave those links out of the email.

If anything is unclear, ask Neil one direct question rather than guessing.

## What to find in the calendar

Neil uses Calendly + Google Calendar. Search for sessions with this family's
name in the title. You're looking for:

- **Child briefing sessions** — typically labelled "1hr Child Briefing | [Child
  Name]"
- **Parent recording sessions** — typically labelled "2hr Parent Life Story
  Recording | [Parent Name] | S.1" (or S.2, S.3)
- **Family Wrap Up & Reflections** — typically a group call at the end

Collect:
- **Date** (e.g., "Tuesday 14 August")
- **Time** (e.g., "14:00 - 15:00")
- **Duration** (child = 1hr, parent = 2hr, wrap-up = 1-2hr, typically)

For each session, write it in UK time first, then convert to family's timezone
if needed (Neil can give you the formula or confirm the conversion).

*Note: If a session is already past its date, don't include it. Only list
upcoming sessions from today onwards.*

## Email structure & voice

**File to create:** A new Google Doc in Neil's `Claude Outputs > Client
Communications` folder (create the folder if it doesn't exist), named:
`[Family Surname]_Onboarding_Email_v1.gdoc`

**Tone:** Neil's email voice — warm, specific, scene-based, not corporate.
This is the tone from his best newsletters, not his LinkedIn posts. Shorter
paragraphs, bold subheadings for clarity, a P.S. that carries emotional weight.

**Structure to follow:**

---

**[GREETING]**
Hi [All names],

I'm so excited to be making this happen with you all!

**[FOLDER INTRO]**
Everything you need is in your Family Project Folder. [Link hyperlinked]

[One scene-based paragraph explaining what's in there: "You'll see folders
for your reflection guides, the photos and family trees you'll want to gather,
and a space for any notes or memories that come up as we go through this. The
most important thing to know: this is *your* space. You control what goes in
here."]

**[SESSIONS — all upcoming times, UK format then family's timezone]**
1. Sessions. All UK times

[Bulleted list of every session in reverse chronological order or sequential order — Neil will clarify which he prefers. Format:]

- Wed 22 Jul 19:30 - 20:30 1hr Child Briefing | Geoff Griffiths
- Tue 4 Aug 14:00 - 15:00 1hr Child Briefing | Nicola Griffiths
- Thu 6 Aug 12:00 - 14:00 2hr Parent Life Story Recording with Vaughan
  Griffiths
- [etc — all of them]

[If family is not in UK: add a line below]
If you're not in the UK, here are those times in [Family Timezone]:
[Same list, times converted]

[Optional: add a note like "We'll confirm exact Zoom/call links 24hrs before
each session" or similar, if that's Neil's process]

**[REFLECTION GUIDES]**
2. Reflection Guides

[Scene-based paragraph, not a bulleted list. Something like:]
Before each session, we'll send you a guide with 10 questions to think about.
There's no right or wrong way to prep — some of you will write pages, some
will just jot down one-word reminders, and some will keep it all in your head.
Whatever works. [Link to the guides folder or specific guide PDFs, depending
on which are ready.]

For [Parent Name], there's also an audio version if you'd rather listen than
read.

**[OTHER ASSETS]**
3. Simple Family Tree

[Short paragraph] We'll ask you to jot down a quick family tree — siblings,
parents, grandparents, whatever feels important. It can be as simple as a
scribble on paper. Drop it here when you're ready. [Link to Trees folder]

4. Photos

[Short paragraph] Dig out any old albums or photos that spark memories for you
— especially childhood pictures, family moments, places that mattered. We'll
reference these in the sessions, and they'll stay in your folder. [Link to
Photos folder]

Other than that — come as you are. [Neil's signature permission line]

**[FINAL BEAT + P.S.]**
I'm your single point of contact for everything. Questions, excitement, random
memories that pop up at 11pm — my inbox is always open.

Can't wait to get started.

Thanks,
Neil

P.S. [Emotional one-liner. This is where Neil puts the thing that matters.
Examples: "You're going to be surprised by what you remember." / "This is one
of those decisions you'll feel good about for the next 30 years." / "We're
going to hear his voice exactly as it is. That's the whole point."]

---

## Key rules for this email

1. **Use their actual names.** Not "everyone" or "you all" — greet them by
   first name. "Hi Geoff, Nicola, Vaughan" or however Neil introduced them.

2. **Hyperlink everything.** Family Project Folder link, Guides folder link,
   Trees link, Photos link — all clickable. No bare URLs.

3. **Times in UK first, then convert.** Neil is UK-based; the default is GMT.
   If they're US, add the converted times clearly below.

4. **Don't repeat information.** If the guides are linked, don't describe them
   again in the text. Link, trust the link.

5. **One scene-based paragraph per section.** Not bullet-point heavy. Neil's
   email voice is warm prose with strategic bold subheadings, not a task list.

6. **No corporate language.** Not "We look forward to connecting with you." Not
   "Thank you for choosing Me & My Old Man." Not "optimise your experience."
   Write like Neil actually talks: "This is going to be something."

7. **The P.S. is the lighthouse.** It's the most powerful moment. Something
   specific and true, not generic. If you can't think of a P.S. that lands,
   flag it to Neil.

8. **Use British vernacular where natural.** "Can't wait." "Come as you are."
   "Brilliant." Keep it warm, not performed.

## After drafting

1. **Create the Gdoc** in Neil's outputs folder (named as above)
2. **Share the link with Neil** for review
3. **Flag anything ambiguous** — missing guides, timezone uncertainty, family
   member names that seem off
4. **Don't send it yet.** Neil will review, tweak, then copy-paste into Gmail
   when he's ready.

## If any session times are missing or unclear

Stop and ask Neil:
- "What time is the first child briefing with Geoff?"
- "Is Wrap Up happening, and if so, when?"
- "What timezone should I convert to?"

Don't guess at calendar times. One wrong time in the email and the family
misses a session.

## Connection to client-folder-setup

This skill assumes `client-folder-setup` has already run. The Family Project
Folder you link to in this email is the one that skill created. If folders
aren't ready yet, ask Neil to confirm before drafting — you need that link to
put in the email.

---

## Example email (this is *guidance*, not a template — adapt to Neil's voice)

---

Hi Geoff, Nicola, Vaughan,

I'm so excited to be making this happen with you all!

Everything you need is in your Family Project Folder. [link] You'll see
folders for your reflection guides, the photos and family trees you'll want to
gather, and a space for any notes or memories that come up as we go through
this. The most important thing to know: this is *your* space. You control
what goes in here.

**1. Sessions**

All UK times

- Wed 22 Jul 19:30 - 20:30 1hr Child Briefing | Geoff Griffiths
- Tue 4 Aug 14:00 - 15:00 1hr Child Briefing | Nicola Griffiths
- Thu 6 Aug 12:00 - 14:00 2hr Parent Life Story Recording with Vaughan
  Griffiths
- Wed 12 Aug 10:00 - 12:00 2hr Parent Life Story Recording with Vaughan
  Griffiths
- Fri 14 Aug 10:00 - 12:00 2hr Parent Life Story Recording with Vaughan
  Griffiths
- Wed 2 Sep 10:30 - 11:30 1hr Family Wrap Up & Reflections with all of you

If you're not in the UK, here are those times in US Eastern:

[Same list with converted times]

**2. Reflection Guides**

Before each session, we'll send you a guide with 10 questions to think about.
There's no right or wrong way to prep — some of you will write pages, some
will just jot down one-word reminders, and some will keep it all in your head.
Whatever works. [link to guides folder]

For Vaughan, there's also an audio version if you'd rather listen than read.

**3. Simple Family Tree**

Dig out a scribble on paper — siblings, parents, grandparents, whatever feels
important. It can be a photo of a sketch, an email, anything. Drop it here
when you're ready. [link to Trees folder]

**4. Photos**

Find any old albums or photos that spark memories — especially childhood
pictures, family moments, places that mattered. We'll reference these in the
sessions, and they'll stay in your folder. [link to Photos folder]

Other than that — come as you are. Share what matters. That's it.

I'm your single point of contact for everything. For questions, excitement, or
random memories that pop up at 11pm — my inbox is always open.

Can't wait to get started.

Thanks,
Neil

P.S. Listening back to sessions like these, families tell us it's the small
details that land hardest. A phrase he uses. The way she laughed. Not the big
stories — the texture. That's what we're after.

---

Use this as a rhythm guide, not a fill-in-the-blanks template. The specifics
come from Neil's actual voice and the family's actual details.
