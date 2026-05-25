# 1.2.2 Uncertainty and Incompatibility
Worked solutions for the homework problems in the [1.2.2 Uncertainty and Incompatibility](../ch1_qubit/1-2-2-uncertainty-and-incompatibility) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Most general operator commuting with Z.** Recall from 1.1.3 Problem 5 that every Hermitian operator on a qubit has the Pauli decomposition $\hat A = a_0\hat I + a_x\hat X + a_y\hat Y + a_z\hat Z$ with $a_0, a_x, a_y, a_z \in \mathbb{R}$.

(a) Compute $[\hat A, \hat Z]$ using the commutators $[\hat I, \hat Z] = 0$, $[\hat X, \hat Z] = -2\mathrm{i}\hat Y$, $[\hat Y, \hat Z] = 2\mathrm{i}\hat X$, $[\hat Z, \hat Z] = 0$.

(b) Set $[\hat A, \hat Z] = 0$ and find the constraints on $(a_0, a_x, a_y, a_z)$. Write the most general $\hat A$ that commutes with $\hat Z$.

(c) By the lecture theorem on commuting operators, $\hat A$ and $\hat Z$ share a complete simultaneous eigenbasis. Identify that basis directly from your answer to (b), and write down the eigenvalues of $\hat A$ on each basis state.

(d) The full Hermitian operator algebra on a qubit is $4$-dimensional (the Pauli basis). What fraction of it commutes with $\hat Z$? Explain in one sentence what this fraction means for the joint-measurability of qubit observables.

**Solution.**

(a) Using linearity of the commutator and the data given,

$$
[\hat A, \hat Z] = a_0[\hat I,\hat Z] + a_x[\hat X,\hat Z] + a_y[\hat Y,\hat Z] + a_z[\hat Z,\hat Z] = -2\mathrm{i}\,a_x\,\hat Y + 2\mathrm{i}\,a_y\,\hat X = 2\mathrm{i}\bigl(a_y\,\hat X - a_x\,\hat Y\bigr).
$$

(b) The operator $2\mathrm{i}(a_y\hat X - a_x\hat Y)$ vanishes iff its expansion coefficients in the linearly independent basis $\{\hat I,\hat X,\hat Y,\hat Z\}$ all vanish. So

$$
[\hat A, \hat Z] = 0 \;\Longleftrightarrow\; a_x = 0 \;\text{and}\; a_y = 0.
$$

The most general $\hat A$ commuting with $\hat Z$ is therefore

$$
\hat A = a_0\,\hat I + a_z\,\hat Z, \qquad a_0, a_z \in \mathbb{R}.
$$

(c) On the $\hat Z$ eigenbasis $\{\vert 0\rangle, \vert 1\rangle\}$, both $\hat I$ and $\hat Z$ are diagonal: $\hat I\vert m\rangle = \vert m\rangle$ and $\hat Z\vert m\rangle = (1 - 2m)\vert m\rangle$ for $m \in \{0,1\}$. Hence

$$
\hat A\vert 0\rangle = (a_0 + a_z)\,\vert 0\rangle, \qquad \hat A\vert 1\rangle = (a_0 - a_z)\,\vert 1\rangle.
$$

So $\vert 0\rangle$ and $\vert 1\rangle$ are the simultaneous eigenstates, with $\hat A$-eigenvalues $a_0 \pm a_z$. The lecture's "commuting operators share eigenbasis" theorem is realised concretely: diagonalising $\hat Z$ has already diagonalised the entire subalgebra $\mathbb R\hat I \oplus \mathbb R\hat Z$.

(d) The full Hermitian algebra has $4$ real degrees of freedom (Pauli coefficients $a_0, a_x, a_y, a_z$); the subalgebra commuting with $\hat Z$ has $2$ degrees of freedom (only $a_0, a_z$). So the commuting-with-$\hat Z$ subalgebra is **half** of the full algebra (a 2-dimensional subspace of a 4-dimensional one). Concretely: of the three Pauli "axes" $\hat X, \hat Y, \hat Z$, only one (the $\hat Z$ direction itself, plus $\hat I$) is compatible with $\hat Z$ — the other two ($\hat X$, $\hat Y$) are incompatible. In a qubit, **any direction except $\pm\boldsymbol{e}_z$** defines an observable that does not commute with $\hat Z$, and so cannot be measured jointly with $\hat Z$ at arbitrary precision.

