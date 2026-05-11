# Rule: MyST markdown, display math, and cross-references

**Display math layout** (blank lines around `$$`, labels, `split` vs `align`, etc.): **single source — `physics-conventions.md` § Display Math**. `validate_project.py` encodes those checks; keep this file aligned with that section when MyST policy changes.

## MyST pitfalls

- **`---`** → docutils crash. Never use.
- **Nested `:::`** → inner admonitions break. Flatten to bold text.
- **Missing blank lines** before/after `:::`, `$$`, `{list-table}` → parse errors (for `$$` detail see **`physics-conventions.md`**).
- **`myst_footnote_transition: false`** in `_config.yml` prevents a docutils crash. Do not remove.

## Cross-reference conventions

- **Equations:** label syntax and `` {eq}`eq-topic-name` `` citations — see **`physics-conventions.md`** § Display Math (layout) and use MyST roles here for linking.
- Section refs in prose: `§6.1.2`
- File links: `[Topic Name](6-1-2-topic-name)` (dashes, no extension)
- Section reordering: two-pass placeholder replacement
- **Arbitrary targets:** `(my-label)=` before heading, or `:name: my-label` on figures/equations. Link with `` {ref}`my-label` ``
- **Figures:** `` {numref}`fig-label` `` (not `Fig. [](#fig-label)` — Sphinx may show raw LaTeX)
- **Footnotes:** `[^1]` in text; `[^1]: Footnote text.` on own line

## Student-facing scope

Lecture notes published to Jupyter Book are **student-facing**. Never reference agent or maintenance infrastructure inside notebook prose, admonitions, dropdowns, footnotes, or any cell content rendered in the book. Forbidden reference targets:

- Any path under **`.claude/`** (`.claude/rules/*.md`, `.claude/skills/*`, `.claude/scripts/*`).
- Repository-only infrastructure files: **`progress.md`**, **`feedback.md`**, **`CLAUDE.md`**, the repo-root **`README.md`**, **`_refs/`** (professor's source notes).
- Section / heading names that exist **only** inside the files above. *Example of the failure:* a parenthetical "(see `physics-conventions.md` § Chapter 4 EM Units, *Exception — spacetime-unified 4-vectors and tensors*)" inside a notebook — that heading lives in `.claude/rules/physics-conventions.md` and is unreachable from the rendered book; the citation dangles.

If a notebook needs to state a convention (e.g. "we use SI throughout this chapter," "we set $c = 1$ in this dropdown"), state it **self-containedly** in the cell. Allowed cross-references — within the published book — use the existing roles: `{eq}`, `{numref}`, `{ref}`, file-link form `[Title](kebab-case-stem)`, and `§x.y[.z]` for chapter / section / subsection numbers (see § Cross-reference conventions above).

## Related

- LaTeX notation (vectors, operators, bras/kets): **`physics-conventions.md`**
- Cell/admonition structure: **`content-style.md`**, **`notebook-architecture.md`**
