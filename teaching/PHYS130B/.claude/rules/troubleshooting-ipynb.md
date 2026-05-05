# Rule: Troubleshooting corrupted or broken notebooks

Detection: `validate_project.py`, `safe_edit.py validate`, and checks in `rules/notebook-editing.md`.

## Char-by-char recovery

When `source` became one character per string (often after bad tool use + newline “fixes”):

```python
chars = []
for s in src:
    if s == '\n':
        chars.append('\n')
    elif s.endswith('\n') and len(s) == 2:
        chars.append(s[0])
    else:
        chars.append(s)
full_text = ''.join(chars)
cell['source'] = text_to_source(full_text)  # define per notebook-editing.md / safe_edit.py
```

## Collapsed content recovery

When headings or admonitions are fused (lines ≫ 1000 chars):

```python
import re
text = ''.join(src)
text = re.sub(r'([^\n])(#{2,4}\s)', r'\1\n\n\2', text)
text = re.sub(r'([^\n])(:::\{)', r'\1\n\n\2', text)
text = re.sub(r'([^\n$])\n?(\$\$)', r'\1\n\n\2', text)
cell['source'] = text_to_source(text)
```

## JSON escape corruption recovery

When Python code writes LaTeX using regular (non-raw) strings, JSON escape sequences silently corrupt commands. See the full table in **`notebook-editing.md`** § "LaTeX in JSON".

**Detection:** `validate_project.py` detects control characters (`\r`, `\t`, `\a`, `\b`, `\f`, `\v`) in markdown cells, runs raw-byte scans, and heuristically flags `\n` corruption at source-array boundaries.

**Fix for `\r`, `\t`, `\a`, `\b`, `\f`, `\v` (control chars in loaded text):**

```python
import json
with open(path) as f:
    nb = json.load(f)
text = ''.join(nb['cells'][i]['source'])
# Replace control chars with their intended LaTeX commands
text = text.replace('\rho', '\\rho')       # CR+ho → \rho
text = text.replace('\text', '\\text')     # TAB+ext → \text
text = text.replace('\alpha', '\\alpha')   # BEL+lpha → \alpha
# ... etc. for each corruption found
nb['cells'][i]['source'] = text_to_source(text)
```

**Fix for raw-byte corruption (before json.load):**

```python
with open(path, 'rb') as f:
    raw = f.read()
import re
# Fix single-escaped \t → \\t (and similarly for \r, \b, \f)
fixed = re.sub(b'(?<!\\\\)\\\\t', b'\\\\\\\\t', raw)  # etc.
with open(path, 'wb') as f:
    f.write(fixed)
```

**Fix for `\n` corruption (split across source entries):**

```python
text = ''.join(cell['source'])
# Rejoin split LaTeX: $\n + u → $\nu, \n + eq → \neq
text = re.sub(r'\$\nu\b', r'$\\nu', text)  # \nu split
text = re.sub(r'(\S) \neq\b', r'\1 \\neq', text)  # \neq split
cell['source'] = text_to_source(text)
```

## Section reordering (major surgery)

Rare; only with explicit approval. Sketch:

1. Rename files via temporary names to avoid collisions.
2. Two-pass placeholder swap for section numbers in prose (e.g. `6.1` ↔ `6.2`).
3. Update titles, `§` refs, file links, equation label prefixes, Topics tables, `_toc.yml`, `index.md`.
4. Re-run `validate_project.py`.

## Parallel / bulk edit pitfalls

- Validate after every batch; spot-check files.
- Commit before large automated passes.
- Agents can blank a file—if that happens, stop and restore from git.

## Build / MyST reminders (for humans)

- `myst_footnote_transition: false` in `_config.yml` must stay (docutils).
- GitHub Pages path rewrites are handled in `build.sh` (human build only).

## Homework cell formatting issues

Homework cells (cell 3 in subsection notebooks) are often damaged by bad merges or tools.

### Detection

**Authoring rules and human checklist:** **`content-style.md`** § Homework Design (especially § Common formatting errors). Automated homework lines: **`validation.md`** (`validate_project.py`, `skills/homework-designer/scripts/audit_homework_format.py`).

### Repair patterns (mechanical)

Use Bash + Python (`notebook-editing.md`). Define `text_to_source` as in **`notebook-editing.md`**.

**Trailing stray `**` after a problem line** (heuristic—review output):

```python
import re
text = ''.join(cell['source'])
text = re.sub(
    r'^(\*\*\d+\.\s[^\n*]*\*\*[^\n]+?)\s+\*\*\s*$',
    r'\1',
    text,
    flags=re.MULTILINE,
)
cell['source'] = text_to_source(text)
```

**Missing blank lines around `$$`:**

```python
import re
text = ''.join(cell['source'])
text = re.sub(r'([^\n])\n(\$\$)', r'\1\n\n\2', text)
text = re.sub(r'(\$\$)\n([^\n])', r'\1\n\n\2', text)
cell['source'] = text_to_source(text)
```

**Sub-parts `(a)`, `(b)` glued to prior text:**

```python
import re
text = ''.join(cell['source'])
text = re.sub(r'([^\n])\s+(\([a-z]\))', r'\1\n\n\2', text)
cell['source'] = text_to_source(text)
```

**Collapsed / fused lines** (same idea as § Collapsed content recovery):

```python
import re
text = ''.join(cell['source'])
text = re.sub(r'([^\n])(#{2,4}\s)', r'\1\n\n\2', text)
text = re.sub(r'([^\n])(:::\{)', r'\1\n\n\2', text)
text = re.sub(r'([^\n$])\n?(\$\$)', r'\1\n\n\2', text)
cell['source'] = text_to_source(text)
```

### Workflow

1. Confirm the issue against **`content-style.md`**.
2. Apply the smallest repair; re-read the cell.
3. Validate per **`validation.md`**.
4. Prefer evolving **`content-style.md`** for new homework anti-patterns rather than duplicating checklists here.
