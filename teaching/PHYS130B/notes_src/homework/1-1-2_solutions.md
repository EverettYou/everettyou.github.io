# 1.1.2 State and Representation
Worked solutions for the homework problems in the [1.1.2 State and Representation](../ch1_qubit/1-1-2-state-and-representation) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Qubit state decomposition.** A qubit is in the state $\vert \psi\rangle = \frac{1}{\sqrt{3}}\vert 0\rangle + \sqrt{\frac{2}{3}}\,\mathrm{e}^{\mathrm{i}\pi/4}\vert 1\rangle$. Find the Bloch sphere angles $(\theta, \varphi)$ for this state by matching against the standard parametrization $\vert \psi\rangle = \cos(\theta/2)\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2)\vert 1\rangle$.

**Solution.**

The Bloch parametrization requires the amplitude of $\vert 0\rangle$ to be **real and non-negative**, with the entire phase carried by the $\vert 1\rangle$ component. Here the $\vert 0\rangle$ amplitude is already $1/\sqrt{3} > 0$, so no global-phase rotation is needed — we can read off the angles by matching term by term:

$$
\cos\tfrac{\theta}{2} = \frac{1}{\sqrt{3}},
\qquad
\mathrm{e}^{\mathrm{i}\varphi}\sin\tfrac{\theta}{2} = \sqrt{\tfrac{2}{3}}\,\mathrm{e}^{\mathrm{i}\pi/4}.
$$

Since $\sqrt{2/3} > 0$, the second relation splits into a modulus and a phase:

$$
\sin\tfrac{\theta}{2} = \sqrt{\tfrac{2}{3}},
\qquad
\varphi = \frac{\pi}{4}.
$$

The two moduli are consistent with normalization, $\cos^2(\theta/2) + \sin^2(\theta/2) = \tfrac13 + \tfrac23 = 1$. Dividing sine by cosine,

$$
\tan\tfrac{\theta}{2} = \frac{\sin(\theta/2)}{\cos(\theta/2)} = \frac{\sqrt{2/3}}{\sqrt{1/3}} = \sqrt{2},
$$

so

$$
\theta = 2\arctan\sqrt{2} \approx 109.47^\circ \approx 1.911\ \mathrm{rad}.
$$

The Bloch angles are therefore

$$
(\theta, \varphi) = \left(2\arctan\sqrt{2},\ \tfrac{\pi}{4}\right) \approx (109.47^\circ,\ 45^\circ).
$$

(The polar angle $109.47^\circ$ is the tetrahedral angle, $\arccos(-1/3)$; equivalently $\cos\theta = \cos^2(\theta/2) - \sin^2(\theta/2) = \tfrac13 - \tfrac23 = -\tfrac13$.) The state sits just below the equator of the Bloch sphere, rotated $45^\circ$ around the $z$-axis from the $x$-direction.

<!-- ─── -->

**2. State reconstruction from Pauli expectations.** A qubit is identically prepared on many copies, and the three Pauli expectation values are measured to be

$$
\langle\hat X\rangle = 0, \qquad \langle\hat Y\rangle = \tfrac{1}{\sqrt{2}}, \qquad \langle\hat Z\rangle = \tfrac{1}{\sqrt{2}}.
$$

(a) Read off the Bloch vector $\boldsymbol{n}$ and verify $\vert\boldsymbol{n}\vert = 1$. Why is this consistent with the assertion that the state is pure?

(b) Convert $\boldsymbol{n}$ to Bloch angles $(\theta, \varphi)$.

(c) Write the state in the standard form $\vert\psi\rangle = \cos(\theta/2)\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2)\vert 1\rangle$.

(d) Are there any other physical states (up to global phase) with the same three Pauli expectation values? Justify your answer by counting the parameters of the qubit Hilbert space against the parameters of the data.

**Solution.**

(a) The Bloch vector is read directly from the three Pauli expectations:

$$
\boldsymbol{n} = (\langle\hat X\rangle,\, \langle\hat Y\rangle,\, \langle\hat Z\rangle) = (0,\, \tfrac{1}{\sqrt{2}},\, \tfrac{1}{\sqrt{2}}).
$$

Its squared length is

