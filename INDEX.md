# Index

## In the brain

| Area | Path | What it holds |
|---|---|---|
| Identity | `README.md` | Who Neil is, beliefs, customer, voice |
| Voice | `knowledge/voice/VOICE_PROFILE_Neil_Taylor.md` | Master voice profile and brand rules |
| Voice of customer | `knowledge/voice/VOC_Intelligence_System.md` | VoC intelligence system |
| Offer | `knowledge/offer/pricing.md` | Confirmed per-parent ladder, Sept 2026 |
| Lessons | `knowledge/lessons.md` | Every correction Neil has made, logged as rules |
| Systems | `knowledge/systems-map.md` | Which tool connects to what |
| Skills | `skills/` | 23 skills: content, sales, delivery, ops |
| Automations | `workflows/scheduled-tasks/` | 22 scheduled tasks |

## Skills by job

**Content** — linkedin-post, linkedin-engagement, instagram, newsletter, lead-magnet, mmom-carousel, mmom-visual, alex-hormozi-youtube

**Sales** — mmom-sales-strategist, mmom-voice-check, proposal, mmom-follow-up, mmom-podcast-pr

**Delivery** — new-client, client-folder-setup, onboarding-complete, client-onboarding-complete, mmom-onboarding, editor-briefing

**Ops** — morning, mmom-weekly-action-plan, mmom-voice-profile-refresh, form-response-to-doc

## Still living outside the brain

These are the next things to pull in or decide about.

- **Claude.ai synced skills** at `~/.claude/skills/synced/...` — as of 22 Sep 2026 every skill in `skills/` is symlinked into `~/.claude/skills/`, so Claude Code runs the repo copy and edits here are live. The Claude.ai web app still runs its own synced copies and will drift until they are re-uploaded by hand.
- **Drive Cowork folder** `Google Drive/My Drive/Mega Claude Cowork/` — as of 22 Sep 2026 its CLAUDE.md and lessons log are frozen pointers to this repo, and the 34 lessons were imported to `knowledge/lessons.md`. It stays the home for assets: `About Me/`, `Projects/`, `Templates/`, `Proposals/`, and `Claude Outputs/` for anything Claude writes there. Skills there are still duplicated and will drift.
- **Airtable CRM** `apprk3RUXdvZNJ8TF` — live operational data. Stays in Airtable, but the brain should hold a schema note.
- **client-handover skill** at `~/.claude/skills/client-handover` — local only, not synced, not yet copied.
- **Advisor corpora** at `~/src/advisors/` — distilled Alex Hormozi, Chris Donnelly, Lara Acosta and Matt Gray teaching, kept current by four weekly scheduled tasks (`workflows/scheduled-tasks/*-sync`). Reference libraries, not Neil's own thinking — left where they are, per `docs/handover-what-to-feed-the-brain.md`.
- **HyperFrames video skills** — general tooling, probably does not belong in the brain.
- **Google Docs** — warm leads playbook, sales scripts, JournoRequest tracker, music library and image bank sheets. Referenced, not mirrored.
