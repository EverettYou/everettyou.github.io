# 2.2.2 Spin Representations
Worked solutions for the homework problems in the [2.2.2 Spin Representations](../ch2_identical-particles/2-2-2-spin-representations) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Stern-Gerlach for spin-1.** A beam of spin-1 atoms (say, $\Omega^-$ baryons or any composite system with integer spin) passes through a Stern-Gerlach apparatus oriented along the $z$-axis. The magnetic moment couples to the spin via $\hat H_{\mathrm{int}} = -\gamma\hat{\boldsymbol S}\cdot\boldsymbol B$, and the field gradient produces a force proportional to $\hat S_z$.

(a) State the possible eigenvalues of $\hat S_z$ for a spin-1 system, and identify how many distinct branches the beam splits into.

(b) For spin-1/2 the beam splits into two branches; for spin-1 it splits into three. Argue from the lecture's general rule $\dim = 2j+1$ that the number of branches in any Stern-Gerlach measurement directly reads off the value of $j$.

(c) An initial spin-1 state $\vert\psi(0)\rangle = a\vert 1,+1\rangle + b\vert 1,0\rangle + c\vert 1,-1\rangle$ (with $\vert a\vert^2 + \vert b\vert^2 + \vert c\vert^2 = 1$) enters the apparatus. State the probability that the atom emerges in each of the three branches.

(d) The beam-splitting can be inverted: by counting the three branches and measuring their relative intensities, one *measures* $j$ (the existence of three rather than two branches) **and** the populations $\vert a\vert^2, \vert b\vert^2, \vert c\vert^2$. Argue that a single-shot Stern-Gerlach experiment is therefore a complete $\hat J_z$-basis measurement of a spin-$j$ atom — the natural generalisation of the qubit projective measurement.

**Solution.**

(a) Spin-1 has $\hat J_z$ eigenvalues $\hbar m$ for $m \in \{+1, 0, -1\}$ — **three** distinct values. The beam splits into three branches.

(b) The dimension of the spin-$j$ Hilbert space is $2j+1$ (2.2.1 P2), and $\hat J_z$ on a spin-$j$ multiplet has $2j+1$ distinct eigenvalues $\hbar m$, $m = -j, -j+1, \ldots, +j$. The Stern-Gerlach apparatus deflects each $m$ to a spatially distinct branch (since the deflection force is $\propto m$), so the beam splits into $2j + 1$ branches. **Counting branches measures the spin.** For $j = 1/2$: 2 branches. For $j = 1$: 3 branches. For $j = 3/2$: 4 branches. This was historically the first proof that angular momentum is *quantised* — the original Stern-Gerlach experiment on silver atoms (1922) showed two discrete branches rather than the continuous spread expected from classical mechanics.

(c) By the Born rule, the probability of finding the atom in branch $m$ is the squared modulus of the corresponding amplitude in the $\hat J_z$ basis:

$$
P(m = +1) = \vert a\vert^2, \quad P(m = 0) = \vert b\vert^2, \quad P(m = -1) = \vert c\vert^2,
$$

summing to $1$ by normalisation. After the measurement, the atom collapses to the corresponding eigenstate $\vert 1, m\rangle$.

(d) The three deflection branches are spatially separated and individually detectable, so each measurement realises one of the three projectors $\hat P_m = \vert 1, m\rangle\langle 1, m\vert$. The full set of three projectors satisfies $\sum_m \hat P_m = \hat I$ (completeness), and the Born-rule probability of branch $m$ equals $\langle\psi\vert\hat P_m\vert\psi\rangle$. So one Stern-Gerlach apparatus implements **the full $\hat J_z$ measurement postulate** (1.2.3) for a spin-$j$ system: three eigenvalues, three projectors, three outcomes per atom — generalising the two-outcome qubit projective measurement to any spin. The Stern-Gerlach setup is the canonical example of a spin-resolving measurement, and its branch count is the experimental signature of the spin quantum number.

<!-- ─── -->

