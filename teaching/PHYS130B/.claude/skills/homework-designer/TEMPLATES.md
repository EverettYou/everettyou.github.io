# Homework cell templates (PHYS130B)

**Law:** `rules/content-style.md` § Homework Design (counts, tone, banned wording) + `rules/physics-conventions.md` (math layout).
**Quality bar:** `SKILL.md` §1 distribution, §2 principles (esp. §2.7 Physics payload), §3 anti-patterns.

Match **live** subsection homework cells—e.g. `notes_src/ch2_identical-particles/2-1-3-second-quantization.ipynb` cell 3, but **calibrate quality against § 3 below**, not against generic templates.

---

## 1. Section header

```markdown
## Homework
```

## 2. Problem statement pattern

- Each problem: **`**N. Short Title.**`** opening sentence, then task on the same line.
- Sub-parts: `(a)`, `(b)` on **separate lines** with a blank line before each.
- Use imperatives or "Show that…"; avoid "a student" / "the student."

```markdown
**1. Spin precession.** A spin-1/2 particle is placed in a magnetic field $\boldsymbol{B} = B\hat{z}$. Show that $\langle \hat{\sigma}^x \rangle(t)$ oscillates at the Larmor frequency.

**2. Landau–Zener transition.** Consider a two-level system with Hamiltonian $\hat{H}(t) = \alpha t\,\hat{\sigma}^z + \Delta\,\hat{\sigma}^x$.

(a) Find the instantaneous eigenvalues $E_\pm(t)$ and the minimum gap.

(b) In the adiabatic limit $\alpha \to 0$, argue that the system stays in the ground state.

(c) Show that the transition probability is $P = \mathrm{e}^{-\pi\Delta^2/\hbar\alpha}$.
```

### Display math in stems

Use `$$` blocks for displayed definitions students reuse across parts; keep prose between parts light.

---

## 3. Gold gallery — annotated examples

