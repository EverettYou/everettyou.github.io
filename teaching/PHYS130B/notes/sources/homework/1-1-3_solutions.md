# 1.1.3 Hermitian Operators
Worked solutions for the homework problems in the [1.1.3 Hermitian Operators](../ch1_qubit/1-1-3-hermitian-operators) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Spectral decomposition of a two-level Hamiltonian.** Consider the Hermitian operator $\hat{H} = \omega\,\hat{X} + \Delta\,\hat{Z}$, with $\omega,\Delta\in\mathbb{R}$. This represents a generic two-level system in which $\hat Z$ encodes an energy splitting $2\Delta$ between $\vert 0\rangle$ and $\vert 1\rangle$ and $\hat X$ provides a coupling of strength $\omega$ between them.

(a) Verify that $\hat H$ is Hermitian, and write its matrix in the $\{\vert 0\rangle,\vert 1\rangle\}$ basis.

(b) Find the eigenvalues $E_\pm$ and the corresponding eigenstates $\vert E_\pm\rangle$. Express the result using the mixing angle $\theta_0$ defined by $\tan\theta_0 = \omega/\Delta$ (with $\theta_0\in[0,\pi]$).

(c) Write the spectral decomposition $\hat H = E_+\vert E_+\rangle\langle E_+\vert + E_-\vert E_-\rangle\langle E_-\vert$ and use it to compute $\hat H^2$ without doing any matrix multiplication. Show that $\hat H^2 = (\omega^2+\Delta^2)\,\hat I$.

(d) Use the spectral form to write an integer power $\hat H^n$ in closed form for any $n\ge 1$.

**Solution.**

(a) The matrix is

$$
\hat H = \omega\begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} + \Delta\begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix} = \begin{pmatrix} \Delta & \omega \\ \omega & -\Delta\end{pmatrix}.
$$

The diagonal entries $\pm\Delta$ are real, and the off-diagonal entries are an equal pair $\omega = \omega^*$ (since $\omega$ is real). So $\hat H = \hat H^\dagger$.

(b) Eigenvalues come from $\det(\hat H - E\hat I) = 0$:

$$
(\Delta - E)(-\Delta - E) - \omega^2 = E^2 - \Delta^2 - \omega^2 = 0 \quad\Longrightarrow\quad E_\pm = \pm\sqrt{\omega^2 + \Delta^2}.
$$

For the eigenstates, set $\sqrt{\omega^2+\Delta^2} = \Omega$ and $\tan\theta_0 = \omega/\Delta$ so that $\cos\theta_0 = \Delta/\Omega$ and $\sin\theta_0 = \omega/\Omega$. Solving $(\hat H - E_+\hat I)v = 0$,

$$
\begin{pmatrix} \Delta - \Omega & \omega \\ \omega & -\Delta - \Omega\end{pmatrix}\begin{pmatrix} a\\ b\end{pmatrix} = 0 \;\Longrightarrow\; \frac{b}{a} = \frac{\Omega - \Delta}{\omega}.
$$

Apply half-angle identities: $\Omega - \Delta = \Omega(1 - \cos\theta_0) = 2\Omega\sin^2(\theta_0/2)$ and $\omega = \Omega\sin\theta_0 = 2\Omega\sin(\theta_0/2)\cos(\theta_0/2)$, giving $b/a = \tan(\theta_0/2)$. Choosing $a = \cos(\theta_0/2)$,

$$
\vert E_+\rangle = \cos(\theta_0/2)\,\vert 0\rangle + \sin(\theta_0/2)\,\vert 1\rangle.
$$

The orthogonal $\vert E_-\rangle$ follows from the antipodal-on-Bloch result of 1.1.2 Problem 5:

$$
\vert E_-\rangle = \sin(\theta_0/2)\,\vert 0\rangle - \cos(\theta_0/2)\,\vert 1\rangle.
$$

Both are real-amplitude states (no relative phase), as expected since $\hat H$ has no $\hat Y$ component.

(c) The spectral form is

$$
\hat H = \Omega\,\vert E_+\rangle\langle E_+\vert + (-\Omega)\,\vert E_-\rangle\langle E_-\vert.
$$

Squaring uses the orthogonality $\langle E_+\vert E_-\rangle = 0$ and idempotence of each projector:

$$
\hat H^2 = \Omega^2\,\vert E_+\rangle\langle E_+\vert + \Omega^2\,\vert E_-\rangle\langle E_-\vert = \Omega^2\bigl(\vert E_+\rangle\langle E_+\vert + \vert E_-\rangle\langle E_-\vert\bigr) = \Omega^2\,\hat I,
$$

