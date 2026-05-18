# AI Skill: Resume Content Coach

This skill equips the AI Agent to run grammatical and quality reviews on the resume experience descriptions, helping you write powerful STAR/XYZ accomplishments.

---

## 📋 Skill Specification

*   **Skill Name**: Resume Content Coach
*   **Identifier**: `content-coach`
*   **Version**: 1.0.0
*   **Runtime**: Python 3

### 🛠️ Input Parameters
*   `tex_file` (string, required): Path to the target LaTeX source file (e.g. `src/main.tex`).

### 📤 Output Artifacts
*   `Audit Report` (stdout): Comprehensive feedback grading each experience line, alerting you to weak verbs, pronoun slips, and lack of metrics.

---

## 🚀 Execution Standard Command
To execute this skill, run the Python coach script:
```bash
python .agents/skills/content-coach/content_coach.py [tex_file_path]
```
