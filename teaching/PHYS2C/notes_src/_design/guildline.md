# PHYS 2C Lecture Note Guideline

This document describes the typical structure and style of lecture notes to ensure consistency across the course. Use the prompt templates to generate content for each part.

---

## 0. Content Selection and Presentation Principles

In the AI era, lecture notes should emphasize **what humans uniquely need**—physical intuition, coherent worldview, and modeling skills—rather than computational techniques or formula memorization. Follow these principles when selecting and presenting material.

**Keep it minimal and concise.**

- Teach only the **essential key ideas** needed to understand the topic.
- Omit lengthy derivations; prefer the physical argument over the algebraic steps.
- When in doubt, cut. Students can use AI for details; the notes should anchor intuition.

**Prioritize fundamental principles and physical intuition.**

- Lead with **why** (physical meaning, causality) before **how** (formulas, procedures).
- Use analogies, diagrams, and concrete examples to build mental models.
- Highlight **unified principles** that connect topics (e.g., conservation laws, symmetry) rather than isolated facts.

**Build the knowledge system of physics.**

- Show how new material **connects** to prior topics and to broader physical structure.
- Prefer a few deep links over many shallow ones.
- Use comparison tables and "vs." framing to clarify conceptual boundaries.

**Develop abstraction and modeling skills.**

- Emphasize **model construction**: what is idealized, what is neglected, and why.
- Include "how to think about" guidance: identify variables, constraints, and objectives.
- Encourage problem definition and model choice, not just problem solving.

---

## 1. Typical Structure

Each lecture note notebook follows this structure:

| Cell | Content | Purpose |
|------|---------|---------|
| **Cell 0** | `# Section Title` | Title only (e.g., `# 32-1 Gauss' Law for Magnetic Fields`) |
| **Cell 1** | Prompts admonition | 4–5 AI-friendly prompts for students to try with LLM before class |
| **Cell 2** | Lecture Notes | Main content: subsections, equations, tables, figures, admonitions |
| **Cell 3** (Optional) | Discussions / Projects | Optional cell to provide additional material |


**Cell 1 (Prompts):** If the notebook contains a Learning Objectives section, use it to design 4–5 prompts. Each prompt should target one or more objectives so that students can use an AI tutor before class to reach those goals. After designing the prompts, remove the Learning Objectives section and replace it with a `:::{admonition} Prompts :class: tip` containing the prompts.

**Cell 2 (Lecture Notes):** Base the content on the textbook PDF. Apply the Content Selection and Presentation Principles (Section 0). If the notebook contains a Key Ideas section, use it as the structural backbone for the lecture notes. After writing the notes, remove the Key Ideas section; the lecture notes replace it.

Do not need to prepare **Discussions** or **Projects**, unless given explicit instruction. These sections should start with a new cell.

---

## 2. Lecture Notes Internal Structure

Within Cell 2, use this hierarchy:

```
## Lecture Notes

### Overview: [topic]
- Brief bullet summary
- Key comparison or contrast (if applicable)

:::{admonition} [Title]
:class: note
Clarification or physical intuition.
:::

---

### [Subsection 1]
- Main points with **bold** key terms
- Equations: display math for key formulas, inline for definitions

:::{admonition} [Title]
:class: note
...
:::

---

### [Subsection 2]
...

---

### Summary
- 3–5 bullet points recapping the main takeaways
```

**Conventions:**

- Use `---` (horizontal rule) to separate major subsections.
- Use `###` for subsection headings; keep them short and descriptive.
- Start with an **Overview** subsection presenting a clear big picture of the topics.
- End with a **Summary** subsection.
- Use bullet lists; prefer `- **Term**: definition` for key concepts.
- Use table to help summarize and compare.

---

## 3. Admonition Types and When to Use

```markdown
:::{admonition} [Title]
:class: [class]
[Content]
:::
```

Class options and suggested use cases:

