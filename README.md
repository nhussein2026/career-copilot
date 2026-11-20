<!-- readme-standard: 1.1 -->
# career-copilot

## Overview

career-copilot is a set of 16 [Claude Code](https://claude.com/claude-code) skills that guide a job search from start to finish: a master profile, the CV, LinkedIn, GitHub and portfolio reviews, the search itself, applications, cover letters, outreach, interviews and offers. Each skill tells the model how to do one job, and every claim it writes must trace back to a source the user gave it. The skills share references and pass results to each other, so they install together as one plugin.

New here? Say *"help me get a job"* (or your goal) and [`career-onboarding`](skills/career-onboarding/) works out which skills to run, in what order.

### The skills

| Skill | What it does |
|---|---|
| [`career-onboarding`](skills/career-onboarding/) | The front door: learns your goal, then gives you a sequenced plan and routes you to the right skills in the right order. |
| [`career-dossier`](skills/career-dossier/) | Consolidates your CV, GitHub, LinkedIn and portfolio into one portable, source-tagged master profile you can paste into any AI or tool. |
| [`resume-builder`](skills/resume-builder/) | Builds a resume from your old resume, GitHub and LinkedIn, surfaces the real accomplishments you under-sell, and writes an ATS-safe draft plus an evidence map tracing every claim to its source. |
| [`resume-reviewer`](skills/resume-reviewer/) | Scores your CV like an LLM hiring screener (0–120, with rubric profiles for junior SWE, experienced SWE and non-SWE fields), audits it for ATS-friendliness, and writes a prioritised fix list and a rewritten draft. |
| [`resume-renderer`](skills/resume-renderer/) | Renders the Markdown draft into the final ATS-safe PDF or DOCX, then checks that the text layer really parses. |
| [`github-reviewer`](skills/github-reviewer/) | Audits your GitHub like a screener who clicks the link (pins, profile README, repository presentation) and writes ready-to-paste fixes. |
| [`linkedin-reviewer`](skills/linkedin-reviewer/) | Audits your LinkedIn profile section by section for recruiter appeal and search discoverability, and rewrites the weak parts. |
| [`linkedin-rebuilder`](skills/linkedin-rebuilder/) | Rebuilds your whole LinkedIn toward one goal, with ready-to-paste copy for every section and a guide for sharing your profile. |
| [`portfolio-reviewer`](skills/portfolio-reviewer/) | Fetches your portfolio site, audits its value proposition, project presentation, links and discoverability, and rewrites the weak parts. |
| [`career-advisor`](skills/career-advisor/) | Assesses where you are, maps the gap to your target role, and produces a roadmap, including which certifications are worth it in your field. |
| [`job-matcher`](skills/job-matcher/) | Turns your background into a focused search: boolean search strings, where to look, alerts, live searches when web tools are available, and a fit assessment for specific postings. |
| [`application-tracker`](skills/application-tracker/) | One table for the whole search (status, next action and due date per application), updated in plain language. |
| [`cover-letter`](skills/cover-letter/) | Checks fit first and tells you when a role is not worth applying to, then writes a truthful, tailored cover letter from your real evidence. |
| [`outreach-writer`](skills/outreach-writer/) | The messages around an application: referral asks, cold notes, follow-ups, thank-yous and status checks. |
| [`interview-prep`](skills/interview-prep/) | A STAR story bank from your real evidence, likely questions per posting, honest gap answers, a resume walkthrough and a live mock interview. |
| [`offer-advisor`](skills/offer-advisor/) | Values the offer (equity caveats included), benchmarks it against the market, reads your real leverage, and scripts an honest negotiation or compares competing offers. |

### Principles

- **Grounded, never invented.** The skills never make up experience, metrics or credentials; every claim traces back to what you provided.
- **Honest over flattering.** They tell you when a project is tutorial-grade, when a certification is a distraction, or when a role will filter you out.
- **Detail lives in references.** `SKILL.md` stays short; the rubrics and checklists live in `references/`, so they are easy to read, tune and reuse.

## Project Journey

I built career-copilot in July 2026 as an open-source personal project: AI tools can help with every step of a job search, but they also make up claims a candidate cannot back up, so every skill here works only from the user's own sources. It started with ten skills on 12 July 2026, grew to sixteen the next day, and is packaged as a Claude Code plugin that is also its own marketplace.

- **Role:** Author and maintainer
- **Team:** Solo
- **Dates:** Jul 2026 – present
- **AI use:** Written with Claude Code; the skills themselves are instructions for Claude.

## Project Status

**Maintained.** All 16 skills pass the validator in CI and install as one plugin; new skill ideas are listed in [Notes.md](Notes.md).

## Technologies

| Category | Used |
| --- | --- |
| Skills | Claude Code skills (`SKILL.md` with YAML frontmatter) and plugin manifests (`.claude-plugin/`) |
| Languages | Markdown; Python 3.12 for the validator (standard library only) |
| Infrastructure and DevOps | GitHub Actions (`validate` workflow on every push to `main` and every pull request) |

## How to Run

Prerequisite: [Claude Code](https://claude.com/claude-code).

### As a plugin (recommended)

This repository is a Claude Code plugin and its own marketplace. In Claude Code:

```
/plugin marketplace add nhussein2026/career-copilot
/plugin install career-copilot@career-copilot
```

This installs all the skills at once, which keeps the hand-offs between them working (the dossier feeding the resume, the evidence map feeding the cover letter).

### Manual copy

Claude Code also finds skills in `~/.claude/skills/` (every project) and `<your-project>/.claude/skills/` (one project):

```bash
# all skills (recommended: several skills reuse their siblings' references)
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/

# or a single skill: it still works alone, with a reduced version of the shared methods
cp -r skills/resume-reviewer ~/.claude/skills/
```

Restart Claude Code, then confirm with `/skills` or describe your task: Claude picks the matching skill from its `description`.

### Give it your details once

Put your files in a `career-copilot-input/` folder in your working directory, and every skill checks it before asking you for anything:

```
career-copilot-input/
├── resume.pdf          # or resume.md: your existing CV, any version
├── linkedin.pdf        # "Save to PDF" export, or linkedin.txt with pasted profile text
├── github.txt          # one line: your username or profile URL
├── portfolio.txt       # one line: your portfolio site URL
└── target.txt          # optional: target role, or a pasted job description
```

Every file is optional; a skill works with fewer sources and says which ones it is missing.

### Keep your data out of version control

`career-copilot-input/` and `career-copilot-output/` hold real personal data: your CV, phone number, email, and later your salary and negotiation notes. If your working directory is a git repository, ignore them before you commit anything:

```bash
printf 'career-copilot-input/\ncareer-copilot-output/\n' >> .gitignore
```

The skills check this and offer to add the lines the first time they write, but verify the `.gitignore` yourself. Nothing is uploaded anywhere: the skills read public sources (the GitHub API, your own site) and write only local files.

### Typical flow

1. **`career-dossier`**: build your master profile once; everything else can draw from it.
2. **`resume-reviewer`** → **`resume-builder`** → **`resume-renderer`**: diagnose your current CV, build the tailored one, render the final PDF.
3. **`github-reviewer`**, **`linkedin-reviewer`** or **`linkedin-rebuilder`**, and **`portfolio-reviewer`**: align your other profiles to the same goal.
4. **`job-matcher`**: find and rank the roles you fit (and **`career-advisor`** if there are real gaps); **`application-tracker`** keeps the state from here on.
5. **`cover-letter`** and **`outreach-writer`**: per application, check fit, write from your real evidence, ask for the referral, send the follow-ups.
6. **`interview-prep`** → **`offer-advisor`**: per interview, then when the offer arrives.

Example requests:

- *"Help me get a job as a full-stack engineer. Where do I start?"* → `career-onboarding`
- *"Review my CV at `~/Downloads/resume.pdf` for this job description: …"* → `resume-reviewer`
- *"Rebuild my whole LinkedIn around data engineering."* → `linkedin-rebuilder`
- *"I applied to Acme on Monday. Track it. What's due this week?"* → `application-tracker`
- *"They offered 85k base plus options. Is that fair? Help me negotiate."* → `offer-advisor`

### Where outputs go

Every skill writes into one folder in your working directory:

```
career-copilot-output/
├── profile/      # dossier.md, career_plan.md, story_bank.md
├── resume/       # resume_draft.md, resume_evidence_map.md, cv_review_report.md,
│                 # and the rendered Firstname_Lastname_Resume.pdf/.docx
├── github/       # github_review.md
├── linkedin/     # linkedin_review.md, linkedin_rebuild.md
├── portfolio/    # portfolio_review.md
└── jobs/         # job_search.md, applications.md (the tracker), and per company:
                  # <company>/cover_letter.md, outreach.md, interview_prep.md, offer_review.md
```

### Validate the suite

```bash
python3 scripts/validate.py
```

It checks each skill's frontmatter, that every `references/` path resolves, that the plugin manifests parse, and that every skill is listed in this README. CI runs the same script.

## Project Structure

```text
.
├── .claude-plugin/        plugin.json and marketplace.json
├── .github/workflows/     validate.yml: runs the validator in CI
├── scripts/validate.py    checks the skill suite
├── skills/<skill>/
│   ├── SKILL.md           the instructions (YAML frontmatter: name and description)
│   └── references/        rubrics, checklists and guides loaded on demand
└── Notes.md               improvement ideas not yet built
```

## Limitations

**Technical limitations**
- Some files are duplicated across skills on purpose (the gathering method and the honesty rules), so each skill still works when installed alone.
- There are no sample inputs or reference outputs yet, so changes to prompts and rubrics are checked by reading, not by tests.

**Future improvements**
- Ideas such as a company-researcher skill, resume variants and regional CV conventions are listed in [Notes.md](Notes.md).

## Additional Documentation

- [Notes.md](Notes.md): improvement ideas not yet built.
- Each skill's `references/` folder: the rubrics and checklists that skill uses.

## Contributing

Issues and pull requests are welcome. Run `python3 scripts/validate.py` before opening a pull request; CI runs it too.

## License

[MIT](LICENSE) © 2026 Nasser Hussein
