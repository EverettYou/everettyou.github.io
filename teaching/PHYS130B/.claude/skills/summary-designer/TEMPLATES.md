# Summary and See Also templates (PHYS130B)

**Law:** `rules/content-style.md` § Summary and See Also + `rules/myst-references.md` (link format, fences).

Gold reference: `notes_src/ch6_quantum-foundations/6-1-1-mixed-states.ipynb` lecture cell (end)—bullets then separate See Also admonition.

## `### Summary`

- Bullet-only; **no** tables inside Summary.
- Typical **5–7** bullets (hard max **8**); each starts with a **bold lead-in** + colon when summarizing a definition cluster (current chapter style).

```markdown
### Summary

- **Density matrix definition:** $\hat{\rho} = \sum_i p_i |\psi_i\rangle\langle\psi_i|$ …
- **Purity:** $\mathrm{Tr}(\hat{\rho}^2) = 1$ iff pure …
- **Expectation values and probabilities:** …
```

## `See Also` admonition (separate, immediately after Summary)

Title exactly `See Also`, class `seealso`, own `:::` fences—**never** fold into Summary list items.

```markdown
:::{admonition} See Also
:class: seealso

- [1.2.3 Measurement Operators](../ch1_qubit/1-2-3-measurement-operators): One-line gloss after the colon.
- [6.1.2 Entropy](6-1-2-entropy): …
:::
```

Use relative stems / paths per `myst-references.md`; **do not** bold-wrap the markdown link token in See Also lines.

## Bootstrap scripts

TOC-driven first pass: see **`SKILL.md`** § bulk scripts (`notebook-writer` session only).