These are problems that **hit the bar** (drawn from the professor's curated "good" list). Each entry includes (i) the full problem text and (ii) why it works, mapped to `SKILL.md` § 2 principles. **Draft new problems against this gallery**, not against abstract principles in isolation. When in doubt, ask: "Does my draft have the same physics payload as Gold N?"

### Gold 1 — Transfer to a new system (HW 1-3-3 #4 Harmonic oscillator dynamics)

> **4. Harmonic oscillator dynamics.** Consider a harmonic oscillator $\hat{H} = \hbar\omega(\hat{a}^\dagger\hat{a} + \frac{1}{2})$. Show that
>
> $$
> [\hat{H}, \hat{a}] = -\hbar\omega\hat{a}, \qquad [\hat{H}, \hat{a}^\dagger] = \hbar\omega\hat{a}^\dagger
> $$
>
> Solve the Heisenberg equations $\frac{\mathrm{d}\hat{a}}{\mathrm{d}t} = \frac{\mathrm{i}}{\hbar}[\hat{H}, \hat{a}]$ and $\frac{\mathrm{d}\hat{a}^\dagger}{\mathrm{d}t} = \frac{\mathrm{i}}{\hbar}[\hat{H}, \hat{a}^\dagger]$ to find $\hat{a}(t)$ and $\hat{a}^\dagger(t)$.

**Why it works.** Lecture 1.3.3 (Heisenberg picture) used spin-1/2 as the primary illustration. This problem transfers the Heisenberg-picture method to a *different physical system* — the harmonic oscillator. The result $\hat{a}(t) = \hat{a}\,\mathrm{e}^{-\mathrm{i}\omega t}$ is the operator counterpart of the classical complex amplitude $a(t) = a(0)\mathrm{e}^{-\mathrm{i}\omega t}$, building the classical-limit bridge.

**Principles:** §2.1 Transfer (spin → oscillator); §2.5 Connection (operator ↔ classical amplitude); §2.7 payload: *"the Heisenberg-picture annihilation operator rotates in the complex plane at the oscillator frequency, just like the classical mode amplitude."*

---

### Gold 2 — Connection between two formalisms (HW 2-1-3 #10 Schwinger boson)

> **10. Schwinger boson.** Define two independent bosonic modes with operators $(\hat{a}, \hat{a}^\dagger)$ and $(\hat{b}, \hat{b}^\dagger)$, and construct
>
> $$
> \hat{S}_+ = \hat{a}^\dagger\hat{b}, \quad \hat{S}_- = \hat{b}^\dagger\hat{a}, \quad \hat{S}_z = \tfrac{1}{2}(\hat{a}^\dagger\hat{a} - \hat{b}^\dagger\hat{b}).
> $$
>
> (a) Verify that these satisfy the angular momentum commutation relations $[\hat{S}_z, \hat{S}_\pm] = \pm\hat{S}_\pm$ and $[\hat{S}_+, \hat{S}_-] = 2\hat{S}_z$.
>
> (b) Show that $\hat{\boldsymbol{S}}^2 = \hat{S}_z^2 + \frac{1}{2}(\hat{S}_+\hat{S}_- + \hat{S}_-\hat{S}_+) = \frac{\hat{N}}{2}(\frac{\hat{N}}{2} + 1)$, where $\hat{N} = \hat{a}^\dagger\hat{a} + \hat{b}^\dagger\hat{b}$ is the total boson number.
>
> (c) In the subspace with $\hat{N} = 2$ (three Fock states $\vert 2,0\rangle$, $\vert 1,1\rangle$, $\vert 0,2\rangle$), write $\hat{S}_z$ and $\hat{S}_+$ as $3\times 3$ matrices. Verify these are the spin-1 representation.
>
> (d) Identify the general correspondence: each Fock state $\vert n_a, n_b\rangle$ with $n_a + n_b = 2s$ maps to $\vert s, m\rangle$ with $m = (n_a - n_b)/2$. What value of $s$ does the $N$-boson subspace carry?

**Why it works.** Lecture 2.1.3 taught second quantization (ladder operators for identical particles). This problem builds a **bridge to angular momentum**: the same SU(2) algebra emerges from two coupled bosonic modes. Reveals that "particles" and "spins" are dual descriptions of the same algebraic structure — a deep duality that recurs in atomic physics (Schwinger), quantum Hall (composite bosons), and quantum simulation.

**Principles:** §2.5 Connection (boson modes ↔ angular momentum); §2.1 Transfer (Fock space → spin representation); §2.7 payload: *"two harmonic oscillators reproduce every spin representation — the algebra alone, not the particles, determines what 'spin' means."*

---

### Gold 3 — Inversion via algebraic bootstrap (HW 2-2-1 #8 Quantum bootstrap)

> **8. Quantum bootstrap.** Two operators $\hat{\alpha}$ and $\hat{\beta}$ satisfy the algebraic relations
>
> $$
> [\hat{\alpha}, \hat{\beta}] = 2\hat{\alpha}, \quad [\hat{\alpha}^\dagger, \hat{\beta}] = -2\hat{\alpha}^\dagger, \quad [\hat{\alpha}^\dagger, \hat{\alpha}] = 2\hat{\beta}, \quad \{\hat{\alpha}^\dagger, \hat{\alpha}\} = 2\hat{I}.
> $$
>
> (a) Show that $\hat{\beta}$ is Hermitian.
>
> (b) Express $\hat{\alpha}^\dagger\hat{\alpha}$ and $\hat{\alpha}\hat{\alpha}^\dagger$ separately as linear combinations of $\hat{\beta}$ and $\hat{I}$.
>
> (c) Show that $(\hat{\alpha}^\dagger)^2 \hat{\alpha}^2 = \hat{\beta}^2 - \hat{I}$. Using positivity ($\hat{\alpha}^\dagger\hat{\alpha} \geq 0$, $\hat{\alpha}\hat{\alpha}^\dagger \geq 0$, $(\hat{\alpha}^\dagger)^2\hat{\alpha}^2 \geq 0$), determine the feasible eigenvalues of $\hat{\beta}$.
>
> (d) Identify the angular momentum operators that $\hat{\alpha}$ and $\hat{\beta}$ correspond to (with $\hbar = 1$). What spin representation does this algebra describe? Write the $2\times 2$ matrix representations of $\hat{\alpha}$ and $\hat{\beta}$ in the eigenbasis of $\hat{\beta}$.

**Why it works.** Lecture 2.2.1 derived the angular momentum algebra **forward**: rotation generators ⇒ commutators ⇒ spectrum. This problem inverts the direction: given an abstract set of commutators plus an anticommutator (which forbids any state but $|\pm\tfrac12\rangle$), use positivity bounds alone to identify the representation. Forces the student to see that **algebraic structure plus positivity determines the spectrum** — the foundation of bootstrap methods in modern physics.

**Principles:** §2.2 Inversion (algebra → representation); §2.3 Edge cases (positivity bounds saturate); §2.6 Misconception (students often think the representation has to be assumed); §2.7 payload: *"an abstract algebra plus Hilbert-space positivity uniquely pins down spin-1/2 — this is the bootstrap principle."*

---

### Gold 4 — Connection to a real experimental phenomenon (HW 2-2-3 #4 Spin-orbit coupling)

> **4. Spin-orbit coupling.** Show that
>
> $$
> \hat{\boldsymbol L}\cdot\hat{\boldsymbol S}=\frac12\bigl(\hat J^2-\hat L^2-\hat S^2\bigr),
> $$
>
> and use it to compute $\langle\hat{\boldsymbol L}\cdot\hat{\boldsymbol S}\rangle$ in $\vert \ell,\tfrac12; j,m_j\rangle$. For hydrogen $2p$, find the fine-structure splitting between $j=3/2$ and $j=1/2$ in terms of $\lambda$.

**Why it works.** Lecture 2.2.3 taught angular momentum addition as formal Clebsch–Gordan machinery. This problem deploys it on a **real physical system** — hydrogen fine structure — connecting the formalism to an empirically observable level splitting students will encounter in any atomic-physics class. Short, focused, builds the knowledge graph.

**Principles:** §2.5 Connection (angular momentum addition → atomic spectra); §2.1 Transfer (formal CG → numerical splitting); §2.7 payload: *"the $j=3/2$ vs $j=1/2$ fine-structure splitting of hydrogen 2p comes from a 2-line algebraic identity, not from solving any differential equation."*

---

### Gold 5 — Edge case: degenerate eigenspace measurement (HW 1-2-3 #4 Two-qubit measurement)

> **4. Two-qubit measurement.** Consider measuring $\hat{Z}$ on a two-qubit state $\vert\Psi\rangle = \frac{1}{\sqrt{2}}(\vert 00\rangle + \vert 01\rangle)$. The first qubit's $\hat{Z}$ has a degenerate $+1$ eigenspace.
>
> (a) Write down the projector onto the $+1$ eigenspace.
>
> (b) Compute the measurement probability of outcome $+1$.
>
> (c) Write down the post-measurement state(s) for outcome $+1$. Is it a superposition or a single eigenstate?

**Why it works.** Lecture 1.2.3 introduced the measurement postulate via projectors on **non-degenerate** spectra. This problem transfers to the **degenerate case**, where the generic formula "post-measurement state is the eigenstate corresponding to the measured eigenvalue" fails — the post-measurement state stays a superposition within the eigenspace. Exposes the edge case that the most common formulation glosses over.

**Principles:** §2.3 Edge cases (degeneracy); §2.6 Misconception (collapse to a single eigenstate is only the non-degenerate case); §2.7 payload: *"degenerate measurements project, but do not select within the eigenspace — the qubit remains entangled with its partner after the partial measurement."*

---

### Gold 6 — Comparison: H versus H² measurement (HW 1-3-2 #9 Three-state evolution)

> **9. Three-state evolution.** Consider a 3-level system with basis $\{\vert 1\rangle, \vert 2\rangle, \vert 3\rangle\}$ and Hamiltonian $\hat{H} = \vert 1\rangle\langle 2\vert + \vert 2\rangle\langle 1\vert - \vert 1\rangle\langle 3\vert - \vert 3\rangle\langle 1\vert$ (in units where the coupling is 1).
>
> (a) Find the eigenvalues and eigenstates of $\hat{H}$.
>
> (b) The system starts in $\vert\psi(0)\rangle = \vert 1\rangle$. Compute $\vert\psi(t)\rangle$.
>
> (c) What is the probability of finding the system in $\vert 3\rangle$ at time $t$?
>
> (d) For a measurement of $\hat{H}^2$ (note: **not** $\hat{H}$) on $\vert\psi(t)\rangle$, list the possible outcomes and their corresponding probabilities.

**Why it works.** Lecture 1.3.2 used two-level systems exclusively. This problem transfers to three levels with a Hamiltonian designed to have a **dark state** ($\vert 2\rangle + \vert 3\rangle$ decouples from $\vert 1\rangle$ via the sign structure). Then sub-part (d) compares measurements of $\hat{H}$ vs $\hat{H}^2$ — same dynamics, different observables, different outcome statistics because $\hat{H}^2$ identifies $|E_+\rangle$ and $|E_-\rangle$ but separates them from the dark state.

**Principles:** §2.1 Transfer (2-level → 3-level); §2.3 Edge cases (dark state from sign cancellation); §2.4 Comparison ($\hat{H}$ vs $\hat{H}^2$ measurements); §2.7 payload: *"interference between $\vert 2\rangle$ and $\vert 3\rangle$ paths protects part of the state from the coupling — and squaring the observable changes the distinguishability of outcomes."*

---

## 4. Anti-pattern examples — do NOT copy

These are real problems from the existing homework that **fail** the criteria above. Listed so the LLM has a concrete reject reference.

### Anti-1 — Pure linear algebra, no physics payload (HW 1-1-3 #1)

> **1. Hermiticity of Pauli matrices.** Show that the Pauli matrix $\hat{Y} = \begin{pmatrix} 0 & -\mathrm{i} \\ \mathrm{i} & 0 \end{pmatrix}$ is Hermitian by explicitly computing $(\hat{Y})^\dagger$ and verifying it equals $\hat{Y}$. Then find its eigenvalues and normalized eigenvectors.

**Why it fails.** Hermiticity of Pauli matrices is *stated* in the lecture as a defining property. Computing the dagger of a 2×2 matrix is high-school linear algebra. §2.7 payload sentence completes as "the student can now transpose and conjugate a 2×2 matrix" — that is not physics. Tripped: §3.1(a) (proving a lecture-stated fact) + §3.1(b) (Pauli toolkit drill).

### Anti-2 — Prove a lecture lemma (HW 1-1-3 #9)

> **9. Reality of expectation values.** Prove that the expectation value of any Hermitian operator $\hat{O}$ is real-valued for any state $\vert\psi\rangle$. That is, show $\langle\hat{O}\rangle^* = \langle\hat{O}\rangle$ using the definition $\langle\hat{O}\rangle = \langle\psi\vert\hat{O}\vert\psi\rangle$ and the Hermiticity condition.

**Why it fails.** The lecture states and proves precisely this lemma (it is the *motivation* for using Hermitian operators in the first place). Asking the student to re-prove it adds nothing. §2.7 sentence: "the student can now reproduce a proof the lecture already showed." Tripped: §3.1(a).

### Anti-3 — Off-topic classical optics (HW 3-1-1 #1)

> **1. Reflection from Fermat.** Use Fermat's principle to derive the law of reflection. Consider a ray from $A$ to $B$ reflecting off a flat mirror. Show that the angle of incidence equals the angle of reflection.

**Why it fails.** The §3.1 lecture sequence uses optics as a **bridge to wave-particle duality and the path integral**. This problem stays entirely on the optics side: no quantum payload, no bridge sub-part, no de Broglie / action / phase. §2.7 sentence: "the student can now derive the law of reflection from a classical variational principle" — a classical-optics fact, not quantum mechanics. Tripped: §3.7 (off-topic).

**Fix sketch.** Either delete, or transform into: *"Use the optics-mechanics dictionary $n(\boldsymbol{r}) \leftrightarrow p(\boldsymbol{r}) = \sqrt{2m(E-V)}$ to predict the bending of a classical particle entering a potential well. Compare to Snell's law and identify the mechanical Snell invariant."*

### Anti-4 — Calculator exercise without payload (HW 3-1-3 #2 part (a) in isolation)

> **2. De Broglie wavelength.** An electron is accelerated through a potential difference of $V = 100$ V. Compute its de Broglie wavelength. Compare this to the lattice spacing of a typical crystal ($\sim 0.3$ nm). Why does this make electron diffraction possible?

**Why it (almost) fails — saved by part 2.** The first sentence on its own is plug-and-chug. What rescues this problem is the *comparison to lattice spacing* and the *Davisson–Germer connection* in the third sentence. Without those, it is §3.1(c) numerical substitution. **Lesson:** numerical computation is only OK when the number serves a physical conclusion.

### Anti-5 — Out-of-scope name-drop (HW 1-1-1 #6, early draft)

> **6. Distinguishing non-orthogonal states.** […] (d) Explain in one sentence why no measurement strategy can achieve guessing probability 1, in contrast to two orthogonal states. (You are **not** asked to derive the **Helstrom bound**, just to argue why perfect single-shot discrimination is impossible.)
>
> *Solution (d):* […] This is the operational reason why an unknown quantum state cannot be cloned and why eavesdropping on a **BB84** photon stream must introduce detectable disturbance — the foundation of quantum cryptography.

**Why it fails.** The problem invokes the **Helstrom bound** and the **BB84** protocol — neither appears in the Chapter-1 lecture. Even the parenthetical "you are not asked to derive it" leaves the student wondering what was named. The physics statement (perfect single-shot discrimination of non-orthogonal states is impossible) is in scope; the *labels* are not. Tripped: §3.9.

**Fix.** Remove the name-drops, keep the impossibility argument in scope-only language. Replace BB84 with the no-cloning link the lecture already established: *"This is the operational reason behind the no-cloning theorem mentioned in the lecture's comparison table: if an unknown state could be perfectly identified, it could be cloned by repeated reading."*

---

## Handoff

Full problem-mix guidance and audit checklist: **`SKILL.md`** §1, §6, §7.
Per-chapter exhausted-skill list: **`BANNED_PROBLEMS.md`**.
Proof-chain QC before writer implements heavy "show that" chains: **`skills/derivation-designer/SKILL.md`**.
