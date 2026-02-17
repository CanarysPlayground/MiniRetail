---
name: cloud.testcases.prompt
description: Describe when to use this prompt
---
You are the Cloud Orchestration Agent for MiniRetail.

Context:
- Use `instructions/requirements-architecture.md` and `instructions/standard.instructions.md`.

Task:
Generate or update the test suite for the MiniRetail API.

Requirements:
- Produce deterministic pytest tests using FastAPI TestClient
- If `tests/test_retail.py` exists, update it in-place (idempotent)
- Cover: products CRUD + cart add/list/remove + total calculation
- No mocks, no async

Output:
- The complete content for `tests/test_retail.py`
- A short "handoff note" describing what changed and how to run the tests

Handoff:
- Target: Test Agent or Maintainer
- Include: file path, diff summary (if any), run command `pytest -q`