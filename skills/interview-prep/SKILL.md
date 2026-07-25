---
name: interview-prep
description: Prepare a candidate for interviews from their real evidence — a reusable STAR story bank mined from the dossier/resume, a "walk me through your background" narrative, per-posting likely questions (technical topics and behavioral) with honest answer outlines, the gap questions they will actually be asked, and good questions to ask back. Can also run a live mock interview. Use when the user has an interview coming up, asks to prep or practice for interviews, or wants likely questions for a role. Takes their background (dossier/resume best) and optionally the job posting, company, and interview stage.
argument-hint: [dossier/resume] [job posting or company] [stage: screen | technical | behavioral | final]
---

# Interview Prep — real stories, honest answers, no scripts for claims you can't back

Interviews are lost twice: by candidates who have the experience but can't retrieve a concrete story under pressure, and by candidates coached into claims that collapse on the follow-up question. You fix the first without causing the second. Everything you prepare comes from the candidate's real evidence — the same law as the rest of the suite: **prepare, never invent.** An answer outline that needs a fact no source supports gets a `[confirm: …]`, not a fabrication.

## Arguments

- **Background** — best: `career-copilot-output/profile/dossier.md` and `resume/resume_evidence_map.md` (already source-verified — the facts & metrics bank is exactly the raw material stories are made of). Otherwise a resume/LinkedIn, gathered minimally.
- **Job posting / company** (optional) — enables the per-posting prep in Phase 3. A URL (fetch it) or pasted text.
- **Stage** (optional) — recruiter screen, technical, behavioral, or final; shifts the emphasis. If unknown, cover screen + behavioral.

## Phase 1 — Gather

Load the dossier and evidence map if they exist; only ask for what they lack. Without them, collect the minimum: the resume, plus the candidate's 3–4 proudest pieces of work. Get the posting and stage. If an interview date exists, note it — it belongs in `career-copilot-output/jobs/applications.md` (the application-tracker's file) when that's in use.

## Phase 2 — Build the story bank

Mine the evidence into **6–10 STAR stories** per `references/interview-playbook.md`, mapped across the behavioral themes (impact, hard technical problem, conflict/disagreement, failure and lesson, leadership/initiative, ambiguity/pressure). Rules:

- Every story is real work from the evidence, with the candidate's own role explicit (their contribution, not the team's).
- Numbers only from the facts & metrics bank or candidate confirmation; a missing number is `[confirm: …]` — flag it, because interviewers ask "how much/many" and the candidate should walk in knowing.
- One story can serve multiple themes — map them, so six strong stories cover twenty questions.
- Write each as bullet-point beats (Situation → Task → Action → Result → what they'd do differently), not a memorizable script — scripts sound scripted.

## Phase 3 — Per-posting prep (when a posting is given)

1. Extract the posting's top priorities and hard skills.
2. **Likely questions, honestly calibrated**: the technical topics this role will probe (matched to what the candidate actually knows — flag the ones where they're thin rather than scripting confidence), the behavioral themes the posting hints at, and the standard screen set (why this company, why now, salary expectations — point the last at `offer-advisor` when installed).
3. **The gap questions they WILL be asked** — employment gaps, short tenures, missing must-have skills, career pivots. For each, an honest answer pattern from the playbook: acknowledge plainly, give the true context in one sentence, pivot to real adjacent proof or concrete ramp-up. Never a cover story.
4. **The walkthrough** — a ~90-second "walk me through your background" outline angled at this role: thread the real history toward why this job is the logical next step.

## Phase 4 — Questions to ask them

5–8 questions from the playbook's categories, tailored with something real about the company (their product, stack, recent news — research, don't recite the generic list).

## Phase 5 — Deliver (and offer the mock)

> **Protect the folders before writing:** `career-copilot-input/` and `career-copilot-output/` hold personal data — CV, contact details, salary figures. If the working directory is a git repo, make sure `.gitignore` lists both; add whichever line is missing and tell the candidate you did.

Write to `career-copilot-output/` (create folders as needed):
1. **`profile/story_bank.md`** — the reusable story bank with theme mapping and open `[confirm: …]` items. Update it, don't duplicate it, on later runs.
2. **`jobs/<company>/interview_prep.md`** (when a posting was given) — likely questions with answer outlines, gap answers, the walkthrough, questions to ask, and the logistics line (stage, date, format).

Then offer a **mock interview**: you ask one question at a time from the prep set, the candidate answers in the chat, you give feedback per the playbook's feedback rubric (concrete? their role clear? result stated? too long?) and iterate. It's the highest-value 20 minutes of the whole prep.

## Final response

Give the candidate their strongest story (the one to lead with), the one gap question to rehearse most, the biggest `[confirm: …]` number to look up before the interview, and where the files are. Offer the mock. Keep it short.

## References

- `references/interview-playbook.md` — the STAR spec, behavioral themes with example questions, honest gap-answer patterns, the walkthrough structure, the questions-to-ask bank, and the mock-interview protocol with its feedback rubric.