**2. Spin-1 rotation operator via polynomial truncation.** For spin-1/2, the identity $(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2 = \hat I$ truncates the Taylor series of $\hat D^{(1/2)}(\boldsymbol{n}, \theta) = \mathrm{e}^{-\mathrm{i}\theta\boldsymbol{n}\cdot\hat{\boldsymbol\sigma}/2}$ into the spinor formula $\cos(\theta/2)\hat I - \mathrm{i}\sin(\theta/2)(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})$.

For **spin-1** the analogous truncation requires one more power. Take $\boldsymbol{n} = \boldsymbol{e}_x$, where $\boldsymbol{e}_a$ denotes the unit vector along the $a$-axis.

(a) Using the spin-1 matrix $\hat J_x = \tfrac{\hbar}{\sqrt 2}\begin{pmatrix}0&1&0\\ 1&0&1\\ 0&1&0\end{pmatrix}$ from 2.2.1 P1, verify by explicit matrix multiplication that $\hat J_x^3 = \hbar^2\hat J_x$ (in particular, the cube reduces back to the first power, not to a higher polynomial). Conclude that the eigenvalues of $\hat J_x$ are $\hbar\cdot m$ with $m \in \{+1, 0, -1\}$ — the *cube* relation $\lambda^3 = \lambda$ holds because $\lambda \in \{+1, 0, -1\}$ solves it.

(b) Use $\hat J_x^3 = \hbar^2\hat J_x$ to truncate the Taylor series $\hat D^{(1)}(\boldsymbol{e}_x, \theta) = \mathrm{e}^{-\mathrm{i}\theta\hat J_x/\hbar}$. Show

$$
\hat D^{(1)}(\boldsymbol{e}_x, \theta) = \hat I - \mathrm{i}\sin\theta\,\frac{\hat J_x}{\hbar} + (\cos\theta - 1)\,\frac{\hat J_x^2}{\hbar^2}.
$$

(c) Evaluate at $\theta = 2\pi$ to show $\hat D^{(1)}(\boldsymbol{e}_x, 2\pi) = +\hat I$. Contrast with the spin-1/2 result $\hat D^{(1/2)}(\boldsymbol{e}_x, 2\pi) = -\hat I$ (Problem 4 below). What property of $j$ produces the sign difference?

**Solution.**

(a) Compute $\hat J_x^2$ first. With $a = \hbar/\sqrt 2$:

$$
\hat J_x^2 = a^2\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix}^2 = a^2\begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix} = \frac{\hbar^2}{2}\begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix}.
$$

Now cube:

$$
\begin{split}
\hat J_x^3 &= \hat J_x^2\cdot\hat J_x = \frac{\hbar^2}{2}\cdot\frac{\hbar}{\sqrt 2}\begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix}\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix} \\
&= \frac{\hbar^3}{2\sqrt 2}\begin{pmatrix}0&2&0\\2&0&2\\0&2&0\end{pmatrix} \\
&= \hbar^2\cdot\frac{\hbar}{\sqrt 2}\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix} = \hbar^2\hat J_x. \quad\checkmark
\end{split}
$$

(Equivalently: $\hat J_x$ has eigenvalues $\hbar\{+1, 0, -1\}$ from the spin-1 multiplet, and these satisfy $\lambda^3 = \lambda$, so the minimal polynomial of $\hat J_x$ is $\hat J_x^3 - \hbar^2\hat J_x = \hat J_x(\hat J_x - \hbar\hat I)(\hat J_x + \hbar\hat I) = 0$.) The cube relation is the spin-1 analogue of $\hat J^2 = \hbar^2/4\,\hat I$ in spin-1/2 (where eigenvalues are $\pm\hbar/2$, satisfying $\lambda^2 = \hbar^2/4$).

(b) Expand the Taylor series with $\hat J_x^3 = \hbar^2\hat J_x$ recycling higher powers. Define $u = \hat J_x/\hbar$ for compactness. The cube relation gives $u^3 = u$, hence $u^{2k+1} = u$ for $k \ge 1$ and $u^{2k} = u^2$ for $k \ge 1$:

$$
\hat D^{(1)}(\boldsymbol{e}_x, \theta) = \sum_{n=0}^\infty\frac{(-\mathrm{i}\theta)^n}{n!}u^n = \hat I + (-\mathrm{i}\theta)u + \sum_{n=2}^\infty\frac{(-\mathrm{i}\theta)^n}{n!}u^n.
$$

