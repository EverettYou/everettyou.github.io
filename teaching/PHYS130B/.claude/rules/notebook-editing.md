# Rule: Safe notebook editing (`.ipynb`)

Mandatory for any change to Jupyter notebooks in this project.

## Banned tools

See **`rules/tooling-security.md`** for why `NotebookEdit`, `Edit`, and `Write` are disallowed for agents and what to use instead.

## Required method

All writes go through **Bash** using Python:

```python
import json
with open(path) as f:
    nb = json.load(f)
nb['cells'][i]['source'] = new_source_list  # use text_to_source() for markdown strings
with open(path, 'w') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
```

For plain text files (`.md`, `.yml`, `.py`), use normal `open` read/write or `str.replace` patterns in `tooling-security.md`.

## Source array format

Each cell `"source"` is a list of strings. **Every line except the last must end with `\n`.**

Canonical helper (duplicate of `skills/notebook-writer/scripts/safe_edit.py`):

```python
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
```

## Pre-edit checklist

1. Read the notebook first—cell count and indices.
2. Never assume indices unchanged after prior edits.
3. Git commit before bulk or risky passes.

## Post-edit checklist

1. `safe_edit.py validate <path>` and/or `validate_project.py --scope …` (`rules/validation.md`).
2. No char-by-char corruption, missing `\n`, or lines >1000 chars (collapsed cells).
3. **Notation consistency sweep across the entire cell.** After substantive edits, grep the cell for every operator/symbol introduced or modified and confirm only one symbol is used per physical quantity. Local edits often inherit a symbol from their immediate context that conflicts with an upstream definition; this only surfaces when the whole cell is read end-to-end. Common collisions: `\hat{p}_\theta` vs `\hat{L}_\theta`, `\Phi(t)` vs `\phi(t)` for flux, bare `X, Z` vs `\hat{X}, \hat{Z}` for Pauli operators.

4. **Related-symbol audit (case/super/sub variants of the same letter).** When a derivation introduces *two* symbols built from the same letter that denote *different* physical quantities — e.g. `\hat{j}` (single-particle current) vs `\hat{J}` (current density), `\rho` (charge density) vs `\rho_e` (electric resistivity), `E` (energy) vs `\mathcal{E}` (electric field), `\sigma_{xy}` (conductivity) vs `\rho_{xy}` (resistivity) — apply the following discipline before writing the derivation:

   - **Define both symbols explicitly upfront**, in one place, before either is used. Do not let the first symbol's definition do double duty.
   - **State the relationship as a labeled equation.** Example: `\hat{J}_a = (1/A)\sum_n \hat{j}_a^{(n)}` with `(eq-current-density-def)`. Whenever the relationship is *invoked* mid-derivation (e.g. when a $1/A$ or $\sum_n$ factor appears), cite that label.
   - **Watch for "smoking-gun" prefactors.** A lone `1/A`, `1/V`, `1/N`, or `\sum_\alpha` in a final formula must trace back to an explicit symbol-conversion step. If you cannot point at the line where it entered, you have probably conflated the two symbols.
   - **No silent reassignment.** A generic placeholder like "take $\hat{O} = \cdots$" mid-derivation is a red flag — it usually masks a symbol switch the reader cannot follow. Either keep the placeholder generic to the end, or substitute the *defined* symbol with explicit citation.

   **Failure mode (pattern to recognise):** copy-pasting a target formula from a reference notebook and reverse-engineering the derivation to match it. The target formula's prefactors get pulled in without a corresponding definition step, and the reader sees a $1/A$ (or similar) appear out of nowhere.

## LaTeX in JSON — escape character hazards

JSON and Python share several escape sequences that silently corrupt LaTeX commands. When writing notebook source via Python, **always use raw strings** (`r"..."`) or **double every backslash** (`"\\\\rho"`). Never write LaTeX in regular Python strings.

| Escape | Char | LaTeX commands corrupted |
|--------|------|------------------------|
| `\n` | newline (0x0A) | `\nabla`, `\nu`, `\neq`, `\not`, `\nrightarrow` |
| `\r` | CR (0x0D) | `\rho`, `\rangle`, `\rightarrow`, `\Re` |
| `\t` | TAB (0x09) | `\text`, `\theta`, `\tau`, `\tanh`, `\to`, `\times` |
| `\b` | BS (0x08) | `\beta`, `\boldsymbol`, `\begin`, `\bar`, `\bra` |
| `\f` | FF (0x0C) | `\frac`, `\forall` |
| `\a` | BEL (0x07) | `\alpha`, `\approx` |
| `\v` | VT (0x0B) | `\varepsilon`, `\vert`, `\varphi`, `\vec` |

**Root cause:** Python code that builds LaTeX strings without raw-string syntax:
```python
# WRONG — \rho becomes CR+ho, \text becomes TAB+ext
cell['source'] = text_to_source("$\rho$ and $\text{Tr}$")

# CORRECT — raw string preserves backslashes
cell['source'] = text_to_source(r"$\rho$ and $\text{Tr}$")
```

**Detection:** `validate_project.py` checks for control characters in markdown cells (`\r`, `\a`, `\b`, `\f`, `\v`, `\t`) and runs a raw-byte scan of the JSON file. The `\n` corruption is detected heuristically (source-array boundary patterns).

**In JSON files directly:** Every LaTeX backslash must be `\\` (double-escaped). If you see `\text` in raw JSON, it should be `\\text`. The validator's raw-byte check catches this.

## Deeper repairs

Char-by-char and collapsed-cell recipes: **`rules/troubleshooting-ipynb.md`**.
