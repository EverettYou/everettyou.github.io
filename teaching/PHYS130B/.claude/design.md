# Design Document — PHYS130B Lecture Notes

Notebook-author conventions overlap with the PHYS 2C lecture-note spec at [`../../PHYS2C/notes_src/_design/design.md`](../../PHYS2C/notes_src/_design/design.md) (repo path: `teaching/PHYS2C/notes_src/_design/design.md`). **This file wins** when rules conflict (notably: **never use `---` horizontal rules** in 130B builds; PHYS 2C uses them between subsections).

## Teaching Philosophy: Physics Education in the AI Era

### The Problem

It is 2026. Large language models can solve undergraduate physics homework at or above the level of most students. Students report frustration and loss of purpose — if AI solves their problems better than they can, what is the point of studying? Traditional teaching that focuses on knowledge transmission and problem-solving drill is no longer sufficient, because AI can do both. We must rethink what physics education is fundamentally for.

### Our Position

We embrace AI as a tool and encourage students to use it. Prohibiting AI is futile and counterproductive. Instead, we teach students *how to use AI effectively* — because only through sustained use can they learn its power and its limitations. The real educational goals are deeper than any homework problem:

1. **世界观 (Worldview)**: Physics education builds an internally consistent knowledge framework of principles. A student with a sound physical worldview can evaluate whether an AI-generated answer makes sense, spot hallucinations, appreciate elegance, and reject nonsense. This internalized value system — knowing what *should* be true based on deep understanding — is what makes humans valuable alongside AI. AI lacks this; it relies on prompt and context and can hallucinate confidently.

2. **方法论 (Scientific Method)**: Physics teaches that knowledge comes from interacting with the real world, not from thinking alone. Forming hypotheses, designing experiments (including numerical ones), analyzing data, reaching conclusions, abstracting to theory — these methods are what physics courses must teach, beyond how to solve the Schrödinger equation.

