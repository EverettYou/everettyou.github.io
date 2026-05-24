# 1.2.3 Measurement Operators
Worked solutions for the homework problems in the [1.2.3 Measurement Operators](../ch1_qubit/1-2-3-measurement-operators) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Spin-axis projector.** For a unit vector $\boldsymbol{n} = (n_x, n_y, n_z) \in \mathbb{R}^3$, the spin observable along $\boldsymbol{n}$ is $\boldsymbol{n}\cdot\hat{\boldsymbol\sigma}$ (1.1.3 Problem 7), with eigenvalues $\pm 1$.

(a) Use the universal Pauli projector pattern $\hat P_{O=m} = (\hat I + m\hat O)/2$ to write the two projectors $\hat P_{\boldsymbol{n},\pm}$ for the eigenvalue $\pm 1$ eigenspaces of $\boldsymbol{n}\cdot\hat{\boldsymbol\sigma}$.

(b) Verify idempotence $\hat P_{\boldsymbol{n},+}^2 = \hat P_{\boldsymbol{n},+}$ **algebraically**, using only $(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2 = \hat I$ from 1.1.3 Problem 7. (Do not compute $2\times 2$ matrix products.)

(c) Verify completeness $\hat P_{\boldsymbol{n},+} + \hat P_{\boldsymbol{n},-} = \hat I$.

(d) Compute the probability of obtaining $+1$ when measuring $\boldsymbol{n}\cdot\hat{\boldsymbol\sigma}$ on the state $\vert 0\rangle$. Express your answer in terms of $n_z$ and check the two limits $\boldsymbol{n} = \boldsymbol{e}_z$ and $\boldsymbol{n} = \boldsymbol{e}_x$.

**Solution.**

(a) Setting $\hat O = \boldsymbol{n}\cdot\hat{\boldsymbol\sigma}$ in the pattern,

$$
\hat P_{\boldsymbol{n},\pm} = \tfrac{1}{2}\bigl(\hat I \pm \boldsymbol{n}\cdot\hat{\boldsymbol\sigma}\bigr) = \tfrac{1}{2}\bigl(\hat I \pm (n_x\hat X + n_y\hat Y + n_z\hat Z)\bigr).
$$

(b) Expand the square:

$$
\hat P_{\boldsymbol{n},+}^2 = \tfrac{1}{4}(\hat I + \boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2 = \tfrac{1}{4}\bigl(\hat I + 2\boldsymbol{n}\cdot\hat{\boldsymbol\sigma} + (\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2\bigr).
$$

Substitute $(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2 = \hat I$ (which uses $\vert\boldsymbol{n}\vert = 1$):

$$
\hat P_{\boldsymbol{n},+}^2 = \tfrac{1}{4}\bigl(\hat I + 2\boldsymbol{n}\cdot\hat{\boldsymbol\sigma} + \hat I\bigr) = \tfrac{1}{4}(2\hat I + 2\boldsymbol{n}\cdot\hat{\boldsymbol\sigma}) = \tfrac{1}{2}(\hat I + \boldsymbol{n}\cdot\hat{\boldsymbol\sigma}) = \hat P_{\boldsymbol{n},+}. \quad\checkmark
$$

The unit-norm condition is exactly what makes idempotence hold — without it, the cross term would not collapse correctly.

(c) Adding the two,

$$
\hat P_{\boldsymbol{n},+} + \hat P_{\boldsymbol{n},-} = \tfrac{1}{2}(\hat I + \boldsymbol{n}\cdot\hat{\boldsymbol\sigma}) + \tfrac{1}{2}(\hat I - \boldsymbol{n}\cdot\hat{\boldsymbol\sigma}) = \hat I. \quad\checkmark
$$

(d) Born rule via projector form, with $\hat X\vert 0\rangle, \hat Y\vert 0\rangle$ orthogonal to $\vert 0\rangle$ (so $\langle 0\vert\hat X\vert 0\rangle = \langle 0\vert\hat Y\vert 0\rangle = 0$) and $\hat Z\vert 0\rangle = \vert 0\rangle$:

$$
\begin{split}
P(+1) &= \langle 0\vert\hat P_{\boldsymbol{n},+}\vert 0\rangle \\
&= \tfrac{1}{2}\langle 0\vert(\hat I + n_x\hat X + n_y\hat Y + n_z\hat Z)\vert 0\rangle \\
&= \tfrac{1}{2}(1 + n_z) = \frac{1 + n_z}{2}.
\end{split}
$$

*Limits.* $\boldsymbol{n} = \boldsymbol{e}_z$: $n_z = 1$, so $P(+1) = 1$ — deterministic, since $\vert 0\rangle$ is the $+1$ eigenstate of $\boldsymbol{e}_z\cdot\hat{\boldsymbol\sigma} = \hat Z$. $\boldsymbol{n} = \boldsymbol{e}_x$: $n_z = 0$, so $P(+1) = 1/2$ — a coin flip, since $\hat X$ is incompatible with $\hat Z$ and $\vert 0\rangle$ is an equal superposition of $\hat X$ eigenstates. Both limits match the Bloch picture: $P(+1) = (1 + \boldsymbol n_\psi\cdot\boldsymbol{n})/2$, with $\boldsymbol n_\psi = (0,0,1)$ being the Bloch vector of $\vert 0\rangle$.

<!-- ─── -->

**2. Born rule via projector formula.** A qubit is in the general Bloch state $\vert\psi\rangle = \cos(\theta/2)\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2)\vert 1\rangle$. Compute the $\hat X$ measurement probabilities using the **projector form** $P(m) = \langle\psi\vert\hat P_m\vert\psi\rangle$, rather than direct amplitude squaring.

(a) Write the projectors $\hat P_{X,\pm} = (\hat I \pm \hat X)/2$.

(b) Use linearity of expectation values and the lecture's Bloch-vector formula $\langle\psi\vert\hat X\vert\psi\rangle = \sin\theta\cos\varphi$ to obtain $P(\pm 1)$.

(c) Find the state that **maximises** $P(+1)$, and the state that **maximises** $P(-1)$. Identify both on the Bloch sphere.

**Solution.**

(a) $\hat P_{X,\pm} = (\hat I \pm \hat X)/2$.

(b) Using linearity,

$$
P(\pm 1) = \langle\psi\vert\hat P_{X,\pm}\vert\psi\rangle = \tfrac{1}{2}\bigl(\langle\psi\vert\hat I\vert\psi\rangle \pm \langle\psi\vert\hat X\vert\psi\rangle\bigr) = \tfrac{1}{2}\bigl(1 \pm \sin\theta\cos\varphi\bigr).
$$

This is the projector-form result, equivalent to the direct amplitude-squaring calculation that would give $P(+1) = \tfrac{1}{2}\vert\cos(\theta/2) + \mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2)\vert^2$ — but obtained in one line.

(c) Maximising $P(+1) = (1 + \sin\theta\cos\varphi)/2$ requires $\sin\theta\cos\varphi = +1$, i.e. $\sin\theta = 1$ and $\cos\varphi = 1$, so $\theta = \pi/2$ and $\varphi = 0$. The state is

$$
\vert\psi\rangle = \cos(\pi/4)\vert 0\rangle + \sin(\pi/4)\vert 1\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle + \vert 1\rangle) = \vert+\rangle,
$$

which gives $P(+1) = 1$ — the $\hat X = +1$ eigenstate. Bloch position: $(\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta) = (1, 0, 0)$, the $+\boldsymbol{e}_x$ direction.

Maximising $P(-1)$ requires $\sin\theta\cos\varphi = -1$, i.e. $\sin\theta = 1$ and $\cos\varphi = -1$, so $\theta = \pi/2$, $\varphi = \pi$. The state is $\vert\psi\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle - \vert 1\rangle) = \vert-\rangle$, with Bloch position $(-1, 0, 0)$ — the $-\boldsymbol{e}_x$ direction.

