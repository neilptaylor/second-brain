# Handover: closing the end-to-end system gaps

Written 22 September 2026. For a fresh session. Read this plus `knowledge/systems-map.md` and you have everything you need.

## Context

Neil runs Me & My Old Man, a 12-week audio documentary experience for families. The business runs in stages held in Google Drive at `Shared drives/Systems`, numbered 00 Strategy through 08 Delivery & Referrals.

This second brain at `~/my second brain` was populated on 22 September 2026 as the single home for the business: 23 skills, the voice profile, the voice-of-customer system, 22 scheduled automations, confirmed pricing, and a map of the whole system.

An audit of every stage against the skills and automations supporting it found four uncovered stages and two structural problems. That is the work.

## Before doing anything

1. Read `CLAUDE.md` in the repo root. The voice rules are non-negotiable, especially no em dashes.
2. Read `knowledge/offer/pricing.md`. Options A to D, not Bronze / Silver / Gold. Never quote a price from memory.
3. Read `knowledge/systems-map.md`. That is the audit this handover acts on.
4. Check whether the skills in `skills/` have been symlinked into `~/.claude/skills/` yet. If not they are inert files, and any new skill needs the same treatment to actually run.

## The work, in priority order

### 1. Enquiry, the highest-value gap

`Shared drives/Systems/02 Enquiry` holds four files and no skill. Awareness has nine skills, Sale has four, Enquiry has zero. It is the narrowest point in the funnel and the least supported.

What exists: a One Deck hit list, a pre-discovery "what to expect" video, and a VSL Calendly email workflow doc. Read all three before designing anything.

Two known holes inside this stage:
- Nothing drafts or qualifies the reply when someone raises a hand.
- Nothing is sent between the Discovery call and the Sales Call. Neil's own plan is a price-reveal VSL at T-3 days, framed as "Watch this before we chat." That plan has never been built.

Likely shape: one `mmom-enquiry` skill covering first response, qualification against the Sarah profile in `README.md`, and the between-calls sequence. Check the CRM (Airtable base `apprk3RUXdvZNJ8TF`) for what enquiry data already exists before inventing fields.

### 2. Collections, the only stage with nothing at all

`Shared drives/Systems/04 Collections` is an empty folder. No invoice trigger, no payment chase, no deposit terms, no failed-payment path. Xero is connected as a tool and no skill touches it.

Ask Neil these before building, because they are business decisions and not inferable:
- Deposit versus payment plan versus full payment up front, per option.
- What happens when a payment fails or a family goes quiet mid-project.
- Whether invoices should be raised on sale or on a schedule.

There is an existing `Gmail invoices to Xero automation` session in Neil's history and a `Xero_Reclass_Handover.md` in his home folder. Both are worth reading, they may already solve part of this.

### 3. Post production, a dead stage

`Shared drives/Systems/07 Post Production` has two documents, one from January 2025 on adding artwork, one from February 2025 on emailing the audiobook to the client. Everything between the editor delivering and the family receiving is in Neil's head.

This is mostly an extraction job. Get Neil to talk through one real recent delivery end to end, write it down, then decide what deserves automating.

### 4. Strategy, folders rather than a system

`00 Strategy` holds Campaigns, Core, Grief and Book as storage. The `mmom-weekly-action-plan` skill plans a week but nothing connects the quarter's strategy to what that week actually contains. Lowest urgency of the four, but it is why the weekly plan can drift from the actual plan.

## Two structural problems underneath

**Follow-ups are hardcoded per person.** There are eight scheduled tasks named after individual prospects: two for Owain, two for Rambo, Petts, and three email3 tasks for named people. That is a missing pattern showing itself. It should be one follow-up engine reading the CRM, not one task per human. Fixing this removes eight fragile things and replaces them with one.

**Onboarding has four overlapping skills.** `onboarding-complete`, `client-onboarding-complete`, `mmom-onboarding`, `new-client` and `client-folder-setup`. Some are genuinely different jobs, the front-of-project editor folder versus the family's own folder versus hiring a team member. Some are duplicates that arrived from different homes. Untangle before building anything on top. Do not delete until each one's real job is confirmed with Neil.

## One thing to fix in passing

Every SOP in `05 Onboarding` is still named Bronze, Silver or Gold. Those tiers no longer exist. Any document naming a tier is describing an offer Neil does not sell. Worth a sweep once the higher-priority work is done.

## How to work

Neil wants plain explanations, not jargon. Explain things the way you would to a bright eleven-year-old, using everyday comparisons. He is a poet who learned business, not an engineer. He is sharp and will spot hedging.

Do not build all four at once. Enquiry first, on its own, finished properly.