$$
\vert\boldsymbol{n}\vert^2 = 0^2 + \left(\tfrac{1}{\sqrt2}\right)^{\!2} + \left(\tfrac{1}{\sqrt2}\right)^{\!2} = 0 + \tfrac12 + \tfrac12 = 1,
$$

so $\vert\boldsymbol{n}\vert = 1$. Pure qubit states sit on the **surface** of the Bloch sphere, so a unit Bloch vector is the signature of purity (mixed states have $\vert\boldsymbol{n}\vert < 1$ — to be developed in Chapter 6). The measurement output is self-consistent with the assumption that the source produces a pure state.

(b) From the parametrization $\boldsymbol n = (\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)$, the polar angle is fixed by $n_z$:

$$
\cos\theta = \tfrac{1}{\sqrt2} \quad\Longrightarrow\quad \theta = \tfrac{\pi}{4}.
$$

Then $\sin\theta = \sqrt{1 - 1/2} = 1/\sqrt{2}$ (positive root, since $\theta\in[0,\pi]$). The azimuth follows from $(n_x, n_y) = (\sin\theta\cos\varphi,\, \sin\theta\sin\varphi)$:

$$
\cos\varphi = \frac{n_x}{\sin\theta} = 0, \qquad \sin\varphi = \frac{n_y}{\sin\theta} = \frac{1/\sqrt2}{1/\sqrt2} = 1 \quad\Longrightarrow\quad \varphi = \tfrac{\pi}{2}.
$$

So $(\theta,\varphi) = (\pi/4,\ \pi/2)$.

(c) Substituting into the standard form,

$$
\vert\psi\rangle = \cos\tfrac{\pi}{8}\,\vert 0\rangle + \mathrm{e}^{\mathrm{i}\pi/2}\sin\tfrac{\pi}{8}\,\vert 1\rangle = \cos\tfrac{\pi}{8}\,\vert 0\rangle + \mathrm{i}\sin\tfrac{\pi}{8}\,\vert 1\rangle.
$$

Numerically, $\cos(\pi/8) \approx 0.924$ and $\sin(\pi/8) \approx 0.383$.

(d) No — the state is uniquely determined (up to global phase). The argument is by parameter counting:

- The space of pure qubit states is 2-dimensional (the Bloch sphere $S^2$).
- The Bloch vector $\boldsymbol{n}$ is constrained to have unit length, $\vert\boldsymbol{n}\vert = 1$: 3 real numbers minus 1 constraint = 2 parameters.
- So **the Bloch vector uniquely encodes the pure state**, and the three Pauli expectations are sufficient to reconstruct it.

This is the operational content of **single-qubit state tomography**: measuring the three Pauli expectations on enough copies pins down the state to within statistical uncertainty. (Contrast with Problem 2 of 1.1.1: there, only two probabilities were given — $Z$- and $X$-basis — which left a sign ambiguity in $n_y$, hence two candidate states. The third measurement breaks that degeneracy.)

<!-- ─── -->

**3. State representation in different bases.** Express the state $\vert \psi\rangle = \tfrac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle)$ in the $X$-basis $\{\vert +\rangle, \vert -\rangle\}$. Then express $\vert \phi\rangle = \tfrac{1}{\sqrt{2}}(\vert 0\rangle + \mathrm{i}\vert 1\rangle)$ in the $X$-basis. Compute the inner product $\langle\phi\vert \psi\rangle$ in both the $Z$-basis and the $X$-basis representations and verify you get the same result.

**Solution.**

A state $\vert\chi\rangle = a\vert 0\rangle + b\vert 1\rangle$ is rewritten in the X-basis by substituting the inverse relations $\vert 0\rangle = \tfrac{1}{\sqrt2}(\vert +\rangle + \vert -\rangle)$ and $\vert 1\rangle = \tfrac{1}{\sqrt2}(\vert +\rangle - \vert -\rangle)$, which gives the general formula

$$
\vert\chi\rangle = \frac{a+b}{\sqrt{2}}\,\vert +\rangle + \frac{a-b}{\sqrt{2}}\,\vert -\rangle.
$$

*State $\vert\psi\rangle$.* Here $a = b = 1/\sqrt{2}$, so

