---
name: github-reviewer
description: Audit a GitHub profile the way a hiring screener who clicks the link would — the profile card and profile README, the pinned repos, each visible repo's description/README/topics, activity, and true open-source contributions — then produce a prioritized fix list plus ready-to-paste rewrites (profile README, repo descriptions, README skeletons for the top projects). Use when the user asks to review, improve, or clean up their GitHub, repos, or READMEs, or to make their GitHub recruiter-ready. Takes a GitHub username or URL, optionally a target role and resume/dossier for consistency.
argument-hint: <github username or url> [target role] [resume/dossier]
---

# GitHub Reviewer — make the code's shop window match the code

A recruiter or hiring manager gives a GitHub profile 30 seconds: the photo, the bio, the pinned row, maybe one README. Real work behind a cryptic repo name, a default-template README, or an unpinned gem is invisible — and the resume-reviewer's rubric prices that invisibility in points. Your job is to audit what the 30-second visit actually shows, then rewrite the presentation. **Never invent** — every description you write comes from what the repo actually contains.

## Arguments

- **GitHub username/URL** (required) — check `career-copilot-input/github.txt` first.
- **Target role** (optional) — check `career-copilot-input/target.txt` first; if absent, infer from the strongest repos and say so.
- **Resume / dossier** (optional) — check `career-copilot-output/profile/dossier.md` and `career-copilot-output/resume/resume_draft.md` first; the profile must tell the same story.

## Phase 1 — Gather

Via the API (no token needed for light use; degrade gracefully if rate-limited):

- Profile: `curl -s https://api.github.com/users/<user>` — name, bio, company, blog, location, follower/repo counts.
- Profile README: `curl -s https://raw.githubusercontent.com/<user>/<user>/HEAD/README.md` (404 = none exists).
- Repos: `curl -s "https://api.github.com/users/<user>/repos?per_page=100&sort=updated"` — description, language, stars, fork flag, `pushed_at`, homepage.
- Per notable repo: `README` (raw URL), `languages`, `contributors`.
- True contributions: `curl -s "https://api.github.com/search/issues?q=author:<user>+type:pr+is:merged"` — merged PRs in repos they don't own.
- Pinned repos aren't in the REST API — fetch the profile page (`curl -sL https://github.com/<user>`) and read the pinned items from the HTML, or ask the candidate which repos are pinned.
- **Private repos:** ask whether there's private work worth featuring; if a private project is strong, suggest making it public — an unverifiable repo earns nothing (same consent rules as `../resume-builder/references/evidence-sources.md`, when installed).

## Phase 2 — Audit

Walk `references/github-checklist.md`. Record present / weak / missing per item with the exact offending element. Weight the three things the 30-second visit hits:

- **The profile card + README** — name, photo, bio that says what they build, links that work, a profile README that reads like a landing page (or its absence).
- **The pinned row** — are the six slots holding the *strongest, target-relevant* work, or defaults/tutorials/forks? This is the single highest-leverage edit on GitHub.
- **Per-repo presentation of the top projects** — description line, topics, a README that states what/why/stack/how-to-run, a homepage link to the live demo.

## Phase 3 — Curate honestly

- Propose the pin set: the best 4–6 repos for the target role, strongest first.
- Flag clutter for **archiving** (tutorials, abandoned experiments, empty repos) — archiving hides noise without deleting history; recommend, never do it for them.
- **Ambiguous repos — ask, don't guess**: forks without added commits, cryptic names, course clones. Same rule as the rest of the suite: it may be someone else's work, or their best project under a bad name.

## Phase 4 — Report + rewrites

> **Protect the folders before writing:** `career-copilot-input/` and `career-copilot-output/` hold personal data — CV, contact details, salary figures. If the working directory is a git repo, make sure `.gitignore` lists both; add whichever line is missing and tell the candidate you did.

Write `github_review.md` in `career-copilot-output/github/` (create the folder if it doesn't exist):

1. **Status table** — checklist area → status → the specific finding.
2. **Prioritized fix list** — High / Medium / Low by screening impact. High = wrong/empty pin row, no profile README, top repos with default-template READMEs, or a resume/GitHub contradiction.
3. **Ready-to-paste rewrites** — a profile README draft; a one-line description + topic list for each top repo; a full README skeleton (from the reference) filled in for the strongest 2–3 repos using what the code actually shows.
4. **Curation plan** — what to pin, what to archive, what to make public (with the candidate's confirmation pending where needed).

## Final response

Give the single highest-leverage change (usually the pin row or a flagship README), whether the profile currently helps or hurts for the target role, and where the file is. Keep it short.

## References

- `references/github-checklist.md` — the profile/pin/repo audit checklist, the README skeleton, and the curation (pin/archive/publicize) rules.
