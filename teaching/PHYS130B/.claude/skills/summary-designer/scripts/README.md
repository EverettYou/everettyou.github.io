# Summary / See Also tooling (PHYS130B)

**Who runs these:** **`notebook-writer`** sessions only (they **mutate** `.ipynb`). **`summary-designer`** chooses which script and edits maps when needed; see **`../SKILL.md`**.

| Script | When to use |
|--------|-------------|
| **`add_missing_seealso_from_toc.py`** | Bootstrap missing `See Also` blocks from `_toc.yml` DFS (prev/next neighbours). `--refresh` rebuilds after template or TOC changes. |
| **`apply_curated_seealso_34.py`** | Overwrite See Also **list lines** using the `CURATED` dict in this file—after designer curates glosses to match lecture text. |
| **`unbold_seealso_link_bullets.py`** | Strip `**` around `- [Title](url):` inside See Also admonitions only (style fix). |
| **`fix_summary_duplicate_seealso_links.py`** | Remove Summary bullets that duplicate See Also link lines (targeted default path list; pass paths to override). |

**Law:** `rules/content-style.md` § Summary and See Also, `rules/myst-references.md`.
