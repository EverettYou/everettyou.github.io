# Rule: Notebook and site architecture

Authoring layout for Jupyter Book source under `notes_src/`. See also **`myst-references.md`** (MyST/Sphinx syntax) and **`content-style.md`** (admonitions, homework format).

## File naming

- Chapter dirs: `ch{N}_{topic}/` (e.g., `ch1_qubit/`)
- Section parents: `{ch}-{sec}-{topic}.ipynb` (e.g., `6-1-density-matrix.ipynb`)
- Subsections: `{ch}-{sec}-{sub}-{topic}.ipynb` (e.g., `6-1-1-mixed-states.ipynb`)
- Chapter index: `ch{N}_{topic}/index.md`
- Titles use dots: `# 6.1 Density Matrix`, `# 6.1.1 Mixed States`

## Chapter index pages

Markdown (`.md`), not notebooks. Contains: course title heading, `{list-table}` with Sec / Topic / Textbook columns, glossary admonition with key terms.

## Section parent notebooks (x.y)

- No Prompts boxes at x.y level (only x.y.z)
- No "Brief Introduction" or "Structure of Chapter" headings
- Topics table links subsection filenames, not URLs
- `## Overview` first, `## Project` last

## Subsection content arc (x.y.z)

Within `## Lecture Notes` (cell 2):

- `### Overview` (heading only, no repeated title)
- Body: `###` subsections; key results visible; derivations in `:::{dropdown}`
- `:::{tab-set}`: compare alternatives (e.g., Schrödinger vs Heisenberg picture)
- Discussion (`dropdown tip`) inline where debate helps
- Application blocks in `example` admonitions
- `### Summary`: 3–5 recap bullets

## Figures and layout

- **Margin figure:** `:::{margin}` + `:::{figure}`, use `:width: 100%`
- **Sidebar:** `:::{sidebar}` for asides (biography, further reading)
- **Side-by-side:** `::::{grid} 1 1 2 2` with `:::{grid-item-card}`
- **Figure options:** `:name:`, `:width: 80%` (or `100%` in margin/cards), `:align: center`

## Jupyter widgets with Matplotlib

- `display(fig)` + `plt.close(fig)` (never `plt.show()`)
- `@interact`: return `fig` OR `display(fig)` in callback — not both
- `observe` + `Output`: for reusing one figure or wiring Play + sliders
- `clear_output(wait=True)` before `display(fig)` in target `Output`
- `plt.ioff()` / `plt.ion()` to suppress spurious draws
- Define `Output` and controls **before** callbacks that reference them
- `continuous_update=False` on sliders; document kernel restart for stale UI
