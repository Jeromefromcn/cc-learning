---
name: commit-message
description: Use when the user asks to write, generate, or draft a commit message for this repo's staged or unstaged changes — produces a Conventional Commits-formatted message from `git diff`.
---

Generate a commit message for the pending changes in this repo, following Conventional Commits.

Steps:
1. Run `git status` and `git diff` (and `git diff --staged` if there are staged changes) to see what changed.
2. Pick a type: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `style`, `perf`. If changes span unrelated concerns, say so and suggest splitting into separate commits instead of picking one type.
3. Write a subject line: `<type>(<scope>): <short imperative summary>`, under ~72 chars, no trailing period. `<scope>` is optional — omit it if the change isn't scoped to one clear area.
4. Add a body only if the "why" isn't obvious from the subject — explain motivation/context, not a restatement of the diff.
5. Output just the commit message text (ready to pass to `git commit -m`), not a wrapped explanation of what you did.