using completeness $\vert E_+\rangle\langle E_+\vert + \vert E_-\rangle\langle E_-\vert = \hat I$. So $\hat H^2 = (\omega^2 + \Delta^2)\hat I$. **Crucially, no $2\times 2$ matrix multiplication was needed** — the spectral form turns operator powers into scalar powers of eigenvalues.

(d) For any integer $n\ge 1$,

$$
\hat H^n = (+\Omega)^n\,\vert E_+\rangle\langle E_+\vert + (-\Omega)^n\,\vert E_-\rangle\langle E_-\vert.
$$

The same spectral structure extends to *any* function of $\hat H$: $f(\hat H) = f(\Omega)\vert E_+\rangle\langle E_+\vert + f(-\Omega)\vert E_-\rangle\langle E_-\vert$. This is the operator-function machinery that powers unitary time evolution $\mathrm{e}^{-\mathrm{i}\hat H t/\hbar}$ — developed in Section 1.3.

<!-- ─── -->

**2. Hermitian and anti-Hermitian decomposition.** Any operator $\hat A$ on a Hilbert space admits a unique decomposition $\hat A = \hat H + \mathrm{i}\hat K$ with both $\hat H$ and $\hat K$ Hermitian.

(a) Show that $\hat H = \tfrac{1}{2}(\hat A + \hat A^\dagger)$ and $\hat K = \tfrac{1}{2\mathrm{i}}(\hat A - \hat A^\dagger)$ are both Hermitian, and that $\hat A = \hat H + \mathrm{i}\hat K$.

(b) Apply to $\hat A = \begin{pmatrix} 1 & \mathrm{i} \\ \mathrm{i} & 1\end{pmatrix}$. Compute $\hat H$ and $\hat K$ explicitly, and express each in terms of the Pauli operators $\hat I, \hat X, \hat Y, \hat Z$.

(c) Draw the analogy with the complex-number decomposition $z = x + \mathrm{i}y$: which operator plays the role of the real part of $z$, and which the imaginary part? Explain in one sentence why this analogy makes the Hermitian operators the natural "real" subspace of the operator algebra.

**Solution.**

(a) **Hermiticity of $\hat H$.** Using $(\hat A^\dagger)^\dagger = \hat A$:

$$
\hat H^\dagger = \left[\tfrac{1}{2}(\hat A + \hat A^\dagger)\right]^\dagger = \tfrac{1}{2}(\hat A^\dagger + \hat A) = \hat H. \quad\checkmark
$$

**Hermiticity of $\hat K$.** Recall that $(\mathrm{i})^\dagger = -\mathrm{i}$ when distributed through a dagger (the dagger conjugates scalars). So

$$
\hat K^\dagger = \left[\tfrac{1}{2\mathrm{i}}(\hat A - \hat A^\dagger)\right]^\dagger = \tfrac{1}{-2\mathrm{i}}(\hat A^\dagger - \hat A) = \tfrac{1}{2\mathrm{i}}(\hat A - \hat A^\dagger) = \hat K. \quad\checkmark
$$

**Decomposition holds.** Plug back:

$$
\hat H + \mathrm{i}\hat K = \tfrac{1}{2}(\hat A + \hat A^\dagger) + \mathrm{i}\cdot\tfrac{1}{2\mathrm{i}}(\hat A - \hat A^\dagger) = \tfrac{1}{2}\hat A + \tfrac{1}{2}\hat A^\dagger + \tfrac{1}{2}\hat A - \tfrac{1}{2}\hat A^\dagger = \hat A. \quad\checkmark
$$

(b) Compute $\hat A^\dagger$ by transposing and conjugating: $\hat A^\dagger = \begin{pmatrix} 1 & -\mathrm{i} \\ -\mathrm{i} & 1\end{pmatrix}$. Then

$$
\hat H = \tfrac{1}{2}(\hat A + \hat A^\dagger) = \tfrac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2\end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1\end{pmatrix} = \hat I,
$$

$$
\hat K = \tfrac{1}{2\mathrm{i}}(\hat A - \hat A^\dagger) = \tfrac{1}{2\mathrm{i}}\begin{pmatrix} 0 & 2\mathrm{i} \\ 2\mathrm{i} & 0\end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} = \hat X.
$$

So $\hat A = \hat I + \mathrm{i}\hat X$ — a clean Pauli decomposition. Verification: $\hat I + \mathrm{i}\hat X = \begin{pmatrix}1 & 0\\0 & 1\end{pmatrix} + \begin{pmatrix}0 & \mathrm{i}\\ \mathrm{i} & 0\end{pmatrix} = \begin{pmatrix}1 & \mathrm{i}\\ \mathrm{i} & 1\end{pmatrix} = \hat A$.

