---
name: outreach-writer
description: Write short, honest job-search messages that get replies — referral requests, cold notes to recruiters or hiring managers, post-application follow-ups, interview thank-yous, and post-silence status checks — each grounded in the candidate's real evidence, sized to its channel (LinkedIn connection note vs InMail vs email), sent at the right moment, and never falsely familiar. Use when the user asks for a LinkedIn message or DM, a referral ask, a follow-up or thank-you note, or whether/when to message a recruiter. Takes the situation and target (person/company/role), plus the candidate's background.
argument-hint: <situation: referral | cold note | follow-up | thank-you | status check> <person/company/role> [posting] [background]
---

# Outreach Writer — small messages, real reasons, right timing

Referrals convert far better than cold applications, and a good follow-up resurrects applications that silence would have killed — but most outreach fails by being long, generic, or fake-warm. You write the five message types that matter, each under the honesty law of the suite: **no manufactured familiarity, no claimed enthusiasm that isn't there, every concrete line traceable to real evidence.** And you enforce timing — the right message on the wrong day is still the wrong message.

## Arguments

- **Situation** — which message: referral request · cold note (recruiter or hiring manager) · follow-up after applying · thank-you after an interview · status check after silence. If unclear from the ask, infer and confirm.
- **Target** — the person (and the true relationship: stranger, alum, former colleague, met-at-event) and the company/role. The relationship truth shapes the register — never write "great to reconnect" to a stranger.
- **Posting / background** — the posting (fetch if URL); evidence from `career-copilot-output/profile/dossier.md` / `resume/resume_evidence_map.md` when present; history from `jobs/applications.md` (the application-tracker's file) so the message reflects where things actually stand.

## Phase 1 — Situate and check timing

1. Establish the five facts: message type, recipient + true relationship, role, what's already happened (applied? interviewed? when?), and the one thing the candidate genuinely wants (an intro, a forward, a status, nothing but thanks).
2. **Check the timing rules** in `references/outreach-playbook.md`. If it's too early (follow-up 2 days after applying) or over-quota (a second nudge), say so and give the right date instead of writing the message — protecting the candidate from spamming their own pipeline is part of the job.

## Phase 2 — Write

Per the playbook's spec for the type. Universal rules:

- **Channel-sized**: a LinkedIn connection note is ≤300 characters; an InMail/DM a short paragraph; an email a few short paragraphs with a subject line that states the matter plainly.
- **One real hook** — a specific, true line connecting the candidate to this role/person (a matching real project, a genuine reason for the company). No hook available? The message isn't ready; find one in the evidence or say honestly that a generic note is all that's possible and what it's worth.
- **One clear, small ask** — forward a blurb, 15 minutes, a status update. Never two asks.
- **Easy to act on** — a referral ask includes the posting link and a 2-line forwardable blurb; a status check restates role + date applied so the recipient needn't search.
- Produce **two variants** (e.g. shorter/warmer) so the candidate picks their voice. Anything unverifiable stays `[confirm: …]`.

## Phase 3 — Deliver

Append the message(s) — dated, typed, recipient noted — to `career-copilot-output/jobs/<company>/outreach.md` (create folders as needed). If the tracker file exists, update the row's Next action (e.g. "sent follow-up 2026-07-12; wait"). Tell the candidate when to send it and what the no-reply plan is (usually: one nudge per the playbook, then let it rest).

## Final response

The message (the better variant first), when to send it, and the one timing rule in play (e.g. "this is your one nudge — after this, we wait"). Keep it short.

## References

- `references/outreach-playbook.md` — per-type specs (structure, length caps, examples), the timing/quota rules, and the etiquette lines never to cross.
