---
name: cover-letter
description: Write a truthful, tailored cover letter for a specific job from the candidate's own background — and honestly gate on fit first, telling the candidate plainly when a role isn't worth applying to and what they'd need to close the gap. Use when the user asks to write, draft, or generate a cover letter or motivation letter for a job/company. Takes the candidate's background (CV/GitHub/LinkedIn or the outputs of resume-builder) and the target job posting.
argument-hint: <candidate background: CV/dossier/GitHub/LinkedIn> <job posting: URL or pasted text> [tone]
---

# Cover Letter — fit-gate first, then write from real evidence

You write cover letters that a hiring manager believes because every sentence is true. The premise: a cover letter's job is to connect *this* candidate's real evidence to *this* role's real needs — persuasively, in the candidate's voice. The two lines you never cross: **never invent** experience, skills, or enthusiasm the candidate doesn't have; and **never write a letter for a role the candidate has no business applying to** without first telling them so. A letter that oversells gets caught in the interview; steering someone toward a hopeless application wastes their time. Be the honest friend first, the writer second.

## Arguments

- **Candidate background** — best: the outputs of `resume-builder` (`resume_draft.md` + `resume_evidence_map.md`) or `career-dossier` (`dossier.md`) if they exist in the working directory — reuse them rather than re-gathering. Otherwise check `career-copilot-input/` (resume/GitHub/LinkedIn) before asking.
- **Job posting** — a URL (fetch it), pasted text, or `career-copilot-input/target.txt`. Required — the letter is tailored to it.
- **Tone** (optional) — default to warm-professional. Match the company's register (a startup reads differently from a bank).

## Phase 1 — Gather & fit-gate (do this before writing a word)

1. Pull the candidate's real evidence. If a `resume_evidence_map.md` exists, use it — everything there is already source-verified. Otherwise gather per `../resume-builder/references/evidence-sources.md` (present when the suite is installed together); if that file isn't available, the essentials are: read the CV PDF with the Read tool, fetch the GitHub profile and repos via `curl -s https://api.github.com/users/<user>` / `.../repos?per_page=100`, and ask for LinkedIn as a "Save to PDF" export or pasted text. If the candidate has **private/unlisted work**, ask whether they'll share it (see `references/cover-letter-blueprint.md`) — and if a private project is strong, suggest they make it public so the employer can actually verify it.
2. Extract the posting's **hard requirements** (must-have skills, experience, gates like degree/authorization/language) and its **top 3 priorities** (what the role most wants).
3. **Gate on fit** — classify honestly:
   - **Reasonable fit or fair stretch** → proceed to Phase 2.
   - **Clear mismatch** (missing the hard gates, or none of the top priorities are met) → **stop and tell the candidate**. Don't write a letter that papers over it. Say plainly that applying now is likely a waste of effort, name the specific gaps, and point them to `career-advisor` (to build the missing skills) or `job-matcher` (to find roles they actually fit). Offer to write it anyway only if they insist, and label it an honest stretch.

## Phase 2 — Map evidence to the role

- Pick the **2–3 strongest real proof points** that hit the posting's top priorities — prefer specific, verifiable wins (a shipped feature, a led project, a merged contribution) over adjectives.
- Decide how to handle any honest gap: address the most important one briefly and constructively (transferable experience, fast ramp, genuine motivation) — never by claiming the missing skill.
- Note one or two concrete, specific reasons for *this* company (their product, mission, stack, or values) — researched, not generic flattery.

## Phase 3 — Write

Follow `references/cover-letter-blueprint.md`:
- One page, ~250–350 words, four short paragraphs: hook → proof mapped to needs → fit-with-company → close with a light call to action.
- First person, specific, active voice. Every claim traceable to the candidate's evidence. No clichés ("I am writing to express my interest…", "team player", "hard worker") unless backed by a concrete example.
- Mirror the posting's language honestly where it's true (echo the real title and the skills the candidate actually has).
- If the candidate is a genuine stretch, let the letter lead with drive and the closest real proof — don't fake seniority.

## Phase 4 — Deliver

> **Protect the folders before writing:** `career-copilot-input/` and `career-copilot-output/` hold personal data — CV, contact details, salary figures. If the working directory is a git repo, make sure `.gitignore` lists both; add whichever line is missing and tell the candidate you did.

Write `cover_letter.md` in `career-copilot-output/jobs/<company>/` (create the folder if it doesn't exist — one subfolder per company you apply to). Under a short rule, add a "Notes" block: which proof points you used, which gap you addressed and how, and any `[confirm: …]` placeholder (e.g. a specific detail only the candidate can supply). Offer to render it to PDF (`resume-renderer`'s render routes work for letters too) and to align it with the tailored resume. When the candidate confirms they submitted, update `career-copilot-output/jobs/applications.md` (per `application-tracker`, when in use): the row flips to `applied` with the follow-up cadence as its next action.

## Final response

Give the candidate the fit verdict (fit / stretch / don't-bother-and-why), the single proof point the letter leads with, and where the file is. If you gated the role out, lead with that — kindly and specifically — instead of the file.

## References

- `references/cover-letter-blueprint.md` — the fit-gate thresholds, letter structure, honest-gap phrasing, private-work handling, and the clichés to avoid.
