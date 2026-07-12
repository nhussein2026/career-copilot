---
name: career-dossier
description: Consolidate everything about a candidate — CV, GitHub, LinkedIn, portfolio — into one comprehensive, portable Markdown "master profile" they can paste into any AI or tool to generate resumes, cover letters, bios, or answers. Unlike a resume (short and curated), the dossier is complete and source-tagged. Use when the user asks for a master profile, a single file with all their info for AI, a career dossier, or a portable/reusable profile. Takes any of: resume, GitHub, LinkedIn, portfolio, and optionally a target direction.
argument-hint: [resume.pdf] [github username/url] [linkedin url/pdf/paste] [portfolio url] [target direction]
---

# Career Dossier — one portable, verified master profile

You build the candidate's single source of truth: a complete, well-structured Markdown file that captures everything real and useful about them, so any tool or AI can slice it into a resume, a cover letter, a bio, or an interview answer without re-gathering. It is comprehensive where a resume is curated — but it obeys the same law: **everything is real and source-tagged.** Nothing invented; every fact carries where it came from, so downstream uses stay honest.

## Arguments

All optional; use whatever the candidate provides (more sources = richer dossier):
- Resume (PDF/text), GitHub (username/URL), LinkedIn (URL/PDF/paste), portfolio URL.
- Optional target direction — used only to order things helpfully, not to filter; the dossier keeps everything.

## Phase 1 — Gather everything

Use the suite's shared gathering method — `../resume-builder/references/evidence-sources.md` (present when the suite is installed together). If that file isn't available, the essentials are: read the resume PDF with the Read tool and pull the URLs hidden behind anchor text from its annotation layer (PyMuPDF `page.get_links()`); fetch GitHub via `curl -s https://api.github.com/users/<user>` and `curl -s "https://api.github.com/users/<user>/repos?per_page=100&sort=updated"`, plus per-repo `languages` and `contributors`; for LinkedIn ask for the "Save to PDF" export or pasted text if the URL is login-walled; fetch the portfolio with `curl -sL`. Two rules carry over:
- **Private work:** ask whether the candidate has private/unlisted repos to include; if a private project is strong, suggest making it public.
- **Ambiguous repos:** when you can't tell if a repo is the candidate's real work or what it does (forks, clones, cryptic names), ask rather than guess.

Record the **source** of every item — the dossier's value is that it's trustworthy.

## Phase 2 — Consolidate

Merge into one deduplicated inventory. Reconcile conflicts across sources (dates, titles, scope) by asking the candidate rather than silently choosing. Classify projects honestly (substantive vs. tutorial). Verify links with `curl -sIL`.

## Phase 3 — Write the dossier

Write `dossier.md` in `career-copilot-output/profile/` (create the folder if it doesn't exist), following `references/dossier-structure.md`. It is complete and reusable:

- **Identity & contact**, **Positioning** (a few honest angles they could target), **Skills with depth + evidence**, **Full work history** (every role, full bullets, scope), **All real projects** (name, links, stack, what it does, the candidate's role, what it proves), **Open-source contributions**, **Education**, **Certifications**, **Languages**, **Links**.
- **Facts & metrics bank** — a running list of every real number, scope figure, and outcome, so any future resume/letter can pull quantified claims without re-deriving them.
- **Gaps & to-confirm** — honest list of missing metrics (`[confirm: …]`), unverified items, and conflicts still open.

Keep the format clean and consistent (predictable headings, one fact per line where possible) so a machine can parse it as easily as a person.

## Phase 4 — Deliver

Tell the candidate the dossier is their reusable source of truth: point the other skills at it (resume-builder, cover-letter, linkedin-rebuilder can all draw from it), and note the top 1–2 items in "to-confirm" that would most improve everything downstream.

## Final response

Give the candidate what the dossier now captures that was scattered before, the single most valuable thing to confirm/fill, and where the file is. Keep it short.

## References

- `references/dossier-structure.md` — the full section layout for the dossier, including the facts-and-metrics bank and the to-confirm list.
