# 2.2.1 Angular Momentum Algebra
Worked solutions for the homework problems in the [2.2.1 Angular Momentum Algebra](../ch2_identical-particles/2-2-1-angular-momentum-algebra) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Spin-1 verification of the angular-momentum algebra.** The lecture states that the commutation relations $[\hat J_i,\hat J_j] = \mathrm{i}\hbar\epsilon_{ijk}\hat J_k$ hold for *any* representation. The spin-1/2 case follows from the Pauli commutators (1.1.3). Here, verify the relation directly for the spin-1 representation, in the basis $\{\vert 1,+1\rangle, \vert 1,0\rangle, \vert 1,-1\rangle\}$ where $\hat J_z = \hbar\,\mathrm{diag}(1, 0, -1)$ and

$$
\hat J_x = \frac{\hbar}{\sqrt 2}\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}, \qquad \hat J_y = \frac{\hbar}{\sqrt 2}\begin{pmatrix} 0 & -\mathrm{i} & 0 \\ \mathrm{i} & 0 & -\mathrm{i} \\ 0 & \mathrm{i} & 0 \end{pmatrix}.
$$

(a) Compute $[\hat J_x, \hat J_y]$ by matrix multiplication and verify it equals $\mathrm{i}\hbar\hat J_z$.

(b) Compute $\hat J^2 = \hat J_x^2 + \hat J_y^2 + \hat J_z^2$ explicitly and confirm $\hat J^2 = 2\hbar^2\hat I = \hbar^2 \cdot 1\cdot(1+1)\hat I$, i.e. the Casimir eigenvalue $j(j+1) = 2$ for $j = 1$.

(c) Compare with the spin-1/2 case from 1.1.3 (where $\hat J^2 = \frac{3}{4}\hbar^2\hat I$). State the general pattern: the Casimir eigenvalue is $j(j+1)\hbar^2$ for every spin-$j$ multiplet, set by $\hat J^2$ alone.

**Solution.**

(a) Compute the two products. Let $a \equiv \hbar/\sqrt 2$. Then

$$
\hat J_x\hat J_y = a^2 \begin{pmatrix} 0&1&0\\ 1&0&1\\ 0&1&0\end{pmatrix}\begin{pmatrix} 0&-\mathrm{i}&0\\ \mathrm{i}&0&-\mathrm{i}\\ 0&\mathrm{i}&0\end{pmatrix} = a^2\begin{pmatrix} \mathrm{i} & 0 & -\mathrm{i} \\ 0 & 0 & 0 \\ \mathrm{i} & 0 & -\mathrm{i}\end{pmatrix},
$$

$$
\hat J_y\hat J_x = a^2 \begin{pmatrix} 0&-\mathrm{i}&0\\ \mathrm{i}&0&-\mathrm{i}\\ 0&\mathrm{i}&0\end{pmatrix}\begin{pmatrix} 0&1&0\\ 1&0&1\\ 0&1&0\end{pmatrix} = a^2\begin{pmatrix} -\mathrm{i} & 0 & -\mathrm{i} \\ 0 & 0 & 0 \\ \mathrm{i} & 0 & \mathrm{i}\end{pmatrix}.
$$

Subtract:

$$
[\hat J_x,\hat J_y] = a^2 \begin{pmatrix} 2\mathrm{i} & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -2\mathrm{i}\end{pmatrix} = 2\mathrm{i}a^2\,\mathrm{diag}(1, 0, -1) = \mathrm{i}\hbar^2\,\mathrm{diag}(1, 0, -1) = \mathrm{i}\hbar\,\hat J_z. \quad\checkmark
$$

(using $2a^2 = 2\cdot\hbar^2/2 = \hbar^2$). The spin-1 matrices reproduce the universal algebra.

(b) Compute $\hat J_x^2$ and $\hat J_y^2$:

$$
\hat J_x^2 = a^2\begin{pmatrix} 1 & 0 & 1 \\ 0 & 2 & 0 \\ 1 & 0 & 1\end{pmatrix}, \qquad \hat J_y^2 = a^2\begin{pmatrix} 1 & 0 & -1 \\ 0 & 2 & 0 \\ -1 & 0 & 1\end{pmatrix},
$$

$$
\hat J_z^2 = \hbar^2\,\mathrm{diag}(1, 0, 1) = 2a^2\,\mathrm{diag}(1, 0, 1).
$$

Add term by term. Off-diagonals: $\hat J_x^2 + \hat J_y^2$ cancels the $\pm 1$ corners, leaving zero off-diagonal. Diagonal: $a^2(1+1) + a^2(1+1) = 4a^2 = 2\hbar^2$ for entries $(1,1)$ and $(3,3)$; $a^2(2) + a^2(2) = 4a^2 = 2\hbar^2$ for entry $(2,2)$; plus $\hat J_z^2$ contributions $2a^2 = \hbar^2, 0, \hbar^2$. Wait, let me redo:

