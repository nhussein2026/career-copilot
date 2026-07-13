# Resume Build Recipe — ATS-Safe Professional Resume Spec

The canonical formatting + output specification for every resume this suite produces. `resume-builder` writes content to this structure; `resume-renderer` produces the `.docx` master and the PDF exported from it to these settings. Content rules here defer to `resume-blueprint.md` where they overlap; **this file governs formatting, section order, and output.**

---

## 1. Document Settings

| Setting | Value |
|---|---|
| Page size | US Letter (8.5" × 11") default — use **A4 for EU/TR applications** when the target market expects it |
| Margins | Top/Bottom: 0.5" · Left/Right: 0.6" |
| Font | Calibri (fallbacks: Arial, Helvetica; Carlito is a metric-compatible Calibri substitute for rendering — never decorative fonts) |
| Body text size | 10 pt |
| Name | 18 pt, bold, ALL CAPS, centered |
| Tagline | 11 pt, bold, accent color |
| Section heading | 11 pt, bold, ALL CAPS, accent color, with a thin accent bottom border |
| Line spacing | 1.05 |
| Accent color | `#1F4E79` (dark professional blue) — headings and tagline ONLY |
| Body color | `#212121` · Secondary/dates: `#555555` |
| Layout | Single column. No tables for layout, no text boxes, no columns, no images, no icons, no graphics |

## 2. Structure & Section Order

1. **Header** — Name, tagline, contact line(s), centered
2. **Professional Summary** — 3–4 sentences, one paragraph
3. **Technical Skills** — grouped by category, one line each
4. **Professional Experience** — reverse chronological
5. **Projects** — reverse chronological
6. **Education**
7. **Certifications**
8. **Volunteering**
9. **Languages** — single line, separated by ` | `

Include only sections the candidate has real content for; keep this order for the ones present.

## 3. Header Rules

- Line 1: `FULL NAME` (caps, bold, 18 pt, centered)
- Line 2: `Job Title | Specialty` (e.g., "Software Engineer | Full-Stack Web Developer")
- Line 3: `City, Country | +XX XXX XXX XXXX | email@domain.com`
- Line 4: `linkedin.com/in/handle | github.com/handle | portfolio-domain.com`
- All links: real clickable hyperlinks, but the **visible text is the readable URL itself** (no "click here", no hidden URLs) — survives printing and ATS parsing.
- Phone in international format; email hyperlinked as `mailto:`.

## 4. Section Heading Style

ALL CAPS, bold, accent color, thin accent bottom border (horizontal rule). ~10 pt before, ~4 pt after.

## 5. Entry Format (Experience / Education / Certifications / Volunteering)

```
**Job Title** | Company | City, Country            [right tab] Mon YYYY – Mon YYYY
• Bullet 1
• Bullet 2
```
- Dates right-aligned via a **right tab stop** (never spaces), `Mon YYYY – Mon YYYY`, en dash (–), "Present" for current roles.
- 2–4 bullets per entry; the most recent role gets the most bullets.

## 6. Project Entry Format

```
**Project Name — Short Descriptor** | tech stack (italic) | visible-link.com     [right tab] Mon YYYY
• What it is / what was built
• Key technical feature implemented
• Impact or quality focus
```
- Every project has a **real, verified link** (live site preferred, else GitHub). Never write "Project Link" placeholder text; omit the link rather than fake it.

## 7. Skills Section Format

One line per category, label bold, canonical spellings (ATS matches exact strings):

```
Languages: JavaScript (ES6+), TypeScript, Java, SQL
Frontend: React.js, Astro.js, HTML5, CSS3, Tailwind CSS
Backend: Node.js, Express.js, RESTful API Design & Integration
Databases: MongoDB, PostgreSQL, MySQL
Tools: Git, GitHub, API Testing, Debugging, Docker (fundamentals)
Practices: Component-based development, code reviews, documentation
```
Canonical spellings: Node.js (not Nodejs), React.js, MongoDB, MySQL, PostgreSQL, TypeScript, GitHub, Tailwind CSS.

## 8. Writing Rules (Content)

- **Summary:** lead with identity + strongest evidence ("Software Engineer with hands-on production experience…"). Never "motivated to learn", "seeking opportunity", or junior-sounding filler — state capabilities as facts.
- **Bullets:** strong action verb first (Developed, Built, Refactored, Implemented, Integrated, Delivered, Designed, Led). Present tense for the current role, past for previous. Each bullet = action + technology + purpose/outcome; add numbers only where truthful.
- No first person, no pronouns. No fabrication of metrics, links, titles, or seniority. 1–2 lines per bullet; cut adjectives before facts.

## 9. ATS Compliance Checklist

- [ ] Single column; no tables/text boxes/images/icons/columns
- [ ] Standard section names (§2)
- [ ] Real list bullets (list formatting, not typed "•" or emoji)
- [ ] Standard font, 10–11 pt body
- [ ] Consistent `Mon YYYY` dates everywhere
- [ ] File name `Firstname_Lastname_Resume.pdf` / `.docx`
- [ ] Selectable real text in the PDF (not scanned/image)
- [ ] Keywords mirror the target JD's exact terms (only where genuinely held)

## 10. Quality Control (run before delivery)

1. **Cross-check every project description against its tech stack** — a "Java, Swing, MySQL" project can't be a "responsive web layout"; a mismatch usually means swapped descriptions.
2. **Verify every link resolves** (`curl -sIL`) — repos exist, live sites load, handles correct.
3. **Scan for duplicated bullets** copied between entries.
4. **Tech-name spelling pass:** Node.js, Express.js, PostgreSQL, TypeScript, GitHub, Tailwind CSS.
5. **Punctuation pass:** no double periods, consistent terminal periods, en dashes in date ranges, colons after skill labels.
6. **Chronology pass:** reverse-chronological within each section.
7. **Render and visually inspect:** no orphaned headings at page bottoms, no overlapping date tabs, no widow bullets.
8. **Length:** 1 page ideal for <5 years; 2 pages maximum.

## 11. Output

- Deliver both `.docx` (editable master) and `.pdf` (exported **from** the docx, so both are identical).
- Render route: build the `.docx` (e.g. python-docx to these settings), then `libreoffice --headless --convert-to pdf <file>.docx`. Verify the PDF's text layer per `render-guide.md`.
