# career-copilot

A suite of [Claude Code](https://claude.com/claude-code) **skills** that help you land a job — build your master profile, write and review your CV, rebuild your LinkedIn, tune your portfolio, plan your next move, run a focused job search, and write honest cover letters. Each skill is self-contained: a `SKILL.md` that tells the model how to do the job, plus `references/` files holding the detailed rubrics and checklists it loads on demand.

**New here?** Just say *"help me get a job"* (or your goal) and [`career-onboarding`](career-onboarding/) figures out which skills to run, in what order.

## The skills

| Skill | What it does |
|---|---|
| [`career-onboarding`](career-onboarding/) | The front door: learns your goal, then hands you a sequenced plan and routes you to the right skills in the right order. |
| [`career-dossier`](career-dossier/) | Consolidates your CV, GitHub, LinkedIn, and portfolio into one portable, source-tagged master profile you can paste into any AI or tool. |
| [`resume-builder`](resume-builder/) | Builds a resume from scratch by consolidating your old resume, GitHub, and LinkedIn — then surfaces the real accomplishments you under-sell, and writes an ATS-safe draft plus an evidence map tracing every claim to its source. |
| [`resume-reviewer`](resume-reviewer/) | Scores your CV like an LLM hiring screener (0–120 rubric), audits it for ATS-friendliness, and writes a prioritized fix list + a rewritten draft. |
| [`linkedin-reviewer`](linkedin-reviewer/) | Audits your LinkedIn profile section-by-section for recruiter appeal and search discoverability, and rewrites the weak parts. |
| [`linkedin-rebuilder`](linkedin-rebuilder/) | Rebuilds your *whole* LinkedIn toward one goal — ready-to-paste copy for every section — plus a guide for sharing your profile. |
| [`portfolio-reviewer`](portfolio-reviewer/) | Fetches your portfolio site, audits its value proposition, project presentation, links, and discoverability, and rewrites the weak parts. |
| [`career-advisor`](career-advisor/) | Assesses where you are, maps the gap to your target role, and produces a concrete roadmap — including which certifications are actually worth it in your field. |
| [`job-matcher`](job-matcher/) | Turns your background into a focused job search: boolean search strings, where to look, alerts, and a fit assessment for specific postings. |
| [`cover-letter`](cover-letter/) | Gates on fit first — tells you honestly when a role isn't worth applying to — then writes a truthful, tailored cover letter from your real evidence, mapped to the posting's priorities. |

Each skill's folder contains:

```
<skill>/
├── SKILL.md            # the instructions (with YAML frontmatter: name + description)
└── references/         # rubrics, checklists, and guides loaded on demand
```

## Install

Claude Code discovers skills in two locations:

- **Personal** (available in every project): `~/.claude/skills/`
- **Project** (shared with a repo, e.g. via version control): `<your-project>/.claude/skills/`

Install a skill by copying its folder into one of those directories.

### Install one skill

```bash
# personal — available everywhere
mkdir -p ~/.claude/skills
cp -r resume-reviewer ~/.claude/skills/
```

```bash
# or into a specific project
mkdir -p /path/to/your-project/.claude/skills
cp -r resume-reviewer /path/to/your-project/.claude/skills/
```

### Install all skills

```bash
mkdir -p ~/.claude/skills
cp -r career-onboarding career-dossier resume-builder resume-reviewer linkedin-reviewer linkedin-rebuilder portfolio-reviewer career-advisor job-matcher cover-letter ~/.claude/skills/
```

After copying, start (or restart) Claude Code and the skills become available. You can confirm with `/skills` or by describing your task — Claude picks the matching skill automatically based on its `description`.

## Getting started

Not sure where to begin? Describe your goal and `career-onboarding` builds you a sequenced plan. The typical full flow:

1. **`career-dossier`** — build your portable master profile once (everything else can draw from it).
2. **`resume-reviewer`** → **`resume-builder`** — diagnose your current CV, then build the tailored one.
3. **`linkedin-reviewer`** / **`linkedin-rebuilder`** and **`portfolio-reviewer`** — align your other surfaces to the same goal.
4. **`job-matcher`** — find and rank the roles you actually fit (and **`career-advisor`** if there are real gaps).
5. **`cover-letter`** — per application: fit-gate, then write from your real evidence.

### Where outputs go

Every skill writes into one organized folder in your working directory, so a full job hunt stays tidy:

```
career-copilot-output/
├── profile/      # dossier.md, career_plan.md
├── resume/       # resume_draft.md, resume_evidence_map.md, cv_review_report.md, …
├── linkedin/     # linkedin_review.md, linkedin_rebuild.md
├── portfolio/    # portfolio_review.md
└── jobs/         # job_search.md, and <company>/cover_letter.md per application
```

## Use

Just describe what you need in Claude Code and the right skill activates. For example:

- *"Help me get a job as a full-stack engineer — where do I start?"* → `career-onboarding`
- *"Pull everything about me into one master profile I can reuse."* → `career-dossier`
- *"Build me a resume from my old one at `~/Downloads/resume.pdf`, my GitHub (`@myhandle`), and my LinkedIn."* → `resume-builder`
- *"Review my CV — it's at `~/Downloads/resume.pdf` — for this job description: …"* → `resume-reviewer`
- *"Optimize my LinkedIn profile for a backend engineer role."* → `linkedin-reviewer`
- *"Rebuild my whole LinkedIn around data engineering."* → `linkedin-rebuilder`
- *"Review my portfolio at `myname.dev` for a frontend role."* → `portfolio-reviewer`
- *"I'm a data analyst who wants to move into ML engineering — what's my path?"* → `career-advisor`
- *"Help me find and rank backend jobs I'm a good fit for."* → `job-matcher`
- *"Write me a cover letter for this job posting."* → `cover-letter`

The skills are designed to work together — the `career-dossier` feeds the resume, LinkedIn, and cover-letter skills; `job-matcher` tells you which keywords to mirror; and the reviewers help you add them honestly.

## Principles

- **Grounded, never invented.** These skills never fabricate experience, metrics, or credentials — every claim traces back to what you provided.
- **Honest over flattering.** They tell you when a project is tutorial-grade, when a certification is a distraction, or when you'll be auto-filtered from a role.
- **Detail lives in references.** `SKILL.md` stays lean; the rubrics and checklists live in `references/` so they're easy to read, tune, and reuse.

## License

[MIT](LICENSE).
