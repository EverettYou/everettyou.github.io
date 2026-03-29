# Chap 6: Quantum Foundations

## Sections

```{list-table}
:class: toc-table
:header-rows: 1
:widths: 5 60 15

* - Sec
  - Topic
  - Textbook
* - 6.1
  - [Density Matrix](6-1-density-matrix)
  - §16.3
* - 6.2
  - [Entanglement](6-2-entanglement)
  - §16.1, §16.2
* - 6.3
  - [Generalized Measurement](6-3-generalized-measurement)
  - §16.4
* - 6.4
  - [Open Quantum Systems](6-4-open-quantum-systems)
  - §16.5
```

## Review & Summary

:::{glossary}
**Entanglement**
  Non-separable correlations in composite systems. Bell states: $|\Phi^\pm\rangle = \frac{1}{\sqrt{2}}(|\uparrow\uparrow\rangle \pm |\downarrow\downarrow\rangle)$.

**Density matrix**
  $\rho = \sum_i p_i|\psi_i\rangle\langle\psi_i|$. Pure: $\mathrm{Tr}(\rho^2)=1$. Mixed: $\mathrm{Tr}(\rho^2)<1$.

**Partial trace**
  $\rho_A = \mathrm{Tr}_B(\rho_{AB})$. Reduced state describing subsystem $A$ alone.

**Von Neumann entropy**
  $S(\rho) = -\mathrm{Tr}(\rho\ln\rho)$. Measures mixedness; equals entanglement entropy for bipartite pure states.

**CHSH inequality**
  $|\langle\mathcal{B}\rangle| \le 2$ classically; quantum violation up to $2\sqrt{2}$ (Tsirelson bound).

**POVM**
  Generalized measurement: $\{M_i\}$ with $\sum_i M_i = I$, $p_i = \mathrm{Tr}(M_i\rho)$.

**Quantum channel**
  CPTP map in Kraus form: $\mathcal{E}(\rho) = \sum_k K_k\rho K_k^\dagger$, $\sum_k K_k^\dagger K_k = I$.

**Lindblad equation**
  $\dot\rho = -\frac{i}{\hbar}[H,\rho] + \sum_k(L_k\rho L_k^\dagger - \tfrac{1}{2}\{L_k^\dagger L_k,\rho\})$.
:::
