# GitHub audit checklist

Walk every item; for each fail name the exact offending element. The standard is the 30-second recruiter visit: profile card → pinned row → maybe one README click.

## 1. Profile card

- [ ] Real name set (matches the resume), professional photo (not the default identicon)
- [ ] Bio says what they build and for what target (≤160 chars, plain words a recruiter searches for) — not empty, not a joke
- [ ] Location, company/role, and the portfolio/blog link set — link verified working (`curl -sIL`)
- [ ] Email visible or reachable via the profile link (recruiters do try)

## 2. Profile README (`<user>/<user>` repo)

- [ ] Exists (its absence wastes the best free real estate on the profile)
- [ ] Opens with who they are + what they build + the target direction — the same story as the resume
- [ ] Shows the 3–4 strongest projects with one-line descriptions and links
- [ ] Honest and current — no aspirational skill walls, no stats badges substituting for content
- [ ] Short: a landing page, not an autobiography

## 3. The pinned row (highest leverage)

- [ ] All six slots used, or deliberately fewer — never left on the defaults
- [ ] Pins = the strongest, target-relevant work, strongest first
- [ ] No tutorials, course clones, empty repos, or unmodified forks in the pins
- [ ] Every pinned repo has a description and a real README (a pin invites a click — a default README wastes it)

## 4. Per-repo hygiene (top ~10 visible repos)

- [ ] One-line description set (what it is + stack) — not blank, not the repo name restated
- [ ] Topics/tags set with the searchable tech terms
- [ ] README states: what it does, why it exists, the stack, how to run it, and a screenshot or demo link where visual
- [ ] Homepage field points at the live demo when one exists (and the link works)
- [ ] License present on anything presented as serious
- [ ] No description promising what the code doesn't contain (READMEs are claims — the resume-reviewer cross-checks them)

## 5. Activity & contributions

- [ ] Recent activity visible (pushes within the last ~3 months; an all-gray year next to "actively looking" undercuts the story)
- [ ] Merged PRs in repos they don't own listed accurately — contribution claims match the `search/issues` results
- [ ] Forks with no added commits are not presented (or pinned) as own work

## 6. Consistency with the resume / dossier

- [ ] The projects the resume highlights are the ones pinned and polished here
- [ ] Same name, same links, no contradictions in what each project is claimed to do
- [ ] Languages shown by the repos roughly support the resume's skills list

## The README skeleton (for the top repos)

```markdown
# <Project name>

<One sentence: what it does and for whom.>

**Live demo:** <url> · **Stack:** <React, Node.js, PostgreSQL, …>

## Why
<2–3 sentences: the real problem it solves; team size and the candidate's role if not solo.>

## Features
- <3–6 bullets of what actually works today>

## Running it
```bash
<the actual commands>
```

<Screenshot or short GIF if the project is visual.>
```

Fill it only with what the code shows — an overstating README costs more credibility than a thin one.

## Curation rules

- **Pin**: 4–6 repos, target-relevant, strongest first. Rework the pin row whenever the target role changes.
- **Archive** (Settings → Archive): tutorials, dead experiments, empty repos. Archiving keeps history but removes noise from the profile. Recommend; the candidate executes.
- **Make public**: when a private repo is genuinely strong for the target, suggest a public version — an employer can't verify what they can't open. Consent first, always.
- **Ask** about anything ambiguous before classifying it (fork? course work? someone else's project?).
