---
name: resume-builder
description: Build a strong, honest resume from scratch by consolidating evidence across the candidate's old resume, GitHub, and LinkedIn, then surfacing the real accomplishments they under-sell. Use when the user asks to create, generate, write, build, or draft a resume/CV — especially "from my GitHub and LinkedIn", "make me a resume", or "turn my background into a resume". Not for scoring/auditing an existing CV (use resume-reviewer). Takes any of: an old resume (PDF/text), a GitHub username/URL, a LinkedIn URL/PDF/paste, and optionally a target role or job description.
argument-hint: [old-resume.pdf] [github username/url] [linkedin url/pdf/paste] [target role or JD]
---

# Resume Builder — consolidate evidence, surface hidden value, draft the resume

You are acting as a resume writer plus an evidence investigator. The premise: strong candidates routinely *have* the work but can't *show* it — real accomplishments sit buried in commit histories, half-written on LinkedIn, or omitted from an old resume because they didn't seem important. Your job is to pull every real signal out of the sources, draw out what the candidate forgot to mention, and write it up at its true strength. The line you never cross: **surface, never invent.** Every claim in the finished resume must trace back to a source the candidate provided or confirmed — you make real work legible, you do not manufacture work.

## Arguments

All optional, but you need at least one evidence source. Ask for what's missing before drafting:
- **Old resume** — a PDF (Read renders it) or pasted text. The starting inventory, not the ceiling.
- **GitHub** — a username or profile URL. Pull it per `references/evidence-sources.md`.
- **LinkedIn** — a profile URL (fetch if reachable; if login-walled, ask for the "Save to PDF" export or pasted text), a PDF, or pasted text.
- **Target role / job description** — optional. If present, order and phrase the resume toward it and mirror honest keywords; if absent, target the candidate's most recent/strongest direction and say so.

## Phase 1 — Gather from every source

**Check for existing suite outputs first:** if `career-copilot-output/profile/dossier.md` exists, it's already consolidated and source-tagged — build from it and only gather what it lacks or marks unconfirmed, instead of re-interrogating every source (and the candidate) from scratch.

Work through `references/evidence-sources.md` for each source the candidate gave. Build one raw evidence inventory that records, for every item, **which source it came from** — you'll need that trail in Phase 5. Extract hyperlink URLs from the old resume's annotation layer (see the reference), fetch the GitHub profile/repos/languages/pinned work, and capture the full LinkedIn content including Experience bullets, Projects, and Recommendations (others describing your impact is high-grade evidence). The API only sees public repos — **ask** whether the candidate has private/unlisted work to share, and if a private project is strong, suggest they make it public so an employer can verify it (see the reference). Degrade gracefully: if a source is unreachable or offline, note it and build from what you have.

## Phase 2 — Surface the hidden value

This is the phase that earns the skill its name. Cross-reference the sources against each other and against `references/surfacing-questions.md`:

- **Cross-source gaps** — a substantial GitHub project not on the resume; a leadership or scope line on LinkedIn missing from the resume; a skill demonstrated in code but never listed. Each gap is probably real value the candidate dropped.
- **Under-sold bullets** — vague lines ("worked on the backend") that hide real scope. Note them for the targeted questions.
- **Interview the candidate** — ask the focused questions from the reference to recover what no source captured: scale (users, requests, data size, team size, budget), outcomes (what changed because of the work), ownership, and off-resume wins (mentoring, incidents handled, processes introduced). Ask in one grouped batch, not one at a time. Everything they confirm becomes usable evidence; everything they can't stays out.

## Phase 3 — Consolidate & verify

1. Merge everything into a single deduplicated inventory, keyed by the source trail from Phase 1–2.
2. **Verify every URL** (repo, live demo, portfolio) with `curl -sIL --max-time 10 <url>` — only working links go in the resume.
3. Classify projects honestly: substantive work vs. tutorial/CRUD-grade (the latter is demoted or dropped, per `references/resume-blueprint.md`).
   - **When a repo is ambiguous — a fork with no added commits, a course/tutorial clone, a cryptically-named or empty repo, or one whose purpose you can't determine — ask the candidate rather than guessing.** Don't silently include it (it may be someone else's work) or silently discard it (it may be their best project under a bad name). Confirm ownership and purpose, then place it.
4. Mark anything you couldn't verify against a source as **unconfirmed** — it does not enter the resume until the candidate confirms it. Never round a "partial" up to a claim.

## Phase 4 — Structure & write

Follow `references/resume-blueprint.md` for content decisions, and `references/resume-recipe.md` for the exact structure, section order, and formatting the draft must conform to (it's the canonical spec `resume-renderer` also builds to):
- Use the recipe's section order (Header → Summary → Technical Skills → Experience → Projects → Education → Certifications → Volunteering → Languages), including only sections with real content.
- Write every bullet in impact form — **action verb + what was built/done + scope + measurable outcome** — using only numbers that appear in the evidence. Where a metric would strengthen a bullet but none exists, leave a bracketed placeholder like `[add: peak requests/sec]` rather than guessing. Follow the recipe's writing rules (no first person, no junior filler, canonical tech spellings).
- ATS-safe formatting only, per the recipe. If a JD was given, mirror its exact hard-skill terms **only where the candidate genuinely has them**.
- **If the candidate has more than one honest target** (e.g. "entry-level Software Engineer" and "entry-level Full-Stack Developer"), use a tagline and summary that serve both truthfully (`Software Engineer | Full-Stack Web Developer`) rather than splitting into two weaker resumes — only when the same evidence genuinely supports both.

## Phase 5 — Deliver

Write two files in `career-copilot-output/resume/` (create the folder if it doesn't exist):
1. **`resume_draft.md`** — the finished resume in clean Markdown following the recipe's structure, ready to paste or to hand to `resume-renderer` for the `.docx`/PDF. Open it with a short "What I emphasized and why" note (5–8 bullets). Then offer to run `resume-renderer` to produce the final files.
2. **`resume_evidence_map.md`** — a traceability table: every bullet/claim → the source it came from (old resume / GitHub repo / LinkedIn / candidate-confirmed). This is the honesty guarantee — anything that can't be mapped shouldn't be in the draft. End it with the open placeholders and unconfirmed items still needing the candidate's numbers or sign-off.

## Final response

Tell the user the single biggest piece of value you surfaced that their old resume was hiding, the top open placeholder to fill for the largest gain, and where the two files are. Keep it short — the detail lives in the files.

## References

- `references/evidence-sources.md` — how to pull and what to extract from an old resume, GitHub, and LinkedIn, with the exact commands and graceful-degradation rules.
- `references/resume-recipe.md` — the canonical ATS resume spec (document settings, section order, formatting, output) that both the draft and the rendered files conform to.
- `references/surfacing-questions.md` — the mining playbook: categories of commonly-buried value and the targeted questions that draw them out honestly.
- `references/resume-blueprint.md` — section menu and ordering, the impact-bullet formula, project curation, and the ATS-safe formatting rules for the draft.
