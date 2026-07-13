# Improvement notes — ideas for future development

Running list of improvements not yet built. (The 2026-07 overhaul already covered: plugin packaging, name/folder alignment, the 3-profile scoring rubric, dossier-as-hub wiring, live search in job-matcher/career-advisor, and six new skills: resume-renderer, github-reviewer, application-tracker, outreach-writer, interview-prep, offer-advisor — plus `scripts/validate.py` and CI.)

## Quality & testing

- **Fixtures + golden outputs** — an `examples/` folder with 2–3 anonymized sample CVs (junior SWE, senior SWE, non-SWE) and reference review outputs, so prompt/rubric changes can be regression-checked instead of eyeballed.
- **Rubric calibration** — collect real screening outcomes (interviews landed per score band) and tune the three profiles' weights against them.
- **Validator additions** — check that every skill writes only into documented `career-copilot-output/` paths; lint for the honesty-rule boilerplate drifting between skills.

## New capabilities

- **company-researcher skill** — pre-interview/pre-offer deep dive: product, funding/stability signals, engineering blog, public reviews, recent news; feeds interview-prep's "questions to ask" and offer-advisor's risk read.
- **portfolio-builder** — not just review: generate a clean static portfolio site from the dossier (the reviewer's checklist as the spec).
- **Resume variants** — one dossier → several targeted resume drafts (e.g. backend vs full-stack), tracked so edits propagate.
- **Mock-interview voice mode** — when voice I/O is available, run the mock out loud; spoken answers expose different weaknesses than typed ones.

## Localization & reach

- **Non-English markets** — CV/LinkedIn conventions differ (photo/DOB expected in DE/TR, CV length norms, language-level frameworks like CEFR); add a regional-conventions reference the resume skills consult.
- **Region-specific boards and salary sources** — extend job-matcher's board list and offer-advisor's benchmark sources beyond the US/EU defaults.

## Automation

- **Scheduled search loop** — a routine (cron/scheduled agent) that re-runs the saved job-matcher searches weekly, appends new Strong/Stretch postings to the tracker, and flags due follow-ups.
- **Tracker nudges** — surface "due today" items at session start when applications.md has overdue next-actions.

## Packaging

- **Shared references** — if plugins gain first-class shared resources, deduplicate the gathering method / honesty rules into one place instead of graceful-degradation copies.
- **Marketplace listing** — publish to a community marketplace index once the plugin has a version or two of mileage; add a CHANGELOG.md when versions start moving.
