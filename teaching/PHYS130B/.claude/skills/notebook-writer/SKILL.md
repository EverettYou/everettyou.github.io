# Skill: Notebook Writer

Safely write and edit Jupyter notebook (.ipynb) cells for the PHYS130B lecture notes project.

## When to Use

- Implementing new content (homework, discussion problems, prompts) into notebooks
- Fixing corrupted cells
- Restructuring notebook cell layout
- Any programmatic modification of .ipynb files

## Critical Rules

1. **NEVER** use `NotebookEdit` or `Edit` on .ipynb files
2. **ALWAYS** use Python `json.load`/`json.dump` via Bash
3. **ALWAYS** read the notebook before writing
4. **ALWAYS** validate after writing

## Workflow

### Step 1: Read the Target Notebook

```python
import json
with open(path) as f:
    nb = json.load(f)
print(f"Cells: {len(nb['cells'])}")
for i, c in enumerate(nb['cells']):
    preview = ''.join(c['source'])[:80]
    print(f"  [{i}] {c['cell_type']}: {preview}")
```

### Step 2: Prepare Content

Use the `text_to_source` helper to convert markdown text to proper source arrays:

```python
def text_to_source(text):
    """Convert markdown string to proper ipynb source array.
    Every line except the last gets a \\n terminator."""
    lines = text.split('\n')
    source = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            source.append(line + '\n')
        else:
            if line:
                source.append(line)
    return source
```

### Step 3: Modify the Notebook

```python
# Replace a cell's content
nb['cells'][CELL_INDEX]['source'] = text_to_source(new_content)

# Insert a new cell
new_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": text_to_source(content)
}
nb['cells'].insert(INDEX, new_cell)
```

### Step 4: Write Back

```python
with open(path, 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
```

### Step 5: Validate

Run the validation script from `.claude/scripts/validate_notebooks.py` on the modified file. Check for:
- Char-by-char corruption
- Missing `\n` terminators
- Collapsed content (lines >1000 chars)

## References

- `.claude/experience.md` — Full corruption patterns and fix recipes
- `.claude/design.md` — Cell structure specs
- `.claude/rules/notebook-editing.md` — Editing rules summary
