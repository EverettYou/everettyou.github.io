# Homework tooling (PHYS130B)

**Who runs these:** **`notebook-writer`** sessions only (they **mutate** `.ipynb`). Designers **audit** and specify; see **`../SKILL.md`**.

| Script | When to use |
|--------|-------------|
| **`homework_format.py`** | Library: homework line checks (no CLI). Imported by **`../../../scripts/validate_project.py`** and **`audit_homework_format.py`**. |
| **`audit_homework_format.py`** | Homework-only report across subsection notebooks (cell 3). After bulk homework edits or phase **C** homework pass. |
| **`check_duplicate_homework.py`** | Find near-duplicate problem bodies across notebooks (post-refactor or periodic audit). Optional `--threshold`. |
| **`fix_homework_duplicate_titles.py`** | One-off repair: `**N. Title.** Title.**` glitches and similar broken homework title lines. |

**Law:** `rules/content-style.md` § Homework Design, `rules/validation.md` for validator order.
