---
name: phys130b-physics-review
description: Physics correctness, notation, homework and discussion sanity for PHYS130B quantum mechanics notes. Use when equations, problems, or claims change.
---

# Skill: Science reviewer (PHYS130B)

Expert-level **quantum mechanics** check: equations, definitions, homework/discussion/project feasibility, notation vs `rules/physics-conventions.md`.

## Activation (auto)

- Any edit touching **display math**, **inline physics**, **homework** “show that” targets, **numeric factors**, or **new claims**.
- After substantial lecture rewrites that introduce new derivations or examples.
- When `feedback.md` flags a possible error.

## Non-goals

- **Not** for pure Markdown formatting or cell-count fixes—`notebook-writer`.
- **Not** for narrative pacing without physics impact—`lecture-content`.
- Never run **`./build.sh`** or **`jupyter-book build`** (sandbox). Does **not** require a successful book build—use validators only (`rules/validation.md`).

## Fallback / de-escalation

- If a possible ERROR depends on convention choice, mark **WARNING** and cite Tong or standard QM text.
- If the notebook is corrupted, **stop**—require `notebook-writer` + `troubleshooting-ipynb` first, then re-run science review.

## Checklist (summary)

1. **Equations:** dimensions, signs, factors of 2, π, ℏ; operator order; matched bras/kets.
2. **Notation:** `\mathrm{i}`, `\mathrm{e}`, `\mathrm{d}`; `\boldsymbol` not `\vec`; Pauli `\hat{\sigma}^x`; eigenstate table.
3. **Concepts:** definitions, limits, approximations; no conflation (e.g. entanglement vs correlation).
4. **Homework:** “show that” true; setups physical; data sufficient; difficulty OK.
5. **Discussion:** debatable but resolvable with physics; tied to lecture.
6. **Projects:** real topics; feasible with AI + ~2 weeks; deliverables clear.

**Textbook:** David Tong, *Quantum Mechanics* (CUP). Standard checks: commutators, spectral decompositions, inequalities (Heisenberg, Bell), symmetries.

## Output format

```markdown
## Science Review: [notebook-name]

### Status: PASS | ERRORS FOUND

### Errors (must fix)
- Cell N: [wrong result / claim; give correction]

### Warnings (should fix)
- Cell N: [notation / clarity]

### Notes (optional)
- [improvement]
```

**Severity:** ERROR = wrong physics; WARNING = notation/clarity; NOTE = optional.

## References

- `rules/physics-conventions.md`, `rules/teaching-philosophy.md`, `rules/notebook-architecture.md`, `CLAUDE.md`
