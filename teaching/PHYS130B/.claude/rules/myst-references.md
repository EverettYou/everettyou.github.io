# Rule: MyST markdown, display math, and cross-references

This file duplicates **display-math policy signals** checked by `scripts/validate_project.py` against `rules/physics-conventions.md` — keep them aligned.

## MyST pitfalls

- **`---`** → docutils crash. Never use.
- **Nested `:::`** → inner admonitions break. Flatten to bold text.
- **Missing blank lines** before/after `:::`, `$$`, `{list-table}` → parse errors.
- **`$$` needs blank lines above and below** — without them, parser treats as inline math.
- **`myst_footnote_transition: false`** in `_config.yml` prevents a docutils crash. Do not remove.

## Display math and equation labels (validator signals)

`$$...$$` blocks MUST have **blank lines above and below**.

Do not put blank lines inside a `$$...$$` block (equation lines must be contiguous).

Example label (no blank lines *within* the block, only outside):

```
$$
E = mc^2
$$ (eq-section-name)
```

Prefer `` {eq}`eq-section-name` `` for cross-refs. Label convention: `eq-{topic}-{description}`.

For multiline equations, always use `\begin{split}...\end{split}` inside `$$...$$`.

Do not use `align` or `aligned` environments in notebooks (unsafe parsing around leading commutators like `[A,B]`).

## Cross-reference conventions

- Section refs in prose: `§6.1.2`
- File links: `[Topic Name](6-1-2-topic-name)` (dashes, no extension)
- Section reordering: two-pass placeholder replacement
- **Arbitrary targets:** `(my-label)=` before heading, or `:name: my-label` on figures/equations. Link with `` {ref}`my-label` ``
- **Figures:** `` {numref}`fig-label` `` (not `Fig. [](#fig-label)` — Sphinx may show raw LaTeX)
- **Footnotes:** `[^1]` in text; `[^1]: Footnote text.` on own line

## Related

- LaTeX notation (vectors, operators, bras/kets): **`physics-conventions.md`**
- Cell/admonition structure: **`content-style.md`**, **`notebook-architecture.md`**