**Geometric reading.** Maximum $P(+1)$ for $\hat X$ measurement occurs at the Bloch vector that points directly *along* $+\boldsymbol{e}_x$ (the measurement's "yes" axis); maximum $P(-1)$ at the antipodal Bloch direction $-\boldsymbol{e}_x$. Probability is a linear function of the Bloch vector's projection onto the measurement axis, $P(\pm 1) = (1 \pm \boldsymbol{e}_x\cdot\boldsymbol n)/2$ — generalising the $P(0) = (1 + n_z)/2$ identity of 1.1.2 Problem 6.

<!-- ─── -->

**3. Spectral decomposition.** Recall from 1.1.3 Problem 5 the Hermitian operator

$$
\hat O = 2\hat I + 2\hat X + \hat Y + \hat Z = \begin{pmatrix} 3 & 2 - \mathrm{i} \\ 2 + \mathrm{i} & 1 \end{pmatrix},
$$

with Pauli coefficients $(a_0, a_x, a_y, a_z) = (2, 2, 1, 1)$.

(a) Using the parametrisation $\hat O = a_0\hat I + \boldsymbol a\cdot\hat{\boldsymbol\sigma}$ and the result of 1.1.3 Problem 5(c), state the eigenvalues of $\hat O$ in closed form. Compute their numerical values.

(b) Identify the unit vector $\boldsymbol{e}_a = \boldsymbol a/\vert\boldsymbol a\vert$ — the "Bloch axis" of $\hat O$ — and write the spectral projectors $\hat P_\pm$ onto the eigenstates.

(c) Verify the spectral decomposition $\hat O = E_+\hat P_+ + E_-\hat P_-$ by expanding the right side and recovering $\hat O = 2\hat I + 2\hat X + \hat Y + \hat Z$ algebraically.

(d) Use the spectral form to compute $\hat O^2$ in two ways: (i) by squaring the spectral expansion, and (ii) by direct $4\times 4$ … wait, $2\times 2$ matrix multiplication. Verify the two agree.

**Solution.**

(a) From 1.1.3 P5(c), the eigenvalues of $\hat O = a_0\hat I + \boldsymbol a\cdot\hat{\boldsymbol\sigma}$ are $E_\pm = a_0 \pm \vert\boldsymbol a\vert$. Here $\boldsymbol a = (2, 1, 1)$, so $\vert\boldsymbol a\vert = \sqrt{4 + 1 + 1} = \sqrt 6$, and

$$
E_\pm = 2 \pm \sqrt 6,
$$

numerically $E_+ \approx 4.449$ and $E_- \approx -0.449$.

(b) $\boldsymbol{e}_a = (2, 1, 1)/\sqrt 6$. The spectral projectors are

$$
\hat P_\pm = \tfrac{1}{2}(\hat I \pm \boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma}) = \tfrac{1}{2}\hat I \pm \frac{1}{2\sqrt 6}\bigl(2\hat X + \hat Y + \hat Z\bigr).
$$

