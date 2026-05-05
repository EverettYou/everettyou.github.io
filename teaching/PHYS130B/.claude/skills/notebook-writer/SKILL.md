---
name: phys130b-notebook
description: Safe read/write and validation for PHYS130B Jupyter notebooks under notes_src. Use when editing, fixing, or restructuring any .ipynb.
---

# Skill: Notebook writer (PHYS130B)

## Role in the stack

**Sole `.ipynb` implementation layer.** Apply patches from **`feedback.md`**, **`progress.md`**, or any **`\*-designer`** skill (proposed markdown + cell index / scope). **All `*-designer` skills only audit, review, plan, and propose**—they **never** run validator commands on notebooks. **Normative tables live in `rules/`**—this skill does not restate them; it implements specs that already cite those rules. When a designer cites **`TEMPLATES.md`**, treat that as the **format shell** to paste unless it conflicts with **`rules/`** (rules win).

**After every `.ipynb` save** (including implementing a designer proposal, ad hoc fixes, or bulk scripts): run validators per **`rules/validation.md`** in the **same** session before claiming the edit is done. No designer skill shares this responsibility.

Programmatic editing of `.ipynb` only—never `NotebookEdit` or `Edit`/`Write` on notebooks in Cowork.

## Activation (auto)

- Start of session: **`feedback.md`** (professor, if any open items) then **`.claude/README.md`** / **`progress.md`**.
- Any task that **modifies** `notes_src/**/*.ipynb` (content, structure, or metadata).
- Fixing issues from `feedback.md` / `progress.md` that require JSON cell edits.
- After a **designer** skill proposes concrete cell content—**this skill applies** the patch and **must** run validation (see § Validation).

## Bulk helpers (See Also / summaries)

Scripts under **`skills/summary-designer/scripts/`** and **`skills/homework-designer/scripts/`** (see each skill’s `SKILL.md` + `scripts/README.md`) **mutate** `.ipynb` files—run them only here, with the same Bash + Python + `text_to_source` discipline as manual edits.

## Non-goals

- Does **not** replace derivation QC or pedagogy **design**—pair with **`derivation-designer`**, **`lecture-designer`**, or other `*-designer` skills when content is non-trivial.
- Does **not** run `./build.sh` or `jupyter-book build` (`rules/validation.md`).

## Fallback / de-escalation

1. If validation reports corruption, **stop feature work**—repair using `rules/troubleshooting-ipynb.md`, re-validate, then continue.
2. If unsure about cell indices, **read** the notebook and print a cell summary before writing.
3. If a write might conflict with parallel edits, prefer **one notebook at a time** and re-read before save.

## Absolute rules

1. **NEVER** `NotebookEdit` on `.ipynb`.
2. **NEVER** `Edit`/`Write` on `.ipynb` in Cowork—use Bash + `json.load` / `json.dump`.
3. **`json.dump(nb, f, indent=1, ensure_ascii=False)`** always.
4. **`text_to_source`** for markdown strings—canonical implementation: `skills/notebook-writer/scripts/safe_edit.py` (same logic as `rules/notebook-editing.md`).
5. **Read** before write; **validate after every write** (mandatory—designers never run validators).

## Workflow

```python
import json

def text_to_source(text):
    lines = text.split('\n')
    source = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            source.append(line + '\n')
        else:
            if line:
                source.append(line)
    return source

with open(path) as f:
    nb = json.load(f)
# inspect len(nb['cells']), then:
nb['cells'][CELL_INDEX]['source'] = text_to_source(new_content)
with open(path, 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
```

## Validation (mandatory after every write)

**Who runs validators:** **only this skill** (or the same agent explicitly acting as notebook-writer after an edit). **`*-designer` skills do not** invoke `safe_edit.py validate` or `validate_project.py`.

**Commands and scopes:** **only** **`rules/validation.md`** (do not duplicate command tables here). Typical pattern: `safe_edit.py validate` on each file touched, then scoped `validate_project.py` when appropriate.

Report results in a small table if many files: `| Notebook | Corruption | Structure | Other |`.

## Fix workflow (from feedback)

1. `json.load` the notebook; locate cell/line from the report.
2. Classify: char-by-char / missing `\n` / collapsed line / content violation of `rules/` (architecture, MyST, style).
3. Patch with `json.dump`; **validate**; update `progress.md` or annotate `feedback.md` when resolved.

## References

- Content **specs** from `*-designer` skills in `.claude/skills/` (this skill implements those specs).
- `CLAUDE.md`, `.claude/README.md`, `rules/notebook-editing.md`, `rules/tooling-security.md`, `rules/validation.md`, `rules/troubleshooting-ipynb.md`
- **`_refs/`** (project root): Professor's original lecture notes. **Read the corresponding `_refs/` file before writing or rewriting any derivation or physics content.** See `CLAUDE.md` § "Reference materials" for the chapter-to-file mapping.
