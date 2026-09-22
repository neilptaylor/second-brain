---
name: mmom-onboarding
description: >
  Me & My Old Man onboarding skill. Use this skill whenever Neil is bringing on a new team member — VA, producer, editor, or any other role — at MMOM. Triggers on phrases like "onboard", "new hire", "first day", "welcome pack", "start them off", "set up for [name]", "what should [name] do on Monday", or any mention of getting someone started at the business. This skill produces: a personalised Welcome Doc, a Day 1 task structure (first 30min / next 1hr / next 1hr), and a pre-populated Google Sheets task tracker. It also references the onboarding system principles so Neil doesn't have to reinvent the wheel each time someone new joins.
---

# MMOM Onboarding Skill

## Purpose

Every time Neil brings on a new team member, three things need to happen quickly:

1. The new person needs to feel genuinely welcomed — not just informed.
2. They need clarity on exactly what to do from minute one, without having to ask Neil.
3. Neil needs a tracker so nothing falls through the cracks in the first two weeks.

This skill creates all three, fast.

---

## Phase 0 — Gather what you need

Before writing anything, collect the following. If it's not in the conversation, use `AskUserQuestion` to get it.

**About the person:**
- Full name (and what they prefer to be called)
- Location / time zone
- Tools they already know (from their interview or application)
- How they were introduced to Neil / what impressed him about them
- Their start date and agreed hours

