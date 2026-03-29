# Chap 5: Perturbation Theory

## Sections

```{list-table}
:class: toc-table
:header-rows: 1
:widths: 5 60 15

* - Sec
  - Topic
  - Textbook
* - 5.1
  - [Time-Independent Perturbation](5-1-time-independent-perturbation-theory)
  - §10.1
* - 5.2
  - [Time-Dependent Perturbation](5-2-time-dependent-perturbation-theory)
  - §11.3
```

## Review & Summary

:::{glossary}
**Perturbation series**
  $E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots$ for $H = H_0 + \lambda V$.

**First-order energy**
  $E_n^{(1)} = \langle n^{(0)}|V|n^{(0)}\rangle$ (Hellmann-Feynman).

**Second-order energy**
  $E_n^{(2)} = \sum_{m\neq n} \frac{|\langle m^{(0)}|V|n^{(0)}\rangle|^2}{E_n^{(0)} - E_m^{(0)}}$. Always lowers the ground state energy.

**Degenerate perturbation**
  Diagonalize $V$ within the degenerate subspace via the effective Hamiltonian.

**Interaction picture**
  $V_I(t) = e^{iH_0 t/\hbar}V(t)e^{-iH_0 t/\hbar}$. Dyson series: $U(t) = \mathcal{T}\exp\!\left(-\frac{i}{\hbar}\int_0^t V_I(t')dt'\right)$.

**Fermi's golden rule**
  $\Gamma_{i\to f} = \frac{2\pi}{\hbar}|\langle f|V|i\rangle|^2 \rho(E_f)$.

**Adiabatic theorem**
  Slow evolution keeps the system in the instantaneous eigenstate, acquiring a Berry phase.
:::
