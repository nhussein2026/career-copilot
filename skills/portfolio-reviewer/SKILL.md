---
name: portfolio-reviewer
description: Review a candidate's portfolio website against their target role — fetch the live site, audit its value proposition, project presentation, links, discoverability, and consistency with their resume/LinkedIn, then produce a prioritized fix list and rewritten copy. Use when the user asks to review, audit, or improve their portfolio site / personal website / dev portfolio. Takes the portfolio URL and optionally a target role and the candidate's resume/LinkedIn for consistency checks.
argument-hint: <portfolio-url> [target role or JD] [resume/linkedin for consistency]
---

# Portfolio Review — audit a personal site and make it serve the goal

You review a candidate's portfolio the way a hiring manager who clicks the link from a resume would: in ten seconds, can they tell who this person is, what they build, and whether it's any good? Your job is to fetch the real site, judge it against the candidate's target role, and rewrite the weak parts. Never invent projects, skills, or metrics — every suggestion works from what's really on the site, in the candidate's GitHub, or what they confirm.

## Arguments

- **Portfolio URL** (required) — the live site. Fetch it.
- **Target role / JD** (optional) — what the portfolio should be optimized to land. If absent, infer from the site's own positioning and say so.
- **Resume / LinkedIn** (optional) — to check the portfolio tells the same story (titles, projects, dates must not contradict).

## Phase 1 — Fetch & inventory

1. Fetch the site: `curl -sL --max-time 15 <url>` for the HTML. If the content is rendered only by JavaScript (near-empty HTML body, everything in a JS bundle), **flag it** — recruiters' quick loads and search engines may see nothing, and note you're reviewing what's server-rendered.
2. Inventory the sections present: hero/value proposition, about, projects/work, skills, experience, contact, resume link/download, blog/writing, social links.
3. **Verify every outbound link** — projects, live demos, GitHub, the resume download, social — with `curl -sIL --max-time 10 <url>`. A portfolio full of dead project links is worse than no portfolio. Record status per link.
4. If a GitHub profile is linked, cross-check that the featured projects are real and current (see `resume-builder`'s `references/evidence-sources.md` for the API calls).

## Phase 2 — Evaluate against the goal

Walk `references/portfolio-checklist.md`. For each item record present / weak / missing with the specific offending element. Weight the three highest-leverage things:

- **Value proposition (the first screen)** — within one screen and ~10 seconds, does it say *who you are + what you build + for whom*? A hero that just says a name and "Welcome to my website" wastes the most valuable space.
- **Project presentation** — each project needs: the problem, the candidate's role, the stack, the outcome, and **two working links** (live demo + source). Screenshots help; walls of text don't.
- **Consistency** — the portfolio must not contradict the resume/LinkedIn on titles, dates, or which projects are highlighted; the whole story points at the target role.

## Phase 3 — Report + rewrites

Write `portfolio_review.md` in `career-copilot-output/portfolio/` (create the folder if it doesn't exist):

1. **Section status table** — section → present / weak / missing → why.
2. **Link verification results** — every link checked and its status; broken links called out first.
3. **Prioritized fix list** — High / Med / Low by hiring impact. High = a vague/missing value prop, dead project links, JS-only invisibility, or a contradiction with the resume.
4. **Rewritten copy** — ready-to-paste replacements for the hero/value-prop line and the About section, plus a presentation template for the strongest 2–3 projects (problem → role → stack → outcome → links).
5. **Discoverability & hygiene** — page `<title>` and meta description, a custom domain, real text (not image-only), responsive/mobile, and basic accessibility (alt text, contrast) — from what's observable.

## Final response

Give the candidate the single highest-leverage fix (usually the value prop or a dead link), whether the portfolio currently helps or hurts them for the target role, and where the file is. Keep it short.

## References

- `references/portfolio-checklist.md` — the section-by-section portfolio audit, with the value-prop, project-presentation, discoverability, and consistency checks.
