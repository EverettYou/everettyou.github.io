| 2026-04-02 | Manager | Admonition audit (18 notebooks) | Class reclassification | 13 important→note, 6 important→attention, 6 renamed; 204→185 important boxes |
| 2026-04-02 | Manager | 4-4-3-monopole-harmonics | Physics correction + alignment | Fixed J=Λ+sR̂ framework; removed wrong L²=ℏ²l(l+1-2s) formula; fixed HW3; trimmed Hopf fibration/Applications sections |
# Progress Tracker — PHYS130B Lecture Note Improvement

This file is the single source of truth for the refactoring effort.
Read before starting work. Update after completing work.

## Agent Status

| Agent | Status | Last Run | Current Task |
|-------|--------|----------|--------------|
| Manager | idle | 2026-04-02 | Physics correction: 4.4.3 Monopole Harmonics (J=Λ+sR̂ framework, fix wrong L² eigenvalue formula) |

## Completed Workstreams

The following workstreams were completed in previous runs:

- **Workstream 1: Prompt Review** — All 63 subsection notebooks reviewed and updated
- **Workstream 2: Homework** — All 63 subsection notebooks have `## Homework` (cell 3)
- **Workstream 3: Projects** — All 21 section parent notebooks have `## Project` (cell 2)
- **Workstream 4: Discussion Problems** — All 63 subsection notebooks have inline Discussion boxes

## Workstream 5: Content Polish

### Work Order

Process units in this order. Each run picks the next pending unit.

**Phase 1 — Ch2 (partially worked on, needs outline alignment + Overview)**
1. 2.1 Bosons and Fermions — 2.1.1/2.1.2 edited (notation, deduplication), 2.1.3 untouched. All lack `### Overview`.
2. 2.2 Angular Momentum — untouched, no structural changes needed. Large notebooks (400-670 lines), lack `### Overview`.
3. 2.3 Anyons — 2.3.1/2.3.2/2.3.3 rewritten (charge-flux, FQH, toric code). Lack `### Overview`. Close to outline.

**Phase 2 — Ch3 (untouched, has title renames)**
4. 3.1 Quantization — RENAMES: 3.1.1 "Classical to Quantum" → "Geometric Optics", 3.1.3 "Quantum Mechanics as Optics" → "Particle-Wave Unification". Update _toc.yml + index.md after rename.
5. 3.2 Propagator — REORDER: outline swaps 3.2.2/3.2.3 (Schrödinger Eq now 3.2.2, Free Particle now 3.2.3). Must swap file contents or rename both files. Update _toc.yml.
6. 3.3 Stationary Phase — no structural changes.
7. 3.4 Imaginary Time — no structural changes. 3.4.3 instanton narrative updated in outline.

**Phase 3 — Ch5 (untouched, no structural changes, cleanest)**
8. 5.1 Time-Independent PT — no structural changes. Outline adds Hellmann-Feynman as organizing principle.
9. 5.2 Time-Dependent PT — no structural changes. 5.2.3 add Hall conductance/Kubo formula example. 5.2.3 is overlong (605 lines) — may need trimming.

**Phase 4 — Ch6 (untouched, content reshuffle in 6.1/6.2)**
10. 6.1 Density Matrix — RESHUFFLE: 6.1.2 "Partial Trace" → "Entropy" (move partial trace to 6.2.1). 6.1.3 "Entropy" → "Quantum Statistics" (new: Bose-Einstein/Fermi-Dirac from single-mode). Rename files, update _toc.yml.
11. 6.2 Entanglement — 6.2.1 "Composite Systems" now includes partial trace (absorb old 6.1.2 content). Otherwise minor changes.
12. 6.3 Generalized Measurement — no structural changes.
13. 6.4 Open Quantum Systems — minor: decoherence = "measure + forget" framing. Otherwise content exists.

**Phase 5 — Ch4 (major restructuring, save for last)**
14. 4.1 Gauge Field — RENAMES: 4.1.1 → "Gauge Principle", 4.1.2 "Gauge Connection" → "Electromagnetic Coupling", 4.1.3 "Electromagnetic Coupling" → "Gauge Invariance". Content substantially rewritten per outline.
15. 4.2 Berry Phase — MAJOR: old unit was "Flux Ring" (AB effect, flux quantization, gauge invariance). New unit is "Berry Phase" (Berry phase, AB effect, flux ring). Must repurpose existing files with new content. Old 4-2-flux-ring.ipynb parent → new 4-2-berry-phase.ipynb.
16. 4.3 Landau Level — RENAMES: 4.3.1 adds Hall effect content. Otherwise similar structure.
17. 4.4 Spin and Monopole — RENAME: 4.4.1 "Orbital vs Spin" → "Classical Spin". Otherwise similar.
18. CLEANUP: Delete old 4.5 Berry Phase unit — remove 4-5-1, 4-5-2, 4-5-3, 4-5-berry-phase.ipynb files. Remove 4.5 entries from _toc.yml, index.md, ch4 index.md. Content absorbed into new 4.2.

**Phase 6 — Ch1 parents (subsections already done)**
19. 1.1 States and Observables — parent overview update only (subsections done 2026-03-30)
20. 1.2 Measurement — parent overview update only
21. 1.3 Time Evolution — parent overview update only

### Structural Changes Reference

When working on units with structural changes, the manager agent MUST:
1. Rename `.ipynb` files to match new titles (convention: `x-y-z-hyphenated-title.ipynb`)
2. Update `notes_src/_toc.yml` — replace old filenames with new ones
3. Update `notes_src/index.md` — master TOC table
4. Update chapter landing page `notes_src/ch{N}_*/index.md`
5. Update parent notebook's Lessons table links
6. `grep -r "old-filename" notes_src/` to catch any remaining cross-references

### Current Notebook Status (Audit 2026-03-31)

All 54 pending subsection notebooks have 4 cells, Prompts (cell 1), Discussion boxes, and Homework (cell 3).
Key gaps by chapter:

| Chapter | `### Overview` | `### Summary` | `important` boxes | Notes |
|---------|:-:|:-:|:-:|---|
| Ch2 (2.1) | 2.1.1 ✓, 2.1.2 ✓ | all ✓ | 2.1.1 ✓, 2.1.2 ✓ | 2.1.3 untouched |
| Ch2 (2.2) | none | all ✓ | some | large notebooks, untouched |
| Ch2 (2.3) | none | 2.3.1 ✓, 2.3.3 ✓ | all ✓ | rewritten but no Overview |
| Ch3 | none | all ✓ | some | untouched, title renames needed |
| Ch4 | none | 4.3.x/4.5.x missing | some | major restructuring |
| Ch5 | none | 5.1.1/5.2.1/5.2.2 missing | some | untouched |
| Ch6 | none | all ✓ | some | content reshuffle in 6.1/6.2 |

### Completed

