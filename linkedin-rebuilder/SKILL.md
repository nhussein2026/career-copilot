---
name: linkedin-rebuild
description: Rebuild an entire LinkedIn profile so every section pulls toward one goal — produce ready-to-paste copy for the headline, About, each Experience entry, Skills, and Featured, plus the profile-hygiene fixes, aligned end-to-end to a single target role. Includes a guide for sharing the profile since LinkedIn blocks automated access. Use when the user wants to rebuild, overhaul, or fully rewrite their LinkedIn (not just audit it — that's linkedin-reviewer). Takes the profile (URL/PDF/paste) and a target role/goal, optionally the resume or dossier.
argument-hint: <linkedin url/pdf/paste> <target role or goal> [resume or dossier]
---

# LinkedIn Rebuild — rewrite the whole profile toward one goal

Where `linkedin-reviewer` audits and fixes the weak parts, you **rebuild the whole thing** so every section reinforces one target. A profile fails when its pieces point in different directions — an old-career headline, an About that rambles, Skills that don't match the goal. You produce ready-to-paste copy for every section, pulling in one direction. Never invent roles, titles, or skills — rewrite what's real into its strongest, most aligned form.

## Phase 0 — Get the profile (share guide)

LinkedIn blocks automated fetches (an HTTP 999). If you don't already have the content, give the candidate this and wait — don't guess at what's on the profile:

> **How to share your LinkedIn profile:** open your profile → click **More** (below your headline) → **Save to PDF** → attach that file. Or copy-paste each section (Headline, About, every Experience entry, Skills, Education) as text. Either works.

If a resume or `dossier.md` exists, use it to cross-check and to source facts — but you still need the current LinkedIn text to know what to rewrite.

## Phase 1 — Lock the goal

Settle the **single target** the whole profile should serve (one role/specialization). Everything downstream is judged by "does this move me toward that target?" If the candidate gives two very different goals, have them pick the primary — one profile can't optimize for both.

## Phase 2 — Rebuild every section toward the goal

Follow `references/rebuild-playbook.md`. Produce ready-to-paste copy for:

- **Headline** (2 options) — role + specialization + value/keywords, target term in the first ~40 chars.
- **About** — full rewrite: a hook in the first 2–3 lines (shown before "…see more"), first person, concrete, keyword-rich, ending in a call to action.
- **Experience** — for each role: a one-line scope statement + 2–4 impact bullets, all angled toward the target and matching the resume.
- **Skills** — the full list to set, with the **top 3 to pin** (weighted in search), mirroring the target's exact terms — only skills genuinely held.
- **Featured** — which projects/posts/links to feature as proof.
- **Profile hygiene** — photo, banner, custom vanity URL, location, "Open to work", contact info: what to set.

## Phase 3 — Consistency pass

Check the rebuilt profile against `linkedin-reviewer`'s `references/profile-checklist.md` concerns: no leftover old-career language anywhere, no contradiction with the resume/dossier (titles, dates, scope), keywords aligned across Headline + About + Skills. One coherent identity, one goal.

## Phase 4 — Deliver

Write `linkedin_rebuild.md` in `career-copilot-output/linkedin/` (create the folder if it doesn't exist): every section's new copy in the order it appears on the profile, ready to paste, each labeled with where it goes. Open with a 1-line "how to apply this" note and close with the profile-hygiene checklist to tick off.

## Final response

Give the candidate the single highest-leverage change (usually the Headline or the About hook), confirm the whole profile now points at their one goal, and where the file is. Keep it short.

## References

- `references/rebuild-playbook.md` — per-section rewrite specs, the pin-the-top-3 mechanics, and the share guide.