<!-- ─── -->

**2. Robertson relation on a specific state.** For the state $\vert\psi\rangle = \vert+\rangle = \tfrac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle)$, the $+1$ eigenstate of $\hat X$:

(a) Compute $\langle\hat{X}\rangle$, $\langle\hat{Y}\rangle$, $\langle\hat{Z}\rangle$.

(b) Compute $\Delta\hat{X}$, $\Delta\hat{Y}$, $\Delta\hat{Z}$ using $(\hat\sigma^i)^2 = \hat I$ and the lecture's variance formula.

(c) Check the Robertson uncertainty relation for the pair $(\hat X, \hat Z)$: verify that $\Delta\hat{X}\cdot\Delta\hat{Z} \geq \tfrac{1}{2}\vert\langle[\hat{X}, \hat{Z}]\rangle\vert$. Is the inequality saturated?

**Solution.**

(a) Since $\vert+\rangle$ is the $+1$ eigenstate of $\hat X$, $\langle\hat X\rangle = +1$. For $\hat Y$: $\hat Y\vert+\rangle = \tfrac{1}{\sqrt 2}(\hat Y\vert 0\rangle + \hat Y\vert 1\rangle) = \tfrac{1}{\sqrt 2}(\mathrm{i}\vert 1\rangle - \mathrm{i}\vert 0\rangle) = -\mathrm{i}\vert-\rangle$, so $\langle\hat Y\rangle = \langle+\vert(-\mathrm{i}\vert-\rangle)\rangle = -\mathrm{i}\langle+\vert-\rangle = 0$. For $\hat Z$: $\hat Z\vert+\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle - \vert 1\rangle) = \vert-\rangle$, so $\langle\hat Z\rangle = \langle+\vert-\rangle = 0$. Summary: $\boldsymbol n_+ = (1, 0, 0)$.

(b) Every Pauli squares to $\hat I$, so $\langle(\hat\sigma^i)^2\rangle = 1$. Then

$$
\Delta\hat X = \sqrt{1 - 1^2} = 0, \qquad \Delta\hat Y = \sqrt{1 - 0^2} = 1, \qquad \Delta\hat Z = \sqrt{1 - 0^2} = 1.
$$

$\hat X$ is sharp (the state is its eigenstate); $\hat Y$ and $\hat Z$ are maximally uncertain.

(c) The Pauli commutator $[\hat X, \hat Z]$ — computed in this problem set's later problems but also implied by the cyclic relation $[\hat X, \hat Y] = 2\mathrm{i}\hat Z$ — is $[\hat X, \hat Z] = -2\mathrm{i}\hat Y$. The bound is

$$
\tfrac{1}{2}\bigl\vert\langle[\hat X,\hat Z]\rangle\bigr\vert = \tfrac{1}{2}\bigl\vert\langle{-2\mathrm{i}}\hat Y\rangle\bigr\vert = \vert\langle\hat Y\rangle\vert = 0.
$$

The Robertson relation reads

$$
\Delta\hat X\cdot\Delta\hat Z = 0\cdot 1 = 0 \;\geq\; 0. \quad\checkmark
$$

The inequality is **saturated** (both sides equal $0$). Two observations: first, the lower bound itself is state-dependent and vanishes here because $\langle\hat Y\rangle = 0$ — saturation is consistent with the bound being zero on $\vert+\rangle$. Second, the saturation does *not* mean the uncertainty principle is doing no work: it correctly reports that sharp $\hat X$ is bought with maximal $\hat Z$ uncertainty (Δ$\hat Z = 1$), and the cost is paid through the $\hat Y$ axis going to zero expectation.

<!-- ─── -->

**3. Spin commutator along arbitrary axes.** For unit vectors $\boldsymbol{n}_1, \boldsymbol{n}_2 \in \mathbb{R}^3$, define the spin observables along those axes,

$$
\hat A = \boldsymbol{n}_1\cdot\hat{\boldsymbol\sigma}, \qquad \hat B = \boldsymbol{n}_2\cdot\hat{\boldsymbol\sigma}.
$$

(a) Using the Pauli multiplication law $\hat\sigma^i\hat\sigma^j = \delta_{ij}\hat I + \mathrm{i}\epsilon_{ijk}\hat\sigma^k$ (1.1.3), compute $[\hat A, \hat B]$. Show that

