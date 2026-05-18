# AI Skill: ATS Readability Scanner

This skill empowers the AI Agent to run structural static analyses on LaTeX resumes, reporting compliance and scoring the PDF text extractability out of 100.

---

## 📋 Skill Specification

*   **Skill Name**: ATS Readability Scanner
*   **Identifier**: `ats-analyzer`
*   **Version**: 1.0.0
*   **Runtime**: Python 3

### 🛠️ Input Parameters
*   `tex_file` (string, required): Path to the target LaTeX source code file (e.g. `src/main.tex`).

### 📤 Output Artifacts
*   `Audit Report` (stdout): A breakdown of passing checks and warnings.
*   `Compliance Score` (integer): A rated metric between 0 and 100 representing parsability.

---

## 🚀 Execution Standard Command
To execute this skill, run the Python analyzer script:
```bash
python .agents/skills/ats-analyzer/ats_analyzer.py [tex_file_path]
```

---

## 🛡️ Checks Performed
1.  **Section Headers Check**: Scans for standard wording (Experience, Education, Skills, Projects).
2.  **Layout Positioning Check**: Flags unsafe absolute coordinate packaging.
3.  **Grid Layout Check**: Detects complex nested tables or abuse of tabular structures for paragraph grids.
4.  **Graphic Check**: Identifies visual progress/skill level graphics.
5.  **Font Encoding Check**: Verifies inclusion of T1 fontenc to ensure ligature searchability.
