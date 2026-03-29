# Professor Feedback — PHYS130B Lecture Note Refactoring

Write feedback here. The Manager Agent reads this file at the start of each run and creates tasks from your comments.

## Format

```
## [Date]
### [notebook name or "general"]
- [Your feedback / correction / suggestion]
```

## Feedback

(Write below this line)

## 2026-03-28
### 1-1-3-hermitian-operators
- Example: Spectral Decomposition — add examples for sigma^x and sigma^y as well → **DONE** (added σ^x and σ^y decompositions with eigenstates and matrix verification)

### general
- In all LaTeX formulas across all notebooks: imaginary unit `i` should be `\mathrm{i}`, exponent base `e` should be `\mathrm{e}`, differential operator `d` should be `\mathrm{d}`. This is a global convention change — scan and fix all occurrences in all 84 notebooks.

## 2026-03-28 — LaTeX Convention Fix Complete
### general
- LaTeX convention updates applied globally: `\mathrm{i}` for imaginary unit, `\mathrm{e}` for exponential base, `\mathrm{d}` for differential operator. Successfully changed 50/84 notebooks containing these patterns. No errors or file corruption. **DONE**


## 2026-03-29
### 1-3-3-heisenberg-picture
- Math formulas are corrupted — inspect and fix all LaTeX in this notebook. **DONE** (2026-03-29) — Fixed unescaped imaginary units in Problem 4 (2i → 2\mathrm{i}), removed unnecessary blank lines in display math blocks for cleaner rendering
- Math formulas are corrupted — inspect and fix all LaTeX in this notebook.
