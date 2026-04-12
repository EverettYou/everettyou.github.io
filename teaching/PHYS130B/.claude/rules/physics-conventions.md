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

## Dot Product (`\cdot`)

- `\cdot` is **only** for dot products between vectors: `\boldsymbol{a} \cdot \boldsymbol{b}`, `\nabla \cdot \boldsymbol{j}`.
- **Never** use `\cdot` between scalar quantities (e.g., `\partial_x \cdot j` is wrong; write `\partial_x j` or `\frac{\partial j}{\partial x}`).
- In 1D, the continuity equation is `\partial_t \rho + \frac{\partial j}{\partial x} = 0`; in 3D, use `\partial_t \rho + \nabla \cdot \boldsymbol{j} = 0`.

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
- Do NOT put blank lines inside a `$$...$$` block (equation lines must be contiguous)
- Label important equations: `$$ E = mc^2 $$ (eq-section-description)`
- Label convention: `eq-{topic}-{description}` (e.g., `eq-mixed-purity`)
- Cross-reference: `` {eq}`eq-section-name` ``
- For multiline equations, always use `\begin{split} ... \end{split}` inside `$$...$$`
- Do NOT use `align` or `aligned` environments in notebooks (unsafe parsing around leading commutators like `[A,B]`)

## Ket/Bra Notation and Pipe Characters

- Use `\vert` for `|` in kets and bras throughout: `$\vert\psi\rangle$`, `$\langle\phi\vert$`, `$\vert 0\rangle$`.
- **Never glue `\vert` to a following letter or digit** (wrong: `\vertV`, `\vertn`, `\vert0\rangle`; right: `\vert V\vert`, `\vert n\rangle`, `\vert 0\rangle`). Otherwise MathJax may misparse. Matrix elements: `\langle m\vert V\vert n\rangle`. For operator norms prefer `\|V\|` or `\lVert V\rVert`. `validate_project.py` flags glued `\vert` inside `$...$` / `$$...$$`.
- This is **required** inside markdown tables (bare `|` clashes with pipe syntax) and **recommended** everywhere else for consistency.

## Inline vs Display

- Use `$...$` for inline math
- Reserve `$$...$$` for key displayed results
