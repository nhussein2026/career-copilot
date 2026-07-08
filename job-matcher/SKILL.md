---
name: job-matcher
description: Turn a candidate's background into a focused job search — a target-role definition, a set of boolean search strings for job boards and LinkedIn, a shortlist of where to look, and (when postings are provided) a fit assessment ranking them. Use when the user asks how or where to find jobs, wants search queries/boolean strings, wants job alerts set up, or wants to know how well they match specific postings. Takes the candidate's background and a target role/field, and optionally one or more job postings to score.
argument-hint: <candidate background> <target role/field> [job postings to assess]
---

# Job Matcher — search strategy and fit assessment

You help a candidate find and prioritize the right openings. Two modes, often both in one run: **build the search** (queries + where to look) and **assess fit** (rank specific postings against the candidate). Be honest about fit — steering someone toward roles they'll be filtered out of wastes their time.

## Arguments

- Candidate background: resume/LinkedIn/GitHub or a description — skills, experience level, and constraints (location, remote/onsite, work authorization/visa, salary floor, timeline).
- Target role/field: the kind of role they want. If broad, narrow to 1–2 concrete titles first.
- Optional job postings: one or more URLs or pasted descriptions to score.

## Phase 1 — Define the target

1. Settle on 1–3 concrete target job titles (roles are listed under many names — e.g. "Software Engineer", "Backend Developer", "Full-Stack Engineer"). Capture the synonyms; you'll need them for boolean queries.
2. Lock the hard constraints: location/remote, seniority, work authorization, must-have vs nice-to-have domain.

## Phase 2 — Build the search

Use `references/search-strategies.md`. Produce:

1. **Boolean search strings** — ready to paste into LinkedIn, Google (`site:` X-ray), and the major job boards. Combine title synonyms with `OR`, required skills with `AND`, and exclude noise with `NOT`/`-`. Give one broad-recall string and one high-precision string.
2. **Where to look** — a shortlist of the right boards/sources for this role and region (general boards, niche/specialized boards, company career pages, and community sources), with a one-line reason for each pick.
3. **Alerts plan** — which searches to save as alerts and at what cadence, so new postings come to them instead of re-searching.

## Phase 3 — Assess fit (when postings are provided)

For each posting, produce a fit read:

1. Extract required hard skills, nice-to-haves, the title, seniority, and any hard gates (years of experience, degree, clearance, work authorization, location).
2. Match against the candidate: **required skills met / partially met / missing**, and whether any hard gate disqualifies them.
3. Give a **fit verdict** — Strong / Stretch / Weak — with the one or two factors that drive it, and the single thing that would most improve their odds for that posting (e.g. surface a buried skill on the resume, add a keyword honestly, address a gate).
4. Never encourage claiming experience they don't have; distinguish "apply anyway, it's a reasonable stretch" from "you'll be auto-filtered."

## Phase 4 — Deliver

Write `job_search.md` in the working directory:

1. **Target roles** — the 1–3 titles and their synonyms.
2. **Boolean strings** — broad and precise, per platform, ready to paste.
3. **Where to look + alerts** — the shortlist and the alert cadence.
4. **Posting assessments** (if any) — a ranked table: posting → fit verdict → gaps → top move.

## Final response

Give the candidate the best-fit target title, the one search string to start with today, and where the file is. Keep it short.

## References

- `references/search-strategies.md` — boolean search construction, board/source selection, X-ray search, and job-alert setup.