$\hat J_x^2 + \hat J_y^2 = a^2\begin{pmatrix}2 & 0 & 0\\ 0 & 4 & 0\\ 0 & 0 & 2\end{pmatrix} = \hbar^2\,\mathrm{diag}(1, 2, 1)$.

Add $\hat J_z^2 = \hbar^2\,\mathrm{diag}(1, 0, 1)$:

$$
\hat J^2 = \hbar^2\,\mathrm{diag}(2, 2, 2) = 2\hbar^2\,\hat I = \hbar^2\cdot j(j+1)\,\hat I\quad\text{with } j(j+1) = 2. \quad\checkmark
$$

So every spin-1 basis state has the same Casimir eigenvalue $\hbar^2\cdot 2$, identifying $j = 1$.

(c) For spin-1/2: $\hat J^2 = \tfrac{\hbar^2}{4}((\hat\sigma^x)^2 + (\hat\sigma^y)^2 + (\hat\sigma^z)^2) = \tfrac{\hbar^2}{4}\cdot 3\hat I = \tfrac{3}{4}\hbar^2\hat I$, consistent with $j(j+1) = \tfrac{1}{2}\cdot\tfrac{3}{2} = \tfrac{3}{4}$.

**General pattern.** On any spin-$j$ multiplet, $\hat J^2 = \hbar^2 j(j+1)\hat I_{2j+1}$. The Casimir labels the *multiplet*; the value $j(j+1)$ is set by the algebra and is the same for every state in the multiplet (no $m$-dependence). The quantum spectrum of total angular momentum is therefore *non-classical* — a state with $j = 1$ has $\vert\hat{\boldsymbol J}\vert = \hbar\sqrt 2$, not $\hbar\cdot 1$; this excess is the hallmark of quantum AM and underlies the vector-model picture of Problem 7.

<!-- ─── -->

**2. j=3/2 multiplet by repeated lowering.** Start from the stretched state $\vert 3/2, 3/2\rangle$ and apply the lowering operator $\hat J_-$ repeatedly to construct all four states of the spin-$\tfrac{3}{2}$ multiplet.

(a) Verify that $\hat J_+\vert 3/2, 3/2\rangle = 0$ using the ladder formula $\hat J_+\vert j,m\rangle = \hbar\sqrt{(j-m)(j+m+1)}\vert j, m+1\rangle$.

(b) Compute $\hat J_-\vert 3/2, m\rangle$ for $m = 3/2, 1/2, -1/2, -3/2$, using $\hat J_-\vert j,m\rangle = \hbar\sqrt{(j+m)(j-m+1)}\vert j, m-1\rangle$. State the coefficient in each step.

(c) Verify that $\hat J_-\vert 3/2, -3/2\rangle = 0$ — the multiplet terminates at the bottom rung.

(d) The four states $\{\vert 3/2, 3/2\rangle, \vert 3/2, 1/2\rangle, \vert 3/2, -1/2\rangle, \vert 3/2, -3/2\rangle\}$ form a $4$-dimensional representation. Argue from this construction that the dimension of a spin-$j$ multiplet is $2j+1$.

**Solution.**

(a) With $j = 3/2$, $m = 3/2$: $(j-m) = 0$, so $\hat J_+\vert 3/2,3/2\rangle = 0$. ✓ The factor $(j-m)$ guarantees that the multiplet does not exceed $m = j$ at the top.

(b) Apply the lowering formula step by step:

$$
\hat J_-\vert 3/2, 3/2\rangle = \hbar\sqrt{(3/2 + 3/2)(3/2 - 3/2 + 1)}\vert 3/2, 1/2\rangle = \hbar\sqrt{3\cdot 1}\,\vert 3/2, 1/2\rangle = \hbar\sqrt 3\,\vert 3/2, 1/2\rangle.
$$

$$
\hat J_-\vert 3/2, 1/2\rangle = \hbar\sqrt{(3/2 + 1/2)(3/2 - 1/2 + 1)}\vert 3/2, -1/2\rangle = \hbar\sqrt{2\cdot 2}\,\vert 3/2, -1/2\rangle = 2\hbar\,\vert 3/2, -1/2\rangle.
$$

$$
\hat J_-\vert 3/2, -1/2\rangle = \hbar\sqrt{(3/2 - 1/2)(3/2 + 1/2 + 1)}\vert 3/2, -3/2\rangle = \hbar\sqrt{1\cdot 3}\,\vert 3/2, -3/2\rangle = \hbar\sqrt 3\,\vert 3/2, -3/2\rangle.
$$

The coefficients $\hbar\sqrt 3, 2\hbar, \hbar\sqrt 3$ form a *palindromic* sequence — the ladder is symmetric under reflection $m\to -m$, because $\sqrt{(j+m)(j-m+1)} = \sqrt{(j+(-m+1))(j-(-m+1)+1)}$ — i.e. the lowering coefficient from $m$ equals the raising coefficient from $-m-1$.

