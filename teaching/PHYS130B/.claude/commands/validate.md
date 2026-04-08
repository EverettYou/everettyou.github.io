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

1. **Run the unified validator**:
   - Full validation:
     - `python3 .claude/scripts/validate_project.py`
   - Chapter scope:
     - `python3 .claude/scripts/validate_project.py --scope ch3`
   - Single notebook:
     - `python3 .claude/scripts/validate_project.py --scope 6-1-1-mixed-states`
   - Docs only (rules/design consistency):
     - `python3 .claude/scripts/validate_project.py --docs-only`

2. **Validator covers**:
   - Notebook corruption checks (char-by-char, long collapsed lines, missing newline terminators)
   - Notebook structure checks (x.y vs x.y.z cell counts and title format)
   - MyST display math checks (`$$` blank lines outside, no blank lines inside)
   - Banned patterns (`---`, `plt.show()`, `### Application:`, nested `:::` admonitions)
   - Physics notation checks in math blocks:
     - Upright differential (`\mathrm{d}`) in common calculus patterns
     - Upright Euler exponential base (`\mathrm{e}^{...}`)
     - Upright imaginary unit in exponentials (`\mathrm{i}`)
     - Forbid `\vec{...}` (use `\boldsymbol{...}`)
     - Enforce `\vert` instead of raw `|` for ket/bra in markdown tables
   - Rule/design consistency checks between `rules/physics-conventions.md` and `design.md`

3. **Report results** as a summary table:
   ```
   | Notebook | Corruption | Structure | LaTeX | Other |
   ```

4. **If issues found**, create entries in `progress.md` → Issues section.
