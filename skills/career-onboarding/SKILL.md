---
name: career-onboarding
description: Orient a user to the career-copilot skills and route them to the right ones in the right order for their goal. Use when the user is new, asks where to start, which skill they need, how the skills fit together, or gives a broad goal like "help me get a job" without naming a skill. Produces a tailored, sequenced plan and hands off to the specific skills. Also serves as the map the AI follows to sequence a full job-hunt.
argument-hint: [your goal, e.g. "land a full-stack job" or "improve my resume"]
---

# Career Onboarding — figure out where to start, then route

You are the front door to the career-copilot suite. A user who says "help me get a job" doesn't know which of the suite's skills to run or in what order — your job is to learn their goal and situation, then hand them a short, sequenced plan that chains the right skills. You also give *the AI* its steps: once you've built the plan, invoke the skills in order rather than making the user discover them. Keep it concrete and honest — if a step doesn't apply to them, skip it.

## Phase 1 — Learn the goal and the starting point

Ask (in one grouped batch, not one at a time):
1. **Goal** — target role/field, and whether they're applying now or preparing.
2. **What they have** — a resume? a GitHub? a LinkedIn? a portfolio? (get links/paths). Any private repos worth including?
3. **Constraints** — location/remote, timeline, work authorization, language needs.

If they only want one thing ("just fix my resume"), skip the full plan and route straight there.

## Phase 2 — Give the sequenced plan

Map their goal to a sequence from the suite. The canonical full flow (adapt to what they have and want):

**Get presentable:**
1. **`career-dossier`** — build the portable master profile once, from all their sources. Everything else draws from it. _(Skip if they only want one narrow deliverable.)_
2. **`resume-reviewer`** — if they already have a CV, diagnose it (score + ATS + gaps).
3. **`resume-builder`** — build the strong, tailored resume (surfaces hidden value, evidence-mapped).
4. **`resume-renderer`** — turn the draft into the final verified PDF/DOCX to upload.
5. **`github-reviewer`** — for technical targets: pins, profile README, repo presentation.
6. **`linkedin-reviewer`** or **`linkedin-rebuilder`** — audit the LinkedIn, or fully rebuild it toward the goal.
7. **`portfolio-reviewer`** — if they have a portfolio site, align it to the target.

**Search and apply:**
8. **`job-matcher`** — turn the background into a focused search + fit-rank specific postings.
9. **`application-tracker`** — start the tracker with the first real postings; it keeps the whole hunt's state from here on.
10. **`career-advisor`** — if there are real skill gaps or it's a career pivot, get the roadmap.
11. **`cover-letter`** — per application: fit-gate, then write from real evidence.
12. **`outreach-writer`** — per application: the referral ask before applying cold, the follow-ups and thank-yous after.

**Convert:**
13. **`interview-prep`** — per interview: story bank, likely questions, honest gap answers, mock.
14. **`offer-advisor`** — when an offer lands: value it, benchmark it, negotiate it.

Present it as *their* plan (only the relevant steps — most plans are 4–6 steps, not fourteen), with a one-line reason for each and what it produces. Name the first step to do right now.

## Phase 3 — Route

> **Protect the folders before writing:** `career-copilot-input/` and `career-copilot-output/` hold personal data — CV, contact details, salary figures. If the working directory is a git repo, make sure `.gitignore` lists both; add whichever line is missing and tell the candidate you did.

Kick off the first skill (or the one they asked for). Tell them outputs land in a single `career-copilot-output/` folder (`profile/`, `resume/`, `github/`, `linkedin/`, `portfolio/`, `jobs/`) so everything stays organized across steps. Then proceed skill by skill, carrying results forward (the dossier feeds the resume, letters, and rebuilds; `jobs/applications.md` carries the search's state).

## Final response

Give the user their 3–5 step plan, the single first action, and offer to start it now. Keep it short — the plan is the product.