(c) The Hermitian part $\hat H$ corresponds to the **real part** of $z = x + \mathrm{i}y$; the anti-Hermitian part $\mathrm{i}\hat K$ (with $\hat K$ Hermitian) corresponds to the **imaginary part**. The analogy is exact: just as every complex number splits uniquely into real + imaginary parts via $x = \tfrac{1}{2}(z+z^*)$ and $y = \tfrac{1}{2\mathrm{i}}(z-z^*)$, every operator splits uniquely into Hermitian + (i times) Hermitian parts via the formulas above — with $\dagger$ playing the role of complex conjugation. Hermitian operators are therefore the natural "real" subspace of the algebra, and observables — being measurable real-valued — are restricted to it. (Forward pointer: the *unitary* operators $\hat U = \mathrm{e}^{\mathrm{i}\hat O}$ — to be introduced in Section 1.3 — play the role of phase factors $\mathrm{e}^{\mathrm{i}\theta}$ for real $\theta$, completing the analogy: Hermitian ↔ real, unitary ↔ unit-modulus.)

<!-- ─── -->

**3. Bloch vector from amplitudes.** A qubit is in the state $\vert\psi\rangle = \tfrac{1}{\sqrt 3}\vert 0\rangle + \sqrt{\tfrac{2}{3}}\,\vert 1\rangle$. Using the lecture's amplitude formulas

$$
\langle\hat X\rangle = 2\operatorname{Re}(\alpha^*\beta),\quad \langle\hat Y\rangle = 2\operatorname{Im}(\alpha^*\beta),\quad \langle\hat Z\rangle = \vert\alpha\vert^2 - \vert\beta\vert^2,
$$

compute the Bloch vector $\boldsymbol n = (\langle\hat X\rangle, \langle\hat Y\rangle, \langle\hat Z\rangle)$. Verify $\vert\boldsymbol n\vert = 1$, and explain in one sentence why this had to come out unit-length.

**Solution.**

With $\alpha = 1/\sqrt 3$ and $\beta = \sqrt{2/3}$ (both real and positive), the product $\alpha^*\beta = (1/\sqrt 3)\cdot\sqrt{2/3} = \sqrt{2}/3$ is real, so $\operatorname{Im}(\alpha^*\beta) = 0$. Hence

$$
\langle\hat X\rangle = 2\cdot\frac{\sqrt 2}{3} = \frac{2\sqrt 2}{3},
\qquad
\langle\hat Y\rangle = 0,
\qquad
\langle\hat Z\rangle = \tfrac{1}{3} - \tfrac{2}{3} = -\tfrac{1}{3}.
$$

The Bloch vector is $\boldsymbol n = \bigl(\tfrac{2\sqrt 2}{3},\, 0,\, -\tfrac{1}{3}\bigr)$. Sum of squares:

$$
\vert\boldsymbol n\vert^2 = \left(\tfrac{2\sqrt 2}{3}\right)^{\!2} + 0 + \left(-\tfrac{1}{3}\right)^{\!2} = \tfrac{8}{9} + \tfrac{1}{9} = 1.
$$

So $\vert\boldsymbol n\vert = 1$, exactly as required for any pure qubit state — pure states sit on the *surface* of the Bloch sphere (1.1.2 Problem 4). The vanishing $\langle\hat Y\rangle$ reflects the absence of a relative phase between the two real amplitudes: the state lies in the $xz$-plane of the Bloch sphere.

<!-- ─── -->

**4. Eigenstate of spin along an arbitrary axis.** Continuing from 1.1.2 Problem 7, the spin observable along a unit axis $\boldsymbol{m}$ is $\boldsymbol{m}\cdot\hat{\boldsymbol\sigma} = m_x\hat X + m_y\hat Y + m_z\hat Z$. Find the $+1$ eigenstate explicitly for the axis $\boldsymbol{m} = (\sin\theta_0, 0, \cos\theta_0)$ in the $xz$-plane.

(a) Write $\boldsymbol{m}\cdot\hat{\boldsymbol\sigma}$ as an explicit $2\times 2$ matrix.

(b) Solve the eigenvalue equation $(\boldsymbol{m}\cdot\hat{\boldsymbol\sigma})\vert\psi\rangle = +\vert\psi\rangle$. Show that the normalized $+1$ eigenstate is $\vert\psi\rangle = \cos(\theta_0/2)\vert 0\rangle + \sin(\theta_0/2)\vert 1\rangle$.

