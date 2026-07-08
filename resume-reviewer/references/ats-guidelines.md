# ATS audit checklist

Walk every item. For each fail, name the exact offending element (heading, line, or section) so the fix is actionable. ATS parsers extract raw text in reading order — anything that breaks text extraction or section detection loses content silently.

## 1. Parse safety (can a machine read it at all?)

- [ ] Single-column layout (multi-column reads out of order in many parsers)
- [ ] No tables or text boxes carrying content (headers of tables often get separated from cells)
- [ ] No content in images, icons, charts, or skill-level graphics (bars/stars) — icons for phone/email are fine only if the text is also present
- [ ] No content in the PDF header/footer regions (some parsers drop them) — contact info must be in the body
- [ ] **No letter-spaced or stylized headings** (e.g. "E X P E R I E N C E") — parsers see them as gibberish, not section markers
- [ ] Standard fonts (system/web-safe); text is selectable in the PDF (not scanned/flattened)
- [ ] Exported as text-based PDF, not an image export from a design tool
- [ ] URLs visible as text, not only behind generic anchor text like "Project Link" (plain-text extraction drops annotation-layer links)

## 2. Section conventions (does the parser find the right sections?)

- [ ] Standard heading names: Summary, Experience (or Work Experience), Projects, Education, Skills, Awards, Certifications
- [ ] Reverse-chronological order within Experience and Education
- [ ] One clear job title line per role: Title, Company, Location, Dates — consistent format across roles
- [ ] Contact block at top: full name, email, phone, city/country, LinkedIn URL, GitHub URL, portfolio URL — as plain text
- [ ] Email address is correct and professional (typos here are fatal and surprisingly common)

## 3. Content conventions

- [ ] Consistent date format everywhere, `MMM YYYY – MMM YYYY` (or `Present`); no bare years mixed with month-years
- [ ] No unexplained gaps in date logic (overlaps are fine if real, e.g. part-time + study)
- [ ] 1 page (junior) / max 2 pages; no orphaned single lines on page 2
- [ ] Bullets start with action verbs; no first-person pronouns
- [ ] No duplicated content across sections (same project in Projects and Experience with identical bullets)
- [ ] Bullets factually match the linked evidence (a project's CV description must match what its repo/demo actually shows; watch for descriptions swapped between projects)
- [ ] Skills listed honestly — no "expert" claims contradicted by experience level; skills grouped (Languages / Frameworks / Tools)
- [ ] Spelling and capitalization of technology names exact: JavaScript, TypeScript, Node.js, PostgreSQL, MongoDB, React (ATS keyword match can be case/spelling sensitive)
- [ ] File name professional: `Firstname_Lastname_CV.pdf` (no versions like "final_v3")
- [ ] Every project has a working link (cross-reference Phase 2 link verification)

## 4. JD keyword matching (only when a job description is provided)

1. Extract from the JD: required hard skills, nice-to-have skills, the exact job title, seniority signals, and domain terms.
2. For each required hard skill, check the CV for an exact-term match (not a synonym — parsers match strings). Record: present / present-but-buried (only in a project bullet, not in Skills) / absent.
3. Title alignment: does the CV's summary or most recent role title echo the JD title where honest (e.g. "Software Engineer" vs "Full-Stack Developer")?
4. Report a gap table: JD term → status → where to add it honestly (or "do not add — no real experience").
5. Never recommend adding a keyword the candidate has no genuine experience with; recommend the closest honest phrasing instead.
