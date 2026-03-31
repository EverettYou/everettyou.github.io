# Rule: Physics and LaTeX Conventions

All notebooks must follow these notation conventions consistently.

## Upright Symbols (ISO 80000-2)

Constants and operators that are not variables use upright (roman) type:

| Symbol | LaTeX | Usage |
|--------|-------|-------|
| Imaginary unit | `\mathrm{i}` | `\mathrm{e}^{\mathrm{i}\theta}` |
| Euler's number | `\mathrm{e}` | `\mathrm{e}^{-\beta E}` |
| Differential | `\mathrm{d}` | `\mathrm{d}x`, `\frac{\mathrm{d}}{\mathrm{d}t}` |

## Vectors and Operators

| Entity | Convention | Example |
|--------|-----------|---------|
| Vectors | `\boldsymbol` (not `\vec`) | `\boldsymbol{S}`, `\boldsymbol{r}`, `\boldsymbol{B}` |
| Quantum operators | `\hat{...}` | `\hat{H}`, `\hat{p}`, `\hat{O}` |
| Pauli operators | Superscript indices | `\hat{\sigma}^x`, `\hat{\sigma}^y`, `\hat{\sigma}^z` |
| Pauli matrices (explicit 2x2) | Plain with superscript | `\sigma^x`, `\sigma^y`, `\sigma^z` |
| Vectorized Pauli | Both | `\hat{\boldsymbol{\sigma}} = (\hat{\sigma}^x, \hat{\sigma}^y, \hat{\sigma}^z)` |

## Eigenstate Notation

| Observable | Eigenstates |
|-----------|-------------|
| X (σ_x) | `\|+\rangle`, `\|-\rangle` |
| Y (σ_y) | `\|\mathrm{i}\rangle`, `\|\bar{\mathrm{i}}\rangle` |
| Z (σ_z) — qubit | `\|0\rangle`, `\|1\rangle` |
| Z (σ_z) — spin | `\|\uparrow\rangle`, `\|\downarrow\rangle` |

## Notation Consistency: Spin vs QI

Two notation systems coexist for qubit operators and states. **Never mix them within the same equation or problem.**

| System | Operators | Ket states |
|--------|-----------|------------|
| **Spin** | `\hat{\sigma}^x`, `\hat{\sigma}^y`, `\hat{\sigma}^z` | `\vert\uparrow\rangle`, `\vert\downarrow\rangle`, `\vert+\rangle`, `\vert-\rangle` |
| **QI (Quantum Information)** | `\hat{X}`, `\hat{Y}`, `\hat{Z}` | `\vert 0\rangle`, `\vert 1\rangle`, `\vert+\rangle`, `\vert-\rangle` |

**Rule:** In any single equation or homework problem, pick one system and stick to it:
- If kets use $\vert 0\rangle, \vert 1\rangle$, operators must be $\hat{X}, \hat{Y}, \hat{Z}$.
- If kets use $\vert\uparrow\rangle, \vert\downarrow\rangle$, operators must be $\hat{\sigma}^x, \hat{\sigma}^y, \hat{\sigma}^z$.

## Display Math

- `$$...$$` blocks MUST have blank lines above and below
- Label important equations: `$$ E = mc^2 $$ (eq-section-description)`
- Label convention: `eq-{topic}-{description}` (e.g., `eq-mixed-purity`)
- Cross-reference: `` {eq}`eq-section-name` ``

## Ket/Bra Notation and Pipe Characters

- Use `\vert` for `|` in kets and bras throughout: `$\vert\psi\rangle$`, `$\langle\phi\vert$`, `$\vert 0\rangle$`.
- This is **required** inside markdown tables (bare `|` clashes with pipe syntax) and **recommended** everywhere else for consistency.

## Inline vs Display

- Use `$...$` for inline math
- Reserve `$$...$$` for key displayed results
