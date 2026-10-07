# End-to-end system map and gaps

The business runs in stages in `Shared drives/Systems`. This maps each stage to the skills and automations that support it, and names what is missing.

## Coverage

| Stage | Drive folder | Skills | Automations | State |
|---|---|---|---|---|
| Strategy | 00 Strategy | mmom-weekly-action-plan, morning | none | Thin. Campaigns, Core, Grief, Book all sit as folders with no skill behind them |
| Awareness | 01 Awareness | linkedin-post, linkedin-engagement, instagram, newsletter, lead-magnet, mmom-carousel, mmom-visual, mmom-podcast-pr, alex-hormozi-youtube | journorequest-watch, 3 advisor YouTube syncs | Strongest stage by far |
| Enquiry | 02 Enquiry | none | discovery-session-crm-logger, questions-lead-crm-logger | **Weakest stage.** Four files and no skill |
| Sale | 03 Sale | proposal, mmom-sales-strategist, mmom-voice-check, mmom-follow-up | 8 named follow-up tasks, onboarding-call-followup-scheduler | Covered around the call. The call itself runs off master scripts in Drive, see `knowledge/offer/sales-call-scripts.md`. Follow-ups are hardcoded per person |
| Collections | 04 Collections | none | none | **Empty folder. No system at all** |
| Onboarding | 05 Onboarding | onboarding-complete, client-onboarding-complete, new-client, client-folder-setup, mmom-onboarding | editor-pipeline-session-logger | Covered, but four overlapping skills doing adjacent jobs |
| Production | 06 Production | editor-briefing | interview-briefing-watcher, fathom-transcript-filer | Covered |
| Post production | 07 Post Production | none | none | **Two docs from January 2025. No skill** |
| Delivery and referrals | 08 Delivery & Referrals | client-handover | wrapup-date-watcher, wrapup-brief-check | Covered |

## The four real gaps

**1. Enquiry has no skill.** The stage between someone raising a hand and a discovery call being booked is the narrowest point in the funnel and it is unautomated. The VSL workflow doc exists, the pre-discovery video exists, but nothing drafts the reply to an enquiry, qualifies it, or moves it. The known between-calls VSL gap sits here too: nothing is sent between Discovery and the Sales Call.

**2. Collections is completely empty.** No invoice trigger, no payment chase, no deposit terms, no failed-payment path. Money is the one stage with zero system. Xero is connected and unused by any skill.

**3. Post production is a dead stage.** Two documents, both from January and February 2025, covering artwork and emailing the audiobook. Everything between the editor delivering and the family receiving is tribal knowledge.

**4. Strategy is folders, not a system.** Campaigns, Core, Grief and Book are storage. The weekly action plan skill plans the week but nothing connects the quarterly strategy to what the week actually contains.

## Structural problems, not stage gaps

- **Follow-ups are hardcoded per person.** There are eight scheduled tasks named after individual prospects. That is a symptom of a missing pattern: one follow-up engine reading the CRM, not one task per human.
- **Onboarding has four overlapping skills.** onboarding-complete, client-onboarding-complete, mmom-onboarding and new-client plus client-folder-setup. Some are duplicates from different homes, some are genuinely different jobs. Needs untangling before anything is built on top.
- **Tier language is stale everywhere outside this repo.** The Onboarding folder still has Bronze, Silver and Gold SOPs. Pricing is now options A to D. Every SOP referencing a tier name is wrong. The repo's own skills were swept clean on 22 Sep 2026, see `docs/drive-skill-sync-2026-09-22.md`, but the Drive SOPs have not been touched.

## Lead source tracking (added 6 Oct 2026)

- **Airtable Full CRM is the master.** Every lead gets `Lead Source` (dropdown: LW Email Campaign, LinkedIn Engagement, LinkedIn Inbound, DM Outbound, Instagram Inbound, Lead Magnet (107 Questions), Kit Newsletter, Podcast, Referral, Talk / Event, Google, Press / Magazine, Other) and `Knows Me` (Knows personally, Knew of me, Stranger). Channel and relationship are separate on purpose: an old contact who came via a LinkedIn post is LinkedIn Inbound + Knows personally.
- Tick-boxes `Discovery Call`, `Sales Call`, `Won` carry each lead's funnel. Back-filled from the Sales Conversion tab.
- `Referred By` holds the referrer name or publication.
- `Contact Type` (added 6 Oct 2026): Client family (parents, siblings, partners on a client project) and Test rows are not leads and are left off the Lead Source tab. Blank means Lead. A client's buyer is a Lead with Won ticked. Kit's Seg: Past Clients and Seg: In Progress tags are the client list to check new rows against.
- Kit (322 subscribers, 6 Oct 2026) will never equal the lead count: about 109 are clients and family, and leads who came by DM, LinkedIn or referral may never join the list.
- The old free-text field is kept as `Lead Source (old text)` for reference only.
- New leads go in with Lead Status "In Discussion".
- The `Lead Source` tab of the Lead Gen sheet (`1hlBVSI4k-sZdJW3Y_KgSzD4yuraPl07zUv4dO3Y7tcs`) is a report, refreshed every Monday 7am by the `lead-source-sync` scheduled task, or on request ("refresh lead sources").

## Calendly booking links (logged 7 Oct 2026)

All under `https://calendly.com/meandmyoldman/`. Individual slots hyperlink as `<link>/<UTC start time>`, for example `30min-connect/2026-10-13T16:00:00Z`.

- `15min-connect`, `20min-connect`, `30min-connect`: the "connect" set, for friends and network (Vinesy, 7 Oct). Use `30min-connect` as the open-diary link at the end of a friend email.
- `20min-family-story-discovery-session`, `30min-family-story-discovery-session`: discovery calls for leads.
