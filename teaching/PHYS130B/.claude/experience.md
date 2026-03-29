# Experience & Lessons Learned — PHYS130B

Hard-won knowledge from building and maintaining these Jupyter Book lecture notes. **Read this before making any programmatic edits to `.ipynb` files.**

## 1. The ipynb Source Format is Fragile

Each markdown cell's `"source"` is a JSON array of strings. Every line **except the last** must end with `\n`.

**Correct:**
```json
"source": [
  "### Heading\n",
  "\n",
  "Some paragraph text.\n",
  "\n",
  "More text."
]
```

**Wrong** (missing `\n` — renders as one giant heading):
```json
"source": ["### Heading", "", "Some paragraph text."]
```

Without `\n` terminators, Jupyter Book's MyST parser concatenates all array elements into a single string: `### HeadingSome paragraph text.` — the entire content becomes the heading.

## 2. NotebookEdit Causes Char-by-Char Corruption

The `NotebookEdit` tool (from the Claude/Cowork toolset) stores new source as **individual characters** — each character becomes a separate array element:

```json
"source": ["#", "#", "#", " ", "T", "o", "p", "i", "c", "s", "\n", ...]
```

This renders as garbage in Jupyter Book.

**Rule: NEVER use `NotebookEdit` for content changes.** Instead:
```python
import json
with open(path) as f:
    nb = json.load(f)
# modify nb['cells'][i]['source'] as list of "\n"-terminated strings
with open(path, 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
```

## 3. The `Edit` Tool Does Not Work on `.ipynb`

The Edit tool expects plain text files. `.ipynb` is JSON. Use Python `json.load`/`json.dump` via Bash instead.

## 4. Safe Pattern for Writing Cell Source

```python
def text_to_source(text):
    """Convert a markdown string to a proper ipynb source array."""
    lines = text.split('\n')
    source = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            source.append(line + '\n')
        else:
            if line:  # skip trailing empty
                source.append(line)
    return source
```

Always use `json.dump(nb, f, indent=1, ensure_ascii=False)` to preserve Unicode and LaTeX characters.

## 5. Three Corruption Patterns and How to Fix Them

### 5a. Char-by-char (from NotebookEdit or buggy json.dump)

**Detection:** Most source elements are 1–2 characters long.
```python
short = sum(1 for s in src if len(s) <= 2)
if short > len(src) * 0.7 and len(src) > 20:
    print("CORRUPTED")
```

**Fix:** Recover original chars, join, split by `\n`:
```python
# If newline fix was already applied (chars are "c\n"):
chars = []
for s in src:
    if s == '\n':
        chars.append('\n')  # original newline
    elif s.endswith('\n') and len(s) == 2:
        chars.append(s[0])  # strip spurious \n
    else:
        chars.append(s)
full_text = ''.join(chars)
cell['source'] = text_to_source(full_text)
```

### 5b. Missing `\n` terminators (from careless json.dump)

**Detection:** Non-final lines don't end with `\n`.
```python
missing = sum(1 for i, s in enumerate(src[:-1]) if not s.endswith('\n'))
```

**Fix:** Append `\n` to all non-final lines.

### 5c. Collapsed content (headings fused to body)

**Detection:** Any single source line > 1000 characters.

**Fix:** Regex to insert `\n\n` before structural markers:
```python
import re
text = ''.join(src)
text = re.sub(r'([^\n])(#{2,4}\s)', r'\1\n\n\2', text)      # headings
text = re.sub(r'([^\n])(:::\{)', r'\1\n\n\2', text)          # admonitions
text = re.sub(r'([^\n$])\n?(\$\$)', r'\1\n\n\2', text)       # display math
cell['source'] = text_to_source(text)
```

### Comprehensive Validation Script

