# Rule: Safe Notebook Editing

These rules are mandatory for ANY edit to `.ipynb` files in this project.

## Banned Tools

- **NEVER use `NotebookEdit`** — it produces char-by-char corruption where each character becomes a separate array element.
- **NEVER use `Edit`** on ANY file — it triggers an "Always allow?" permission dialog on every invocation in Cowork mode, blocking autonomous operation. Denied in `settings.local.json`.
- **NEVER use `Write`** tool — same permission issue as `Edit`. Denied in `settings.local.json`.

All three tools are in the `deny` list. Agents that attempt to call them will be blocked.

## Required Method: Bash for ALL File Modifications

Every file write — `.ipynb`, `.md`, `.json`, `.py`, anything — must go through **Bash** using Python file I/O. This is the only tool that runs without permission prompts in Cowork mode.

**For `.ipynb` notebooks:**
```python
import json
with open(path) as f:
    nb = json.load(f)
nb['cells'][i]['source'] = new_source_list
with open(path, 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
```

**For `.md` / `.json` / `.py` / any text file:**
```python
# Create or overwrite
with open(path, 'w') as f:
    f.write(new_content)

# Find-and-replace
with open(path) as f:
    content = f.read()
content = content.replace(old_string, new_string)
with open(path, 'w') as f:
    f.write(content)
```

## Source Array Format

Each cell's `"source"` is a list of strings. Every line **except the last** must end with `\n`:

```python
def text_to_source(text):
    """Convert markdown string to proper ipynb source array."""
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

## Pre-edit Checklist

1. Always `Read` the notebook first — verify cell count and indices
2. Never assume cell indices — they may have shifted from prior edits
3. Back up or git commit before bulk changes

## Post-edit Checklist

1. Run `safe_edit.py validate` or the inline validation checks on every modified file
2. Verify no char-by-char corruption
3. Verify no missing `\n` terminators
4. Verify no collapsed content (lines >1000 chars)

## LaTeX in JSON

Do not split TeX commands across JSON strings in a way that produces `\n` (newline) inside commands like `\nabla`, `\nu`, `\partial`. The sequence `\n` in JSON is a newline character, not a backslash followed by `n`.