- [x] 4.2 Berry Phase — 2026-04-01 — MAJOR restructure: old "Flux Ring" unit → "Berry Phase". Rewrote 4.2.1→Berry Phase (adiabatic theorem, Berry connection/curvature, Phase=Action connection, spin-1/2 example); rewrote 4.2.2→Aharonov-Bohm Effect (AB setup, phase accumulation, flux quantization, persistent currents, SQUIDs); rewrote 4.2.3→Flux Ring (ring Hamiltonian, periodic spectrum, persistent current, pi-flux degeneracy, SQUID application); renamed all 4 files (parent + 3 subsections); updated _toc.yml, index.md, ch4 index.md; fixed cross-refs in 4-1-2/4-1-3/4-4-2; updated parent Overview (Berry phase as central concept, lessons table, key concepts, learning objectives); all 8 modified notebooks validated OK
- [x] 6.2 Entanglement — 2026-04-01 — Polished all 3 subsections + parent. 6.2.1: tightened Overview to 2 sentences, enhanced partial trace physical interpretation ("trace out unobserved → environment"), collapsed worked examples to dropdown. 6.2.2: condensed opening paragraph, collapsed concurrence example, trimmed Summary to 5 bullets. 6.2.3: compressed Overview, removed tangential Contextuality section, tightened CHSH angle calculation, trimmed Summary from 9→7 bullets. Parent: updated Overview motivating paragraph and Key Concepts/Learning Objectives. All 4 notebooks validated OK.
- [x] 4.1 Gauge Field — 2026-04-01 — Rewrote 4.1.1→Gauge Principle (local U(1), covariant derivative, forced Hamiltonian); rewrote 4.1.2→Electromagnetic Coupling (Lorentz force from Heisenberg EOM, E/B from gauge potentials, gauge principle derives EM); rewrote 4.1.3→Gauge Invariance (gauge transformations of ψ/A/Φ, gauge-invariant vs gauge-dependent quantities, canonical vs kinetic momentum, gauge = redundancy); renamed all 3 files, updated _toc.yml, fixed cross-refs in 4-2-1/4-2-3/4-3-1/4-5-1; updated parent Overview; all 5 notebooks validated OK
- [x] 4.3 Landau Level — 2026-04-01 — Added ### Overview and ### Summary to all 3 subsections; rewrote 4.3.1 (added classical Hall effect R_H=B/nq, IQHE motivation, magnetic length, removed Bohr-Sommerfeld to 4.3.2); rewrote 4.3.2 (added Bohr-Sommerfeld, Landau gauge approach, guiding center [X,Y]=il_B^2, two ladder operator towers a/b, complex coordinates and LLL wavefunctions, degeneracy); rewrote 4.3.3 (added Laughlin charge pumping argument for σ_xy=νe²/h, explicit FQHE-anyon connection to §2.3, removed tangential edge state/topology details); updated parent Overview (Core Questions, Key Concepts, Learning Objectives); all 4 notebooks validated OK
- [x] 5.2 Time-Dependent Perturbation Theory — 2026-03-31 — Major content reshuffle: moved Green's functions + Feynman diagrams to 5.2.1, moved adiabatic theorem to 5.2.2, rewrote 5.2.3 with electric dipole transitions + lifetime/linewidth + Kubo formula/Hall conductance; added ### Overview to all 3 subsections; updated Prompts for all 3; trimmed 5.2.3 from 21K→6K chars; updated parent Overview; all 4 notebooks validated OK
- [x] 6.1 Density Matrix — 2026-03-31 — Polished 6.1.1 (added Overview, Expectation Values, Time Evolution sections; fixed nested admonitions, duplicate boxes); rewrote 6.1.2 as Entropy (von Neumann entropy, max-entropy principle, thermal state, partition function); rewrote 6.1.3 as Quantum Statistics (Bose-Einstein, Fermi-Dirac from single mode, classical limit); renamed files (partial-trace→entropy, entropy→quantum-statistics); updated _toc.yml + cross-refs in 6.2.1/6.2.2; updated parent Overview; fixed LaTeX corruption in 6.1.3 Prompts; all 6 notebooks validated OK
- [x] 5.1 Time-Independent Perturbation Theory — 2026-03-31 — Added ### Overview to all 3 subsections; fixed broken caution admonition + important admonition in 5-1-1; fixed 41 double-brace LaTeX escapes + restructured cell 2 in 5-1-2; updated parent notebook Overview (Hellmann-Feynman as organizing principle, fixed keywords); all 4 notebooks validated OK
- [x] 3.1 Quantization — 2026-03-31 — Rewrote 3.1.1 as Geometric Optics (particle theory, Fermat, Snell); added ### Overview to 3.1.2 Physical Optics; rewrote 3.1.3 as Particle-Wave Unification (Action=Phase, path integral idea); renamed files + updated _toc.yml + fixed cross-refs; updated parent notebook Overview; all 4 notebooks validated OK
- [x] 3.3 Stationary Phase — 2026-03-31 — Added ### Overview to all 3 subsections; fixed broken #::: admonition in 3-3-2-wkb; updated parent notebook Overview (removed erroneous instanton references, fixed 3.3.3 keywords); all 4 notebooks validated OK
- [x] 3.4 Imaginary Time — 2026-03-31 — Added ### Overview to all 3 subsections (Wick Rotation, Statistical Mechanics, Instantons); fixed broken #::: admonition in 3-4-1; fixed broken 4-5-3-topology cross-ref in 3-4-3; fixed duplicate eq-snell-law label in 3-1-2 (→ eq-snell-refraction); all 5 notebooks validated OK
- [x] 3.2 Propagator — 2026-03-31 — Reordered 3.2.2↔3.2.3 (Schrödinger Equation now 3.2.2, Free Particle Propagator now 3.2.3); added ### Overview to all 3 subsections + updated parent Overview; fixed cross-refs in 3-2-1 and 3-3-1; updated _toc.yml; all 5 notebooks validated OK
- [x] 2.3 Anyons — 2026-03-31 — Added ### Overview to all 3 subsections; fixed Summary format in 2.3.2 (admonition→heading); all 4 notebooks validated OK
- [x] 2.2 Angular Momentum — 2026-03-31 — Added ### Overview to all 3 subsections; added spin-1 3×3 matrices to 2.2.1; validated all notebooks OK
- [x] 2.1 Bosons and Fermions — 2026-03-31 — Fixed invalid `dropdown information` admonition class in 2.1.2, fixed HW8/HW10 Jordan-Wigner cross-refs, added mode label α note in 2.1.1; all 4 notebooks validated OK
- [x] 1-1-1-what-is-a-qubit.ipynb — 2026-03-30 — Full rewrite: narrative intro, physical realizations table; renamed from spins-and-qubits
- [x] 1-1-2-state-and-representation.ipynb — 2026-03-30 — Rewrote overview, added outer-product row, fixed \vert
- [x] 1-1-3-hermitian-operators.ipynb — 2026-03-30 — Full rewrite: why Hermitian, spectral decomp, two Pauli tables
- [x] 1-2-1-measurement-postulate.ipynb — 2026-03-30 — Full rewrite: SG experiments, PSD/projection, three-axiom box
- [x] 1-2-2-uncertainty-and-incompatibility.ipynb — 2026-03-30 — Full rewrite: commutator, Robertson uncertainty
- [x] 1-2-3-measurement-operators.ipynb — 2026-03-30 — Full rewrite: projectors, Bayesian updating, degenerate measurements
- [x] 1-3-1-unitary-evolution.ipynb — 2026-03-30 — Full rewrite: unitary operators, Hermitian generators, Schrödinger eq
- [x] 1-3-2-schrodinger-picture.ipynb — 2026-03-30 — Full rewrite + rename from spin-dynamics
- [x] 1-3-3-heisenberg-picture.ipynb — 2026-03-30 — Full rewrite: Heisenberg picture, conserved quantities, Lie groups
- [x] 6.3 Generalized Measurement — 2026-04-01 — Added ### Overview to all 3 subsections; fixed broken #::: Born Rule admonition in 6.3.1; fixed nested admonition (Discussion inside Definition) in 6.3.3; reformatted 6.3.3 homework (removed banned ### Problem N: format and --- separators); consolidated duplicate Naimark content in 6.3.2; trimmed tangential sections (weak measurement, IC-POVM, Choi-Jamiołkowski details, erasure channel, channel capacity); updated Prompts to 4 questions each; updated parent Overview (keywords, Key Concepts, Learning Objectives); all 4 notebooks validated OK
- [x] 6.4 Open Quantum Systems — 2026-04-01 — Added ### Overview to all 3 subsections; rewrote decoherence as quantum channel framing in 6.4.1; added toric code connection + threshold theorem to 6.4.3; removed tangential sections (Quantum Darwinism, teleportation, BB84); fixed homework format (### Problem → **N.**); updated parent Overview; all 4 notebooks validated OK
- [x] 6.2 Entanglement — 2026-04-01 — Added partial trace section to 6.2.1 (was only a reference); added entanglement entropy to 6.2.1 per outline; added ### Overview to all 3 subsections; moved Bell states definition to 6.2.2; added hierarchy of correlations (PPT, negativity) to 6.2.2; removed Bell states section from 6.2.3 (now in 6.2.2); expanded teleportation protocol in 6.2.3; updated parent Overview (Core Questions, expanded Key Concepts + Learning Objectives); fixed LaTeX corruption in 6.2.1 homework (\frac, \rangle escape chars); fixed cross-refs (6-1-1-mixed-states, 6-1-2-entropy); all 4 notebooks validated OK