(c) With $m = -3/2$: $(j+m) = 0$, so $\hat J_-\vert 3/2, -3/2\rangle = 0$. ✓ The factor $(j+m)$ guarantees that the multiplet does not fall below $m = -j$.

(d) The multiplet runs from $m = j$ down to $m = -j$ in unit steps, giving the states $m = j, j-1, j-2, \ldots, -j+1, -j$. The number of integer (or half-integer) steps from $-j$ to $j$ inclusive is $2j + 1$. For $j = 3/2$ this is $4$; for $j = 1$ it is $3$; for $j = 1/2$ it is $2$ (the Bloch sphere). Every multiplet has dimension $2j+1$ — the dimension of the irreducible representation of $\mathfrak{su}(2)$ with Casimir $\hbar^2 j(j+1)$.

<!-- ─── -->

**3. Ladder formula via Schwinger bosons.** Recall the Schwinger boson construction from 2.1.3 Problem 10: spin operators $\hat S_+ = \hat a^\dagger\hat b$, $\hat S_- = \hat b^\dagger\hat a$, $\hat S_z = \tfrac{1}{2}(\hat a^\dagger\hat a - \hat b^\dagger\hat b)$, with the Fock state $\vert n_a, n_b\rangle$ identified with $\vert s, m\rangle$ via $s = (n_a + n_b)/2$ and $m = (n_a - n_b)/2$. Use the bosonic algebra to derive the angular-momentum ladder formula.

(a) Express $n_a$ and $n_b$ in terms of $s$ and $m$.

(b) Apply $\hat S_+ = \hat a^\dagger\hat b$ to $\vert n_a, n_b\rangle$ and read off the coefficient using $\hat a^\dagger\vert n_a\rangle = \sqrt{n_a+1}\vert n_a+1\rangle$ and $\hat b\vert n_b\rangle = \sqrt{n_b}\vert n_b-1\rangle$. Show that

$$
\hat S_+\vert s, m\rangle = \sqrt{(s-m)(s+m+1)}\,\vert s, m+1\rangle,
$$

reproducing the lecture's ladder formula (in units $\hbar = 1$).

(c) Argue that this derivation makes the ladder coefficient $\sqrt{(s-m)(s+m+1)}$ **automatic** — it emerges directly from the bosonic normalisation factors $\sqrt{n}$, with no separate calculation needed. Contrast with the standard approach (lecture), which derives the same coefficient from $\hat J_+\hat J_- = \hat J^2 - \hat J_z^2 + \hbar\hat J_z$.

**Solution.**

(a) From $s = (n_a + n_b)/2$ and $m = (n_a - n_b)/2$:

$$
n_a = s + m, \qquad n_b = s - m.
$$

(For consistency, $s$ is a non-negative half-integer (set by $N = n_a + n_b \ge 0$) and $m$ runs from $-s$ to $+s$ in unit steps — exactly the AM multiplet structure.)

(b) Apply $\hat S_+ = \hat a^\dagger\hat b$ to $\vert n_a, n_b\rangle$:

$$
\hat S_+\vert n_a, n_b\rangle = \sqrt{n_b}\,\sqrt{n_a+1}\,\vert n_a+1, n_b-1\rangle.
$$

Under the identification $\vert n_a, n_b\rangle \leftrightarrow \vert s, m\rangle$ with $s$ fixed (since $\hat S_+$ raises $n_a$ by one and lowers $n_b$ by one, preserving $n_a + n_b = 2s$) and $m \to m + 1$ (since $n_a - n_b$ increases by $2$):

$$
\hat S_+\vert s, m\rangle = \sqrt{(s-m)(s+m+1)}\,\vert s, m+1\rangle,
$$

substituting $n_b = s - m$ and $n_a + 1 = s + m + 1$.

(c) The Schwinger construction makes the ladder formula **structurally obvious**: it is simply the product of two boson normalisation factors $\sqrt{n_b}\cdot\sqrt{n_a+1}$. There is no need to compute commutators, evaluate $\hat J^2 - \hat J_z^2$, or take square roots of positive operators — the algebra of $\hat a, \hat b$ does all the work.

The conventional derivation (lecture) starts from $\hat J_+\hat J_- + \hat J_z^2 = \hat J^2$ together with $[\hat J_z, \hat J_\pm] = \pm\hbar\hat J_\pm$, and *constructs* the coefficient $\sqrt{j(j+1) - m(m\pm 1)} = \sqrt{(j\mp m)(j\pm m + 1)}$ via a careful norm calculation. The Schwinger route gives the same answer by reinterpreting AM as a *system of two harmonic oscillators*, where the same combinatorial factor emerges from straightforward Fock-space arithmetic. This is one of the deepest pieces of the Schwinger boson formalism: it *trivialises* the most computationally heavy part of angular-momentum theory.

<!-- ─── -->

