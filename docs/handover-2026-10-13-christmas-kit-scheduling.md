# Handover: Christmas Cold arc scheduling in Kit (13 Oct 2026)

Written at the end of a cloud session. Read `README.md`, `INDEX.md`, `knowledge/lessons.md` first, as `CLAUDE.md` says.

## What a new session can and cannot do

- Needs Claude in Chrome open on the Kit tab (`app.kit.com`). Cloud sessions cannot reach Neil's browser.
- The Kit connector (MCP) can read broadcasts, sequences, tags and subscribers, and can edit drafts. It cannot schedule or send a broadcast, cannot change the account time zone, and cannot save an audience that has both a "send to" and an "exclude" group (Kit rejects it: "Only a single filter group is supported"). So scheduling and exclusions are UI work.
- Never press the final confirm on a send without Neil saying yes to that exact email, per `CLAUDE.md`. Neil has asked for these to be scheduled, so for the seven below, the yes is given once the audience, time and subject read back correctly.

## Kit facts checked on 13 Oct 2026

- Account time zone is Europe/Madrid (+1 on the UK). Neil wants London.
- Tag IDs: Seg: Cold (Drifted) 24064205 (189 subscribers), Seg: Lapsed 24064206 (14), Seg: Past Clients 24064207 (102), Seg: In Progress 24064208 (6), Seg: In Sales 24064209 (2).
- Cold 1, broadcast 26385319, "What did you want at eight?": still a draft, not scheduled. Audience saved correctly (Cold, excluding Lapsed, Past Clients, In Progress, In Sales). Needs Continue, then confirm, for Fri 30 Oct, 07:05 UK. While Kit is on Madrid time, pick 8:05 AM.
- Rotation email, broadcast 26130324, "Your dad isn't going to write that memoir book", is scheduled for Fri 23 Oct at 18:05 UTC, which is 19:05 UK. Wrong. It should be 07:05 UK.
- Rotation email 26130293 ("A shoebox of lizards") on Fri 16 Oct is correct at 07:05 UK.

## Job 1: fix the time zone

Settings, General, time zone to London. Then open the 23 Oct email and reschedule to 07:05. After that every schedule is simply 07:05 UK.

## Job 2: schedule Cold 1 and the seven ready drafts

Each needs: send to the segment, add the exclusion group, set the date and time, Continue, confirm. Read the screen back to Neil before confirming. If Kit is still on Madrid time, add one hour to the time you pick.

| Email | Broadcast ID | Date | Send to | Exclude |
|---|---|---|---|---|
| Cold 1 | 26385319 | Fri 30 Oct | Seg: Cold | already saved |
| Cold 2 | 26385333 | Tue 24 Nov | Seg: Cold | Lapsed, Past Clients, In Progress, In Sales |
| Cold 4 | 26385335 | Tue 8 Dec | Seg: Cold | same four |
| Cold 5 | 26385336 | Fri 11 Dec | Seg: Cold | same four |
| Cold 6 | 26385337 | Tue 15 Dec | Seg: Cold | same four |
| Cold 8 | 26385353 | Mon 21 Dec | Seg: Cold | same four |
| Cold 9 | 26385354 | Wed 23 Dec | Seg: Cold | same four |
| Lapsed 3 | 26385361 | Tue 22 Dec | Seg: Lapsed | Cold, Past Clients, In Progress, In Sales |

Edit page for any draft: `https://app.kit.com/campaigns/<broadcast ID>/draft`.

Hold back, do not schedule yet:
- Cold 3 (26385334): check family consent for the quoted lines.
- Cold 7 (26385352): add one real detail from that last Christmas.
- Cold 10 (26385356): check family consent for the closing line.
- Lapsed 1, 2, 4, 5 (26385377, 26385359, 26385363, 26385364): consent checks, a placeholder P.S. and the P.S. about the Friday rotation still to settle.

Check before moving on: Cold 6 (Tue 15 Dec) and Lapsed 2 (Tue 15 Dec) share a date but go to different audiences, so that is fine.

## Job 3: Drift sequence (checked 13 Oct, recommendation below)

Sequence "The Drift | Feb-26", ID 2666400. Ten emails. 266 subscribers. Sequence-level setting: Tuesdays only, 09:00 Madrid, which is 08:00 UK. A subscriber seen today got their email at 08:20 UK on Tue 13 Oct. It excludes In Progress, In Sales and Past Clients, but NOT Lapsed.

Findings:
- Collision: Christmas Cold broadcasts land on Tuesdays (24 Nov, 8 Dec, 15 Dec) at 07:05 UK, and Lapsed ones on Tue 22 Dec. Anyone still moving through Drift on a Tuesday would get two emails inside an hour. Cold 3 (1 Dec) is held back but is also a Tuesday.
- Lapsed (14) are not excluded from Drift, and they also get Lapsed Drip 1 and the Christmas Lapsed emails. Three streams on one small group.
- Per-email send days disagree with the sequence setting. Email 2 is Tue and Fri only, emails 3 to 10 say every day, and the sequence says Tuesday only. A new joiner seen today (added Sat 10 Oct) got their first email on Tuesday, which fits Tuesday-only, but this was not proven for later emails. Check in the Kit UI how the two settings combine before trusting either.
- Performance: opens hold at 44 to 63 per cent across the ten. Email 10 ("My mum caught me not practising what I preach") has 74 opens and only 1 click, the weakest closer. Emails 3 and 4 show only 86 and 77 recipients against 250-ish at email 5, because they were added after most people had passed that point. That is not a bug.

Recommendation, needs Neil's yes: put the sequence on hold from Mon 23 Nov and release on Mon 28 Dec, and add Seg: Lapsed to its exclusions now. Nobody loses an email, they just shift by five weeks. The alternative is to leave it running and exclude Seg: Cold from Drift in that window only, which is fiddlier and risks a missed untag.

## Job 4: Past Clients (102 subscribers)

Decide the objective first, then write: Snapshot for the children, a top-up for the parent, or referrals. Read `knowledge/offer/pricing.md` before any price. Follow the CLAUDE.md voice rules (no em dashes, "audio documentaries", real stories only).

## Job 5: the seven drafts waiting on consent checks and edits

Cold 3, Cold 7, Cold 10 and Lapsed 1, 2, 4, 5, as listed above. Neil owns the consent checks and the real-detail swap.

## Not done

Nothing was scheduled, edited or sent in Kit by this session. No lessons logged yet. If Neil corrects anything while scheduling, log it in `knowledge/lessons.md` the same turn.