(c) Plug into the spectral expansion:

$$
E_+\hat P_+ + E_-\hat P_- = (2 + \sqrt 6)\tfrac{1}{2}(\hat I + \boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma}) + (2 - \sqrt 6)\tfrac{1}{2}(\hat I - \boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma}).
$$

Collect $\hat I$ and $\boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma}$ coefficients separately:

$$
= \tfrac{1}{2}[(2+\sqrt 6) + (2-\sqrt 6)]\,\hat I + \tfrac{1}{2}[(2+\sqrt 6) - (2-\sqrt 6)]\,\boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma} = 2\hat I + \sqrt 6\,\boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma}.
$$

Substitute $\sqrt 6\,\boldsymbol{e}_a = (2, 1, 1) = \boldsymbol a$:

$$
\begin{split}
\sqrt 6\,\boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma} &= 2\hat X + \hat Y + \hat Z, \\
\Longrightarrow\;\; E_+\hat P_+ + E_-\hat P_- &= 2\hat I + 2\hat X + \hat Y + \hat Z = \hat O. \quad\checkmark
\end{split}
$$

(d) *Method 1 — squaring the spectral expansion.* Using orthogonality $\hat P_+\hat P_- = 0$ and idempotence,

$$
\hat O^2 = E_+^2\hat P_+ + E_-^2\hat P_- = (2 + \sqrt 6)^2\hat P_+ + (2 - \sqrt 6)^2\hat P_-.
$$

Expanding: $(2 \pm \sqrt 6)^2 = 4 \pm 4\sqrt 6 + 6 = 10 \pm 4\sqrt 6$. So