**4. Ladder action: termination and verification.** Use $\hat J_+\vert j, m\rangle = \hbar\sqrt{(j-m)(j+m+1)}\,\vert j, m+1\rangle$ to explain why $\hat J_+\vert 1,1\rangle = 0$. Then compute $\hat J_-\vert 1, 0\rangle$ from the lowering formula and verify the result using the spin-1 matrix representation from Problem 1.

**Solution.**

*Why $\hat J_+\vert 1,1\rangle = 0$.* Set $j=1$, $m=1$ in the raising formula. The coefficient $(j-m) = 0$:

$$
\hat J_+\vert 1,1\rangle = \hbar\sqrt{(1-1)(1+1+1)}\,\vert 1,2\rangle = 0.
$$

The factor $(j-m)$ vanishes at $m = j$, terminating the multiplet at the top rung. A nonzero $\hat J_+\vert 1,1\rangle$ would be a state with $m = 2 > j$, which doesn't exist in the spin-1 multiplet. The ladder closes *exactly* at $m = \pm j$.

*Compute $\hat J_-\vert 1, 0\rangle$.* From $\hat J_-\vert j,m\rangle = \hbar\sqrt{(j+m)(j-m+1)}\vert j, m-1\rangle$ with $j = 1$, $m = 0$:

$$
\hat J_-\vert 1,0\rangle = \hbar\sqrt{(1+0)(1-0+1)}\,\vert 1,-1\rangle = \hbar\sqrt 2\,\vert 1,-1\rangle.
$$

*Matrix verification.* Construct $\hat J_- = \hat J_x - \mathrm{i}\hat J_y$ from the spin-1 matrices in Problem 1. Computing,

$$
\hat J_- = \frac{\hbar}{\sqrt 2}\begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix} - \mathrm{i}\,\frac{\hbar}{\sqrt 2}\begin{pmatrix} 0 & -\mathrm{i} & 0 \\ \mathrm{i} & 0 & -\mathrm{i} \\ 0 & \mathrm{i} & 0\end{pmatrix} = \frac{\hbar}{\sqrt 2}\begin{pmatrix} 0 & 0 & 0 \\ 2 & 0 & 0 \\ 0 & 2 & 0\end{pmatrix} = \hbar\sqrt 2\begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0\end{pmatrix}.
$$

Acting on $\vert 1, 0\rangle = (0, 1, 0)^{\mathsf T}$:

$$
\hat J_-\vert 1, 0\rangle = \hbar\sqrt 2\begin{pmatrix} 0\\ 0\\ 1\end{pmatrix} = \hbar\sqrt 2\,\vert 1, -1\rangle. \quad\checkmark
$$

The matrix calculation and the ladder formula agree exactly — and they must, because the lecture's ladder formula was *constructed* to be consistent with the matrix representation of each multiplet.

<!-- ─── -->

**5. Transverse variance on an angular-momentum eigenstate.** Compute $\langle\hat J_x\rangle$, $\langle\hat J_x^2\rangle$, and the variance $(\Delta\hat J_x)^2$ on a state $\vert j, m\rangle$.

(a) Express $\hat J_x = \tfrac{1}{2}(\hat J_+ + \hat J_-)$ and use it to compute $\langle\hat J_x\rangle = \langle j, m\vert\hat J_x\vert j, m\rangle$. Explain in one sentence why the result is zero.

(b) Use the lecture's ladder product identity $\hat J_+\hat J_- + \hat J_-\hat J_+ = 2(\hat J^2 - \hat J_z^2)$ to compute $\hat J_x^2 + \hat J_y^2 = \tfrac{1}{2}(\hat J_+\hat J_- + \hat J_-\hat J_+) = \hat J^2 - \hat J_z^2$. Conclude

$$
\langle\hat J_x^2\rangle + \langle\hat J_y^2\rangle = \hbar^2\bigl[j(j+1) - m^2\bigr].
$$

(c) By the symmetry of the algebra under $x \leftrightarrow y$ on a $\hat J_z$-eigenstate, $\langle\hat J_x^2\rangle = \langle\hat J_y^2\rangle$. Conclude

$$
(\Delta\hat J_x)^2 = \langle\hat J_x^2\rangle - \langle\hat J_x\rangle^2 = \frac{\hbar^2}{2}\bigl[j(j+1) - m^2\bigr].
$$

(d) Identify the limiting values: at the stretched state $m = \pm j$, $(\Delta\hat J_x)^2 = \hbar^2 j/2$ — *not* zero, even though the state is a $\hat J_z$ eigenstate. Explain physically why even the most "extreme" $\hat J_z$ eigenstate has *some* transverse uncertainty — the quantum AM vector cannot be perfectly aligned with $\boldsymbol{e}_z$.

**Solution.**

(a) Using $\hat J_x = \tfrac{1}{2}(\hat J_+ + \hat J_-)$ and the ladder action $\hat J_\pm\vert j,m\rangle \propto \vert j, m\pm 1\rangle$:

$$
\langle j, m\vert\hat J_x\vert j, m\rangle = \tfrac{1}{2}\langle j, m\vert(\hat J_+ + \hat J_-)\vert j, m\rangle.
$$

Both $\hat J_+\vert j,m\rangle$ and $\hat J_-\vert j,m\rangle$ shift to states orthogonal to $\vert j, m\rangle$ (different $\hat J_z$ eigenvalue), so each matrix element vanishes. Hence $\langle\hat J_x\rangle = 0$. The same argument gives $\langle\hat J_y\rangle = 0$. **Physically:** a $\hat J_z$ eigenstate has no preferred direction in the $xy$-plane (rotational symmetry about $\boldsymbol{e}_z$), so the transverse expectation values must vanish.

(b) Compute $\hat J^2 = \hat J_x^2 + \hat J_y^2 + \hat J_z^2$, so $\hat J_x^2 + \hat J_y^2 = \hat J^2 - \hat J_z^2$. Take the expectation on $\vert j, m\rangle$:

$$
\langle\hat J_x^2\rangle + \langle\hat J_y^2\rangle = \langle\hat J^2\rangle - \langle\hat J_z^2\rangle = \hbar^2 j(j+1) - \hbar^2 m^2 = \hbar^2\bigl[j(j+1) - m^2\bigr].
$$

(c) The state $\vert j, m\rangle$ has axial symmetry about $\boldsymbol{e}_z$ — rotations about $\boldsymbol{e}_z$ leave it invariant (up to a phase). This symmetry implies $\langle\hat J_x^2\rangle = \langle\hat J_y^2\rangle$. So each equals half the sum:

$$
\langle\hat J_x^2\rangle = \frac{\hbar^2}{2}\bigl[j(j+1) - m^2\bigr].
$$

With $\langle\hat J_x\rangle = 0$ from (a), the variance is exactly this:

$$
(\Delta\hat J_x)^2 = \frac{\hbar^2}{2}\bigl[j(j+1) - m^2\bigr].
$$

(d) At $m = \pm j$:

$$
(\Delta\hat J_x)^2_{\text{stretched}} = \frac{\hbar^2}{2}\bigl[j(j+1) - j^2\bigr] = \frac{\hbar^2 j}{2}.
$$

So $\Delta\hat J_x = \hbar\sqrt{j/2}$ — strictly positive for any $j > 0$. **The quantum AM vector can never be perfectly aligned with $\boldsymbol{e}_z$**: even the stretched state has irreducible transverse uncertainty $\Delta J_x \sim \hbar\sqrt j$. Geometrically, the vector tilts at an angle (Problem 7) from $\boldsymbol{e}_z$, and the transverse uncertainty reflects rotational averaging around this tilted direction. Only in the classical limit $j\to\infty$ does the *relative* uncertainty $\Delta J_x/(\hbar j) \sim 1/\sqrt j \to 0$, recovering the sharp classical AM vector.

<!-- ─── -->

**6. Robertson uncertainty for angular momentum.** Apply the Robertson uncertainty relation from 1.2.2 to the pair $(\hat J_x, \hat J_y)$ on a state $\vert j, m\rangle$.

(a) Using $[\hat J_x, \hat J_y] = \mathrm{i}\hbar\hat J_z$, write down the Robertson bound $\Delta\hat J_x\cdot\Delta\hat J_y \geq \tfrac{1}{2}\vert\langle[\hat J_x, \hat J_y]\rangle\vert$.

(b) Evaluate both sides on the stretched state $\vert j, j\rangle$. Use the variance from Problem 5 and the fact that $\langle\hat J_z\rangle_{\vert j, j\rangle} = \hbar j$.

(c) Show that the Robertson inequality is **saturated** on the stretched state. Why is this the angular-momentum analogue of the minimum-uncertainty state $\vert 0\rangle$ for $(\hat X, \hat Z)$ from 1.2.2 Problem 6?

(d) Compute the ratio $\Delta\hat J_x/\langle\hat J_z\rangle$ on the stretched state and show that in the classical limit $j \to \infty$, this ratio vanishes as $1/\sqrt j$. The angular momentum becomes a sharp 3-vector in the classical limit, recovering the macroscopic notion of AM.

**Solution.**

(a) The Robertson uncertainty relation reads

$$
\Delta\hat J_x\cdot\Delta\hat J_y \geq \tfrac{1}{2}\vert\langle[\hat J_x, \hat J_y]\rangle\vert = \tfrac{\hbar}{2}\vert\langle\hat J_z\rangle\vert.
$$

The bound is **state-dependent**, with right-hand side proportional to $\langle\hat J_z\rangle$ — it is largest on states with definite, large $\hat J_z$.

(b) On $\vert j, j\rangle$, $\langle\hat J_z\rangle = \hbar j$, so the right-hand side is $\tfrac{\hbar^2}{2}j$. From Problem 5(d),