$$
[\hat A, \hat B] = 2\mathrm{i}\,(\boldsymbol{n}_1\times\boldsymbol{n}_2)\cdot\hat{\boldsymbol\sigma}.
$$

(b) State the geometric condition on $\boldsymbol{n}_1, \boldsymbol{n}_2$ under which $\hat A$ and $\hat B$ commute. Interpret on the Bloch sphere.

(c) Apply the Robertson uncertainty relation: for a state with Bloch vector $\boldsymbol n$,

$$
\Delta\hat A\cdot\Delta\hat B \geq \bigl\vert(\boldsymbol{n}_1\times\boldsymbol{n}_2)\cdot\boldsymbol n\bigr\vert.
$$

For what configurations of $\boldsymbol{n}_1, \boldsymbol{n}_2, \boldsymbol n$ does this lower bound vanish? Give two geometrically distinct scenarios.

**Solution.**

(a) Expand and use the Pauli multiplication law. Write $\hat A = \sum_i n_1^i\hat\sigma^i$ and $\hat B = \sum_j n_2^j\hat\sigma^j$, then

$$
\hat A\hat B = \sum_{i,j} n_1^i n_2^j\,\hat\sigma^i\hat\sigma^j = \sum_{i,j} n_1^i n_2^j\bigl(\delta_{ij}\hat I + \mathrm{i}\epsilon_{ijk}\hat\sigma^k\bigr).
$$

The commutator picks out the antisymmetric part:

$$
\begin{split}
[\hat A,\hat B] &= \hat A\hat B - \hat B\hat A \\
&= 2\mathrm{i}\,\epsilon_{ijk}\,n_1^i\,n_2^j\,\hat\sigma^k \\
&= 2\mathrm{i}\,(\boldsymbol{n}_1\times\boldsymbol{n}_2)^k\,\hat\sigma^k \\
&= 2\mathrm{i}\,(\boldsymbol{n}_1\times\boldsymbol{n}_2)\cdot\hat{\boldsymbol\sigma}.
\end{split}
$$

The symmetric ($\delta_{ij}\hat I$) part cancels between $\hat A\hat B$ and $\hat B\hat A$ — only the cross-product survives.

(b) The commutator vanishes iff $\boldsymbol{n}_1\times\boldsymbol{n}_2 = 0$, i.e. iff $\boldsymbol{n}_1$ and $\boldsymbol{n}_2$ are **parallel or antiparallel**. Geometrically: two spin observables commute iff their measurement axes point along the same line on the Bloch sphere (the same or diametrically opposite directions). Any other configuration — including perpendicular axes (e.g. $\boldsymbol{n}_1 = \boldsymbol{e}_z$ vs $\boldsymbol{n}_2 = \boldsymbol{e}_x$) — gives non-commuting operators.

(c) Using $\langle\hat\sigma^k\rangle = n_k$ from the Bloch parametrization,

$$
\tfrac{1}{2}\bigl\vert\langle[\hat A,\hat B]\rangle\bigr\vert = \bigl\vert\langle(\boldsymbol{n}_1\times\boldsymbol{n}_2)\cdot\hat{\boldsymbol\sigma}\rangle\bigr\vert = \bigl\vert(\boldsymbol{n}_1\times\boldsymbol{n}_2)\cdot\boldsymbol n\bigr\vert.
$$

This vanishes in two distinct geometric scenarios:

- **Parallel axes** ($\boldsymbol{n}_1\parallel\boldsymbol{n}_2$). Then $\boldsymbol{n}_1\times\boldsymbol{n}_2 = 0$, the operators commute, and the bound is identically zero on every state. This is the algebraic origin of compatibility.

- **State in the plane of the two axes** ($\boldsymbol n \in \mathrm{span}(\boldsymbol{n}_1, \boldsymbol{n}_2)$). Then $\boldsymbol n$ is perpendicular to $\boldsymbol{n}_1\times\boldsymbol{n}_2$, so the dot product vanishes — the bound is zero on *that particular state*, even though $\hat A$ and $\hat B$ themselves do not commute. Example: $\boldsymbol{n}_1 = \boldsymbol{e}_z$, $\boldsymbol{n}_2 = \boldsymbol{e}_x$, $\boldsymbol n = \pm\boldsymbol{e}_z$ or $\pm\boldsymbol{e}_x$ (the four "axial" Bloch points), all in the $xz$-plane.

