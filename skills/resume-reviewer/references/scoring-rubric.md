# Scoring rubric

Three rubric profiles share one skeleton — four categories totaling 100, bonus ≤20, deductions subtract, overall cap 120 — but weight the categories differently, because what predicts hiring changes with seniority and field. **Select the profile first**; scoring a senior engineer or a designer with the junior-SWE weights produces a confidently wrong number.

## Profile selection (do this before scoring)

Pick from the CV's own evidence (years of experience, field, target role) — state the profile and the reason at the top of the report:

- **Profile A — Student / early-career software engineer** — still studying, or ≤ ~3 years of professional software work. Open source and self-projects are the strongest signal available at this stage. (Distilled from a real LLM screener written for a Software Intern role.)
- **Profile B — Experienced software engineer** — 3+ years of professional software work. Production impact dominates; OSS and personal projects are secondary signals whose *absence* is not damning.
- **Profile C — Non-SWE fields** — design, product, data/analytics, marketing, ops, and other fields where GitHub-centric rules don't apply. The field's native proof of work (case studies, dashboards, campaigns, publications) plus work impact carry the score.

If a CV straddles profiles (e.g. a data scientist with heavy engineering), pick the profile matching the **target role** and say so.

## Fairness rules (all profiles, apply first)

Scores must NEVER depend on: name, gender, demographics, university/school name, GPA/grades, city/location. Evaluate ONLY: technical/domain skills, project complexity and real-world impact, contributions and proof of work, work/production experience, communication, problem-solving evidenced in the work.

## Link rules (all profiles — verify with curl, don't trust the CV)

- No URL/GitHub/demo/case-study link for a claimed project → score that item 30–50% lower
- Broken/inactive link → 20–30% lower
- Working live demo / published case study → 10–20% higher

---

# Profile A — Student / early-career SWE

Categories: **Open Source /35 · Self Projects /30 · Production /25 · Technical Skills /10.**

## Open Source — 0–35

| Band | Points | Evidence required |
|---|---|---|
| High | 25–35 | Contributions to popular projects (1000+ stars), significant contributions to well-known projects, GSoC participation, substantial community involvement |
| Medium | 15–24 | Contributions to smaller open-source projects, active GitHub presence with meaningful contributions **to other people's repositories** |
| Low | 5–10 | Only personal repos, minimal open-source activity. Hacktoberfest alone (no significant-project contributions): 3–5 max |
| Very low | 0–4 | No GitHub presence, or only tutorial-derived personal repos |

**Hard rules:**
- Personal repositories do NOT count as open-source contribution. Open source = contributing to OTHER people's projects.
- If GitHub data shows all projects are single-contributor (`self_project`), Open Source MUST be ≤10, and apply a 3–5 point deduction for lack of true contributions.
- Do not list "open source" as a key strength unless there are actual contributions to others' projects.
- "Google Summer of Code (GSoC)" and "Girl Script Summer of Code" are different programs — never conflate them.

## Self Projects — 0–30

| Band | Points | Evidence required |
|---|---|---|
| High | 20–30 | Complex projects with real-world impact, advanced architecture, multiple technologies, user adoption |
| Medium | 10–19 | Some complexity, good documentation, multiple features or moderate technical challenge |
| Low | 1–9 | Tutorial-grade: todo lists, calculators, weather apps, note/recipe/exercise apps, basic sentiment analysis with standard libraries, classroom assignments |
| Zero | 0 | No projects, only trivially basic ones, or **basic CRUD applications (mandatory 0)** |

**Complexity signals (high):** full-stack with multiple features, auth + database, ML/AI, real-time (chat/streaming), mobile with native features, microservices, significant user adoption, real-world problem solved, advanced algorithms/data structures.

**Hard rule:** only tutorial-based projects → Self Projects MUST be ≤15.

## Production — 0–25

Score from work + volunteer sections: real-world, internship, or production experience. Extra points for founder/co-founder roles or early-stage engineer (first 10–20 employees) at a startup — these demonstrate initiative and building from scratch.

## Technical Skills — 0–10

Score from skills/languages sections plus evidence of technical breadth or problem-solving in projects, work, or competitions.

---

# Profile B — Experienced SWE (3+ years)

Categories: **Production & impact /45 · Technical depth /20 · Open Source /20 · Self Projects /15.**

## Production & impact — 0–45

