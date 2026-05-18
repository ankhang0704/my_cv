# Workflow: LaTeX Compile Bug-Fixing and Troubleshooting

Follow this systematic procedure when resolving LaTeX compilation errors or visual layout rendering bugs.

---

## Workflow Steps

```mermaid
graph TD
    A[Identify Compilation Failure] --> B[Parse Log File / .log]
    B --> C{Determine Bug Type}
    C -->|Unescaped Special Char| D[Locate & Escape Char e.g., \% \&]
    C -->|Missing Package| E[Declare Package in Preamble]
    C -->|Brace Mismatch| F[Find Mismatched { } and Rebalance]
    C -->|Undefined Command| G[Check Macro Definition / Typos]
    D --> H[Run Compiler Skill]
    E --> H
    F --> H
    G --> H
    H --> I{Success?}
    I -->|Yes| J[Cleanup Temp Cache & Complete]
    I -->|No| B
```

### Step 1: Parse the Log Output
*   Read the compiler terminal output or search the generated `.log` file.
*   Locate the specific line number where the error occurred and the error message (e.g., `Undefined control sequence`, `Missing } inserted`, or `Paragraph ended before \resumeJob was complete`).

### Step 2: Categorize and Fix the Bug
1.  **Unescaped Special Characters (Most Common)**:
    *   *Check*: Did you write raw `%`, `&`, `_`, `$`, `#` in your bullet points?
    *   *Fix*: Escape them immediately: `\%`, `\&`, `\_`, `\$`, `\#`.
2.  **Mismatched Braces/Environments**:
    *   *Check*: Did you open a `\begin{itemize}` and forget to close it with `\end{itemize}`? Or miss a closing curly brace `}` inside a `\resumeItem`?
    *   *Fix*: Track and balance the braces or environment closures.
3.  **Missing Package Declarations**:
    *   *Check*: Are you using a modern icon command (like `\faLinkedin` from `fontawesome5`) or colors, but forgot to import the respective package in the preamble?
    *   *Fix*: Ensure `\usepackage{fontawesome5}` or `\usepackage{xcolor}` is declared at the top of the file.
4.  **Undefined Control Sequence**:
    *   *Check*: Did you typo a command name (e.g. `\resumItem` instead of `\resumeItem`)?
    *   *Fix*: Correct the spelling to match predefined commands.

### Step 3: Compile and Verify
*   Execute the `latex-compiler` skill to recompile the PDF.
*   If compiling succeeds, immediately run the temporary file cleanup workflow.
*   If compiling fails, repeat from **Step 1**.
