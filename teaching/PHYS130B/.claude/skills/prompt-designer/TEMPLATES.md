# Prompts cell templates (PHYS130B)

**Law:** `rules/prompt-preview.md` (criteria + anti-patterns). **Structure:** `rules/notebook-architecture.md` (subsections only). **Cross-refs:** `rules/myst-references.md`.

When drafting or refreshing prompts, open a **gold** subsection notebook (same chapter if possible)—e.g. `notes_src/ch6_quantum-foundations/6-1-1-mixed-states.ipynb` cell 1—and match its tone, density, and MyST fences.

## MyST shell (cell 1, x.y.z)

Replace bracketed placeholders; keep **4–5** bullets typical.

```
:::{admonition} Prompts
:class: tip

- What is [concept], and why does [key property] follow? How does it differ from [related concept]?
- Derive [result]. Why does [notable feature] emerge from the derivation?
- How does [object A] relate to [object B]? What does this connection reveal about [physics]?
- For [specific setup], [compute/show] [quantity]. What does the result tell us about [interpretation]?
- Why does [surprising fact] hold? What would go wrong if [alternative]?
:::
```

Each bullet should be **specific enough** for an LLM to give a focused, lecture-relevant answer—name the concept or object precisely (short inline math like `$\hat{\rho}$` is fine). Avoid pasting full Hamiltonians; refer to objects by name.

## Style references (from live notes)

These are **pattern** excerpts; all bullets still must pass **`prompt-preview.md`**.

**Early chapter (conceptual breadth):**

```
- What distinguishes quantum physics from classical physics in the way it describes physical systems? How does quantum mechanics represent states and predict outcomes?
- What is a qubit, and why is it the simplest quantum system? How does it illustrate the core ideas of quantum mechanics?
```

**Perturbation / derivations (naming + why):**

```
- What is the Hellmann-Feynman theorem, and how does it give the first-order energy correction as an expectation value without expanding eigenstates?
- Derive the first-order state correction. Why does the admixture of state $m$ scale as coupling/gap?
- Why does the second-order energy correction always lower the ground state? Connect this to the variational principle.
```

**Density matrix subsection (6-1-1 style—four bullets is OK):**

```
- What is the difference between a pure state and a mixed state? Why can't a mixed state be described by a single ket $|\psi\rangle$?
- Construct the density matrices for a qubit superposition $(|0\rangle + |1\rangle)/\sqrt{2}$ and a 50-50 classical mixture. How do they differ?
- How does purity $\mathrm{Tr}(\hat{\rho}^2)$ distinguish pure from mixed states? What is the geometric meaning on the Bloch ball?
```

Add a fourth or fifth bullet when the lecture cell introduces another major thread (e.g. ensemble non-uniqueness in 6-1-1).
