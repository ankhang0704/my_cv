# AI Agents Workspace Workspace Configuration (AGENTS.md)

Welcome Agent! This workspace is fully configured for specialized, automated LaTeX CV editing, compilation, design customization, and ATS auditing. Use this manifest to load rules, trigger automated workflows, and call custom extended skills.

---

## 🤖 1. Workspace Agents

This project utilizes three specialized roles:
1.  **Visual Designer Agent**: Focuses on typographic proportions, custom primary/secondary HSL/HEX color mappings, and margin adjustments.
2.  **Content Writer Coach Agent**: Specializes in auditing accomplishment bullet points against Google's XYZ/STAR formulas and past-tense action vocabularies.
3.  **Latex Compilation & QA Agent**: Specializes in checking local compiler packages, building PDF artifacts, and cleaning temporary cache logs.

---

## 📜 2. Predefined Agent Rules

All operations must strictly adhere to the rule sheets defined in `.agents/rules/`:
*   **[global.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/rules/global.md)**: Universal code quality, path restrictions, and interactions standards.
*   **[security.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/rules/security.md)**: Strict parameters preventing PII leakage, raw credential commits, and unsafe macro executions during builds.
*   **[latex.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/rules/latex.md)**: Font selections, spacing parameters, structural naming constraints, and ATS compliance guidelines.

---

## 🔄 3. Automated Agent Workflows

When performing routine tasks, execute these step-by-step procedures:
*   **[bug-fixing.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/workflows/bug-fixing.md)**: Troubleshooting guidelines to solve compile warnings, unescaped characters, or layout conflicts.
*   **[deploy.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/workflows/deploy.md)**: Compilation flow, build Quality Assurance checklists, and auxiliary log cleanup.
*   **[review-code.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/workflows/review-code.md)**: Playbook for parsing and reviewing work experience bullet points.

---

## 🛠️ 4. Loaded AI Extension Skills

The following skills are fully implemented inside `.agents/skills/` and can be called directly from your terminal:

### 1. LaTeX Compiler Engine (`latex-compiler`)
*   *Purpose*: Compiles source files into high-quality PDFs and cleans up build caches.
*   *Manifest*: [latex-compiler/SKILL.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/skills/latex-compiler/SKILL.md)
*   *Execution*:
    ```bash
    python .agents/skills/latex-compiler/compiler.py src/main.tex
    ```

### 2. ATS Compliance Scanner (`ats-analyzer`)
*   *Purpose*: Performs structural audits for Applicant Tracking Systems.
*   *Manifest*: [ats-analyzer/SKILL.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/skills/ats-analyzer/SKILL.md)
*   *Execution*:
    ```bash
    python .agents/skills/ats-analyzer/ats_analyzer.py src/main.tex
    ```

### 3. Resume Content Coach (`content-coach`)
*   *Purpose*: Scores and suggestions rewrites for CV bullet points.
*   *Manifest*: [content-coach/SKILL.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/skills/content-coach/SKILL.md)
*   *Execution*:
    ```bash
    python .agents/skills/content-coach/content_coach.py src/main.tex
    ```
