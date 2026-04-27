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

## Chapter 4 Electromagnetic Units

Chapter 4 (`notes_src/ch4_phase-and-gauge/`) uses **SI units only**.

- Minimal coupling: `\hat{\boldsymbol\pi}=\hat{\boldsymbol p}-q\boldsymbol A` (no `(q/c)\boldsymbol A`).
- Aharonov-Bohm phase: `q\oint\boldsymbol A\cdot\mathrm{d}\boldsymbol l/\hbar` (no `/(\hbar c)`).
- Maxwell equations: `\nabla\cdot\boldsymbol E=\rho_e/\epsilon_0`, `\nabla\times\boldsymbol E=-\partial_t\boldsymbol B`, and `\nabla\times\boldsymbol B=\mu_0\boldsymbol j_e+\mu_0\epsilon_0\partial_t\boldsymbol E` (no `1/c` factors).
- Point-charge fields: `\boldsymbol E=q\hat{\boldsymbol r}/(4\pi\epsilon_0 r^2)` and `\boldsymbol B=\mu_0 g\,\hat{\boldsymbol r}/(4\pi r^2)`.
- Monopole convention: `\nabla\cdot\boldsymbol B=\mu_0\rho_m`; a point monopole has total flux `\mu_0 g`.
- Use scalar electric potential `\phi`, so `\boldsymbol E=-\nabla\phi-\partial_t\boldsymbol A`.
- Gauge transformations use a dimensionful gauge function: `\psi\to\mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi`, `\boldsymbol A\to\boldsymbol A+\nabla\alpha`, and `\phi\to\phi-\partial_t\alpha`.
- Do not introduce Chapter 4 lecture material as using Gaussian units. `validate_project.py --scope ch4` flags Gaussian-only markers.

## Phase Symbols

- Use uppercase `\Phi` for phase variables, consistent with path-integral phase notation.
- Magnetic flux should use `\Phi`; the flux quantum should use `\Phi_0`.
- Flux-count degeneracy should use `N_\Phi` (and flux density `n_\Phi` if needed), not `N_\phi` or `N_{\mathrm{flux}}`.
- Path-integral accumulated phase should use `\Phi_{\mathrm{path}}`.
- Berry phases should use `\Phi_{\mathrm{Berry}}`; do not use `\Phi_{\mathrm{B}}`, which is too easy to confuse with magnetic flux.
- Aharonov-Bohm/monopole phases should use `\Phi_{\mathrm{AB}}` or `\Delta\Phi_{\mathrm{AB}}`.
- Reserve lowercase `\phi` for scalar electric potential.
- Use curly `\varphi` for azimuthal angles and azimuthal components, e.g. `(\theta,\varphi)`, `\mathrm{d}\varphi`, `A_\varphi`.

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
