# Per-chapter exhausted-skill list (PHYS130B homework)

Concrete reject list paired with **`SKILL.md` § 3.8**. A skill is *exhausted* once the lecture and one homework round have drilled it; after that, the skill may only appear **embedded** in a larger problem (as a sub-step toward a different primary task), never as the standalone task.

**How to read this file.** Each section lists skills that became exhausted at or before the end of the named subsection. When designing homework for a *later* subsection, scan this file: any drafted problem whose primary task matches an entry here must be redesigned or replaced.

**Status of the existing homework set.** This list documents skills that **have already been over-drilled** in the existing homework (see audit notes). For redesign, treat these as a hard reject; the underlying skill is assumed available.

---

## Chapter 1 — Qubit

**Exhausted by end of 1-1-3 (Hermitian operators):**

- Computing the Hermitian conjugate / dagger of an explicit 2×2 matrix.
- Verifying that a given matrix is (or is not) Hermitian by inspection or matrix transpose.
- Diagonalizing a 2×2 Hermitian matrix to find eigenvalues and eigenvectors.
- Computing $\langle\hat{X}\rangle$, $\langle\hat{Y}\rangle$, $\langle\hat{Z}\rangle$ for a given qubit state by direct substitution.
- Showing $(\hat{n}\cdot\hat{\boldsymbol{\sigma}})^2 = \hat{I}$ for a unit vector $\hat{n}$.
- Proving general properties of projectors (idempotence, eigenvalues 0/1, Hermiticity) — lecture-stated.
- Proving that $\langle\hat{O}\rangle$ is real for Hermitian $\hat{O}$ — lecture-stated lemma.
- Verifying the spectral decomposition of $\hat{X}$, $\hat{Y}$, $\hat{Z}$ by matrix multiplication.

**Exhausted by end of 1-2-2 (uncertainty / commutators):**

- Computing $[\hat{X},\hat{Z}]$, $[\hat{X},\hat{Y}]$, etc. by explicit matrix multiplication.
- Verifying the Pauli commutator identity $[\hat{\sigma}^a,\hat{\sigma}^b] = 2\mathrm{i}\epsilon^{abc}\hat{\sigma}^c$ for individual index pairs.
- Proving the commutator product rule $[\hat{A},\hat{B}\hat{C}] = [\hat{A},\hat{B}]\hat{C} + \hat{B}[\hat{A},\hat{C}]$ (pure algebraic identity, no physics).
- Verifying $\Delta A \cdot \Delta B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$ on a generic qubit state by plug-and-chug.

**Exhausted by end of 1-2-3 (measurement operators):**

- Writing explicit 2×2 projectors $\hat{P}_\pm = (\hat{I} \pm \hat{O})/2$ for Pauli $\hat{O}$.
- Verifying projector idempotence $\hat{P}^2 = \hat{P}$ for these.
- Verifying completeness $\sum_m \hat{P}_m = \hat{I}$.
- Computing measurement probabilities on a given qubit state via $|\langle m|\psi\rangle|^2$.

**Exhausted by end of 1-3-1 (unitary evolution):**

- Verifying unitarity $\hat{U}^\dagger\hat{U} = \hat{I}$ for $\hat{U} = \mathrm{e}^{\mathrm{i}\hat{G}\theta}$ with Hermitian $\hat{G}$.
- Computing $\mathrm{e}^{\mathrm{i}\theta\hat{\sigma}^a/2} = \cos(\theta/2)\hat{I} + \mathrm{i}\sin(\theta/2)\hat{\sigma}^a$ by spectral decomposition or Taylor series (the formula itself).
- Proving normalization preservation under unitary evolution.
- Proving the composition property $\hat{U}(t_1)\hat{U}(t_2) = \hat{U}(t_1+t_2)$ for $\hat{U} = \mathrm{e}^{-\mathrm{i}\hat{H}t/\hbar}$.

**Exhausted by end of 1-3-3 (Heisenberg picture):**

- Proving Schrödinger ↔ Heisenberg picture equivalence $\langle\psi(t)|\hat{A}|\psi(t)\rangle = \langle\psi(0)|\hat{A}(t)|\psi(0)\rangle$.
- Showing $\mathrm{d}\hat{H}/\mathrm{d}t = 0$ in the Heisenberg picture (one-line tautology).
- Computing Heisenberg evolution of a single Pauli operator under $\hat{H} = \tfrac{\hbar\omega}{2}\hat{\sigma}^z$.
- Proving that $[\hat{A},\hat{H}] = 0 \Rightarrow \mathrm{d}\langle\hat{A}\rangle/\mathrm{d}t = 0$ (standard textbook proof).

## Chapter 2 — Identical particles

**Exhausted by end of 2-1-1 (tensor product):**

- Computing $\dim(\mathcal{H}_A \otimes \mathcal{H}_B)$ and listing product-basis states.
- Verifying orthonormality of product-basis states from $\langle\alpha_1\alpha_2|\beta_1\beta_2\rangle = \langle\alpha_1|\beta_1\rangle\langle\alpha_2|\beta_2\rangle$.
- Writing $\hat{O}_A \otimes \hat{I}$ or $\hat{I} \otimes \hat{O}_B$ as an explicit Kronecker product matrix.
- Proving $\langle\psi_A\otimes\psi_B|\hat{A}\otimes\hat{B}|\psi_A\otimes\psi_B\rangle = \langle\hat{A}\rangle_A \langle\hat{B}\rangle_B$ for product states (factorization).
- Showing operators on different factors commute, $[\hat{A}\otimes\hat{I}, \hat{I}\otimes\hat{B}] = 0$.