| Class | Use for |
|-------|---------|
| `note` | Background, clarifications, physical intuition, paradox setup/resolution  |
| `important` | Core takeaways, definitions students must remember, essential conditions |
| `hint` | Nudge toward a solution without giving it away, "think about..." prompts |
| `seealso` | Exercises, examples, additional info, animations, videos, links to other sections or resources |
| `tip` | Pre-class prompts, best practices, general approach, step-by-step methods, shortcuts, study suggestions |
| `poll dropdown` | In-class clicker/poll questions (folded by default; students click to reveal) |
| `attention` | Things students often overlook, subtle distinctions worth noticing |
| `caution` | Sign conventions, common pitfalls, Lenz's law, minus signs, easy-to-make mistakes |
| `warning` | Stronger than caution: serious misconceptions, conceptual traps |
| `danger` | Incorrect approaches, formulas that do not apply here, "do not confuse with..." |
| `error` | Explicitly wrong statements, common exam mistakes, misconceptions to avoid |

---

## 4. Figures and Layout

- **Margin figure**: Use `:::{margin}` + `:::{figure}` for auxiliary diagrams (e.g., surface/loop setup). In margin, use `:width: 100%` so the image fits the sidebar.
- **Sidebar**: Use `:::{sidebar}` for floating content with background (e.g., physicist biography, further-reading links).
- **Side-by-side figures**: Use `::::{grid} 1 1 2 2` with `:::{grid-item-card}` for comparing two cases.
- **Figure options**: `:name:`, `:width: 80%` (or 100% in margin/cards), `:align: center`.
- **Math**: Use `$...$` for inline formula and ``$$\label{my_label} ...$$`` for numbered formula.

**Interactive elements:**

- **`:::{dropdown}`** — Collapsible content. Use for **worked examples**: show the problem first, hide the full derivation behind a click so students try on their own.
- **`:::{tab-set}`** — Tab switching. Use for comparing alternatives (e.g., theory vs. experiment, different solution methods).

**Jupyter widgets with Matplotlib:**

When building interactive widgets (e.g., `ipywidgets` sliders) that display or update matplotlib figures, follow these practices to avoid figure leakage and double-display bugs:

- **Display strategy**: Use `display(fig)` and `plt.close(fig)` instead of `plt.show()`. `plt.show()` displays *all* open figures and can leak figures from one cell into another. Use only one display path—never both `display(fig)` and `plt.show()`.
- **Avoid double figures**: `interactive_output` and `@interact` capture callback output; if the callback also calls `display(fig)`, you get two copies. Either let the decorator show the return value (return `fig`) or call `display(fig)` inside—not both. Add `plt.figure(); plt.close()` at cell end so the inline backend does not auto-display your figure again.
- **`@interact` vs manual wiring**: Use `@interact` for simple sliders when each callback creates a new figure. Use manual `observe` + `Output` when reusing a figure in place or when wiring Play + sliders + buttons together.
- **Output duplicates**: Use `clear_output(wait=True)` before every `display(fig)` in the callback. `wait=True` reduces flicker. This only clears the specific `Output` used in `with out:`.
- **`plt.ioff` / `plt.ion`**: Wrap visualization callbacks with `plt.ioff()` at the start and `plt.ion()` at the end to suppress auto-display during updates. Use `plt.ioff()` at cell start when reusing figures.
- **Figure reuse**: If a widget updates a figure in place, set `%config InlineBackend.close_figures = False` in the setup cell so the figure stays alive for callbacks.
- **Definition order**: Define `Output` widgets and control widgets *before* any callback that uses them. Callbacks close over names at call time—`NameError` occurs if `out` is referenced before it exists.
- **Simplify controls**: Prefer `@interact` when it fits; use one update function for all widgets; set `continuous_update=False` on sliders; group controls in `VBox`/`HBox`.
- **Re-run behavior**: Re-running a cell that creates widgets produces new instances; old ones may remain. Document that users should restart the kernel to reset, or design for a single persistent widget.

**Cross-referencing and footnotes:**

