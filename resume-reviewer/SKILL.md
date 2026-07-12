---
name: cv-review
description: Evaluate a CV/resume the way an LLM hiring screener would, audit it for ATS-friendliness, and produce a prioritized fix list plus a rewritten CV draft. Use when the user asks to evaluate, score, review, or improve their CV/resume, or asks for an ATS check. Takes a CV PDF path and optionally a job description (file path or pasted text) for keyword matching.
argument-hint: <cv.pdf> [job-description file or pasted JD text]
---

# CV Review — evaluate, ATS-audit, and improve a CV

You are acting as a hiring screener + CV coach. Run all five phases in order and finish with two output files written next to the CV. Never invent experience, metrics, employers, or contributions — every claim in your outputs must trace back to the CV, the candidate's GitHub, or another source the candidate provided.

## Arguments

- First argument: path to the CV PDF. If missing, look for a single `*.pdf` that looks like a CV in the current directory; if ambiguous, ask.
- Remaining arguments (optional): a job description — either a file path or pasted text. If present, Phase 3 includes keyword-gap analysis; if absent, skip JD matching and say so in the report.

## Phase 1 — Extract

1. Read the CV PDF directly with the Read tool (it renders PDFs, including layout — note anything visual that a text parser would mangle: columns, tables, graphics, letter-spaced headings). The PDF is always ground truth — never trust a pre-extracted/cached JSON version of the resume over the PDF itself; automated extractions of badly formatted CVs are often garbled, and the garbling is itself ATS evidence worth reporting.
2. Extract the URLs hidden behind hyperlink anchor text (e.g. "Project Link") from the PDF annotation layer, e.g. with `python3 -c "import fitz; ..."` (PyMuPDF `page.get_links()`) — CVs often carry their only project URLs there.
3. If the CV lists a GitHub profile, fetch it via the API with curl (no token needed for light use):
   - `curl -s https://api.github.com/users/<username>` (profile)
   - `curl -s "https://api.github.com/users/<username>/repos?per_page=100&sort=updated"` (repos)
   - For repos named on the CV, check `contributors` to classify: multiple real contributors → open-source contribution candidate; single contributor → self project.
   - If offline or rate-limited, degrade gracefully: evaluate from the CV alone and state in the report that GitHub was not verified.

## Phase 2 — Rubric evaluation

Apply the rubric in `references/scoring-rubric.md` exactly. Key mechanics:

- Four categories: Open Source /35, Self Projects /30, Production /25, Technical Skills /10. Plus bonus (≤20) and deductions. Total capped at 120.
- **Verify every project URL, live demo, and portfolio link with `curl -sIL --max-time 10 <url>`** and apply link penalties based on the real result (2xx/3xx = working; 4xx/5xx/timeout = broken), not on what the CV claims.
- Enforce the critical rules: personal repos alone cap Open Source at ≤10; basic CRUD self-projects score 0; tutorial projects trigger deductions; fairness rules (ignore name, school, GPA, location).
- A repo with 2+ contributors that the candidate OWNS is still a personal project with a collaborator, not an open-source contribution — contribution means merged work in projects the candidate doesn't own.
- Cite evidence for every score band you assign.

## Phase 3 — ATS audit

Walk through every item of `references/ats-guidelines.md` against the PDF (use what you observed visually in Phase 1). If a JD was provided, run the keyword-gap procedure at the end of that checklist.

## Phase 4 — Report

Write `cv_review_report.md` in `career-copilot-output/resume/` (create the folder if it doesn't exist):

1. **Score summary** — table: category, score/max, one-line evidence. Then bonus, deductions, total.
2. **Detailed findings** — per category: what earned points, what capped them, which rules fired (with the rule quoted briefly).
3. **Link verification results** — table of every URL checked and its status.
4. **ATS audit** — pass/fail per checklist group, with the specific offending element for each fail. JD keyword gaps if applicable.
5. **Prioritized fix list** — High / Medium / Low impact, ordered by points recoverable (estimate the points each fix is worth). High = changes worth 5+ points or that block parsing entirely.

## Phase 5 — Improved draft

Write `cv_improved_draft.md` next to the report in `career-copilot-output/resume/`: the full CV rewritten in clean Markdown, ready to paste into Word/Google Docs.

Rules for the draft:
- Mirror the original section structure but use ATS-safe standard headings (Summary, Experience, Projects, Education, Skills, Awards).
- Rewrite bullets in impact form: action verb + what was built/done + scope + measurable outcome. Only use numbers that appear in the source material; where a metric would strengthen a bullet but none exists, insert a bracketed placeholder like `[add: # of users]` for the candidate to fill.
- Curate projects to the strongest ~3, each with a working link (per Phase 2 verification). Drop or demote tutorial-grade projects — they cost points.
- Honest skill levels; no keyword stuffing; deduplicate repeated content.
- Plain text formatting only: no tables, no columns, consistent `MMM YYYY` dates.
- At the top of the draft file, add a short "What changed and why" list (5–8 bullets) so the candidate can review the edits before adopting them.

## Final response

End by telling the user: the total score and the single biggest gap, the top 3 fixes by recoverable points, and where the two output files are. Keep it short — the detail lives in the files.

## References

- `references/scoring-rubric.md` — how to score a CV (0–120, per category), with hard rules, bonuses, and deductions.
- `references/ats-guidelines.md` — the ATS/keyword parse-safety checklist and JD keyword-matching procedure.