$$
\frac{a+b}{\sqrt2} = 1,
\qquad
\frac{a-b}{\sqrt2} = 0
\quad\Longrightarrow\quad
\vert\psi\rangle = \vert +\rangle.
$$

This is no surprise: $\tfrac{1}{\sqrt2}(\vert 0\rangle + \vert 1\rangle)$ is the definition of $\vert +\rangle$ — in the X-basis it is the first basis vector.

*State $\vert\phi\rangle$.* Here $a = 1/\sqrt{2}$, $b = \mathrm{i}/\sqrt{2}$, so

$$
\frac{a+b}{\sqrt2} = \frac{1+\mathrm{i}}{2},
\qquad
\frac{a-b}{\sqrt2} = \frac{1-\mathrm{i}}{2},
$$

giving

$$
\vert\phi\rangle = \frac{1+\mathrm{i}}{2}\,\vert +\rangle + \frac{1-\mathrm{i}}{2}\,\vert -\rangle.
$$

(Sanity check: $\vert(1+\mathrm{i})/2\vert^2 + \vert(1-\mathrm{i})/2\vert^2 = \tfrac24 + \tfrac24 = 1$, so $\vert\phi\rangle$ is still normalized — as it must be, since a change of orthonormal basis is unitary.)

*Inner product in the Z-basis.* With $\vert\phi\rangle \leftrightarrow (1/\sqrt2,\ \mathrm{i}/\sqrt2)$ and $\vert\psi\rangle \leftrightarrow (1/\sqrt2,\ 1/\sqrt2)$, the inner product conjugates the components of the bra:

$$
\langle\phi\vert\psi\rangle = \left(\tfrac{1}{\sqrt2}\right)^{\!*}\tfrac{1}{\sqrt2} + \left(\tfrac{\mathrm{i}}{\sqrt2}\right)^{\!*}\tfrac{1}{\sqrt2}
= \tfrac12 - \tfrac{\mathrm{i}}{2} = \frac{1-\mathrm{i}}{2}.
$$

*Inner product in the X-basis.* With $\vert\phi\rangle \leftrightarrow \bigl(\tfrac{1+\mathrm{i}}{2},\ \tfrac{1-\mathrm{i}}{2}\bigr)$ and $\vert\psi\rangle \leftrightarrow (1,\ 0)$,

$$
\langle\phi\vert\psi\rangle = \left(\tfrac{1+\mathrm{i}}{2}\right)^{\!*}\!(1) + \left(\tfrac{1-\mathrm{i}}{2}\right)^{\!*}\!(0)
= \frac{1-\mathrm{i}}{2}.
$$

Both representations give $\langle\phi\vert\psi\rangle = \dfrac{1-\mathrm{i}}{2}$. The agreement is guaranteed: the inner product is a basis-independent geometric quantity, and any change of orthonormal basis is a unitary map that preserves all inner products.

<!-- ─── -->

**4. Bloch vector calculation.** Compute the Bloch vector $\boldsymbol{n} = (\langle \hat{X}\rangle, \langle\hat{Y}\rangle, \langle\hat{Z}\rangle)$ for the state $\vert \psi\rangle = \cos(\pi/8)\vert 0\rangle + \mathrm{e}^{\mathrm{i}\pi/3}\sin(\pi/8)\vert 1\rangle$. Verify that $\vert \boldsymbol{n}\vert = 1$ as a sanity check that the state is pure.

**Solution.**

The state is already in the standard Bloch parametrization $\cos(\theta/2)\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2)\vert 1\rangle$. Matching:

$$
\frac{\theta}{2} = \frac{\pi}{8} \;\Longrightarrow\; \theta = \frac{\pi}{4},
\qquad
\varphi = \frac{\pi}{3}.
$$

The Bloch vector is then read off from $\boldsymbol{n} = (\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)$. With $\theta = \pi/4$ and $\varphi = \pi/3$:

$$
\sin\theta = \cos\theta = \frac{1}{\sqrt2},
\qquad
\cos\varphi = \frac12,
\qquad
\sin\varphi = \frac{\sqrt3}{2}.
$$

Therefore

