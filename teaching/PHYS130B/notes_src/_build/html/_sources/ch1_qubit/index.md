# Chap 1: Qubit

## Sections

```{list-table}
:class: toc-table
:header-rows: 1
:widths: 5 60 15

* - Sec
  - Topic
  - Textbook
* - 1.1
  - [States and Observables](1-1-states-and-observables)
  - §4.1
* - 1.2
  - [Measurement](1-2-measurement)
  - §4.2
* - 1.3
  - [Time Evolution](1-3-time-evolution)
  - §4.3
```

## Review & Summary

:::{glossary}
**Qubit**
  A two-state quantum system; the quantum generalization of a classical bit.

**Ket notation** $|\psi\rangle$
  Quantum state vector in Hilbert space. In a chosen basis: $|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$ with $|\alpha|^2 + |\beta|^2 = 1$.

**Bloch sphere**
  Geometric representation of qubit pure states on a unit sphere: $|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$.

**Pauli matrices**
  $\sigma^x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $\sigma^y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$, $\sigma^z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$. Eigenvalues $\pm 1$.

**Born rule**
  Probability of outcome $m$: $p(m|O,\psi) = \langle\psi|P_{O=m}|\psi\rangle = |\langle m|\psi\rangle|^2$.

**Uncertainty principle**
  $\sigma_A \sigma_B \geq \tfrac{1}{2}|\langle [A,B] \rangle|$.

**Schrödinger equation**
  $i\hbar \partial_t |\psi\rangle = H|\psi\rangle$. Time evolution: $U(t) = e^{-iHt/\hbar}$.
:::
