# Derivation dropdown templates (PHYS130B)

**Law:** `rules/derivation-quality.md` (depth, `_refs/` alignment, anti-patterns) + `rules/physics-conventions.md` (notation in math).

Gold reference: `notes_src/ch6_quantum-foundations/6-1-1-mixed-states.ipynb` — e.g. `:::{admonition} Derivation: Purity Bounds` / `Derivation: Von Neumann Equation` with `:class: dropdown information`.

## MyST shell

```markdown
:::{admonition} Derivation: [Short title matching lecture]
:class: dropdown information

**Setup or case label:** …

$$
…
$$

**Next step label:** …

:::
```

## Internal layout (common in notes)

- Short **bold** labels before each mini-paragraph or equation (`**Pure state:**`, `**Lower bound:**`, …).
- Keep steps in **logical order**; no “obviously” skips—if a step is standard, still name the theorem or operation.
- Close the dropdown before starting an unrelated `###` section.

## QC

Before proposing replacement text: read **`derivation-quality.md`** end-to-end and the relevant **`_refs/`** section. This file is **presentation** only; the rule file is the checklist.