$$
\begin{split}
\hat O^2 &= (10 + 4\sqrt 6)\hat P_+ + (10 - 4\sqrt 6)\hat P_- \\
&= 10(\hat P_+ + \hat P_-) + 4\sqrt 6(\hat P_+ - \hat P_-) \\
&= 10\hat I + 4\sqrt 6\,\boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma} \\
&= 10\hat I + 4(2\hat X + \hat Y + \hat Z).
\end{split}
$$

Hence $\hat O^2 = 10\hat I + 8\hat X + 4\hat Y + 4\hat Z$.

*Method 2 — direct matrix squaring.*

$$
\hat O^2 = \begin{pmatrix} 3 & 2 - \mathrm{i} \\ 2 + \mathrm{i} & 1 \end{pmatrix}^2 = \begin{pmatrix} 9 + (2-\mathrm{i})(2+\mathrm{i}) & 3(2-\mathrm{i}) + (2-\mathrm{i}) \\ (2+\mathrm{i})(3+1) & (2+\mathrm{i})(2-\mathrm{i}) + 1 \end{pmatrix}.
$$

Compute: $(2-\mathrm{i})(2+\mathrm{i}) = 5$. So the $(1,1)$ entry is $9 + 5 = 14$. The $(1,2)$ entry: $3(2-\mathrm{i}) + (2-\mathrm{i}) = 4(2-\mathrm{i}) = 8 - 4\mathrm{i}$. The $(2,1)$ entry: $(2+\mathrm{i})\cdot 4 = 8 + 4\mathrm{i}$. The $(2,2)$ entry: $5 + 1 = 6$. So

$$
\hat O^2 = \begin{pmatrix} 14 & 8 - 4\mathrm{i} \\ 8 + 4\mathrm{i} & 6 \end{pmatrix}.
$$

Read off Pauli coefficients via $a_0 = \tfrac{1}{2}\operatorname{Tr}(\hat O^2)$ etc.: trace $= 20$, so $a_0 = 10$. Off-diagonal $\hat X$ contribution: $a_x = \tfrac{1}{2}(\operatorname{Tr}(\hat O^2\hat X)) = \tfrac{1}{2}((8 - 4\mathrm{i}) + (8 + 4\mathrm{i})) = 8$. Similarly $a_y = 4$ and $a_z = (14 - 6)/2 = 4$. So $\hat O^2 = 10\hat I + 8\hat X + 4\hat Y + 4\hat Z$, matching Method 1. ✓

The spectral form turned a $2\times 2$ matrix squaring into eigenvalue squaring — and the result is automatically in Pauli form, without the trace-extraction step. This is the general payoff: operator functions are *scalar* functions of eigenvalues, plus projectors.

<!-- ─── -->

**4. Two-qubit measurement.** Consider measuring $\hat{Z}$ on the equal-weight two-qubit superposition $\vert\Psi\rangle = \tfrac{1}{2}(\vert 00\rangle + \vert 01\rangle + \vert 10\rangle + \vert 11\rangle)$. The first qubit's $\hat{Z}$ — i.e. $\hat Z \otimes \hat I$ acting on the two-qubit space — has a degenerate $+1$ eigenspace.

(a) Write the projector $\hat P_{+1}$ onto the $+1$ eigenspace as an outer-product sum, and as an explicit $4\times 4$ matrix in the ordered basis $\{\vert 00\rangle, \vert 01\rangle, \vert 10\rangle, \vert 11\rangle\}$.

(b) Compute the measurement probability $P(+1) = \langle\Psi\vert\hat P_{+1}\vert\Psi\rangle$.

(c) Write the post-measurement state for outcome $+1$. Is it a single basis state, or a superposition? Factor it as a tensor product $\vert\text{first qubit}\rangle\otimes\vert\text{second qubit}\rangle$, and identify what the second qubit "remembers" about the original state.

**Solution.**

The observable $\hat Z\otimes\hat I$ has eigenvalues $\pm 1$, each with a **degenerate** two-dimensional eigenspace. The $+1$ eigenspace is spanned by $\{\vert 00\rangle, \vert 01\rangle\}$ (first qubit $\vert 0\rangle$), and the $-1$ eigenspace by $\{\vert 10\rangle, \vert 11\rangle\}$. The initial state factors as

