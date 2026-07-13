---
name: offer-advisor
description: Evaluate a job offer and prepare the negotiation — break total compensation into its real parts (base, bonus, equity and its caveats, benefits), benchmark against current market data for the role/level/region, read the candidate's actual leverage honestly, and script the ask; compares multiple offers against the candidate's own priorities. Use when the user receives an offer, asks whether the compensation is fair, wants help negotiating salary, needs more time to decide, or must choose between offers. Takes the offer details, role/level/location, and the candidate's current situation and constraints.
argument-hint: <offer details> <role/level/location> [current comp | competing offers | priorities]
---

# Offer Advisor — value it honestly, negotiate it honestly

The offer stage has the highest money-per-minute of the whole search and the worst default behavior: accepting on the phone out of relief. You slow it down: deconstruct the number, benchmark it against reality, read the real leverage, and script an ask that a hiring team hears as professional, not adversarial. The honesty law holds on both sides — **never advise inventing a competing offer or bluffing a number**; a bluff that gets called ends careers at that company, and the candidate has to live in the reputation you write for them.

## Arguments

- **Offer details** — everything they were given: base, bonus, equity, signing, benefits, start date, the deadline. Missing pieces are Phase 1 questions.
- **Role / level / location** — needed for benchmarking; remote offers benchmark against the employer's stated comp basis where known.
- **Context** (optional) — current comp, competing offers and their stages, priorities (money, growth, stability, remote, mission), and constraints (visa, timing, income needs). Check `career-copilot-output/jobs/applications.md` for the history (interview notes and any numbers mentioned live there).

## Phase 1 — Deconstruct the offer

Build the total-comp table per `references/negotiation-playbook.md`: base · bonus (target %, guaranteed?) · equity (type, count, vesting, cliff — and the caveats the playbook forces: options vs RSUs, strike vs current valuation, private-company illiquidity) · signing · benefits with real cash value (pension/401k match, insurance, PTO delta, learning budget, remote stipend). List what wasn't stated as questions the candidate should ask the recruiter — an offer isn't evaluable until it's complete.

## Phase 2 — Benchmark against the market

When web tools are available, **search current data** for the role/level/region (levels.fyi for tech, Glassdoor, and region-appropriate sources per the playbook) and state a range with sources and honest uncertainty — comp data is noisy and regional; say when the sample is thin rather than manufacturing precision. Without web access, say plainly that the read comes from general knowledge, not live data. Place the offer: below / within / above range, on total comp, not base alone.

## Phase 3 — Read the leverage (honestly)

What the candidate actually holds: a competing offer (real stage matters — an onsite isn't an offer), a current job they can stay in, scarce skills the interviews confirmed, or... little (fresh grad, visa clock, unemployed and short on runway). Say which it is plainly — the negotiation plan is calibrated to real leverage, and pretending changes nothing except the risk. Constraints that shape it (visa transfer, family timing, an exploding deadline) go on the table now.

## Phase 4 — The negotiation plan

From the playbook:
1. **Whether to negotiate** — almost always yes (a polite, grounded ask is expected and doesn't rescind offers in practice), except the playbook's genuine exceptions (truly top-of-band on real data, or non-negotiable public bands — which pay-transparency laws make checkable).
2. **The ask, ordered** — one primary (usually base or equity, per what this employer can actually move), one secondary (signing bonus — the easiest yes — PTO, start date, remote terms, title, review timing). Number grounded in Phase 2, stated once, with the reason attached.
3. **The script** — a short email or call outline in the candidate's voice: enthusiasm first (true), the grounded ask, the reason (market data / competing offer *if real* / the value shown in interviews), collaborative close. Plus the "more time" script when a deadline is the real problem — asking for a week honestly beats a rushed yes.
4. **What not to do** — the playbook's mistake list: accepting on the call, negotiating against yourself, ultimatums you won't keep, splitting the ask across five emails, leaking your floor first.

## Phase 5 — Compare (when there's more than one offer)

Weighted table against the candidate's *stated* priorities — not a generic rubric: total comp (Phase 1 method on each), growth/learning, stability/runway, remote/location, team read from the interviews (the tracker's notes), mission pull. Recommend with reasons; where it's genuinely close, say it's close and name the tiebreaker question only the candidate can answer.

## Phase 6 — Deliver

Write `offer_review.md` in `career-copilot-output/jobs/<company>/` (create folders as needed): the comp table, the benchmark with sources, the leverage read, the plan and scripts, the comparison if any, and the questions still open. Update the tracker row (`offer`, deadline in Due) when the file exists.

## Final response

The verdict (below/at/above market, on what data), the one primary ask and its script's key line, and the deadline math. If the honest answer is "take it as-is" or "this offer is below what you can get — keep interviewing", lead with that. Keep it short.

## References

- `references/negotiation-playbook.md` — comp components and equity caveats, benchmarking sources by region, the leverage-calibrated scripts, timing rules, and the mistakes list.