$$
(\Delta\hat J_x)^2 = (\Delta\hat J_y)^2 = \frac{\hbar^2 j}{2}, \qquad \Delta\hat J_x = \Delta\hat J_y = \hbar\sqrt{j/2}.
$$

Therefore

$$
\Delta\hat J_x\cdot\Delta\hat J_y = \frac{\hbar^2 j}{2}.
$$

(c) The two sides are equal — the Robertson inequality is **saturated**: $\Delta\hat J_x\cdot\Delta\hat J_y = \tfrac{\hbar}{2}\langle\hat J_z\rangle$. The stretched state is the angular-momentum analogue of the **minimum-uncertainty state**: it has the smallest possible transverse uncertainty consistent with the algebra (just as $\vert 0\rangle$ does for $(\hat X, \hat Z)$ in 1.2.2 P6, saturating $\Delta\hat X\cdot\Delta\hat Z \geq \tfrac{1}{2}\vert\langle\hat Y\rangle\vert = 0$). The geometric picture: among all states in the spin-$j$ multiplet, $\vert j, j\rangle$ is the most strongly aligned with $\boldsymbol{e}_z$, and its transverse uncertainty is the price the algebra exacts for that alignment.

(d) Ratio:

$$
\frac{\Delta\hat J_x}{\langle\hat J_z\rangle} = \frac{\hbar\sqrt{j/2}}{\hbar j} = \frac{1}{\sqrt{2j}}.
$$

As $j \to \infty$, this ratio vanishes as $j^{-1/2}$. The classical limit: a macroscopic AM with $j \sim 10^{34}$ (typical of a spinning top) has relative transverse uncertainty $\sim 10^{-17}$ — undetectable. **The classical sharp AM vector is the $j\to\infty$ limit of the quantum stretched state**, and the algebraic uncertainty bound — never zero at finite $j$ — disappears smoothly into the macroscopic regime. This is the AM analogue of the harmonic-oscillator's coherent-state classical limit (2.1.3 P3).

<!-- ─── -->

**7. Vector model and the tilt angle.** The state $\vert j, m\rangle$ has $\langle\hat J^2\rangle = \hbar^2 j(j+1)$, $\langle\hat J_z\rangle = \hbar m$, and $\langle\hat J_x\rangle = \langle\hat J_y\rangle = 0$. The **vector model** pictures the angular momentum as a classical 3-vector of length $\vert\boldsymbol J\vert = \hbar\sqrt{j(j+1)}$ with $z$-component $J_z = \hbar m$.

(a) Show that the angle $\theta$ between $\boldsymbol J$ and the $z$-axis satisfies

$$
\cos\theta = \frac{m}{\sqrt{j(j+1)}}.
$$

(b) For the stretched state $\vert j, j\rangle$, find the *minimum* tilt angle $\theta_{\min}$ in terms of $j$, and evaluate it for $j = 1/2$, $j = 1$, and $j = 100$.

(c) The quantum AM cannot be exactly aligned with $\boldsymbol{e}_z$: even the stretched state has $\theta_{\min} > 0$. Use Problem 5 to compute the transverse magnitude $\sqrt{\langle\hat J_x^2 + \hat J_y^2\rangle} = \hbar\sqrt{j(j+1) - m^2}$ and identify it with the *radius* of a precession circle in the vector model.

(d) Compare with the classical prediction: for a classical AM vector of length $\vert\boldsymbol J\vert$ tilted at angle $\theta$, the transverse projection is $\vert\boldsymbol J\vert\sin\theta$. Verify that the quantum result $\hbar\sqrt{j(j+1) - m^2}$ equals $\vert\boldsymbol J\vert\sin\theta$ using the value of $\cos\theta$ from (a).

**Solution.**

(a) Treating $\boldsymbol J$ as a classical vector of length $\hbar\sqrt{j(j+1)}$ with $z$-component $\hbar m$:

$$
\cos\theta = \frac{J_z}{\vert\boldsymbol J\vert} = \frac{\hbar m}{\hbar\sqrt{j(j+1)}} = \frac{m}{\sqrt{j(j+1)}}.
$$

(b) Stretched state: $m = j$.

$$
\cos\theta_{\min} = \frac{j}{\sqrt{j(j+1)}} = \sqrt{\frac{j}{j+1}}.
$$

Evaluations:

- $j = 1/2$: $\cos\theta_{\min} = \sqrt{1/3} \approx 0.577$, so $\theta_{\min} \approx 54.7^\circ$.
- $j = 1$: $\cos\theta_{\min} = \sqrt{1/2} = 1/\sqrt 2$, so $\theta_{\min} = 45^\circ$.
- $j = 100$: $\cos\theta_{\min} = \sqrt{100/101} \approx 0.9950$, so $\theta_{\min} \approx 5.71^\circ$.

The angle decreases monotonically toward $0$ as $j \to \infty$ — the stretched state aligns ever more sharply with $\boldsymbol{e}_z$.

(c) From Problem 5(b),

