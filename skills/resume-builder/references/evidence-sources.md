# Evidence sources — how to pull, what to extract

Every source is mined for two things: **claims** (what the candidate did) and **proof** (links, repos, recommendations that back a claim). Record the source of every item so Phase 5 can map the finished resume back to it. If a source is missing, unreachable, or offline, note it and build from the rest — never fill a gap with a guess.

**Check `career-copilot-input/` first**, before asking the candidate for anything. If present, use its files directly instead of prompting for the same paths/links again:

- `resume.pdf` or `resume.md` → the old resume (Section 1 below)
- `github.txt` → a username or profile URL, one line → Section 2
- `linkedin.pdf` or `linkedin.txt` → Section 3
- `portfolio.txt` → the portfolio URL
- `target.txt` → a target role or pasted job description

Only ask for what's still missing after checking this folder.

## 1. The old resume (starting inventory, not the ceiling)

1. Read the PDF directly with the Read tool — it renders layout, so note anything a text parser would mangle (columns, tables, skill-bar graphics). Treat the PDF as ground truth over any cached/extracted text.
2. Extract URLs hidden behind anchor text ("Project Link", "Portfolio") from the annotation layer — resumes often carry their only working links there:
   ```
   python3 -c "import fitz,sys; d=fitz.open(sys.argv[1]); [print(l.get('uri')) for p in d for l in p.get_links() if l.get('uri')]" resume.pdf
   ```
3. Inventory every role, project, skill, credential, and date. Flag vague or under-specified bullets ("worked on the backend", "various improvements") — these are Phase 2 interview targets, not finished lines.
4. Note what's *absent* that a strong resume usually has: quantified outcomes, a summary line, links to work. Absence is a lead, not a defect to hide.

## 2. GitHub (proof of real, shippable work)

No token is needed for light use. Replace `<user>` and `<repo>`:

- **Profile** — `curl -s https://api.github.com/users/<user>` → name, bio, company, blog/portfolio URL, public repo count, followers.
- **Repos** — `curl -s "https://api.github.com/users/<user>/repos?per_page=100&sort=updated"` → for each: description, primary language, stars, forks, `pushed_at` (recency), `fork` flag, homepage (live demo). Stars/forks are honest scope signals; a fork with no added commits is not the candidate's work.
- **Languages per repo** — `curl -s https://api.github.com/repos/<user>/<repo>/languages` → the real language mix, better than a self-reported skills list.
- **README** — `curl -s https://raw.githubusercontent.com/<user>/<repo>/HEAD/README.md` → what the project actually does, which becomes the honest project description. If the README overstates, describe what the code shows instead.
- **Contribution vs. self-project** — check `curl -s https://api.github.com/repos/<owner>/<repo>/contributors`. A repo the candidate **owns** is a self-project even with collaborators. "Open-source contribution" means merged work in a repo they **don't** own — verify with `curl -s "https://api.github.com/search/issues?q=author:<user>+type:pr+is:merged"` (merged PRs across others' repos).
- **Pinned/most-substantial repos** — prioritize repos with real commit history, a README, and either stars or a live demo over throwaway or tutorial repos.

If GitHub is offline or rate-limited, say so and evaluate from the resume/LinkedIn alone.

### Private and unlisted repos (ask before reaching)

The API only returns **public** repos — a candidate may have far more private work (e.g. 111 total, 54 public). Real, strong work is often the hidden part. Handle it with consent:

- **Ask first.** "The API only shows your public repos — you may have private work I can't see. Do you want to share it?" Never access anything the candidate hasn't offered.
- **If they grant access** via their own authenticated GitHub CLI (local, stays on their machine): `gh repo list --visibility private --json name,description,primaryLanguage,pushedAt,url` — then mine it like any other source.
- **When a private repo is genuinely strong for the target, suggest making it public.** An employer can't verify a repo they can't open, so a public version is worth far more in an application. Frame it as an improvement to their real work, not a demand.
- **If it can't be public**, still count it honestly — describe it and mark it candidate-confirmed / "available on request" in the evidence map — but prefer public, verifiable proof in the resume itself.

## 3. LinkedIn (scope, narrative, and third-party proof)

- **Access** — fetch the URL if reachable. If it's login-walled, ask the candidate for the "Save to PDF" export (profile → *More* → *Save to PDF*) or pasted text. Don't guess at contents you can't see.
- **Experience** — capture each role's title, company, dates, and every bullet. LinkedIn bullets are often fuller than the resume's and reveal scope (team size, ownership, cross-functional work) the resume compressed away.
- **About / headline** — the candidate's own framing of what they do and want; a source for the resume summary and for target direction when no JD is given.
- **Projects & Featured** — links and descriptions of work, sometimes not on the resume or GitHub.
- **Recommendations** — high-grade evidence: other people describing the candidate's impact in their own words. A manager writing "shipped X that cut Y" is a defensible, sourced claim — mine these hard.
- **Licenses & Certifications, Volunteer, Publications** — real credentials and off-resume contributions to fold in where relevant.

## Reconciling sources

When two sources disagree (dates, titles, scope), surface the conflict to the candidate rather than silently picking one — resumes must be internally consistent and match what a recruiter will see on LinkedIn. When one source has something the others lack, that's usually recoverable value: carry it forward into Phase 2, not into the draft unexamined.