$$
n_x = \frac{1}{\sqrt2}\cdot\frac12 = \frac{1}{2\sqrt2} \approx 0.354,
$$

$$
n_y = \frac{1}{\sqrt2}\cdot\frac{\sqrt3}{2} = \frac{\sqrt6}{4} \approx 0.612,
$$

$$
n_z = \cos\theta = \frac{1}{\sqrt2} \approx 0.707.
$$

So $\boldsymbol{n} = \bigl(\tfrac{1}{2\sqrt2},\ \tfrac{\sqrt6}{4},\ \tfrac{1}{\sqrt2}\bigr)$. Its length squared is

$$
\vert\boldsymbol{n}\vert^2 = n_x^2 + n_y^2 + n_z^2 = \frac{1}{8} + \frac{3}{8} + \frac{1}{2} = \frac{1 + 3 + 4}{8} = 1,
$$

hence $\vert\boldsymbol{n}\vert = 1$. The sanity check passes: the Bloch vector of any *pure* qubit state is a unit vector, which is the geometric statement that pure states sit on the *surface* of the Bloch sphere. (Independent cross-check: $\langle\hat{Z}\rangle = P(0) - P(1) = \cos^2(\theta/2) - \sin^2(\theta/2) = \cos\theta = n_z$.)

<!-- ─── -->

**5. Antipodal states on Bloch sphere.** On the Bloch sphere, orthogonal quantum states correspond to antipodal points (diametrically opposite). Verify this explicitly: show that if $\vert \psi\rangle$ has Bloch angles $(\theta, \varphi)$, then the orthogonal state $\vert \psi^\perp\rangle$ (satisfying $\langle\psi^\perp\vert \psi\rangle = 0$) has Bloch angles $(\pi - \theta, \varphi + \pi)$, and that its Bloch vector equals $-\boldsymbol{n}$.

**Solution.**

Write $\vert\psi\rangle$ in standard form and build the candidate $\vert\psi^\perp\rangle$ from the proposed angles $(\pi - \theta,\ \varphi + \pi)$:

$$
\vert\psi\rangle = \cos\tfrac{\theta}{2}\,\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\sin\tfrac{\theta}{2}\,\vert 1\rangle,
$$

$$
\vert\psi^\perp\rangle = \cos\!\left(\tfrac{\pi-\theta}{2}\right)\vert 0\rangle + \mathrm{e}^{\mathrm{i}(\varphi+\pi)}\sin\!\left(\tfrac{\pi-\theta}{2}\right)\vert 1\rangle.
$$

Simplify the half-angle factors using $\tfrac{\pi-\theta}{2} = \tfrac{\pi}{2} - \tfrac{\theta}{2}$ together with the co-function identities $\cos(\tfrac{\pi}{2}-x) = \sin x$ and $\sin(\tfrac{\pi}{2}-x) = \cos x$, and the phase factor with $\mathrm{e}^{\mathrm{i}\pi} = -1$:

$$
\cos\!\left(\tfrac{\pi-\theta}{2}\right) = \sin\tfrac{\theta}{2},
\qquad
\sin\!\left(\tfrac{\pi-\theta}{2}\right) = \cos\tfrac{\theta}{2},
\qquad
\mathrm{e}^{\mathrm{i}(\varphi+\pi)} = -\,\mathrm{e}^{\mathrm{i}\varphi}.
$$

Hence

$$
\vert\psi^\perp\rangle = \sin\tfrac{\theta}{2}\,\vert 0\rangle - \mathrm{e}^{\mathrm{i}\varphi}\cos\tfrac{\theta}{2}\,\vert 1\rangle.
$$

Now take the inner product with $\vert\psi\rangle$. The bra is $\langle\psi^\perp\vert = \sin\tfrac{\theta}{2}\,\langle 0\vert - \mathrm{e}^{-\mathrm{i}\varphi}\cos\tfrac{\theta}{2}\,\langle 1\vert$, and using orthonormality $\langle 0\vert 0\rangle = \langle 1\vert 1\rangle = 1$, $\langle 0\vert 1\rangle = 0$:

$$
\langle\psi^\perp\vert\psi\rangle
= \sin\tfrac{\theta}{2}\cos\tfrac{\theta}{2}
\;-\; \mathrm{e}^{-\mathrm{i}\varphi}\cos\tfrac{\theta}{2}\,\cdot\,\mathrm{e}^{\mathrm{i}\varphi}\sin\tfrac{\theta}{2}.
$$

The phase factors cancel ($\mathrm{e}^{-\mathrm{i}\varphi}\mathrm{e}^{\mathrm{i}\varphi} = 1$), leaving

$$
\langle\psi^\perp\vert\psi\rangle = \sin\tfrac{\theta}{2}\cos\tfrac{\theta}{2} - \cos\tfrac{\theta}{2}\sin\tfrac{\theta}{2} = 0.
$$

So the state with angles $(\pi-\theta,\ \varphi+\pi)$ is indeed orthogonal to $\vert\psi\rangle$. That these angles describe the **antipodal point** is seen directly from the Bloch vector: under $\theta \mapsto \pi-\theta$, $\varphi \mapsto \varphi+\pi$,

$$
\sin(\pi-\theta) = \sin\theta,\quad \cos(\pi-\theta) = -\cos\theta,\quad
\cos(\varphi+\pi) = -\cos\varphi,\quad \sin(\varphi+\pi) = -\sin\varphi,
$$

so

$$
\boldsymbol{n}^\perp = \bigl(-\sin\theta\cos\varphi,\, -\sin\theta\sin\varphi,\, -\cos\theta\bigr) = -\,\boldsymbol{n}.
$$

The orthogonal state's Bloch vector is exactly $-\boldsymbol{n}$ — diametrically opposite on the sphere. (Note: $\sin\tfrac{\theta}{2}\ge 0$ for $\theta\in[0,\pi]$, so $\vert\psi^\perp\rangle$ is already in standard form with a real non-negative $\vert 0\rangle$ amplitude; the orthogonal state is unique up to the usual global phase.)

<!-- ─── -->

**6. Bloch vector rotation.** A qubit state $\vert \psi\rangle$ has Bloch vector $\boldsymbol{n} = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$. Show that a measurement in the computational basis gives

$$
P(0) = \frac{1 + n_z}{2}, \qquad P(1) = \frac{1 - n_z}{2}.
$$

Interpret this geometrically: how does the measurement probability relate to the "height" of the Bloch vector along the $z$-axis?

**Solution.**

In the Bloch parametrization the state is $\vert\psi\rangle = \cos(\theta/2)\vert 0\rangle + \mathrm{e}^{\mathrm{i}\varphi}\sin(\theta/2)\vert 1\rangle$, so by the Born rule the computational-basis probabilities are the squared moduli of the amplitudes:

$$
P(0) = \left\vert\cos\tfrac{\theta}{2}\right\vert^2 = \cos^2\tfrac{\theta}{2},
\qquad
P(1) = \left\vert\mathrm{e}^{\mathrm{i}\varphi}\sin\tfrac{\theta}{2}\right\vert^2 = \sin^2\tfrac{\theta}{2}.
$$

The relative phase $\varphi$ has dropped out, as it must — the computational basis is the eigenbasis of $\hat{Z}$ and is insensitive to azimuthal rotations about the $z$-axis. Now apply the half-angle identities $\cos^2 x = \tfrac{1+\cos 2x}{2}$ and $\sin^2 x = \tfrac{1-\cos 2x}{2}$ with $x = \theta/2$:

$$
P(0) = \cos^2\tfrac{\theta}{2} = \frac{1 + \cos\theta}{2} = \frac{1 + n_z}{2},
$$

$$
P(1) = \sin^2\tfrac{\theta}{2} = \frac{1 - \cos\theta}{2} = \frac{1 - n_z}{2},
$$

since $n_z = \cos\theta$. The two probabilities sum to $1$ as required, and their difference is $P(0) - P(1) = n_z = \langle\hat{Z}\rangle$.

*Geometric interpretation.* The quantity $n_z$ is the projection of the Bloch vector onto the $z$-axis — literally the **height** of the state's point above the equatorial plane of the Bloch sphere. The measurement probability is a *linear* function of this height:

- North pole, $n_z = +1$ (state $\vert 0\rangle$): $P(0) = 1$ — a certain outcome.
- South pole, $n_z = -1$ (state $\vert 1\rangle$): $P(0) = 0$.
- Equator, $n_z = 0$ (states $\vert+\rangle$, $\vert-\rangle$, $\vert\mathrm{i}\rangle$, $\vert\bar{\mathrm{i}}\rangle$): $P(0) = P(1) = \tfrac12$ — a maximally uncertain outcome.

As the state slides from the north pole down to the south pole, $P(0)$ decreases linearly from $1$ to $0$. The "how likely is outcome $0$" question is answered entirely by how high the Bloch vector points along the $z$-axis; the azimuthal angle $\varphi$ is irrelevant to a $Z$-basis measurement.

<!-- ─── -->

**7. Spin expectation along an arbitrary axis.** For a unit vector $\boldsymbol{m} = (m_x, m_y, m_z) \in \mathbb{R}^3$, define the spin observable along $\boldsymbol{m}$ by

$$
\boldsymbol{m}\cdot\hat{\boldsymbol{\sigma}} \equiv m_x\,\hat{X} + m_y\,\hat{Y} + m_z\,\hat{Z}.
$$

(a) Using linearity of the expectation value, show that for any qubit state with Bloch vector $\boldsymbol{n} = (\langle\hat X\rangle, \langle\hat Y\rangle, \langle\hat Z\rangle)$,

$$
\langle\boldsymbol{m}\cdot\hat{\boldsymbol{\sigma}}\rangle = \boldsymbol{m}\cdot\boldsymbol{n}.
$$

State the geometric meaning of this identity.

(b) Find the axis $\boldsymbol{m}$ that **maximizes** $\langle\boldsymbol{m}\cdot\hat{\boldsymbol{\sigma}}\rangle$ at fixed Bloch vector $\boldsymbol{n}$. What is the maximum value? What is the relation between the optimal $\boldsymbol{m}$ and $\boldsymbol{n}$?

(c) Apply to the state $\vert+\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle + \vert 1\rangle)$. Compute its Bloch vector. Along which axis $\boldsymbol{m}$ is the spin maximally aligned? Verify the answer by direct calculation of $\langle\hat X\rangle_+$ and $\langle\hat Z\rangle_+$.

**Solution.**

(a) The expectation-value operation is linear in its argument operator, so

$$
\begin{split}
\langle\boldsymbol{m}\cdot\hat{\boldsymbol{\sigma}}\rangle
&= \langle m_x\hat X + m_y\hat Y + m_z\hat Z\rangle \\
&= m_x\langle\hat X\rangle + m_y\langle\hat Y\rangle + m_z\langle\hat Z\rangle \\
&= m_x n_x + m_y n_y + m_z n_z \\
&= \boldsymbol{m}\cdot\boldsymbol{n}.
\end{split}
$$

**Geometric meaning.** The expectation value of the spin operator along axis $\boldsymbol{m}$ is the **projection of the Bloch vector onto $\boldsymbol{m}$**. The 3-vector $\boldsymbol{n}$ has the same status as a classical vector under inner products: physical observables along any spatial direction read off by ordinary dot products.

(b) Since $\boldsymbol{m}$ and $\boldsymbol{n}$ are both 3-vectors,

$$
\boldsymbol{m}\cdot\boldsymbol{n} = \vert\boldsymbol{m}\vert\,\vert\boldsymbol{n}\vert\,\cos\alpha = \vert\boldsymbol{n}\vert\cos\alpha,
$$

where $\alpha$ is the angle between $\boldsymbol{m}$ and $\boldsymbol{n}$ (using $\vert\boldsymbol{m}\vert = 1$). This is maximized at $\alpha = 0$, giving

$$
\max_{\boldsymbol{m}}\,\langle\boldsymbol{m}\cdot\hat{\boldsymbol{\sigma}}\rangle = \vert\boldsymbol{n}\vert.
$$

For a pure state, $\vert\boldsymbol{n}\vert = 1$ (Problem 4), so the maximum equals **$1$** — the largest eigenvalue of any spin observable. The optimal axis is $\boldsymbol{m} = \boldsymbol{n}/\vert\boldsymbol{n}\vert$: the Bloch vector direction itself.

