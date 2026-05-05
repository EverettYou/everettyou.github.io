# Lecture arc templates (subsection x.y.z)

**Law:** `rules/notebook-architecture.md`, `rules/content-style.md`, `rules/myst-references.md`, `rules/physics-conventions.md`, `rules/prompt-preview.md` (cell 1 criteria only).

Gold reference for **full** subsection shape: e.g. `notes_src/ch6_quantum-foundations/6-1-1-mixed-states.ipynb` (title → Prompts → Lecture Notes with Overview → `###` body → Summary / See Also).

## Cell 0 — title

```markdown
# 6.1.1 Mixed States
```

Use **dots** in the heading text; filename stays hyphenated (`6-1-1-mixed-states.ipynb`).

## Cell 1 — Prompts

Use **`skills/prompt-designer/TEMPLATES.md`**.

## Cell 2 — Lecture Notes skeleton

Common **current** patterns (mix as the lesson needs):

```markdown
## Lecture Notes

### Overview

[Motivation + roadmap prose—minimal display math per content-style.]

### [First technical heading]

:::{admonition} [Definition block title]
:class: important

[Definitions and numbered properties.]
:::

[Connecting prose.]

:::{admonition} [Worked comparison / short example]
:class: dropdown example

**Problem.** …

**Solution.** …
:::

:::{admonition} Poll: [short title]
:class: dropdown poll

(A) … (B) …
:::

### [Next heading]

:::{admonition} Derivation: [title]
:class: dropdown information

[Stepwise derivation—depth per `rules/derivation-quality.md`.]
:::

### Summary

- …

:::{admonition} See Also
:class: seealso

- [Visible title](../path/stem): gloss
:::
```

Closing **Summary / See Also** detail: **`skills/summary-designer/TEMPLATES.md`** + `rules/content-style.md` § Summary and See Also.

## Cell 3 — Homework

**`skills/homework-designer/TEMPLATES.md`**.

## New or heavily edited x.y.z — integration checklist

Use this when **bootstrapping** a subsection; cite **rule §** in audits, not as a second law.

- [ ] Content: minimal, principled, connected (`content-style.md`, `teaching-philosophy.md`)
- [ ] Cell 0: `# x.y.z Title` (dots)
- [ ] Cell 1: Prompts, `:class: tip`, 4–5 questions (`prompt-preview.md` + `prompt-designer/TEMPLATES.md`)
- [ ] Cell 2: `## Lecture Notes` → `### Overview` → body → `### Summary` (+ See Also when present)
- [ ] No `---`; no nested `:::`
- [ ] Key equations labeled; citations via `` {eq}`...` `` (`myst-references.md`)
- [ ] Figures use `:name:` when cross-referenced
- [ ] Cell 3: `## Homework` — `**N. Title.**` format per `homework-designer/TEMPLATES.md` + `content-style.md` § Homework Design
- [ ] Widgets: `display(fig)` / `plt.close(fig)`, `Output` before callbacks (`notebook-architecture.md`)
