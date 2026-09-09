---
paths:
  - "tests/**/*.py"
---

## Testing

- Test files are named `test_<module>.py`; test functions `test_<behavior>`.
- Every public function needs at least one happy-path test and one edge-case/error test.
- Assert on behavior (inputs/outputs, raised exceptions), not on internal implementation details.
- Use `pytest.raises` to assert exceptions rather than try/except blocks in tests.
