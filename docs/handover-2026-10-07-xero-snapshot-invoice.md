# Handover: Xero invoice for Snapshot Founding Five (7 Oct 2026)

**Update, 7 Oct evening: invoices are no longer part of the flow.** The Kit email now has a "Pay £99" button linking to a reusable Revolut Business payment link (https://checkout.revolut.com/payment-link/a6fc1035-9010-4980-85b9-4464b78b4804). Payments come into Xero through the bank feed. Code them to the `SNAP-F5` item / 200 Sales, No VAT. The rest of this doc only matters if someone needs a formal invoice.

For a new session, or for Neil doing it by hand. The goal is one £99 invoice per Founding Five, raised the same way every time.

## Context

- Someone confirms on https://www.meandmyoldman.co.uk/snapshot-f5k. Kit tags them `snapshot-founding-five`, and the sequence "Snapshot Founding Five: confirmed" sends the email. That email says the invoice comes separately from Xero, and links to the Calendly booking page.
- The invoice is the missing step. Xero has no single payment link that works for everyone, so each person needs their own invoice.
- Card payment already works. Chuck Baumberg's invoices (6 Oct) used "Pay now", by card, through Revolut Business.
- The Xero connector in Claude Code can read data but can't create invoices. To do this in a session, either authorise the small-business Xero plugin in claude.ai connector settings, or drive Xero through Claude in Chrome.

## One-off setup (5 minutes)

1. In Xero, go to **Business > Products and services > New item**.
   - Code: `SNAP-F5`
   - Name: Snapshot, Founding Five
   - Description: "Snapshot: a 1h30 recorded conversation, edited into about an hour of audio plus video, delivered within 7 days. Founding Five price, video included."
   - Sell price: **£99.00**
   - Account: the same sales account as the family documentary invoices
   - Tax rate: **No VAT** (zero tax). Confirmed by Neil, 7 Oct 2026.
2. Open one of Chuck's invoices and check that the online payment option (card through Revolut) is set as the default for the branding theme. If it is, every new invoice gets "Pay now" automatically.

Don't use Xero's "Repeating invoice" feature. That's for schedules like Chuck's monthly payments, not a template.

## For each person (2 minutes)

1. **Business > Invoices > New invoice.**
2. Contact: first and last name, plus the email from the Kit tag list. Create the contact if it's new.
3. Issue date: today. Due date: **3 days**, so it's paid before the session.
4. Reference: `SNAP-F5-[SURNAME]`
5. Item: `SNAP-F5`. Quantity 1, and the £99 fills itself in.
6. Check that "Pay now" is switched on.
7. **Approve and email.** Subject: "Your Snapshot invoice, Me & My Old Man". Message: "Here's your invoice for your Snapshot. Hit Pay now to pay by card. Booking link is in my other email. Neil"

## Who to invoice

| Name | Status | Invoice |
|---|---|---|
| Emma Fletcher | Booked, next Wednesday. Counts as one of the five, not paying | none |
| Sam Ulph | Said yes, link sent. Neil wants him to confirm through the landing page himself, so the full flow gets tested | raise once he is tagged in Kit |
| Stefan Cataldo | Said yes. Confirms through the landing page himself, same as Sam | raise once he is tagged in Kit |
| 2 to 3 more | Being chased 7 Oct. Five or six is fine, per Neil | |

## After payment

- Mark as paid in Xero. If the payment comes through Revolut, it reconciles automatically.
- Send the reflection form. It isn't built yet.
- Margin note: £99 is below the £145 full cost. Per pricing.md that's deliberate marketing spend, capped at five.