Split the sum for $n \ge 2$ into even and odd powers. Even powers ($n = 2, 4, 6, \ldots$) all give $u^2$:

$$
\sum_{n=2,4,\ldots}\frac{(-\mathrm{i}\theta)^n}{n!}u^n = u^2\sum_{n=2,4,\ldots}\frac{(-\mathrm{i}\theta)^n}{n!} = u^2\bigl(\cos\theta - 1\bigr).
$$

Odd powers ($n = 3, 5, \ldots$) all give $u$:

$$
\sum_{n=3,5,\ldots}\frac{(-\mathrm{i}\theta)^n}{n!}u^n = u\sum_{n=3,5,\ldots}\frac{(-\mathrm{i}\theta)^n}{n!} = u\bigl(-\mathrm{i}\sin\theta - (-\mathrm{i}\theta)\bigr) = -\mathrm{i}u(\sin\theta - \theta).
$$

Combining with the $n=0, 1$ terms:

$$
\hat D^{(1)}(\boldsymbol{e}_x, \theta) = \hat I + (-\mathrm{i}\theta)u + u^2(\cos\theta - 1) - \mathrm{i}u(\sin\theta - \theta) = \hat I - \mathrm{i}u\sin\theta + u^2(\cos\theta - 1).
$$

Restoring $u = \hat J_x/\hbar$:

$$
\hat D^{(1)}(\boldsymbol{e}_x, \theta) = \hat I - \mathrm{i}\sin\theta\,\frac{\hat J_x}{\hbar} + (\cos\theta - 1)\,\frac{\hat J_x^2}{\hbar^2}. \quad\checkmark
$$

(c) At $\theta = 2\pi$: $\sin 2\pi = 0$ and $\cos 2\pi - 1 = 0$. Both correction terms vanish, leaving

$$
\hat D^{(1)}(\boldsymbol{e}_x, 2\pi) = \hat I - 0 + 0 = +\hat I.
$$

Contrast: spin-1/2 gives $\hat D^{(1/2)}(\boldsymbol{e}_x, 2\pi) = \cos\pi\hat I - \mathrm{i}\sin\pi(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma}) = -\hat I$ — the half-angle $\theta/2$ in the exponent advances the spinor phase by only $\pi$ at a $2\pi$ physical rotation, producing the sign flip. Spin-1 has *no* half-angle: the exponent contains $\hat J_x$ (not $\hat J_x/2$), and $2\pi$ in the exponent gives $+\hat I$ outright.

**The general pattern.** For spin-$j$, the rotation operator $\hat D^{(j)}(\boldsymbol{n}, 2\pi)$ is diagonal in the $\vert j, m\rangle$ basis with entries $\mathrm{e}^{-2\pi\mathrm{i}m}$. For integer $m$ this is $1$; for half-integer $m$ this is $-1$. **The $\pm$ sign of $\hat D^{(j)}(\boldsymbol{n}, 2\pi)$ is the integer / half-integer signature of $j$ itself.** This dichotomy — and only this dichotomy — is what the spin-statistics theorem promotes to "bosons or fermions" at the multi-particle level (Problem 5).

<!-- ─── -->

**3. Spinor rotation by ninety degrees about x.** Compute the rotation operator $\hat{D}^{(1/2)}(\boldsymbol{e}_x, \pi/2) = \mathrm{e}^{-\mathrm{i}\pi\hat{\sigma}^x/4}$ and apply it to $\vert\uparrow\rangle$. Verify the result is an equal superposition of spin-up and spin-down along $z$, and identify the resulting Bloch direction.

**Solution.**

*The rotation operator.* The spinor rotation formula is $\hat{D}^{(1/2)}(\boldsymbol{n}, \theta) = \cos\tfrac{\theta}{2}\,\hat{I} - \mathrm{i}\sin\tfrac{\theta}{2}\,(\boldsymbol{n}\cdot\hat{\boldsymbol{\sigma}})$. It follows from the exponential because $(\boldsymbol{n}\cdot\hat{\boldsymbol{\sigma}})^2 = \hat{I}$ truncates the Taylor series into separate cosine and sine pieces. Here $\boldsymbol{n} = \boldsymbol{e}_x$ and $\theta = \pi/2$, so $\theta/2 = \pi/4$:

