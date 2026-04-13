---
name: phys130b-notebook
description: Safe read/write and validation for PHYS130B Jupyter notebooks under notes_src. Use when editing, fixing, or restructuring any .ipynb.
---

# Skill: Notebook writer (PHYS130B)

Programmatic editing of `.ipynb` only—never `NotebookEdit` or `Edit`/`Write` on notebooks in Cowork.

## Activation (auto)

- Start of session: see **`.claude/README.md`** (feedback → progress → work).
- Any task that **modifies** `notes_src/**/*.ipynb` (content, structure, or metadata).
- Fixing issues from `feedback.md` / `progress.md` that require JSON cell edits.
- After another skill proposes changes—**this skill applies the patch** and runs validation.

## Non-goals

- Does **not** replace a physics or pedagogy pass—pair with `science-reviewer` or `lecture-content` when content changes.
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
5. **Read** before write; **validate** after write.

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

## Validation (after every write)

```bash
python3 .claude/skills/notebook-writer/scripts/safe_edit.py validate path/to.ipynb
```

For broader checks (structure, MyST, notation heuristics):

```bash
python3 .claude/scripts/validate_project.py --scope <chapter-or-file-stem>
```

Full list of checks: see former validate playbook—**corruption**, **cell counts/titles**, **`$$` blank lines**, **banned patterns** (`---`, nested `:::`, `plt.show()`, etc.), **notation hints** in math (script docstring).

Report results in a small table if many files: `| Notebook | Corruption | Structure | Other |`.

## Fix workflow (from feedback)

1. `json.load` the notebook; locate cell/line from the report.
2. Classify: char-by-char / missing `\n` / collapsed line / content violation of `rules/` (architecture, MyST, style).
3. Patch with `json.dump`; **validate**; update `progress.md` or annotate `feedback.md` when resolved.

## References

- `CLAUDE.md`, `.claude/README.md`, `rules/notebook-editing.md`, `rules/tooling-security.md`, `rules/validation.md`, `rules/troubleshooting-ipynb.md`
- **`_refs/`** (project root): Professor's original lecture notes. **Read the corresponding `_refs/` file before writing or rewriting any derivation or physics content.** See `CLAUDE.md` § "Reference materials" for the chapter-to-file mapping.