(c) Compute the Bloch vector of this $\vert\psi\rangle$ from the formulas in Problem 3 and verify it equals $\boldsymbol{m}$ itself — consistent with the result of 1.1.2 Problem 7 that the Bloch axis is the unique direction of maximal spin alignment.

**Solution.**

(a) With $n_y = 0$,

$$
\boldsymbol{m}\cdot\hat{\boldsymbol\sigma} = \sin\theta_0\,\hat X + \cos\theta_0\,\hat Z = \begin{pmatrix} \cos\theta_0 & \sin\theta_0 \\ \sin\theta_0 & -\cos\theta_0\end{pmatrix}.
$$

(b) The $+1$ eigenvalue equation reads $(\boldsymbol{m}\cdot\hat{\boldsymbol\sigma} - \hat I)v = 0$, i.e.

$$
\begin{pmatrix} \cos\theta_0 - 1 & \sin\theta_0 \\ \sin\theta_0 & -\cos\theta_0 - 1\end{pmatrix}\begin{pmatrix} a\\b\end{pmatrix} = 0.
$$

The first row gives $(\cos\theta_0 - 1)a + \sin\theta_0\,b = 0$, so $b/a = (1-\cos\theta_0)/\sin\theta_0$. Applying the half-angle identities $1-\cos\theta_0 = 2\sin^2(\theta_0/2)$ and $\sin\theta_0 = 2\sin(\theta_0/2)\cos(\theta_0/2)$:

$$
\frac{b}{a} = \frac{2\sin^2(\theta_0/2)}{2\sin(\theta_0/2)\cos(\theta_0/2)} = \tan(\theta_0/2).
$$

The natural normalised choice is $a = \cos(\theta_0/2)$, $b = \sin(\theta_0/2)$, satisfying $a^2 + b^2 = 1$. Hence

$$
\vert\psi\rangle = \cos(\theta_0/2)\,\vert 0\rangle + \sin(\theta_0/2)\,\vert 1\rangle.
$$

This is exactly the Bloch parametrization $\vert\psi\rangle = \cos(\theta/2)\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2)\vert 1\rangle$ with $\theta = \theta_0$ and $\varphi = 0$ — consistent with $\boldsymbol{m}$ lying in the $xz$-plane (no azimuth).

(c) The amplitudes are real, so $\alpha^*\beta = \cos(\theta_0/2)\sin(\theta_0/2) = \tfrac12\sin\theta_0$ (real). Then

$$
\langle\hat X\rangle = 2\cdot\tfrac12\sin\theta_0 = \sin\theta_0, \quad \langle\hat Y\rangle = 0, \quad \langle\hat Z\rangle = \cos^2(\theta_0/2) - \sin^2(\theta_0/2) = \cos\theta_0.
$$

So $\boldsymbol n = (\sin\theta_0, 0, \cos\theta_0) = \boldsymbol{m}$. The Bloch vector of the $+1$ eigenstate of $\boldsymbol{m}\cdot\hat{\boldsymbol\sigma}$ points along $\boldsymbol{m}$ itself — saturating the alignment bound of 1.1.2 Problem 7. Geometrically, the $+1$ eigenstate of spin along $\boldsymbol{m}$ is the state whose Bloch arrow *is* $\boldsymbol{m}$.

<!-- ─── -->

**5. Pauli decomposition of a 2x2 Hermitian operator.** Any Hermitian operator on the qubit Hilbert space can be written uniquely as

$$
\hat O = a_0\,\hat I + a_x\,\hat X + a_y\,\hat Y + a_z\,\hat Z,
$$