$$
\hat{D}^{(1/2)}(\boldsymbol{e}_x, \pi/2) = \cos\frac{\pi}{4}\,\hat{I} - \mathrm{i}\sin\frac{\pi}{4}\,\hat{\sigma}^x = \frac{1}{\sqrt2}\bigl(\hat{I} - \mathrm{i}\,\hat{\sigma}^x\bigr) = \frac{1}{\sqrt2}\begin{pmatrix}1 & -\mathrm{i}\\ -\mathrm{i} & 1\end{pmatrix}.
$$

*Apply to $\vert\uparrow\rangle$.* With $\vert\uparrow\rangle = (1,0)^{\mathsf T}$,

$$
\hat{D}^{(1/2)}(\boldsymbol{e}_x, \pi/2)\,\vert\uparrow\rangle = \frac{1}{\sqrt2}\begin{pmatrix}1 & -\mathrm{i}\\ -\mathrm{i} & 1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \frac{1}{\sqrt2}\begin{pmatrix}1\\-\mathrm{i}\end{pmatrix} = \frac{1}{\sqrt2}\bigl(\vert\uparrow\rangle - \mathrm{i}\,\vert\downarrow\rangle\bigr).
$$

The probabilities for a $\hat{S}_z$ measurement are $P_\uparrow = \tfrac12$ and $P_\downarrow = \tfrac12$, an exactly equal superposition. ✓

*Bloch direction.* The state $\vert\uparrow\rangle$ has Bloch vector $+\boldsymbol{e}_z$. A rotation by $+\pi/2$ about $\boldsymbol{e}_x$ carries $\boldsymbol{e}_z \to -\boldsymbol{e}_y$ (right-hand rule), so the rotated spinor must point along $-\boldsymbol{e}_y$ — i.e. the $-1$ eigenstate of $\hat{\sigma}^y$, which is $\vert\bar{\mathrm{i}}\rangle = \tfrac{1}{\sqrt2}(\vert\uparrow\rangle - \mathrm{i}\vert\downarrow\rangle)$. The computed result matches exactly, including the relative phase.

This is the canonical *Hadamard-like* rotation: a $\pi/2$ pulse about $\boldsymbol{e}_x$ takes a $\hat{\sigma}^z$-eigenstate to a $\hat{\sigma}^y$-eigenstate. Combined with a subsequent rotation about $\boldsymbol{e}_z$, it can prepare any qubit state from $\vert\uparrow\rangle$ — a single resource for arbitrary state preparation in quantum control.

<!-- ─── -->

**4. Spinor 2-pi rotation and neutron interferometry.** Show that $\hat{D}^{(1/2)}(\boldsymbol{n}, 2\pi) = -\hat{I}$ for spin-1/2, and $\hat{D}^{(1/2)}(\boldsymbol{n}, 4\pi) = +\hat{I}$. Explain why the $-1$ phase is unobservable for a single particle but becomes physical in interferometric experiments — describe how a neutron-interferometry setup detects it.

**Solution.**

*The two rotations.* Insert $\theta = 2\pi$ and $\theta = 4\pi$ into the spinor formula:

$$
\hat{D}^{(1/2)}(\boldsymbol{n}, 2\pi) = \cos\pi\,\hat{I} - \mathrm{i}\sin\pi\,(\boldsymbol{n}\cdot\hat{\boldsymbol{\sigma}}) = (-1)\hat{I} = -\hat{I},
$$

$$
\hat{D}^{(1/2)}(\boldsymbol{n}, 4\pi) = \cos 2\pi\,\hat{I} - \mathrm{i}\sin 2\pi\,(\boldsymbol{n}\cdot\hat{\boldsymbol{\sigma}}) = (+1)\hat{I} = +\hat{I}.
$$

The result is independent of the axis $\boldsymbol{n}$. The half-angle $\theta/2$ in the spinor formula advances the phase by $\pi$ at a full $2\pi$ physical rotation, giving $\mathrm{e}^{\mathrm{i}\pi} = -1$; a full $4\pi$ turn (two complete rotations) returns to $+\hat I$.

