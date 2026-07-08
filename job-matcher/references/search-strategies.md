# Job search strategies

How to build searches that surface the right roles, where to run them, and how to make new postings come to the candidate. Tailor every string to the candidate's real target titles, skills, and constraints.

## 1. Boolean search construction

Search engines and job boards accept boolean logic. The core operators:

- `AND` — all terms must appear. Narrows results (higher precision). Many boards treat a space as `AND`.
- `OR` — any term matches. Widens results (higher recall). Use it to cover the many names one role has.
- `NOT` or `-term` — exclude noise (e.g. seniority you don't want, staffing-agency spam, wrong domain).
- `"quotes"` — exact phrase, so multi-word titles/skills stay together: `"machine learning engineer"`.
- `( )` — group logic so it evaluates the way you mean: `(react OR vue) AND typescript`.

**Cover title synonyms with OR.** One role has many names. Examples:
- Software: `("software engineer" OR "software developer" OR "backend developer" OR "full stack developer")`
- Data: `("data scientist" OR "data analyst" OR "machine learning engineer" OR "ml engineer")`
- Product: `("product manager" OR "associate product manager" OR "product owner")`

**Require the must-have skills with AND, drop nice-to-haves.** Over-constraining hides good roles — only `AND` the true must-haves:
`("backend developer" OR "software engineer") AND (python OR go) AND (postgres OR sql)`

**Cut noise with NOT.** Filter out mismatched seniority, contract types, or agencies:
`("software engineer") NOT (senior OR principal OR staff OR intern) NOT recruiter`

**Give two strings per search:**
- *Broad recall* — title synonyms only, minimal constraints. Use to scan the whole market.
- *High precision* — title synonyms `AND` must-have skills `AND` location/remote, with `NOT` exclusions. Use for a focused daily pass.

## 2. Google X-ray search (find postings and career pages directly)

Use `site:` and `intitle:` to search a specific board or company career pages that on-site search buries:

- Company pages: `("software engineer" OR "backend developer") (remote) site:boards.greenhouse.io OR site:jobs.lever.co`
- A single company's openings: `site:careers.<company>.com "software engineer"`
- LinkedIn jobs via Google: `site:linkedin.com/jobs "data analyst" "remote"`
- Title-focused: `intitle:("product manager") site:jobs.lever.co`

X-ray search is the best way to reach applicant-tracking-system postings (Greenhouse, Lever, Ashby, Workday) that never show up on aggregators.

## 3. Where to look (pick sources to fit the role and region)

- **General aggregators** — LinkedIn Jobs, Indeed, Glassdoor, Google Jobs. Broad reach; also the most competition and the most reposted/stale listings.
- **Company career pages / ATS** — Greenhouse, Lever, Ashby, Workday boards. Freshest source of truth; reach them via X-ray search or a company list.
- **Niche / specialized boards** — match to the field:
  - Startups: Wellfound (formerly AngelList Talent), Y Combinator's Work at a Startup.
  - Remote-first: We Work Remotely, Remotive, RemoteOK.
  - Engineering/product: Hacker News "Who is hiring" monthly threads, Stack Overflow-style community boards.
  - Design: Dribbble Jobs, Behance.
  - Data/ML, security, devops, etc.: the field's well-known community boards and Slack/Discord job channels.
  - Government/regulated and region-specific boards where relevant.
- **Community & network** — role-specific Slack/Discord communities, local meetups, alumni networks, and warm referrals. Referrals convert far better than cold applications; prioritize them for high-fit roles.

Pick a small shortlist rather than spraying every board. For each pick, note *why* it fits this candidate/role.

## 4. Job alerts (make postings come to you)

Re-running searches by hand misses time-sensitive early-applicant advantage. Instead:

- Save the **high-precision** string as an alert on LinkedIn and Indeed; leave the broad string for manual weekly scans.
- Set cadence deliberately: **daily** for active searches (applying early matters), weekly for passive/monitoring.
- Create a Google Alert for X-ray-style queries to catch new ATS postings and company pages.
- Keep 3–6 alerts, not 30 — too many trains you to ignore them. Tune the strings when an alert returns mostly noise.

## 5. Applying with leverage

- **Apply early.** Many roles screen on a rolling basis; the first days of a posting matter.
- **Mirror the posting's exact keywords** (honestly) in the resume/LinkedIn so both ATS and recruiter search match — coordinate with the resume-reviewer and linkedin-reviewer skills.
- **Prioritize fit.** Concentrate effort on Strong/Stretch roles with a tailored application over mass-applying to weak fits.
- **Chase a referral** for any role you genuinely fit before applying cold.
- **Track everything** — a simple sheet of company, role, date applied, source, status, and next action keeps a real search from falling apart.