Run this after any bulk edit:
```python
import json, glob

for f in sorted(glob.glob('notes_src/**/*.ipynb', recursive=True)):
    if '/_build/' in f: continue
    with open(f) as fh:
        nb = json.load(fh)
    for ci, cell in enumerate(nb['cells']):
        if cell['cell_type'] != 'markdown': continue
        src = cell['source']
        if not src or len(src) < 5: continue

        # Check 1: char-by-char
        short = sum(1 for s in src if len(s) <= 2)
        if short > len(src) * 0.7 and len(src) > 20:
            print(f'CHAR-BY-CHAR: {f} cell {ci}')

        # Check 2: collapsed lines
        max_len = max(len(s) for s in src)
        if max_len > 1000:
            print(f'LONG LINE: {f} cell {ci} (max {max_len})')

        # Check 3: missing newlines
        missing = sum(1 for i, s in enumerate(src[:-1]) if not s.endswith('\n'))
        if missing > 0:
            print(f'MISSING \\n: {f} cell {ci} ({missing} lines)')
```

## 6. Display Math `$$` Requires Blank Lines Above and Below

Every `$$...$$` display math block **must** have an empty line above and below it. Without blank lines, the MyST parser treats `$$` as inline math delimiters and merges the equation with adjacent text, producing broken output with stray `$` signs floating around.

**Correct:**
```markdown
The energy is given by

$$
E = mc^2
$$ (eq-energy)

where $m$ is the mass.
```

**Wrong** (no blank lines — parser treats as inline math):
```markdown
The energy is given by
$$
E = mc^2
$$ (eq-energy)
where $m$ is the mass.
```

This also applies when writing cell source programmatically — ensure `\n\n` separates `$$` from surrounding text.

## 7. Section Reordering (Swapping x.y Sections)


When swapping two sections (e.g., 6.1 ↔ 6.2):

1. **Rename files via temp names** to avoid collisions: `6-1-*` → `tmp-a-*`, `6-2-*` → `tmp-b-*`, then `tmp-a-*` → `6-2-*`, `tmp-b-*` → `6-1-*`.

2. **Two-pass placeholder replacement** to avoid circular substitutions:
   - Pass 1: `6.1` → `__PLACEHOLDER_A__`, `6.2` → `__PLACEHOLDER_B__`
   - Pass 2: `__PLACEHOLDER_A__` → `6.2`, `__PLACEHOLDER_B__` → `6.1`

3. **Update everything**: titles (`# 6.x.y`), `§` references, file links, equation labels (`eq-6-x-`), Topics table numbers, `_toc.yml` block ordering, `index.md`, chapter `index.md`.

4. **Verify `_toc.yml` ordering** — the block-swap logic can leave sections in wrong order. Check manually.

## 8. Parallel Agent Pitfalls

When using multiple agents to process notebooks in parallel:

- **Agents can corrupt files.** One agent destroyed `6-1-2-entanglement-measures.ipynb` content entirely, replacing it with a placeholder string. Always validate after agent runs.
- **Agents may use json.dump without `\n` terminators.** Always run the validation script after.
- **Agents may miss edge cases.** Always do a manual spot-check on a few files.
- **Keep the original content recoverable.** If possible, git commit before launching parallel agents.

## 9. Build Gotchas

- **Always clear `_build/`** before rebuilding: `rm -rf notes_src/_build`. Stale copies in `_build/html/_sources/` and `_build/jupyter_execute/` persist and mask fixes.
- **`build.sh` must run from `PHYS130B/`**, not from `notes_src/`.
- **GitHub Pages ignores `_` prefixed dirs** — `build.sh` copies `_static` → `static`, `_images` → `images`, and rewrites HTML references.
- The `myst_footnote_transition: false` setting in `_config.yml` prevents a docutils crash. Do not remove it.

## 10. Content Quality Patterns

- **"Example" or "Application" sections** with detailed calculations belong in `:::{admonition} Example: ...\n:class: example` boxes, not bare `###` headings.
- **Large text blocks** should be broken into bullet points or shorter paragraphs for readability.
- **Prompts boxes** (`:::{admonition} Prompts\n:class: tip`) belong only at the `x.y.z` subsection level, never at `x.y` parent level.
- **Overview sections** at x.y level should be motivating paragraphs, not bullet lists.

## 11. Known Remaining Issues

- **5.2.3** covers 4 unrelated topics at 13K chars — candidate for splitting into sub-notebooks.
- Some Ch3 notebooks may still have dense single-paragraph content from the collapsed-content fix (headings restored but paragraph breaks within sections may be missing).
