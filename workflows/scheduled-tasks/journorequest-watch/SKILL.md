---
name: journorequest-watch
description: Scans X hashtag #journorequest each morning for requests relevant to MMOM's business area and drafts a Gmail digest.
---

You are running a scheduled daily scan for Neil Taylor, founder of Me & My Old Man (MMOM) — a company that produces audio documentaries capturing family stories, mainly interviews with aging parents/grandparents, for their children as gifts.

STEP 0 — TOOLS: This task uses the Chrome browser extension (mcp__claude-in-chrome__* tools), not the built-in browser. Call ToolSearch with query "select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find,mcp__claude-in-chrome__form_input" before starting. You'll also need the Gmail MCP (mcp__ffce937d-12cb-4a5b-bc52-2321647acf20__create_draft) and the Claude Docs MCP (mcp__1a59c906-04da-521d-bda7-7f71b9f9e01c__*) — load the docs guide with topic.instructions before creating any doc.

STEP 1 — SCAN X: Using the Chrome extension, open a new tab and navigate to https://x.com/hashtag/journorequest?f=live (most recent tab). Neil's Chrome is expected to already be logged into X. If not logged in, stop, do not log in yourself, and report that login is needed. If logged in, read through the most recent ~50-100 posts under #journorequest (scroll, use get_page_text / read_page), covering roughly the last 24 hours.

STEP 1B — GIFT GUIDE HASHTAG SCRAPE (added 18 Sep 2026, confirmed by Neil): also scan the gift-guide hashtags below, since journalists soliciting gift-guide ideas often skip #journorequest entirely. Search X for a combined query covering the last 24 hours, e.g. navigate to a URL like `https://x.com/search?q=%28%23GiftGuide%20OR%20%23ChristmasGiftGuide%20OR%20%23HolidayGiftGuide%20OR%20%23ChristmasGiftIdeas%20OR%20%23HolidayGiftIdeas%20OR%20%23ChristmasGifts%20OR%20%23GiftIdeas%20OR%20%23HolidayGifts%29&f=live` (or split into a couple of OR-grouped queries if X truncates the query). Hashtags: #GiftGuide, #ChristmasGiftGuide, #HolidayGiftGuide, #ChristmasGiftIdeas, #HolidayGiftIdeas, #ChristmasGifts, #GiftIdeas, #HolidayGifts.

STRICT FILTER for this hashtag group only (these tags are used extremely broadly, year-round, by brands, PR agencies, published-article bots, and randoms sharing their own gift picks — none of that counts): only flag a post if it is a **media outlet, journalist, editor, or producer actively soliciting product/idea submissions from readers or PR contacts** — i.e. they are asking for ideas so they can build a feature, not publishing/promoting one themselves. Apply the same theme filter and the two hard exclusions below to whatever passes this strict check. When genuinely unsure whether a post is a solicitation vs. self-promotion, skip it — this hashtag group needs a tighter bar than #journorequest, not a looser one.

FILTER: Flag any request a journalist/producer/podcaster/newsletter writer has posted that touches on ONE OR MORE of these themes (match on spirit, not just exact keywords):
- Families, parenting, parent-child relationships
- Aging parents, aging, older generations, "olderhood", elder care
- Grief, loss, bereavement
- Personal/life stories, biographies, autobiographies, oral history, memoir
- Christmas gift ideas, Mother's Day gift ideas, Father's Day gift ideas (especially sentimental/experience gifts)
- Unique/meaningful experiences, experience gifts
- Legacy, family history, recording memories, interviewing relatives

Ignore anything unrelated and ignore requests with deadlines already passed.

