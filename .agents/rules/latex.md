---
trigger: always_on
---

# Domain-Specific Rules: LaTeX CV and ATS Compatibility

This document outlines the strict engineering and compilation guidelines required to keep the LaTeX CV files clean, readable by humans, and perfectly parsable by corporate Applicant Tracking Systems (ATS).

---

## 1. Visual Geometry & Margins
*   **Uniform Borders**: Maintain uniform page margins between `0.5in` (compact) and `0.75in` (spacious). Standard configuration is `0.6in`.
*   **Pristine Section Lines**: Separate major sections with modern horizontal lines (`\titlerule`) at `0.8pt` thick.
*   **Proportional Headings**:
    *   Full Name: `\Huge\bfseries`
    *   Job Title Sub-header: `\small\bfseries\scshape`
    *   Section Titles: `\large\bfseries\scshape`
    *   Body Text: `\small` (base font scale `10pt` or `11pt`)

## 2. Text Searchability & ATS Parsing Guidelines
*   **Single-Column Focus**: Prefer single-column layouts for chronological work experience to prevent parsers from reading across parallel columns.
*   **Searchable PDF Encoding**:
    *   Always declare `\usepackage[T1]{fontenc}` in the preamble.
    *   Ensure all text in the output PDF is copy-pasteable without special symbol replacements.
*   **Standard Naming Conventions**: Use corporate-friendly section headers:
    *   `Work Experience` or `Professional Experience`
    *   `Education`
    *   `Skills` or `Technical Skills`
    *   `Projects`
*   **Elements to Ban**:
    *   No graphical skill progress bars (unparsable by ATS).
    *   No icons used as the sole labels for contact details (always place text besides icons).
    *   No nested tables or tables used as grids for bullet points.

## 3. Predefined Styling Commands
To decouple layout presentation from resume content, always use predefined custom commands:
*   `\resumeHeader{Name}{Title}{Email}{Phone}{LinkedIn}{GitHub}`: ATS-friendly title block.
*   `\resumeJob{Title}{Company}{Date}{Location}`: Structured job heading row.
*   `\resumeEducation{School}{Degree}{Date}{Location}`: Standardized education row.
*   `\resumeProject{Name}{TechStack}{Date}`: Clean project heading row.
*   `\resumeItem{Accomplishment}`: Single bullet point item with controlled vertical separation.
*   `\resumeSkillGroup{Category}{SkillsList}`: Clean skills listing line.
