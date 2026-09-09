---
description: Review pending changes against this repo's code review checklist
allowed-tools: Bash(git diff:*), Bash(git status:*), Bash(git log:*)
---

Review the pending changes:

!`git status`

!`git diff`

The `git status` output above may list untracked (`??`) files or directories — `git diff` does not show their content. Read every untracked file yourself before reviewing, so new files aren't skipped.

Check the changes against this checklist:
1. **Correctness** — obvious bugs, off-by-one errors, unhandled edge cases.
2. **Convention compliance** — does it follow `.claude/rules/code-style.md` and `.claude/rules/testing.md`?
3. **Security** — hardcoded secrets, command/SQL injection, unsafe deserialization.
4. **Test coverage** — does new/changed behavior have a corresponding test?

Output format: group findings by category above, most severe first. For each finding give `file:line` and a one-line fix suggestion. If a category has no issues, state "no issues found" for it — don't skip it silently.