**Payload.** The Bloch vector is not just a parameterisation — its *direction* is the unique axis along which the state has definite spin. A state is "spin up" along *exactly one* axis (its own Bloch axis), and the value of the Bloch vector's magnitude tells how sharp that alignment is. For pure states, alignment is perfect; for mixed states it is partial.

(c) The state $\vert+\rangle$ has $\theta = \pi/2$ and $\varphi = 0$, so

$$
\boldsymbol{n}_+ = (\sin\theta\cos\varphi,\, \sin\theta\sin\varphi,\, \cos\theta) = (1,\, 0,\, 0).
$$

By part (b), the spin is maximally aligned along $\boldsymbol{m} = \boldsymbol{e}_x$ (with $\boldsymbol{e}_x$ the unit vector along the $x$-axis), with $\langle\hat X\rangle_+ = 1$. Direct check:

- $\hat X\vert+\rangle = \vert+\rangle$ (since $\vert+\rangle$ is the $+1$ eigenstate of $\hat X$), so $\langle+\vert\hat X\vert+\rangle = \langle+\vert+\rangle = 1$. ✓
- $\hat Z\vert+\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle - \vert 1\rangle) = \vert-\rangle$, which is orthogonal to $\vert+\rangle$, so $\langle+\vert\hat Z\vert+\rangle = 0$. ✓

The Bloch vector lies entirely along $\boldsymbol{e}_x$, consistent with $\vert+\rangle$ being the eastern point of the equator on the Bloch sphere. The state "knows" its preferred axis: it is the unique direction $\boldsymbol{m}$ for which the spin observable has definite value $+1$.

<!-- ─── -->

**8. Parametrization of n-level systems.** How many real parameters are needed to specify a general $n$-level quantum state (a "qudit")? Start with the naive count of $2n$ real numbers (from $n$ complex amplitudes), then subtract constraints from normalization and global phase. Verify your formula gives $2$ for $n = 2$ (the qubit), and identify the geometric space of states for general $n$.

**Solution.**

A general state of an $n$-level system is expanded in an orthonormal basis $\{\vert e_1\rangle, \dots, \vert e_n\rangle\}$ as

$$
\vert\psi\rangle = \sum_{k=1}^{n} c_k \vert e_k\rangle,
\qquad c_k \in \mathbb{C}.
$$

*Naive count.* There are $n$ complex amplitudes, each carrying a real and an imaginary part, for a naive total of

$$
2n \quad\text{real parameters.}
$$

*Normalization.* Physical states obey $\langle\psi\vert\psi\rangle = \sum_k \vert c_k\vert^2 = 1$. This is a **single real equation** relating the $2n$ numbers, so it removes **1** parameter:

$$
2n - 1.
$$

*Global phase.* Multiplying the whole state by $\mathrm{e}^{\mathrm{i}\alpha}$ ($\alpha\in\mathbb{R}$) leaves every measurement probability unchanged (lecture, and Problem 3 of 1.1.1), so it does not produce a new physical state. We may spend this freedom to fix one parameter — for instance, rotate the overall phase so that $c_1$ is real and non-negative. That removes **1** further parameter:

$$
2n - 1 - 1 = 2n - 2.
$$

So a general pure qudit state is specified by

$$
\boxed{\,2n - 2\,}\quad\text{independent real parameters.}
$$

*Check for $n = 2$.* The qubit gives $2(2) - 2 = 2$, the two Bloch-sphere angles $(\theta, \varphi)$.

*Geometry for general $n$.* The space of pure $n$-level states is the **complex projective space** $\mathbb{CP}^{\,n-1}$, with real dimension $2(n-1) = 2n-2$. A qutrit ($n=3$) needs $4$ real parameters and lives on $\mathbb{CP}^2$; a ququart ($n=4$) needs $6$ and lives on $\mathbb{CP}^3$; and so on. Only for $n=2$ does $\mathbb{CP}^1$ happen to be an ordinary 2-sphere ($\mathbb{CP}^1 \cong S^2$, the Bloch sphere). For $n\ge 3$ no such simple low-dimensional sphere exists, which is why the Bloch-sphere picture is special to the qubit and does not straightforwardly generalize to qudits.
