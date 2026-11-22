---
name: linkedin-applier
description: Apply to LinkedIn jobs in a real browser session — search with the candidate's own boolean strings, triage each posting against their evidence, upload the right resume, prefill Easy Apply, and draft honest screener answers from a pre-approved answer bank — then log the result to the tracker. Never submits; the candidate reviews and clicks. When no browser tools are available, writes a self-contained brief the candidate pastes into a browser agent (e.g. the Claude Chrome extension) instead. Use when the user wants help applying on LinkedIn, wants Easy Apply filled in, wants their applications automated or semi-automated, or wants a brief for a browser agent.
argument-hint: [how many to apply to, or a specific posting URL] [search string or filters to use]
---

# LinkedIn Applier — apply in the browser, honestly, one at a time

Applying is where a good profile turns into interviews, and where most candidates leak value: they answer screeners carelessly, upload the stale resume, and lose track of what they sent. You drive the browser to remove that friction — but the candidate stays the author of every claim and the one who presses Submit.

## Ground rules (read first, they override convenience)

1. **Never submit.** Fill every field, then stop and hand control back. "Submit application", "Send", "Continue to next step" on the *final* review screen — the candidate clicks those. Say clearly when a form is ready for review.
2. **Never invent an answer.** Screener questions are attestations: years of experience, work authorization, sponsorship, salary, notice period, certifications, language level. Every one comes from the answer bank (Phase 2) or from asking the candidate. A guessed "yes" can void an offer later. `[unanswered]` is an acceptable state; a fabricated answer is not.
3. **One account, human pace.** LinkedIn's User Agreement prohibits bots and automated access, and bulk activity gets accounts restricted — the candidate's profile is the asset the whole search runs on. Work a small batch per session, at reading speed, with a human in the loop on every submit. If the candidate asks for mass-apply, say plainly that it risks the account and offer the batch instead.
4. **Quality gate before volume.** A posting the candidate is auto-filtered from is worse than not applying: it burns time and teaches nothing. Triage (Phase 3) kills weak fits before any form is opened.
5. **Fix the shop window first.** Recruiters click from the application to the profile. If the profile still disagrees with the resume (stale headline, missing projects, "Open to Work" unset), say so before the first application — one hour of profile work outranks ten applications. Route to `linkedin-rebuilder` when installed.

## Phase 1 — Load the candidate and pre-flight

1. **Evidence:** read `career-copilot-output/profile/dossier.md`, then `career-copilot-output/resume/resume_draft.md`; fall back to `career-copilot-input/`. Never apply from a resume you haven't read — the answer bank is derived from it.
2. **Target and search:** read `career-copilot-output/jobs/job_search.md` for target titles, boolean strings, filters, and green/red flags. If it doesn't exist, run `job-matcher` first (or build the target inline and say you did).
3. **Resume file:** identify the *one* file to upload — normally the rendered `career-copilot-output/resume/Firstname_Lastname_Resume.pdf`, not an older CV sitting in `career-copilot-input/`. Confirm it with the candidate, and have them set it as the default resume on LinkedIn so Easy Apply reuses it.
4. **Batch size:** agree how many applications this session (default 5–10) and which lane (remote / local / both).

## Phase 2 — Build the answer bank before opening any form

This is the step that makes the rest safe. Per `references/screener-answers.md`, derive every reusable answer **once**, with its source, and get the candidate's sign-off:

- **Derivable from evidence** — years per skill, total professional experience (state whether internships are included; the two numbers differ), education, certifications, language levels, location, tools. Compute from real dates and show the arithmetic so the candidate can defend the number in an interview.
- **Only the candidate knows** — work authorization and sponsorship, salary expectation, notice period / earliest start, relocation, willingness to work on-site, voluntary EEO answers. **Ask for these. Never derive, never leave to the form's default.**
- **Hard zeros** — technologies with no evidence get `0`, and postings that gate on them go on the skip list. This is a feature: it converts a lie into a search filter.

Write the bank into `career-copilot-output/jobs/linkedin_apply_brief.md` so it survives the session and can be pasted into a browser agent.

## Phase 3 — Find and triage

Search with the candidate's own string and filters from `job_search.md` (experience level, date posted, remote/location, sort by most recent). For each posting, before touching a form, read the description and produce a two-line verdict:

- **Fit** — Strong / Stretch / Skip, driven by the green and red flags in `job_search.md`.
- **Gates** — any hard requirement that auto-filters them (years, a framework they don't have, a language, on-site in another country, authorization). Any gate hit with a hard `0` from the answer bank ⇒ **Skip**, and say why in one line.

Apply to Strong and defensible Stretch. Show the triage verdicts and let the candidate veto before you open forms.

## Phase 4 — Drive the application

Follow `references/apply-playbook.md` — the Easy Apply step map, the external-ATS fallback (Greenhouse / Lever / Workday), field-matching rules, upload handling, and what to do when a form fights back. Per posting:

1. Open it in its own tab; capture the company, role, URL, and posting date for the tracker.
2. Walk the steps: contact → resume upload → screeners → review. Fill from the answer bank only.
3. **Stop at the review screen.** Report: what you filled, any answer you left `[unanswered]` and why, and anything the posting asked that the bank couldn't cover. Hand back for the click.
4. If a screener needs a written paragraph (a "why this company" box), draft it from real evidence per `cover-letter`'s standard — grounded, specific, no invented enthusiasm — and mark it as a draft for the candidate to edit.

Never re-apply to a role already in the tracker. Never edit the candidate's profile, connections, or messages as a side effect of applying.

## Phase 5 — Log every outcome

> **Protect the folders before writing:** `career-copilot-input/` and `career-copilot-output/` hold personal data — CV, contact details, salary figures. If the working directory is a git repo, make sure `.gitignore` lists both; add whichever line is missing and tell the candidate you did.

Append each submitted application to `career-copilot-output/jobs/applications.md` per `../application-tracker/references/tracker-format.md`: company, role, link, fit, applied date, status `applied`, next action (follow-up date), and in Notes anything that will matter later — the screener answers given, the salary number entered, the recruiter named on the posting. Skipped postings are **not** logged; the tracker is not a wishlist. Record a one-line reason for skips in the session summary instead.

## When there are no browser tools

Don't stall. Write `career-copilot-output/jobs/linkedin_apply_brief.md` as a **self-contained** document the candidate pastes into a browser agent: identity and contact block, target roles, the search string and filters, the triage rules, the full answer bank, the per-application procedure, the tracker row format, and the ground rules above (especially "never submit"). Self-contained means it repeats the facts rather than pointing at repo files the agent can't read.

## Final response

The batch result: how many applied, how many skipped and why, any answer still `[unanswered]`, and the next follow-up due. If the profile needed fixing first, lead with that instead. Keep it short.

## References

- `references/apply-playbook.md` — the Easy Apply step map, external-ATS fallback, field-matching and upload rules, rate discipline, and failure recovery.
- `references/screener-answers.md` — how to derive each answer class honestly, the ask-don't-guess list, and the phrasing that survives an interview.
- `../application-tracker/references/tracker-format.md` — the row schema each application is logged to.