**Exhausted by end of 2-1-3 (second quantization):**

- Deriving $\hat{n}_\alpha|n_\alpha\rangle = n_\alpha|n_\alpha\rangle$ from $[\hat{b},\hat{b}^\dagger] = 1$ (ladder-spectrum proof).
- Computing $[\hat{n}_\alpha,\hat{b}_\beta]$, $[\hat{n}_\alpha,\hat{b}_\beta^\dagger]$ from the canonical (anti)commutators.
- Showing $(\hat{c}^\dagger_\alpha)^2 = 0$ from the fermionic anticommutator.
- Listing Fock states with fixed total $N$ for two-mode bosons/fermions (counting exercise).
- Computing $\langle 0|\hat{b}_\alpha\hat{b}^\dagger_\alpha|0\rangle$ vs $\langle 0|\hat{b}^\dagger_\alpha\hat{b}_\alpha|0\rangle$ (vacuum expectation values).
- Showing $[\hat{H},\hat{N}] = 0$ for $\hat{H} = \sum_\alpha \epsilon_\alpha\hat{n}_\alpha$ (one-line tautology).

**Exhausted by end of 2-2-1 (angular momentum algebra):**

- Verifying $[\hat{J}_x,\hat{J}_y] = \mathrm{i}\hbar\hat{J}_z$ by explicit matrix computation for spin-1/2.
- Verifying $[\hat{J}^2,\hat{J}_z] = 0$ by expansion.
- Deriving the ladder commutators $[\hat{J}_z,\hat{J}_\pm] = \pm\hbar\hat{J}_\pm$, $[\hat{J}_+,\hat{J}_-] = 2\hbar\hat{J}_z$.

**Exhausted by end of 2-2-2 (spin representations):**

- Verifying Pauli identities $\{\hat{\sigma}^i\}^2 = \hat{I}$, $\mathrm{Tr}\hat{\sigma}^i = 0$, $\hat{\sigma}^i\hat{\sigma}^j = \delta_{ij}\hat{I} + \mathrm{i}\epsilon_{ijk}\hat{\sigma}^k$.
- Finding spin-1/2 eigenstates of $\hat{S}_x = \tfrac{\hbar}{2}\hat{\sigma}^x$.
- Verifying $[\hat{S}_x,\hat{S}_y] = \mathrm{i}\hbar\hat{S}_z$ in the spin-1 (3×3) representation.

## Chapter 3 — Path integral (in-progress audit)

**Topic-scope rule.** §3.7 (off-topic chapter material) applies to all of Chapter 3:

- Pure geometric / physical optics problems with no quantum bridge — see `SKILL.md` §3.7 examples (Fermat reflection, Snell critical angle, layered ray tracing, Huygens reflection, curved mirror equation). These belong in an optics course, not a quantum-mechanics homework set, **unless** the problem explicitly invokes the optics-mechanics dictionary or the de Broglie / action / phase connection.

**Exhausted by end of 3-1-1 / 3-1-2 (geometric and physical optics — bridging chapters):**

- Direct Fermat-principle derivations of reflection, refraction, Snell critical angle (use sparingly and only with QM payload).
- Snell's law on parallel-interface stacks (mathematical ray tracing).
- Huygens-construction derivations of reflection/refraction (no QM content).

**Exhausted by end of 3-1-3 (wave-particle duality):**

- Verifying de Broglie relations $\boldsymbol{p} = \hbar\boldsymbol{k}$, $E = \hbar\omega$ from $\psi = A\mathrm{e}^{\mathrm{i}S/\hbar}$ by matching exponents.
- Computing $\lambda = h/p$ for a single given electron / particle (without a downstream physical argument).
- Optics-mechanics dictionary translation as the **standalone** task — it should reappear only as a stepping stone to a richer problem (e.g. WKB application, tunneling, action quantization).

(*Further entries to be added as the audit reaches Chapters 4–5.*)

---

## How designers should use this file

1. **Before drafting** homework for subsection $x.y.z$: scan all preceding chapters' sections above; any drafted *primary task* that matches an entry here is rejected — redesign.
2. **Embedded use is allowed.** A multi-part problem whose primary thrust is Connection / Inversion / Misconception (§2.5 / §2.2 / §2.6) may invoke an exhausted skill as a sub-step (e.g. "use $[\hat{a},\hat{a}^\dagger]=1$ in sub-part (b) to evaluate the commutator that appears" — fine; *"Show that $[\hat{a},\hat{a}^\dagger]=1$"* — exhausted).
3. **When in doubt**, prefer to keep the skill embedded. The §2.7 *Physics payload* test is the final arbiter: if the problem's payload depends on the embedded skill being non-trivial, and the skill is exhausted, the problem fails.

## How to update this file

- When a new chapter is fully redesigned, add a new heading with the exhausted skills it drills.
- Group entries by the *subsection* at which the skill becomes exhausted (not just by chapter).
- Each entry should be one line, naming the skill in plain English (with key formulas where useful).
- **Do not** delete past entries — exhaustion is cumulative across the course.