- [x] 4.4 Spin and Monopole — 2026-04-01 — Rewrote 4.4.1 "Orbital vs Spin"→"Classical Spin" (classical top, Larmor precession, gyromagnetic ratio, Stern-Gerlach puzzle, preview of monopole resolution); added ### Overview to 4.4.2 Dirac Monopole and 4.4.3 Monopole Harmonics; added Berry phase connection section to 4.4.3 (Berry curvature of spin-1/2 = monopole field in parameter space); added ### Summary to 4.4.2 and fixed Summary format in 4.4.3; fixed homework format in 4.4.2/4.4.3 (removed banned --- separators, standardized numbering); renamed 4-4-1-orbital-vs-spin.ipynb→4-4-1-classical-spin.ipynb; updated _toc.yml, parent Overview (duplicate admonition removed, keywords→Core Questions, updated motivating paragraph + Key Concepts + Learning Objectives); fixed cross-refs in 4-4-2, 4-4-3, 2-2-2-spin-representations; all 5 modified notebooks validated OK
- [x] 4.5 CLEANUP — 2026-04-01 — Blanked old 4.5 Berry Phase files (4-5-berry-phase, 4-5-1-berry-phase, 4-5-2-applications, 4-5-3-topology); removed 4.5 entries from _toc.yml, index.md, ch4 index.md; fixed cross-ref in 3-3-3-bohr-sommerfeld-quantization (4-5-1→4-2-1); all validations passed

- [x] 1.1 States and Observables — 2026-04-01 — Parent overview update: rewrote motivating paragraph, converted Lessons/Keywords table to Topics/Core Question format, tightened Key Concepts (added global phase, Bloch sphere) and Learning Objectives (4 items); validated OK
- [x] 1.2 Measurement — 2026-04-01 — Parent overview update: converted Lessons table to Topics format, tightened motivating paragraph and Key Concepts/Learning Objectives; validated OK
- [x] 1.3 Time Evolution — 2026-04-01 — Parent overview update: converted to Topics/Core Question format, condensed Key Concepts from 9 to 6 items (cut Ehrenfest, stationary states, superposition dynamics as covered in subsections), reduced Learning Objectives from 10 to 4; validated OK
- [x] 2.1 Bosons and Fermions (deep polish) — 2026-04-01 — Trimmed 2-1-2 Symmetrization from 24K→15K chars: consolidated overlapping creation/annihilation operator sections (two 7K+ subsections) into one concise 4K section; removed 4 verbose worked examples (kept 1 concise fermion-sign example + 1 derivation dropdown); added forward reference to §2.1.3 for full algebra; updated Prompts (5→4 focused questions); updated parent Overview (Keywords→Core Question format in Topics table, tightened Key Concepts and Learning Objectives); 2-1-1 and 2-1-3 already well-polished from prior runs; both modified notebooks validated OK

- [x] 2.2 Angular Momentum (deep polish) — 2026-04-01 — Trimmed 2-2-1 (14K→10K): tightened prose, added SU(2)/Lie algebra connection to §1.3.3, consolidated redundant sections; trimmed 2-2-2 (20K→8K): removed tangential sections (product states, entanglement, Stern-Gerlach, Bell) that belong in §1.2.1/§6.2, kept core spin definition/spinor rotations/spin-1/general-j/spatial+spin; trimmed 2-2-3 (12K→6K): tightened CG treatment, removed Bell discussion, highlighted singlet as maximally entangled; updated all Prompts (6→4 questions each); updated all Homework (aligned with new content); updated parent Overview (Keywords→Core Question format, tightened Key Concepts and Learning Objectives); all 4 notebooks validated OK

- [x] 2.3 Anyons (deep polish) — 2026-04-01 — Updated Prompts in 2.3.1 (3→4 questions) and 2.3.2 (3→4 questions); fixed "excitation excitation" typo in 2.3.2; added Emergent Statistics section to 2.3.2 per outline; updated parent Overview (Keywords→Core Question format in Topics table, tightened Key Concepts and Learning Objectives); all 4 modified notebooks validated OK

- [x] 5.1 Time-Independent Perturbation Theory (deep polish) — 2026-04-01 — Fixed 5.1.1: removed prose before Overview, removed redundant "What is Perturbation Theory?" section (3K chars), fixed level-4 headings, fixed .ipynb links; fixed 5.1.2: removed duplicate Problem Setup section (5K chars), removed duplicate Second-Order Energy Correction box (1.1K chars), removed redundant Level Repulsion and State Hybridization sections (2K chars), added proper ### Summary, fixed level-4 headings; fixed 5.1.3: fixed 3 broken #::: admonitions (now render as proper collapsible boxes), removed prose before Overview, fixed level-4 headings, reordered Comparison before Summary, trimmed Prompts from 6→5 questions; all 4 notebooks validated OK


- [x] 3.2 Propagator (deep polish) — 2026-04-01 — Fixed 3 broken #::: admonitions in 3.2.2 (Derivation: Time Derivative, Laplacian of Free, Adding Potential — now render as collapsed dropdown info boxes); fixed broken seealso link in 3.2.3 (title "3 2 3 Schrodinger Equation" → "3.2.2 Schrödinger Equation", bad link 3-2-3-schrodinger-equation → 3-2-2-schrodinger-equation); restructured 3.2.1 cell 2 (moved appendix derivation blocks + seealso to before ### Summary for correct flow); updated 3.2.1 Prompts (replaced Wick rotation question with time-slicing question); fixed seealso titles in 3.2.1 (3.1.3 renamed to Particle-Wave Unification, removed .ipynb extensions); updated parent 3.2 to Topics/Core Question format (Lessons→Topics, Keywords→Core Questions with actual questions per subsection); all 4 notebooks validated OK
- [x] Ch1 Discussion boxes fix — 2026-04-01 — Added missing Discussion boxes to 4 Ch1 subsections (1-1-3-hermitian-operators, 1-2-2-uncertainty-and-incompatibility, 1-3-2-schrodinger-picture, 1-3-3-heisenberg-picture). These were lost during the 2026-03-30 full rewrites. Topics: non-Hermitian observables (1.1.3), measurement disturbance vs intrinsic uncertainty (1.2.2), quantum control limits/decoherence (1.3.2), symmetry vs dynamics (1.3.3). All 4 notebooks validated OK