*Why $-1$ is invisible for a single particle.* States $\vert\psi\rangle$ and $-\vert\psi\rangle$ differ by a global phase. Every physical prediction — expectation value $\langle\psi\vert\hat O\vert\psi\rangle$ or Born probability $\vert\langle\phi\vert\psi\rangle\vert^2$ — has the phase appearing as $(-1)^*(-1) = 1$, cancelling. No measurement on an isolated spin can distinguish "rotated by $2\pi$" from "not rotated."

*Interferometric signature: neutron experiments.* Split a neutron's amplitude into two coherent branches. Apply a $2\pi$ rotation (e.g., via a magnetic field traversed during transit) on one branch only, while leaving the other branch in its initial state. Recombine the two branches at the output. They add as

$$
\vert\psi_{\mathrm{out}}\rangle \propto \vert\psi\rangle + \hat{D}^{(1/2)}(\boldsymbol{n}, 2\pi)\,\vert\psi\rangle = \vert\psi\rangle + (-\vert\psi\rangle) = 0,
$$

producing **destructive interference** at the detector. The naive classical prediction "$2\pi$ rotation = no rotation" would have given doubled amplitude (constructive interference). The actual measured intensity oscillates with the applied rotation angle as $\cos^2(\theta/2)$, completing one full oscillation at $\theta = 4\pi$ — exactly the $\theta/2$ half-angle signature.

This was confirmed experimentally by Rauch et al. (1975) and Werner et al. (1975) using thermal neutrons in a single-crystal silicon interferometer. The result is one of the most direct empirical tests of the spinor representation: a $2\pi$ rotation observably differs from no rotation, but only via *relative* phase with a reference path. The sign is also the algebraic origin of fermionic antisymmetry under particle exchange (developed in 2.1.2) — two-fermion wavefunctions pick up the same $-1$ under the geometric "swap = exchange = $2\pi$ rotation" identification.

<!-- ─── -->

**5. Spin-j rotation: integer vs half-integer.** Generalise the $2\pi$ rotation comparison to arbitrary spin.

(a) Compute $\hat D^{(j)}(\boldsymbol{e}_z, 2\pi) = \mathrm{e}^{-2\pi\mathrm{i}\hat J_z/\hbar}$ in the $\vert j, m\rangle$ basis. Show it is diagonal with entries $\mathrm{e}^{-2\pi\mathrm{i}m}$.

(b) Evaluate $\mathrm{e}^{-2\pi\mathrm{i}m}$ for integer $m$ versus half-integer $m$. Conclude that for integer $j$, $\hat D^{(j)}(\boldsymbol{e}_z, 2\pi) = +\hat I$, while for half-integer $j$, $\hat D^{(j)}(\boldsymbol{e}_z, 2\pi) = -\hat I$.

(c) By the rotation-axis-independence of the $2\pi$ behaviour (Problem 4 for spin-1/2 and Problem 2 for spin-1), state the general formula

$$
\hat D^{(j)}(\boldsymbol n, 2\pi) = (-1)^{2j}\,\hat I.
$$

(d) Connect to the **spin-statistics theorem** quoted in the lecture: integer spin ↔ bosons; half-integer spin ↔ fermions. Argue that the $(-1)^{2j}$ factor under a $2\pi$ rotation is the *single-particle* signature of the multi-particle exchange statistics — the same minus sign that flips a fermion wavefunction under particle swap.

**Solution.**

(a) The operator $\hat J_z$ is diagonal in the $\vert j, m\rangle$ basis with eigenvalues $\hbar m$. The exponential is diagonal with entries $\mathrm{e}^{-2\pi\mathrm{i}m}$:

$$
\hat D^{(j)}(\boldsymbol{e}_z, 2\pi) = \mathrm{e}^{-2\pi\mathrm{i}\hat J_z/\hbar} = \sum_m \mathrm{e}^{-2\pi\mathrm{i}m}\vert j, m\rangle\langle j, m\vert.
$$

