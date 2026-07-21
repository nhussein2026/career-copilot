# Resume blueprint — structure, bullets, and ATS-safe formatting

How to turn the verified evidence inventory into the draft. Everything here assumes Phase 3 is done: links verified, projects classified, unconfirmed items held back.

## Section menu & ordering

Include only sections the candidate has real content for. Order by what makes *this* candidate strongest for the target:

- **Contact block** (always, top, plain text) — full name, email, phone, city/country, LinkedIn URL, GitHub URL, portfolio URL. No photos, no icons carrying the only copy of the info.
- **Summary** (2–3 lines) — role + specialization + strongest proof *by category*, aimed at the target. Written last, once you know the highlights. Skip it rather than pad it. **Summary claims, body proves:** keep specific names, metrics, and links out of the summary — they're evidence, so they live in the sections below and must not be repeated here (see `resume-recipe.md` §8).
- **Experience** — the core for anyone with work history. Reverse-chronological.
- **Projects** — lead with this for students/career-changers, or place after Experience to show range. Curate to the **strongest ~3**, each with a verified working link.
- **Skills** — grouped (Languages / Frameworks / Tools / Domains), honest levels, terms spelled exactly.
- **Education**, **Certifications**, **Awards / Recognition** — as the evidence supports.

Ordering rule: the section with the candidate's best evidence comes first after the summary. Experienced hire → Experience first. Strong GitHub, thin job history → Projects first.

## The impact-bullet formula

Every Experience/Project bullet: **action verb + what was built/done + scope + measurable outcome.**

- Start with a strong, honest verb (Built, Led, Designed, Migrated, Automated, Cut, Shipped) — no first-person pronouns, no "responsible for".
- State scope and outcome using **only numbers that appear in the evidence or the candidate confirmed.** Where a metric would strengthen the line but none exists, insert a bracketed placeholder like `[add: % latency reduction]` — never invent a figure.
- One idea per bullet; 2–4 bullets per role, best first. Lead each role with a one-line scope/context statement (team, product, what it does).
- For team work, phrase the candidate's own contribution, not the team's collective output.
- Don't repeat the same project verbatim in both Experience and Projects — cross-reference or pick the stronger home.

Weak → strong (same underlying fact, better articulated):
- ✗ "Worked on backend APIs."
- ✓ "Built and shipped 12 REST endpoints for the payments service handling `[add: requests/day]`, cutting checkout latency from 800 ms to 300 ms."

## Project curation

- Keep substantive projects with a README, real commit history, and a working link. Drop or demote tutorial/CRUD-clone/course-follow-along projects — they signal inexperience and cost credibility.
- Each kept project: name (linked to the verified URL), one line on what it does and the stack, then 1–2 impact bullets. Prefer projects with real users, stars, or a live demo.
- A project that only exists because the candidate confirmed it (no public link) can stay, but mark it in the evidence map as candidate-confirmed.

## ATS-safe formatting (non-negotiable)

The draft must parse cleanly in automated screeners. Follow every point; these mirror the suite's `../../resume-reviewer/references/ats-guidelines.md`:

- **Single column.** No tables, text boxes, or multi-column layouts carrying content.
- **Standard headings** only: Summary, Experience, Projects, Education, Skills, Certifications, Awards. No letter-spaced or stylized headings ("E X P E R I E N C E").
- **Plain text** — no content locked inside images, icons, charts, or skill-bar graphics.
- **Consistent dates** everywhere: `MMM YYYY – MMM YYYY` (or `Present`). No bare years mixed with month-years.
- **URLs as visible text**, not hidden behind generic anchor text.
- **Exact technology spelling**: JavaScript, TypeScript, Node.js, PostgreSQL, MongoDB, React — ATS keyword matching is case/spelling sensitive.
- **Length**: 1 page for juniors, max 2 for experienced; no orphaned single line on page 2.
- Suggested file name: `Firstname_Lastname_Resume.pdf` (no "final_v3").

## Target/JD alignment (when a job description is given)

- Extract the JD's required hard skills, exact title language, and seniority signals.
- Mirror the exact terms **only where the candidate genuinely has the skill** — surface it from a buried project bullet into the Skills line and summary. Never add a keyword the candidate has no real experience with; use the closest honest phrasing instead.
- Echo the JD's title in the summary where it's honest (e.g. "Backend Engineer" vs. "Software Developer").
- In the evidence map, note which keywords you surfaced and which you deliberately left out because the candidate lacks the experience.
