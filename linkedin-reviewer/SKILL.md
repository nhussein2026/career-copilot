---
name: linkedin-reviewer
description: Review a LinkedIn profile the way a recruiter and LinkedIn's search ranking would, then produce a prioritized fix list and rewritten copy for the weak sections. Use when the user asks to review, audit, optimize, or improve their LinkedIn profile, or to make it more discoverable to recruiters. Takes a LinkedIn profile URL, a PDF export of the profile, or pasted profile text, and optionally a target role/job description for keyword alignment.
argument-hint: <linkedin-url | profile.pdf | pasted profile text> [target role or job description]
---

# LinkedIn Review — audit and optimize a profile

You are acting as a technical recruiter plus a LinkedIn SEO coach. Recruiters skim; LinkedIn's search ranks profiles on keyword match, completeness, and activity. Your job is to judge the profile on both, then rewrite the weak parts. Never invent experience, titles, employers, or metrics — every claim traces back to what the candidate supplied.

## Arguments

- First argument: the profile. A LinkedIn URL (fetch it if reachable; if the fetch is blocked by login walls, ask the user to paste the profile text or attach the "Save to PDF" export from their profile's *More* menu), a PDF export, or pasted text.
- Remaining arguments (optional): a target role title or a job description. If present, run keyword alignment against it; if absent, evaluate against the candidate's own most recent role and say so.

## Phase 1 — Gather

1. Get the full profile content: headline, About, every Experience entry, Education, Skills, Licenses & Certifications, Projects, Recommendations, and the custom URL.
2. Note what's visually or structurally missing — no profile photo, default banner, empty About, "Skills" with fewer than 5 entries, no custom vanity URL (`/in/firstname-lastname`), no recent activity.
3. If a target role/JD is provided, extract its hard skills, title language, and seniority signals for Phase 3.

## Phase 2 — Section-by-section audit

Walk every item in `references/profile-checklist.md`. For each section, record: present / weak / missing, and the specific offending element. Pay special attention to the three highest-leverage fields, because recruiters and search weight them most:

- **Headline** — the single most important field. 220 chars. Should say role + specialization + value/keywords, not just the current job title. This is indexed heavily in recruiter search.
- **About** — first 2–3 lines show before the "see more" fold; they must hook. First person, concrete, keyword-rich without stuffing.
- **Experience** — each role needs a one-line scope statement plus 2–4 impact bullets, mirroring resume impact form (action + what + measurable outcome).

## Phase 3 — Keyword & discoverability alignment

- Check that the target-role hard skills appear in the Headline, About, Experience, and the Skills section (LinkedIn search weights the Skills list and Headline strongly). Record present / present-but-buried / absent.
- Verify the top 3 Skills are pinned and reflect the target role (LinkedIn lets you pin 3 that show first).
- Flag honesty issues: endorsements or "expert" framing not backed by experience — recommend the closest honest phrasing instead of removing real skills.

## Phase 4 — Report + rewrites

Write `linkedin_review.md` in `career-copilot-output/linkedin/` (create the folder if it doesn't exist):

1. **Completeness score** — a simple table: section → status (strong / weak / missing) → why.
2. **Prioritized fix list** — High / Medium / Low by recruiter impact. High = the Headline, the About hook, missing photo/custom URL, or an empty Skills section.
3. **Rewritten copy** — ready-to-paste replacements for the Headline, the About section, and the bullets of the 2 most recent roles. Give 2 headline options. Keep every rewrite truthful to the source.
4. **Keyword gap table** (if a target role was given) — term → status → where to add it honestly.

## Final response

Tell the user the completeness score, the single highest-leverage fix, and where the file is. Keep it short.

## References

- `references/profile-checklist.md` — the full section-by-section LinkedIn audit checklist.
