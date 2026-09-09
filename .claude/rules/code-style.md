---
paths:
  - "src/**/*.py"
---

## Code Style

- Function and variable names use `snake_case`.
- Keep functions single-purpose; don't add input validation for cases that can't occur (e.g. type-checking arguments in a small internal module).
- Don't write comments that restate what the code does. Only comment on the *why* when it's non-obvious (a workaround, an invariant, a subtle edge case).
- Raise built-in exception types (`ValueError`, `TypeError`, etc.) with a short, specific message rather than inventing custom exception classes for a module this small.
