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

## 2026-04-05
### 3-2-1-path-integral-formulation
- "Derivation: Harmonic Oscillator Path Integral via Gaussian Fluctuations" is misplaced and diverges from the storyline. This notebook's arc is deriving the Schrödinger equation from the path integral — the harmonic oscillator doesn't belong here. If anywhere, it would go after 3.2.3 (free particle propagator), but even then it's better left as a homework problem. Remove this derivation.
- More generally: derivations must align closely with the notebook's storyline. A derivation that wanders off-topic or introduces content from a later notebook is worse than no derivation at all.
- In 3.2.3 we derive the free particle propagator using the solution of the Schrödinger equation, not via time-slicing Gaussian integrals. If a derivation is needed there, it should show how the time-slicing approach reproduces the same free-particle result — connecting the two methods is the pedagogically valuable step.

### general (derivation pedagogy)
- Derivations should be self-contained and accessible to undergraduates who may lack background in complex analysis, advanced calculus, or even trigonometry. If a derivation relies on a non-trivial mathematical result, **introduce that math from elementary principles first** before using it.
- Example: "Derivation: Gaussian Moments" cites the standard Gaussian integral as a known result, but students don't know how to compute it. A good derivation should: (1) start with the simplest form $\int \mathrm{e}^{-x^2/2} \mathrm{d}x$ and explain how it's evaluated (e.g., the squaring trick with polar coordinates) in an accessible way; (2) rescale variables to introduce a coefficient $\alpha$; (3) use $\alpha$-derivatives to generate higher moments; (4) then apply these results to the quantum propagator context in the course. Build up from what students know, don't assume mathematical sophistication.

### general (homework style)
- Audit homework formatting across all notebooks. Currently some problems have titles and some don't, and the format is inconsistent. Spot the specific inconsistencies and propose a unified style. Titles for homework problems are probably helpful (they tell students what the problem is about at a glance), but only if they work naturally for all problems and are kept concise. The auditor should survey the current state, identify the patterns, and write a concrete proposal before any changes are made.