$$
\vert\Psi\rangle = \tfrac{1}{2}(\vert 00\rangle + \vert 01\rangle + \vert 10\rangle + \vert 11\rangle) = \vert+\rangle\otimes\vert+\rangle,
$$

an unentangled product with each qubit in $\vert+\rangle$.

(a) The projector onto the $+1$ eigenspace sums the outer products of the two spanning states (equivalently, projects the first qubit onto $\vert 0\rangle$ and leaves the second untouched):

$$
\hat P_{+1} = \vert 0\rangle\langle 0\vert \otimes \hat I = \vert 00\rangle\langle 00\vert + \vert 01\rangle\langle 01\vert.
$$

As a $4\times 4$ matrix in the ordered basis,

$$
\hat P_{+1} \mapsto \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}.
$$

(b) $\hat P_{+1}$ acts component-by-component on $\vert\Psi\rangle$: it keeps the $\vert 00\rangle,\vert 01\rangle$ components (first qubit already $\vert 0\rangle$) and kills the $\vert 10\rangle,\vert 11\rangle$ components:

$$
\hat P_{+1}\vert\Psi\rangle = \tfrac{1}{2}(\vert 00\rangle + \vert 01\rangle).
$$

The probability is the squared norm,

$$
P(+1) = \langle\Psi\vert\hat P_{+1}\vert\Psi\rangle = \bigl\Vert\hat P_{+1}\vert\Psi\rangle\bigr\Vert^{2} = \left(\tfrac{1}{2}\right)^{2} + \left(\tfrac{1}{2}\right)^{2} = \tfrac{1}{2}.
$$

By the same calculation $P(-1) = 1/2$ — the two outcomes are equally likely, reflecting that the first qubit is in $\vert+\rangle$, a balanced superposition of $\vert 0\rangle$ and $\vert 1\rangle$. Unlike a state that already lies in one eigenspace, this measurement is genuinely informative.

(c) Normalising the projected vector,

$$
\begin{split}
\vert\Psi'\rangle
&= \frac{\hat P_{+1}\vert\Psi\rangle}{\sqrt{P(+1)}}
= \frac{(1/2)(\vert 00\rangle + \vert 01\rangle)}{\sqrt{1/2}}\\
&= \tfrac{1}{\sqrt 2}(\vert 00\rangle + \vert 01\rangle)
= \vert 0\rangle\otimes\tfrac{1}{\sqrt 2}(\vert 0\rangle + \vert 1\rangle)
= \vert 0\rangle\otimes\vert+\rangle.
\end{split}
$$

The post-measurement state is a **superposition** in the full two-qubit space (not a single basis state) — it spans the entire 2D $+1$ eigenspace — but it factors cleanly as a tensor product. The first qubit has collapsed to $\vert 0\rangle$ (the $+1$ eigenvector), while the second qubit emerges in $\vert+\rangle$ — exactly its component in the original $\vert+\rangle\otimes\vert+\rangle$. The measurement $\hat Z\otimes\hat I$ acts on the first-qubit factor only; *because the initial state was unentangled*, the second-qubit factor passes through unchanged.

**Defining feature of degenerate measurement.** A rank-$r$ projector leaves the post-state somewhere inside an $r$-dimensional eigenspace, but does **not** pick out a unique direction within it; the exact post-state vector depends on the initial state. Here the post-state is $\vert 0\rangle\otimes\vert+\rangle$. The second qubit emerges *unchanged* from its initial value $\vert+\rangle$ only because the input was a product state: nothing about the first-qubit projection could feed into the second-qubit factor. For an entangled input such as $(\vert 00\rangle+\vert 11\rangle)/\sqrt 2$, the same projector $\vert 0\rangle\langle 0\vert\otimes\hat I$ collapses the second qubit too (to $\vert 0\rangle$, via the correlation), even though it is the same rank-$2$ projector. Compare with non-degenerate measurement (Pauli on a single qubit): a rank-$1$ projector pins the post-state to a unique eigenvector (up to a global phase) regardless of the initial state.

<!-- ─── -->