(b) For integer $m$ (any element of $\{-j, \ldots, +j\}$ when $j$ is integer): $\mathrm{e}^{-2\pi\mathrm{i}m} = 1$. The whole sum collapses to $\sum_m\vert j, m\rangle\langle j, m\vert = \hat I$.

For half-integer $m$ (when $j$ is half-integer): $\mathrm{e}^{-2\pi\mathrm{i}m} = \mathrm{e}^{-\mathrm{i}\pi(2m)} = (-1)^{2m}$. Since $2m$ is an odd integer for half-integer $m$, this equals $-1$ for every $m$. The whole sum becomes $-\sum_m\vert j, m\rangle\langle j, m\vert = -\hat I$.

So integer $j$ gives $+\hat I$, half-integer $j$ gives $-\hat I$.

(c) The result depends only on the spectrum of $\hat J_z$, which is fixed by $j$ alone (not the rotation axis). Equivalently, $\hat D^{(j)}(\boldsymbol n, 2\pi) = \hat U^\dagger\hat D^{(j)}(\boldsymbol{e}_z, 2\pi)\hat U$ for some unitary $\hat U$ implementing the change of basis from $\boldsymbol n$ to $\boldsymbol{e}_z$, and the central element $(-1)^{2j}\hat I$ commutes with every $\hat U$. So

$$
\hat D^{(j)}(\boldsymbol n, 2\pi) = (-1)^{2j}\,\hat I
$$

for every direction $\boldsymbol n$ and every spin $j$.

(d) The spin-statistics theorem says: integer-spin particles (bosons) have *symmetric* multi-particle wavefunctions under exchange; half-integer-spin particles (fermions) have *antisymmetric* wavefunctions.

There is a deep connection between **single-particle $2\pi$ rotation** and **two-particle exchange**: in a continuous path that swaps the two particles in 3D space, each particle effectively rotates by $2\pi$ relative to the other (a fact made geometrically explicit in the spin-statistics proof in relativistic field theory). The two-particle exchange therefore inherits the factor $(-1)^{2j}\hat I$ from the single-particle $2\pi$ rotation:

- Integer $j$: $(-1)^{2j} = +1$ → symmetric exchange → bosons.
- Half-integer $j$: $(-1)^{2j} = -1$ → antisymmetric exchange → fermions.