with $a_0, a_x, a_y, a_z\in\mathbb{R}$ (lecture's "$4$ real degrees of freedom" statement).

(a) Using the lecture's trace identities $\operatorname{Tr}(\hat\sigma^i) = 0$, $\operatorname{Tr}(\hat I) = 2$, and $\operatorname{Tr}(\hat\sigma^i\hat\sigma^j) = 2\delta_{ij}$, show that the coefficients are recovered by

$$
a_0 = \tfrac{1}{2}\operatorname{Tr}(\hat O), \qquad a_i = \tfrac{1}{2}\operatorname{Tr}(\hat O\,\hat\sigma^i)\quad (i\in\{x,y,z\}).
$$

(b) Apply to $\hat O = \begin{pmatrix} 3 & 2-\mathrm{i} \\ 2+\mathrm{i} & 1\end{pmatrix}$. Compute $a_0, a_x, a_y, a_z$ and write the result.

(c) For an observable of the form $\hat O = a_0\,\hat I + \boldsymbol a\cdot\hat{\boldsymbol\sigma}$ with $\boldsymbol a = (a_x, a_y, a_z)$, identify (i) what $a_0$ represents, (ii) what $\vert\boldsymbol a\vert$ controls, and (iii) what the direction $\boldsymbol{e}_a = \boldsymbol a/\vert\boldsymbol a\vert$ encodes. (Hint: use the result of Problem 4 and the spectral structure of $\boldsymbol{n}\cdot\hat{\boldsymbol\sigma}$ from Problem 7.)

**Solution.**

(a) Apply $\operatorname{Tr}$ to the decomposition. The Pauli operators are traceless and the identity has trace $2$, so

$$
\operatorname{Tr}(\hat O) = a_0\,\operatorname{Tr}(\hat I) + \sum_i a_i\,\operatorname{Tr}(\hat\sigma^i) = 2a_0 + 0 \;\Longrightarrow\; a_0 = \tfrac{1}{2}\operatorname{Tr}(\hat O).
$$

For each Pauli component, multiply by $\hat\sigma^j$ on the right and take the trace. Using $\hat\sigma^i\hat\sigma^j = \delta_{ij}\hat I + \mathrm{i}\epsilon_{ijk}\hat\sigma^k$ (lecture eq-pauli-multiplication), $\operatorname{Tr}(\hat I) = 2$, and $\operatorname{Tr}(\hat\sigma^k) = 0$:

$$
\operatorname{Tr}(\hat O\,\hat\sigma^j) = a_0\operatorname{Tr}(\hat\sigma^j) + \sum_i a_i\operatorname{Tr}(\hat\sigma^i\hat\sigma^j) = 0 + \sum_i a_i\cdot 2\delta_{ij} = 2 a_j \;\Longrightarrow\; a_j = \tfrac{1}{2}\operatorname{Tr}(\hat O\,\hat\sigma^j).
$$

(b) Compute each trace.

$\operatorname{Tr}(\hat O) = 3 + 1 = 4$, so $a_0 = 2$.

$\operatorname{Tr}(\hat O\,\hat X)$: multiply $\hat O$ by $\hat X = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, which swaps columns:

$$
\hat O\,\hat X = \begin{pmatrix} 3 & 2-\mathrm{i} \\ 2+\mathrm{i} & 1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix} 2-\mathrm{i} & 3 \\ 1 & 2+\mathrm{i}\end{pmatrix},
\qquad \operatorname{Tr}(\hat O\hat X) = (2-\mathrm{i}) + (2+\mathrm{i}) = 4.
$$

So $a_x = 2$.

$\operatorname{Tr}(\hat O\,\hat Y)$: with $\hat Y = \begin{pmatrix}0 & -\mathrm{i}\\ \mathrm{i} & 0\end{pmatrix}$,

$$
\hat O\,\hat Y = \begin{pmatrix} 3 & 2-\mathrm{i} \\ 2+\mathrm{i} & 1\end{pmatrix}\begin{pmatrix}0 & -\mathrm{i}\\ \mathrm{i} & 0\end{pmatrix} = \begin{pmatrix} \mathrm{i}(2-\mathrm{i}) & -3\mathrm{i} \\ \mathrm{i} & -\mathrm{i}(2+\mathrm{i})\end{pmatrix} = \begin{pmatrix} 1 + 2\mathrm{i} & -3\mathrm{i} \\ \mathrm{i} & 1 - 2\mathrm{i}\end{pmatrix},
$$

$$
\operatorname{Tr}(\hat O\hat Y) = (1 + 2\mathrm{i}) + (1 - 2\mathrm{i}) = 2 \;\Longrightarrow\; a_y = 1.
$$

$\operatorname{Tr}(\hat O\,\hat Z)$: with $\hat Z = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}$, $\hat O\hat Z$ flips the sign of the second column, leaving the diagonal as $3$ and $-1$:

$$
\operatorname{Tr}(\hat O\,\hat Z) = 3 + (-1) = 2 \;\Longrightarrow\; a_z = 1.
$$

So $\hat O = 2\hat I + 2\hat X + \hat Y + \hat Z$. (Sanity: rebuild the matrix — $2\hat X = \begin{pmatrix}0&2\\2&0\end{pmatrix}$, $\hat Y = \begin{pmatrix}0&-\mathrm{i}\\ \mathrm{i}&0\end{pmatrix}$, $\hat Z = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$. Summing with $2\hat I$ gives $\begin{pmatrix}3 & 2-\mathrm{i}\\ 2+\mathrm{i} & 1\end{pmatrix}$. ✓)

(c) **Physical role of the four numbers.**