The first scenario reflects an algebraic compatibility; the second reflects an *accidental* state-dependent saturation. The same Robertson bound — distinguishing them tracks how the lower bound varies between identically-zero (commuting case) and state-dependent zeros (non-commuting case).

<!-- ─── -->

**4. Total Pauli uncertainty for a pure qubit.** Show that for any pure qubit state with Bloch vector $\boldsymbol n$ (so $\vert\boldsymbol n\vert = 1$),

$$
(\Delta\hat X)^2 + (\Delta\hat Y)^2 + (\Delta\hat Z)^2 = 2.
$$

(a) For each Pauli component, compute $(\Delta\hat\sigma^i)^2$ using $\langle\hat\sigma^i\rangle = n_i$ and $\langle(\hat\sigma^i)^2\rangle = 1$.

(b) Sum the three variances and apply $\vert\boldsymbol n\vert^2 = 1$ to obtain the identity.

(c) Interpret physically: a pure qubit state cannot have all three Pauli observables simultaneously sharp — the total uncertainty budget is *exactly* $2$, independent of the state's location on the Bloch sphere. For each state, identify the unique direction in which the uncertainty is zero.

(d) Verify the identity explicitly on $\vert+\rangle$: compute each $(\Delta\hat\sigma^i)^2$ and confirm the sum equals $2$. Which observable is sharp, and how is the total uncertainty distributed among the other two?

**Solution.**

(a) The variance of any Pauli observable on a state with Bloch vector $\boldsymbol n$ is

$$
(\Delta\hat\sigma^i)^2 = \langle(\hat\sigma^i)^2\rangle - \langle\hat\sigma^i\rangle^2 = 1 - n_i^2,
$$

using $(\hat\sigma^i)^2 = \hat I$ (so $\langle(\hat\sigma^i)^2\rangle = 1$) and $\langle\hat\sigma^i\rangle = n_i$ (the Bloch vector component, from 1.1.2 / 1.1.3).

(b) Sum over the three components:

$$
\begin{split}
(\Delta\hat X)^2 + (\Delta\hat Y)^2 + (\Delta\hat Z)^2 &= (1 - n_x^2) + (1 - n_y^2) + (1 - n_z^2) \\
&= 3 - (n_x^2 + n_y^2 + n_z^2) \\
&= 3 - 1 = 2,
\end{split}
$$

using $\vert\boldsymbol n\vert^2 = 1$ for pure states (1.1.2 Problem 4).

(c) The total Pauli uncertainty $\sum_i (\Delta\hat\sigma^i)^2 = 2$ is **state-independent**: every pure qubit state carries the same "uncertainty budget" of $2$, distributed across the three Pauli axes. A state has zero uncertainty along its own Bloch direction $\boldsymbol{n}$ — because $n_i^2 = 1$ when the measurement axis aligns with $\boldsymbol n$, contributing $0$ to the variance sum. Along the perpendicular axes, the variance is positive and the total carries the remaining $2$. **A pure state is sharp for exactly one observable (the one whose axis is its Bloch vector); all other directions share the budget of $2$.**

(d) For $\vert+\rangle$, $\boldsymbol n = (1, 0, 0)$. The variances are

$$
(\Delta\hat X)^2 = 1 - 1^2 = 0, \qquad (\Delta\hat Y)^2 = 1 - 0^2 = 1, \qquad (\Delta\hat Z)^2 = 1 - 0^2 = 1.
$$

Sum: $0 + 1 + 1 = 2$. ✓

$\hat X$ is sharp ($\Delta\hat X = 0$, as the lecture warned: $\vert+\rangle$ is its eigenstate). The total uncertainty $2$ is split equally between $\hat Y$ and $\hat Z$ — both perpendicular to the Bloch vector — with each contributing $1$. This is the qubit analog of "you can't be sharp about everything at once," now expressed as a quantitative budget conservation rather than just an inequality.

<!-- ─── -->

**5. Sharp observable does not violate Heisenberg.** Explain why the Heisenberg/Robertson uncertainty relation does **not** prevent measuring $\hat Z$ with zero uncertainty on the eigenstate $\vert 0\rangle$. Does the deterministic outcome violate the relation? Demonstrate by computing both sides of $\Delta\hat Z\cdot\Delta\hat X \geq \tfrac{1}{2}\vert\langle[\hat Z,\hat X]\rangle\vert$ on $\vert 0\rangle$.