So the *integer/half-integer dichotomy of spin* (read off from a single particle's $2\pi$ rotation in Problem 4 and Problem 2) is **the same mathematical fact** as the *symmetric/antisymmetric dichotomy of multi-particle wavefunctions* (used in 2.1.2 to derive Pauli exclusion). The neutron-interferometry $-1$ of Problem 4 is the *first-quantised* shadow of the *second-quantised* anticommutator $\{\hat c^\dagger, \hat c^\dagger\} = 0$ of 2.1.3 — the same algebraic minus sign, viewed in two different formalisms.

<!-- ─── -->

**6. Higher spin representations.** For general spin-$j$, explain why the representation is $(2j+1)$-dimensional and irreducible. What does "irreducible" mean physically?

**Solution.**

*Why the dimension is $2j+1$.* A spin-$j$ system is described by the simultaneous eigenstates $\vert j,m\rangle$ of the commuting pair $\hat{J}^2$ and $\hat{J}_z$, with $\hat{J}^2\vert j,m\rangle = \hbar^2 j(j+1)\vert j,m\rangle$ and $\hat{J}_z\vert j,m\rangle = \hbar m\vert j,m\rangle$. The algebra fixes the allowed $m$: the ladder operators $\hat{J}_\pm$ shift $m$ by one unit, and the chain must terminate at both ends because the squared norms

$$
\big\|\hat{J}_+\vert j,m\rangle\big\|^2 = \hbar^2(j-m)(j+m+1), \qquad \big\|\hat{J}_-\vert j,m\rangle\big\|^2 = \hbar^2(j+m)(j-m+1)
$$

cannot be negative. They vanish exactly at $m = +j$ (top) and $m = -j$ (bottom), so $m$ runs over

$$
m = -j,\; -j+1,\; \ldots,\; j-1,\; j,
$$

in unit steps. Counting endpoints inclusive, that is $2j+1$ values, hence a $(2j+1)$-dimensional Hilbert space carrying the representation.

*Why it is irreducible.* An *invariant subspace* of a representation is a subspace mapped into itself by every operator of the representation — here every rotation $\hat{D}^{(j)}(\boldsymbol{n},\theta)$, equivalently every generator $\hat{J}_x, \hat{J}_y, \hat{J}_z$ (since $\hat{J}_\pm$ are built from them). Within a spin-$j$ multiplet the only invariant subspaces are the trivial ones, $\{0\}$ and the whole space: starting from any single state $\vert j,m\rangle$, repeated action of $\hat{J}_+$ and $\hat{J}_-$ reaches every other $\vert j,m'\rangle$, because each rung connects to its neighbors with a *nonzero* coefficient. Any invariant subspace containing one nonzero vector must therefore contain all $2j+1$ basis states. A representation with no proper nontrivial invariant subspace is, by definition, **irreducible**.

*Physical meaning.* Irreducibility says a spin-$j$ system is an *elementary* rotational object — it cannot be split into smaller, rotationally independent pieces. Under rotations all $2j+1$ states mix together; there is no way to partition them into subsets that each transform only among themselves. The contrast is a *reducible* representation, such as the four-dimensional space of two spin-1/2 particles: it splits into a spin-1 triplet and a spin-0 singlet, $\tfrac12\otimes\tfrac12 = 1\oplus 0$, two blocks that never mix under any rotation. Irreducible representations are thus the "atoms" of angular momentum: every rotational system decomposes into a direct sum of them, and analyzing that decomposition is the subject of angular-momentum addition (§2.2.3).

<!-- ─── -->

★ **7. Spin-1 time evolution.** A spin-1 particle is prepared in $\vert 1, +1\rangle$ and evolves under $\hat{H} = \omega\hat{J}_x^2$ (set $\hbar = 1$).

(a) Write $\hat{J}_x^2$ as a $3\times 3$ matrix in the $\{\vert 1,+1\rangle, \vert 1,0\rangle, \vert 1,-1\rangle\}$ basis. Show that $\vert 1,0\rangle$ is an eigenstate, and find the two eigenvalues and eigenstates of $\hat{J}_x^2$ in the $\{\vert 1,+1\rangle, \vert 1,-1\rangle\}$ subspace.

(b) Decompose $\vert 1,+1\rangle$ in the eigenbasis of $\hat{J}_x^2$ and find $\vert\psi(t)\rangle$. Show that $P_{+1}(t) = \cos^2(\omega t/2)$, $P_{-1}(t) = \sin^2(\omega t/2)$, and $P_0 = 0$ at all times.

(c) At $t = \pi/(2\omega)$ the state has $P_{+1} = P_{-1} = 1/2$. One measures $\hat{J}_z^2$ and obtains the outcome $1$ (i.e. $m^2 = 1$). What is the post-measurement state? Compute $\langle\hat{J}_z\rangle$.

**Solution.**

**(a)** With $\hbar = 1$, the spin-1 operator $\hat{J}_x = \tfrac{1}{\sqrt2}\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix}$. Square it:

$$
\hat{J}_x^2 = \frac12\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix}\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix} = \frac12\begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix}.
$$

The middle row and column couple only to themselves: $\hat{J}_x^2$ is block-diagonal, an isolated $\vert 1,0\rangle$ entry plus a $2\times 2$ block on $\{\vert 1,+1\rangle, \vert 1,-1\rangle\}$.

*The state $\vert 1,0\rangle$.* With $\vert 1,0\rangle = (0,1,0)^{\mathsf T}$,

$$
\hat{J}_x^2\,\vert 1,0\rangle = \frac12\begin{pmatrix}1&0&1\\0&2&0\\1&0&1\end{pmatrix}\begin{pmatrix}0\\1\\0\end{pmatrix} = \begin{pmatrix}0\\1\\0\end{pmatrix} = 1\cdot\vert 1,0\rangle,
$$

so $\vert 1,0\rangle$ is an eigenstate with eigenvalue $1$.