- **$a_0$** is the *trace-average* of $\hat O$. It is an overall **shift of every measured eigenvalue** (an additive constant in the spectrum): replacing $\hat O$ by $\hat O + c\hat I$ adds $c$ to each outcome without changing eigenstates or any *differences* between measurement results (splittings, commutators, etc.). Only when $\hat O$ is the Hamiltonian does this constant read as an energy offset; for a general observable it is simply an unobservable overall shift of reported values.
- **$\vert\boldsymbol a\vert$** sets the **eigenvalue spread**. By Problem 7, $(\boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma})^2 = \hat I$, so $\boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma}$ has eigenvalues $\pm 1$. Therefore $\hat O = a_0\hat I + \vert\boldsymbol a\vert(\boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma})$ has eigenvalues $a_0 \pm \vert\boldsymbol a\vert$, separated by $2\vert\boldsymbol a\vert$.
- **$\boldsymbol{e}_a = \boldsymbol a/\vert\boldsymbol a\vert$** encodes the **Bloch axis of the eigenstates**: by Problem 4, the $+1$ eigenstate of $\boldsymbol{e}_a\cdot\hat{\boldsymbol\sigma}$ has Bloch vector $\boldsymbol{e}_a$, and the $-1$ eigenstate has Bloch vector $-\boldsymbol{e}_a$ (antipodal, 1.1.2 Problem 5). The direction of $\boldsymbol a$ thus determines the spatial axis of the observable; its magnitude determines the eigenvalue spread; the additive $a_0$ is an unobservable overall shift of measured eigenvalues.

For the example above, $\boldsymbol a = (2, 1, 1)$, $\vert\boldsymbol a\vert = \sqrt{6}$, $\boldsymbol{e}_a = (2,1,1)/\sqrt 6$, and eigenvalues $2 \pm \sqrt 6$.

<!-- ─── -->

**6. Non-Hermitian eigenstates.** The lecture proves that distinct eigenvalues of a *Hermitian* operator yield orthogonal eigenvectors. Investigate what happens when the operator is *not* Hermitian.

Consider the (non-Hermitian) operator

$$
\hat A = \begin{pmatrix} 1 & 1 \\ 0 & 2\end{pmatrix}.
$$

(a) Verify that $\hat A$ is not Hermitian.

(b) Find the two eigenvalues by solving the characteristic equation.

(c) Find the corresponding eigenvectors $\vert v_1\rangle, \vert v_2\rangle$ (normalised). Compute the inner product $\langle v_1\vert v_2\rangle$ and check whether it vanishes.

(d) Identify the step in the lecture's proof of "orthogonal eigenvectors for distinct eigenvalues" that *required* Hermiticity. Why does the argument fail for $\hat A$?

**Solution.**

(a) The transpose-conjugate is $\hat A^\dagger = \begin{pmatrix} 1 & 0 \\ 1 & 2\end{pmatrix} \neq \hat A$ (the upper-right $1$ versus the lower-left $0$ already differ). Not Hermitian.

(b) Eigenvalues from $\det(\hat A - \lambda\hat I) = 0$:

$$
(1 - \lambda)(2 - \lambda) - (1)(0) = 0 \;\Longrightarrow\; \lambda_1 = 1,\ \lambda_2 = 2.
$$

(For an upper-triangular matrix, the eigenvalues are simply the diagonal entries.)

(c) Eigenvector for $\lambda_1 = 1$: $(\hat A - \hat I)v = 0$ gives $\begin{pmatrix} 0 & 1 \\ 0 & 1\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix} = 0$, so $b = 0$ and $a$ is free. Normalised:

$$
\vert v_1\rangle = \begin{pmatrix} 1\\ 0\end{pmatrix} = \vert 0\rangle.
$$

Eigenvector for $\lambda_2 = 2$: $(\hat A - 2\hat I)v = 0$ gives $\begin{pmatrix} -1 & 1 \\ 0 & 0\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix} = 0$, so $a = b$. Normalised:

$$
\vert v_2\rangle = \frac{1}{\sqrt 2}\begin{pmatrix} 1\\ 1\end{pmatrix} = \vert+\rangle.
$$

Inner product:

$$
\langle v_1\vert v_2\rangle = \langle 0\vert+\rangle = \frac{1}{\sqrt 2} \neq 0.
$$

The eigenvectors are **not orthogonal**, despite belonging to distinct eigenvalues.

(d) The lecture's proof writes

$$
\langle v_1\vert\hat O\vert v_2\rangle = \lambda_2\langle v_1\vert v_2\rangle \quad\text{(from }\hat O\vert v_2\rangle = \lambda_2\vert v_2\rangle\text{)}.
$$

