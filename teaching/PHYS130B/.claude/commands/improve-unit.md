# /project:improve-unit — Improve a Unit's Notebooks

Rewrite all notebooks in a unit (x.y) to follow the storyline narrative outlined in `outline.md`,
applying consistent style: concise language, visible key results, hidden derivations, structured layout.

## Usage

```
/project:improve-unit <unit>
```

Example: `/project:improve-unit 1.2`

## Style Principles (apply to every notebook)

- **Concise and accurate language** — every sentence earns its place; cut padding and repetition
- **Key definitions and results go in `important` boxes** — always visible, never hidden
- **Long derivations go in `dropdown` boxes** — collapsed by default to keep flow clean
- **Avoid wall-of-text** — break content into item lists, tables, and named boxes
- **Keep and reuse useful existing content** — rewrite prose, preserve correct physics
- **Remove digressions** — stick to the narrative the outline specifies
- **Discussion boxes** use `:class: dropdown tip` (never `dropdown warning`)
- **Physics conventions**: `\boldsymbol` for vectors, `\hat{}` for operators, `\mathrm{i/e/d}` for constants, `\vert` for kets/bras

## Instructions

1. **Read companion docs first:**
   - `.claude/rules/content-style.md` — admonition classes, cell structure, banned patterns
   - `.claude/rules/physics-conventions.md` — notation conventions
   - `.claude/rules/notebook-editing.md` — safe editing (Bash only, never NotebookEdit/Edit/Write)
   - `.claude/design.md` — teaching philosophy
   - `outline.md` — find the section for this unit; this is the narrative blueprint

2. **Read current notebooks** for all x.y.z subsections and the x.y parent:
   - Use `Read` tool to inspect each notebook's current content
   - Note cell count, what content already exists (reuse the good parts), what to remove
   - Check if the outline specifies a different title/topic than the current notebook
     - If so, this notebook needs a title change AND file rename (handled in step 6)

3. **Rewrite each x.y.z subsection notebook** following the outline narrative for this unit:
   - Cell 0: `# x.y.z Title` — concise, descriptive; if the title changes, note it for step 6
   - Cell 1: 4–5 Prompts (`:class: tip`) — guiding questions that preview the narrative
   - Cell 2: `## Lecture Notes` → `### Overview` → body sections → `### Summary`
   - Cell 3: `## Homework` — 5–10 problems per design spec (alignment checked in step 5b)
   - Inline `:::{admonition} Discussion\n:class: dropdown tip` boxes in cell 2

4. **Edit via Bash Python only** (Edit/Write/NotebookEdit are ALL denied):
   ```python
   import json
   def text_to_source(text):
       lines = text.split('\n')
       source = []
       for i, line in enumerate(lines):
           if i < len(lines) - 1:
               source.append(line + '\n')
           else:
               if line:
                   source.append(line)
       return source

   with open(path) as f:
       nb = json.load(f)
   nb['cells'][i]['source'] = text_to_source(new_content)
   with open(path, 'w') as f:
       json.dump(nb, f, indent=1, ensure_ascii=False)
   ```

   **LaTeX safety**: Never split TeX commands across JSON strings where `\n` occurs
   inside commands like `\nabla`, `\nu`, `\partial`. Use raw strings or double backslashes.

5. **Review Prompts, Homework, and unit Overview** — after subsection rewrites are done:

   **a. Review each notebook's Prompts (cell 1):**
   - Re-read the finished cell 2 lecture content
   - Verify each prompt question accurately previews something actually covered in the lecture
   - Revise any prompt that asks about content that was removed, or that misses a key theme now present
   - Prompts should follow the narrative arc of the notebook, roughly in order of coverage
   - Aim for 4–5 questions; each should be answerable by reading the notebook

   **b. Review each notebook's Homework (cell 3):**
   - Re-read the finished cell 2 lecture content
   - Verify every problem targets a concept, result, or technique that is actually taught in the new lecture
   - Remove or rewrite any problem whose prerequisite content was removed or substantially changed
   - Add problems for important new topics that are not yet tested
   - Check problem numbering is sequential (1., 2., 3., …) and each problem has a clear single focus
   - Cross-reference format: `HW x.y.z.k` — ensure any internal cross-references are still valid

   **c. Update the x.y parent notebook (section Overview):**
   - Find the x.y index notebook (e.g., `notes_src/ch1_qubit/1-2-measurement.ipynb`)
   - Its cell 1 has: `## Overview` → motivating paragraph → `### Lessons` table → `### Key Concepts` → `### Learning Objectives`
   - Update each part to reflect what the rewritten subsections actually contain:
     - **Motivating paragraph**: 2–3 sentences capturing the unit's core narrative arc
     - **Lessons table**: columns `Lesson | Title | Core Question` — one row per x.y.z, titles and questions aligned with new content
     - **Key Concepts**: bullet list of 5–8 essential terms/ideas now covered across the unit
     - **Learning Objectives**: 3–5 "Students will be able to..." statements matching the new lecture content
   - Do NOT edit the x.y parent's cell 2 (`## Project`) unless instructed

