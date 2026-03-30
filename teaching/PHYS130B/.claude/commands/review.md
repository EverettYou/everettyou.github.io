# /project:review — Review a Notebook

Review a specific notebook for quality, correctness, and compliance with design.md conventions.

## Usage

```
/project:review <notebook-name>
```

Example: `/project:review 1-1-1-spins-and-qubits`

## Instructions

1. **Read companion docs first:**
   - `.claude/design.md` — cell structure, admonition classes, notation conventions
   - `.claude/experience.md` — ipynb format rules, corruption patterns

2. **Locate the notebook** in `notes_src/` (search by name fragment if needed).

3. **Load and inspect** using Python `json.load` (never NotebookEdit or Edit on .ipynb).

4. **Check against the design spec:**

   For **x.y.z subsection** notebooks:
   - Cell 0: `# x.y.z Title` (dots in title)
   - Cell 1: Prompts admonition (`:class: tip`), 4–5 natural questions
   - Cell 2: `## Lecture Notes` → `### Overview` → body → `### Summary`
   - Cell 3: `## Homework` with numbered problems (5–10)
   - No `---` horizontal rules; no nested `:::` admonitions
   - Key equations labeled; display math has blank lines above/below
   - LaTeX uses `\mathrm{i}`, `\mathrm{e}`, `\mathrm{d}`
   - Vectors use `\boldsymbol`, operators use `\hat`

   For **x.y section parent** notebooks:
   - Cell 0: `# x.y Section Title`
   - Cell 1: `## Overview` → paragraph → `### Topics` table → `### Key Concepts` → `### Learning Objectives`
   - Cell 2: `## Project` with one research-level project
   - No Prompts boxes at x.y level

5. **Run corruption checks:**
   - Char-by-char corruption (most source elements ≤2 chars)
   - Missing `\n` terminators on non-final lines
   - Collapsed content (lines >1000 chars)

6. **Report findings** organized by:
   - 🔴 Critical (corruption, missing cells, wrong structure)
   - 🟡 Warning (missing homework, weak prompts, notation issues)
   - 🟢 Suggestions (content improvements, readability)

7. **Update `progress.md`** with findings under the relevant workstream.
