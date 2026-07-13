# career-copilot

A suite of [Claude Code](https://claude.com/claude-code) **skills** that cover a job hunt end to end — build your master profile, write, review, and render your CV, rebuild your LinkedIn, tune your portfolio and GitHub, plan your next move, run a focused job search, track your applications, write honest cover letters and outreach, prep your interviews, and negotiate the offer. Each skill is a folder: a `SKILL.md` that tells the model how to do the job, plus `references/` files holding the detailed rubrics and checklists it loads on demand. The skills are designed to work as a set — several reuse each other's references and outputs — so install them together (the plugin does this in one command).

**New here?** Just say *"help me get a job"* (or your goal) and [`career-onboarding`](skills/career-onboarding/) figures out which skills to run, in what order.

## The skills

| Skill | What it does |
|---|---|
| [`career-onboarding`](skills/career-onboarding/) | The front door: learns your goal, then hands you a sequenced plan and routes you to the right skills in the right order. |
| [`career-dossier`](skills/career-dossier/) | Consolidates your CV, GitHub, LinkedIn, and portfolio into one portable, source-tagged master profile you can paste into any AI or tool. |
| [`resume-builder`](skills/resume-builder/) | Builds a resume from scratch by consolidating your old resume, GitHub, and LinkedIn — then surfaces the real accomplishments you under-sell, and writes an ATS-safe draft plus an evidence map tracing every claim to its source. |
| [`resume-reviewer`](skills/resume-reviewer/) | Scores your CV like an LLM hiring screener (0–120, with rubric profiles for junior SWE, experienced SWE, and non-SWE fields), audits it for ATS-friendliness, and writes a prioritized fix list + a rewritten draft. |
| [`resume-renderer`](skills/resume-renderer/) | The last mile: renders the Markdown draft into the final ATS-safe PDF/DOCX you actually upload, then verifies the text layer really parses. |
| [`github-reviewer`](skills/github-reviewer/) | Audits your GitHub like a screener who clicks the link — pins, profile README, repo presentation — and writes the ready-to-paste fixes. |
| [`linkedin-reviewer`](skills/linkedin-reviewer/) | Audits your LinkedIn profile section-by-section for recruiter appeal and search discoverability, and rewrites the weak parts. |
| [`linkedin-rebuilder`](skills/linkedin-rebuilder/) | Rebuilds your *whole* LinkedIn toward one goal — ready-to-paste copy for every section — plus a guide for sharing your profile. |
| [`portfolio-reviewer`](skills/portfolio-reviewer/) | Fetches your portfolio site, audits its value proposition, project presentation, links, and discoverability, and rewrites the weak parts. |
| [`career-advisor`](skills/career-advisor/) | Assesses where you are, maps the gap to your target role, and produces a concrete roadmap — including which certifications are actually worth it in your field. |
| [`job-matcher`](skills/job-matcher/) | Turns your background into a focused job search: boolean search strings, where to look, alerts, live searches when web tools are available, and a fit assessment for specific postings. |
| [`application-tracker`](skills/application-tracker/) | One table for the whole hunt — status, next action, due date per application — updated in plain language, always pointing at what to do next. |
| [`cover-letter`](skills/cover-letter/) | Gates on fit first — tells you honestly when a role isn't worth applying to — then writes a truthful, tailored cover letter from your real evidence, mapped to the posting's priorities. |
| [`outreach-writer`](skills/outreach-writer/) | The messages around the application: referral asks, cold notes, follow-ups, thank-yous, status checks — channel-sized, honestly personalized, sent at the right time. |
| [`interview-prep`](skills/interview-prep/) | A STAR story bank from your real evidence, per-posting likely questions, honest gap answers, a resume walkthrough, and a live mock interview. |
| [`offer-advisor`](skills/offer-advisor/) | Values the offer (equity caveats included), benchmarks it against the market, reads your real leverage, and scripts an honest negotiation — or compares competing offers. |

Each skill's folder (under `skills/`) contains:

```
skills/<skill>/
├── SKILL.md            # the instructions (with YAML frontmatter: name + description)
└── references/         # rubrics, checklists, and guides loaded on demand
```

## Install

### As a plugin (recommended — one command, everything works together)

This repo is a Claude Code **plugin** and its own marketplace. In Claude Code:

```
/plugin marketplace add nhussein2026/career-copilot
/plugin install career-copilot@career-copilot
```

That installs all the skills at once — which also keeps the cross-skill hand-offs working (the dossier feeding the resume, the evidence map feeding the cover letter).

### Manual copy

Claude Code also discovers skills in two locations:

- **Personal** (available in every project): `~/.claude/skills/`
- **Project** (shared with a repo, e.g. via version control): `<your-project>/.claude/skills/`

```bash
# all skills (recommended — several skills reuse their siblings' references)
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/

# or a single skill — it still works alone, with a reduced version of the shared methods
cp -r skills/resume-reviewer ~/.claude/skills/
```

After installing, start (or restart) Claude Code and the skills become available. You can confirm with `/skills` or by describing your task — Claude picks the matching skill automatically based on its `description`.

### Give it your details once

Drop your files into a `career-copilot-input/` folder in your working directory (next to where `career-copilot-output/` will appear) and every skill checks it automatically before asking you for anything — no need to repeat paths/links in every conversation:

```
career-copilot-input/
├── resume.pdf          # or resume.md — your existing CV, any version
├── linkedin.pdf         # "Save to PDF" export, or linkedin.txt with pasted profile text
├── github.txt           # one line: your username or profile URL
├── portfolio.txt         # one line: your portfolio site URL
└── target.txt            # optional: target role, or a pasted job description
```

Only add what you have — every file is optional, and a skill still works with fewer sources (it just says so). This folder is gitignored, like the output folder, so nothing personal ends up in version control.

## Getting started

Not sure where to begin? Describe your goal and `career-onboarding` builds you a sequenced plan. The typical full flow:

1. **`career-dossier`** — build your portable master profile once (everything else can draw from it).
2. **`resume-reviewer`** → **`resume-builder`** → **`resume-renderer`** — diagnose your current CV, build the tailored one, render the final PDF.
3. **`github-reviewer`**, **`linkedin-reviewer`** / **`linkedin-rebuilder`**, and **`portfolio-reviewer`** — align your other surfaces to the same goal.
4. **`job-matcher`** — find and rank the roles you actually fit (and **`career-advisor`** if there are real gaps); **`application-tracker`** keeps the state from here on.
5. **`cover-letter`** + **`outreach-writer`** — per application: fit-gate, write from your real evidence, chase the referral, send the follow-ups.
6. **`interview-prep`** → **`offer-advisor`** — per interview, then when the offer lands.

### Where outputs go

Every skill writes into one organized folder in your working directory, so a full job hunt stays tidy:

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
- *"Make my GitHub look hire-ready."* → `github-reviewer`
- *"Export my resume as the final PDF."* → `resume-renderer`
- *"I applied to Acme on Monday — track it. What's due this week?"* → `application-tracker`
- *"Write a referral request to a former colleague at Stripe."* → `outreach-writer`
- *"I have an interview Thursday for this role — prep me."* → `interview-prep`
- *"They offered 85k base plus options — is that fair? Help me negotiate."* → `offer-advisor`

The skills are designed to work together — the `career-dossier` feeds the resume, LinkedIn, cover-letter, and interview skills; `job-matcher` tells you which keywords to mirror; the reviewers help you add them honestly; and `applications.md` carries the search's state between all of them.

## Principles

- **Grounded, never invented.** These skills never fabricate experience, metrics, or credentials — every claim traces back to what you provided.
- **Honest over flattering.** They tell you when a project is tutorial-grade, when a certification is a distraction, or when you'll be auto-filtered from a role.
- **Detail lives in references.** `SKILL.md` stays lean; the rubrics and checklists live in `references/` so they're easy to read, tune, and reuse.

## License

[MIT](LICENSE).