$$
\sqrt{\langle\hat J_x^2 + \hat J_y^2\rangle} = \hbar\sqrt{j(j+1) - m^2}.
$$

In the vector model this is the radius of the circle traced by the perpendicular projection of $\boldsymbol J$ — the "precession circle" of the semiclassical picture.

(d) Classical: $\vert\boldsymbol J\vert\sin\theta = \hbar\sqrt{j(j+1)}\sin\theta$. Using $\sin^2\theta = 1 - \cos^2\theta = 1 - m^2/[j(j+1)] = [j(j+1) - m^2]/[j(j+1)]$:

$$
\vert\boldsymbol J\vert\sin\theta = \hbar\sqrt{j(j+1)}\cdot\sqrt{\frac{j(j+1) - m^2}{j(j+1)}} = \hbar\sqrt{j(j+1) - m^2},
$$

exactly the quantum result. The vector model is internally consistent: $\boldsymbol J$ has length $\hbar\sqrt{j(j+1)}$, $z$-projection $\hbar m$, and transverse projection $\hbar\sqrt{j(j+1) - m^2}$, all in agreement with the quantum expectation values. The picture should be used with care — $\hat J_x$ and $\hat J_y$ are not simultaneously sharp, so the "precession circle" is a statistical/conceptual aid, not a literal trajectory — but it is the right intuitive bridge between the quantum spectrum and the macroscopic notion of a spinning object.

<!-- ─── -->

★ **8. Quantum bootstrap.** Two operators $\hat{\alpha}$ and $\hat{\beta}$ satisfy the algebraic relations

$$
[\hat{\alpha}, \hat{\beta}] = 2\hat{\alpha}, \quad [\hat{\alpha}^\dagger, \hat{\beta}] = -2\hat{\alpha}^\dagger, \quad [\hat{\alpha}^\dagger, \hat{\alpha}] = 2\hat{\beta}, \quad \{\hat{\alpha}^\dagger, \hat{\alpha}\} = 2\hat{I},
$$

where $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ is the commutator, $\{\hat{A}, \hat{B}\} = \hat{A}\hat{B} + \hat{B}\hat{A}$ is the anticommutator, and $\hat{I}$ is the identity operator.

(a) Show that $\hat{\beta}$ is Hermitian.

(b) Express $\hat{\alpha}^\dagger\hat{\alpha}$ and $\hat{\alpha}\hat{\alpha}^\dagger$ separately as linear combinations of $\hat{\beta}$ and $\hat{I}$.

(c) Show that $(\hat{\alpha}^\dagger)^2 \hat{\alpha}^2 = \hat{\beta}^2 - \hat{I}$ by expressing the left-hand side in terms of $\hat{\beta}$. Using the positivity conditions $\hat{\alpha}^\dagger\hat{\alpha} \geq 0$, $\hat{\alpha}\hat{\alpha}^\dagger \geq 0$, and $(\hat{\alpha}^\dagger)^2\hat{\alpha}^2 \geq 0$, determine the feasible eigenvalues of $\hat{\beta}$.

(d) Identify the angular momentum operators that $\hat{\alpha}$ and $\hat{\beta}$ correspond to (with $\hbar = 1$). What spin representation does this algebra describe? Write the $2\times 2$ matrix representations of $\hat{\alpha}$ and $\hat{\beta}$ in the eigenbasis of $\hat{\beta}$.

**Solution.**

(a) Take the Hermitian conjugate of $[\hat\alpha^\dagger, \hat\alpha] = 2\hat\beta$. The conjugate of a commutator: $[\hat A, \hat B]^\dagger = (\hat A\hat B)^\dagger - (\hat B\hat A)^\dagger = \hat B^\dagger\hat A^\dagger - \hat A^\dagger\hat B^\dagger = [\hat B^\dagger, \hat A^\dagger] = -[\hat A^\dagger, \hat B^\dagger]$. Applying:

$$
2\hat\beta^\dagger = ([\hat\alpha^\dagger, \hat\alpha])^\dagger = -[\hat\alpha, \hat\alpha^\dagger] = [\hat\alpha^\dagger, \hat\alpha] = 2\hat\beta.
$$

So $\hat\beta^\dagger = \hat\beta$. Hermitian. ✓

(b) Add and subtract the commutator and anticommutator:

$$
[\hat\alpha^\dagger, \hat\alpha] + \{\hat\alpha^\dagger, \hat\alpha\} = 2\hat\alpha^\dagger\hat\alpha, \qquad \{\hat\alpha^\dagger, \hat\alpha\} - [\hat\alpha^\dagger, \hat\alpha] = 2\hat\alpha\hat\alpha^\dagger.
$$

Substituting the given relations:

$$
\hat\alpha^\dagger\hat\alpha = \tfrac{1}{2}(2\hat\beta + 2\hat I) = \hat\beta + \hat I,
$$

$$
\hat\alpha\hat\alpha^\dagger = \tfrac{1}{2}(2\hat I - 2\hat\beta) = \hat I - \hat\beta.
$$

