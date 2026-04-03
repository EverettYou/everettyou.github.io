# Professor Feedback — PHYS130B Lecture Note Refactoring

Write feedback here. The Manager Agent reads this file at the start of each run and creates tasks from your comments.

## Format

```
## [Date]
### [notebook name or "general"]
- [Your feedback / correction / suggestion]
```

## Feedback

---
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


## 2026-03-31
### 3-1-2-physical-optics
- Build warning: duplicate label `eq-snell-law` — also used in 3-1-1-geometric-optics. Rename one of them (e.g., `eq-snell-refraction` in 3.1.2 since 3.1.1 derives it first from Fermat's principle). **DONE** (2026-03-31) — renamed to eq-snell-refraction in 3-1-2-physical-optics.ipynb


## 2026-04-01
### 2-3-3-toric-code
- Math input error: "charges () and fluxes () — whose composite" — empty parentheses indicate corrupted LaTeX. Inspect and fix all math in this notebook. **DONE** (2026-04-01) — Fixed corrupted \\varepsilon (\\x0b from \\v) and \\times (tab from \\t) in Overview paragraph. No other corruption found.

### General
- Audit consistency of the Chapter-Unit-Lesson naming hierarchy across all notes. Specifically:
  - **Chapter landing pages** (ch1–ch6 `index.md`): verify they all follow the same style — heading format, table structure, glossary, etc.
  - **Unit landing pages** (x.y parent notebooks): verify they all follow the same style — cell structure, heading names (Overview, Topics table, Key Concepts, Learning Objectives, Project), table format, and content depth.
  - Fix any inconsistencies so every page at the same level looks and reads the same way.
  **DONE** (2026-04-01) — Fixed all 20 parent notebooks: `## Projects`→`## Project`, `### Lessons`→`### Topics`, Keywords→Core Questions (3.4, 4.1, 5.1, 6.3, 6.4). Chapter index pages already consistent.

### General
- Audit admonition class usage across all notebooks for consistency with `.claude/rules/content-style.md`. Specifically:
  - Verify each admonition uses the correct class for its role (e.g., `important` for core definitions/theorems, `note` for background/intuition, `information` for derivations, etc.).
  - Some `important` boxes may be overused — downgrade to `note` if the content is supplementary context, physical intuition, or clarification rather than a core definition or fundamental result that students must memorize.
  - Reserve `important` strictly for key definitions, theorems, and fundamental equations.
  **DONE** (2026-04-02) — Audited all 84 source notebooks (204 `important` boxes → 185). Downgraded 13 to `note` (supplementary properties/context), 6 to `attention` (subtle insights/clarifications), renamed 6 with generic titles (Definition, Key X, Important) to descriptive names. All 18 modified notebooks validated OK.
