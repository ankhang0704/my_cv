# Workspace Security and Privacy Rules

Security, privacy, and data protection are critical—especially when designing CVs that contain personal contact details. These security guidelines must be enforced at all times.

---

## 1. Credentials and Secret Protection
*   **No API Keys/Secrets**: Never hardcode API keys, credentials, or tokens anywhere in the codebase.
*   **Environment Variables**: If any skill requires an LLM call or external API (e.g. advanced AI parsing), read the credentials strictly from environment variables or a local, git-ignored `.env` file.
*   **Strict Git-Ignore**: The `.env` file and all auxiliary LaTeX cache logs must be included in `.gitignore`.

## 2. Personal Data Protection (PII)
*   **Placeholder Usage in Templates**: In public templates (under `templates/`), always use dummy placeholders (e.g., "Alex Rivers", "alex.rivers@email.com", "+1 (555) 019-2834") to protect candidate privacy.
*   **Explicit Candidate Consent**: Never export or upload resume PDF or LaTeX files to external API services without explicit permission from the developer.

## 3. Local Execution Safety
*   **No Destructive Script Executions**: Script skills (e.g., Python compilers) must only read and write inside the current workspace. Absolute paths outside the workspace must never be edited, deleted, or traversed.
*   **Sanitize Compiler Inputs**: Before compiling, check the LaTeX code for dangerous macro executions (such as `\write18` or `\shell-escape` commands) to prevent arbitrary shell commands from running during PDF compilation.
