# Workflow: Resume Review & Content Polishing

Use this workflow to perform a deep editorial and grammatical check on your CV to maximize its persuasive impact.

---

## Workflow Steps

### Step 1: Content Extraction
*   Locate all `\resumeItem` bullet points in the source file `src/main.tex`.
*   Clean out the LaTeX control tags to get a raw string of text for each item.

### Step 2: Metric and Action Verb Audit
*   **Strong Action Verb Check**: Verify that the very first word of the bullet point is a high-impact past-tense action verb (e.g. *Optimized*, *Architected*, *Spearheaded*).
*   **Quantifiable Results Audit**: Scan each bullet point for numeric figures (percentages, dollar values, user counts, latency drops).
    *   *Rule*: A high-quality resume must have at least 70% of its experience bullets quantified with real-world metrics.
*   **Pronoun Detection**: Search for forbidden subjective pronouns ("I", "my", "our"). Flag them for immediate removal.

### Step 3: Readability & Conciseness Audit
*   **Length Check**: Measure the word count of each bullet point:
    *   `10 - 30 words`: Perfect.
    *   `< 8 words`: Too short (vague description).
    *   `> 35 words`: Too long (loses recruiter engagement).
*   **ATS Check**: Run the `ats-analyzer` skill to double-check that no tabular hacks, drawing coordinates, or structural textboxes are blocking text readers.

### Step 4: Write recommendations
*   Deliver a detailed, bullet-by-bullet report card highlighting:
    1.  The original text.
    2.  An active rating (e.g., `Strong` or `Polishing recommended`).
    3.  Precise, step-by-step instructions on how to rewrite the line to fulfill the STAR/XYZ standards.