TWO HARD EXCLUSIONS even when a request matches a theme above (confirmed by Neil, 18 Sep 2026 — he rejected matches that broke these):
1. **No estrangement/family-breakdown angles.** MMOM's positioning is the opposite of this: capturing stories while relationships are close and present, not repairing or dwelling on distant/broken ones. Skip any request framed around regret, estrangement, children who "never see their parents anymore," family rifts, etc. — even if it superficially touches "parent-child relationships." (Rejected example: a Telegraph request for a parent who sent their child to boarding school and now regrets it, estranged from the child.)
2. **No pure "conduit" requests.** Skip requests that only ask Neil to introduce/refer a third-party case study he has no personal stake in — e.g. "know someone who did X, DM me" asks where MMOM/Neil gets no feature, credit, or mention even if he happened to know someone. Neil gets nothing from being a middleman. Only flag a match if MMOM's own product, story, or expertise can plausibly be the thing featured (gift guides where MMOM's audio documentaries are pitched as the product; requests for expert commentary where Neil himself would be quoted/credited; "know a business that does X" style pitches where MMOM is the business). (Rejected examples: a freelance journalist's "know a parent whose child got something from what their mum taught them" case-study request; a request for people over 70 who enjoy adventurous travel — Neil would just be a source of leads, not featured.)

When in doubt whether a match is a pure conduit ask or a direct-feature opportunity, lean toward flagging it but say so explicitly in the doc entry (e.g. "note: this may be a conduit-only ask, check before pitching") rather than silently dropping it.

For EACH matching post capture — the direct post/tweet URL is mandatory, get it from the post's timestamp link, never substitute the profile URL:
- Journalist/outlet name and handle
- The request text (verbatim, trimmed of filler)
- The deadline if stated
- The direct tweet URL (e.g. https://x.com/handle/status/1234567890)
- Whether the post (or the journalist's bio/pinned post, check if not obvious) gives an email address to send pitches to

STEP 2 — RESPOND PER MATCH, one of two modes:

MODE A — EMAIL GIVEN: If the post (or journalist's bio) states an email address to pitch to, draft a personalised reply email in Gmail using create_draft, addressed TO that email address (not to Neil). Before writing it, load the Skill "anthropic-skills:mmom-podcast-pr" (and "anthropic-skills:mmom-voice-check" if available) so tone matches Neil's voice — warm, specific, British, no em dashes, double quotes for any quoted speech, no "not trying to be salesy" disclaimers. Subject: reference their specific ask. Body: directly engage with what they asked for, briefly position Neil Taylor / MMOM as a relevant source or case study for their piece (do not oversell — one short paragraph plus an offer to send more/connect), sign off as Neil. Do NOT send — draft only.

MODE B — NO EMAIL GIVEN (reply expected on X): Do not post anything to X yourself. Instead, write a suggested reply tweet (under 280 characters, same MMOM voice — no em dashes, no disclaimers, plain and specific) that Neil could post manually. This goes in the doc only (Step 3), not Gmail.

STEP 3 — GOOGLE DOC: Reuse the standing doc "JournoRequest Tracker — Source of Truth" if one already exists (check the user's artifact list / ask if unsure which URL) — don't create a fresh doc per run. Add a new dated section (e.g. "## Scan — 18 Sep 2026") for each run's matches rather than starting over. Each match gets its own entry containing, as separate clearly-labelled lines (not just a link embedded in a handle mention — Neil needs the raw tweet URL visibly clickable on its own line):
- **Tweet:** the direct tweet URL as its own line, written as an actual markdown hyperlink (not just plain pasted text) — "Tweet: [https://x.com/handle/status/1234567890](https://x.com/handle/status/1234567890)" — so it renders clickable in the doc, confirmed by Neil 18 Sep 2026
- What they want (one line, trimmed)
- Deadline if stated
- Mode (Email or Reply-on-X)
- If Mode A: the email address used + a one-line note "email drafted in Gmail"
- If Mode B: the full suggested reply tweet text, ready to copy-paste, as a blockquote
If a match is a conduit-only ask being flagged cautiously (see FILTER above), say so on its own line.
If zero matches, the section should just say no relevant requests were found today.

STEP 4 — TRACKER: If there is at least one match, open (via the Chrome extension) this Google Sheet: https://docs.google.com/spreadsheets/d/1bW1Dp_e2Vxm40ynjiZCtzCaX2jHy6Co69EnRqEd_hpY/edit?gid=1314505899#gid=1314505899 — should already be signed in as Neil. Go to the "Media List" tab (columns #, Priority, Campaign, Media Type, Theme, Outlet/Programme, Contact, Email/Route, Status, Sent, Last Action). For each match add a new row at the bottom of the existing table (stay inside the table range, don't touch/reorder existing rows) with:
- Priority: P1
- Campaign: leave blank
- Media Type: best-fit from the existing dropdown (check "Lists" tab if unsure)
- Theme: best-fit from the existing dropdown (check "Lists" tab)
- Outlet/Programme: journalist's outlet/publication
- Contact: journalist's name and/or @handle
- Email/Route: the direct tweet URL (mandatory, never blank, never the profile URL)
- Status: "Sent" if Mode A (email drafted), "Not started" if Mode B (reply needed)
- Next Action: "Awaiting reply" if Mode A, "Reply on X" if Mode B, plus deadline if stated e.g. "Reply on X by [deadline]"
- Last Action: today's date + short note e.g. "#journorequest match found"
Skip near-duplicates already in the sheet (skim Contact/Outlet column first).

STEP 5 — REPORT: In your final chat response, start with a one-line summary for the completion notification, e.g. "3 matches — 1 email drafted, 2 X replies suggested. Doc: [doc link]." Include the doc link and list each match's tweet link again directly in the chat response. If X login failed, Gmail/Docs/Sheets weren't accessible, or anything else went wrong, say so clearly instead of guessing at results.