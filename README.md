# career-copilot

A small suite of [Claude Code](https://claude.com/claude-code) **skills** that help you land a job — review your CV, tighten your LinkedIn, plan your next career move, and run a focused job search. Each skill is self-contained: a `SKILL.md` that tells the model how to do the job, plus `references/` files holding the detailed rubrics and checklists it loads on demand.

## The skills

| Skill | What it does |
|---|---|
| [`resume-reviewer`](resume-reviewer/) | Scores your CV like an LLM hiring screener (0–120 rubric), audits it for ATS-friendliness, and writes a prioritized fix list + a rewritten draft. |
| [`linkedin-reviewer`](linkedin-reviewer/) | Audits your LinkedIn profile section-by-section for recruiter appeal and search discoverability, and rewrites the weak parts. |
| [`career-advisor`](career-advisor/) | Assesses where you are, maps the gap to your target role, and produces a concrete roadmap — including which certifications are actually worth it in your field. |
| [`job-matcher`](job-matcher/) | Turns your background into a focused job search: boolean search strings, where to look, alerts, and a fit assessment for specific postings. |

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
cp -r resume-reviewer linkedin-reviewer career-advisor job-matcher ~/.claude/skills/
```

After copying, start (or restart) Claude Code and the skills become available. You can confirm with `/skills` or by describing your task — Claude picks the matching skill automatically based on its `description`.

## Use

Just describe what you need in Claude Code and the right skill activates. For example:

- *"Review my CV — it's at `~/Downloads/resume.pdf` — for this job description: …"* → `resume-reviewer`
- *"Optimize my LinkedIn profile for a backend engineer role."* → `linkedin-reviewer`
- *"I'm a data analyst who wants to move into ML engineering — what's my path?"* → `career-advisor`
- *"Help me find and rank backend jobs I'm a good fit for."* → `job-matcher`

The skills are designed to work together — e.g. `job-matcher` tells you which keywords to mirror, and `resume-reviewer` / `linkedin-reviewer` help you add them honestly.

## Principles

- **Grounded, never invented.** These skills never fabricate experience, metrics, or credentials — every claim traces back to what you provided.
- **Honest over flattering.** They tell you when a project is tutorial-grade, when a certification is a distraction, or when you'll be auto-filtered from a role.
- **Detail lives in references.** `SKILL.md` stays lean; the rubrics and checklists live in `references/` so they're easy to read, tune, and reuse.

## License

[MIT](LICENSE).
