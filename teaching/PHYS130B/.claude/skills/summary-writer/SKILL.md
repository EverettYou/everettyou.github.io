---
name: summary-writer
description: Standardize `### Summary` and `See Also` blocks in PHYS130B notebooks—summary bullets, cross-links, placement, and link style. Use when auditing or adding See Also, or fixing summary consistency.
---

# Skill: Summary writer (PHYS130B)

Create consistent, student-readable `### Summary` sections across `notes_src/**/*.ipynb` without changing physics claims.

## Activation (auto)

- User asks to audit/fix summary style consistency.
- You see mixed summary patterns (equation-citation heavy vs no-citation, bullet/prose drift, overlong summaries).
- Any bulk summary cleanup across multiple notebooks.
- Adding or normalizing `:::{admonition} See Also` blocks (placement, link format, gloss style).

## Core template (default)

Use this structure for each `### Summary` section:

1. Bullet-only list (no prose paragraphs between bullets). Nested **sub-bullets** are still list structure, not prose blocks.
2. **No markdown tables** in Summary: do not use `| col | col |` rows (including “table rows as list items” like `- | ... |`). For contrasts, use **separate top-level `-` bullets** and, if needed, **sub-bullets** (indented list items under one parent bullet) instead of a grid—keep nesting shallow (typically one level; at most two short sub-items per parent).
3. Target **5-7 bullets** (hard max 8).
4. Each bullet is one concise takeaway sentence.
5. Prefer concept/result language over derivation steps.
6. Keep notation only when essential; avoid citation clutter.

Canonical shape:

```md
### Summary

- [Main physical idea in one sentence.]
- [Key equation-level result in plain language; include formula only if essential.]
- [Interpretation or comparison.]
  - [Optional sub-point when a mini contrast helps—still no tables.]
- [Constraint/assumption/regime of validity.]
- [Bridge to next subsection.]

:::{admonition} See Also
:class: seealso

- [Previous subsection](slug-or-relative-path): One-line gloss (do not repeat the link title).
- [Next subsection](slug-or-relative-path): One-line gloss.
:::
```

See **See Also authoring** below for full rules (counts, paths, gloss tone, and bulk tooling).

## Equation-reference rule

- Default: **do not cite equation labels** in Summary (`{eq}` or `(eq-...)`).
- If one anchor is truly necessary, allow at most **one** short reference in the whole Summary.
- Never put equation references on every bullet.

## Language style rules

- Use direct teaching language, present tense, no rhetorical filler.
- Avoid "we have shown..." repetition.
- Avoid slogan-like all-bold lines.
- Keep bullets parallel in grammar (noun-phrase or declarative-sentence style, not mixed). Under one parent bullet, **sub-bullets** should stay parallel to each other and short (one line each when possible).

## Detail-level rules

- Summary is not a derivation recap.
- Keep algebraic steps in derivation/admonition sections; Summary keeps outcomes and meaning.
- Include at most one compact formula per bullet, and only when it adds clarity.
- **Tables:** never put a markdown/HTML table inside `### Summary`. For side-by-side contrasts, use parallel top-level bullets (e.g. **With …** / **Without …** lead-ins) **or** one parent bullet with **indented sub-bullets** (`  - …`) for the cases being compared—never pipe tables.

## Consistency checklist (per notebook)

- [ ] `### Summary` exists in lecture cell.
- [ ] Bullet-only format (no tables; no `|` row lines posing as bullets). Sub-bullets under a parent `-` item are allowed when they replace a small table.
- [ ] 5-7 bullets (or 4 when subsection is intentionally short).
- [ ] No equation-label spam.
- [ ] No mixed notation with nearby sections.
- [ ] Final bullet connects forward (next notebook or next section).
- [ ] `See Also` is a separate admonition after Summary (not flattened into bullets). Every lecture notebook should include one unless there is a deliberate editorial exception.
- [ ] Any `See Also` box uses `:class: seealso` and valid cross-notebook links when present.
- [ ] `See Also` link bullets use **plain** markdown links: `- [Title](slug-or-path): gloss` — **do not** wrap the link in `**` (no `- **[Title](url)**:`).

## Safety constraints

- Preserve physics content and sign/factor conventions.
- Do not introduce new claims in Summary that are absent from lecture body.
- For `.ipynb` edits, use programmatic JSON edit + validator.

## MyST: `See Also` admonition (critical)

