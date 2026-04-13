---
name: phys130b-prompt-auditor
description: Audit and improve Prompts boxes (cell 1) across PHYS130B notebooks. Use whenever prompts need review, a lecture has been edited and prompts may be stale, or when writing prompts for a new notebook. Triggers on: "audit prompts", "fix prompts", "improve prompts", "prompts are bad/stale/complicated", or any mention of cell 1 quality. Also use proactively after any lecture-content edit to check whether prompts still match.
---

# Skill: Prompt Auditor (PHYS130B)

Audit, redesign, and maintain the **Prompts** admonition (cell 1) in subsection notebooks (x.y.z). Prompts are the student's first contact with a topic — they use these to prompt an LLM for AI-assisted preview before class.

## Why this skill exists

Prompts are not homework problems or exam questions. They are **LLM input strings** that a student pastes into ChatGPT/Claude to learn the material before lecture. A bad prompt produces a bad AI conversation; a good prompt produces a focused, educational preview. The quality bar is therefore different from other parts of the notes.

## Design principles

### 1. Descriptive enough for the LLM to give a focused answer

Each prompt must give the LLM enough context to understand **which specific concept** the student is asking about and **what angle** to address. Oversimplified prompts like "What is a qubit?" are too vague — the LLM doesn't know what level, what aspects, or what connections matter.

**Good (specific, descriptive):**
> What is a qubit, and why is it the simplest quantum system? How does it illustrate the core ideas of quantum mechanics?

**Bad (oversimplified):**
> What is a qubit?

A prompt should typically be 1–2 sentences and may include a follow-up question to sharpen the focus ("How does X differ from Y?", "Why does Z follow?", "What happens when W?").

### 2. Math is a tool, not the point

LaTeX formulas **are allowed** when they help identify the specific object or equation being discussed — naming a quantity precisely is valuable. But formulas should not be the *starting point* of a prompt (e.g., "Starting from $\hat{H} = \ldots$, compute...") and should not dominate the prompt.

**Guidelines:**
- **Use math to name things:** "$K(x,t;x',t')$" identifies the propagator; "$\mathrm{Tr}(\hat{\rho}^2)$" identifies purity. These help the LLM give a precise answer.
- **Don't use math as instructions:** "Compute $\frac{\mathrm{d}\langle\hat{O}\rangle}{\mathrm{d}t}$" turns the prompt into a homework problem. Instead: "How does the Heisenberg equation of motion govern observable evolution?"
- **Don't paste full Hamiltonians or long expressions** as prompt setup. Refer to them by name: "the gauge-invariant Hamiltonian" not "$\hat{H} = \frac{1}{2m}(\hat{\boldsymbol{p}} - q\boldsymbol{A})^2 + q\Phi$".
- **Keep inline math short** — a symbol, a short expression, or an equation name. If the math is longer than ~30 characters, rephrase in words.

### 3. One main topic per prompt, but depth is welcome

Each prompt should center on **one concept or one connection**. But within that focus, asking a two-part question ("What is X? Why does Y follow?") is good — it tells the LLM to both define and explain, producing a richer answer. This is different from a compound prompt that chains unrelated tasks.

**Good (focused depth):**
> Derive the first-order state correction. Why does the admixture of state $m$ scale as coupling/gap?

**Bad (unfocused compound):**
> Derive first-order energy and state corrections, then explain second-order energy, and discuss when perturbation theory breaks down.

### 4. Prompts must track the lecture

After any edit to cell 2 (lecture notes), prompts may become stale — referencing removed content, missing new topics, or using old terminology. Always check alignment.

### 5. Cover the lecture, not more

Prompts should span the key ideas actually taught in the lecture. Do not introduce concepts that appear only in later sections, homework, or the textbook. Do not duplicate — each prompt covers a different idea.

### 6. Prompt variety

Mix these types (not all are needed in every notebook — pick 4–5 that fit):

| Type | Pattern | Example |
|------|---------|---------|
| **Conceptual** | "What is X? How/why does it differ from Y?" | "What is the difference between a pure state and a mixed state? Why can't a mixed state be described by a single ket?" |
| **Derivation** | "Derive X. Why does [key feature] emerge?" | "Derive the Berry connection and explain why it is a gauge field in parameter space." |
| **Why** | "Why does X happen / matter?" | "Why does the second-order energy correction always lower the ground state?" |
| **Connection** | "How does X relate to / emerge from Y?" | "Connect the path integral to Huygens' principle. How are they saying the same thing about waves?" |
| **Application** | "For [specific setup], compute/show X." | "For a spin-1/2 in a rotating magnetic field, compute the Berry phase and show it equals half the solid angle." |
| **Contrast** | "How do X and Y differ in terms of Z?" | "How do classical bits and qubits differ in terms of what information they can hold?" |

### 7. Respectful tone

Do not comment on the student's knowledge or ability. Never write "Many students find this confusing" or "If you haven't seen relativity." Just ask the question directly.

### 8. Only x.y.z subsection notebooks have Prompts

Section parent notebooks (x.y) do **not** have a Prompts box. Their cell 1 is `## Overview` with a Topics table, Key Concepts, and Learning Objectives (see `notebook-architecture.md`). If an x.y notebook has a Prompts box, it is a structural error — remove it and replace with the correct Overview content.

### 9. Self-contained — no internal references

