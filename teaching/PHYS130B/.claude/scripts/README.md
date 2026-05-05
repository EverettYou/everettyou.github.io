# `.claude/scripts/` (repo-wide)

| Script | Role | Invoked from |
|--------|------|----------------|
| **`validate_project.py`** | Unified notebook + rules doc checks (`rules/validation.md`). Imports **`homework_format`** from **`../skills/homework-designer/scripts/`**. | Every batch edit; **`notebook-writer`** after saves. |
| **`fix_display_math_blocks.py`** | Normalize `$$` blank-line layout (uses helpers from `validate_project.py`). | Mechanical MyST repair; **`notebook-writer`**. |

**Skill-hosted scripts** (when / why documented in each skill’s `SKILL.md` + `scripts/README.md`):

- **`../skills/homework-designer/scripts/`** — homework audit, duplicates, title fixes, shared `homework_format` library.
- **`../skills/summary-designer/scripts/`** — See Also bootstrap, curated apply, dembold, Summary dedupe.

**Archive:** `archive/` — historical one-offs; prefer `validate_project.py` + skill scripts unless a ticket names an archive tool.
