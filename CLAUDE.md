# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is a learning/experimentation repo for walking through Claude Code's features end-to-end (`CLAUDE.md`, `settings.json`, `rules/`, `commands/`, `skills/`, `agents/`, `hooks/`, `.mcp.json`). See [roadmap.md](roadmap.md) for the full step-by-step plan; each step defines what to build, why, and how to verify it. When asked to "execute step N", follow that step's definition in roadmap.md.

## Commands

- Run all tests: `python3 -m pytest -v`
- Run a single test file: `python3 -m pytest tests/test_calculator.py -v`
- Run a single test: `python3 -m pytest tests/test_calculator.py::test_add -v`
- Install dependencies: `pip install -r requirements.txt`

## Architecture

- `src/calculator.py` — toy module with basic arithmetic functions.
- `tests/test_calculator.py` — pytest tests importing from `src.calculator` (imports are rooted at the repo root, so tests must be run from there).

The codebase itself is intentionally minimal — the real subject of this repo is the `.claude/` configuration being built up around it step by step, not the toy application logic.