**5. Sequential projectors and non-commutativity.** Two single-qubit projectors $\hat P_{Z,+} = \vert 0\rangle\langle 0\vert$ and $\hat P_{X,+} = (\hat I + \hat X)/2 = \vert+\rangle\langle+\vert$ each describe a "yes" outcome of one Pauli measurement.

(a) Write each projector as an explicit $2\times 2$ matrix.

(b) Compute both products $\hat P_{Z,+}\hat P_{X,+}$ and $\hat P_{X,+}\hat P_{Z,+}$ as matrices. Show that they are unequal.

(c) Apply each product to a generic state $\vert\psi\rangle = a\vert 0\rangle + b\vert 1\rangle$. Verify that the order of projector application changes the result.

(d) Compute $(\hat P_{Z,+}\hat P_{X,+})^2$ and show that it is **not** equal to $\hat P_{Z,+}\hat P_{X,+}$ — i.e., the product is not idempotent. Explain in one sentence why the product of two non-commuting projectors fails to be a projector, and what this means physically for sequential incompatible measurements.

**Solution.**

(a) $\hat P_{Z,+} \mapsto \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $\hat P_{X,+} \mapsto \tfrac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.

(b) Compute the two products:

$$
\hat P_{Z,+}\hat P_{X,+} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \cdot \tfrac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \tfrac{1}{2}\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix},
$$

$$
\hat P_{X,+}\hat P_{Z,+} = \tfrac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \cdot \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = \tfrac{1}{2}\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}.
$$

These are different matrices: $\hat P_{Z,+}\hat P_{X,+}$ has nonzero top row; $\hat P_{X,+}\hat P_{Z,+}$ has nonzero left column. So $\hat P_{Z,+}\hat P_{X,+} \neq \hat P_{X,+}\hat P_{Z,+}$ — projectors do not commute.

(c) Apply to $\vert\psi\rangle = a\vert 0\rangle + b\vert 1\rangle$:

$$
\begin{split}
\hat P_{X,+}\vert\psi\rangle &= \tfrac{a + b}{\sqrt 2}\vert+\rangle = \tfrac{a + b}{2}(\vert 0\rangle + \vert 1\rangle), \\
\hat P_{Z,+}\hat P_{X,+}\vert\psi\rangle &= \tfrac{a + b}{2}\vert 0\rangle,
\end{split}
$$

$$
\begin{split}
\hat P_{Z,+}\vert\psi\rangle &= a\vert 0\rangle, \\
\hat P_{X,+}\hat P_{Z,+}\vert\psi\rangle &= \tfrac{a}{2}(\vert 0\rangle + \vert 1\rangle) = \tfrac{a}{\sqrt 2}\vert+\rangle.
\end{split}
$$

The two outputs differ in *both* their magnitude (after-norm survival probability) and their direction (post-measurement state). Order matters.

(d) Compute the square of $\hat P_{Z,+}\hat P_{X,+}$:

$$
(\hat P_{Z,+}\hat P_{X,+})^2 = \tfrac{1}{4}\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = \tfrac{1}{4}\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = \tfrac{1}{2}\hat P_{Z,+}\hat P_{X,+}.
$$

This is **not** equal to $\hat P_{Z,+}\hat P_{X,+}$ — the square is half of the original, not equal. So the product is not idempotent, and therefore not a projector.

**Physical interpretation.** A projector represents the "filter" or "yes/no" outcome of a single measurement. The product of two non-commuting projectors represents the consecutive application of two such filters. After both filters have acted, the remaining amplitude is *smaller* (some of the state was discarded by each filter), and a third application of the same filter sequence would reduce the amplitude again — not leave it invariant. This is the algebraic counterpart of "incompatible measurements modify the state": the sequence $Z$-then-$X$ does not commute with $X$-then-$Z$, and neither sequence is a fixed-point operation. The non-idempotence reflects information actively being thrown away at each stage.

<!-- ─── -->

**6. Repeatability from idempotence.** Show that if measuring observable $\hat O$ on a state $\vert\psi\rangle$ yields outcome $m$ (with probability $p_m > 0$), then an immediately repeated measurement of $\hat O$ on the post-measurement state returns the same outcome $m$ with probability $1$.

