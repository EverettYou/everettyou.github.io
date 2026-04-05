# /project:improve-unit — Improve a Unit's Notebooks

Rewrite all notebooks in a unit (x.y) to follow the storyline narrative in `outline.md`,
applying the style and conventions defined in the rules files.

## Usage

```
/project:improve-unit <unit>
```

Example: `/project:improve-unit 1.2`

## Prerequisites

Read these before starting:
- `.claude/rules/content-style.md` — admonition classes, cell structure, banned patterns
- `.claude/rules/physics-conventions.md` — notation conventions
- `.claude/rules/notebook-editing.md` — safe editing method (Bash only), validation checklist
- `.claude/design.md` — teaching philosophy
- `outline.md` — find the section for this unit; this is the narrative blueprint

## Procedure

### 1. Read current notebooks

Read all x.y.z subsection notebooks and the x.y parent for this unit. Note cell count, existing content to reuse, and any title changes specified in `outline.md`.

### 2. Rewrite each x.y.z subsection notebook

Follow the outline narrative. Apply the cell structure from `content-style.md`:
- Cell 0: `# x.y.z Title`
- Cell 1: 4–5 Prompts (`:class: tip`)
- Cell 2: `## Lecture Notes` → `### Overview` → body sections → `### Summary`, with inline Discussion boxes (`:class: dropdown tip`)
- Cell 3: `## Homework` — 5–10 problems

Keep and reuse correct existing content. Rewrite prose, don't invent new physics.

### 3. Edit via Bash + Python only

Follow the method in `notebook-editing.md`. Key points:
- Use `text_to_source()` for cell source arrays
- Never split TeX commands where `\n` occurs inside `\nabla`, `\nu`, `\partial` etc.

### 4. Review Prompts, Homework, and unit Overview

After subsection rewrites are done:

**a. Prompts (cell 1):** Verify each question previews something actually covered in the rewritten lecture. Revise any stale or missing prompts. Aim for 4–5 questions in narrative order.

**b. Homework (cell 3):** Verify every problem targets a concept taught in the rewritten lecture. Remove/rewrite stale problems, add problems for new topics. Check sequential numbering.

**c. Unit parent overview (x.y, cell 1):** Update to reflect rewritten subsections:
- Motivating paragraph (2–3 sentences)
- `### Lessons` table: `Lesson | Title | Core Question` — one row per x.y.z
- `### Key Concepts`: 5–8 essential terms
- `### Learning Objectives`: 3–5 "Students will be able to..." statements
- Do NOT edit the parent's cell 2 (`## Project`)

### 5. Rename files and update TOC if any title changed

If a notebook's title changed per the outline:
- Rename `.ipynb` file: `x-y-z-hyphenated-title.ipynb` (lowercase, hyphens)
- Update `_toc.yml`, `index.md`, chapter `index.md`, parent notebook Lessons table
- `grep -r "old-filename" notes_src/` to catch stale cross-references

If no title changed, skip this step.

### 6. Validate

Run the validation checks from `notebook-editing.md` on every modified notebook.

### 7. Update `progress.md`

Record what was done under Workstream 5.

## Dispatch Strategy (for the manager agent)

For a unit with three subsections, dispatch **three parallel agents** — one per notebook — for steps 2–3. Each agent receives the outline content for its notebook and the current notebook content.

Then handle step 4 (review pass) and step 5 (renames/TOC) in a **single follow-up pass** after all rewrites are confirmed complete.

## Structural Changes: Outline vs Current Files

The outline may differ from current file structure. Key changes to watch for:

### Ch3 — Title renames
- 3.1.1: "Classical to Quantum" → "Geometric Optics"
- 3.1.3: "Quantum Mechanics as Optics" → "Particle-Wave Unification"
- 3.2.2 and 3.2.3: swapped order (Schrödinger Equation now 3.2.2, Free Particle Propagator now 3.2.3)

### Ch4 — Restructured from 5 units to 4 units
- 4.1: lesson titles changed (4.1.1 → "Gauge Principle", 4.1.2 → "Electromagnetic Coupling", 4.1.3 → "Gauge Invariance")
- 4.2: completely new unit "Berry Phase" replacing old "Flux Ring"
  - 4.2.1 Berry Phase (new), 4.2.2 Aharonov-Bohm Effect, 4.2.3 Flux Ring
  - Old files: 4-2-1-aharonov-bohm-effect, 4-2-2-flux-quantization, 4-2-3-gauge-invariance
- 4.3: Landau Level — lessons renamed (4.3.1 adds Hall effect content)
- 4.4: Spin and Monopole — 4.4.1 renamed to "Classical Spin"
- Old 4.5 Berry Phase unit REMOVED — content absorbed into new 4.2
  - Old files 4-5-*.ipynb need archiving/deletion; update _toc.yml, index.md

### Ch6 — Content reshuffled
- 6.1.2: "Partial Trace" → "Entropy" (partial trace → 6.2.1)
- 6.1.3: "Entropy" → "Quantum Statistics" (new: Bose-Einstein/Fermi-Dirac)
- 6.2.1: "Composite Systems" now includes partial trace content

When working on these chapters, handle file renames, _toc.yml updates, index.md updates, and cross-reference fixes as part of step 5.