*The $\{\vert 1,+1\rangle, \vert 1,-1\rangle\}$ block.* Restricted to this subspace, $\hat{J}_x^2\big|_{\text{block}} = \frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$. Eigenvalues $\lambda = 0, 1$, with eigenvectors

$$
\vert s\rangle = \tfrac{1}{\sqrt2}(\vert 1,+1\rangle + \vert 1,-1\rangle) \;\;(\lambda = 1), \qquad \vert a\rangle = \tfrac{1}{\sqrt2}(\vert 1,+1\rangle - \vert 1,-1\rangle) \;\;(\lambda = 0).
$$

Consistent with the $\hat J_x^2$ spectrum $\{m_x^2 : m_x \in \{-1, 0, +1\}\} = \{0, 1, 1\}$: eigenvalue $1$ is doubly degenerate (spanned by $\vert 1,0\rangle$ and $\vert s\rangle$); eigenvalue $0$ is non-degenerate ($\vert a\rangle$).

**(b)** Decompose: $\vert 1,+1\rangle = \tfrac{1}{\sqrt 2}(\vert s\rangle + \vert a\rangle)$. Under $\hat H = \omega\hat J_x^2$, $\vert s\rangle$ has energy $\omega$ and $\vert a\rangle$ has energy $0$:

$$
\vert\psi(t)\rangle = \tfrac{1}{\sqrt 2}\bigl(\mathrm{e}^{-\mathrm{i}\omega t}\vert s\rangle + \vert a\rangle\bigr) = \tfrac{1}{2}\Bigl[(\mathrm{e}^{-\mathrm{i}\omega t}+1)\vert 1,+1\rangle + (\mathrm{e}^{-\mathrm{i}\omega t}-1)\vert 1,-1\rangle\Bigr].
$$

Probabilities via $\vert\mathrm{e}^{-\mathrm{i}\omega t}\pm 1\vert^2 = 2 \pm 2\cos\omega t$:

$$
P_{+1}(t) = \tfrac{1}{4}\vert\mathrm{e}^{-\mathrm{i}\omega t}+1\vert^2 = \cos^2(\omega t/2), \qquad P_{-1}(t) = \sin^2(\omega t/2), \qquad P_0 = 0.
$$

Since $\hat J_x^2$ is block-diagonal, no $\vert 1, 0\rangle$ component is ever generated from the initial $\vert 1, +1\rangle$. Population oscillates between $m = +1$ and $m = -1$ at angular frequency $\omega$.

**(c)** At $t = \pi/(2\omega)$, $\omega t = \pi/2$, so $\mathrm{e}^{-\mathrm{i}\omega t} = -\mathrm{i}$:

$$
\vert\psi\rangle = \tfrac{1}{2}\bigl[(1 - \mathrm{i})\vert 1,+1\rangle - (1 + \mathrm{i})\vert 1,-1\rangle\bigr] = \tfrac{\mathrm{e}^{-\mathrm{i}\pi/4}}{\sqrt 2}\bigl(\vert 1,+1\rangle - \mathrm{i}\vert 1,-1\rangle\bigr).
$$

$\hat J_z^2$ has eigenvalues $\{m^2\} = \{1, 0, 1\}$, with the $m^2 = 1$ eigenspace spanned by $\{\vert 1, +1\rangle, \vert 1, -1\rangle\}$ — *degenerate*. The state $\vert\psi\rangle$ lies entirely in this eigenspace, so measurement of $\hat J_z^2$ returns $1$ with certainty (probability $1$). By the projection postulate the state is unchanged:

$$
\vert\psi_{\mathrm{after}}\rangle = \tfrac{1}{\sqrt 2}(\vert 1,+1\rangle - \mathrm{i}\vert 1,-1\rangle).
$$

The degenerate measurement extracts $m^2 = 1$ but cannot distinguish $m = +1$ from $m = -1$ — the coherent superposition survives inside the eigenspace.

*Expectation:* $\langle\hat J_z\rangle = (+1)\cdot\tfrac{1}{2} + (-1)\cdot\tfrac{1}{2} = 0$. Knowing only $m^2 = 1$ leaves $m = +1$ and $m = -1$ equally likely; the mean cancels. The spread is maximal, $\Delta\hat J_z = 1$.