- **Labels**: Define with `(my-label)=` before a heading or `:name: my-label` on figures/equations.
- **References**: Use `` {ref}`my-label` `` to link (e.g., "see `` {ref}`sec-gauss` `` for the definition").
- **Footnotes**: Use `[^1]` for inline definitions without interrupting the flow; define the note with `[^1]: Your footnote text.`

---

## 5. Tables

Use Markdown tables for comparisons:

```markdown
| Electric | Magnetic |
|----------|----------|
| Flux $\propto$ enclosed charge | Flux = 0 always |
| Monopoles exist | Monopoles do not exist |
```

---

## 6. Math Conventions

- **Display math**: `$$\Phi_B = \oint_S \vec{B} \cdot d\vec{A} = 0$$`
- **Display math spacing**: `$$...$$` must have an **empty line before and after**; otherwise it will be interpreted as inline formula.
- **Labeled equations**: Use `$$ ... $$ (label)` for display math you may want to cite. Cite with `[](#label)`.

  ```markdown
  $$
  \rho = \frac{\Delta m}{\Delta V}
  $$ (eq-density)

  We can write [](#eq-density) in simplified form when ...
  ```

  It is good practice to label every displayed equation (even if it is not referenced), so it can be cited later if needed.
- **Inline math**: `$\Phi_E = \oint \vec{E} \cdot d\vec{A}$`
- **Subscripts**: `$i_{\text{enc}}$`, `$\Sigma_{\text{gap}}$`
- **Vertical bar**: `$\bigg\vert_\Sigma$` or `$\vert_\Sigma$` (use `\vert` in tables to avoid pipe conflicts)

---

## 7. Prompt Templates

Each lecture note starts with some prompts for the student to use, and to ask AI as a helpful tutor to help them achieving the learning objectives, understand key concepts, clear up confusions, or get examples. Use AI-assisted systems for pre-class work. AI provides immediate feedback on conceptual gaps. prompt should focus on fundamental principles, broad inter connection

```
:::{admonition} Prompts
:class: tip

- Explain [main physical idea]. How does this differ from [related concept]?
- What is [key structure]? Why [physical consequence]?
- Walk me through [calculation or procedure]. Then show how to [extension].
- I'm given [specific scenario]. How do I use [law/method] to find [quantity]? Can you work through an example?
- [Conceptual or comparison question about the topic]
:::
```
In the AI era, **prompt engineering** is not merely a technique but a tool for logical expression and scientific communication. Students must learn to make AI a helpful tutor rather than a cheating tool through precise instructions. Research shows that structured prompt frameworks significantly improve AI assistance in physics problems:

- **COSTAR framework**: By defining Context, Objective, Style, Tone, Audience, and Response format, students obtain highly tailored explanations of physical concepts.
- **RACE framework**: For designing physical experiments or course plans, clear delineation of Role, Action, Context, and Expectation effectively reduces AI hallucinations and improves output logic.
- **CREATE framework**: Emphasizing Character, Request, Examples, Additions, output Type, and Extras, suitable for generating complex physical visualization code or innovative thought experiments.


---

## 8. Checklist for New Lecture Notes

- [ ] Content follows Section 0 principles: minimal, fundamental, connected, modeling-focused
- [ ] Title cell: `# XX-Y [Topic]`
- [ ] Prompts cell: 4–5 prompts, `:class: tip`
- [ ] Lecture Notes: `## Lecture Notes`
- [ ] Overview subsection (if applicable)
- [ ] Subsections separated by `---`
- [ ] Key equations in display math
- [ ] Tables for comparisons
- [ ] Admonitions for clarifications, paradoxes, methods
- [ ] Summary subsection at end
- [ ] Figures: margin or grid as needed; dropdown/tab-set for examples or comparisons
- [ ] Math: use `\oint`, `\vert`, `\text{}` for subscripts
- [ ] Widgets (if any): use `display(fig)` + `plt.close(fig)`; define `Output` before callbacks; avoid `plt.show()`
