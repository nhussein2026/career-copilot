# Scoring rubric

Distilled from a real LLM resume screener (written for a Software Intern screen; applies well to junior SWE roles generally). Categories total 100; bonus adds up to 20; deductions subtract; overall cap 120.

## Fairness rules (apply first)

Scores must NEVER depend on: name, gender, demographics, university/school name, GPA/grades, city/location. Evaluate ONLY: technical skills, project complexity and real-world impact, open-source contributions, work/production experience, technical communication, problem-solving evidenced in projects.

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

**Link rules (verify with curl, don't trust the CV):**
- No URL/GitHub/demo at all → score that project 30–50% lower
- Broken/inactive link → 20–30% lower
- Working live demo → 10–20% higher

**Hard rule:** only tutorial-based projects → Self Projects MUST be ≤15.

## Production — 0–25

Score from work + volunteer sections: real-world, internship, or production experience. Extra points for founder/co-founder roles or early-stage engineer (first 10–20 employees) at a startup — these demonstrate initiative and building from scratch.

## Technical Skills — 0–10

Score from skills/languages sections plus evidence of technical breadth or problem-solving in projects, work, or competitions.

## Bonus points (total ≤20)

| Bonus | Points |
|---|---|
| Google Summer of Code participation | +5 |
| Girl Script Summer of Code participation | +3 |
| Startup founder/co-founder experience | +3–5 |
| Early-stage engineer (first 10–20 employees) | +2–3 |
| Portfolio website | +2 |
| LinkedIn profile | +1 |
| High-quality technical blog | +1–3 |

Also credit Outreachy, Season of Docs, and similar open-source programs.

## Deductions

**Simple projects:** −2 to −5 if the CV has only simple tutorial projects; −1 to −3 per simple project beyond the first; −1 per generically named project ("Calculator", "Todo App", "Weather App"); −2 if all projects are classroom/tutorial-based.

**Missing links:** −3 to −5 per project with no GitHub link, demo, or URL; −2 to −3 per project with GitHub link but no live demo; −1 to −2 per broken link. Before deducting for a missing GitHub/portfolio profile, check the CV's contact/profiles section carefully — only deduct if genuinely absent.

## Scoring discipline

- Every category must be scored with cited evidence, even if 0.
- Quality over quantity: one complex project outweighs several simple ones.
- Category caps are absolute: 35 / 30 / 25 / 10; bonus ≤20; total ≤120.
