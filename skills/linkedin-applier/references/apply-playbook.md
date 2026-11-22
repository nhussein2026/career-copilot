# Apply playbook — driving the browser without breaking anything

Written tool-agnostically: it applies whether the browser is driven by Claude in Chrome, another extension, or a human following along. Everything here assumes the candidate's own logged-in session — no scraping infrastructure, no credential handling, no second account.

## Session setup

1. **Use the existing session.** Open a new tab in the browser the candidate is already logged into. Never ask for LinkedIn credentials, never attempt a login flow, never touch a password manager. If the session is logged out, stop and ask the candidate to log in themselves.
2. **Set the default resume first.** On LinkedIn, `Jobs → Application settings → Manage your resumes`: upload the current rendered PDF and make it the top entry. Easy Apply offers the most recent resumes first, so this removes an upload step (and an upload mistake) from every subsequent application.
3. **One posting per tab**, closed when done. A long-lived tab pile makes it easy to double-apply.
4. **Read the page before acting.** Take the page's text/accessibility tree rather than clicking blind — Easy Apply modals vary by posting, and a click aimed at a remembered coordinate lands on the wrong control.

## Pace and volume

LinkedIn's User Agreement prohibits automated access; the observable enforcement is rate-based and behavioral. Keep the session indistinguishable from an attentive human:

- **5–10 applications per session**, one session a day. Beyond that the marginal application is low-quality anyway.
- **Read at reading speed.** Don't fire a burst of navigations; each posting gets a real triage pass.
- **No infinite scroll harvesting.** Page through search results normally, and only as far as the batch needs.
- **Never touch anything that isn't the application** — don't send connection requests, don't message recruiters as a side effect (that's `outreach-writer`, deliberately, later), don't edit the profile, don't follow companies in bulk.
- If LinkedIn shows a checkpoint, CAPTCHA, or "unusual activity" notice: **stop the session entirely** and tell the candidate. Do not solve it, do not retry, do not switch tactics to get around it.

## Search and triage

Paste the candidate's boolean string into the keyword box (LinkedIn requires `OR`/`AND`/`NOT` in uppercase; quoted phrases for multi-word titles). Apply the saved filters: experience level, date posted, remote/on-site, location, and — under *All filters* — "Under 10 applicants" when available. Sort by **Most recent**.

For each result, read the full description before opening a form. Kill on any hard gate: a years-of-experience floor above the candidate's real number, a required technology that is a hard zero, an on-site requirement in a city they can't reach, a language requirement above their real level, or authorization they don't have. Postings that survive get applied to; the rest get one line of reason in the session summary.

Note the **posting date and applicant count** — a two-week-old posting with 400 applicants is a worse use of the batch than a fresh one with 8.

## LinkedIn Easy Apply — the step map

Easy Apply is a modal wizard, typically 2–5 steps, with a progress bar. The steps, in the order they usually appear:

1. **Contact info** — name, email, phone (country code + number). Pre-filled from the profile; verify rather than retype.
2. **Resume** — choose the default resume set up above, or upload the specific PDF. Verify the *filename shown after upload* matches the intended file. This is the most common silent error: an old CV attached to a good application.
3. **Additional questions** — the screeners. Fill **only** from the answer bank. Radio buttons and dropdowns often default to the first option — an untouched default is an answer the candidate never gave, so set every one explicitly or leave it visibly `[unanswered]`.
4. **Work authorization / EEO** — Class B answers; see `screener-answers.md`. Voluntary demographic questions are the candidate's alone.
5. **Review** — **stop here.** Summarize every field's final value, flag anything unanswered, and hand back the click.

Notes:
- **"Follow `<Company>`" is pre-checked** on the final step. Leave it or untick it per the candidate's preference — but tell them it's there; it posts activity to their network.
- **Multi-step forms lose state** if the modal is dismissed. Don't navigate away mid-wizard; finish or discard deliberately.
- **"Save" vs "Submit"** — LinkedIn's draft save keeps a partial application. It is a fine parking spot when a Class B answer is missing.

## External ATS fallback

Many postings route to the company's own system. The rules don't change; the mechanics do.

- **Greenhouse / Lever / Ashby** — plain forms. Fill the same bank; upload the same PDF. These usually parse the resume into fields — **re-read every parsed field**, since resume parsers routinely mangle dates, employers, and phone numbers. Fix them to match the resume exactly.
- **Workday** — wants an account per employer. Account creation is the candidate's decision (it's a new credential); ask before creating one, and let them set the password. Workday's multi-page flow saves drafts, so a session can stop at the review page cleanly.
- **"Apply with your profile" / one-click aggregators** — check what they actually send; if it submits the LinkedIn profile rather than the rendered resume, prefer the company's own form when one exists.
- Any site demanding credentials, payment, or ID documents to apply is a red flag — stop and tell the candidate.

## Failure recovery

- **Field won't accept input** — it's usually a custom dropdown or a masked input, not a text box. Read the DOM/accessibility tree and interact with the real control rather than retyping.
- **Form rejects the answer** (e.g. numeric field, text entered) — re-read the constraint and reformat; never change the *substance* of an answer to satisfy a validator.
- **Two failed attempts on the same control** — stop, describe what's stuck, and let the candidate finish that field by hand. Don't loop.
- **Posting is closed / 404** — mark it closed in the summary, don't log it to the tracker.
- **Duplicate detected** (already in `applications.md`) — skip and say so. Double-applying reads as careless to the recruiter who sees both.

## After the batch

Report per posting: company, role, link, fit verdict, submitted or stopped-for-review, and anything left unanswered. Then log the submitted ones to the tracker (`../../application-tracker/references/tracker-format.md`), each with its follow-up due date. The next action after a batch is never "apply more" — it's the follow-up cadence on what was already sent.