**Solution.**

The state $\vert 0\rangle$ is an eigenstate of $\hat Z$ with eigenvalue $+1$. Every measurement of $\hat Z$ on a freshly prepared copy of $\vert 0\rangle$ returns $+1$, so the distribution has no spread:

$$
\langle\hat Z\rangle = 1, \quad \langle\hat Z^2\rangle = 1, \quad \Delta\hat Z = 0.
$$

Nothing in the uncertainty principle forbids this. The **Robertson inequality** constrains a *pair* of observables — it bounds the *product* of two uncertainties — and never the uncertainty of a single observable in isolation. A state can always be made sharp for one chosen observable (its own eigenstate); the relation only says that doing so *forces uncertainty into the incompatible partner*.

Concretely on $\vert 0\rangle$: with $[\hat Z, \hat X] = 2\mathrm{i}\hat Y$ (cyclic permutation of the lecture's relation),

$$
\tfrac{1}{2}\bigl\vert\langle[\hat Z,\hat X]\rangle\bigr\vert = \tfrac{1}{2}\bigl\vert\langle 0\vert 2\mathrm{i}\hat Y\vert 0\rangle\bigr\vert = \vert\langle 0\vert\hat Y\vert 0\rangle\vert = 0,
$$

since $\hat Y$ is off-diagonal in the $\hat Z$ basis ($\hat Y\vert 0\rangle = \mathrm{i}\vert 1\rangle$, orthogonal to $\vert 0\rangle$). The Robertson inequality reads

$$
\Delta\hat Z\cdot\Delta\hat X = 0\cdot 1 = 0 \;\geq\; 0. \quad\checkmark
$$

(The partner $\Delta\hat X = 1$ because $\vert 0\rangle$ has $\boldsymbol n = (0, 0, 1)$, giving $\langle\hat X\rangle = 0$ and $(\Delta\hat X)^2 = 1$ — the maximum possible.) Two lessons:

1. The lower bound is **state-dependent**: when $\langle\hat Y\rangle = 0$ on the chosen state, the bound collapses to zero and imposes no constraint at all.

2. The price for sharp $\hat Z$ is paid in $\hat X$: $\vert 0\rangle$ has *maximal* $\hat X$ uncertainty. The total-uncertainty identity of Problem 4 says $(\Delta\hat X)^2 + (\Delta\hat Y)^2 + (\Delta\hat Z)^2 = 2$ on every pure state, so squeezing $\Delta\hat Z$ to $0$ pushes the budget entirely into the other two — consistent with $\Delta\hat X = \Delta\hat Y = 1$.

Sharp $\hat Z$ does not break Heisenberg; it just demonstrates that the principle is about the *cost* of sharpness in one direction, paid in the other.

<!-- ─── -->

**6. Saturation and maximum of the Robertson bound.** The Robertson relation for the pair $(\hat X, \hat Z)$ reads $\Delta\hat X\cdot\Delta\hat Z \geq \vert\langle\hat Y\rangle\vert$ (using $[\hat X,\hat Z] = -2\mathrm{i}\hat Y$).

(a) Over all pure qubit states (Bloch vector $\boldsymbol n$ with $\vert\boldsymbol n\vert = 1$), find the state that maximises the lower bound $\vert\langle\hat Y\rangle\vert$. Compute the maximum value.

(b) Using the Bloch parametrization with $\Delta\hat X = \sqrt{1 - n_x^2}$ and $\Delta\hat Z = \sqrt{1 - n_z^2}$, find the condition on the Bloch vector for which the Robertson inequality is **saturated** (equality $\Delta\hat X\cdot\Delta\hat Z = \vert\langle\hat Y\rangle\vert$). Identify the states geometrically.

(c) Find the pure states that both (i) maximise the lower bound from (a) AND (ii) saturate the inequality from (b). Identify them on the Bloch sphere. What spin direction is sharp for these states?

**Solution.**

(a) The lower bound is $\vert\langle\hat Y\rangle\vert = \vert n_y\vert$, maximised over pure states with the constraint $n_x^2 + n_y^2 + n_z^2 = 1$. The constraint allows $\vert n_y\vert \le 1$, with equality at $\boldsymbol n = (0, \pm 1, 0)$. The maximum value of the bound is $\vert n_y\vert_{\max} = 1$, achieved by the two states

$$
\boldsymbol n = (0, 1, 0): \vert\mathrm{i}\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle + \mathrm{i}\vert 1\rangle), \qquad \boldsymbol n = (0, -1, 0): \vert\bar{\mathrm{i}}\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle - \mathrm{i}\vert 1\rangle),
$$