**About the role:**
- Which task areas they're starting with (see MMOM role types below)
- Their first specific task or project (the concrete thing they'll do in Week 1)
- What access they'll need (Riverside, Canva, Google Drive, etc.)
- Any gaps in their knowledge to be aware of

**What Neil has ready:**
- Is there a family list / starting batch prepared?
- Have logins been sorted (LastPass or equivalent)?
- Are brand assets (colours, fonts, Canva templates) accessible?
- Is the Google Drive folder structure in place?

Also check: does a transcript from an intro call exist? If so, read it — it's gold. The specific things Neil said he'd do are commitments that should show up in the onboarding docs.

---

## Phase 1 — Write the Welcome Doc

**Tone:** Warm, personal, mission-connected. Written from Neil. Not corporate. Not a handbook. A letter from a founder who genuinely cares.

**Structure:**

1. **Opening — why this exists** (Neil's founding story, briefly — the loss of his dad, the birth of his son, the gap between them). This is not just backstory. It's why their work matters.

2. **What we actually do** (the 12-week experience: child interview → parent sessions → wrap up → audio documentary). Be specific. Use the correct terminology.

3. **The content types they'll work with** (only the ones relevant to their role — don't include pipeline management content for someone starting on production tasks). Include brief descriptions of each type and a reference example where available.

4. **Brand voice & tone** (what MMOM sounds and looks like — warm, intimate, private. The banned words. The natural-conversation philosophy. Keep it brief; link to the Voice Profile if available.)

5. **Tools overview** (only the tools they'll actually use in their first weeks — don't overwhelm).

6. **How we work together** (hours, reporting cadence, communication channels, time zone setup, check-in schedule).

7. **What Neil needs from them** (proactivity, care for the material, questions — this is where to set the tone for the relationship).

8. **A personal close** — what specifically impressed Neil about this person. Reference something concrete from their application or intro call. This should not be generic.

**Length:** ~800–1,000 words. Readable in 10 minutes.

**Voice:** Read the VOICE_PROFILE before writing. The Welcome Doc is from Neil. It should sound like him — warm, direct, specific, no corporate language. It's not a welcome email from HR. It's a letter from someone who cares about the work and the person.

**What to avoid:**
- Generic welcome phrases ("We're delighted to have you join the team!")
- Lists of policies
- Anything that sounds like it could be from any company
- Banned words: preserve, legacy, heirloom, keepsake, process (say "experience"), treasure

---

## Phase 2 — Write the Day 1 Task Guide

This is the most operationally important document. A new person should be able to open it on their first morning and know exactly what to do — without asking Neil a single question before the first check-in call.

**Structure:** Three timed blocks.

### Block 1: First 30 minutes — Orientation
- Log into each tool they'll use (Riverside, Canva, Google Drive, etc.)
- Read the Welcome Doc (if not done already)
- Find the task tracker and read Week 1 tasks
- No producing yet — just orientating

### Block 2: Next hour — Understand the work
- Watch any reference examples (e.g. Abel case study clip)
- Review the family list / starting batch / brief
- Find the first piece of work in the relevant tool
- Listen to / watch a sample of source material (get a feel for the MMOM style)

### Block 3: Final hour — Make one thing
- Produce one test output (the simplest version of whatever their first task type is)
- Save it in the correct folder with the correct naming convention
- Write a brief end-of-day note to Neil: what's done, what's missing, biggest question for the check-in call

**Tone:** Practical and precise. No fluff. Numbered steps. If a step could be misinterpreted, add a note. The goal is zero ambiguity.

**Always include at the end:**
- Quick reference cheat sheet for content types (if production role)
- "If you get stuck" guidance — what to do when something's missing or confusing
- The time and format of the first check-in call

---

## Phase 3 — Build the Task Tracker (Google Sheets / .xlsx)

**Format:** A clean .xlsx file, exported to Google Drive. Simple enough that the new person doesn't need a tutorial.

**Sheet 1 — Task Tracker:**

Columns: `#` | `Task` | `Area` | `Status` | `Priority` | `Due` | `Output / File` | `Notes`

**Status options** (colour-coded):
- `To do` — warm off-white
- `Doing` — amber tint
- `Done ✓` — soft green
- `Blocked` — soft red

**Priority options:**
- 🔴 Do first (Day 1 essentials)
- 🟠 High (complete within the day/block)
- 🟡 Medium (by end of week)
- 🟢 Normal (Week 2 onwards)

**Pre-populate with:**
- All Day 1 orientation tasks (Block 1–3 from the Day 1 Guide)
- Week 1 production tasks (based on their specific brief)
- Week 2 tasks listed as 🟢 Normal with "TBD" due dates
- Any admin/logistics tasks (filing, Wise invoice setup, access confirmation, etc.)

**Group tasks into labelled sections** (e.g. "Block 1 — Orientation", "Block 2 — Content Research") — this mirrors the Day 1 Guide so she can follow both together.

**Sheet 2 — How to use:**
A brief key explaining status colours, priority meanings, the daily update format, and the file naming convention.

**Styling:** Clean, warm, professional. Dark header row. Alternating row shading. Consistent Arial font. MMOM brand feel — not a cold corporate spreadsheet.

---

## Phase 4 — Final checklist before sending

Before handing everything to Neil, check:

- [ ] Welcome Doc sounds like Neil (warm, specific, no banned words)
- [ ] The person's name is used correctly throughout
- [ ] The intro call transcript (if available) has been mined — promises Neil made are reflected
- [ ] Day 1 Guide assumes the new person has all tools set up — if they don't, add a "before you start" prerequisite block
- [ ] Tracker is pre-populated with enough tasks to fill Week 1 without overwhelming
- [ ] File naming follows: `MMOM_[DocType]_[Name]_v1.md/.xlsx`
- [ ] All files saved to: `Claude Outputs/[Name] Onboarding/`

---

## MMOM Role Types (reference)

Use these to tailor the onboarding content to the right task areas.

**VA + Producer (current: Ronnie)**
- Task Area 1 (start here): Mine Riverside for content clips. Produce audiograms, video clips, audio highlights, case study clips. Organise Riverside into family folders.
- Task Area 2 (3–4 weeks in): VA support — scheduling, Calendly, client comms, Google Drive organisation.
- Task Area 3 (once settled): Editorial pipeline management — briefing editors, reviewing edits, chapter titles, family delivery emails.

**Freelance Editor**
- Primary task: Receive briefing doc + raw session files. Produce edited audio chapters to MMOM technical specification. Return V1 for QA review.
- Onboarding focus: Technical spec, reference chapters, turnaround expectations, feedback process.

**Content / Social Support**
- Primary task: Publish approved clips to Instagram, LinkedIn. Write captions following Voice Profile SOP. Manage scheduling.
- Onboarding focus: Voice Profile, platform SOPs, approval workflow.

---

## Onboarding Principles (from Founder OS, adapted for MMOM)

These are the underlying beliefs that shape every MMOM onboarding. Keep them in mind when writing.

**People before paperwork.** The Welcome Doc comes before the how-to guides. A new person needs to understand *why* the work matters before they learn *how* to do it.

**Clarity beats choice.** The Day 1 Guide tells people exactly what to do — not a menu of options. Ambiguity is expensive in the first week.

**Nothing ever lost.** File structure and naming conventions are established from Day 1. It's not pedantry — it's respect for the families whose stories live in these files.

**Check-ins over chaos.** Daily notes in Week 1, weekly from Week 2. The tracker makes work visible without requiring constant communication.

**Build to delegate.** Every onboarding should be written as if you're handing the system to someone else next time. Notes, naming conventions, and structure exist so Neil doesn't have to explain from scratch twice.

---

## Week 1 Check-in Structure

Neil's default check-in rhythm for new hires:

- **Day 1 (Mon): 60-min call** — walk through first clip, answer questions, confirm Week 1 priorities
- **Daily (Tue–Thu): short written update** from new hire (what done, what blocked, what's needed)
- **End of Week 1 (Thu/Fri): 30-min review call** — what worked, what needs adjusting, confirm Week 2 plan

From Week 2: weekly written update + bi-weekly 30-min call (moving to monthly once settled).
