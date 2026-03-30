# /project:validate — Validate All Notebooks

Run comprehensive validation across all 84 notebooks to catch corruption and structural issues.

## Usage

```
/project:validate [scope]
```

- `/project:validate` — all notebooks
- `/project:validate ch3` — only Chapter 3
- `/project:validate 6-1-1-mixed-states` — single notebook

## Instructions

1. **Run the corruption validation script** (`skills/notebook-writer/scripts/safe_edit.py validate`):
   - Char-by-char corruption (source elements mostly ≤2 chars)
   - Collapsed content (lines >1000 chars)
   - Missing `\n` terminators on non-final lines

2. **Check cell structure** per `design.md`:
   - x.y.z notebooks: exactly 4 cells (title, prompts, lecture notes, homework)
   - x.y notebooks: exactly 3 cells (title, overview, project)
   - Verify heading formats match `# x.y.z Title` pattern

3. **Check LaTeX conventions:**
   - `\mathrm{i}` for imaginary unit (not bare `i` in exponents)
   - `\mathrm{e}` for Euler's number (not bare `e`)
   - `\mathrm{d}` for differential operator (not bare `d`)
   - `\boldsymbol` for vectors (not `\vec`)
   - `\hat` for operators
   - Display math `$$` has blank lines above and below

4. **Check for banned patterns:**
   - `---` horizontal rules
   - Nested `:::` admonitions
   - `plt.show()` (should use `display(fig)`)

5. **Report results** as a summary table:
   ```
   | Notebook | Corruption | Structure | LaTeX | Other |
   ```

6. **If issues found**, create entries in `progress.md` → Issues section.