To get a second expression with $\lambda_1$, one uses Hermiticity to act $\hat O$ to the left:

$$
\langle v_1\vert\hat O\vert v_2\rangle = \langle\hat O^\dagger v_1\vert v_2\rangle = \langle\hat O v_1\vert v_2\rangle = \lambda_1^*\langle v_1\vert v_2\rangle.
$$

The last step uses $\hat O^\dagger = \hat O$ (Hermiticity) **and** $\lambda_1^* = \lambda_1$ (which itself requires Hermiticity). Equating the two expressions gives $(\lambda_2 - \lambda_1)\langle v_1\vert v_2\rangle = 0$, hence orthogonality for distinct eigenvalues.

For our $\hat A$, $\hat A^\dagger \neq \hat A$, so the "act to the left" step does **not** turn $\hat A^\dagger$ into $\hat A$. The chain of equalities breaks, and the conclusion fails. **Hermiticity is the load-bearing assumption.** This is the operational reason quantum mechanics promotes observables to Hermitian operators: not just to ensure real eigenvalues, but to guarantee an orthonormal eigenbasis — without which the spectral decomposition and the Born rule would have no clean home.

<!-- ─── -->

**7. Pauli square along an arbitrary axis.** Use the Pauli multiplication law $\hat\sigma^i\hat\sigma^j = \delta_{ij}\hat I + \mathrm{i}\epsilon_{ijk}\hat\sigma^k$ to prove that, for any unit vector $\boldsymbol{n} = (n_x, n_y, n_z)$,

