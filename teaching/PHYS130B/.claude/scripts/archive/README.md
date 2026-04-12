# Archived one-off scripts

These were used for past bulk migrations or repairs. **Do not run** unless you are deliberately reproducing history.

| Script | Former role |
|--------|----------------|
| `validate_notebooks.py` | Early validator; superseded by `../validate_project.py` |
| `swap_6_1_6_2.py` | Chapter 6 section swap helper |
| `fix_corrupted_cells.py` | Batch corruption repair |
| `fix_and_add_admonitions.py` | Admonition migration |
| `format_notebooks.py` | Formatting pass |
| `update_section_parents.py` | Section parent structure update |
| `unify_section_parents.py` | Section parent unification |

Active tooling: `../validate_project.py` and `../../skills/notebook-writer/scripts/safe_edit.py`.
