---
name: phys130b-summary-designer
description: Design and audit `### Summary` and `See Also` blocks in PHYS130B—templates, bullets, cross-links; specify changes for notebook-writer. Use when auditing summaries or See Also consistency.
---

# Skill: Summary designer (PHYS130B)

## Role in the stack

**Content designer:** define templates, audit bullets/links, and **specify** replacement markdown (cell index + text). **Do not** edit `.ipynb` JSON. **Do not** run validators. **`notebook-writer`** applies changes **and** runs **`rules/validation.md`** after each save. Bulk scripts that touch `.ipynb` run only in a **`notebook-writer`** session.

Specify consistent, student-readable `### Summary` and See Also blocks without changing physics claims.

**MyST shells:** **`TEMPLATES.md`** (this folder)—aligned to **`rules/content-style.md`** § Summary and See Also and to **gold** subsection closings (e.g. `6-1-1-mixed-states`).

**Automation:** bulk / repair Python lives in **`scripts/`** (see **`scripts/README.md`**); execution is always **`notebook-writer`** after the designer specifies the command + any `CURATED` edits.

## Activation (auto)

- **Phase C** maintenance: **`.claude/README.md`** / **`skills/maintenance-phases/SKILL.md`** when normalizing `### Summary` / See Also.
- User asks to audit/fix summary style consistency.
- You see mixed summary patterns (equation-citation heavy vs no-citation, bullet/prose drift, overlong summaries).
- Any bulk summary cleanup across multiple notebooks.
- Adding or normalizing `:::{admonition} See Also` blocks (placement, link format, gloss style).

## Norms (do not duplicate here)

**Law:** **`rules/content-style.md`** § **Summary and See Also** (bullets, length, MyST fences, link style, navigation, grounding) plus **`rules/myst-references.md`** for cross-reference mechanics. Do **not** restate those tables in tickets—cite the rule § instead.

## Audit workflow (skill-only)

1. Read the lecture cell; compare `### Summary` and `See Also` to **`content-style.md`** § Summary and See Also + **`myst-references.md`**.
2. Draft replacement markdown (preserve physics—no new claims absent from the lecture body).
3. Hand cell index + markdown to **`notebook-writer`**; writer validates (**`rules/validation.md`**).

### Per-notebook checklist (maps to rules—do not expand here)

- [ ] Summary + See Also satisfy **`content-style.md`** § Summary and See Also.
- [ ] Links and stems satisfy **`myst-references.md`**.
- [ ] Final Summary bullet still bridges forward where the rule expects it.
- [ ] Physics unchanged from lecture body (signs/factors).

## Safety constraints

- Preserve physics content and sign/factor conventions.
- Do not introduce new claims in Summary that are absent from lecture body.
- Any change to notebook files: **`notebook-writer`** applies the edit **and** runs validators (**`rules/validation.md`**)—not this skill.

### Bulk fill from `_toc.yml` (implementation)

These commands **modify** `.ipynb` files—run only as part of a **`notebook-writer`** session (from `teaching/PHYS130B/`). **Which script when:** **`scripts/README.md`** (this skill folder).

```bash
python3 .claude/skills/summary-designer/scripts/add_missing_seealso_from_toc.py
python3 .claude/skills/summary-designer/scripts/add_missing_seealso_from_toc.py --refresh   # rebuild existing blocks after rule changes
```

The script derives **prev / next / +1 TOC neighbour** targets from `notes_src/_toc.yml` and pulls link titles from each target notebook’s first `#` heading. It is a **navigation bootstrap only**.

**Content-informed replacement:** after bootstrap (or whenever `See Also` should match the lecture body), edit the `CURATED` map in **`scripts/apply_curated_seealso_34.py`** and run:

```bash
python3 .claude/skills/summary-designer/scripts/apply_curated_seealso_34.py
```

That script overwrites only the **list lines** inside existing `See Also` admonitions for the notebooks listed in the map—links and glosses should reflect **Overview / in-text cross-references / Summary**, not TOC order alone.

**Other repairs** (dembold See Also links; strip Summary bullets that duplicate See Also): **`scripts/unbold_seealso_link_bullets.py`**, **`scripts/fix_summary_duplicate_seealso_links.py`** — see **`scripts/README.md`**.

## References

- **`TEMPLATES.md`** — Summary + See Also shells
- `rules/content-style.md`, `rules/notebook-architecture.md`, `rules/myst-references.md`, `rules/physics-conventions.md`
- `skills/notebook-writer/SKILL.md` — sole `.ipynb` implementation, runs **`scripts/*.py`** here, **and post-edit validation**
