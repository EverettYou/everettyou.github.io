# Skill: Homework Designer

Design homework problems for PHYS130B quantum mechanics subsection notebooks.

## When to Use

- Creating the `## Homework` section (cell 3) for x.y.z notebooks
- Reviewing or improving existing homework problems
- Designing exam-appropriate physics problems

## Design Principles

1. **5–10 problems per subsection**, each targeting one concept or skill
2. **Mix of problem types:**
   - Conceptual questions ("Explain why...", "What happens if...")
   - Short derivations ("Show that...", "Derive...")
   - "Show that" proofs with specific results to verify
   - Physical reasoning ("Predict...", "Compare...")
   - Simple applications with concrete calculations
3. **Difficulty:** Standard undergraduate quantum mechanics — challenging but fair
4. **Exam-ready:** Problems appear on the in-person final. They must test *understanding*, not just *procedure*
5. **No tedious computation** or trick combinations of simple ideas
6. **AI-compatible:** Students work with AI, so problems should reward genuine understanding

## Format

```markdown
## Homework

**1.** [Clear problem statement targeting one concept.]

**2.** [Another problem. If multi-part, use (a), (b), (c).]

**3.** Show that [specific mathematical result] starting from [given expression or definition].

...
```

Cross-reference format: `HW x.y.z.k` (e.g., HW 1.1.1.3 = problem 3 of §1.1.1).

## Workflow

### Step 1: Read the Lecture Content

Load the notebook's cell 2 (`## Lecture Notes`) and identify:
- Key definitions and theorems introduced
- Important equations and results
- Physical concepts and intuitions
- Common misconceptions or subtle points

### Step 2: Design Problems

For each key concept, design at least one problem. Ensure:
- Problems are self-contained (all needed info in the problem statement)
- Notation matches the lecture notes (check `.claude/rules/physics-conventions.md`)
- Difficulty is appropriate (not trivial, not research-level)
- At least one problem involves physical reasoning, not just math

### Step 3: Review for Physics Accuracy

- Verify all equations and results are correct
- Check that "show that" targets are actually true
- Ensure physical scenarios are realistic
- Confirm notation consistency with the rest of the notes

### Step 4: Write to Notebook

Use the notebook-writer skill to insert/replace cell 3.

## References

- `.claude/design.md` §"Homework" — Full design requirements
- `.claude/rules/physics-conventions.md` — Notation conventions
- `.claude/rules/content-style.md` — Formatting rules
