---
name: "mmom-weekly-action-plan"
description: "Me & My Old Man daily and weekly planning skill. Runs in three modes: (1) SUNDAY EVENING — generates the full weekly plan from CRM and growth strategy; (2) WEEKDAY MORNING — generates a daily briefing with top 3 priorities and Gmail triage; (3) END OF DAY — ingests voice note transcript, logs what happened, sets tomorrow's priorities. Use this skill whenever Neil asks for his weekly plan, daily briefing, or wants to log end-of-day notes."
---

<!-- v1.2 — 2026-07-15: Mode 1 template locked to April action-plan format (Real Talk, Done =, Stop List, Kill Switches, Scoreboard); sales calls = discovery calls -->
<!-- v1.3 — 2026-07-17: Dashboard money tiles — cross-check Airtable Lead Status before reading a low Xero invoiced figure as "nothing billed"; some clients pay via Stripe and won't show cleanly in Xero yet -->
<!-- v1.4 — 2026-07-17: Neil prefers the dashboard as a Cowork artifact, not a raw HTML file link. Moved to mcp__cowork__create_artifact / update_artifact with a fixed id ("mmom-mission-control") instead of the old claude.ai/code/artifact URL -->
<!-- v1.5 — 2026-08-08: Fixed a real bug — Xero's get_cash_position/get_profit_and_loss tools cache on a slower cycle than get_aged_receivables and can silently show a stale snapshot (was ~2 weeks stale, £11,407 vs actual £14,209). Always cross-check cash_position's `last_refreshed` timestamp against aged_receivables' `last_refreshed` (or as_of_date) — if cash_position is older, don't trust its cash_balance figure at face value; sanity-check against what Neil says Revolut shows. Also added: Accounts Receivable box (Xero aged receivables, including named future-dated invoices — these are often client Direct Debit schedules, e.g. "Bronze Package - Payment 2/3" — surface them explicitly with due dates) and Accounts Payable/COGS forecast box (Airtable Editor Pipeline Budget field — money owed to editors for edits not yet paid). -->
<!-- v1.6 — 2026-09-22: Merged with the Drive lineage (folder name `weekly-action-plan`), which had forked at v1.4 with no unique content of its own. Also repaired HTML-entity corruption (&lt; / &gt; / &amp;) that had crept into the repo copy's code fences and headings. -->

# Me & My Old Man — Daily & Weekly Action Plan Skill

This skill runs in three modes. Detect which one applies from context:

- Neil mentions "weekly plan" or it's Sunday → **MODE 1: SUNDAY WEEKLY PLAN**
- Neil says "morning briefing" or "what's today" → **MODE 2: DAILY BRIEFING**
- Neil pastes a voice note or says "end of day" → **MODE 3: EOD LOG + TOMORROW'S PRIORITIES**

---

## ALWAYS READ FIRST (EVERY MODE)

Before doing anything, read these files:

1. **CRM / Sales Tracker** — search Google Drive for "Full CRM-SALES TRACKER". This is the source of truth for all pipeline actions. Pull every Hot lead and all active onboarding clients.
2. **Latest weekly plan** — find the most recent file in `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/Mega Claude Cowork/Claude Outputs/Weekly Action Plans/` — read it.
3. **Daily log for this month** — look for `MMOM_DailyLog_[Month-Year].md` in the same folder. Read any entries from the past 7 days to understand what has actually happened vs. what was planned.
4. **Steve Session Notes** — search Google Drive for "Steve Session Notes". If there's one from the past 30 days, read it. Steve's priorities override the growth strategy if they conflict.
5. **Growth Strategy** — `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/Mega Claude Cowork/Claude Outputs/Weekly Action Plans/MMOM_Growth_Strategy_May2026_Update.md`

Do NOT invent leads or family names. Use only what's in the CRM and existing plans.

---

## MODE 1: SUNDAY EVENING — FULL WEEKLY PLAN

**Trigger:** Sunday, or Neil explicitly asks for the weekly plan.

**Output:** One markdown file saved to the Weekly Action Plans folder.