| Band | Points | Evidence required |
|---|---|---|
| High | 35–45 | Clear ownership of production systems with quantified outcomes (scale, latency, reliability, revenue/cost), leadership signals (led projects or people, mentored, drove migrations/incidents), visible progression (promotions, growing scope) |
| Medium | 20–34 | Solid production work described concretely but thinly quantified; steady responsibility without visible growth in scope |
| Low | 5–19 | Vague "worked on / responsible for" bullets that hide scope; titles without evidence of what was actually built or changed |
| Very low | 0–4 | No verifiable production work |

**Hard rules:**
- **Titles alone earn nothing.** A senior/staff title with vague bullets scores below a mid-level CV with quantified outcomes — the CV is judged on what it shows.
- Founder/co-founder and early-stage-engineer credit applies as in Profile A.

## Technical depth — 0–20

Evidence of depth, not lists: systems designed and their trade-offs, performance/scaling numbers, debugging or migration war stories, breadth across the stack with named production use. A bare skills list with no supporting evidence anywhere → ≤8.

## Open Source — 0–20

Same definitions as Profile A (contribution = merged work in repos the candidate does NOT own; personal-repos-only caps this at ≤6). **No GitHub at all → this category scores 0, but apply no extra deductions** — many strong engineers work entirely in private codebases; note it neutrally in the report.

## Self Projects — 0–15

Same complexity signals as Profile A, scaled down. The CRUD-0 rule applies only to projects presented as flagship work. A tutorial-grade project on an experienced CV is worse than none — deduct per the deductions table rather than merely scoring it low.

---

# Profile C — Non-SWE fields

Categories: **Proof of work /40 · Work experience & impact /40 · Tools & skills /10 · Community & credentials /10.**

## Proof of work — 0–40

The field's native portfolio, judged the way Profile A judges projects:

- **Design/UX** — case studies showing problem → process → outcome (not just final screens)
- **Product** — shipped features/products with the candidate's role and measurable outcomes
- **Data/analytics** — dashboards, notebooks, published analyses, models with stated impact
- **Marketing/content** — campaigns with real numbers, published work, audience growth
- **Other fields** — whatever a hiring manager in that field accepts as verifiable work product

| Band | Points |
|---|---|
| High | 30–40 — multiple substantive, verifiable pieces aligned to the target role, with outcomes |
| Medium | 15–29 — real proof but thin, unquantified, or misaligned with the target |
| Low | 1–14 — claims with little verifiable backing |
| Zero | 0 — no proof of work at all (make this the report's headline gap) |

## Work experience & impact — 0–40

Same logic as Profile B's Production & impact, in the field's terms: scope owned, outcomes changed, progression, leadership. Titles alone earn nothing.

## Tools & skills — 0–10

The field's toolchain, honestly leveled, with evidence of use in the work above.

## Community & credentials — 0–10

Certifications **where they're real hiring filters in that field** (cross-check `../../career-advisor/references/certifications-by-field.md` when installed), publications, talks, awards, community leadership.

---

## Bonus points (all profiles, total ≤20)

| Bonus | Points | Applies to |
|---|---|---|
| Google Summer of Code participation | +5 | A, B |
| Girl Script Summer of Code participation | +3 | A, B |
| Startup founder/co-founder experience | +3–5 | all |
| Early-stage engineer/employee (first 10–20) | +2–3 | all |
| Portfolio website | +2 | all |
| LinkedIn profile | +1 | all |
| High-quality technical/field blog or publications | +1–3 | all |
| Field awards, competitions, recognized publications | +1–3 | C |

Also credit Outreachy, Season of Docs, and similar open-source programs (A, B).

## Deductions (all profiles unless noted)

**Simple projects:** −2 to −5 if the CV has only simple tutorial projects; −1 to −3 per simple project beyond the first; −1 per generically named project ("Calculator", "Todo App", "Weather App"); −2 if all projects are classroom/tutorial-based. **Profile B:** −2 to −4 for a tutorial-grade project presented as flagship work on an experienced CV.

**Missing links:** −3 to −5 per claimed project/case study with no link, demo, or URL; −2 to −3 per project with a repo link but no live demo (Profile A only); −1 to −2 per broken link. Before deducting for a missing GitHub/portfolio profile, check the CV's contact/profiles section carefully — only deduct if genuinely absent, and in Profile B don't deduct for a missing GitHub at all.

## Scoring discipline

- Name the profile applied (and why) before any score.
- Every category must be scored with cited evidence, even if 0.
- Quality over quantity: one complex, verifiable piece outweighs several simple ones.
- Category caps are absolute per profile; bonus ≤20; total ≤120.