- **Never** merge `:::{admonition} See Also` … `:::` into Summary as bullets, and **never** emit `- :class: seealso` as a list item under `### Summary`.
- The `See Also` block must stay a **separate** MyST admonition **immediately after** the Summary bullets (same markdown cell), with its own `:::` fences.
- When editing Summary text only, **leave** an existing `See Also` block unchanged unless the user explicitly asks to update cross-links. Do not delete or relocate it except to fix a confirmed formatting bug.
- **Link bullet format (canonical):** each item is `- [Visible title](relative-path-or-anchor): short gloss`. Do **not** bold the link (`- **[...](...)**:` is forbidden in `See Also`). Inline cross-references elsewhere in the lecture may still use bold+link if the prose style requires it; the `See Also` box itself stays unbold for the link token.

## See Also authoring (course-wide)

Use the same spirit as the blocks collected under `origin/master` in `.tmp_origin_master_seealso_blocks.md`: **short list**, **valid MyST links**, **one gloss per line** that explains *why* the reader should open that note—not a second copy of the title.

### Placement and structure

1. Exactly one `See Also` admonition per lecture-notes markdown cell.
2. Place it **immediately after** the `### Summary` block (blank line before the opening `:::` is fine).
3. Title line must be exactly `See Also` with `{admonition}`; always include `:class: seealso` on the next line.

### How many items

- Typical **2–4** bullets; allow **5** only when the section sits at a hub (e.g. path-integral overview tying many follow-ons).
- Prefer **prev / next** along `notes_src/_toc.yml` depth-first order, plus at most **one** lateral link (same chapter theme, prerequisite in another chapter, or chapter index `../ch*/index`).

### Link targets (MyST / Jupyter Book)

| Situation | Target form | Example |
|-----------|-------------|---------|
| Same chapter folder | filename stem only | `(1-2-2-uncertainty-and-incompatibility)` |
| Another chapter | relative to current folder | `(../ch6_quantum-foundations/6-1-1-mixed-states)` |
| Chapter landing page | index | `(../ch3_path-integral/index)` |

Use **kebab-case** stems that match the notebook basename (without `.ipynb`). Do not use bare URLs.

### Visible title

- Use the **same wording as the leading `# ...` title** of the target notebook when possible (matches student-facing sidebar / header).
- For chapter indices, titles like `Ch3 Path Integral` are acceptable if that is what the index page uses.

### Gloss (one line after `:`)

- **Content-forward:** say what the reader gets (e.g. “Density-matrix view of collapse”, “Semiclassical tunneling for comparison with instantons”).
- **Do not repeat** the link text: avoid `…: Title restated`—the archive examples almost always add *new* information after the colon.
- **Do not** use the legacy em-dash list style (`[A](a) — gloss`); use **colon** form `- [A](a): gloss` for consistency.
- Keep LaTeX inline when needed (`$\\hbar$`, `$\\Delta A$`); stay one line per bullet if possible.

### Bulk fill from `_toc.yml`

When many notebooks still lack `See Also`, you may run (from `teaching/PHYS130B/`):

```bash
python3 .claude/scripts/add_missing_seealso_from_toc.py
python3 .claude/scripts/add_missing_seealso_from_toc.py --refresh   # rebuild existing blocks after rule changes
```

The script derives **prev / next / +1 TOC neighbour** targets from `notes_src/_toc.yml` and pulls link titles from each target notebook’s first `#` heading. It is a **navigation bootstrap only**.

**Content-informed replacement:** after bootstrap (or whenever `See Also` should match the lecture body), edit the `CURATED` map in `.claude/scripts/apply_curated_seealso_34.py` and run:

```bash
python3 .claude/scripts/apply_curated_seealso_34.py
```

That script overwrites only the **list lines** inside existing `See Also` admonitions for the notebooks listed in the map—links and glosses should reflect **Overview / in-text cross-references / Summary**, not TOC order alone.

**Grounding rule:** each `See Also` bullet must be defensible from that notebook’s own lecture text (including explicit `§…` / markdown links). Prefer **two strong links** over three weak ones; **drop** a bullet rather than add a vague “conceptual cousin” or distant topic never named in the lesson.

### Anti-patterns (from repair history)

- Do not flatten `See Also` into Summary bullets (`- :class: seealso`, or duplicate link lines under `### Summary`).
- Do not duplicate the same link line in Summary and in `See Also`.
- Do not mix bold-wrapped link tokens inside `See Also` list items.

## Validation after edits

```bash
python3 .claude/skills/notebook-writer/scripts/safe_edit.py validate <notebook>
python3 .claude/scripts/validate_project.py --notebooks-only --scope <scope>
```
