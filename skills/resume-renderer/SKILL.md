---
name: resume-renderer
description: Render a finished Markdown resume (e.g. resume-builder's resume_draft.md) into the final ATS-safe PDF and DOCX the candidate actually uploads — via a clean single-column HTML template and whatever local tool is available (WeasyPrint, pandoc, headless Chromium, LibreOffice), then verify the PDF's text layer really parses. Use when the user asks to export, render, or convert their resume/CV to PDF or Word, or to "make the final file". Takes the Markdown resume path and optionally an output name or small style preferences.
argument-hint: [resume_draft.md] [output name or style tweaks]
---

# Resume Renderer — the last mile, from Markdown to the file you upload

The other skills end at a Markdown draft; this one produces the file a candidate actually submits. The rendered PDF must obey the same ATS rules the draft was written under — a beautiful two-column export would undo everything upstream. You render locally, verify the result parses, and never ship a placeholder.

## Arguments

- **Markdown resume** — defaults to `career-copilot-output/resume/resume_draft.md`, then `cv_improved_draft.md`, if present; otherwise ask for the path.
- **Output name / style** (optional) — default file name `Firstname_Lastname_Resume.pdf` (from the resume's own contact block); style tweaks limited to what stays ATS-safe (accent color for headings, margins, font size).

## Phase 1 — Pre-flight the source

1. Read the Markdown. Strip any "What I emphasized / What changed" preamble block — that's reviewer notes, not resume content.
2. **Search for unresolved placeholders** (`[add: …]`, `[confirm: …]`). If any exist, stop and list them: the candidate either supplies the real value or the line is rephrased without it. A placeholder must never appear in a submitted file.
3. Confirm the contact block is complete (name, email, phone, links) — it becomes the document header text, never a PDF header/footer region.

## Phase 2 — Build the master document

> **Protect the folders before writing:** `career-copilot-input/` and `career-copilot-output/` hold personal data — CV, contact details, salary figures. If the working directory is a git repo, make sure `.gitignore` lists both; add whichever line is missing and tell the candidate you did.

Build to the canonical spec in `../resume-builder/references/resume-recipe.md` (document settings, section order, header rules, date tab stops, accent color, real bullets). Two routes, in preference order — both in `references/render-guide.md`:

1. **Preferred — `.docx` master (python-docx):** build the `.docx` to the recipe's settings (Calibri 10 pt, US Letter / A4, accent `#1F4E79` headings with bottom borders, right-tab dates, real list bullets, real hyperlinks with visible-URL text). This is the editable master the candidate keeps, and the source the PDF is exported from — so the two never drift.
2. **Fallback — HTML:** if python-docx isn't available and can't be installed, generate the standalone HTML template from the reference (same recipe settings) and render that.

## Phase 3 — Render the PDF (from the master)

- From a `.docx` master: `libreoffice --headless --convert-to pdf <file>.docx` — the PDF is exported **from** the docx, so both are identical (Carlito renders Calibri metrically). Deliver both files.
- From HTML: use the first available route in the reference (WeasyPrint → headless Chromium → LibreOffice).
- If no renderer exists at all, offer the one-line install (python-docx / LibreOffice) or the paste-into-Google-Docs fallback — don't leave the candidate stuck.

## Phase 4 — Verify (the point of this skill)

1. **Extract the text back out of the PDF** (`pdftotext` or PyMuPDF, commands in the reference) and check: contact block present, section headings intact and in order, no garbled or missing lines, URLs visible.
2. **Page count**: 1 page for early-career, 2 max otherwise; no orphaned single line on the last page. Adjust spacing/font size within the recipe's safe ranges and re-render rather than shipping a bad break.
3. Run the recipe's **Quality Control** pass (§10): project-description/stack cross-check, link resolution, duplicated bullets, tech-name spelling, punctuation, chronology.
4. Confirm the file name is professional (`Firstname_Lastname_Resume.pdf`/`.docx` — no `final_v3`).

## Final response

Tell the candidate the output file paths (DOCX master + PDF), that the PDF was exported from the docx and its text layer verified to parse, and the page count. If placeholders blocked rendering, lead with the list to fill instead. Keep it short.

## References

- `../resume-builder/references/resume-recipe.md` — the canonical resume spec (settings, structure, output) this skill renders to.
- `references/render-guide.md` — the python-docx build notes, the HTML fallback template, per-tool render commands, and the verification commands.
