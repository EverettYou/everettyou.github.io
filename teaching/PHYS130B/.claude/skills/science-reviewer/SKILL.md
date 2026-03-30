# Skill: Science Reviewer

Review notebook content for physics correctness, notation consistency, and conceptual accuracy.

## When to Use

- After new content is written (homework, discussion problems, projects)
- When professor flags potential errors
- As part of the validation pipeline before publishing
- When reviewing AI-generated physics content

## Review Checklist

### 1. Equations and Mathematics

- All equations are dimensionally consistent
- Signs and factors are correct (especially factors of 2, π, ℏ)
- Operator ordering is correct (quantum operators don't commute)
- Bra-ket notation is properly matched
- Display math has blank lines above and below `$$`

### 2. Notation Consistency

Per `.claude/rules/physics-conventions.md`:
- `\mathrm{i}` for imaginary unit, `\mathrm{e}` for Euler's number, `\mathrm{d}` for differentials
- `\boldsymbol` for vectors, `\hat` for operators
- Pauli operators with superscript indices: `\hat{\sigma}^x`
- Eigenstate notation matches the standard table

### 3. Physical Concepts

- Definitions are precise and complete
- Physical interpretations are correct
- Approximations are stated and justified
- Limiting cases are consistent
- No conflation of distinct concepts (e.g., entanglement vs. correlation)

### 4. Homework Problems

- "Show that" targets are mathematically correct
- Problem setups are physically realistic
- Given information is sufficient to solve each problem
- Expected difficulty is appropriate for undergraduates
- Solutions exist and are unique (unless stated otherwise)

### 5. Discussion Problems

- Questions have verifiable physics answers (not pure philosophy)
- The "controversial" aspect is genuine (not manufactured)
- Multiple defensible positions exist
- The question connects to specific lecture content

### 6. Projects

- Research topics are real and current
- Suggested approaches are feasible with AI + 2 weeks
- Expected deliverables are well-defined
- Background references exist and are accessible

## Workflow

1. Load the notebook and read all cells
2. Check each equation against known results (textbook, established references)
3. Verify notation consistency across the notebook and with neighboring notebooks
4. Flag issues with severity:
   - **ERROR**: Incorrect physics, wrong equations, misleading statements
   - **WARNING**: Notation inconsistency, unclear wording, missing context
   - **NOTE**: Style suggestions, alternative approaches worth mentioning
5. Report findings and update `progress.md`

## References

- David Tong, *Quantum Mechanics* (Cambridge University Press) — primary textbook
- `.claude/design.md` — Notation and structure conventions
- `.claude/rules/physics-conventions.md` — LaTeX and notation rules
