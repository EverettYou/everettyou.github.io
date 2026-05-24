# Skill: Homework designer (PHYS130B)

## Role in the stack

**Content designer:** produce problem text, ordering, and **formatting instructions** (or full cell-3 markdown) for **`notebook-writer`** to apply. **Do not** edit `.ipynb` JSON directly. **Do not** run validators. Proof / "show that" **chain** correctness: **`derivation-designer`** before writer implements heavy proofs.

**Homework cell layout:** **`TEMPLATES.md`** (this folder)—match `rules/content-style.md` § Homework and the **gold gallery** in `TEMPLATES.md § 3`.

Workflow for **designing** and **auditing** homework. **Law** (counts, cell placement, banned patterns): **`rules/content-style.md`** § Homework + related bullets; notation and math layout: **`rules/physics-conventions.md`**. This skill adds **distribution, quality principles, and audit recipes**—when something conflicts, the **rule file** wins.

## Activation (auto)

- Designing new homework problems for a subsection notebook (deliver markdown for **`notebook-writer`**).
- Reviewing or auditing existing homework for quality, formatting, or alignment with lecture content.
- Specifying fixes for homework formatting (bold markers, sub-parts, display math spacing, etc.).
- Responding to feedback items about homework quality or style.
- **Phase C** (style) pass in **`.claude/README.md`** / **`skills/maintenance-phases/SKILL.md`** when the homework cell needs a deep audit or rewrite.

## Non-goals

- Mathematical correctness of **proof-style** "show that" chains — hand off to **`derivation-designer`** (this skill owns problem **design**, not step-by-step proof QC).
- JSON / cell-level notebook editing mechanics — hand off to **`notebook-writer`**.
- Lecture narrative changes outside the homework cell — hand off to **`lecture-designer`**.

---

## 1. Teaching Context

### Why homework matters in 2026

LLMs solve undergraduate physics homework at or above student level. Students work with AI on homework and are graded on submission, not correctness. **The same problems appear on the final exam (in-person, no AI).** Homework must therefore build *internalized understanding* — worldview (世界观) and method (方法论) — not just procedural skill.

### What homework must achieve

- **Build worldview**: problems that force the student to hold a mental model, not just follow steps.
- **Prepare for the exam**: a student who truly understood the homework (not just copied AI output) can solve exam variants.
- **Reveal physics**: every problem should surface a phenomenon, a connection, a misconception, or a method the student would not otherwise internalize.

### Difficulty distribution and lecture-connectedness

Each subsection notebook should have **7–8 problems** in a graded mix. The mix matters as much as the problems themselves.

**Required composition for a 7–8 problem set:**

| Bucket | Count | Role |
|--------|-------|------|
| **Near-lecture application** (Transfer §2.1 of a definition/formula to a concrete case) | **at most 2** | Build fluency; not a vehicle for proving lecture content. |
| **Transfer / Comparison / Guided derivation** (§2.1, §2.4) | 2–3 | Adapt lecture material to a related setting; compare methods or representations. |
| **Connection / Misconception / Inversion / Edge case / Approximation** (§2.2, §2.3, §2.5, §2.6, §2.8) | **at least 3** | Reveal a phenomenon, link to another area of physics, expose a wrong intuition, or build approximation-method skill. **This is where the bar lives.** |

**Hard caps:**

- Near-lecture problems cap at 2 — a fluency problem is a *tool*, not a deliverable. Beyond 2, the set drifts into drill.
- At most **one** "show that [result already in the lecture]" problem per set, and only if it adds a non-obvious twist (a different system, an inverted direction, a positivity bound). Direct lecture-proof rehashes are §3.1 anti-patterns.
- **Every problem** must pass §2.7 *Physics payload* — no exceptions, even for the near-lecture bucket. A trivial-substitution problem fails §2.7 even if it would otherwise slot as "easy/near-lecture."