(a) Write the post-measurement state $\vert\psi'\rangle$ in terms of the projector $\hat P_{O=m}$ and $\vert\psi\rangle$.

(b) Compute the probability $P(m'\,\vert\,\vert\psi'\rangle)$ of obtaining outcome $m'$ on the repeated measurement. Apply idempotence $\hat P_{O=m}^2 = \hat P_{O=m}$ and projector orthogonality $\hat P_{O=m}\hat P_{O=m'} = 0$ for $m'\neq m$.

(c) Conclude that $P(m\,\vert\,\vert\psi'\rangle) = 1$ and $P(m'\,\vert\,\vert\psi'\rangle) = 0$ for every $m' \neq m$.

(d) Explain in one sentence why this property — repeatability — would fail if the measurement operators were Hermitian but not idempotent (i.e., $\hat P^2 \neq \hat P$).

**Solution.**

(a) The projection rule of the measurement postulate:

$$
\vert\psi'\rangle = \frac{\hat P_{O=m}\vert\psi\rangle}{\sqrt{p_m}}, \qquad p_m = \langle\psi\vert\hat P_{O=m}\vert\psi\rangle.
$$

(b) For the repeated measurement, the probability of outcome $m'$ is

$$
P(m'\,\vert\,\vert\psi'\rangle) = \langle\psi'\vert\hat P_{O=m'}\vert\psi'\rangle = \frac{\langle\psi\vert\hat P_{O=m}\hat P_{O=m'}\hat P_{O=m}\vert\psi\rangle}{p_m},
$$

where the projector $\hat P_{O=m}^\dagger = \hat P_{O=m}$ (Hermitian) was used in moving from bra $\langle\psi'\vert$ back to $\langle\psi\vert$. The numerator contains the triple product $\hat P_{O=m}\hat P_{O=m'}\hat P_{O=m}$, which simplifies in two cases.

**Case $m' = m$:** apply idempotence twice,

$$
\hat P_{O=m}\hat P_{O=m}\hat P_{O=m} = \hat P_{O=m}^3 = \hat P_{O=m}^2 = \hat P_{O=m}.
$$

So the numerator equals $\langle\psi\vert\hat P_{O=m}\vert\psi\rangle = p_m$, giving $P(m\,\vert\,\vert\psi'\rangle) = p_m/p_m = 1$.

**Case $m' \neq m$:** projector orthogonality $\hat P_{O=m}\hat P_{O=m'} = 0$ (eigenstates of $\hat O$ with distinct eigenvalues are orthogonal) collapses the triple product:

