# Progress Tracker — PHYS130B Lecture Note Improvement

This file is the single source of truth for the refactoring effort.
Read before starting work. Update after completing work.

## Agent Status

| Agent | Status | Last Run | Current Task |
|-------|--------|----------|--------------|
| Manager | idle | — | — |
| Review | idle | — | — |
| Design | idle | — | — |
| Writer | idle | — | — |
| Science | idle | — | — |

## Completed Workstreams

The following workstreams were completed in previous runs:

- **Workstream 1: Prompt Review** — All 63 subsection notebooks reviewed and updated
- **Workstream 2: Homework** — All 63 subsection notebooks have `## Homework` (cell 3)
- **Workstream 3: Projects** — All 21 section parent notebooks have `## Project` (cell 2)
- **Workstream 4: Discussion Problems** — All 63 subsection notebooks have inline Discussion boxes

## Workstream 5: Content Polish (84 notebooks)

### Completed

### In Progress

### Pending

#### Section Parents (21)
- [ ] 1-1-states-and-observables
- [ ] 1-2-measurement
- [ ] 1-3-time-evolution
- [ ] 2-1-bosons-and-fermions
- [ ] 2-2-angular-momentum
- [ ] 2-3-anyons
- [ ] 3-1-quantization
- [ ] 3-2-propagator
- [ ] 3-3-stationary-phase
- [ ] 3-4-imaginary-time
- [ ] 4-1-gauge-field
- [ ] 4-2-flux-ring
- [ ] 4-3-landau-level
- [ ] 4-4-spin-and-monopole
- [ ] 4-5-berry-phase
- [ ] 5-1-time-independent-perturbation-theory
- [ ] 5-2-time-dependent-perturbation-theory
- [ ] 6-1-density-matrix
- [ ] 6-2-entanglement
- [ ] 6-3-generalized-measurement
- [ ] 6-4-open-quantum-systems

#### Subsections (63)
- [ ] 1-1-1-spins-and-qubits
- [ ] 1-1-2-state-and-representation
- [ ] 1-1-3-hermitian-operators
- [ ] 1-2-1-measurement-postulate
- [ ] 1-2-2-uncertainty-and-incompatibility
- [ ] 1-2-3-measurement-operators
- [ ] 1-3-1-unitary-evolution
- [ ] 1-3-2-spin-dynamics
- [ ] 1-3-3-heisenberg-picture
- [ ] 2-1-1-tensor-product
- [ ] 2-1-2-symmetrization
- [ ] 2-1-3-second-quantization
- [ ] 2-2-1-angular-momentum-algebra
- [ ] 2-2-2-spin-representations
- [ ] 2-2-3-addition-of-angular-momenta
- [ ] 2-3-1-exchange-statistics
- [ ] 2-3-2-fractional-quantum-hall-anyons
- [ ] 2-3-3-toric-code
- [ ] 3-1-1-classical-to-quantum
- [ ] 3-1-2-physical-optics
- [ ] 3-1-3-quantum-mechanics-as-optics
- [ ] 3-2-1-path-integral-formulation
- [ ] 3-2-2-free-particle-propagator
- [ ] 3-2-3-schrodinger-equation
- [ ] 3-3-1-stationary-phase-approximation
- [ ] 3-3-2-wkb-approximation
- [ ] 3-3-3-bohr-sommerfeld-quantization
- [ ] 3-4-1-wick-rotation
- [ ] 3-4-2-statistical-mechanics
- [ ] 3-4-3-instantons
- [ ] 4-1-1-gauge-transformations
- [ ] 4-1-2-gauge-connection
- [ ] 4-1-3-electromagnetic-coupling
- [ ] 4-2-1-aharonov-bohm-effect
- [ ] 4-2-2-flux-quantization
- [ ] 4-2-3-gauge-invariance
- [ ] 4-3-1-cyclotron-motion
- [ ] 4-3-2-landau-quantization
- [ ] 4-3-3-quantum-hall-effect
- [ ] 4-4-1-orbital-vs-spin
- [ ] 4-4-2-dirac-monopole
- [ ] 4-4-3-monopole-harmonics
- [ ] 4-5-1-berry-phase
- [ ] 4-5-2-applications
- [ ] 4-5-3-topology
- [ ] 5-1-1-toy-model
- [ ] 5-1-2-non-degenerate-perturbation-theory
- [ ] 5-1-3-degenerate-perturbation-theory
- [ ] 5-2-1-interaction-picture
- [ ] 5-2-2-fermis-golden-rule
- [ ] 5-2-3-applications
- [ ] 6-1-1-mixed-states
- [ ] 6-1-2-partial-trace
- [ ] 6-1-3-entropy
- [ ] 6-2-1-composite-systems
- [ ] 6-2-2-entanglement-measures
- [ ] 6-2-3-bell-inequality
- [ ] 6-3-1-projective-measurement
- [ ] 6-3-2-povm
- [ ] 6-3-3-quantum-channels
- [ ] 6-4-1-decoherence
- [ ] 6-4-2-lindblad-master-equation
- [ ] 6-4-3-error-correction

### Issues

## Workstream 6: Validation

### Last Full Validation
- Date: —
- Result: —

### Known Issues
- 5.2.3 covers 4 unrelated topics at 13K chars — candidate for splitting
- Some Ch3 notebooks may have dense single-paragraph content from collapsed-content fix
- 1-3-3-heisenberg-picture: repeated feedback about corrupted math formulas (check if resolved)

## Log

| Date | Agent | Notebook | Action | Notes |
|------|-------|----------|--------|-------|
| 2026-03-28 | — | general | LaTeX convention fix | `\mathrm{i/e/d}` applied to 50/84 notebooks |
| 2026-03-28 | — | progress.md | Rebuild | Progress file corrupted by parallel agents |
| 2026-03-29 | — | 1-3-3-heisenberg-picture | Fix LaTeX | Fixed unescaped imaginary units in Problem 4 |
| 2026-03-30 | — | .claude/ | Infrastructure | Built commands, rules, skills, agents structure |
| 2026-03-30 | — | .claude/ | Admonition redesign | Discussion → `tip` class; full admonition table in rules |
