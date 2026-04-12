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

Homework cells (cell 3 in subsection notebooks) are frequently corrupted by automated reformatting, tool misuse, or bad merges. This section provides audit checklists and repair patterns.

### Detection checklist

Scan homework cells for these common problems:

- [ ] **Mismatched bold markers**: Problem lines with unmatched trailing `**` (e.g., `**3. Title.** text **`)
- [ ] **Missing blank lines around `$$`**: Display math without blank lines above/below (should be `

$$..$$

`)
- [ ] **Inline sub-parts**: Sub-parts `(a)`, `(b)` on same line as preceding text or each other (should be on separate lines)
- [ ] **Lowercase titles**: Problem title first word not capitalized (should be `**N. Capitalized Title.**`)
- [ ] **Mixed bullet syntax**: Inconsistent `-` and `*` markers in same problem's list
- [ ] **LaTeX inside `**N. Title.**`**: Dollar signs or `\(` / `\)` inside the bold title span (breaks parsing; titles must be ASCII words only — see **`content-style.md`** § Homework Design § Problem format)
- [ ] **Lines > 1000 chars**: Collapsed content (headings, admonitions, or multi-line math fused into single line)

If any box is checked, proceed to repair.

### Repair pattern: Mismatched bold markers

When a problem line has a trailing `**` that should not be there:

```python
# Before: "**3. Spin precession.** A particle is placed in a field. **"
# After:  "**3. Spin precession.** A particle is placed in a field."

text = ''.join(cell['source'])
text = re.sub(r'(\*\*\d+\. [^*]+\.\*\*[^
]*?)\s*\*\*(
)', r'', text)
cell['source'] = text_to_source(text)
```

### Repair pattern: Missing blank lines around display math

When `$$` blocks lack required blank lines:

```python
import re
text = ''.join(cell['source'])
# Ensure blank line before $$
text = re.sub(r'([^
])
(\$\$)', r'

', text)
# Ensure blank line after $$
text = re.sub(r'(\$\$)
([^
])', r'

', text)
cell['source'] = text_to_source(text)
```

### Repair pattern: Inline sub-parts

When sub-parts `(a)`, `(b)`, etc. are on the same line or fused together:

```python
import re
text = ''.join(cell['source'])
# Separate sub-part labels onto new lines with blank lines before them
text = re.sub(r'([^
])\s+(\([a-z]\))', r'

', text)
cell['source'] = text_to_source(text)
```

### Repair pattern: Collapsed content

When long lines (> 1000 chars) indicate fused headings or admonitions:

```python
import re
text = ''.join(cell['source'])
# Break headings from preceding text
text = re.sub(r'([^
])(#+\s)', r'

', text)
# Break admonition openings from preceding text
text = re.sub(r'([^
])(:::\{)', r'

', text)
# Break math blocks from adjacent text
text = re.sub(r'([^
$])
?(\$\$)', r'

', text)
cell['source'] = text_to_source(text)
```

### Workflow

1. **Detect**: Run the checklist above on homework cells in question.
2. **Repair**: Apply the appropriate repair pattern(s) using Bash + Python (`notebook-editing.md`).
3. **Validate**: Run `safe_edit.py validate <path>` on the edited cell to confirm fixes.
4. **Spot-check**: Visually inspect the cell in Jupyter to ensure rendered output matches the intended format (see **`content-style.md`** § Homework Design).

### Prevention

Follow **`content-style.md`** § Homework Design § Problem format and § Common formatting errors to avoid when authoring or refactoring homework cells. Always use programmatic edits (Bash + Python) for bulk changes to avoid tool-induced corruption.

