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
