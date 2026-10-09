# Handover: move meandmyoldman.co.uk off Squarespace (9 Oct 2026)

For a new session, or for Neil doing it by hand. The goal is to drop Squarespace as a tool. The website is on Lovable, but the domain is still registered at Squarespace, and Squarespace is also where the DNS records live.

## Context

- 9 Oct 2026: a Snapshot sign-up (Geoff) got the Kit emails in junk, tagged "Unverified". Cause: the domain had never authorised Kit to send on its behalf. Fixed the same day by updating three Kit CNAMEs in Squarespace DNS (`ckespa`, `cka._domainkey`, `cka2._domainkey`). Kit validated, and now reports DMARC configured. That fix is done. Do not redo it.
- Those records sit in Squarespace DNS. If DNS moves, they must move too, or the Kit problem comes straight back.
- Squarespace account page says: renews 24 Oct 2026 for €18, auto-renew on, domain lock on. The domain list says expiration 8 Nov 2026. These two dates disagree. Check which one is right before relying on either.

## What lives in Squarespace DNS today (must all carry over)

- Google Workspace: five MX records (`aspmx.l.google.com`, `alt1` to `alt4`), two Google site verification TXT records, the `google._domainkey` DKIM TXT.
- SPF TXT on `@`: `v=spf1 include:_spf.google.com include:_spf.squarespace.com ~all`
- DMARC TXT on `_dmarc`: `v=DMARC1; p=none;`
- Lovable website: A records for `@` and `www` pointing to `185.158.133.1`, plus TXT `_lovable` and `_lovable.www`.
- Kit: the three CNAMEs above.
- Mailchimp leftovers: CNAMEs `k2._domainkey` and `k3._domainkey`. Probably dead, leave them until Neil confirms Mailchimp is gone.

## Cost: Squarespace vs Cloudflare

| | Squarespace | Cloudflare Registrar |
|---|---|---|
| .co.uk renewal | €18 a year (about £15.50). Read from Neil's account on 9 Oct. | About $5.30 a year (about £4). From a third-party price tracker, not Cloudflare itself. Confirm at checkout. |
| Transfer in | n/a | No fee. Cloudflare's docs say no extra year is added. |
| DNS hosting | Included | Free |
| Likely saving | | Roughly £11 a year, about £11 over the next renewal alone |

Notes:
- Cloudflare says it charges the registry price with no markup, so the price should stay flat. UK VAT may be added at checkout. Check the final figure.
- Currency conversions are rough.
- Cloudflare is also the better home for DNS: faster, free, and a proper record editor. Squarespace asks for a Google re-login before every DNS edit.

## Steps

Do these in order. The order matters for .co.uk.

1. **Check the real expiry date.** Squarespace overview says 24 Oct, the list says 8 Nov. Whichever is first is the deadline. If it expires before the transfer lands, the domain, website and email all stop.
2. **Create a Cloudflare account** and add `meandmyoldman.co.uk` as a site (free plan). Cloudflare scans and imports the existing DNS records.
3. **Compare the import to the list above, record by record.** Add anything missing by hand. Check that the MX, TXT and CNAME records match exactly. Lovable A records and Kit CNAMEs should be set to "DNS only" (grey cloud), not proxied.
4. **Do not change nameservers yet.** Cloudflare will show two nameservers. Leave Squarespace's nameservers in place until step 8.
5. **Start the transfer in Cloudflare:** Domain Registration, Transfer Domains, select the domain, go to checkout. Pay. There is no transfer fee. Do this **before** step 6. A tag change requested before checkout gets the transfer auto-rejected.
6. **Ask Squarespace to change the IPS tag to `CLOUDFLARE`.** .co.uk domains use an IPS tag change at Nominet, not an auth code. Squarespace support may need to do this for you. In the Squarespace domain page, "Transfer domain" is the place to start, and the domain lock may need turning off. If nothing happens within 24 hours, ask again. The request cancels itself after 30 days.
7. **Wait for Cloudflare to confirm the transfer.** Usually a few days.
8. **Switch nameservers** at Cloudflare to the two it gave you, once it is the registrar. Check DNS has propagated.
9. **Test everything.** Send an email to and from neil@meandmyoldman.co.uk. Load https://www.meandmyoldman.co.uk. In Kit, Settings, Email, confirm the sending domain still shows verified. Submit the Snapshot form with a test address and check the Kit email lands in the inbox, not junk.
10. **Turn off Squarespace auto-renew** and cancel the Squarespace account only after step 9 passes.

## Watch-outs

- A domain transferred into Cloudflare is locked for 60 days before it can move again. Not a problem, just know it.
- Auto-renew at Squarespace charges €18 on 24 Oct if the transfer has not landed. That is an acceptable fallback, better than a lapse.
- The `_spf.squarespace.com` entry in the SPF record is likely unneeded once Squarespace is gone, but remove it only after checking nothing else sends through Squarespace.
- Cloudflare's .co.uk support and pricing came from search results. Confirm both on the Cloudflare transfer page before paying.
- If Cloudflare does not accept .co.uk on the day, Porkbun and Namecheap are the fallbacks. Same IPS tag process.

## Needs Neil

- The payment at Cloudflare checkout.
- Possibly a support request to Squarespace for the tag change.

## Sources

- Cloudflare docs, transfer a .uk domain: https://developers.cloudflare.com/registrar/get-started/transfer-uk-domain/
- Cloudflare TLD policies: https://www.cloudflare.com/tld-policies
- Price tracker (third party, July 2026): https://domainoffer.net/tld/co.uk/cloudflare