**Anti-pattern (§3.6):** All problems too far from lecture. Students need the first 2 problems to be solvable using only the lecture content — but those 2 problems still must be physically meaningful, not mechanical substitutions.

---

## 2. Quality Principles — What Makes Homework Meaningful

Every problem must satisfy **at least one** of §2.1–§2.6 or §2.8 **and** §2.7 (mandatory). A problem that nominally satisfies a principle but fails §2.7 is rejected.

### 2.1 Transfer

> Apply a concept or method to a new context not shown in lecture.

The lecture proves a theorem for spin-1/2; the homework asks the student to work it out for spin-1. The lecture derives the Heisenberg evolution for Pauli operators; the homework transfers it to the harmonic oscillator (see Gold 1 in `TEMPLATES.md`). **The student must adapt, not copy.**

### 2.2 Inversion

> Reverse the logical direction of a lecture derivation.

The lecture derives the output from the input; the homework gives the output and asks "what input produces this?" Example: lecture builds the angular momentum algebra from rotation generators; homework gives the algebraic relations and asks the student to identify the representation by positivity bounds (Gold 3 in `TEMPLATES.md`).

### 2.3 Edge Cases and Limits

> Explore what happens at boundaries, special values, or limiting regimes.

What happens when the coupling goes to zero? When two energy levels become degenerate? When the system size goes to infinity? Edge cases reveal whether the student truly understands the structure or just memorized the generic formula. A "degenerate eigenspace" measurement (see Gold 5) is an edge case the generic formula does not cover.

**Sanity-check role.** The best edge-case problems double as **verification**: the answer must reduce, in a named limit, to a previously-established result — the lecture's small-coupling formula, the classical limit ($\hbar \to 0$ or $S/\hbar \to \infty$), a free-particle case, a dimensional bound. An explicit "verify your answer in the limit $X \to 0$ recovers result $Y$" sub-part is encouraged — it teaches the student to interrogate AI-generated solutions by checking limits, the most generally transferable scientific-method skill.

### 2.4 Comparison

> Compare two methods, representations, or approximations on the same problem.

Solve the same problem in the Schrödinger and Heisenberg pictures. Compare exact and perturbative results. Use both position and momentum representations. Measure $\hat{H}$ versus $\hat{H}^2$ on the same state. This builds judgment about when to use which tool.

### 2.5 Connection

> Link the current topic to a different part of the course or to a different area of physics.

Show that a quantum result reduces to the classical limit. Connect an entanglement measure to a thermodynamic quantity. Show that two bosonic modes realize the angular momentum algebra (Schwinger boson, Gold 2). Use Clebsch–Gordan to compute hydrogen 2p fine structure (Gold 4). **These problems build the knowledge graph and are the most exam-worthy.**

### 2.6 Misconception Testing

> Design a problem where a common wrong approach gives a specific wrong answer.

