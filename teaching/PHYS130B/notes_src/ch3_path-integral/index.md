# Chap 3: Path Integral

## Sections

```{list-table}
:class: toc-table
:header-rows: 1
:widths: 5 60 15

* - Sec
  - Topic
  - Textbook
* - 3.1
  - [Quantization](3-1-quantization)
  -
* - 3.2
  - [Propagator](3-2-propagator)
  - §15.1
* - 3.3
  - [Stationary Phase](3-3-stationary-phase)
  - §15.2
* - 3.4
  - [Imaginary Time](3-4-imaginary-time)
  - §15.3
```

## Review & Summary

:::{glossary}
**Path integral**
  $K(x_f,t_f;x_i,t_i) = \int \mathcal{D}[x]\, e^{iS[x]/\hbar}$. Sum over all paths weighted by the action phase.

**Propagator**
  Transition amplitude kernel satisfying the composition property and the Schrödinger equation.

**Free-particle propagator**
  $K_{\text{free}} = \left(\frac{m}{2\pi i\hbar T}\right)^{d/2} \exp\!\left(\frac{im(\Delta x)^2}{2\hbar T}\right)$.

**Stationary phase**
  Dominant contribution from classical paths where $\delta S = 0$. Quantum corrections are fluctuations around these paths.

**WKB approximation**
  Semiclassical ansatz $\psi = A(x)e^{iS(x)/\hbar}$; valid when the potential varies slowly on the scale of the de Broglie wavelength.

**Bohr-Sommerfeld quantization**
  $\oint p\,dx = 2\pi\hbar(n+\tfrac{1}{2})$.

**Wick rotation**
  $t \to -i\tau$: connects quantum mechanics ($e^{iS/\hbar}$) to statistical mechanics ($e^{-S_E/\hbar}$).

**Partition function**
  $Z(\beta) = \mathrm{Tr}(e^{-\beta H}) = \int \mathcal{D}[x]\, e^{-S_E/\hbar}$ over closed paths with period $\beta = 1/k_BT$.
:::
