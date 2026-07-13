# Render guide — template, tools, verification

Everything here serves one rule: the rendered file must parse at least as well as the Markdown did. No columns, no graphics carrying content, no text in header/footer regions. Build to the spec in `../../resume-builder/references/resume-recipe.md`.

## Preferred route — `.docx` master + PDF exported from it

The recipe makes the `.docx` the editable master and the PDF an export of it, so they never drift. Build with **python-docx** (`pip install python-docx` if missing) to the recipe's settings, then convert with LibreOffice.

Key python-docx mechanics for the recipe:
- **Page + margins:** `section.page_width/height = Inches(8.5)/Inches(11)` (US Letter; A4 = `Cm(21)/Cm(29.7)`); margins `Inches(0.5)` top/bottom, `Inches(0.6)` left/right.
- **Base font:** set the Normal style font to Calibri 10 pt, colour `#212121`, line spacing 1.05. Carlito (installed) renders Calibri metrically in the PDF.
- **Name / tagline:** centered paragraphs; name run bold 18 pt ALL CAPS; tagline bold 11 pt colour `#1F4E79`.
- **Section heading:** paragraph, run bold 11 pt ALL CAPS colour `#1F4E79`; add a bottom border via the paragraph's `pPr` (`w:pBdr` → `w:bottom`).
- **Right-aligned dates:** add a right tab stop at `page_width − left − right` (US Letter = `Inches(7.3)`) with `WD_TAB_ALIGNMENT.RIGHT`; put a `\t` between the title text and the date run (date run colour `#555555`).
- **Real bullets:** use the built-in `List Bullet` style — not typed "•" characters.
- **Hyperlinks (visible URL text):** python-docx has no native helper; add the relationship (`part.relate_to(url, RT.HYPERLINK, is_external=True)`) and build a `w:hyperlink` element wrapping a run whose text is the readable URL. Use `mailto:` for the email.

Convert to PDF (identical to the docx):
```bash
libreoffice --headless --convert-to pdf Firstname_Lastname_Resume.docx --outdir .
```
Deliver both `Firstname_Lastname_Resume.docx` and `.pdf`.

## Fallback — the HTML template

Use only when python-docx can't be installed. Fill the body from the Markdown (headings → `h2`, roles → the `role` block, bullets → `ul`). Keep it standalone — all CSS inline in `<style>`, no external assets. Match the recipe's settings (single column, Calibri/Arial, accent `#1F4E79`, visible URLs).

Fill the body from the Markdown (headings → `h2`, roles → the `role` block, bullets → `ul`). Keep it standalone — all CSS inline in `<style>`, no external assets.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Firstname Lastname — Resume</title>
<style>
  @page { size: A4; margin: 16mm 18mm; }        /* Letter for US targets: size: letter */
  * { box-sizing: border-box; }
  body { font: 10.5pt/1.35 Helvetica, Arial, sans-serif; color: #111; margin: 0; }
  h1 { font-size: 17pt; margin: 0 0 2pt; }
  .contact { font-size: 9.5pt; margin: 0 0 10pt; }
  .contact a { color: #111; text-decoration: none; }
  h2 { font-size: 11pt; text-transform: uppercase; letter-spacing: 0;   /* real words, never letter-spaced */
       border-bottom: 1pt solid #333; padding-bottom: 2pt; margin: 12pt 0 6pt; }
  .role { display: flex; justify-content: space-between; font-weight: bold; margin-top: 7pt; }
  .role .dates { font-weight: normal; white-space: nowrap; }
  .org { font-style: italic; }
  ul { margin: 3pt 0 0; padding-left: 14pt; }
  li { margin-bottom: 2.5pt; }
  p { margin: 4pt 0; }
</style>
</head>
<body>
  <h1>Firstname Lastname</h1>
  <p class="contact">City, Country · email@example.com · +00 000 000 0000 ·
     linkedin.com/in/handle · github.com/handle · site.dev</p>
  <!-- sections: Summary, Experience, Projects, Skills, Education, Certifications -->
</body>
</html>
```

Safe adjustment ranges (for page-fit or taste, nothing else): font 10–11pt, line-height 1.25–1.45, page margin 14–20mm, one accent color on `h2`/links if asked (keep text near-black). The `.role` flexbox is safe: it renders as one line of plain text in reading order.

## Render routes (try in this order)

Detect with `command -v <tool>`; use the first hit.

1. **WeasyPrint** — best CSS fidelity for print:
   `weasyprint resume.html Firstname_Lastname_Resume.pdf`
2. **pandoc** (with a PDF engine present):
   `pandoc resume.html -o Firstname_Lastname_Resume.pdf --pdf-engine=weasyprint` (or `wkhtmltopdf`)
3. **Headless Chromium/Chrome**:
   `chromium --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=Firstname_Lastname_Resume.pdf resume.html` (binary may be `google-chrome` / `chromium-browser`)
4. **LibreOffice**:
   `libreoffice --headless --convert-to pdf resume.html --outdir .`

**DOCX** (many portals want Word): `pandoc resume.md -o Firstname_Lastname_Resume.docx` — pandoc's default docx styling is plain and single-column, which is exactly right. Tell the candidate to open it once and eyeball it before uploading.

**Nothing installed?** Offer `pip install weasyprint` (or the distro package), or the manual fallback: open the Markdown, paste into Google Docs / Word, apply single-column formatting per the resume blueprint, export as PDF. Never render by converting to an image.

## Verification commands

```bash
pdftotext Firstname_Lastname_Resume.pdf - | head -50     # text layer, reading order
python3 -c "import fitz,sys; d=fitz.open(sys.argv[1]); print(d.page_count)" Firstname_Lastname_Resume.pdf
```

Check in the extracted text: name + email on top, every section heading present and in order, a spot-check of 2–3 bullets, URLs visible as text. If `pdftotext` is missing, use PyMuPDF (`page.get_text()`) for both checks.

Fail → fix → re-render. Common failures: page break orphaning a heading (tighten margins or move a section), Unicode bullets rendering as boxes (use plain `•` or `-`), a too-long line of links wrapping badly in the contact block (split into two lines).