$$
(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2 = \hat I.
$$

(a) Expand $(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2 = \sum_{i,j} n_i n_j\,\hat\sigma^i\hat\sigma^j$ using the Pauli multiplication law. Identify the two contributions (symmetric and antisymmetric in $i,j$).

(b) Use the symmetry of $n_i n_j$ and the antisymmetry of $\epsilon_{ijk}$ to argue that the $\hat\sigma^k$ term vanishes after summation.

(c) Use the result to deduce that every eigenvalue of $\boldsymbol{n}\cdot\hat{\boldsymbol\sigma}$ satisfies $\lambda^2 = 1$, so $\lambda = \pm 1$. Why does this confirm that "every spin observable along any axis has the same two-point spectrum $\{+1, -1\}$" — and not, say, more outcomes when $\boldsymbol{n}$ is far from one of the coordinate axes?

**Solution.**

(a) Expanding the product and applying the multiplication law:

$$
(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2 = \sum_{i,j} n_i n_j\,\hat\sigma^i\hat\sigma^j = \sum_{i,j} n_i n_j\bigl(\delta_{ij}\hat I + \mathrm{i}\epsilon_{ijk}\hat\sigma^k\bigr) = \underbrace{\sum_i n_i^2\,\hat I}_{\text{diagonal part}} + \mathrm{i}\underbrace{\sum_{i,j,k} n_i n_j\,\epsilon_{ijk}\,\hat\sigma^k}_{\text{off-diagonal part}}.
$$

The diagonal part collapses via $\delta_{ij}$ to $\sum_i n_i^2$, which equals $\vert\boldsymbol{n}\vert^2 = 1$. So this contribution is $\hat I$.

(b) The off-diagonal part contracts the *symmetric* tensor $n_i n_j$ (since $n_i n_j = n_j n_i$) with the *antisymmetric* tensor $\epsilon_{ijk}$. Any such contraction vanishes:

$$
\sum_{i,j} n_i n_j\,\epsilon_{ijk} = \tfrac{1}{2}\sum_{i,j}(n_i n_j - n_j n_i)\,\epsilon_{ijk} = 0,
$$

(making the contracted pair manifestly antisymmetric/symmetric). Hence the off-diagonal term is zero, and

$$
(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2 = \hat I.
$$

(c) If $\lambda$ is an eigenvalue with eigenvector $\vert v\rangle$, applying the operator twice gives $(\boldsymbol{n}\cdot\hat{\boldsymbol\sigma})^2\vert v\rangle = \lambda^2\vert v\rangle$. But the square equals $\hat I$, so $\lambda^2\vert v\rangle = \vert v\rangle$, forcing

$$
\lambda^2 = 1 \quad\Longrightarrow\quad \lambda = \pm 1.
$$

There are no additional eigenvalues: the spin observable along any axis returns exactly two possible outcomes, $+1$ and $-1$. This is a special, geometry-independent statement — the $z$-axis carries no privileged spectrum, and a "tilted" spin observable along an off-axis $\boldsymbol{n}$ still gives the same dichotomous outcome set. (Misconception check: one might guess that tilting $\boldsymbol{n}$ produces intermediate eigenvalues like $\pm n_z$. Problem 7 rules this out: the spectrum is *invariant* under rotation of the measurement axis; only the eigenstates rotate.)

<!-- ─── -->

**8. Pauli multiplication from commutator and anti-commutator.** The lecture gives two relations: the commutator $[\hat\sigma^i, \hat\sigma^j] = 2\mathrm{i}\epsilon_{ijk}\hat\sigma^k$ and the anti-commutator $\{\hat\sigma^i, \hat\sigma^j\} = 2\delta_{ij}\hat I$. Use them to derive the product $\hat\sigma^i\hat\sigma^j$ without computing any matrices.

(a) Write the defining identities for the operator product:

$$
\hat\sigma^i\hat\sigma^j = \tfrac{1}{2}\bigl(\{\hat\sigma^i,\hat\sigma^j\} + [\hat\sigma^i,\hat\sigma^j]\bigr).
$$

Substitute the lecture's commutator and anti-commutator to recover the Pauli multiplication law $\hat\sigma^i\hat\sigma^j = \delta_{ij}\hat I + \mathrm{i}\epsilon_{ijk}\hat\sigma^k$.

(b) Specialise to $(i,j) = (1,2)$ to compute $\hat X\hat Y$ and $\hat Y\hat X$ directly. Verify $\hat X\hat Y = \mathrm{i}\hat Z$ and $\hat Y\hat X = -\mathrm{i}\hat Z$.

(c) The decomposition "product = (anti-commutator + commutator)/2" works for **any** pair of operators. Explain in one sentence why this identity is structural: every operator product splits into a symmetric (anti-commutator) and an antisymmetric (commutator) part, independent of whether the operators are Hermitian, unitary, or arbitrary.

**Solution.**

(a) Add and subtract the two identities. For any operators $\hat A, \hat B$,

$$
\{\hat A,\hat B\} + [\hat A,\hat B] = (\hat A\hat B + \hat B\hat A) + (\hat A\hat B - \hat B\hat A) = 2\hat A\hat B,
$$

so $\hat A\hat B = \tfrac{1}{2}(\{\hat A,\hat B\} + [\hat A,\hat B])$. Applied to Pauli operators and substituting the lecture's data,

$$
\hat\sigma^i\hat\sigma^j = \tfrac{1}{2}\bigl(2\delta_{ij}\hat I + 2\mathrm{i}\epsilon_{ijk}\hat\sigma^k\bigr) = \delta_{ij}\hat I + \mathrm{i}\epsilon_{ijk}\hat\sigma^k.
$$

This is the lecture's multiplication law — *recovered without computing any $2\times 2$ matrices.*

(b) For $(i,j) = (1,2)$ (i.e. $(\hat X,\hat Y)$), $\delta_{ij} = 0$ and $\epsilon_{ijk} = \epsilon_{12k}$ is nonzero only at $k = 3$, with $\epsilon_{123} = +1$. So

$$
\hat X\hat Y = 0\cdot\hat I + \mathrm{i}\cdot(+1)\cdot\hat Z = \mathrm{i}\hat Z.
$$

Swapping order, $\epsilon_{21k}$ has $\epsilon_{213} = -1$, so

$$
\hat Y\hat X = \mathrm{i}\cdot(-1)\cdot\hat Z = -\mathrm{i}\hat Z.
$$

(Cross-check via the anti-commutator: $\hat X\hat Y + \hat Y\hat X = \mathrm{i}\hat Z - \mathrm{i}\hat Z = 0$, agreeing with $\{\hat X,\hat Y\} = 0$ from anti-commutation.)

(c) Any operator product $\hat A\hat B$ admits the identity decomposition

$$
\hat A\hat B = \underbrace{\tfrac12(\hat A\hat B + \hat B\hat A)}_{\text{symmetric, anti-commutator}} + \underbrace{\tfrac12(\hat A\hat B - \hat B\hat A)}_{\text{antisymmetric, commutator}}.
$$

The split into symmetric + antisymmetric parts under exchange $\hat A \leftrightarrow \hat B$ is purely algebraic — it makes no reference to Hermiticity, unitarity, or the dimension of the Hilbert space. It is the operator-theoretic analogue of writing a matrix as the sum of its symmetric and antisymmetric parts under transposition. The Pauli multiplication law is the special case where both the commutator and anti-commutator are particularly simple (proportional to Pauli operators and to the identity, respectively), but the *structure* of the derivation is universal.
