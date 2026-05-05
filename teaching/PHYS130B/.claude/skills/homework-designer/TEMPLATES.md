# Homework cell templates (PHYS130B)

**Law:** `rules/content-style.md` § Homework Design (counts, tone, banned wording) + `rules/physics-conventions.md` (math layout).

Match **live** subsection homework cells—e.g. `notes_src/ch6_quantum-foundations/6-1-1-mixed-states.ipynb` cell 3.

## Section header

```markdown
## Homework
```

## Problem statement pattern

- Each problem: **`**N. Short Title.**`** opening sentence, then task.
- Sub-parts: `(a)`, `(b)` on **separate lines** with a blank line before each when the stem is long.
- Use imperatives or “Show that …”; avoid “a student” / “the student.”

```markdown
**1. Density Matrix Properties.** Suppose $\{|\psi_i\rangle\}$ is an orthonormal set … Show that:

(a) $\hat{\rho}$ is Hermitian: $\hat{\rho}^\dagger = \hat{\rho}$.

(b) $\hat{\rho}$ has non-negative eigenvalues.

(c) $\mathrm{Tr}(\hat{\rho}) = 1$.

**2. Pure vs. Mixed States.** Work through parts (a)–(c).

(a) Show that …

(b) Show that …
```

## Display math in stems

Use `$$` blocks for displayed definitions students reuse across parts; keep prose between parts light (see gold notebook above).

## Handoff

Full problem sets and difficulty curve: **`SKILL.md`**. Proof-chain QC before writer implements heavy “show that” chains: **`skills/derivation-designer/SKILL.md`**.