The student must recognize why the naive method fails and apply the correct one. Example: using non-degenerate perturbation theory on a degenerate level gives a divergent answer — the student must recognize and switch to degenerate perturbation theory. Or: assuming a global phase is observable in a single-system measurement (it's not) but becomes physical in interference (it is).

### 2.7 Physics payload (mandatory)

> After solving this problem, can the student name a concept, phenomenon, connection, or method they now appreciate that they did not before?

If the answer is **"they can now perform a 2×2 matrix multiplication"** or **"they can plug a number into λ = h/p"**, the problem fails this criterion. It is mechanical, not pedagogical, regardless of which formal principle (§2.1–§2.6) it nominally satisfies.

A problem may be 100% computational *and* still satisfy §2.7 — but only if the computation reveals something. Example: HW 2-1-3 #9 (equal partition theorem) is fully computational, but the punchline is that the harmonic oscillator obeys classical equipartition state-by-state and on time-average — a non-obvious physical insight. That problem passes. A problem that asks "compute $[\hat{X},\hat{Z}]$ by matrix multiplication" produces no insight beyond what the lecture already stated; it fails.

**The §2.7 test, applied as a one-sentence claim:** before drafting, write one sentence beginning "After this problem, the student will understand that…" If the completion is a fact already stated in the lecture, or a manipulation already drilled in a previous chapter, redesign.

**Visual / geometric representation booster.** Problems that force translation between formal expressions and a **geometric picture** (Bloch-sphere rotation, energy-level diagram, phase-space picture, phasor / phase-circle diagram, propagator-path sketch, Feynman-diagram skeleton) reliably satisfy §2.7. Not a separate principle, but a strong indicator of pedagogical value — quantum-mechanics worldview is largely about internalizing the right pictures, and the student should be asked to draw or describe them when natural.

### 2.8 Approximation reasoning

> Order-of-magnitude reasoning grounded in an **explicitly named approximation method**, never in "everyday intuition" — quantum mechanics has none, and "common sense" estimation does not transfer.

The student must (i) **name the principle** invoked — uncertainty relation, dimensional analysis from fundamental constants, virial-theorem scaling, energy minimization (variational), WKB / imaginary momentum, perturbative expansion in a small parameter — (ii) use it to derive a scale, rate, or bound, and (iii) **compare** the result to another scale or to an experimental value. All three steps are mandatory; an estimation problem missing any one is rejected.

*Good examples (principle named, comparison made):*

- Estimate the hydrogen ground-state radius and energy by minimizing $\langle\hat{H}\rangle \sim \hbar^2/(2m\Delta x^2) - e^2/(4\pi\epsilon_0\Delta x)$ over $\Delta x$, using $\Delta x\,\Delta p \sim \hbar$. Recover the Bohr radius as the minimizer; compare to experimental $a_0$. *Basis: uncertainty relation + variational minimization.*
- Estimate the lifetime of a quasi-bound state of width $\Delta E$ from $\Delta t \sim \hbar/\Delta E$. Compare to the classical traversal time of the well. *Basis: time–energy uncertainty.*
- Estimate the tunneling decay rate through a square barrier of height $V_0 > E$ and width $L$ from $\kappa \sim \sqrt{2m(V_0 - E)}/\hbar$ and rate $\sim \mathrm{e}^{-2\kappa L}$. Apply to alpha decay of $^{238}\mathrm{U}$ (give the order-of-magnitude lifetime; compare to $4.5 \times 10^9$ yr). *Basis: WKB / imaginary momentum.*
- Estimate the magnetic field at which an electron's cyclotron radius at room temperature ($\tfrac{1}{2}m v_{\mathrm{th}}^2 \sim k_B T$) equals the copper lattice spacing. Is the regime experimentally accessible? *Basis: scale-matching with named velocities.*

*Rejected examples (no basis, or single-substitution):*

- ❌ "Estimate the de Broglie wavelength of an electron in a metal." No approximation principle named; relies on an undefined Fermi velocity. (If the problem first guides the student to $v_F \sim \hbar/(m a)$ from confinement at lattice spacing $a$ via the uncertainty relation, *then* it becomes §2.8 — but the principle must appear explicitly.)
- ❌ "Estimate the ground-state energy of a quantum oscillator." No principle named; reduces to plugging into the lecture's $\tfrac{1}{2}\hbar\omega$ formula — that is §3.1(c) lecture substitution, not §2.8.
- ❌ "Use everyday intuition to estimate…" Quantum mechanics has no everyday-intuition basis; rejected on sight.

**Hard rule:** the problem text (or an opening hint) must *name* the approximation principle. Implicit "figure out how to estimate this" prompts collapse into §3.5 trick combinations.

---

## 3. Anti-Patterns — Problems to Avoid

### 3.1 Lecture duplication (broad)

Three forms, all rejected:

**(a) Proving a lecture theorem with the lecture's method.** Statements like *"Show that $\langle\hat{O}\rangle$ is real for Hermitian $\hat{O}$"*, *"Show $\hat{H}$ is conserved in the Heisenberg picture"*, *"Show projector eigenvalues are 0 and 1"*, *"Prove picture equivalence $\langle\psi(t)|\hat{A}|\psi(t)\rangle = \langle\psi(0)|\hat{A}(t)|\psi(0)\rangle$"*, *"Show $(\hat{c}^\dagger)^2 = 0$ from $\{\hat{c}^\dagger,\hat{c}^\dagger\}=0$"*. If the lemma is stated and proved in the lecture cell, do not ask the student to prove it again. **Use it.**

**(b) Drilling lecture toolkit algebra past the chapter that introduced it.** Pauli commutators, ladder algebra $[\hat{n},\hat{b}]$, commutator product rule, projector idempotence, $(\hat{n}\cdot\hat{\boldsymbol{\sigma}})^2 = \hat{I}$, spectral-decomposition matrix-multiply checks. These are toolbox skills that should be **assumed available** once their introducing chapter ends. The per-chapter exhaustion list is `BANNED_PROBLEMS.md`.

**(c) Numerical substitution into a lecture formula.** *"Compute $\lambda = h/p$ for $V = 100$ V"* in isolation is a calculator exercise; it counts toward §2.7 only if the next sub-part uses the number to argue a phenomenon (Davisson–Germer, baseball ratio, etc.).

**Fix:** if the underlying skill must be exercised, embed it in a problem whose primary task is different — Transfer, Inversion, Connection, etc.

### 3.2 Trivial table-copy

"Fill in the analogy table" or "list the properties of X" when the answer is a direct copy of a table or list already in the lecture notes. **Fix:** ask the student to *use* the table to solve a problem, or extend it to a case not covered.

### 3.3 "Explain in N sentences"

Open-ended prompts with no concrete physics task. "Explain the significance of entanglement in 3 sentences." These are trivially answered by AI and test nothing on the exam. **Fix:** replace with a concrete conceptual question with a definite answer.

### 3.4 Tedious computation

Long algebra or numerical calculations that test patience, not understanding. If the main challenge is bookkeeping rather than physics, the problem is not exam-worthy. **Fix:** simplify the system or break into guided sub-parts.

### 3.5 Trick combinations

Problems requiring an unmotivated clever trick that students cannot be expected to discover. **Fix:** provide the trick as a hint, or restructure as guided sub-parts.

### 3.6 All problems too far from lecture

Every problem requires context, techniques, or physical systems not discussed in the lecture. Students who understood the lecture perfectly still cannot start the homework without external research. **Fix:** ensure 1–2 problems are directly solvable from lecture content (still subject to §2.7).

### 3.7 Off-topic chapter material

Every problem must serve the chapter's *quantum* theme — not the topic the lecture uses as scaffolding.

**Example failure (real, from §3.1):** Chapter 3 (path integral) introduces classical optics as motivation for the action principle. The §3.1 lecture sequence is meant to bridge classical optics → wave-particle duality → path integral. The current homework set drifts onto pure optics — Fermat reflection, Snell critical angle, layered slab ray tracing, Huygens reflection construction, curved mirror focusing — most of which have **no QM payload**. A student going through §3.1 spends most of their time on optics with no connection back to quantum mechanics.

- ❌ "Use Fermat's principle to derive Snell's law from $A$ to $B$ via a flat mirror" (classical optics for its own sake)
- ❌ "Layered medium ray tracing: apply Snell at each interface to compute $\theta_2,\theta_3,\theta_4$" (optical engineering)
- ❌ "Curved mirror focusing — derive the mirror equation" (geometric optics, no QM bridge)
- ✅ "Use the optics-mechanics dictionary to translate Snell's law into a particle crossing a potential step. What plays the role of refractive index?" (the bridge is the point)
- ✅ "An electron at 100 V has $\lambda \approx 0.12$ nm — comparable to crystal spacing. Argue from this why Davisson–Germer was the first matter-wave experiment, and what changes for a $30$ m/s baseball." (the number serves a QM conclusion)

**Rule:** scaffolding material (classical mechanics, optics, linear algebra, complex analysis) may appear, but only via an explicit bridge that points back at quantum physics. A standalone classical-mechanics problem in a quantum course is off-topic, even if interesting in isolation.

### 3.8 Exhausted skills (chapter-keyed)

Concrete per-chapter exhaustion list: **`BANNED_PROBLEMS.md`** (this folder). After a skill is exhausted, it may only appear **embedded** in a larger problem (one sub-part of a multi-step task whose primary thrust is something else), never as the standalone task.

Examples (full list in `BANNED_PROBLEMS.md`):

- Pauli matrix multiplication / `(\hat{n}\cdot\hat{\boldsymbol{\sigma}})^2=\hat{I}` — exhausted after ch1.
- Commutator product rule `[A,BC]=[A,B]C+B[A,C]` and Pauli commutator identities — exhausted after 1-2-2.
- Bosonic ladder algebra `[\hat{n},\hat{b}^\dagger]=\hat{b}^\dagger`, `(\hat{c}^\dagger)^2=0` — exhausted after 2-1-3.
- Schrödinger ↔ Heisenberg picture equivalence proof — exhausted after 1-3-3.
- Projector eigenvalue / idempotence proofs — exhausted after 1-2-3.

The audit step (§6 step 2) cross-references `BANNED_PROBLEMS.md` against drafted problems.

### 3.9 Out-of-scope references (named theorems, bounds, protocols)

Problems and solutions must not invoke **named theorems, named bounds, named protocols, named experiments, or named inequalities** that have not been introduced in the current or any prior lecture. The lecture sets the curricular boundary. Homework that imports external knowledge — even when the concept itself is interesting — forces students to look up jargon before they can engage, and conflicts with the AI-era goal of building *internal* worldview rather than encyclopedic name recognition.

**Failure cases (real, from this project's homework history):**

- "(You are not asked to derive the **Helstrom bound**…)" in a discrimination problem where the lecture only established that pure states are vectors and projective measurements obey Born's rule. The bound is a real result but its *name* is out-of-scope; the problem can argue the underlying impossibility without invoking it.
- "…the foundation of **quantum cryptography (BB84)**" in a solution to a first-week qubit problem. BB84 is a multi-step protocol students have never seen.
- "This is the content of **Holevo's bound**…" when the lecture only states the underlying claim ("≤1 bit per measurement"). Mentioning the proper name attaches a label not in the lecture.
- "…Bell-state correlations violate the **CHSH inequality**…" in a Chapter-1 problem on quantum information — CHSH is Chapter-6 material.
- "*Example:* the **Mach–Zehnder interferometer**…" in a Chapter-1 problem on superposition — MZI is not in the lecture and not in any prior chapter.

**What is allowed:**

- The underlying *concept* the name refers to, expressed in language the student already has.
- **Forward pointers** to future chapters using the chapter/section number, provided the current problem does **not** depend on that future material. *Example:* "Entanglement, developed in Chapter 2, generalizes this." — fine. *Example:* "Compute the entanglement entropy of this state." — out-of-scope in Chapter 1.
- Generic physics terminology with wide undergraduate currency (harmonic oscillator, energy eigenstate, magnetic field, momentum, Boltzmann factor, classical limit). Such language is not a "named result" — it is the vocabulary of physics itself.
- Procedure names that are descriptive rather than borrowed-result labels (e.g., "state tomography" as the natural label for "reconstructing the state from Pauli expectations" — descriptive, not a borrowed theorem).

**Audit step.** Before finalising, scan for proper nouns and named bounds/theorems/protocols/inequalities. For each, ask: *does this appear in the current or a prior lecture cell?* If not, rewrite using lecture-available language or remove. The §2.7 *Physics payload* statement is a useful guide: if the payload sentence requires invoking the name, the problem is out-of-scope.

### 3.10 Above-lecture depth or extension

Problems must use **only the techniques, formalism, and methods introduced in the current or a prior lecture**. Even when the topic stays in scope, a problem requiring significantly more advanced reasoning — statistical machinery, higher-order perturbation theory, formalism not yet developed — is rejected.

This is the partner rule to §3.9 (which catches named *labels*). §3.10 catches **machinery and depth**: a problem can fail §3.10 without naming any forbidden theorem, simply by requiring the student to deploy techniques the lecture has not taught.

**Failure cases (real, from this project's homework history):**

- A 1-2-1 (Measurement Postulate) homework asking for **binomial standard deviation** of the estimator $\hat p = k/N$, when the lecture states the Born rule only in the infinite-copy limit and never introduces statistical estimation, finite-sample variance, or confidence intervals. The statistics is correct physics but goes *beyond the lecture's level*.
- A Chapter-1 homework requiring **density-matrix** machinery ($\langle\hat Oangle = \operatorname{Tr}(ho\hat O)$, partial traces) when only state vectors have been covered.
- A Chapter-3 homework that asks the student to **compute a path integral by saddle-point** when the lecture has only introduced the path-integral *concept* and not the stationary-phase technique.

**What's allowed:**

- A new specific instance of a lecture technique (different operator, different state, different basis, different limit).
- A one-step extension along the lecture's logical chain to a non-obvious example.
- An inversion / misconception test that exercises the lecture's logic without invoking new machinery.

**Test ("does the solution use only lecture-introduced tools?").** Before finalising any problem, draft the solution chain in your head. If any step requires a formula, technique, distribution, theorem, or named principle that is **not in** the current or any prior lecture, the problem fails §3.10. Replace it with a problem that exercises the same physical content using lecture-available tools — or move it to the chapter that introduces the needed machinery.

**Distinction from §3.7 (off-topic chapter material):** §3.7 catches problems that drift to a *different theme* (optics in a quantum lecture). §3.10 catches problems that stay on the *right theme* but at the *wrong depth* (statistical estimation in a measurement-postulate lecture). Both can apply simultaneously; both are rejection grounds.

---

## 4. Formatting Rules

### 4.1 Problem format

Every problem starts with a **bold number and short title** (1–5 words), followed by the task on the same line:

```
**N. Title.** Task sentence describing what to do...
```

**Problem voice:** Never use "a student" / "the student" in problem wording. Use imperative or impersonal tasks, or **one** for generic framing ("One might claim…," "Suppose one measures…"). See `content-style.md` § Homework Design.

Rules:
- Number, period, title, and closing period are **all inside one bold span**: `**N. Title.**`
- The task continues on the same line after the closing `**` (inline, not standalone).
- Every problem **must** have a title — no bare `**N.** Show that...`.
- **ASCII words only inside the bold title** — no `$...$`, `\(...\)`, or LaTeX inside `**...**`. All math goes in the task text after the closing `**`.
- Do **not** use `**Problem.**`, `###` headings, or parenthetical titles like `(Topic)`.
- Capitalize the first word of every title.

### 4.2 Sub-parts

- Each sub-part `(a)`, `(b)`, ... starts on its **own line** with a blank line before it.
- **No subtitles** on sub-parts — `(a)` states the task directly, never `**(a) Title.**`.
- **Every sub-part must ask a question or assign a task** ("show that," "compute," "find," "explain why"). Never use a sub-part just to provide context.
- Part (a) should start simple; subsequent parts escalate.

### 4.3 Problem preamble

- If a problem needs extended context (more than ~2 sentences of setup), place it in a **preamble paragraph** between the title line and `(a)`.
- Do not bury context inside a sub-part.
- Use sub-parts to **guide step by step** through complexity.

### 4.4 Display math in homework

- `$$...$$` blocks MUST have **blank lines above and below**.
- Do NOT put blank lines inside a `$$...$$` block.
- For multiline equations, use `\begin{split}...\end{split}` inside `$$...$$`.
- Do NOT use `align` or `aligned` environments.

### 4.5 Cross-referencing

- Reference problems as `HW x.y.z.k` (e.g., `HW 6.1.2.3`).
- 5–10 problems per subsection (target 7–8; see §1 distribution).

---

## 5. Common Formatting Errors

These are frequently introduced during automated editing. Check for all of them after any homework edit.

| Error | Wrong | Right |
|-------|-------|-------|
| Trailing `**` | `**3. Title.** text **` | `**3. Title.** text` |
| Missing `$$` blank lines | `text\n$$\nE=mc^2\n$$\ntext` | `text\n\n$$\nE=mc^2\n$$\n\ntext` |
| Inline sub-parts | `text. (a) Find X. (b) Find Y.` | `text.\n\n(a) Find X.\n\n(b) Find Y.` |
| Lowercase title | `**2. spin precession.**` | `**2. Spin precession.**` |
| LaTeX in bold title | `**5. Limit ($\lambda$).**` | `**5. Short-wavelength limit.**` |
| Mixed bullets | `- X\n* Y\n- Z` | `- X\n- Y\n- Z` |
| "A student" in task text | `A student claims that…` | `One might claim that…` (or impersonal setup) |

---

## 6. Design Process

When creating or revising homework for a subsection notebook:

1. **Read the lecture cell** (cell 2). List the key concepts, results, and methods taught. Identify the chapter's *quantum* theme — what does this section ultimately teach about quantum mechanics?
2. **Read the prior subsection's homework** (and one further back, if in the same chapter). Note which toolkit skills have already been drilled — those are off the table as standalone tasks. Cross-reference `BANNED_PROBLEMS.md` for the current chapter's exhaustion list.
3. **Open `TEMPLATES.md § 3` (gold gallery).** Use it as the calibration of "what good looks like" for this skill, not just abstract principles.
4. **Draft 7–8 problems**, one per major concept, satisfying at least one of §2.1–§2.6 or §2.8 quality principles AND §2.7 physics payload. Apply the §1 distribution constraints (≤2 near-lecture; ≥3 from {connection, misconception, inversion, edge, approximation}).
5. **Check anti-patterns** (§3.1–§3.8). For each draft, write one sentence: "After this problem, the student will understand that ___." If the completion is hollow, redesign.
6. **Format** per §4.
7. **Proof-heavy "show that"** statements — get **`derivation-designer`** sign-off in the design report before **`notebook-writer`** implements.
8. **Audit checklist (§7).** Every box must be checked before handoff.
9. **Do not run validators** here — **`notebook-writer`** runs **`rules/validation.md`** after it applies your cell-3 markdown.

### 6.x Cross-notebook duplication check

Before finalizing, scan:

- `homework/homework.md` (index of problem titles across all notebooks) — does any drafted primary task duplicate an earlier problem title?
- Adjacent subsection homework cells (one before, one after) — same skill drilled as standalone task?
- `BANNED_PROBLEMS.md` — does the draft trip an exhaustion rule?

If yes to any: redesign the problem. The repeated skill may be a sub-part of a larger task, but not the standalone task.

---

## 7. Audit Checklist

When reviewing existing homework (or before handing off a fresh draft):

**Quality / pedagogy:**
- [ ] **Every problem passes §2.7 Physics payload** — one-sentence "After this problem, the student will understand that…" completion is non-trivial?
- [ ] Each problem satisfies at least one of §2.1–§2.6 or §2.8 quality principles?
- [ ] No problem trips §3.1 (lecture duplication: theorem-proving, toolkit drill, isolated numerical substitution)?
- [ ] No problem trips §3.7 (off-topic chapter material — every problem serves the chapter's quantum theme)?
- [ ] No problem or solution trips §3.9 (out-of-scope references — named theorems/bounds/protocols not introduced in the current or a prior lecture)?
- [ ] No problem or solution trips §3.10 (above-lecture depth — every step of the solution must use only lecture-introduced techniques)?
- [ ] No problem drills an exhausted skill from `BANNED_PROBLEMS.md` as its standalone task?
- [ ] No primary task duplicates a problem title in an earlier notebook's homework (`homework.md` check)?
- [ ] At most 2 near-lecture problems? At least 3 from {Connection, Misconception, Inversion, Edge cases, Approximation (§2.8)}?
- [ ] At most 1 "show that [lecture result]" problem, and only with a non-obvious twist?

**Format:**
- [ ] 7–8 problems (5–10 allowed)?
- [ ] No "a student" / "the student" in problem wording (use imperatives or "one")?
- [ ] Each problem has `**N. Title.** Task...` format?
- [ ] Titles are ASCII-only, capitalized?
- [ ] Sub-parts on separate lines with blank lines before each?
- [ ] Every sub-part has a concrete task (not just context)?
- [ ] Display math has blank lines above and below `$$`?
- [ ] No trailing `**` or other formatting errors (§5)?

**Handoffs:**
- [ ] Gold gallery (`TEMPLATES.md § 3`) consulted for style?
- [ ] Proof-style "show that" targets covered by **`derivation-designer`** report when non-trivial?

---

## 8. Validation (notebook-writer only)

This skill does not edit notebooks **and does not run** `validate_project.py` / `safe_edit.py validate`. After **`notebook-writer`** applies your homework cell, **it** runs validators per **`rules/validation.md`**.

---

## 9. Automation scripts (`scripts/`)

Homework-specific CLIs and the **`homework_format`** library live beside this skill in **`scripts/`**. **When to use which:** **`scripts/README.md`**. **`notebook-writer`** executes them; you **specify** the command (e.g. after a refactor that might have duplicated problems, run **`check_duplicate_homework.py`**; for line-level homework reports before a big fix, **`audit_homework_format.py`**).

---

## 10. LaTeX Conventions in Homework

Follow `rules/physics-conventions.md`:
- Vectors: `\boldsymbol{v}` (not `\vec{v}`)
- Operators: `\hat{H}`, `\hat{p}`
- Imaginary unit: `\mathrm{i}`; Euler: `\mathrm{e}`; differential: `\mathrm{d}`
- Kets: `\vert\psi\rangle` (use `\vert`, not `|`)
- Dot product `\cdot` only between vectors, never between scalars
- In homework JSON: beware Python escape sequences corrupting `\rho`, `\alpha`, `\beta`, `\frac` — always use raw strings or double backslashes

---

## References

- **`TEMPLATES.md`** (this folder) — problem MyST layout + **§3 Gold gallery** (annotated examples)
- **`BANNED_PROBLEMS.md`** (this folder) — per-chapter exhausted-skill list
- **`scripts/README.md`** — homework automation entry point
- `rules/content-style.md` § Homework Design (canonical formatting rules)
- `rules/teaching-philosophy.md` (course strategy, role of homework)
- `rules/physics-conventions.md` (LaTeX notation)
- `skills/lecture-designer/TEMPLATES.md` (new-notebook integration checklist)
- `rules/validation.md` (validators are executed by **`notebook-writer`**, not this skill)
- `rules/notebook-editing.md` (safe JSON editing)
- `skills/lecture-designer/SKILL.md` (lecture-wide context)
- `skills/derivation-designer/SKILL.md` (proof / derivation chain QC)
- **`_refs/`** (project root): Professor's original lecture notes and `HOMEWORK.md`. Read the relevant `_refs/` file before designing problems to ensure alignment with the professor's presentation and notation. See `CLAUDE.md` § "Reference materials" for the chapter-to-file mapping.
