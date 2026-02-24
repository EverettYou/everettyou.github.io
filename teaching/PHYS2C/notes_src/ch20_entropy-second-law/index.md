# Chap 20: Entropy and the Second Law of Thermodynamics

## Sections

| Sec | Topic |
|-----|------|
| 20-1 | [Entropy](20-1-entropy.ipynb) |
| 20-2 | [Entropy in the Real World: Engines](20-2-entropy-in-the-real-world-engines.ipynb) |
| 20-3 | [Refrigerators and Real Engines](20-3-refrigerators-and-real-engines.ipynb) |
| 20-4 | [A Statistical View of Entropy](20-4-a-statistical-view-of-entropy.ipynb) |

## Review & Summary

:::{glossary}
One-Way Processes
  An **irreversible process** is one that cannot be reversed by means of small changes in the environment. The direction is set by the *change in entropy* $\Delta S$ of the system. Entropy $S$ is a *state property*; it depends only on the state of the system. The **entropy postulate:** If an irreversible process occurs in a closed system, the entropy of the system always increases.

Calculating Entropy Change
  The **entropy change** $\Delta S$ for an irreversible process from state $i$ to $f$ equals the entropy change for *any reversible process* between those same states. We can compute the latter with

  $$
  \Delta S = S_f - S_i = \int_i^f \frac{dQ}{T}
  $$ (eq-20-entropy)

  where $Q$ is the energy transferred as heat and $T$ is the temperature in kelvins. For a reversible isothermal process, $\Delta S = Q/T$. When an ideal gas changes reversibly from $(T_i, V_i)$ to $(T_f, V_f)$,

  $$
  \Delta S = n C_V \ln\frac{T_f}{T_i} + n R \ln\frac{V_f}{V_i}
  $$ (eq-20-entropy-gas)

The Second Law of Thermodynamics
  The entropy of a closed system increases for irreversible processes and remains constant for reversible processes. It never decreases: $\Delta S \geq 0$.

Engines
  An **engine** is a device that, operating in a cycle, extracts energy as heat $|Q_H|$ from a high-temperature reservoir and does work $|W|$. The *efficiency* is

  $$
  \varepsilon = \frac{|W|}{|Q_H|} = 1 - \frac{|Q_C|}{|Q_H|}
  $$ (eq-20-efficiency)

  where $|Q_C|$ is the energy discharged as heat to the low-temperature reservoir. A **Carnot engine** is an ideal reversible engine. Its efficiency is

  $$
  \varepsilon_C = 1 - \frac{T_L}{T_H}
  $$ (eq-20-carnot)

  where $T_H$ and $T_L$ are the reservoir temperatures. A *perfect engine* (converting heat entirely to work) would violate the second law.

Refrigerators
  A **refrigerator** extracts energy $|Q_L|$ as heat from a low-temperature reservoir with work $W$ done on it. The **coefficient of performance** is $K = |Q_L|/W$. For a **Carnot refrigerator**, $K_C = T_L/(T_H - T_L)$. A *perfect refrigerator* (transferring heat from cold to hot without work) would violate the second law.

Entropy from a Statistical View
  The entropy can be defined in terms of **microstates** (possible distributions of molecules). The **multiplicity** $W$ is the number of microstates in a configuration. For a system of $N$ molecules,

  $$
  S = k \ln W
  $$ (eq-20-boltzmann)

  where $k$ is the Boltzmann constant. This connects thermodynamics to the microscopic behavior of molecules.
:::
