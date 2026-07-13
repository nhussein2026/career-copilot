---
name: application-tracker
description: Create and maintain the single source of truth for a job hunt — one table of every application's company, role, link, fit, dates, status, and next action with a due date, updated from plain-language input ("applied to Acme", "rejected by X", "interview Friday"). Surfaces what needs doing now — follow-ups due, interviews to prep, offers to evaluate, stale applications. Use when the user wants to track or log applications, reports a status change, or asks where their search stands / what to do next. Other skills (job-matcher, cover-letter) feed it.
argument-hint: [update in plain language, e.g. "applied to Acme backend role" — or "status" for the overview]
---

# Application Tracker — one table, always current, always pointing at the next action

A real job search dies of untracked state: the follow-up never sent, the interview prepped the night before, the same company applied to twice. You keep one file — `career-copilot-output/jobs/applications.md` — as the search's single source of truth, and every time it changes you say what needs doing *now*. You track honestly: a stale application is marked dormant, not kept alive for morale.

## Phase 1 — Load or initialize

1. Read `career-copilot-output/jobs/applications.md`. If missing, create it per `references/tracker-format.md`.
2. On first creation, **import what already exists**: each `career-copilot-output/jobs/<company>/` folder (a cover letter there implies at least `applied` — confirm with the user), and any posting assessments in `job_search.md`, become rows.

## Phase 2 — Apply the update

Parse the plain-language update into row changes per the format reference: one row per company + role; status moves along the pipeline (`found → applied → screen → interview → offer → accepted/rejected/withdrawn/dormant`); every change stamps today's date and recomputes **Next action + Due**. Unknown company or ambiguous role → ask, don't guess a row. Log substance (recruiter name, feedback quotes, salary numbers mentioned) in the row's Notes — that context is gold at offer time.

## Phase 3 — Review after every change

Scan the whole table and surface, in order of urgency:

- **Follow-ups due** — `applied` with no response past the cadence in the reference → suggest `outreach-writer` (when installed) for the nudge.
- **Interviews upcoming** — → suggest `interview-prep` with the posting.
- **Offers on the table** — → suggest `offer-advisor`; flag any exploding deadline.
- **Staleness** — no movement past the dormancy threshold → mark `dormant` (recoverable, but out of the active count). Honesty rule: the active pipeline number the user sees reflects reality.
- **Balance check** — if everything in the pipeline is `found` and nothing is `applied`, or interviews keep dying at the same stage, say so plainly; a pattern is information.

## Phase 4 — Deliver

Rewrite the file, keeping the format stable (other skills parse it). Respond with only: what changed, the pipeline count by stage, and the top 1–3 next actions with due dates. The table lives in the file; don't repaste it into chat unless asked ("status" → show the summary view from the reference).

## Final response

The change made, the pipeline snapshot (e.g. "9 active: 4 applied, 2 screen, 2 interview, 1 offer"), and the single most urgent action. Keep it short.

## References

- `references/tracker-format.md` — the exact table schema and status vocabulary, cadence/dormancy thresholds, the summary view, and how the other skills read/write the file.