the $\hat Y$ eigenstates. So the $\hat Y$ eigenstates make $\hat X$ and $\hat Z$ "most incompatible."

(b) Saturation requires $\Delta\hat X\cdot\Delta\hat Z = \vert n_y\vert$, i.e.

$$
\sqrt{(1 - n_x^2)(1 - n_z^2)} = \vert n_y\vert.
$$

Squaring both sides and using $n_y^2 = 1 - n_x^2 - n_z^2$ (pure-state constraint),

$$
(1 - n_x^2)(1 - n_z^2) = 1 - n_x^2 - n_z^2.
$$

Expanding the left side and simplifying:

$$
\begin{split}
1 - n_x^2 - n_z^2 + n_x^2 n_z^2 &= 1 - n_x^2 - n_z^2 \\
\Longrightarrow\;\; n_x^2\,n_z^2 &= 0.
\end{split}
$$

So saturation occurs iff $n_x = 0$ **or** $n_z = 0$. Geometrically: the Bloch vector lies in the $yz$-plane (the "$\boldsymbol{e}_x = 0$" great circle) or in the $xy$-plane (the "$\boldsymbol{e}_z = 0$" great circle). Equivalently, the state is in the *plane spanned by $\boldsymbol{e}_y$ and one of* $\boldsymbol{e}_x, \boldsymbol{e}_z$.

(c) Combining (a) and (b): maximum requires $\boldsymbol n = (0, \pm 1, 0)$. Both maximum states already satisfy $n_x = 0$ *and* $n_z = 0$, so they are in *both* of the saturation planes — they sit at the intersection. So the $\hat Y$ eigenstates $\vert\mathrm{i}\rangle$ and $\vert\bar{\mathrm{i}}\rangle$ are the unique pure states that both maximise the lower bound *and* saturate the inequality. On these states:

$$
\Delta\hat X = \Delta\hat Z = 1, \qquad \Delta\hat X\cdot\Delta\hat Z = 1, \qquad \vert\langle\hat Y\rangle\vert = 1.
$$

The sharp direction is $\boldsymbol{e}_y$: these states are eigenstates of $\hat Y$ with $\Delta\hat Y = 0$. The total-uncertainty identity from Problem 4 confirms it: $(\Delta\hat X)^2 + (\Delta\hat Y)^2 + (\Delta\hat Z)^2 = 1 + 0 + 1 = 2$. The Bloch vector points purely along $\boldsymbol{e}_y$, making $\hat X$ and $\hat Z$ — the two directions perpendicular to $\boldsymbol{e}_y$ — simultaneously maximally uncertain and maximally incompatible.

<!-- ─── -->

**7. Maximising the Z-uncertainty.** A qubit is prepared in $\vert\psi\rangle = \cos\alpha\vert 0\rangle + \sin\alpha\vert 1\rangle$ (real $\alpha$). Find the value(s) of $\alpha$ that maximise $\Delta\hat Z$. Identify the maximising states on the Bloch sphere and interpret the result via Problem 4's total-uncertainty identity.

**Solution.**

The amplitudes $c_0 = \cos\alpha$, $c_1 = \sin\alpha$ are real, so $\vert c_0\vert^2 + \vert c_1\vert^2 = 1$ for every real $\alpha$. A measurement of $\hat Z$ returns $+1$ with probability $\cos^2\alpha$ and $-1$ with probability $\sin^2\alpha$, so

$$
\langle\hat Z\rangle = \cos^2\alpha - \sin^2\alpha = \cos 2\alpha, \qquad \langle\hat Z^2\rangle = 1\text{ (since }\hat Z^2=\hat I\text{)}.
$$

The variance is

$$
(\Delta\hat Z)^2 = \langle\hat Z^2\rangle - \langle\hat Z\rangle^2 = 1 - \cos^2 2\alpha = \sin^2 2\alpha, \qquad \Delta\hat Z = \vert\sin 2\alpha\vert.
$$