- [x] 3.3 Stationary Phase (deep polish) — 2026-04-01 — Trimmed 3.3.1 (17K→12K): removed redundant Definition box, consolidated prose, added Semiclassical Propagator important box, tightened Summary (6→4 bullets); trimmed 3.3.2 (16K→10K): removed Bohr-Sommerfeld overlap (fully in 3.3.3), consolidated WKB hierarchy into single important box, trimmed Summary (9→4 bullets); trimmed 3.3.3 (17K→13K): cut verbose EBK/Accuracy sections to dropdown note, added "Quantization = Constructive Interference" important box, tightened Summary (9→4 bullets); fixed seealso links in all 3 (removed .ipynb extensions, fixed ugly titles); updated all Prompts (5→4 questions each); updated parent Overview (Lessons/Keywords→Topics/Core Question format); all 4 notebooks validated OK

- [x] 2.3.3 Toric Code (feedback fix) — 2026-04-01 — Fixed corrupted LaTeX in Overview: \\varepsilon (\\x0b control char from unescaped \\v) and \\times (tab from unescaped \\t); validated OK
- [x] 3.1 Quantization (deep polish) — 2026-04-01 — Trimmed 3.1.2 Physical Optics (7.6K→5.0K chars): consolidated verbose Phase section into dropdown note, added Interference section (Young's double slit, $I=|\psi|^2$ foreshadowing Born's rule) per outline; added Discussion boxes to all 3 subsections (Fermat saddle points in 3.1.1, double-slit electrons in 3.1.2, tunneling paths in 3.1.3); updated 3.1.2 Prompts (added interference question); updated parent Overview (Lessons→Topics header); all 5 notebooks validated OK
- [x] 3.4 Imaginary Time (deep polish) — 2026-04-01 — Fixed seealso titles in all 3 subsections ("3 4 N" → "3.4.N" format); trimmed Summary bullets (8-9→4-5 each); restructured 3.4.3 Instantons cell 2 to follow the outline's three-step derivation (eigenstate expansion → dilute instanton gas → matching); updated 3.4.3 Prompts to 4 questions; fixed broken eq-kink-instanton cross-ref in 3.4.3 homework; updated 3.4.1 homework format (Problem X.Y.Z.N: Title → N. italicized-title); all 3 notebooks validated OK


- [x] Consistency audit — 2026-04-01 — Fixed 20 parent notebooks (all x.y units): (1) renamed `## Projects`→`## Project` in all 20; (2) renamed `### Lessons`→`### Topics` in 13 notebooks; (3) converted Keywords columns to proper Core Questions in 5 notebooks (3.4, 4.1, 5.1, 6.3, 6.4); (4) removed extra `### Core Questions` standalone section in 6.4. Chapter landing pages (ch1–ch6 index.md): structure confirmed consistent — all follow same format (heading, `## Units` table, `## Review & Summary` with glossary). All 20 notebooks validated OK.


- [x] 5.2 Time-Dependent PT (deep polish) — 2026-04-01 — Trimmed 5.2.1 (18K→9K): removed redundant "Perturbative Expansion" and "Virtual Processes" sections, trimmed Green's function section to retarded propagator + brief Feynman diagram intro, trimmed Summary (10→4 bullets), updated Prompts (removed Lippmann-Schwinger/Born series references); fixed 5.2.2: removed duplicate `example` admonition on selection rules (was preceded by identical `important` box), removed redundant "Interpreting Forbidden Transitions" section, trimmed Summary (8→4 bullets); added missing Discussion box to 5.2.3 (Hall conductance quantization); all 3 notebooks validated OK

