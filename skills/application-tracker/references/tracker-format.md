# Tracker format — schema, statuses, cadences, integrations

The file is `career-copilot-output/jobs/applications.md`. Keep the format exactly stable — humans scan it and other skills parse it.

## File layout

```markdown
# Applications — <candidate name>
_Updated: YYYY-MM-DD. One row per company + role. Statuses: found · applied · screen · interview · offer · accepted · rejected · withdrawn · dormant._

## Active

| Company | Role | Link | Fit | Applied | Status | Last update | Next action | Due | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Acme | Backend Engineer | [posting](url) | Strong | 2026-07-03 | interview | 2026-07-10 | Prep for tech interview (interview-prep) | 2026-07-14 | Recruiter: Dana. Stack: Go/Postgres. |

## Closed

| Company | Role | Fit | Applied | Outcome | Closed | What we learned |
|---|---|---|---|---|---|---|
| BetaCo | Full-Stack Dev | Stretch | 2026-06-20 | rejected (after screen) | 2026-07-01 | Asked hard for K8s experience — real gap. |
```

Rules:
- Dates `YYYY-MM-DD`. `Fit` uses job-matcher's vocabulary: Strong / Stretch / Weak.
- **Every active row must have a Next action and a Due date** — a row with neither is unmanaged state; compute one at every touch.
- When a row closes (accepted/rejected/withdrawn), move it to Closed and fill "What we learned" — one honest line; patterns across these lines are Phase 3 material.
- `dormant` stays in Active but doesn't count in the pipeline number; it revives on any new event.

## Status vocabulary

`found` (worth applying, not yet applied) → `applied` → `screen` (recruiter/HR call) → `interview` (any technical/team round; note "interview 2/3" in Notes) → `offer` → terminal: `accepted` / `rejected` / `withdrawn` (candidate's choice) / `dormant` (auto, see below).

## Cadences (defaults — the user can override)

- **Follow-up nudge**: `applied` + 7 business days with no response → next action: follow-up via outreach-writer. One nudge only; after it, the row just waits.
- **Post-interview thank-you**: same day or next morning → outreach-writer.
- **Post-interview silence**: stated timeline + 3 business days (or 7 if none stated) → polite status check.
- **Dormancy**: 21 days with no movement and the nudge already sent → mark `dormant`. Honest pipeline > hopeful pipeline.
- **Offer deadline**: always in Due; if the user needs more time, that's an outreach-writer message and an offer-advisor conversation.

## The summary view (what "status" prints)

```
Pipeline: 9 active — 4 applied · 2 screen · 2 interview · 1 offer   (3 dormant, 6 closed)
Due now:
  1. Acme — tech interview 2026-07-14 → run interview-prep
  2. Nimbus — follow-up due (applied 2026-07-02, no response) → outreach-writer
  3. Orbit — offer expires 2026-07-18 → offer-advisor
```

## How the other skills use this file

- **job-matcher** appends `found` rows for Strong/Stretch postings it assessed (never Weak — the tracker isn't a wishlist).
- **cover-letter** flips the row to `applied` (creating it if needed) when a letter is delivered, and sets the follow-up cadence as Next action.
- **interview-prep / offer-advisor** read the row's Notes for context (recruiter names, stated timelines, numbers mentioned) and write their outputs into the same `jobs/<company>/` folder.
- Any skill touching a row updates `Last update` and the header's `_Updated:_` date.
