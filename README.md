# 🚀 Premium LaTeX CV Agent Workspace

Welcome to your **Premium LaTeX CV Agent Workspace**! This is a state-of-the-art developer environment designed to help you craft, compile, style, and audit high-impact, professional, and **ATS-friendly resumes** in LaTeX with automated AI-like agent assistance.

This project is fully structured with a standardized agent workspace layout, incorporating passive rules, operational workflows, and active extended skills.

---

## 📂 Project Directory Structure

```text
my_cv/
├── .agents/                      # Smart Agent Configuration Root [📂]
│   ├── rules/                    # 1. Passive Rule Guides [📂]
│   │   ├── global.md             # Standard engineering guidelines
│   │   ├── security.md           # Privacy & compile macro safety rules
│   │   └── latex.md              # Typographic & ATS-readability standards
│   │
│   ├── workflows/                # 2. Operational Workflows [📂]
│   │   ├── bug-fixing.md         # Tracing & solving compile errors
│   │   ├── deploy.md             # Compilation & Visual QA checklist
│   │   └── review-code.md        # Content review (STAR/XYZ validation)
│   │
│   ├── skills/                   # 3. Active Extended Skills [📂]
│   │   ├── latex-compiler/       # Skill: LaTeX Compiling Engine
│   │   │   ├── SKILL.md          # Skill manifest config
│   │   │   └── compiler.py       # Compiling & auxiliary cleanup script
│   │   ├── ats-analyzer/         # Skill: ATS Readability Scanner
│   │   │   ├── SKILL.md          # Skill manifest config
│   │   │   └── ats_analyzer.py   # Static structural audit script
│   │   └── content-coach/        # Skill: Resume Content Coach
│   │       ├── SKILL.md          # Skill manifest config
│   │       └── content_coach.py  # Achievement metrics scoring script
│   │
│   └── orchestrator.py           # Master CLI Orchestrator Script [📄]
│
├── AGENTS.md                     # Flat Agent Configuration Manifest [📄]
├── src/                          # Primary Resume Source Directory [📂]
│   └── main.tex                  # Premium LaTeX CV Source Document [📄]
└── README.md                     # General Workspace Documentation [📄]
```

---

## 🛠️ Requirements & Setup

To use the automated compiling tool, you will need a LaTeX engine registered in your system's PATH.

### 1. Install LaTeX Engine (Choose One):
*   **Tectonic (Recommended - Super Light & Automatic)**: Downloads only the packages you actually use, leaving a tiny system footprint.
    *   *Windows (PowerShell)*: `winget install Tectonic.Tectonic`
*   **MikTeX (Standard)**: Easy graphical installer. Download from [MikTeX Downloads](https://miktex.org/download).
*   **TeX Live**: Complete, robust distribution.

### 2. Python Setup:
The agents run on standard Python 3 (no third-party dependencies are required for the base CLI, keeping it extremely light and fast!).

---

## 🎮 How to Operate Your Workspace Orchestrator

All skills are tied together under the unified master command center: `python .agents/orchestrator.py`.

### 1. Compile LaTeX to PDF
Compiles your resume into a gorgeous PDF using the best available local engine and cleans up cluttered auxiliary files (`.aux`, `.log`, `.out`) instantly:
```bash
python .agents/orchestrator.py compile
```
*Your compiled output will be generated as `src/main.pdf`.*

### 2. Audit ATS Compliance
Scan your LaTeX code for hidden structural blocks that might trigger parser warnings in corporate application portals:
```bash
python .agents/orchestrator.py analyze-ats
```
Generates a detailed scorecard rating your CV's parsing friendliness out of 100 with clear improvement suggestions.

### 3. Content Polishing Coach
Run the **Content Writer Coach Agent** to analyze your resume achievements against the high-impact **STAR/XYZ formula**:
```bash
python .agents/orchestrator.py polish-content
```
This tool checks every single bullet point (`\resumeItem`) and highlights weak start words, missing numeric metrics, forbidden personal pronouns ("I", "my"), and bad line lengths.

---

## 💡 Quick Tips for Designing Your Dream CV
1.  **Read the Rules**: Before editing, review [.agents/rules/latex.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/rules/latex.md) and [.agents/rules/global.md](file:///c:/Users/Admin/Documents/GitHub/my_cv/.agents/rules/global.md) for maximum results.
2.  **Action + Metric = Interview**: Every experience line should prove the impact you made with a clear percentage, dollar amount, or time-saving figure.
3.  **Deploy cleanly**: Use the orchestrator to compile. It automatically cleans up intermediate logs so your Git repository remains clean.
