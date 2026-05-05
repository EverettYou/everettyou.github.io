---
name: phys130b-prompt-designer
description: Design and audit Prompts boxes (cell 1) for PHYS130B notebooks—specify LLM-preview questions; implementation via notebook-writer only. Triggers on prompt review, stale prompts after lecture edits, new notebook prompts, or cell 1 quality issues.
---

# Skill: Prompt designer (PHYS130B)

## Role in the stack

**Content designer:** audit cell 1 and **deliver** the Prompts markdown (or a marked-up plan). **Do not** edit `.ipynb` JSON. **Do not** run validators. Hand final markdown to **`notebook-writer`**; it validates after save (**`rules/validation.md`**).

**MyST shells and style-matched examples:** **`TEMPLATES.md`** (this folder)—keep aligned with **`rules/prompt-preview.md`** and a **gold** subsection notebook in the same course style.

Audit and redesign the **Prompts** admonition (cell 1) in subsection notebooks (x.y.z). Prompts are the student's first contact with a topic — they use these to prompt an LLM for AI-assisted preview before class.

## Activation

Same triggers as the YAML `description`, plus **Phase C** in **`.claude/README.md`** / **`skills/maintenance-phases/SKILL.md`**. After **`lecture-designer`**-driven lecture edits, re-check prompt alignment.

## Norms (do not duplicate here)

**Law:** **`rules/prompt-preview.md`** (LLM preview criteria + anti-patterns). **Copy-paste template + style references:** **`TEMPLATES.md`** (this folder). This `SKILL.md` defines **workflow** only—read the rule + template before drafting or auditing.

## Workflow: Audit → Plan → Hand off → Spot-check

### Step 1: Audit

For each target notebook (or batch):

```python
# Pseudocode for audit
for each x.y.z notebook:
    read cell 1 (prompts) and cell 2 (lecture)
    verify every dimension in **`rules/prompt-preview.md`**
    report gaps vs those sections (do not invent parallel criteria here)
```

For bulk audit, scan all subsection notebooks:

```bash
python3 -c "
import json, glob, re
for p in sorted(glob.glob('notes_src/**/*.ipynb', recursive=True)):
    if '/_build/' in p: continue  # skip build cache
    with open(p) as f:
        nb = json.load(f)
    if len(nb['cells']) < 4: continue  # skip x.y parents
    cell1 = ''.join(nb['cells'][1].get('source', []))
    if 'Prompts' not in cell1: continue
    issues = []
    prompts = [l.strip() for l in cell1.split('\n') if l.strip().startswith('- ')]
    for pr in prompts:
        if len(pr) > 350:
            issues.append(f'very long prompt ({len(pr)} chars)')
        if len(pr) < 40:
            issues.append(f'possibly oversimplified ({len(pr)} chars): {pr[:60]}')
        if pr.count('?') > 3:
            issues.append('too many questions in one prompt')
    if len(prompts) < 3:
        issues.append(f'too few prompts ({len(prompts)})')
    if len(prompts) > 6:
        issues.append(f'too many prompts ({len(prompts)})')
    if issues:
        print(f'{p}: {issues}')
"
```

### Step 2: Plan

For each notebook with issues, draft replacement prompts:

1. **Read cell 2** and list the key concepts/sections taught.
2. **Map one prompt per concept** — pick the most important 4–5.
3. **Draft** per **`rules/prompt-preview.md`** + **`TEMPLATES.md`**. Each prompt should:
   - Name the specific concept or object (using short math notation if it helps)
   - Ask what it is, why it matters, or how to derive/apply it
   - Optionally include a sharpening follow-up question
4. **Cross-check** against the old prompts to preserve any good ones.

### Step 3: Hand off to notebook-writer

Provide the final cell-1 markdown to **`notebook-writer`** for programmatic write (Bash + Python, raw strings, `text_to_source()`). Target format (full shell + placeholders: **`TEMPLATES.md`**):

```
:::{admonition} Prompts
:class: tip

- [prompt 1]
- [prompt 2]
- [prompt 3]
- [prompt 4]
- [prompt 5]
:::
```

### Step 4: Acceptance checklist (designer—no validators)

After **`notebook-writer`** has applied your draft (separate step), the **writer** runs **`rules/validation.md`**. As designer, you may **spot-check** the written cell 1 in the repo for:

1. Prompt count 4–5.
2. Each prompt maps to a `###` section in cell 2.
3. **Specificity:** each prompt is specific enough for a lecture-aligned LLM answer (revise spec and re-hand off if not).

## References

- **`TEMPLATES.md`** — MyST shell + style references
- `rules/prompt-preview.md` — criteria + anti-patterns (law)
- `rules/teaching-philosophy.md` — AI-assisted preview workflow (§1)
- `rules/content-style.md` — cell structure (cell 1 = Prompts)
- `skills/lecture-designer/SKILL.md` — lecture-wide content includes prompt alignment
- `skills/notebook-writer/SKILL.md` — sole `.ipynb` implementation **and post-edit validation**
