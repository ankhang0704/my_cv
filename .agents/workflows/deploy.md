# Workflow: Resume Deployment & Build Release

Use this workflow to compile, perform quality assurance, and publish the final CV output files cleanly.

---

## Workflow Steps

### Step 1: Pre-Build Verification
*   Before building, run the `ats-analyzer` skill to ensure the source code has a 100/100 or highly compatible score.
*   Ensure that all contact placeholders have been customized with the correct personal detail formats (no raw templates remaining).

### Step 2: PDF Compilation
*   Run the `latex-compiler` skill using the optimal local compilation engine:
    ```bash
    python .agents/skills/latex-compiler/compiler.py src/main.tex
    ```
*   Verify that `src/main.pdf` is successfully generated in the same directory.

### Step 3: Post-Build Cache Cleanup
*   Do not clutter the repository with LaTeX's heavy auxiliary logs.
*   The compiler skill automatically removes these, but if running manual tools, ensure all files matching these extensions are deleted:
    *   `.aux`, `.log`, `.out`, `.toc`, `.synctex.gz`, `.fls`, `.fdb_latexmk`.

### Step 4: Quality Review
*   Open the compiled `src/main.pdf` and check:
    *   **Page Constraints**: Does the content fit precisely on 1 page (or 2 pages if highly senior)? No trailing blank page or single-line spillover onto a new page is allowed.
    *   **Visual Balance**: Is the vertical spacing balanced across all sections?
    *   **Selectable Text**: Highlight some paragraphs to verify the text parses correctly without ligature corruption.
