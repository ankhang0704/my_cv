# Global Workspace Rules & Quality Standards

Welcome Agent! This document acts as the universal standard for all interactions, edits, and operations in this workspace. Adhere to these guidelines strictly.

---

## 1. Core Architecture Principles
*   **Source Folder First**: All primary resume source documents, template codes, and content additions must reside inside the `src/` directory. The main entrypoint is `src/my_cv.tex`.
*   **Deterministic Workflows**: Follow workflows specified in `.agents/workflows/` step-by-step. Do not take shortcuts.
*   **Modular Extension Skills**: When writing helper tools or script engines, implement them under `.agents/skills/<skill-name>/` with a clean `SKILL.md` file describing the interface.

## 2. LaTeX Coding Standards
*   **Preamble Integrity**: Never modify core layout packages or defined layout macros in `src/my_cv.tex` unless specifically instructed to run a redesign workflow.
*   **Content Isolation**: Work experience and achievements are formatted strictly within `\resumeItem{...}` list blocks inside standard section environments.
*   **Clean Compiles**: Maintain a workspace free of auxiliary cache files. Any compile workflow must conclude with a temporary cache cleanup.

## 3. General AI Interaction Policies
*   **Read Before Writing**: Before editing any LaTeX code, run the local analysis workflows to detect potential formatting collisions.
*   **Non-Destructive Modifications**: When editing LaTeX markup, preserve existing comment strings and document configuration values.
*   **Maintain clickable links**: In reports, always refer to local files using active, absolute markdown links of the form `[filename](file:///absolute/path/to/file)`.