Each prompt is pasted into an LLM that has no access to the lecture notes. Do not reference other sections, chapter numbers, or units (e.g., "Recall from §3.2 that..." or "In the previous lecture we showed..."). The LLM has no idea what those refer to. Every prompt must be self-contained and understandable on its own.

**Exception:** Referencing a well-known physics concept by name (e.g., "Huygens' principle", "the variational principle") is fine — these are things the LLM knows. Just don't reference *our* section numbering.

## Workflow: Audit → Plan → Implement → Validate

### Step 1: Audit

For each target notebook (or batch):

```python
# Pseudocode for audit
for each x.y.z notebook:
    read cell 1 (prompts) and cell 2 (lecture)
    check:
      - [ ] Specific enough? (LLM can give focused, lecture-aligned answer)
      - [ ] Math used judiciously? (names objects, not homework-style computation)
      - [ ] No long formulas as setup? (no pasted Hamiltonians)
      - [ ] One main topic per prompt? (depth OK, compound chains not OK)
      - [ ] Tracks lecture? (every prompt maps to content in cell 2)
      - [ ] Covers lecture? (key topics in cell 2 all have a prompt)
      - [ ] No stale references? (no mention of removed/renamed content)
      - [ ] 4–5 prompts? (not fewer, not many more)
      - [ ] Respectful? (no "students often", "you may not know", etc.)
      - [ ] Self-contained? (no references to other sections, chapters, or units)
    report issues
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
3. **Draft** using the design principles above. Each prompt should:
   - Name the specific concept or object (using short math notation if it helps)
   - Ask what it is, why it matters, or how to derive/apply it
   - Optionally include a sharpening follow-up question
4. **Cross-check** against the old prompts to preserve any good ones.

### Step 3: Implement

Write the new cell 1 using `notebook-writer` (Bash + Python, raw strings, `text_to_source()`). The format is always:

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

### Step 4: Validate

1. Run `safe_edit.py validate <path>` on edited notebooks.
2. Verify prompt count is 4–5.
3. Verify each prompt maps to a `###` section in cell 2.
4. **Specificity check**: for each prompt, ask "Could a general-purpose LLM give a focused, lecture-relevant answer from this prompt alone?" If the answer is no (too vague), add detail.

## Anti-patterns

| Anti-pattern | Problem | Fix |
|---|---|---|
| Bare concept name only | "What is a qubit?" — too vague, LLM gives generic Wikipedia answer | Add specificity: "What is a qubit, and why is it the simplest quantum system? How does it illustrate the core ideas of quantum mechanics?" |
| Full Hamiltonian as setup | "$\hat{H} = \frac{1}{2m}(\hat{\boldsymbol{p}} - q\boldsymbol{A})^2$. Compute..." — homework, not preview | Refer by name: "Starting from the gauge-invariant Hamiltonian, derive the Lorentz force law." |
| Compound chain | "Derive X, then show Y, then discuss Z." | Split into 2–3 focused prompts |
| Content not in lecture | Prompt about a topic from a different section | Remove or replace with on-topic prompt |
| Commenting on students | "Many students struggle with..." | Just ask the question |
| Homework problem repackaged | "Show that $E_n^{(2)} = \sum_{m \neq n} ...$" | Rewrite as conceptual: "Why does the second-order energy correction always lower the ground state?" |
| > 6 prompts | Too many, student won't use them all | Trim to the 4–5 most essential |
| Section references | "Recall from §3.2 that..." | State the concept directly by name |
| Oversimplified | "Explain Berry phase." | Add depth: "Explain the difference between dynamical phase and geometric (Berry) phase. How do they arise from the time-dependent Schrödinger equation?" |

## Examples of good prompts (from approved notebooks)

**1-1-1 (What is a Qubit):**
```
- What distinguishes quantum physics from classical physics in the way it describes physical systems? How does quantum mechanics represent states and predict outcomes?
- What is a qubit, and why is it the simplest quantum system? How does it illustrate the core ideas of quantum mechanics?
```

**5-1-2 (Non-degenerate Perturbation Theory):**
```
- What is the Hellmann-Feynman theorem, and how does it give the first-order energy correction as an expectation value without expanding eigenstates?
- Derive the first-order state correction. Why does the admixture of state $m$ scale as coupling/gap?
- Why does the second-order energy correction always lower the ground state? Connect this to the variational principle.
```

**6-1-1 (Mixed States):**
```
- What is the difference between a pure state and a mixed state? Why can't a mixed state be described by a single ket $|\psi\rangle$?
- Construct the density matrices for a qubit superposition $(|0\rangle + |1\rangle)/\sqrt{2}$ and a 50-50 classical mixture. How do they differ?
- How does purity $\mathrm{Tr}(\hat{\rho}^2)$ distinguish pure from mixed states? What is the geometric meaning on the Bloch ball?
```

These work because they: name the specific object/concept, ask the LLM to explain at the right level, include short math where it adds precision, and have enough detail for a focused response.

## References

- `rules/prompt-templates.md` — format template and new-notebook checklist
- `rules/teaching-philosophy.md` — AI-assisted preview workflow (§1)
- `rules/content-style.md` — cell structure (cell 1 = Prompts)
- `skills/lecture-content/SKILL.md` — content review includes prompt alignment
- `skills/notebook-writer/SKILL.md` — implementation (JSON editing)
