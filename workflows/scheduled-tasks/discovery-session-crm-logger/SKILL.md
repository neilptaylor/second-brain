---
name: discovery-session-crm-logger
description: Logs new Calendly 30/20-min Family Story Discovery Session bookings into the Full CRM Airtable and creates the client's Sales Call Drive folder.
---

You are checking Neil's Gmail for new Calendly "Family Story Discovery Session" bookings and logging them into his CRM and Drive.

## 1. Find matching emails
Search Gmail (search_threads on connector ffce937d-12cb-4a5b-bc52-2321647acf20) with a query like:
`from:notifications@calendly.com subject:(discovery session) newer_than:1d`
This catches subjects like "New Event: [Name] - [time] - 30min Family Story Discovery Session" or "...20min Family Story Discovery Session". Only process emails whose subject contains "Family Story Discovery Session" (30min or 20min, or "30 minute"/"20 minute" phrasing). Ignore cancellation/reschedule notification emails (subject starts "Canceled Event:" or "Rescheduled:") — only act on "New Event:" bookings.

For each matching thread, call get_thread (messageFormat FULL_CONTENT) to get the full body.

## 2. Extract from the email body
- Invitee First Name and Last Name (from "Invitee:")
- Invitee Email
- Phone number (answer to "What is your phone number?")
- Lead source (answer to "How did you hear about us?")
- Reasons why / context (answer to "Please share anything that will help prepare for our chat...")
- Booked event date (from "Event Date/Time:", e.g. "16:00 - Thursday, 6 August 2026") — convert to YYYYMMDD for folder naming
- Session length (30min or 20min) for the "Last Action" note

## 3. Dedupe check (IMPORTANT — do this before creating anything)
Airtable base "M&MOM Database" (baseId app077Z4RXX1PShzN), table "Full CRM" (tableId tblFy3hGmEDRBgExi).
Call list_records_for_table filtered on Last Name (fldXw4FwKXgoqydqW) = the extracted last name. If a record already exists with that Last Name AND matching Email (fldx2HNmBbCFg5zyU) or Phone (fldMxrQYaIuNYHNlG), skip creating a new CRM record for this person (already logged) — but still check step 4 for the Drive folder independently, since the folder might not have been created yet even if the CRM record exists.

## 4. Create the CRM record (only if not a duplicate per step 3)
create_records_for_table on the same base/table with fields:
- fldXw4FwKXgoqydqW (Last Name): extracted last name
- fld0VQIeWc8V3BBKm (First Name): extracted first name
- fld3MSSKTM73LOCXY (Lead Status, singleSelect): "In Discussion"
- fldqSA7Xkn7fM9HLO (Temp, singleSelect): "Hot"
- fldx2HNmBbCFg5zyU (Email): invitee email
- fldMxrQYaIuNYHNlG (Phone): phone number
- fldnzOYkCUH7QFAUh (Lead Source): the "how did you hear about us" answer
- fld3wl956E80OSGcd (Notes / Comments): the reasons-why text (include any co-signer/gift-giver names mentioned)
- fld3QpJ7HE9DphNEU (Last Action): "Booked [30min/20min] Family Story Discovery Session via Calendly"
- fldfvJnxKCLUiabxY (Last Action date): today's date (YYYY-MM-DD)
- fld3LAYeeoYQq6sgb (Next Action Date): the booked call date (YYYY-MM-DD)

## 5. Create the Drive folder (only if it doesn't already exist)
Search Drive (search_files, connector 04e9ba0e-2617-42ef-ae1a-45896d238f63) for a folder titled "YYYYMMDD FirstName LastName" (booked call date, not today) with parentId '1ba_mqJkb95u7l8aI2UMcGN4cGkuc1MF3' (this is .../Systems/03 Sale/02 Sales Call/). If none exists, create_file with mimeType application/vnd.google-apps.folder, that title, and that parentId.

## 6. Report
At the end, summarize what was processed this run: how many matching emails found, how many new CRM records created (name + record ID), how many Drive folders created (name + folder ID), and how many were skipped as duplicates. If no matching emails were found this run, just say so briefly — don't create a verbose report for a no-op run.

## Reference / already done manually
Gemma Hughes (booked 6 Aug 2026, 30min session) was already logged manually on 2026-07-24: CRM record recXs6RtFYdP3MMFy, Drive folder 1tBjkNXrlTBWKRK1f630NKr1LsIB0rajP ("20260806 Gemma Hughes"). Do not recreate these if her booking email is seen again — the dedupe check in step 3 should catch her by Last Name + Email match.

## Notes
- Neil considers "sales calls" and "discovery calls" the same thing — always use the CRM's "In Discussion" / "Hot" values as specified above, don't invent new status values.
- Don't mark emails as read or otherwise modify the Gmail thread — dedupe is handled entirely via the Airtable and Drive existence checks above, since label-write permissions aren't available to this task.