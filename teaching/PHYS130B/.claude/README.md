# PHYS130B `.claude` — agent session guide

Read this at **the start of each scheduled or manual session** (after `CLAUDE.md`).

## 1. Ingest priorities

1. **`feedback.md`** (project root) — professor corrections and requests. **Highest priority.** Address open items before optional work.
2. **`progress.md`** (project root) — pending tasks, issues, and work order. Pick the next actionable item (or continue “In progress”).

## 2. Do the job

- Follow **`CLAUDE.md`** (constitution), **`rules/`** (constraints), and **`skills/`** (workflows).
- After notebook edits, validate per **`rules/validation.md`** only (`validate_project.py` / `safe_edit.py validate`).
- **Never** run **`./build.sh`** or **`jupyter-book build`** in an agent session—they error or are disallowed in typical sandboxes.
- When you finish something: update **`progress.md`** (mark done, date, short summary) and, if the item came from **`feedback.md`**, mark it **DONE** there with date.

## 3. If nothing is assigned

**Propose** concrete maintenance work that fits **`rules/maintenance-scope.md`** (e.g. one notebook: clarity, alignment, notation, structure).

- **Small / well-scoped** (single file, clear fix): **do it now**, then validate and update **`progress.md`**.
- **Large / risky** (TOC moves, renames, multi-chapter refactors, ambiguous physics): **do not start blindly** — add a **Pending** (or **Issues**) entry to **`progress.md`** with enough detail for the **next** session (or for a human to approve).

## 4. Read order (reference)

| Order | Doc |
|-------|-----|
| 1 | `CLAUDE.md` |
| 2 | This `README.md` |
| 3 | `feedback.md` → `progress.md` |
| 4 | Relevant `rules/*.md` and `skills/*/SKILL.md` for the task |

Teaching philosophy and authoring live in **`rules/teaching-philosophy.md`**, **`rules/notebook-architecture.md`**, **`rules/myst-references.md`**, **`rules/prompt-templates.md`** (not a monolithic `design.md`).
