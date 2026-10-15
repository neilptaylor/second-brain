---
name: inbound-weekly-scan
description: Thursday 8am: runs the inbound skill over the last 8 days of Gmail, updates Airtable, drafts the three-touch drip in Gmail and adds Trello cards with deadlines.
---

Cron: `0 8 * * 4` (local time). Lives in the scheduled-tasks app as `inbound-weekly-scan`. The prompt there says: read CLAUDE.md, run `skills/inbound/SKILL.md` end to end, scan 8 days of Gmail, never send, never use Zapier. The method lives in the skill, not here.
