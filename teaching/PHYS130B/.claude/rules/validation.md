# Rule: Validation (agents)

**Policy:** `.claude/settings.json` does **not** define a `build_command` for agents. Full Jupyter Book builds are **human-only** (local machine); sandboxes often error or block them.

## What agents run

| Situation | Command |
|-----------|---------|
| After editing one notebook | `python3 .claude/skills/notebook-writer/scripts/safe_edit.py validate <path/to.ipynb>` |
| After batch edits or before claiming “clean” | `python3 .claude/scripts/validate_project.py` |
| One chapter | `python3 .claude/scripts/validate_project.py --scope ch3` |
| One file by stem | `python3 .claude/scripts/validate_project.py --scope 6-1-1-mixed-states` |
| Rules/docs consistency only | `python3 .claude/scripts/validate_project.py --docs-only` |
| Homework-format report only (subsection cell 3) | `python3 .claude/scripts/audit_homework_format.py` |

`validate_project.py` checks corruption patterns, cell structure, MyST `$$` spacing, banned patterns, notation heuristics, and **homework problem lines** in subsection notebooks (`content-style.md` § Homework Design — shared logic in `scripts/homework_format.py`).

## What agents do **not** run for validation

- **`./build.sh`**, **`jupyter-book build`**, or any step that requires a full local book build inside the agent environment.
- Do **not** treat “build succeeded” as proof of correctness.

## Humans (local development only)

For rendered HTML and Sphinx/MyST errors that only appear in a full build:

- From repo `PHYS130B/`: `./build.sh`
- Stale cache: removing `notes_src/_build` before rebuild avoids confusing incremental artifacts (human workflow; not required of agents).

## After validation failures

1. Fix corruption or structure per `rules/troubleshooting-ipynb.md` and `rules/notebook-editing.md`.
2. Re-run scoped `validate_project.py` or `safe_edit.py validate`.
3. If unsure, **stop** after repair and report—avoid chained edits that amplify mistakes.