6. **Rename files and update TOC/references if any notebook title changed:**
   - If a notebook's `# x.y.z Title` was changed, rename the `.ipynb` file to match:
     - Convention: `x-y-z-hyphenated-title.ipynb` (lowercase, spaces → hyphens, drop punctuation)
     - Use `mv` in Bash to rename the file
   - Update `notes_src/_toc.yml` — find the old filename entry and replace with the new one
   - Update `notes_src/index.md` — the master TOC table links notebooks by filename
   - Update the chapter landing page `notes_src/ch{N}_*/index.md` — section table links
   - Update the x.y parent notebook's Lessons table (cell 1) — the `[Title](filename)` links
   - Search for any other cross-references to the old filename:
     ```bash
     grep -r "old-filename" notes_src/ --include="*.ipynb" --include="*.md" --include="*.yml"
     ```
   - If no title changed, skip this step entirely

7. **Validate after editing:**
   ```python
   import json
   for path in notebook_paths:
       with open(path) as f:
           nb = json.load(f)
       for i, cell in enumerate(nb['cells']):
           for j, line in enumerate(cell['source'][:-1]):
               assert line.endswith('\n'), f"Cell {i} line {j} missing \\n"
           assert all(len(s) > 2 for s in cell['source'] if s.strip()), f"Cell {i}: char corruption"
   print("Validation passed")
   ```
   Check: no char-by-char corruption, no missing `\n` terminators, no collapsed lines >1000 chars.

8. **Update `progress.md`** under Workstream 5 with what was done.

## Dispatch Strategy (for the manager agent)

For a unit with three subsections, dispatch **three parallel agents** — one per notebook — for steps 3–4.
Each agent receives:
- The full style principles and physics conventions (copy from rules)
- The specific outline content for its notebook (extract from outline.md)
- The current notebook content to reuse and build on (Read the notebook first)

Then handle step 5 (Prompts + Homework review, Overview update) and step 6 (renames/TOC) in a **single
follow-up pass** after all three rewrites are confirmed complete, since the Overview and any rename
cascade both need to see all three notebooks' final state.

## Structural Changes: Outline vs Current Files

The outline has been redesigned and may differ from the current file structure. Key changes to watch for:

### Ch3 — Title renames
- 3.1.1: "Classical to Quantum" → "Geometric Optics"
- 3.1.3: "Quantum Mechanics as Optics" → "Particle-Wave Unification"
- 3.2.2 and 3.2.3: swapped order (Schrödinger Equation now 3.2.2, Free Particle Propagator now 3.2.3)

### Ch4 — Restructured from 5 units to 4 units
- 4.1: lesson titles changed (4.1.1 → "Gauge Principle", 4.1.2 → "Electromagnetic Coupling", 4.1.3 → "Gauge Invariance")
- 4.2: completely new unit "Berry Phase" replacing old "Flux Ring"
  - 4.2.1 Berry Phase (new content), 4.2.2 Aharonov-Bohm Effect, 4.2.3 Flux Ring
  - Old files: 4-2-1-aharonov-bohm-effect, 4-2-2-flux-quantization, 4-2-3-gauge-invariance
- 4.3: Landau Level — lessons renamed (4.3.1 adds Hall effect content)
- 4.4: Spin and Monopole — 4.4.1 renamed to "Classical Spin"
- Old 4.5 Berry Phase unit is REMOVED — content absorbed into new 4.2
  - Old files 4-5-*.ipynb and 4-5-berry-phase.ipynb should be archived or deleted
  - _toc.yml must be updated to remove 4.5 entries

### Ch6 — Content reshuffled
- 6.1.2: "Partial Trace" → "Entropy" (partial trace moved to 6.2.1)
- 6.1.3: "Entropy" → "Quantum Statistics" (new content: Bose-Einstein/Fermi-Dirac)
- 6.2.1: "Composite Systems" now includes partial trace content

When working on any of these chapters, the manager agent MUST handle file renames, _toc.yml updates,
index.md updates, and cross-reference fixes as part of step 6.

## Important Reminders

- **NEVER use Edit, Write, or NotebookEdit** — all three are denied. Use only Bash + Python.
- **Always Read before writing** — verify cell structure hasn't changed.
- **One unit at a time** — complete one unit fully before starting another.
- **Depth over breadth** — finish completely, don't leave partially-done notebooks.
- **Check outline.md for the canonical narrative** — the outline is the source of truth for content decisions.
- **Preserve correct physics** — rewrite prose, don't invent new physics. When uncertain, flag for professor review.
