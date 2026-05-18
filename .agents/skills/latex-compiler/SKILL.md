# AI Skill: LaTeX Compiler Engine

This skill equips the AI Agent with the capability to automatically compile LaTeX source documents into premium PDF files while managing the cache lifecycle.

---

## 📋 Skill Specification

*   **Skill Name**: LaTeX Compiler Engine
*   **Identifier**: `latex-compiler`
*   **Version**: 1.0.0
*   **Runtime**: Python 3 / Local LaTeX Engine (`tectonic`, `pdflatex`, `xelatex`, `lualatex`, or `latexmk`)

### 🛠️ Input Parameters
The skill takes a structured file path argument:
*   `tex_file` (string, required): Absolute or relative path to the primary LaTeX source document (e.g. `src/main.tex`).
*   `--engine` (string, optional): Specific compiler override.
*   `--no-clean` (boolean, optional): Flag to retain intermediate cache logs.

### 📤 Output Artifacts
*   `[base_name].pdf` (binary PDF): A rendered, high-quality, and ATS-parsable document.
*   `Console Logs` (stdout): Status updates and compiler execution details.

---

## 🚀 Execution Standard Command
To execute this skill, run the Python compiler script:
```bash
python .agents/skills/latex-compiler/compiler.py [tex_file_path]
```

---

## 🛡️ Safety Constraints
*   Ensure that the target file resides strictly within the workspace.
*   Do not allow any compilation commands that execute external shell hooks (preventing unsafe macros like `\write18`).