3. **Asking Good Questions**: In this era, asking the right question is more important than knowing the answer. A well-framed question maximizes what AI can deliver. But asking good questions requires both worldview (to know what's worth asking) and method (to know how to probe for truth).

### Course Strategy

#### 1. AI-Assisted Preview (预习)

Before each lecture, students use AI to preview the material. Each x.y.z lecture note contains a **Prompts** box (cell 1) with guiding questions designed to help students engage AI productively. Students submit a **preview report** (预习报告) — simply their chat history with AI about the lecture — before class starts. Graded on submission only, not content. Purpose: arrive at class already familiar with the landscape, with questions AI couldn't fully resolve.

#### 2. Homework (课后作业)

Each x.y.z subsection notebook includes a `## Homework` section after `## Lecture Notes`. Problems (5–10 per subsection) target specific skills: applying key concepts, formal derivations, understanding physical reasoning. Problems should be straightforward and well-grounded — directly testing one idea — not tediously numerical or combinatorially complex. Students are encouraged to work with AI. Graded on timely submission, not correctness (since AI assistance makes correctness grading meaningless). Late submissions receive decaying credit.

**Homework design principles:**
- Each problem targets one concept or skill
- Problems should be solvable by a student who understood the lecture, with or without AI
- Avoid problems that are just tedious computation or trick combinations of simple ideas
- Include a mix of: conceptual questions, short derivations, "show that" proofs, physical reasoning, simple applications
- The same problems will appear on the in-person final exam (with possible slight variations), so they must test *understanding* not just *procedure*

#### 3. In-Class Discussion (课堂讨论)

Students bring AI to class. The lecture notes include **Discussion** admonition boxes with deliberately controversial or conceptually challenging problems — not problems to solve, but conceptual barriers that benefit from collective debate. Students share AI outputs, identify disagreements, research literature together, and reach consensus. The professor moderates rather than lectures.

**Discussion problem design principles:**
- Must be **physics** questions with verifiable answers — NOT philosophical musings
- Good: presenting a paradox, clarifying a subtle concept, resolving a common misunderstanding, debating whether an approximation is valid, interpreting a surprising physical result
- Bad: "what does measurement really mean?", "is quantum mechanics complete?", vague interpretational questions with no concrete physical content
- Open-ended is fine, but the question must be grounded in specific physics
- Should provoke students to check AI answers against physical reasoning and primary sources
- Use `:class: dropdown warning` so discussion boxes are collapsed by default (don't interrupt lecture flow)

#### 4. Assessment

Two complementary approaches:

**Final Exam (in-person, no AI):** Problems are drawn from homework (with slight variations). Students who genuinely learned from working with AI — not just copy-pasted — will succeed. This tests whether the worldview and skills were internalized.

**Research Projects:** Each student completes two research projects with AI assistance during the quarter. Each x.y section notebook includes a `## Projects` section with 2–3 project ideas. Projects may involve writing simulation code, conducting a comprehensive literature study, investigating an open-ended problem, or writing a research report. Graded (potentially by AI) on correctness, novelty, and presentation quality. Students present to the class if enrollment permits.

**Project design principles:**
- Must be at the FRONTIER of physics research — topics like classical shadow tomography, measurement-induced entanglement transitions, quantum Zeno effect, surface codes, topological order, etc.
- NOT a big homework problem — a genuine research investigation requiring literature survey, computational exploration, and scientific writing
- AI can help with implementation (code, writing, calculations) but the student must drive the scientific inquiry
- Each section has exactly ONE project, designed to comprehensively cover the section's themes
- Each project should be achievable in ~2 weeks with AI assistance
- Output: written research report (and oral presentation if class size allows)

#### 5. Role of the Lecture Notes

In the AI era, lecture notes are no longer the primary narrative interface to students — AI is. Each student has a different background and thinking style; AI can adapt its explanation to each individual, something no single set of notes can do. Starting next quarter, the university provides an AI agent per course that reads the notes and answers student questions.

Therefore, the lecture notes serve a different purpose: they are the **authoritative reference** that pins down definitions, concepts, key results, and the logical structure of the course. They should be:

- **Clean and inviting**: Key definitions, theorems, and results are prominently displayed; derivations and extended discussions are in collapsible boxes
- **Structurally precise**: The hierarchy (chapter → section → subsection) defines the knowledge graph
- **AI-friendly**: Written so that an AI reading the notes can accurately teach from them
- **Not a specific narrative**: The notes don't try to tell one story for all students; they provide the skeleton that AI can flesh out differently for each learner

## Content selection and presentation

In the AI era, emphasize **what humans uniquely need**—physical intuition, a coherent worldview, and modeling skills—rather than computational drill or formula memorization.

**Keep it minimal and concise.** Teach only **essential** ideas; omit lengthy derivations in favor of physical argument. When in doubt, cut; students can use AI for details while the notes anchor intuition.

**Prioritize principles and intuition.** Lead with **why** (meaning, causality) before **how** (formulas, procedures). Use analogies, figures, and examples. Highlight **unifying** structure (symmetry, conservation, limits) rather than isolated facts.

**Build the knowledge graph.** Connect new material to prior topics and the broader course. Prefer a few deep links over many shallow ones. Use comparison tables and “vs.” framing where helpful.

**Modeling and abstraction.** Say what is idealized, what is neglected, and why. Encourage defining the problem and choosing a model, not only executing calculations.

### Admonition classes (extended for AI-era pedagogy)

| Class | Use |
|-------|-----|
| `tip` | **Prompts** — guiding questions for AI-assisted preview (cell 1 of x.y.z) |
| `example` | Worked examples with detailed calculations |
| `note` | Background, clarifications, physical intuition, paradox setup/resolution |
| `important` | Core definitions, theorems, fundamental equations students must retain |
| `hint` | Nudge toward a solution without giving it away; “think about…” prompts |
| `seealso` | Exercises, extra examples, animations, links to other sections or resources |
| `attention` | Easy-to-miss subtleties and important distinctions |
| `caution` | Sign conventions, common pitfalls, easy algebraic mistakes |
| `warning` | **Discussion** — controversial or subtle **physics** questions for in-class debate (see Course Strategy); stronger conceptual traps than `caution` |
| `danger` | Wrong approaches or formulas that do not apply in this context |
| `error` | Explicit misconceptions, wrong statements, frequent exam mistakes |
| `poll dropdown` | Optional: in-class poll/clicker prompts (collapsed by default) |

**Discussion boxes:** Per Course Strategy §3, discussion prompts should be **collapsed by default** so they do not interrupt the lecture flow. Use the project’s established MyST pattern (e.g. `dropdown` combined with `warning`). **Do not nest** one `:::{admonition}` inside another `:::{admonition}`—nested `:::` breaks rendering (see MyST pitfalls); flatten inner content or use a single admonition with a title that signals “Discussion.”

## Notebook Architecture

### File Naming

- Chapter directories: `ch{N}_{topic}/` (e.g., `ch1_qubit/`, `ch4_phase-and-gauge/`)
- Section parents: `{ch}-{sec}-{topic}.ipynb` (e.g., `6-1-density-matrix.ipynb`)
- Subsections: `{ch}-{sec}-{sub}-{topic}.ipynb` (e.g., `6-1-1-mixed-states.ipynb`)
- Chapter index: `ch{N}_{topic}/index.md`
- Titles inside use dots: `# 6.1 Density Matrix`, `# 6.1.1 Mixed States`

### Cell Structure

**Section parent notebooks (x.y)** — 3 cells:

| Cell | Content |
|------|---------|
| 0 | `# x.y Section Title` |
| 1 | `## Overview` → leading paragraph → `### Topics` table → `### Key Concepts` → `### Learning Objectives` |
| 2 | `## Projects` → `### Project 1: ...` → `### Project 2: ...` etc. |

**Subsection notebooks (x.y.z)** — 4 cells:

| Cell | Content |
|------|---------|
| 0 | `# x.y.z Subsection Title` |
| 1 | Prompts admonition (tip box with guiding questions for AI-assisted preview) |
| 2 | `## Lecture Notes` followed by all content (`###` subsections, with Discussion boxes inline) |
| 3 | `## Homework` with 5–10 problems |

**Chapter index pages** — Markdown (`.md`), not notebooks:
- Course title heading
- `{list-table}` with Sec / Topic / Textbook columns
- Glossary admonition with key terms

### Section Parent Structure (x.y level)

All 21 section parents follow this structure:

**Cell 1 (Overview):**
```
## Overview
A motivating paragraph introducing the section's theme, its physical significance,
and what students will gain from studying it.

### Topics
{list-table} with Sec / Topic / Keywords columns

### Key Concepts
Bullet list of 4–6 key ideas, each with brief math notation.

### Learning Objectives
Bullet list of 3–4 concrete skills students should gain.
```

**Cell 2 (Projects):**
```
## Project

### [Research-Level Title]
A single, carefully designed research project at the frontier of physics.
Should comprehensively cover the section's themes.
Specify: objective, background, suggested approach, expected deliverable.
Must require literature survey, computational exploration, and scientific writing.
```

**Rules:**
- No Prompts boxes at x.y level (only at x.y.z level)
- No "Brief Introduction" or "Structure of Chapter" headings
- Topics table must link subsection filenames, not URLs
- `## Overview` comes first, `## Projects` comes last
- Each section has exactly ONE research-level project (not 2-3)
- Projects should require genuine scientific inquiry at the frontier, not just calculation

### Subsection content structure (x.y.z level)

Within the `## Lecture Notes` cell (cell 2), use a clear arc (adapted from PHYS 2C, **without** horizontal rules):

- Start with **`### Overview`** only (do not write `### Overview: [repeated title]`—the H1 already names the page): short bullets and, if useful, one key contrast.
- **Body:** `###` subsections for each conceptual unit; key definitions and results stay **visible**; extended derivations go in **`:::{dropdown}`** (worked examples: state the problem, hide the solution behind a click).
- **`:::{tab-set}` / tabs:** Use to compare alternatives (e.g. Schrödinger vs Heisenberg picture, two limits).
- **Discussion** (`warning`) inline where debate helps; **application** blocks in `example` admonitions (see also “Application Sections → Example Boxes” below).
- End with **`### Summary`**: 3–5 bullets recapping takeaways.

**Do not use `---` between sections** (Jupyter Book / docutils error in this project). Separate major blocks with blank lines and heading level only.

**Figures and layout (when useful):**

- **Margin figure:** `:::{margin}` + `:::{figure}` for auxiliary diagrams; in margin use `:width: 100%`.
- **Sidebar:** `:::{sidebar}` for asides (biography, further reading).
- **Side-by-side:** `::::{grid} 1 1 2 2` with `:::{grid-item-card}` for comparisons.
- **Figure options:** `:name:`, `:width: 80%` (or `100%` in margin/cards), `:align: center`.

**Jupyter widgets with Matplotlib** (interactive demos):

- Prefer `display(fig)` and `plt.close(fig)` over `plt.show()` (avoids leaking figures across cells). Never both `display(fig)` and `plt.show()`.
- With `interactive_output` / `@interact`: either return `fig` **or** call `display(fig)` inside the callback—not both; end cells with `plt.figure(); plt.close()` if needed to suppress duplicate inline output.
- Use `@interact` when each update creates a new figure; use manual `observe` + `Output` when reusing one figure or wiring Play + sliders + buttons.
- In callbacks: `clear_output(wait=True)` before each `display(fig)` inside the target `Output`.
- Wrap update callbacks with `plt.ioff()` … `plt.ion()` when suppressing spurious draws; for in-place figure updates, `%config InlineBackend.close_figures = False` in setup.
- Define `Output` and control widgets **before** callbacks that reference them.
- Prefer one update function, `continuous_update=False` on sliders, controls in `VBox`/`HBox`; document kernel restart if re-running widget cells leaves stale UI.

The `## Homework` cell (cell 3) follows this format:
```
## Homework

**1.** [Problem statement targeting one specific concept or skill.]

**2.** [Another problem...]

...
```

**Homework numbering:** Problems are numbered `1, 2, 3, ...` within each subsection. Cross-references use format `HW x.y.z.k` (e.g., HW 1.1.1.3 = problem 3 of §1.1.1).

## MyST Markdown Conventions

Admonition classes are summarized in **Content selection → Admonition classes** above.

Syntax:
```
:::{admonition} Title Here
:class: example

Content here.
:::
```

### Things That Break Jupyter Book

- **`---` horizontal rules** → `docutils.utils.AssertionError`. Never use them.
- **Nested admonitions** → inner `:::` blocks inside outer `:::` break rendering. Flatten inner ones to bold text.
- **Missing blank lines** before/after `:::` blocks, `$$` math, `{list-table}` → parse errors.
- **`$$` display math MUST have blank lines above and below** — without them, the parser treats `$$` as inline math delimiters, merging the equation with adjacent text and producing stray `$` signs. This is the most common rendering bug.
- **`myst_footnote_transition: false`** is set in `_config.yml` to work around a related docutils bug.

### Equation labels and citations

Display math with labels (note the blank lines):
```

$$
E = mc^2
$$ (eq-section-name)

```

**Cross-references:** Prefer MyST `` {eq}`eq-section-name` ``. The form `Eq. [](#eq-section-name)` is acceptable if you need prose “Eq. (…)” style and the label is defined as `$$ ... $$ (eq-section-name)` on its own lines.

Label every displayed equation that might be cited later; label convention: `eq-{topic}-{description}` (e.g., `eq-mixed-purity`, `eq-6-1-pure-density`).

**LaTeX inside notebook JSON:** Do not split TeX across JSON strings in a way that inserts a real newline inside `\nabla`, `\nu`, `\partial`, etc.—the sequence `\n` is a newline, not part of the command.

### Application Sections → Example Boxes

Sections titled `### Application: ...` that contain detailed calculations demonstrating theory should be wrapped in example admonition boxes, not left as regular subsections. Same for `#### Application at ...`.

## Math Notation Conventions

**Display math:** `$$...$$` must have **blank lines above and below** (see “Things That Break Jupyter Book”).

**Inline vs display:** Use `$...$` inline; reserve `$$...$$` for key displayed results.

**Subscripts and norms:** Use `$i_{\text{enc}}$`, `$\Sigma_{\text{gap}}$` where words appear in subscripts. For evaluation bars or norms in tables, prefer `\vert` (e.g. `$\bigg\vert_\Sigma$`) to avoid clashing with Markdown pipe `|`.

### Vectors and Operators

- **Vectors**: use `\boldsymbol` (not `\vec`) for all vector quantities, e.g. `\boldsymbol{S}` for spin, `\boldsymbol{n}` for Bloch vector, `\boldsymbol{r}` for position, `\boldsymbol{p}` for momentum, `\boldsymbol{B}` for magnetic field.
- **Operators**: use `\hat{...}` for all quantum operators, e.g. `\hat{H}` for Hamiltonian, `\hat{p}` for momentum operator, `\hat{O}` for a generic observable.
- **Pauli operators**: Pauli matrices acting as operators use SUPERSCRIPT indices: `\hat{\sigma}^x`, `\hat{\sigma}^y`, `\hat{\sigma}^z`. The vectorized Pauli operator is `\hat{\boldsymbol{\sigma}} = (\hat{\sigma}^x, \hat{\sigma}^y, \hat{\sigma}^z)`.
- **Pauli matrices as matrices**: When referring to the explicit 2×2 matrices (not as operators), plain `\sigma^x`, `\sigma^y`, `\sigma^z` with superscript indices.

### Upright Symbols for Special Constants and Operators

- **Imaginary unit**: always `\mathrm{i}` (e.g., `\mathrm{e}^{\mathrm{i}\theta}`, not `e^{i\theta}`)
- **Euler's number / exponential base**: always `\mathrm{e}` (e.g., `\mathrm{e}^{-\beta E}`, not `e^{-\beta E}`)
- **Differential operator**: always `\mathrm{d}` (e.g., `\mathrm{d}x`, `\frac{\mathrm{d}}{\mathrm{d}t}`, not `dx` or `\frac{d}{dt}`)

These follow the ISO 80000-2 convention: constants and operators that are not variables are set in upright (roman) type to distinguish them from italic variables.

## Eigenstate Notation

Consistent across all notebooks:

| Observable | Eigenstates |
|-----------|-------------|
| X (σ_x) | $\|+\rangle$, $\|-\rangle$ |
| Y (σ_y) | $\|\mathrm{i}\rangle$, $\|\bar{\mathrm{i}}\rangle$ |
| Z (σ_z) — qubit context | $\|0\rangle$, $\|1\rangle$ |
| Z (σ_z) — spin context | $\|\uparrow\rangle$, $\|\downarrow\rangle$ |

## Cross-Reference Conventions

- Section references in prose: `§6.1.2` (with section symbol and dots)
- File links in MyST: `[Topic Name](6-1-2-topic-name)` (dashes, no extension)
- When reordering sections, use two-pass placeholder replacement to avoid circular substitutions
- **Arbitrary targets:** Define labels with `(my-label)=` before a heading, or `:name: my-label` on figures/equations. Link with `` {ref}`my-label` ``.
- **Figures:** Prefer `` {numref}`fig-label` `` (e.g. “see `` {numref}`fig-bloch` ``”) so the caption renders correctly. Avoid `Fig. [](#fig-label)` with empty link text when the caption contains math—Sphinx may show raw LaTeX in the link.
- **Footnotes:** `[^1]` in text; `[^1]: Footnote text.` on its own line for the definition.

## Content style

- Use bullet points within admonition boxes for key takeaways
- Break large text blocks into digestible paragraphs (no wall-of-text)
- Each `###` section within Lecture Notes should be a self-contained conceptual unit
- End subsection notebooks with **`### Summary`** and 3–5 recap bullets (see Subsection content structure)

### Prompt templates (for cell 1)

Students use the **Prompts** box for AI-assisted preview. Questions should read like a professor’s study guide—natural and specific—not like API boilerplate (see `CLAUDE.md` Workstream 1). A useful pattern:

```
:::{admonition} Prompts
:class: tip

- Explain [main idea]. How does it differ from [related concept]?
- What is [structure or object]? Why does [consequence] follow?
- Walk me through [short derivation or argument]. What changes if [variation]?
- Given [scenario], how do I use [method] to find [quantity]? Work a concrete example.
- [Conceptual or comparison question that may stress-test AI answers]
:::
```

Optional **student-facing** frameworks for structuring their own chats (from broader AI-literacy practice): **COSTAR** (Context, Objective, Style, Tone, Audience, Response format), **RACE** (Role, Action, Context, Expectation), **CREATE** (Character, Request, Examples, Additions, Type, Extras).

### Checklist (new or heavily edited x.y.z notebooks)

- [ ] Content matches **Content selection and presentation** (minimal, principled, connected)
- [ ] Cell 0: `# x.y.z Title` (dots in title)
- [ ] Cell 1: Prompts admonition, `:class: tip`, 4–5 questions
- [ ] Cell 2: `## Lecture Notes` → `### Overview` (heading only) → body → `### Summary`
- [ ] No `---` horizontal rules; no nested `:::` admonitions
- [ ] Key equations labeled; citations via `` {eq}`...` ``
- [ ] Tables where they clarify comparisons; figures use `:name:` when cross-referenced
- [ ] Cell 3: `## Homework` with numbered problems
- [ ] Widgets (if any): `display(fig)` / `plt.close(fig)`, `Output` defined before callbacks, no `plt.show()`