The maximum is $1$, achieved when $\vert\sin 2\alpha\vert = 1$, i.e. $\alpha = \pi/4 + n\pi/2$ for $n\in\mathbb Z$. Within $\alpha\in[0,\pi)$, the two distinct solutions are $\alpha = \pi/4$ and $\alpha = 3\pi/4$, corresponding to

$$
\vert\psi\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle + \vert 1\rangle) = \vert+\rangle \qquad\text{and}\qquad \vert\psi\rangle = \tfrac{1}{\sqrt 2}(-\vert 0\rangle + \vert 1\rangle) \equiv \vert-\rangle\ \text{(up to global sign)}.
$$

So $\Delta\hat Z$ is maximised exactly on the $\hat X$ eigenstates. Geometrically, these sit at the equator of the Bloch sphere along $\pm\boldsymbol{e}_x$ — perpendicular to $\boldsymbol{e}_z$ — so they have $n_z = 0$ and the $\hat Z$ outcomes are maximally split $50$/$50$.

**Connection to Problem 4.** The total-uncertainty identity $(\Delta\hat X)^2 + (\Delta\hat Y)^2 + (\Delta\hat Z)^2 = 2$ means that pushing $(\Delta\hat Z)^2$ to $1$ — its maximum on any single component — leaves only $1$ unit of variance for $(\Delta\hat X)^2 + (\Delta\hat Y)^2$. The maximising states are $\hat X$ eigenstates, which have $(\Delta\hat X)^2 = 0$ and $(\Delta\hat Y)^2 = 1$; the budget consistency checks out: $0 + 1 + 1 = 2$.

<!-- ─── -->

**8. Minimum of the X-Z uncertainty product.** Apply the Robertson uncertainty relation to the pair $(\hat X, \hat Z)$. Over all pure qubit states, find the minimum value of $\Delta\hat X\cdot\Delta\hat Z$ and identify the minimising states. Verify that the Robertson inequality is consistent with this minimum.

**Solution.**

Using the Bloch parametrization with $\langle\hat\sigma^i\rangle = n_i$ and $(\hat\sigma^i)^2 = \hat I$,

$$
\Delta\hat X = \sqrt{1 - n_x^2}, \qquad \Delta\hat Z = \sqrt{1 - n_z^2}, \qquad \Delta\hat X\cdot\Delta\hat Z = \sqrt{(1 - n_x^2)(1 - n_z^2)}.
$$

Both factors are non-negative, so the product is non-negative; its smallest value is $0$, achieved when either factor vanishes:

- $n_x^2 = 1$: the state is an $\hat X$ eigenstate, $\vert\pm\rangle$. Here $\Delta\hat X = 0$.
- $n_z^2 = 1$: the state is a $\hat Z$ eigenstate, $\vert 0\rangle$ or $\vert 1\rangle$. Here $\Delta\hat Z = 0$.

So $\bigl(\Delta\hat X\cdot\Delta\hat Z\bigr)_{\min} = 0$, achieved by any eigenstate of $\hat X$ *or* of $\hat Z$.

**Consistency with the Robertson bound.** On these minimising states, the Bloch vector lies in the $xz$-plane ($n_y = 0$), so the lower bound $\vert\langle\hat Y\rangle\vert = \vert n_y\vert = 0$ as well. The relation reads $0 \geq 0$ — satisfied with equality. The Heisenberg bound for an incompatible pair is **not a fixed positive number**: it is state-dependent and can drop to zero (along the great circle perpendicular to the commutator's axis), allowing the uncertainty product itself to reach zero on those special states. The minimising states are exactly the ones for which the bound is uninformative.

A useful complement: the *maximum* of $\Delta\hat X\cdot\Delta\hat Z$ over pure states occurs at $\boldsymbol n = (0, \pm 1, 0)$ — the $\hat Y$ eigenstates (Problem 6) — where the product equals $1$ and saturates the maximally incompatible Robertson bound. So $\Delta\hat X\cdot\Delta\hat Z$ ranges over $[0, 1]$ as the Bloch vector sweeps the unit sphere, with the extrema picking out the eigenstates of $\hat X$/$\hat Z$ (minimum) and $\hat Y$ (maximum).