- [x] 3.1.1 Geometric Optics (outline alignment) — 2026-04-02 — Added historical Newton vs Huygens framing to Overview; added "The Particle Theory of Light" section (v=c/n, three geometric laws table, diffraction/interference limitation); updated Prompts (4→5 questions, now includes corpuscle theory + action parallel + diffraction limitation); added HW problem 6 (Foucault experiment: which theory wins, and does Fermat's principle depend on direction of speed change?); updated Summary to include historical debate and limitation; validated OK
- [x] 1.1.1 Qubits (homework outline alignment) — 2026-04-02 — Replaced 7 Stern-Gerlach-focused homework problems with 7 problems aligned to the lesson content per outline directive "[don't deviate to discuss spins and SG experiments]". New problems cover: (1) Born's rule and sign vs probability, (2) normalization calculation, (3) global phase is unobservable (proof), (4) parameter counting → 2-sphere, (5) classical bit vs qubit information capacity, (6) physical realizations with energy gaps and gate types, (7) thermal energy scales for photon vs superconducting qubits. Validated OK
- [x] 1.1.3 Hermitian Operators (outline alignment) — 2026-04-02 — Improved per outline: (1) made "counting dof" argument explicit with general 2×2 Hermitian matrix form showing 4 real parameters; (2) wrapped general expectation value rule and Pauli expectation values (both α,β and θ,φ forms) in `important` boxes for visual prominence; (3) combined verification into single `dropdown information` block that also derives the θ,φ form from the α,β form by substituting the Bloch parametrization; (4) fixed bare `i` → `\mathrm{i}` typos in Homework Problems 1 and 2 (lower-left matrix entries). Validated OK
- [x] 1.3.1 Unitary Evolution (outline alignment) — 2026-04-02 — Added phase factor motivation (z*z=1 → e^{iθ} analogy for unitary operators); added spectral decomposition method for computing matrix exponentials (important box with formula + derivation dropdown + σ^z worked example); added derivative extraction of generator (G = -i dU/dθ at θ=0, infinitesimal form); updated Prompts (5 questions, now covers spectral decomposition and generator extraction); updated Homework (9 problems, added spectral decomposition computation #2, generator extraction #3, explicit eigenvalue computation #9); updated Summary (7→8 bullets, includes spectral decomposition and derivative extraction). Validated OK
- [x] 1.1.2 State and Representation (outline alignment) — 2026-04-02 — Added explicit orthonormal basis definition (important box) to math preparation section; added conversion tip (hint box) for ket↔vector notation per outline; consolidated X/Y/Z bases section into single comprehensive table (outline: "make a table to spell out their basis states"); moved inverse relations and basis change example to dropdown note; enhanced narrative flow from parameter counting → "just parameters" → "aha, they parametrize a sphere"; tightened Prompts from 5→4 questions aligned to new content flow; removed redundant seealso box (links now inline). Validated OK
- [x] 1.2 Measurement (outline alignment) — 2026-04-02 — Changed SG experiment admonitions in 1.2.1 from `example` (visible) to `dropdown information` (collapsed) per outline directive; fixed typo "perserving"→"preserving" in 1.2.3; fixed equation label typo `eq-schrodinger-equantion`→`eq-schrodinger-equation` in 1.3.2; fixed seealso links in 1.3.2 (removed .ipynb extensions, updated "Spins and Qubits"→"Qubits" title); fixed .ipynb link extensions in 1.1.1 seealso box; all 4 modified notebooks validated OK
- [x] Admonition class audit — 2026-04-02 — Audited all 84 source notebooks (204 `important` boxes). Downgraded 13 to `note` (supplementary properties/context: Key Properties in 6.1.2/6.2.2/6.4.2, The Hierarchy in 6.2.2, SQUID Sensitivity in 4.2.2, Key Result in 3.4.2, Quantum-to-classical in 3.2.1, Maximal Entanglement in 6.2.2, Landau Gauge Reduction + Two Ladder Operators + Magnetic Length recap in 4.3.2, Orbital Period in 4.3.1, Gaussian Integrals + Propagator→Schrödinger + Wavepacket in 3.2.3, Pulse Durations in 1.3.2). Downgraded 6 to `attention` (subtle insights: Gauge=Redundancy + All Gauges Identical in 4.1.3, String is Gauge-Dependent in 4.4.2, Quantization=Interference in 3.3.3, Path Integral↔Schrödinger in 3.2.2, Wick Rotation in 3.4.1). Renamed 6 generic titles (Definition→specific, Key X→descriptive, Important→Entanglement Witness Completeness). Final count: 185 `important` boxes, all core definitions/theorems/equations. 18 notebooks modified, all validated OK.
- [x] Cross-reference link fix (25 notebooks) — 2026-04-02 — Removed .ipynb extensions from all markdown cross-reference links across 25 notebooks (Ch2–Ch6). Fixed 17 broken/wrong links: corrected 6 wrong titles (e.g., "Aharonov-Bohm Effect"→"Berry Phase" for 4-2-1, "Orbital vs Spin"→"Classical Spin" for 4-4-1, "3 2 1"→"3.2.1" format), fixed 4 wrong targets (nonexistent files like 4-1-index, 3-0-index, 6-2-index, 4-1-2-berry-phase), corrected 1 wrong section number ("6.1.3 Entropy"→"6.1.2 Entropy"). All 84 notebooks validated OK.
- [x] 5.2.2 Fermi's Golden Rule (deep trim) — 2026-04-02 — Trimmed cell 2 from 16K→9K chars: removed redundant Applications subsection (content already in 5.2.3), consolidated Sinc Function and Resonance section, shortened Validity Conditions to single caution box, tightened Selection Rules (removed verbose "Symmetry-Based Constraints" subheading), trimmed Adiabatic Theorem section (shorter derivation, condensed Berry phase connection); trimmed homework from 8 verbose problems to 8 concise problems (removed oscillator strength problem, added adiabatic/Berry phase problem); updated Summary to 4 concise bullets. Validated OK.
- [x] 3.2.1 Path Integral Formulation (outline alignment + trim) — 2026-04-02 — Trimmed cell 2 from 16K→9K chars: removed redundant Action/Lagrangian/Euler-Lagrange section (already covered in §3.1.3), removed verbose Physical Interpretation section (repeats §3.1.3 punchline), collapsed composition property proof into one-line derivation, moved "Free Particle as Motivation" and normalization derivations to §3.2.3 where they belong. Added: prominent K=⟨x_f|U|x_i⟩ connection to time-evolution operator (per outline), time-sliced path integral formula in important box (per outline "state in box, derivation in dropdown"), short-time propagator Trotter-Suzuki derivation in dropdown. Trimmed Summary from 7→4 bullets, Prompts from 5→4 questions. Validated OK.
- [x] 3.2.2 Schrödinger Equation (outline trim) — 2026-04-02 — Trimmed cell 2 from 13.5K→7.8K chars: removed tangential sections (Time-Independent SE, Normalization/Probability Conservation, Classical-Quantum Correspondence note) that are covered elsewhere or not in outline; tightened derivation flow to focus on the outline’s core arc (infinitesimal time step → SE → two equivalent formulations); reformatted Two Equivalent Formulations as comparison table in important box; updated Prompts (5→4 questions), trimmed Homework (8→8 problems, removed references to deleted content). Validated OK.
- [x] 3.2.3 Free Particle Propagator (trim) — 2026-04-02 — Removed duplicate Classical-Quantum Correspondence note (covered in §3.3); tightened Summary from 6→4 bullets. Cell 2: 13.0K→12.3K chars. Validated OK.
- [x] 2.1.2 Symmetrization (outline alignment) — 2026-04-02 — Removed redundant "Creation and Annihilation Operators" section (4K chars, duplicated §2.1.3 content); replaced with brief forward-reference to §2.1.3; updated Prompts (replaced creation/annihilation question with Pauli exclusion consequences question); replaced HW7 (Fock state induction, now in §2.1.3) with insertion-rule construction of three-boson state; updated Summary (removed creation/annihilation bullet, added forward-ref). Cell 2: 14.8K→10.8K chars. Validated OK.

- [x] Identity operator notation unification — 2026-04-02 — Unified identity operator symbol across 4 notebooks: replaced `\mathbb{I}` → `\hat{I}` in 5-1-1 (1 instance), 5-1-3 (6 instances), 5-2-1 (4 instances); replaced `\mathbb{1}` → `\hat{I}` in 6-1-2 (4 instances, identity matrix context). Now consistent with Ch1 convention (`\hat{I}` throughout). Note: `\mathbb{1}` in 2-1-2 left unchanged (represents tensor algebra vacuum state, not identity operator). Remaining `\mathbb{C/R/Z/CP}` are standard number field notations, not identity operators. All 4 modified notebooks validated OK.


- [x] 5-1-1-toy-model structural fix — 2026-04-02 — Added `important` admonition boxes for two key results: (1) Exact Eigenvalues box with level repulsion statement, (2) Convergence Criterion box with general rule and qubit specifics. Removed redundant paragraphs now consolidated in boxes. Validated OK.
- [x] 6-1-1-mixed-states structural fix — 2026-04-02 — Added missing Discussion box (`:class: dropdown tip`) on ensemble ambiguity and the nature of entropy (placed before Bloch Ball section). All 63 subsection notebooks now pass full structural check (Overview, Summary, Discussion, important boxes). Validated OK.

- [x] 6-1-1-mixed-states content trim — 2026-04-02 — Trimmed cell 2 from 16.6K→8.5K chars: consolidated Pure States + Mixed States + Valid Conditions into single Definition box; collapsed verbose examples (Qubit in Superposition, Maximally Mixed, Thermal State, σ^z expectation) into dropdown examples or removed; removed redundant Properties proof section; moved von Neumann equation derivation to dropdown; tightened Prompts (5→4 questions). All content preserved, just more concise. Validated OK.
- [x] 4-1-3-gauge-invariance content trim — 2026-04-02 — Trimmed cell 2 from 15.8K→7.6K chars: removed duplicate gauge transformation rules (was stated in prose then again in box), consolidated gauge-invariant/dependent bullet lists into single table, removed verbose "What Does Same Physical State Mean?" subsection (point already made in Redundancy box), consolidated two redundant attention boxes into one, shortened gauge fixing section. All physics preserved. Validated OK.
- [x] 5.1 Time-Independent PT (deep content trim) — 2026-04-02 — Trimmed all 3 subsections per outline: 5.1.1 Toy Model (16.5K→6.9K chars: removed redundant Overview bullet list, verbose "Power Series" section, "Graphical Insight" section; tightened Summary to 4 bullets; homework 8→7 problems); 5.1.2 Non-Degenerate PT (17.4K→9.0K chars: removed triple-redundant E_n^(1) formula, merged two important boxes into Hellmann-Feynman as organizing principle per outline, collapsed Qubit Revisited example to dropdown, added Physical Intuitions section; homework 8→7 problems); 5.1.3 Degenerate PT (21.3K→10.1K chars: added Generalized Hellmann-Feynman framing per outline, collapsed Stark effect to dropdown, removed verbose "Main Takeaways" note, simplified projection operator section, tightened comparison table; homework 8→7 problems). Parent 5-1 already aligned. All 3 notebooks validated OK.
- [x] 1.3 Time Evolution (outline alignment) — 2026-04-02 — Fixed 1.3.2: eliminated 5 level-4 headings (####), fixed spin/QI notation mixing (spin precession section now uses consistent $\hat{\sigma}^z$ + $\vert\uparrow\rangle,\vert\downarrow\rangle$; Rabi section uses $\hat{X}$ + $\vert 0\rangle,\vert 1\rangle$), fixed bare $I$ → $\hat{I}$, trimmed Prompts (5→4). Fixed 1.3.1: notation fix in spectral decomposition example ($\vert 0\rangle$ → $\vert\uparrow\rangle$ with $\hat{\sigma}^z$). 1.3.3 verified clean (no issues). Both modified notebooks validated OK

- [x] 6-2-3 Bell Inequality (content trim) — 2026-04-02 — Trimmed cell 2 from 14.7K→7.7K chars: merged EPR + Local Hidden Variables into single concise section; removed redundant "Interpretation: Nonlocality" section (content already in Bell's Theorem box); condensed Loophole-Free Bell Tests to 1 paragraph + dropdown note; tightened No-Communication proof; condensed Teleportation (kept protocol steps, collapsed example to dropdown, added attention box for no-comm explanation); trimmed Summary from 7→4 bullets; trimmed Prompts from 5→4 questions; trimmed Homework from 10→8 problems (removed redundant product-state and teleportation-explanation problems). Validated OK.

- [x] 4-1-2 Electromagnetic Coupling (content trim) — 2026-04-02 — Trimmed cell 2 from 12.0K→7.0K chars: removed verbose "Physical Interpretation" and "Conceptual Significance" subsections (redundant with important boxes), tightened Lorentz force derivation (moved detail to dropdown), condensed E/B field section, fixed wrong seealso title ("Electromagnetic Coupling"→"Gauge Invariance" for 4-1-3), fixed `::::::` rendering bug (extra colons closing seealso block). All physics preserved (kinetic momentum, Lorentz force, field strength tensor, gauge principle). Validated OK.
- [x] Rendering fixes (3 notebooks) — 2026-04-02 — Fixed `::::::` (6-colon) closing tags in 2-3-1-exchange-statistics (2 instances: nested margin+figure blocks now properly closed with separate `:::` tags); normalized `::::` (4-colon) admonition markers to standard `:::` in 3-1-3-particle-wave-unification (2 admonition opens + 2 closes). All 3 notebooks validated OK.

- [x] 4.4.3 Monopole Harmonics (physics correction + outline alignment) — 2026-04-02 — Fixed critical physics error: replaced incorrect L² eigenvalue formula ħ²l(l+1−2s) with correct total angular momentum J=Λ+s̃r framework where J satisfies standard SU(2) [J_i,J_j]=iħε_{ijk}J_k with j≥|s|; added dropdown derivation showing J=Λ+s̃r cancels the monopole modification to [Λ_i,Λ_j]; removed incorrect eigenvalue in Comparison table, tangential Hopf fibration section, and padding Applications section; aligned with outline’s “SU(2) symmetry: J=L+(monopole contribution), algebra still works, j≥|q|” requirement; fixed HW problem 3 (replaced wrong commutation relation formula with correct J=Λ+s̃r derivation exercise); rewrote Prompts to 4 focused questions; revised HW to 8 problems testing correct physics; validated OK

### In Progress

### Pending

(See Work Order above for the full list with structural notes.)

### Issues

## Workstream 6: Validation

### Last Full Validation
- Date: 2026-04-01
- Result: ALL 84 source notebooks passed validation (structure, \n terminators, no char corruption, no collapsed lines, no banned --- separators)

### Known Issues
- 5.2.3 was trimmed from 21K→6K chars in earlier pass (resolved)
- 1-3-3-heisenberg-picture: math formulas inspected 2026-04-01, no corruption found — LaTeX is clean
- Ch3 dense paragraphs: checked, no collapsed content issues found

## Log

| Date | Agent | Notebook | Action | Notes |
|------|-------|----------|--------|-------|
| 2026-03-28 | — | general | LaTeX convention fix | `\mathrm{i/e/d}` applied to 50/84 notebooks |
| 2026-03-28 | — | progress.md | Rebuild | Progress file corrupted by parallel agents |
| 2026-04-02 | Manager | 2-1-2-symmetrization | Outline alignment | Removed 4K chars redundant with §2.1.3; 14.8K→10.8K |
| 2026-04-02 | Manager | 3-2-1-path-integral-formulation | Outline alignment + trim | 16K→9K chars, added K=⟨x_f|U|x_i⟩, time-slicing box, removed redundant sections |
| 2026-04-02 | Manager | 3-2-2-schrodinger-equation | Outline trim | 13.5K→7.8K chars, removed tangential sections |
| 2026-04-02 | Manager | 3-2-3-free-particle-propagator | Trim | Removed duplicate note, tightened Summary |
| 2026-03-29 | — | 1-3-3-heisenberg-picture | Fix LaTeX | Fixed unescaped imaginary units in Problem 4 |
| 2026-03-30 | — | .claude/ | Infrastructure | Built commands, rules, skills, agents structure |
| 2026-03-30 | — | .claude/ | Admonition redesign | Discussion → `tip` class; full admonition table in rules |
| 2026-03-31 | — | outline.md | Redesign Ch3-6 | Rewrote 3.1 (optics arc), 3.2 (reorder), 3.4.3 (instanton), Ch4 (5→4 units, Berry phase moved to 4.2), Ch5 (Hellmann-Feynman, Kubo), Ch6 (partial trace → 6.2, quantum statistics in 6.1.3) |
| 2026-03-31 | — | progress.md | Audit + rewrite | Full audit of 63 subsections, work order with structural notes |
| 2026-04-02 | Manager | 6-1-1-mixed-states | Content trim | 16.6K→8.5K chars, consolidated definitions, collapsed verbose examples |
| 2026-04-02 | Manager | 4-1-3-gauge-invariance | Content trim | 15.8K→7.6K chars, removed duplicated content, consolidated tables |
| 2026-03-31 | Manager | 2.1 Bosons and Fermions | Polish | Fixed dropdown information→note in 2.1.2, HW cross-refs (Jordan-Wigner→insertion/deletion), added mode label note in 2.1.1 |
| 2026-03-31 | Manager | 2.2 Angular Momentum | Polish | Added ### Overview + spin-1 3×3 matrices to 2.2.1; added ### Overview to 2.2.2 and 2.2.3; converted Summary admonition to heading in 2.2.1; all validated OK |
| 2026-03-31 | Manager | 2.3 Anyons | Polish | Added ### Overview to 2.3.1/2.3.2/2.3.3; fixed Summary admonition→heading in 2.3.2; renamed Summary of Facts→Summary in 2.3.1; all 4 notebooks validated OK |
| 2026-03-31 | Manager | 3.1 Quantization | Polish+Rename | Rewrote 3.1.1→Geometric Optics, polished 3.1.2 (added Overview), rewrote 3.1.3→Particle-Wave Unification; renamed files, updated _toc.yml, fixed cross-refs, updated parent Overview |
| 2026-03-31 | Manager | 3.2 Propagator | Polish+Reorder | Swapped 3.2.2↔3.2.3 (Schrödinger Eq now 3.2.2, Free Particle now 3.2.3); added ### Overview to all 3 subsections; updated parent notebook Overview and Lessons table; fixed cross-refs; updated _toc.yml |
| 2026-03-31 | Manager | 3.3 Stationary Phase | Polish | Added ### Overview to 3-3-1/3-3-2/3-3-3; fixed broken #::: admonition in 3-3-2; updated parent notebook Overview (removed erroneous instanton references, fixed 3.3.3 keywords to Maslov index/harmonic oscillator/hydrogen); all 4 notebooks validated OK |
| 2026-03-31 | Manager | 3.4 Imaginary Time | Polish | Added ### Overview to 3-4-1/3-4-2/3-4-3; fixed broken #::: in 3-4-1; fixed topology cross-ref in 3-4-3; fixed duplicate eq-snell-law label in 3-1-2 (feedback); all 5 notebooks validated OK |
| 2026-03-31 | Manager | 5.1 Time-Independent PT | Polish | Added ### Overview to 5-1-1/5-1-2/5-1-3; fixed broken caution admonition + important admonition in 5-1-1; fixed 41 double-brace LaTeX escapes + restructured cell 2 header in 5-1-2; updated parent notebook Overview (Hellmann-Feynman as organizing principle, corrected keywords); all 4 notebooks validated OK |
| 2026-03-31 | Manager | 6.1 Density Matrix | Polish+Rename+Reshuffle | Polished 6.1.1 (Overview, Expectation Values, Time Evolution); rewrote 6.1.2→Entropy (max-entropy, thermal state); rewrote 6.1.3→Quantum Statistics (BE/FD distributions); renamed files; updated _toc.yml + cross-refs |
| 2026-03-31 | Manager | 5.2 Time-Dependent PT | Polish+Reshuffle | Moved Green's functions/Feynman diagrams 5.2.3→5.2.1; moved adiabatic theorem 5.2.3→5.2.2; rewrote 5.2.3 (harmonic perturbation, dipole transitions, lifetime, Kubo formula); updated all Prompts + parent Overview; validated all 4 notebooks OK |
| 2026-04-01 | Manager | 6.3 Generalized Measurement | Polish | Added ### Overview to 6.3.1/6.3.2/6.3.3; fixed broken admonitions (6.3.1 Born Rule, 6.3.3 nested Discussion); reformatted 6.3.3 HW; consolidated Naimark in 6.3.2; trimmed tangential content; updated Prompts + parent Overview; all 4 notebooks validated OK |
| 2026-04-01 | Manager | 6.4 Open Quantum Systems | Polish | Added ### Overview to 6.4.1/6.4.2/6.4.3; added decoherence=quantum-channel framing to 6.4.1; thermal steady state example to 6.4.2; added toric code + threshold theorem to 6.4.3; removed Quantum Darwinism/teleportation/BB84; fixed HW format; updated parent Overview; all 4 notebooks validated OK |
| 2026-04-01 | Manager | 6.2 Entanglement | Polish+Partial Trace | Added partial trace to 6.2.1, Bell states to 6.2.2, expanded teleportation in 6.2.3; added ### Overview to all 3; updated parent Overview; fixed LaTeX corruption + cross-refs; all 4 notebooks validated OK |
| 2026-04-01 | Manager | 4.2 Berry Phase | Polish+Rename+Restructure | Major restructure: old Flux Ring → Berry Phase. Rewrote 4.2.1 (Berry phase, connection, curvature, Phase=Action), 4.2.2 (AB effect, flux quantization, SQUIDs), 4.2.3 (flux ring model, persistent current, pi-flux degeneracy). Renamed 4 files, updated _toc.yml + index.md + ch4 index.md, fixed cross-refs in 4-1-2/4-1-3/4-4-2. All 8 notebooks validated OK |
| 2026-04-01 | Manager | 4.1 Gauge Field | Polish+Rename | Rewrote 4.1.1→Gauge Principle, 4.1.2→Electromagnetic Coupling, 4.1.3→Gauge Invariance; renamed files, updated _toc.yml, fixed cross-refs in 4-2-1/4-2-3/4-3-1/4-5-1; updated parent Overview; all 5 notebooks validated OK |
| 2026-04-01 | Manager | 4.3 Landau Level | Polish | Rewrote 4.3.1 (added Hall effect, IQHE motivation, magnetic length); rewrote 4.3.2 (Bohr-Sommerfeld, Landau gauge, guiding center, two towers, LLL); rewrote 4.3.3 (charge pumping, FQHE-anyon connection); updated parent Overview; all 4 notebooks validated OK |
| 2026-04-01 | Manager | 4.4 Spin and Monopole | Polish+Rename | Rewrote 4.4.1→Classical Spin (classical top, precession, gyromagnetic ratio, half-integer puzzle); added ### Overview to 4.4.2/4.4.3; added Berry phase connection to 4.4.3; fixed HW format (removed --- and ### Problem N:); renamed file, updated _toc.yml + parent + cross-refs; all 5 notebooks validated OK |
| 2026-04-01 | Manager | 4.5 Berry Phase (old) | Cleanup | Blanked 4 old notebooks, removed from _toc.yml + index.md + ch4 index.md, fixed cross-ref in 3-3-3 (4-5-1→4-2-1); all validations passed |
| 2026-04-01 | Manager | 1.1 States and Observables | Parent Overview | Rewrote motivating paragraph, Topics/Core Question table, tightened Key Concepts + Learning Objectives; validated OK |
| 2026-04-01 | Manager | 1.2 Measurement | Parent Overview | Converted to Topics format, tightened Key Concepts + Learning Objectives; validated OK |
| 2026-04-01 | Manager | 1.3 Time Evolution | Parent Overview | Condensed Key Concepts (9→6), Learning Objectives (10→4), converted to Topics/Core Question format; validated OK |
| 2026-04-01 | Manager | Workstream 6 | Full Validation | Ran full validation across all 84 source notebooks. Fixed: banned --- separators in HW cells of 3-3-3, 4-2-1, 4-2-2, 5-1-3 (32 occurrences); renamed ### Key Takeaways → ### Summary in 5-1-1-toy-model. All 84 notebooks now pass: structure checks, \n terminators, no char corruption, no collapsed lines, no banned patterns |
| 2026-04-01 | Manager | 2.1 Bosons and Fermions | Deep Polish | Trimmed 2-1-2 Symmetrization (24K→15K): consolidated creation/annihilation operator sections, removed verbose examples, updated Prompts; updated parent Overview to Core Question format; validated both notebooks OK |
| 2026-04-01 | Manager | 2.2 Angular Momentum | Deep Polish | Trimmed all 3 subsections (total 46K→25K chars): consolidated redundancies, removed tangential content (SG/Bell/entanglement → proper chapters), added SU(2) connections, updated all Prompts/Homework/parent Overview to Core Question format; all 4 notebooks validated OK |
| 2026-04-01 | Manager | 2.3 Anyons | Deep Polish | Updated Prompts (3→4 questions each in 2.3.1/2.3.2); fixed typo in 2.3.2; added Emergent Statistics section to 2.3.2; updated parent Overview to Core Question format; all 4 notebooks validated OK |
| 2026-04-01 | Manager | Ch1 (4 subsections) | Discussion Fix | Added missing Discussion boxes to 1-1-3, 1-2-2, 1-3-2, 1-3-3 (lost during 2026-03-30 full rewrites); all 4 validated OK |
| 2026-04-01 | Manager | 3.2 Propagator | Deep Polish | Fixed 3 broken #::: admonitions in 3.2.2; fixed broken seealso link in 3.2.3 (3-2-3→3-2-2); restructured 3.2.1 (appendix blocks before Summary, Prompts updated); parent updated to Topics/Core Question format; all 4 notebooks validated OK |
| 2026-04-01 | Manager | 3.3 Stationary Phase | Deep Polish | Trimmed all 3 subsections (total 51K→35K chars): removed redundant Definition boxes, Bohr-Sommerfeld overlap from 3.3.2, verbose EBK/Accuracy from 3.3.3; fixed seealso links; updated Prompts to 4 each; parent to Topics/Core Question format; all 4 notebooks validated OK |
| 2026-04-01 | Manager | 2-3-3-toric-code | Feedback Fix | Fixed corrupted LaTeX (\\varepsilon, \\times control chars) in Overview paragraph; validated OK |
| 2026-04-01 | Manager | 3.1 Quantization | Deep Polish | Trimmed 3.1.2 (7.6K→5.0K), added interference section per outline, added Discussion boxes to all 3 subsections, updated Prompts + parent Topics header; all 5 notebooks validated OK |
| 2026-04-01 | Manager | All 20 parent notebooks | Consistency audit | Fixed `## Projects`→`## Project` (all 20), `### Lessons`→`### Topics` (13 notebooks), Keywords→Core Questions (5 notebooks: 3.4/4.1/5.1/6.3/6.4), removed extra standalone `### Core Questions` from 6.4. Chapter index pages verified consistent. All 20 validated OK |
| 2026-04-01 | Manager | 5.1 Time-Independent PT | Deep Polish | Fixed prose-before-Overview in 5.1.1/5.1.3, 3 broken #::: admonitions in 5.1.3, duplicate content in 5.1.2 (Problem Setup, duplicate E^(2) box, redundant Level Repulsion section); added ### Summary to 5.1.2; reordered 5.1.3 Comparison→Summary; fixed all .ipynb links; all 4 notebooks validated OK |
| 2026-04-01 | Manager | 3.4 Imaginary Time | Deep Polish | Fixed seealso titles (all 3), trimmed Summaries (8-9→4-5 bullets), restructured 3.4.3 to 3-step instanton derivation (eigenstate expansion + dilute gas + matching), fixed broken eq cross-ref + HW format; all 3 notebooks validated OK |
| 2026-04-01 | Manager | 5.2 Time-Dependent PT | Deep Polish | Trimmed 5.2.1 (18K→9K): removed redundant sections, trimmed Green's function to retarded propagator only, updated Prompts; fixed 5.2.2: removed duplicate selection rules example block, removed redundant subsection, trimmed Summary (8→4 bullets); added missing Discussion box to 5.2.3; all 3 validated OK |
| 2026-04-02 | Manager | 3.1.1 Geometric Optics | Outline alignment | Added Newton vs Huygens historical framing, particle theory section (v=c/n, three-law table, diffraction limitation), updated Prompts + HW problem 6 (Foucault experiment); validated OK |

| 2026-04-02 | Manager | 1.1.1 Qubits | Homework outline alignment | Replaced 7 SG-experiment HW problems with 7 lesson-aligned problems (Born's rule, normalization, global phase, parameter counting, classical vs quantum info, physical realizations, thermal scales) |
| 2026-04-02 | Manager | 1.1.3 Hermitian Operators | Outline alignment | Made counting-dof explicit (general 2×2 Hermitian matrix, 4 real params); wrapped expectation value results in `important` boxes; combined verification dropdown with θ,φ derivation; fixed bare `i` typos in HW 1 and 2 |
| 2026-04-02 | Manager | 1.1.2 State and Representation | Outline alignment | Added orthonormal basis definition box, ket↔vector conversion tip, consolidated X/Y/Z basis table, moved inverse relations to dropdown, enhanced parameter→sphere narrative; Prompts 5→4; validated OK |
| 2026-04-02 | Manager | All chapters (18 notebooks) | Admonition class audit | Downgraded 13 `important`→`note` (supplementary), 6 `important`→`attention` (insights), renamed 6 generic titles; 204→185 important boxes; all validated OK |
| 2026-04-02 | Manager | 25 notebooks (Ch2–Ch6) | Cross-ref fix | Removed .ipynb extensions, fixed 17 wrong titles/targets/section numbers; all 84 notebooks validated OK |
| 2026-04-02 | Manager | 5-2-2-fermis-golden-rule | Deep trim | 16K→9K chars: removed redundant Applications (in 5.2.3), trimmed Sinc/Validity/Selection/Adiabatic sections, 8 concise HW problems; validated OK |
| 2026-04-02 | Manager | 4.2.1 Berry Phase, 4.2.2 Aharonov-Bohm | Level-4 heading fix + content trim | Eliminated all level-4 headings in 4.2.1 (5→0) and 4.2.2 (12→0); removed duplicate persistent-current/SQUID sections from 4.2.2 (already in 4.2.3); trimmed 4.2.2 cell 2 from 14.7K→8.4K chars, HW 10→7 problems; trimmed 4.2.1 cell 2 from 10K→8K chars; validated OK |
| 2026-04-02 | Manager | 5-1-1, 5-1-3, 5-2-1, 6-1-2 | Notation fix | \mathbb{I}/\mathbb{1} → \hat{I} (15 replacements across 4 notebooks) |
| 2026-04-02 | Manager | 5-1-1-toy-model | Structural fix | Added 2 important boxes (exact eigenvalues, convergence criterion) |
| 2026-04-02 | Manager | 6-1-1-mixed-states | Structural fix | Added missing Discussion box |
| 2026-04-02 | Manager | 5-1-1, 5-1-2, 5-1-3 | Deep content trim | 5.1.1: 16.5K→6.9K, 5.1.2: 17.4K→9.0K, 5.1.3: 21.3K→10.1K |
| 2026-04-02 | Manager | 1.3 Time Evolution | Outline alignment + notation fix | Eliminated 5 #### headings in 1.3.2, fixed spin/QI notation mixing in 1.3.1/1.3.2, fixed bare I→\hat{I}; both validated OK |
| 2026-04-02 | Manager | 6-2-3-bell-inequality | Content trim | 14.7K→7.7K chars, merged sections, tightened prose |
| 2026-04-02 | Manager | 4-1-2-electromagnetic-coupling | Content trim | 12.0K→7.0K chars, fixed seealso bug + extra colons |
| 2026-04-02 | Manager | 2-3-1, 3-1-3 | Rendering fixes | Fixed ::::::  and :::: directive markers |
| 2026-04-02 | Manager | 3-4-2-statistical-mechanics | Outline alignment | Added Quantum-Classical Correspondence section with important box: "QM at Temperature T = Classical Stat Mech in d+1 Dimensions"; highlights imaginary time as extra dimension with L_τ=βℏ, high-T/low-T limits, practical consequences (lattice QCD, quantum Monte Carlo); validated OK |
| 2026-04-02 | Manager | 4-1-1-gauge-principle | Section header fix | Renamed misleading "### The Lorentz Force from Gauge Invariance" (which contained only a Discussion box, no derivation) to "### From Gauge Symmetry to Electromagnetism"; replaced intro paragraph claiming to show the Lorentz force with accurate forward-reference to §4.1.2; added seealso box pointing to 4-1-2-electromagnetic-coupling; validated OK |

## 2026-04-02 — LaTeX Corruption Fix: Open Quantum Systems
### Fixed
- `6-4-1-decoherence.ipynb` — 46 corrupted LaTeX escape sequences fixed (\\alpha, \\beta, \\varphi, \\vert, \\frac, \\rangle, \\rho, \\text)
- `4-1-1-gauge-principle.ipynb` — 5 corrupted sequences fixed (\\alpha x3, \\boldsymbol, \\to)
- `6-4-2-lindblad-master-equation.ipynb` — 215 corrupted sequences fixed (\\rho x86, \\text x20, \\varphi x13, \\vert x28, \\frac x25, \\rangle x18, \\beta x3, \\bar x4, \\tau x7, \\approx x1, \\right x4, \\times x1, \\to x3)
- All 3 notebooks validated: no corruption, no missing \\n, no collapsed lines.