(c) Compute $(\hat\alpha^\dagger)^2\hat\alpha^2$ by inserting $\hat\alpha^\dagger\hat\alpha = \hat\beta + \hat I$ in the middle:

$$
(\hat\alpha^\dagger)^2\hat\alpha^2 = \hat\alpha^\dagger(\hat\alpha^\dagger\hat\alpha)\hat\alpha = \hat\alpha^\dagger(\hat\beta + \hat I)\hat\alpha = \hat\alpha^\dagger\hat\beta\hat\alpha + \hat\alpha^\dagger\hat\alpha.
$$

For the first term, use $[\hat\alpha^\dagger, \hat\beta] = -2\hat\alpha^\dagger$, i.e. $\hat\alpha^\dagger\hat\beta = \hat\beta\hat\alpha^\dagger - 2\hat\alpha^\dagger$, then $\hat\alpha^\dagger\hat\alpha = \hat\beta + \hat I$:

$$
\begin{split}
\hat\alpha^\dagger\hat\beta\hat\alpha
&= (\hat\beta\hat\alpha^\dagger - 2\hat\alpha^\dagger)\hat\alpha \\
&= \hat\beta\hat\alpha^\dagger\hat\alpha - 2\hat\alpha^\dagger\hat\alpha \\
&= \hat\beta(\hat\beta + \hat I) - 2(\hat\beta + \hat I) \\
&= \hat\beta^2 - \hat\beta - 2\hat I.
\end{split}
$$

Therefore

$$
(\hat\alpha^\dagger)^2\hat\alpha^2 = \hat\beta^2 - \hat\beta - 2\hat I + (\hat\beta + \hat I) = \hat\beta^2 - \hat I. \quad\checkmark
$$

**Feasible eigenvalues of $\hat\beta$.** Apply positivity to each operator in turn. Let $\beta$ be an eigenvalue of $\hat\beta$ (real, since $\hat\beta$ is Hermitian).

- $\hat\alpha^\dagger\hat\alpha = \hat\beta + \hat I \geq 0$ forces $\beta + 1 \geq 0$, i.e. $\beta \geq -1$.
- $\hat\alpha\hat\alpha^\dagger = \hat I - \hat\beta \geq 0$ forces $1 - \beta \geq 0$, i.e. $\beta \leq +1$.
- $(\hat\alpha^\dagger)^2\hat\alpha^2 = \hat\beta^2 - \hat I \geq 0$ forces $\beta^2 \geq 1$, i.e. $\beta \leq -1$ or $\beta \geq +1$.

The intersection of all three is $\beta = +1$ or $\beta = -1$. **Only two eigenvalues are feasible**: $\beta = \pm 1$. The algebra forces a *two-dimensional* representation.

(d) The relations $[\hat\beta, \hat\alpha] = -2\hat\alpha$ and $[\hat\beta, \hat\alpha^\dagger] = 2\hat\alpha^\dagger$ are exactly the standard ladder commutators $[\hat J_z, \hat J_\pm] = \pm\hbar\hat J_\pm$ with $\hbar = 1$, $\hat J_z = \hat\beta/2$, $\hat J_- = \hat\alpha$, $\hat J_+ = \hat\alpha^\dagger$. The values $\beta = \pm 1$ correspond to $m = \pm 1/2$ — exactly the **spin-1/2 representation**.

In the eigenbasis of $\hat\beta$, label the states $\vert+\rangle$ (with $\beta = +1$, i.e. $m = +1/2$) and $\vert-\rangle$ (with $\beta = -1$). Then $\hat\beta = \mathrm{diag}(1, -1) = \hat\sigma^z$. The ladder operators act as $\hat\alpha^\dagger\vert-\rangle = \vert+\rangle$ (raising) and $\hat\alpha^\dagger\vert+\rangle = 0$ (top), with coefficient $\sqrt{(\tfrac{1}{2} - m)(\tfrac{1}{2} + m + 1)}$ from Problem 4 — equal to $\sqrt{1} = 1$ for $m = -1/2$. Likewise $\hat\alpha\vert+\rangle = \vert-\rangle$, $\hat\alpha\vert-\rangle = 0$. So in the $\{\vert+\rangle, \vert-\rangle\}$ basis,

$$
\hat\alpha = \begin{pmatrix} 0 & 0 \\ 1 & 0\end{pmatrix} = \hat\sigma^-, \qquad \hat\alpha^\dagger = \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} = \hat\sigma^+, \qquad \hat\beta = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix} = \hat\sigma^z.
$$

The "quantum bootstrap" recovers the spin-1/2 Pauli operators **from the algebra alone** — no commutator-by-commutator construction, no requirement of a specific representation, just positivity bounds applied to algebraic relations. This is the operator-algebra version of the conformal-bootstrap approach in modern theoretical physics: spectrum and matrix elements pinned down entirely by symmetry constraints + positivity.
