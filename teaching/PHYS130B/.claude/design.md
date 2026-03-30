# Design Document — PHYS130B Lecture Notes

This file covers teaching philosophy, course strategy, and authoring conventions NOT found in the modular rule files. For quick reference on specific topics, see:
- `rules/content-style.md` — cell structure, admonition table, content philosophy, homework/project format
- `rules/physics-conventions.md` — LaTeX notation, eigenstate table, display math rules
- `rules/notebook-editing.md` — safe ipynb editing, banned tools, validation

Conventions overlap with PHYS 2C at `../../PHYS2C/notes_src/_design/design.md`. **This file wins** when rules conflict (notably: **never use `---` horizontal rules** in 130B).

## Teaching Philosophy: Physics Education in the AI Era

### The Problem

It is 2026. LLMs solve undergraduate physics homework at or above student level. Traditional teaching focused on knowledge transmission and problem-solving drill is no longer sufficient. We must rethink what physics education is for.

### Our Position

We embrace AI and encourage students to use it. The real educational goals:

1. **世界观 (Worldview)**: An internally consistent knowledge framework. A student with sound physical worldview can evaluate AI answers, spot hallucinations, appreciate elegance, reject nonsense. This internalized value system is what makes humans valuable alongside AI.

2. **方法论 (Scientific Method)**: Knowledge comes from interacting with the real world. Forming hypotheses, designing experiments, analyzing data, abstracting to theory — these methods are what physics courses must teach beyond solving the Schrödinger equation.

3. **Asking Good Questions**: A well-framed question maximizes what AI can deliver. Good questions require both worldview and method.

### Course Strategy

**1. AI-Assisted Preview (预习):** Students use AI to preview material via the Prompts box (cell 1). Submit preview report (chat history with AI) before class. Graded on submission only.

**2. Homework (课后作业):** 5–10 problems per subsection. Students work with AI. Graded on timely submission, not correctness. Late submissions get decaying credit. Same problems appear on final exam.

**3. In-Class Discussion (课堂讨论):** Students bring AI to class. Discussion boxes present conceptual barriers for collective debate. Professor moderates.

**4. Assessment:**
- **Final Exam** (in-person, no AI): Problems drawn from homework with slight variations. Tests whether worldview and skills were internalized.
- **Research Projects**: Two per student per quarter. Each x.y section has one project. Graded on correctness, novelty, presentation. Students present if enrollment permits.

**5. Role of the Lecture Notes:** Notes are the **authoritative reference** (not the narrative interface — AI is). They pin down definitions, concepts, key results, and logical structure. The knowledge graph skeleton that AI teaches from.

## Notebook Architecture (unique details)

### File Naming

- Chapter dirs: `ch{N}_{topic}/` (e.g., `ch1_qubit/`)
- Section parents: `{ch}-{sec}-{topic}.ipynb` (e.g., `6-1-density-matrix.ipynb`)
- Subsections: `{ch}-{sec}-{sub}-{topic}.ipynb` (e.g., `6-1-1-mixed-states.ipynb`)
- Chapter index: `ch{N}_{topic}/index.md`
- Titles use dots: `# 6.1 Density Matrix`, `# 6.1.1 Mixed States`

### Chapter Index Pages

Markdown (`.md`), not notebooks. Contains: course title heading, `{list-table}` with Sec / Topic / Textbook columns, glossary admonition with key terms.

### Section Parent Rules

- No Prompts boxes at x.y level (only x.y.z)
- No "Brief Introduction" or "Structure of Chapter" headings
- Topics table links subsection filenames, not URLs
- `## Overview` first, `## Project` last

### Subsection Content Arc

Within `## Lecture Notes` (cell 2):
- `### Overview` (heading only, no repeated title)
- Body: `###` subsections; key results visible; derivations in `:::{dropdown}`
- `:::{tab-set}`: compare alternatives (e.g., Schrödinger vs Heisenberg picture)
- Discussion (`dropdown tip`) inline where debate helps
- Application blocks in `example` admonitions
- `### Summary`: 3–5 recap bullets

### Figures and Layout

- **Margin figure:** `:::{margin}` + `:::{figure}`, use `:width: 100%`
- **Sidebar:** `:::{sidebar}` for asides (biography, further reading)
- **Side-by-side:** `::::{grid} 1 1 2 2` with `:::{grid-item-card}`
- **Figure options:** `:name:`, `:width: 80%` (or `100%` in margin/cards), `:align: center`

### Jupyter Widgets with Matplotlib

- `display(fig)` + `plt.close(fig)` (never `plt.show()`)
- `@interact`: return `fig` OR `display(fig)` in callback — not both
- `observe` + `Output`: for reusing one figure or wiring Play + sliders
- `clear_output(wait=True)` before `display(fig)` in target `Output`
- `plt.ioff()` / `plt.ion()` to suppress spurious draws
- Define `Output` and controls **before** callbacks that reference them
- `continuous_update=False` on sliders; document kernel restart for stale UI

## MyST Pitfalls

- **`---`** → docutils crash. Never use.
- **Nested `:::`** → inner admonitions break. Flatten to bold text.
- **Missing blank lines** before/after `:::`, `$$`, `{list-table}` → parse errors.
- **`$$` needs blank lines above and below** — without them, parser treats as inline math.
- **`myst_footnote_transition: false`** in `_config.yml` prevents a docutils crash. Do not remove.

### Equation Labels

```
$$
E = mc^2
$$ (eq-section-name)
```

No blank lines *within* `$$...$$`, only outside. Prefer `` {eq}`eq-section-name` `` for cross-refs. Label convention: `eq-{topic}-{description}`.

## Cross-Reference Conventions

- Section refs in prose: `§6.1.2`
- File links: `[Topic Name](6-1-2-topic-name)` (dashes, no extension)
- Section reordering: two-pass placeholder replacement
- **Arbitrary targets:** `(my-label)=` before heading, or `:name: my-label` on figures/equations. Link with `` {ref}`my-label` ``
- **Figures:** `` {numref}`fig-label` `` (not `Fig. [](#fig-label)` — Sphinx may show raw LaTeX)
- **Footnotes:** `[^1]` in text; `[^1]: Footnote text.` on own line

## Prompt Templates

```
:::{admonition} Prompts
:class: tip

- Explain [main idea]. How does it differ from [related concept]?
- What is [structure]? Why does [consequence] follow?
- Walk me through [derivation]. What changes if [variation]?
- Given [scenario], use [method] to find [quantity]. Work a concrete example.
- [Conceptual question that may stress-test AI answers]
:::
```

Student-facing prompt frameworks: **COSTAR** (Context, Objective, Style, Tone, Audience, Response), **RACE** (Role, Action, Context, Expectation), **CREATE** (Character, Request, Examples, Additions, Type, Extras).

## Checklist (new or heavily edited x.y.z notebooks)

- [ ] Content: minimal, principled, connected
- [ ] Cell 0: `# x.y.z Title` (dots)
- [ ] Cell 1: Prompts, `:class: tip`, 4–5 questions
- [ ] Cell 2: `## Lecture Notes` → `### Overview` → body → `### Summary`
- [ ] No `---`; no nested `:::`
- [ ] Key equations labeled; citations via `` {eq}`...` ``
- [ ] Figures use `:name:` when cross-referenced
- [ ] Cell 3: `## Homework` with numbered problems
- [ ] Widgets: `display(fig)` / `plt.close(fig)`, `Output` before callbacks
