---
name: questions-lead-crm-logger
description: Hourly: logs new Kit subscribers tagged "107 Questions" (homepage lead magnet, via Lovable→Kit) into the Full CRM Airtable base apprk3RUXdvZNJ8TF. Replaces the old Zapier "Kit LP To Airtable" Zap.
---

You are logging new Kit lead-magnet subscribers into Neil's Full CRM Airtable. This replaces the old Zapier "Kit LP To Airtable" Zap.

## 1. Fetch tagged subscribers from Kit
Kit MCP connector: 90367ace-ea6f-4fd4-ad1b-cfc01223e841.
Call list_subscribers_for_tag with id 18943262 (tag "107 Questions" — the "Send me the questions" lead magnet on the Me & My Old Man homepage / Lovable site, wired via the Lovable→Kit connector), per_page 100. Paginate with `after` while has_next_page is true. Each subscriber returns id, email_address, first_name, state, created_at, tagged_at.

Only consider subscribers whose created_at is within roughly the last 3 days (older ones are already handled). state must be "active".

## 2. Skip Neil's own test signups
Ignore any subscriber whose email is neil.p.taylor1@gmail.com, tayls13@gmail.com, or ends in @meandmyoldman.co.uk. Don't create CRM records for them and don't report them as missing.

## 3. Dedupe against Airtable
Airtable base "M&MOM Database" — baseId apprk3RUXdvZNJ8TF, table "Full CRM" tableId tblFy3hGmEDRBgExi, Email field fldx2HNmBbCFg5zyU.
(NOTE: the old baseId app077Z4RXX1PShzN is dead / inaccessible — do not use it.)
Run ONE list_records_for_table call with an OR filter of `contains` conditions on fldx2HNmBbCFg5zyU, one per candidate email. Any email that comes back already has a record — skip it, don't modify existing records.

## 4. Create CRM records for the genuinely missing ones
create_records_for_table on apprk3RUXdvZNJ8TF / tblFy3hGmEDRBgExi, one record per missing subscriber, fields:
- fld0VQIeWc8V3BBKm (First Name, multilineText): subscriber's first_name. If it contains a space (e.g. "Paul DeGregorio"), put the first token here and the rest in Last Name. If blank, use "Unknown".
- fldXw4FwKXgoqydqW (Last Name, singleLineText / primary): surname if split out per above, else leave blank.
- fld3MSSKTM73LOCXY (Lead Status, singleSelect): "New"
- fldqSA7Xkn7fM9HLO (Temp, singleSelect): "Warm"
- fldx2HNmBbCFg5zyU (Email): subscriber's email_address
- fldiUXRktA5yLnKba (Tag, multipleSelects): ["107Q Website"]  (exact existing option — don't create a new one)
- fld3QpJ7HE9DphNEU (Last Action, singleLineText): "Downloaded 107 Questions lead magnet (Kit)"
- fldfvJnxKCLUiabxY (Last Action date, date): today's date, YYYY-MM-DD
- fldnzOYkCUH7QFAUh (Lead Source, multilineText): "107 Questions lead magnet (Kit / Lovable site)"
Do not invent any other Lead Status / Temp / Tag option values.

## 5. Report
Briefly: how many "107 Questions" subscribers seen in the last 3 days, how many already in CRM (skipped), how many test emails ignored, how many new records created (name/email + record ID). If nothing new, say so in one line.

## Context
Backfill done manually 2026-09-10: 31 subscribers from 2026-09-10 (Jonathan Page through Steve Scharf) were added to the CRM by hand after the task was found to be writing to the dead old base. Runs from 2026-08-29 to 2026-09-10 silently failed for that reason. From this run on, the task points at the correct base.