### Step 1 — Build the real pipeline snapshot

From the CRM, identify:

**Hot leads** — for each one, state:
- Last action + date
- What's needed this week (call, chase, proposal, park)
- Buyer-only rule: the person who paid or initiated, not siblings or family groups

**Active onboarding clients** — for each one, state:
- Which SOP stage they're at
- What the next deliverable is and when it's due

**Active production families** — any family in delivery with pending assets (clips, edits, mementos, welcome packs, wrap-up calls)

### Step 2 — Write the weekly plan

Use this exact structure (format locked to the April 2026 action plans in
`Shared drives/Systems/00 Rituals & Action Plans/` — Neil's preferred format):

```
# ME & MY OLD MAN — Weekly Action Plan
[Mon Date] – [Fri Date]
*vN — [one-line context] | Target: [the current target, e.g. "2 sales by 21 May"]*

## ⚡ [DAY]'S TOP 3 — START HERE
(living-document top section — replaced each evening by Mode 3)

## PIPELINE REALITY CHECK
*[Honest one-line count: X hot, X in motion, X stalling, X paused.]*
[Table: Lead | Status | Real Talk | Next Action]
— "Real Talk" is one honest human sentence per lead ("Sold but stuck. Mum objection
   loop. Force the fork now."), never CRM-speak.

## [DAY, DATE] — [Headline for the day, e.g. "Sales First. Finance Second. Nothing Else."]
*[One-line intent for the day.]*
[Table: Action | Detail / Script | Done =]
— Priority tags inline in the Action cell: [CRITICAL] / [HIGH] / [MEDIUM]
— "Detail / Script" carries the actual words or script fragment where a message is involved
— "Done =" is a definition of done ("Sent by 9am", "Call booked"), never a tick-box
(...one section per working day; Friday is always Review + Close the Week)

## REFERRAL ACTIVATION PLAN
[Table: Family | Priority | Action This Week]

## STOP LIST
[Table: Parked Item | Why]
— The "Why" is a rule, not an apology ("Ship 10 pieces manually before building a system.")

## KILL SWITCHES
[Table: Initiative | Kill Condition | Deadline]
— Every live initiative gets an exit condition.

## ACCOUNTABILITY SCOREBOARD
*Target: [same target as the header]*
[Table: Metric | This Week | Target | Status]
Default metrics: warm conversations started · sales calls booked · referral asks
made · clips dispatched to families · content with CTA published.
(Terminology: sales calls and discovery calls are THE SAME THING — one metric,
always called "sales calls". Never track them separately.)

## THE QUESTION YOU'RE NOT ASKING
*[One paragraph that names the uncomfortable number or pattern.]*

## END-OF-DAY VOICE NOTE PROMPT
Three questions Neil should answer each evening:
1. What did I actually do today?
2. What moved in the pipeline?
3. What needs to happen first tomorrow?
(Friday adds: newsletter subs, LinkedIn impressions, Insta reach — for the dashboard.)

Updated: [date] (vN) | Review: Friday [date]
```

The ✅ COMPLETED section (Mode 3) is appended at the bottom, below the footer line.

### Rules for writing each day

- Every day starts with a sales action. Never admin first.
- Sales calls = discovery calls. One term ("sales call"), one metric, everywhere.
- 3-hour morning blocks: Sales → Production → Admin (strict order)
- Specific names and deadlines. "Chase Chuck by Wed" not "follow up with prospect."
- Buyer-only rule on family/referral actions. Go to the person who paid. Not siblings.
- Friday is always pipeline review + voice note. No exceptions.
- Parked items from the growth strategy stay parked (Instagram, LinkedIn automation, website, new IP, B2B outreach).

### Step 3 — Save the file

Name: `MMOM_Weekly_Action_Plan_[MonDate]-[FriDate]_v1.md`
Location: `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/Mega Claude Cowork/Claude Outputs/Weekly Action Plans/`

If a file for this week already exists, increment the version number. Never overwrite.

---

## MODE 2: WEEKDAY MORNING — DAILY BRIEFING

**Trigger:** Monday–Friday morning, or Neil asks "what's today" / "morning briefing."

**Output:** Printed in chat. Not saved to file unless Neil asks.

Neil has 3 hours blocked. The briefing is designed to be read in 2 minutes and executed immediately.

### Section 1 — Top 3 priorities for today

Pull from the weekly plan. Reorder based on the daily log (what moved yesterday? what slipped?).

Format:
```
## Good morning, Neil. Here's your [Day].

**3 hours. Sales first.**

1. [Specific action — name, task, what "done" looks like]
2. [Second priority]
3. [Third priority]

**If you only do one thing today:** [The single most important action, one sentence]
```

### Section 2 — Email triage (Gmail)

Use the Gmail connector to scan for unread emails. Look for:
- Any name from the CRM (lead replies, client questions, production updates)
- Editors, Abhi, Vuk — production updates
- Anything that blocks today's top priorities

Format:
```
## Inbox — Action Needed

| From | Subject | What To Do | Priority |
|------|---------|------------|----------|
| [name] | [subject] | [specific action] | 🔴/🟡/🟢 |

**Safe to ignore today:** [any threads that can wait]
```

If Gmail is not accessible, say so clearly and skip this section.

### Section 3 — One line from Steve

The most relevant tactical truth from Steve's session notes for today's work. Not motivation — a specific strategic reminder.

Example: *"Done means sent. Every hour on V16 is an hour not spent closing."*
Example: *"Chasing a volunteer multiple times is resistance dressed as due diligence."*

---

## MODE 3: END-OF-DAY VOICE NOTE INGESTION

**Trigger:** Neil pastes a voice note transcript, or says "end of day" / "log this."

**Output:** Updated daily log file + revised tomorrow's priorities printed in chat.

### Step 1 — Parse the voice note

Extract:
- What got done today (completed actions, calls run, emails sent)
- What moved in the pipeline (replies received, leads converted, leads parked)
- What didn't happen and why (slipped, blocked, ran out of time)
- Energy / mood signal (one phrase — Neil often signals this without labelling it)
- New names, leads, or ideas mentioned

### Step 2 — Append to the daily log

File: `MMOM_DailyLog_[Month-Year].md`
Location: `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/Mega Claude Cowork/Claude Outputs/Weekly Action Plans/`
Create the file if it doesn't exist for this month.

Append this entry:
```
### [Day, Date]
**Done:** [list]
**Pipeline moves:** [lead updates — names and what changed]
**Didn't happen:** [what slipped and why]
**Feeling:** [one word or phrase — captured from tone, not judged]
**Tomorrow's priority:** [what Neil said or what logically follows]
```

### Step 3 — Update the weekly plan file (living document)

Find the current week's plan file in the Weekly Action Plans folder. Rewrite it with these three changes:

**1. Replace the top section with tomorrow's top 3:**
```
## ⚡ [TOMORROW'S DAY]'S TOP 3 — START HERE

**3 hours. Sales first.**

1. 🔴 [Most important action — name, task, what done looks like]
2. 🔴 [Second priority]
3. 🟡 [Third priority]

**If you only do one thing today:** [one sentence]
```

**2. Update any pipeline or onboarding rows** whose status changed in today's voice note. Reflect real current state. If a lead was lost or parked, remove them from the active pipeline table and add them to the completed section.

**3. Add or update the ✅ COMPLETED section at the bottom:**
```
## ✅ COMPLETED — [Day Date]

| Item | Outcome |
|------|---------|
| [action] | ✅ [result] |

**Closed / Lost / Parked:**
- [Name] — [reason]
```

Save by overwriting the same file. This is a living document — one file for the week, updated each evening.

### Step 4 — Print tomorrow's top 3 in chat

```
## Based on today — here's tomorrow's top 3:

1. [Updated priority]
2. [Second]
3. [Third]

[One sentence flag if anything changed urgently.]
```

---

## WEEKLY REVIEW (FRIDAY EVENING OR MONDAY MORNING)

When Neil asks for a weekly review, or at the start of a new week if no weekly plan exists yet:

Read `MMOM_DailyLog_[Month-Year].md` for the past 7 days.

Produce:
```
## Week of [dates] — What Actually Happened

**Wins:** [what got done]
**Pipeline:** [leads that moved, calls run, sales closed]
**Production:** [deliverables completed]
**Didn't happen:** [what slipped — no judgement, just truth]
**One pattern:** [single observation about how the week went]
**Carry forward:** [what goes into next week's plan]
```

This feeds directly into Sunday's weekly plan.

---

## MONTHLY REVIEW

**Trigger:** First Sunday of each month, or Neil asks "monthly review."

Read all daily log entries from the previous month.

Produce:
```
## [Month Year] — Monthly Review

**Clients onboarded:** [names + tier]
**Pipeline:** [new leads in, leads converted, leads parked]
**Production completed:** [families delivered]
**Referrals asked:** [how many, how many responded]
**Content published:** [LinkedIn posts, newsletters]
**What worked:** [2–3 specific observations]
**What didn't:** [honest read]
**One number:** [the metric that matters most this month]
**Into next month:** [top 3 priorities]
```

Save to: `MMOM_MonthlyReview_[Month-Year].md` in the Weekly Action Plans folder.

---

## SAVE LOCATIONS

| Output | Filename | Location |
|--------|----------|----------|
| Weekly plan | `MMOM_Weekly_Action_Plan_[MonDate]-[FriDate]_v1.md` | `Claude Outputs/Weekly Action Plans/` |
| Daily log | `MMOM_DailyLog_[Month-Year].md` | `Claude Outputs/Weekly Action Plans/` |
| Monthly review | `MMOM_MonthlyReview_[Month-Year].md` | `Claude Outputs/Weekly Action Plans/` |

---

## THE LIVING DASHBOARD — REFRESH AT THE END OF EVERY MODE

Neil's visual dashboard ("MMOM Mission Control") is the front door to this whole system.

- **Source file:** `/Users/neiltayloradmin/Library/CloudStorage/GoogleDrive-neil@meandmyoldman.co.uk/My Drive/Mega Claude Cowork/Claude Outputs/Weekly Action Plans/MMOM_Dashboard_v1.html`
- **Live artifact:** a Cowork artifact with the fixed id `mmom-mission-control` (created 2026-07-17 via `mcp__cowork__create_artifact`). Neil prefers this over a raw HTML file/URL — it shows as a card in Cowork and persists across sessions.

After finishing ANY mode above — and whenever Neil says "update my dashboard" — refresh it:

1. Edit the source file. Update ONLY the content inside sections marked `<!-- DATA: ... -->`:
   - Masthead: day name, date, and the three freshness stamps (pipeline / money / plan)
   - Today's Top 3 + "if you only do one thing" + "also owed" — from the current plan or tomorrow's priorities
   - **Cash tile — Xero MCP `get_cash_position`.** Known bug: this tool (and `get_profit_and_loss`) can return a `last_refreshed` timestamp that is days or weeks stale — it caches on a slower cycle than `get_aged_receivables`, which tends to refresh live on each call. Before trusting `cash_balance`, compare `get_cash_position`'s `last_refreshed` against `get_aged_receivables`'s `as_of_date`/`last_refreshed`. If cash_position is older, do not use its number — instead sanity-check with Neil (he can see Revolut directly) or note the figure as stale and flag it on the dashboard rather than presenting it as current. Always state the actual `last_refreshed` date on the dashboard next to the cash figure.
   - **Accounts receivable tile — Xero MCP `get_aged_receivables`.** Pull `total_outstanding`, `overdue_total`, and the `top_debtors`/`aged_receivables` list. Surface each named invoice with its due date, especially ones that read as a payment plan or Direct Debit schedule (e.g. "Bronze Package - Payment 2/3", "Payment Plan Option A - Deposit") — these are client DDs Neil wants visibility on. List them individually with amounts and due dates, not just the total.
   - **Accounts payable / COGS forecast tile — Airtable `M&MOM Database` base, `Editor Pipeline` table** (`search_bases` → `list_tables_for_base` → `list_records_for_table`, baseId `app077Z4RXX1PShzN`, tableId `tblWkRNY5rcvthBMs` as of 2026-08 — re-resolve via search if these IDs ever 404). For each record with a non-empty `Budget` field, check `Payment status` (field "Payment status": Unpaid/Paid/Logged in Xero). Sum all records where Payment status is NOT "Paid" — that's the forecast editor cost still owed. Split the total by whether `Session Date` is set (dated = a real near-term forecast, grouped by month) vs unset (still TBC, held separately). Note the `Editor` field per record if Neil wants a per-editor breakdown. Flag any record with a `Date Created` or `Session Date` that looks stale (e.g. more than ~60 days old and still unpaid) as worth double-checking rather than trusting blindly.
   - Together these three — cash in bank, accounts receivable (what's coming in, including DD schedule), accounts payable/COGS forecast (what's going out to editors) — give Neil a simple near-term cash picture. State it as one plain sentence in the hygiene line under the payable box, not a full P&L.
   - Money tiles — Xero MCP: `get_cash_position` and `get_profit_and_loss` (current month to date vs last full month). "Signed, not yet invoiced" = recently signed clients at list price from the 3-tier offer, minus anything now invoiced. Before flagging a low "invoiced this month" figure as a problem, cross-check Airtable Lead Status: "Won - Recent" means the client has actually paid (often via Stripe), even if it hasn't shown up cleanly in Xero yet — don't read Xero alone as "nothing billed"
   - Pipeline bar + tiles + Hot list table — live Airtable Full CRM (Temp field; the live hot count excludes Lost and already-signed clients still tagged Hot). Don't hard-code "Nine" anywhere — state the actual current count, it drifts as leads close or die. If the Airtable connector is unavailable this refresh, say so on the dashboard and carry over last-known figures rather than guessing.
   - Rest-of-week strip — remaining days from the weekly plan
   - Audience tiles — newsletter subscribers auto-pull from the Kit MCP (`get_growth_stats`) every refresh now that the connector is live; LinkedIn/Insta stay manual — only fill if Neil gave numbers in a voice note
   - Goals panel — only when the growth strategy or monthly priorities change
   - Tonight/wins panel — wins from the latest daily log entry
   - In the `<script>` block: set `var DAY = 'mmom-YYYY-MM-DD'` to today's date so the tick-boxes reset each morning
2. Data only. Never restructure the page, change the design system, or rename the file. Keep `:root { color-scheme: light }` in the stylesheet — required for Cowork artifacts.
3. Copy the updated source file to the scratch/outputs directory, then republish with `mcp__cowork__update_artifact`, `id: "mmom-mission-control"`, pointing `html_path` at that copy. Keep the title "MMOM Mission Control".
4. If the artifact tools aren't available in the session, say so plainly and skip — never publish under a different id.
5. Trello: Neil has a Trello workspace but no boards or cards set up yet (checked 2026-07-17). He wants stray non-CRM tasks pulled onto the dashboard leaderboard eventually — revisit once he's actually using Trello, don't build this yet.

In the Friday EOD flow, ask Neil for the three funnel numbers ("newsletter X, LinkedIn X, Insta X") so Monday's dashboard has a live audience row.

---

## WHAT THIS SKILL NEVER DOES

- Never invents leads or family names not in the CRM
- Never rewrites the growth strategy
- Never chases parked leads — inbound only unless CRM says otherwise
- Never puts Instagram, website tweaks, LinkedIn automation, or new IP into any plan
- Never produces motivational content — only executable actions
- Never saves daily briefings to file unless Neil explicitly asks

---

## SUCCESS CRITERIA

A good weekly plan: Neil wakes up Monday, reads it in 2 minutes, and knows exactly what to do first.

A good daily briefing: Three actions. One "if you only do one thing." Inbox clear. Done in 2 minutes.

A good EOD log: The voice note is captured, the day is recorded, tomorrow has a clear number one.