$$
\hat P_{O=m}\hat P_{O=m'}\hat P_{O=m} = \hat P_{O=m}\cdot 0 = 0.
$$

So the numerator vanishes and $P(m'\,\vert\,\vert\psi'\rangle) = 0$.

(c) Combining, the repeated measurement returns $m$ with certainty: $P(m) = 1$, $P(m') = 0$ for every $m' \neq m$. This is the **repeatability** of measurement: once $\hat O$ has been measured, the system sits in an $\hat O$ eigenstate, and any further $\hat O$ measurement merely confirms that result.

(d) Without idempotence, $\hat P^2 \neq \hat P$, so the chain $\hat P_{O=m}^3 = \hat P_{O=m}$ used in part (b) would fail. The numerator $\langle\psi\vert\hat P_{O=m}^3\vert\psi\rangle$ would generally not equal $p_m$, breaking the equality $P(m\,\vert\,\vert\psi'\rangle) = 1$. Idempotence is the precise algebraic property that turns "projecting twice = projecting once," and that in turn is what makes "measurement reveals a value that is then stable under re-measurement" — a non-trivial empirical claim of quantum mechanics, anchored in a one-line operator identity.

<!-- ─── -->

**7. Operator functions via spectral decomposition.** The spectral decomposition extends to operator functions: for any function $f$,

$$
f(\hat O) = \sum_m f(m)\,\hat P_{O=m}.
$$

This makes operator powers, exponentials, and other functions easy to compute once the projectors are known.

(a) Apply this to compute $\hat Z^n$ for an integer $n$. Distinguish the cases $n$ even and $n$ odd.

(b) Apply it to the Hermitian operator $\hat H = \omega\hat X + \Delta\hat Z$ from 1.1.3 Problem 1, with eigenvalues $E_\pm = \pm\Omega = \pm\sqrt{\omega^2 + \Delta^2}$. Express $\hat H^n$ in spectral form, distinguishing even and odd $n$. Confirm that $\hat H^2 = \Omega^2\hat I$ (matching the result of 1.1.3 P1(c)).

(c) Compute the unitary operator $\hat U(\theta) = \mathrm{e}^{-\mathrm{i}\hat Z\theta}$ for real $\theta$. Write it as an explicit $2\times 2$ matrix in the $\{\vert 0\rangle, \vert 1\rangle\}$ basis, and verify directly that $\hat U^\dagger\hat U = \hat I$.

**Solution.**

(a) The spectral form of $\hat Z$: $\hat Z = (+1)\hat P_0 + (-1)\hat P_1 = \hat P_0 - \hat P_1$, with $\hat P_0 = \vert 0\rangle\langle 0\vert$ and $\hat P_1 = \vert 1\rangle\langle 1\vert$. So

$$
\hat Z^n = (+1)^n\hat P_0 + (-1)^n\hat P_1 = \hat P_0 + (-1)^n\hat P_1.
$$

For even $n$: $\hat Z^n = \hat P_0 + \hat P_1 = \hat I$ (completeness).

For odd $n$: $\hat Z^n = \hat P_0 - \hat P_1 = \hat Z$.

Equivalently and more memorably, $\hat Z^2 = \hat I$, which iterates to even powers being $\hat I$ and odd powers being $\hat Z$ — the same pattern as $(-1)^n$.

(b) From 1.1.3 P1, $\hat H = \Omega\hat P_+ + (-\Omega)\hat P_-$. Then

$$
\hat H^n = \Omega^n\hat P_+ + (-\Omega)^n\hat P_- = \Omega^n\bigl(\hat P_+ + (-1)^n\hat P_-\bigr).
$$

Even $n$: $\hat H^n = \Omega^n(\hat P_+ + \hat P_-) = \Omega^n\hat I = (\omega^2 + \Delta^2)^{n/2}\hat I$. Matches 1.1.3 P1(c) at $n=2$: $\hat H^2 = \Omega^2\hat I = (\omega^2 + \Delta^2)\hat I$. ✓

Odd $n$: $\hat H^n = \Omega^n(\hat P_+ - \hat P_-) = \Omega^{n-1}\,\Omega(\hat P_+ - \hat P_-) = \Omega^{n-1}\hat H$.

(c) For $f(x) = \mathrm{e}^{-\mathrm{i}x\theta}$,

$$
\hat U(\theta) = \mathrm{e}^{-\mathrm{i}\hat Z\theta} = \mathrm{e}^{-\mathrm{i}\theta}\hat P_0 + \mathrm{e}^{+\mathrm{i}\theta}\hat P_1.
$$

As a matrix in the $\{\vert 0\rangle, \vert 1\rangle\}$ basis,

$$
\hat U(\theta) = \mathrm{e}^{-\mathrm{i}\theta}\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \mathrm{e}^{+\mathrm{i}\theta}\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} \mathrm{e}^{-\mathrm{i}\theta} & 0 \\ 0 & \mathrm{e}^{+\mathrm{i}\theta} \end{pmatrix}.
$$

Unitarity check: $\hat U^\dagger = \begin{pmatrix} \mathrm{e}^{+\mathrm{i}\theta} & 0 \\ 0 & \mathrm{e}^{-\mathrm{i}\theta} \end{pmatrix}$, and

$$
\hat U^\dagger\hat U = \begin{pmatrix} \mathrm{e}^{+\mathrm{i}\theta}\mathrm{e}^{-\mathrm{i}\theta} & 0 \\ 0 & \mathrm{e}^{-\mathrm{i}\theta}\mathrm{e}^{+\mathrm{i}\theta} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \hat I. \quad\checkmark
$$

The same structure underlies the time-evolution operator $\mathrm{e}^{-\mathrm{i}\hat H t/\hbar}$ developed in §1.3: once the Hamiltonian's spectral form is known, time evolution reduces to scalar exponentials of eigenvalues, multiplying the corresponding projectors.
