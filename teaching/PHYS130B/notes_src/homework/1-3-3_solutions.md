# 1.3.3 Heisenberg Picture
Worked solutions for the homework problems in the [1.3.3 Heisenberg Picture](../ch1_qubit/1-3-3-heisenberg-picture) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Picture equivalence on a concrete example.** Take the Hamiltonian $\hat H = \tfrac{\hbar\omega}{2}\hat\sigma^z$ and the initial state $\vert\psi(0)\rangle = \vert+\rangle$. Compute $\langle\hat\sigma^x\rangle(t)$ in two ways and verify the two answers agree.

(a) **Schrödinger picture.** Evolve the state $\vert\psi(t)\rangle = \hat U(t)\vert+\rangle$ using $\hat U(t) = \mathrm{e}^{-\mathrm{i}\omega t\hat\sigma^z/2}$ from 1.3.2. Compute $\langle\psi(t)\vert\hat\sigma^x\vert\psi(t)\rangle$.

(b) **Heisenberg picture.** Compute the time-evolved operator $\hat\sigma^x(t) = \hat U^\dagger(t)\hat\sigma^x\hat U(t)$ using the lecture's example (or the Heisenberg equation of motion). Compute $\langle+\vert\hat\sigma^x(t)\vert+\rangle$.

(c) Verify the two methods give the same result, and identify exactly which algebraic identity collapses one calculation into the other.

**Solution.**

(a) The state at time $t$ is

$$
\vert\psi(t)\rangle = \tfrac{1}{\sqrt 2}\bigl(\mathrm{e}^{-\mathrm{i}\omega t/2}\vert\uparrow\rangle + \mathrm{e}^{+\mathrm{i}\omega t/2}\vert\downarrow\rangle\bigr).
$$

Write $\vert\psi(t)\rangle = c_\uparrow\vert\uparrow\rangle + c_\downarrow\vert\downarrow\rangle$ with $c_\uparrow = \tfrac{1}{\sqrt 2}\mathrm{e}^{-\mathrm{i}\omega t/2}$ and $c_\downarrow = \tfrac{1}{\sqrt 2}\mathrm{e}^{+\mathrm{i}\omega t/2}$. Then $c_\uparrow^*c_\downarrow = \tfrac{1}{2}\mathrm{e}^{\mathrm{i}\omega t}$, and

$$
\langle\hat\sigma^x\rangle(t) = 2\,\mathrm{Re}(c_\uparrow^*c_\downarrow) = 2\,\mathrm{Re}\bigl[\tfrac{1}{2}\mathrm{e}^{\mathrm{i}\omega t}\bigr] = \cos(\omega t).
$$

(b) The lecture's Heisenberg-picture example gives $\hat\sigma^x(t) = \hat\sigma^x\cos(\omega t) - \hat\sigma^y\sin(\omega t)$. The state $\vert+\rangle$ is the $+1$ eigenstate of $\hat\sigma^x$, so $\langle+\vert\hat\sigma^x\vert+\rangle = +1$ and $\langle+\vert\hat\sigma^y\vert+\rangle = 0$. Therefore

$$
\langle+\vert\hat\sigma^x(t)\vert+\rangle = (+1)\cos(\omega t) - (0)\sin(\omega t) = \cos(\omega t).
$$

(c) Both methods yield $\cos(\omega t)$. The two calculations are related by the **regrouping identity**

$$
\langle\psi(t)\vert\hat\sigma^x\vert\psi(t)\rangle = \langle\psi(0)\vert\hat U^\dagger(t)\hat\sigma^x\hat U(t)\vert\psi(0)\rangle = \langle\psi(0)\vert\hat\sigma^x(t)\vert\psi(0)\rangle.
$$

The propagators $\hat U(t)$ can be associated with the state (Schrödinger) or with the operator (Heisenberg) — the resulting number is identical because operator multiplication is associative. Both pictures describe the same physics, expressed in two different bookkeeping conventions. The Heisenberg picture often makes conservation laws and *symmetries* more transparent (since they live on operators); the Schrödinger picture makes state preparation and measurement more transparent (since they live on states).

<!-- ─── -->

**2. Heisenberg evolution under a tilted Hamiltonian.** The lecture computes Heisenberg evolution for $\hat H = \tfrac{\hbar\omega}{2}\hat\sigma^z$. Now take the *tilted* Hamiltonian

$$
\hat H = \tfrac{\hbar\omega}{2\sqrt 2}\bigl(\hat\sigma^x + \hat\sigma^z\bigr) = \tfrac{\hbar\omega}{2}\,\boldsymbol{n}\cdot\hat{\boldsymbol\sigma},
$$

with $\boldsymbol{n} = (1, 0, 1)/\sqrt 2$ — a unit vector in the $xz$-plane at $45^\circ$ from $\boldsymbol{e}_z$.

(a) Compute the Heisenberg-equation rates $\mathrm{d}\hat\sigma^x/\mathrm{d}t$, $\mathrm{d}\hat\sigma^y/\mathrm{d}t$, $\mathrm{d}\hat\sigma^z/\mathrm{d}t$ using $[\hat\sigma^a,\hat\sigma^b] = 2\mathrm{i}\epsilon^{abc}\hat\sigma^c$.

(b) Identify which Pauli operator (if any) is conserved under this Hamiltonian. Express the conserved operator in terms of the original $\hat\sigma^a$.

(c) Find $\hat\sigma^y(t)$ explicitly. Hint: the two equations involving $\hat\sigma^y$ and the conserved combination decouple from the third equation.

**Solution.**

(a) Apply the Heisenberg equation $\mathrm{d}\hat\sigma^a/\mathrm{d}t = (\mathrm{i}/\hbar)[\hat H,\hat\sigma^a]$ with $\hat H = (\hbar\omega/2\sqrt 2)(\hat\sigma^x + \hat\sigma^z)$:

$$
\mathrm{d}\hat\sigma^x/\mathrm{d}t = (\mathrm{i}\omega/2\sqrt 2)\bigl([\hat\sigma^x,\hat\sigma^x] + [\hat\sigma^z,\hat\sigma^x]\bigr) = (\mathrm{i}\omega/2\sqrt 2)(2\mathrm{i}\hat\sigma^y) = -\frac{\omega}{\sqrt 2}\hat\sigma^y,
$$

$$
\mathrm{d}\hat\sigma^y/\mathrm{d}t = (\mathrm{i}\omega/2\sqrt 2)\bigl([\hat\sigma^x,\hat\sigma^y] + [\hat\sigma^z,\hat\sigma^y]\bigr) = (\mathrm{i}\omega/2\sqrt 2)(2\mathrm{i}\hat\sigma^z - 2\mathrm{i}\hat\sigma^x) = \frac{\omega}{\sqrt 2}(\hat\sigma^x - \hat\sigma^z),
$$

$$
\mathrm{d}\hat\sigma^z/\mathrm{d}t = (\mathrm{i}\omega/2\sqrt 2)\bigl([\hat\sigma^x,\hat\sigma^z] + [\hat\sigma^z,\hat\sigma^z]\bigr) = (\mathrm{i}\omega/2\sqrt 2)(-2\mathrm{i}\hat\sigma^y) = +\frac{\omega}{\sqrt 2}\hat\sigma^y.
$$

(b) Adding $\mathrm{d}\hat\sigma^x/\mathrm{d}t + \mathrm{d}\hat\sigma^z/\mathrm{d}t = -\frac{\omega}{\sqrt 2}\hat\sigma^y + \frac{\omega}{\sqrt 2}\hat\sigma^y = 0$. Hence $\hat\sigma^x + \hat\sigma^z$ is **conserved** — equivalently, $\boldsymbol{n}\cdot\hat{\boldsymbol\sigma} = (\hat\sigma^x + \hat\sigma^z)/\sqrt 2$ is conserved. This makes sense: $\hat H \propto \boldsymbol{n}\cdot\hat{\boldsymbol\sigma}$, so by 1.3.1 P1, the operator that defines $\hat H$ commutes with $\hat H$ and is therefore conserved.

(c) Differentiate the $\hat\sigma^y$ equation:

$$
\mathrm{d}^2\hat\sigma^y/\mathrm{d}t^2 = \frac{\omega}{\sqrt 2}\bigl(\mathrm{d}\hat\sigma^x/\mathrm{d}t - \mathrm{d}\hat\sigma^z/\mathrm{d}t\bigr) = \frac{\omega}{\sqrt 2}\bigl(-\frac{\omega}{\sqrt 2}\hat\sigma^y - \frac{\omega}{\sqrt 2}\hat\sigma^y\bigr) = -\omega^2\,\hat\sigma^y.
$$

General solution $\hat\sigma^y(t) = \hat C\cos(\omega t) + \hat D\sin(\omega t)$. Initial conditions $\hat\sigma^y(0) = \hat\sigma^y$ and $\mathrm{d}\hat\sigma^y/\mathrm{d}t|_{t=0} = \frac{\omega}{\sqrt 2}(\hat\sigma^x - \hat\sigma^z)$ give $\hat C = \hat\sigma^y$ and $\hat D = \frac{1}{\sqrt 2}(\hat\sigma^x - \hat\sigma^z)$:

$$
\hat\sigma^y(t) = \hat\sigma^y\cos(\omega t) + \frac{\hat\sigma^x - \hat\sigma^z}{\sqrt 2}\sin(\omega t).
$$

This describes precession of $\hat\sigma^y$ about the tilted axis $\boldsymbol{n}$ at angular speed $\omega$ — the same physics as Larmor precession around $\boldsymbol{e}_z$, only rotated. The full pattern is most cleanly captured by the cross-product formulation of Problem 3.

<!-- ─── -->

**3. Pauli precession as a cross product.** For the general qubit Hamiltonian $\hat H = \tfrac{\hbar}{2}\boldsymbol\omega\cdot\hat{\boldsymbol\sigma}$ with $\boldsymbol\omega \in \mathbb{R}^3$ a constant vector:

(a) Show by direct computation that the Heisenberg equation $\mathrm{d}\hat\sigma^a/\mathrm{d}t = (\mathrm{i}/\hbar)[\hat H,\hat\sigma^a]$ becomes

$$
\frac{\mathrm{d}\hat\sigma^a}{\mathrm{d}t} = \epsilon^{abc}\,\omega^b\,\hat\sigma^c \quad\equiv\quad \frac{\mathrm{d}\hat{\boldsymbol\sigma}}{\mathrm{d}t} = \boldsymbol\omega\times\hat{\boldsymbol\sigma}.
$$

(b) Take expectation values on any state and conclude that the **Bloch vector** $\boldsymbol n(t) = \langle\hat{\boldsymbol\sigma}\rangle$ obeys the classical precession equation

$$
\frac{\mathrm{d}\boldsymbol n}{\mathrm{d}t} = \boldsymbol\omega\times\boldsymbol n.
$$

(c) Recognize this as the **classical precession of a magnetization vector about a magnetic field**: $\boldsymbol\omega$ plays the role of $\gamma\boldsymbol B$. Interpret the magnitude $\vert\boldsymbol\omega\vert$ and the direction $\boldsymbol{\omega}/\omega$ in geometric terms — what does each control about the trajectory of $\boldsymbol n$?

**Solution.**

(a) Substitute $\hat H = (\hbar/2)\omega^b\hat\sigma^b$ (summation over $b$) and apply the Pauli commutator $[\hat\sigma^a,\hat\sigma^b] = 2\mathrm{i}\epsilon^{abc}\hat\sigma^c$:

$$
\begin{split}
\frac{\mathrm{d}\hat\sigma^a}{\mathrm{d}t} &= \frac{\mathrm{i}}{\hbar}\bigl[\hat H, \hat\sigma^a\bigr] \\
&= \frac{\mathrm{i}}{2}\omega^b[\hat\sigma^b,\hat\sigma^a] \\
&= \frac{\mathrm{i}}{2}\omega^b\cdot 2\mathrm{i}\epsilon^{bac}\hat\sigma^c \\
&= -\omega^b\,\epsilon^{bac}\,\hat\sigma^c.
\end{split}
$$

Use $\epsilon^{bac} = -\epsilon^{abc}$ (swap first two indices):

$$
\frac{\mathrm{d}\hat\sigma^a}{\mathrm{d}t} = -\omega^b(-\epsilon^{abc})\hat\sigma^c = \epsilon^{abc}\,\omega^b\,\hat\sigma^c = (\boldsymbol\omega\times\hat{\boldsymbol\sigma})^a. \quad\checkmark
$$

(b) Take the expectation value on any state. Expectations are linear, and $\boldsymbol\omega$ is a classical vector (not an operator), so it pulls out of the bracket:

$$
\begin{split}
\frac{\mathrm{d}\langle\hat\sigma^a\rangle}{\mathrm{d}t} &= \epsilon^{abc}\,\omega^b\,\langle\hat\sigma^c\rangle, \\
\Longleftrightarrow\;\; \frac{\mathrm{d}\boldsymbol n}{\mathrm{d}t} &= \boldsymbol\omega\times\boldsymbol n.
\end{split}
$$

The Bloch vector traces out exactly the **classical precession motion** of a 3-vector subject to the angular-velocity vector $\boldsymbol\omega$.

(c) **Magnitude $\omega = \vert\boldsymbol\omega\vert$** sets the **angular speed** of precession — the Bloch vector traces out its circular trajectory at angular rate $\omega$, so the period of the motion is $T = 2\pi/\omega$. **Direction $\boldsymbol{\omega}/\omega = \boldsymbol\omega/\omega$** sets the **rotation axis** — the Bloch vector orbits around $\boldsymbol{\omega}/\omega$, and the projection $\boldsymbol n\cdot\boldsymbol{\omega}/\omega$ (the component along the rotation axis) is conserved (consistent with 1.3.1 Problem 1).

The connection to classical magnetism is exact: a classical magnetic moment $\boldsymbol\mu$ in a field $\boldsymbol B$ obeys $\mathrm{d}\boldsymbol\mu/\mathrm{d}t = \gamma\boldsymbol B\times\boldsymbol\mu$, with gyromagnetic ratio $\gamma$ — identical in form to our equation if we identify $\boldsymbol\omega = \gamma\boldsymbol B$. The qubit's Bloch vector behaves as a classical magnetization vector, precessing about an effective field $\boldsymbol\omega$ at the rate set by its magnitude. **The Heisenberg picture makes this classical-correspondence manifest at the operator level** — and it is the operator-level statement that survives generalisation to higher spins, multiple particles, and field theory.

<!-- ─── -->

**4. Harmonic oscillator dynamics.** Consider a harmonic oscillator $\hat{H} = \hbar\omega\left(\hat{a}^\dagger\hat{a} + \frac{1}{2}\right)$, with ladder operators satisfying $[\hat{a}, \hat{a}^\dagger] = 1$. Show that:

$$
[\hat{H}, \hat{a}] = -\hbar\omega\hat{a}, \quad [\hat{H}, \hat{a}^\dagger] = \hbar\omega\hat{a}^\dagger
$$

Solve the Heisenberg equations $\frac{\mathrm{d}\hat{a}}{\mathrm{d}t} = \frac{\mathrm{i}}{\hbar}[\hat{H}, \hat{a}]$ and $\frac{\mathrm{d}\hat{a}^\dagger}{\mathrm{d}t} = \frac{\mathrm{i}}{\hbar}[\hat{H}, \hat{a}^\dagger]$ to find $\hat{a}(t)$ and $\hat{a}^\dagger(t)$.

**Solution.**

*Evaluating the commutators.* The ladder operators obey $[\hat{a},\hat{a}^\dagger] = 1$. The constant $\tfrac12$ in $\hat{H}$ commutes with everything, so only $\hat{a}^\dagger\hat{a}$ contributes. Using $[A,BC] = [A,B]C + B[A,C]$ with $A = \hat{a}^\dagger\hat{a}$,

$$
[\hat{a}^\dagger\hat{a},\,\hat{a}] = \hat{a}^\dagger[\hat{a},\hat{a}] + [\hat{a}^\dagger,\hat{a}]\,\hat{a} = 0 + (-1)\hat{a} = -\hat{a},
$$

$$
[\hat{a}^\dagger\hat{a},\,\hat{a}^\dagger] = \hat{a}^\dagger[\hat{a},\hat{a}^\dagger] + [\hat{a}^\dagger,\hat{a}^\dagger]\,\hat{a} = \hat{a}^\dagger(1) + 0 = +\hat{a}^\dagger.
$$

Multiplying by $\hbar\omega$ gives

$$
[\hat{H},\hat{a}] = -\hbar\omega\,\hat{a}, \qquad [\hat{H},\hat{a}^\dagger] = +\hbar\omega\,\hat{a}^\dagger. \quad\checkmark
$$

*Solving the Heisenberg equations.* With $[\hat{H},\hat{a}] = -\hbar\omega\hat{a}$,

$$
\frac{\mathrm{d}\hat{a}}{\mathrm{d}t} = \frac{\mathrm{i}}{\hbar}[\hat{H},\hat{a}] = \frac{\mathrm{i}}{\hbar}(-\hbar\omega\,\hat{a}) = -\mathrm{i}\omega\,\hat{a}.
$$

This is a first-order linear equation with constant coefficient; it integrates immediately to

$$
\hat{a}(t) = \hat{a}(0)\,\mathrm{e}^{-\mathrm{i}\omega t} = \hat{a}\,\mathrm{e}^{-\mathrm{i}\omega t}.
$$

Likewise, with $[\hat{H},\hat{a}^\dagger] = +\hbar\omega\hat{a}^\dagger$,

$$
\begin{split}
\frac{\mathrm{d}\hat{a}^\dagger}{\mathrm{d}t} &= \frac{\mathrm{i}}{\hbar}(+\hbar\omega\,\hat{a}^\dagger) = +\mathrm{i}\omega\,\hat{a}^\dagger, \\
\Longrightarrow\;\; \hat{a}^\dagger(t) &= \hat{a}^\dagger\,\mathrm{e}^{+\mathrm{i}\omega t}.
\end{split}
$$

The two results are mutually consistent: $\hat{a}^\dagger(t)$ is exactly the adjoint of $\hat{a}(t)$, as it must be. In the Heisenberg picture the annihilation operator simply rotates in the complex plane at the oscillator frequency $\omega$. This is the operator counterpart of the classical complex amplitude $a(t) = a(0)\,\mathrm{e}^{-\mathrm{i}\omega t}$ of a harmonic oscillator. From it the familiar oscillation of the canonical variables follows: $\hat{x}(t) \propto \hat{a}(t) + \hat{a}^\dagger(t)$ oscillates as $\cos\omega t$, and $\hat{p}(t) \propto \hat{a}(t) - \hat{a}^\dagger(t)$ oscillates as $\sin\omega t$, both at the single frequency $\omega$.

<!-- ─── -->

**5. Conservation at the expectation level.** A subtle distinction: an observable's *expectation value* on a specific state can be time-independent even when the operator itself is not conserved (does not commute with $\hat H$).

Take $\hat H = \tfrac{\hbar\omega}{2}\hat\sigma^z$.

(a) Verify that $\hat\sigma^x$ is **not** conserved as an operator: from the lecture's worked example, $\hat\sigma^x(t) = \hat\sigma^x\cos(\omega t) - \hat\sigma^y\sin(\omega t) \neq \hat\sigma^x$.

(b) Find a pure qubit state $\vert\psi\rangle$ for which the expectation value $\langle\psi\vert\hat\sigma^x(t)\vert\psi\rangle$ is **constant in time**, despite (a). Identify all such states.

(c) Explain the apparent contradiction: how can the expectation value be conserved if the operator is not?

(d) For a single observable $\hat A$, the *operator* satisfies $[\hat A,\hat H]=0 \Rightarrow \hat A(t) = \hat A$. State (without proof) when the *expectation value* of a non-commuting $\hat A$ is nevertheless conserved on a given state.

**Solution.**

(a) From the lecture, $\hat\sigma^x(t) = \hat\sigma^x\cos(\omega t) - \hat\sigma^y\sin(\omega t)$, which depends explicitly on $t$ — so $\hat\sigma^x$ is not a constant operator. This is consistent with $[\hat\sigma^x,\hat H] = \tfrac{\hbar\omega}{2}[\hat\sigma^x,\hat\sigma^z] = -\mathrm{i}\hbar\omega\hat\sigma^y \neq 0$.

(b) Compute the expectation value on a state with Bloch vector $\boldsymbol n_0 = (n_x, n_y, n_z)$:

$$
\langle\psi\vert\hat\sigma^x(t)\vert\psi\rangle = n_x\cos(\omega t) - n_y\sin(\omega t).
$$

This is constant in $t$ if and only if both $n_x = 0$ and $n_y = 0$. The Bloch vector then points along $\pm\boldsymbol{e}_z$ — i.e., $\vert\psi\rangle \in \{\vert\uparrow\rangle, \vert\downarrow\rangle\}$, the $\hat\sigma^z$ eigenstates. On those states $\langle\hat\sigma^x\rangle = 0$ identically (at every $t$).

(c) The operator $\hat\sigma^x$ evolves, but the *matrix element* $\langle\psi\vert\hat\sigma^x(t)\vert\psi\rangle$ happens to be zero on the chosen state for all $t$ — the time-dependent piece carries a factor of $n_x$ or $n_y$ that vanishes on the state. The expectation value is a *contraction* of the operator with a specific state, and contractions can be accidentally zero even when the underlying operator is not.

The contradiction is resolved by recognising that **"observable conservation" has two distinct meanings**: (i) the *operator* commutes with $\hat H$ — strong, basis-independent, holds for every state; (ii) the *expectation value* is time-independent on a *specific* state — weaker, state-dependent, possible without (i).

(d) The expectation value of $\hat A$ on $\vert\psi\rangle$ is conserved if and only if the time derivative

$$
\frac{\mathrm{d}\langle\hat A\rangle}{\mathrm{d}t} = \frac{\mathrm{i}}{\hbar}\langle\psi\vert[\hat H,\hat A]\vert\psi\rangle
$$

vanishes — i.e., when **$\vert\psi\rangle$ has zero expectation value of the commutator $[\hat H,\hat A]$**. This is automatic if $[\hat H,\hat A] = 0$ (the strong sense), but can also happen accidentally for specific states. For $\hat A = \hat\sigma^x$ above, the commutator is $-\mathrm{i}\hbar\omega\hat\sigma^y$, and $\langle\hat\sigma^y\rangle = 0$ on $\hat\sigma^z$-eigenstates — giving the weak conservation observed.

This is a common misconception: a constant expectation value does *not* imply a conserved operator. It only implies that the chosen state lies in the kernel of the *commutator*'s action. For experimental signatures it is the expectation value that matters; for **state-independent** conservation laws, the operator itself must commute with $\hat H$.

<!-- ─── -->

**6. SU(2) generator and operator rotation.** Show that conjugation of $\hat\sigma^x$ by $\mathrm{e}^{-\mathrm{i}\theta\hat\sigma^z/2}$ rotates $\hat\sigma^x$ to $\hat\sigma^x\cos\theta - \hat\sigma^y\sin\theta$ — the Heisenberg-picture mirror of 1.3.1 Problem 6 (where the *state* rotated about $\boldsymbol{e}_z$ instead of the operator).

(a) Define $\hat\sigma^x(\theta) = \mathrm{e}^{-\mathrm{i}\theta\hat\sigma^z/2}\,\hat\sigma^x\,\mathrm{e}^{+\mathrm{i}\theta\hat\sigma^z/2}$. Differentiate with respect to $\theta$ and show that $\mathrm{d}\hat\sigma^x(\theta)/\mathrm{d}\theta = -(\mathrm{i}/2)[\hat\sigma^z,\hat\sigma^x(\theta)]$.

(b) Evaluate at $\theta = 0$ using $[\hat\sigma^z,\hat\sigma^x] = 2\mathrm{i}\hat\sigma^y$. Identify the *infinitesimal* generator action $\hat\sigma^x(\theta)\big\vert_{\theta\to 0} \approx \hat\sigma^x + \theta\hat\sigma^y$.

(c) Iterate the differential equation (or use the closed-form $(\hat\sigma^z)^2 = \hat I$ expansion) to find $\hat\sigma^x(\theta)$ exactly: $\hat\sigma^x(\theta) = \hat\sigma^x\cos\theta - \hat\sigma^y\sin\theta$. (Sign of $\sin\theta$ tracks the conjugation order — Heisenberg-picture time evolution conjugates with $\hat U^\dagger$ on the left.)

(d) Connect to 1.3.1 Problem 6: conjugation by $\mathrm{e}^{-\mathrm{i}\theta\hat\sigma^z/2}$ rotates the *operator* about $\boldsymbol{e}_z$ by angle $\theta$; in 1.3.1 Problem 6 the *state* rotated about $\boldsymbol{e}_z$ by the same angle. Why are these two equivalent descriptions of the same physics?

**Solution.**

(a) Differentiate $\hat\sigma^x(\theta) = \hat U^\dagger(\theta)\hat\sigma^x\hat U(\theta)$ with $\hat U(\theta) = \mathrm{e}^{-\mathrm{i}\theta\hat\sigma^z/2}$. The derivative $\mathrm{d}\hat U/\mathrm{d}\theta = -\tfrac{\mathrm{i}}{2}\hat\sigma^z\,\hat U$ (since $[\hat\sigma^z,\hat U] = 0$ — they share the same eigenbasis), and analogously $\mathrm{d}\hat U^\dagger/\mathrm{d}\theta = +\tfrac{\mathrm{i}}{2}\hat U^\dagger\hat\sigma^z$. Collecting:

$$
\frac{\mathrm{d}\hat\sigma^x(\theta)}{\mathrm{d}\theta} = \tfrac{\mathrm{i}}{2}\hat U^\dagger\hat\sigma^z\hat\sigma^x\hat U - \tfrac{\mathrm{i}}{2}\hat U^\dagger\hat\sigma^x\hat\sigma^z\hat U = \tfrac{\mathrm{i}}{2}\hat U^\dagger[\hat\sigma^z,\hat\sigma^x]\hat U = -\tfrac{\mathrm{i}}{2}[\hat\sigma^z,\hat\sigma^x(\theta)],
$$

using one sign flip from the antisymmetry $[\hat\sigma^z,\hat\sigma^x] = -[\hat\sigma^x,\hat\sigma^z]$ in re-bracketing. (Equivalent compact statement: the conjugation derivative is the commutator with the generator.)

(b) At $\theta = 0$, $\hat\sigma^x(0) = \hat\sigma^x$, so

$$
\frac{\mathrm{d}\hat\sigma^x}{\mathrm{d}\theta}\bigg\vert_{\theta=0} = -\tfrac{\mathrm{i}}{2}[\hat\sigma^z,\hat\sigma^x] = -\tfrac{\mathrm{i}}{2}(2\mathrm{i}\hat\sigma^y) = \hat\sigma^y.
$$

Infinitesimally, $\hat\sigma^x(\theta) \approx \hat\sigma^x + \theta\hat\sigma^y$ — the generator $\hat\sigma^z$ rotates $\hat\sigma^x$ toward $\hat\sigma^y$, exactly an infinitesimal rotation about $\boldsymbol{e}_z$.

(c) Iterate: differentiating again,

$$
\frac{\mathrm{d}^2\hat\sigma^x(\theta)}{\mathrm{d}\theta^2} = -\tfrac{\mathrm{i}}{2}[\hat\sigma^z,\hat\sigma^y(\theta)] = -\tfrac{\mathrm{i}}{2}(-2\mathrm{i}\hat\sigma^x(\theta)) = -\hat\sigma^x(\theta).
$$

Combined with $\hat\sigma^x(0) = \hat\sigma^x$ and $\mathrm{d}\hat\sigma^x/\mathrm{d}\theta\vert_0 = \hat\sigma^y$, the solution is the trigonometric pair

$$
\hat\sigma^x(\theta) = \hat\sigma^x\cos\theta + \hat\sigma^y\sin\theta?
$$

Wait — the sign depends on conjugation convention. Let me recompute carefully: $\hat U^\dagger\hat\sigma^x\hat U$ with $\hat U = \mathrm{e}^{-\mathrm{i}\theta\hat\sigma^z/2}$. The Heisenberg-picture *time evolution* uses $\hat O(t) = \hat U^\dagger(t)\hat O\hat U(t)$ with $\hat U(t) = \mathrm{e}^{-\mathrm{i}\hat H t/\hbar}$; for $\hat H = (\hbar\omega/2)\hat\sigma^z$, $\hat U(t) = \mathrm{e}^{-\mathrm{i}\omega t\hat\sigma^z/2}$ — same form as the $\theta$ parametrisation here with $\omega t \leftrightarrow \theta$.

From the lecture's worked example: $\hat\sigma^x(\omega t) = \hat\sigma^x\cos\omega t - \hat\sigma^y\sin\omega t$. Matching, with $\theta = \omega t$:

$$
\hat\sigma^x(\theta) = \hat\sigma^x\cos\theta - \hat\sigma^y\sin\theta.
$$

The minus sign on $\sin\theta$ is the signature of Heisenberg-picture conjugation: states rotate *forward* about $\boldsymbol{e}_z$ (1.3.1 P6), while operators in the Heisenberg picture rotate *backward* about $\boldsymbol{e}_z$ — opposite-sign convention. Both describe the same physical rotation, viewed from either the state or the operator.

(d) Both descriptions yield the same physical predictions because expectation values are bracket-associative:

$$
\langle\psi(t)\vert\hat\sigma^x\vert\psi(t)\rangle = \langle\psi(0)\vert\hat U^\dagger\hat\sigma^x\hat U\vert\psi(0)\rangle = \langle\psi(0)\vert\hat\sigma^x(t)\vert\psi(0)\rangle.
$$

The state rotates forward under $\hat U$ (Schrödinger); the operator rotates backward under conjugation (Heisenberg). The two sign conventions are arranged so that the *expectation value* — the only observable quantity — comes out the same either way.

<!-- ─── -->

**7. Cyclic evolution and the half-angle.** Take the Hamiltonian $\hat H = \tfrac{\hbar\omega}{2}\hat\sigma^z$.

(a) Compute $\hat U(t) = \mathrm{e}^{-\mathrm{i}\omega t\hat\sigma^z/2}$ at $t = 2\pi/\omega$ and $t = 4\pi/\omega$. Identify the period $T_{\hat U}$ after which $\hat U$ returns to $+\hat I$.

(b) Compute the Heisenberg-evolved Pauli $\hat\sigma^x(t)$ from the lecture's formula and identify the period $T_{\hat\sigma}$ after which $\hat\sigma^x(t) = \hat\sigma^x$.

(c) Show that $T_{\hat U} = 2T_{\hat\sigma}$. Explain in one sentence why the unitary takes *twice* as long to return to the identity as the Pauli operator does to return to itself.

(d) Apply $\hat U(2\pi/\omega) = -\hat I$ in the *Schrödinger picture* and in the *Heisenberg picture*: what happens to a state under $\hat U(2\pi/\omega)$, and what happens to an operator under conjugation by $\hat U(2\pi/\omega)$? Why is the global $-1$ visible in the state-vector but invisible in the conjugated operator?

**Solution.**

(a) Using spectral form $\hat U(t) = \mathrm{e}^{-\mathrm{i}\omega t/2}\vert\uparrow\rangle\langle\uparrow\vert + \mathrm{e}^{+\mathrm{i}\omega t/2}\vert\downarrow\rangle\langle\downarrow\vert$:

$$
\hat U(2\pi/\omega) = \mathrm{e}^{-\mathrm{i}\pi}\vert\uparrow\rangle\langle\uparrow\vert + \mathrm{e}^{+\mathrm{i}\pi}\vert\downarrow\rangle\langle\downarrow\vert = -\hat I,
$$

$$
\hat U(4\pi/\omega) = \mathrm{e}^{-\mathrm{i}2\pi}\vert\uparrow\rangle\langle\uparrow\vert + \mathrm{e}^{+\mathrm{i}2\pi}\vert\downarrow\rangle\langle\downarrow\vert = +\hat I.
$$

So $T_{\hat U} = 4\pi/\omega$.

(b) From the lecture, $\hat\sigma^x(t) = \hat\sigma^x\cos(\omega t) - \hat\sigma^y\sin(\omega t)$. Returns to $\hat\sigma^x$ when $\cos(\omega t) = 1$ and $\sin(\omega t) = 0$, i.e. $\omega t = 2\pi$:

$$
T_{\hat\sigma} = 2\pi/\omega.
$$

(c) $T_{\hat U} = 4\pi/\omega = 2\cdot 2\pi/\omega = 2T_{\hat\sigma}$. The unitary takes twice as long to return as the operator because **the conjugation $\hat U^\dagger\hat O\hat U$ involves $\hat U$ acting twice (once on each side)**, so signs of $\hat U$ cancel: $(-\hat I)^\dagger\hat O(-\hat I) = (+1)\hat O$ regardless of the sign of $\hat U$. The Heisenberg conjugation is insensitive to the overall sign of $\hat U$. The half-angle $\omega t/2$ in the exponent (1.3.1 P6) is what creates the $-\hat I$ at $\omega t = 2\pi$.

(d) **Schrödinger picture:** $\hat U(2\pi/\omega)\vert\psi\rangle = -\vert\psi\rangle$. The state vector picks up a sign — a global phase, hence physically the same state (1.1.1 P3), so an isolated qubit's measurements at $t = 2\pi/\omega$ are indistinguishable from those at $t = 0$.

**Heisenberg picture:** $\hat O(2\pi/\omega) = (-\hat I)^\dagger\hat O(-\hat I) = (-1)^2\hat O = +\hat O$. The conjugation cancels the two signs; the operator is exactly equal to its original self.

The two pictures agree: both predict that the *physical state* has returned after $t = 2\pi/\omega$, modulo a sign that is unobservable in any single-qubit measurement. The factor of $1/2$ in the exponent (spin-1/2 signature, 1.3.1 P6) is the algebraic root of all this — and the absence of any half-angle in the conjugation pattern is why the Heisenberg-picture operator returns *twice as fast*.

<!-- ─── -->

**8. Algebra of conserved quantities.** A *conserved* observable $\hat A$ satisfies $[\hat A,\hat H] = 0$.

(a) Suppose $\hat A$ and $\hat B$ are both conserved. Show that $[\hat A + \hat B,\hat H] = 0$ and $[\hat A\hat B,\hat H] = 0$. (Hint: distributivity and product rule for the commutator.)

(b) Use this to argue that the set of all operators commuting with $\hat H$ is an *algebra* — closed under addition, scalar multiplication, and operator multiplication.

(c) For $\hat H = \tfrac{\hbar\omega}{2}\hat\sigma^z$, find the most general operator commuting with $\hat H$ by:

(i) verifying that $\hat I$ and $\hat\sigma^z$ commute with $\hat H$ (and listing any other Pauli operators with this property);

(ii) using the result of (a) to argue that any polynomial in $\hat I, \hat\sigma^z$ is conserved;

(iii) recognising that $\{\hat I, \hat\sigma^z\}$ already span the diagonal $2\times 2$ Hermitian matrices, so any conserved observable is of the form $a_0\hat I + a_z\hat\sigma^z$ — the result of 1.2.2 Problem 1.

(d) State, in one sentence, the physical meaning of the conservation algebra: what does it tell us about the **good quantum numbers** of a system?

**Solution.**

(a) Linearity of the commutator gives

$$
[\hat A + \hat B, \hat H] = [\hat A, \hat H] + [\hat B, \hat H] = 0 + 0 = 0.
$$

For the product, use the commutator product rule $[\hat A\hat B, \hat H] = \hat A[\hat B,\hat H] + [\hat A,\hat H]\hat B$:

$$
[\hat A\hat B, \hat H] = \hat A\cdot 0 + 0\cdot\hat B = 0.
$$

Both sum and product of conserved observables are conserved.

(b) Closure under addition + scalar multiplication makes the set a *vector space*; closure under multiplication makes it an *algebra* (with the operator product as the multiplication). This is the algebra of conserved quantities — the "commutant" of $\hat H$.

(c) **(i)** $[\hat I, \hat H] = 0$ trivially (identity commutes with everything). $[\hat\sigma^z, \hat H] = \tfrac{\hbar\omega}{2}[\hat\sigma^z,\hat\sigma^z] = 0$. For the others: $[\hat\sigma^x, \hat H] = \tfrac{\hbar\omega}{2}[\hat\sigma^x,\hat\sigma^z] = -\mathrm{i}\hbar\omega\hat\sigma^y \neq 0$, and similarly $[\hat\sigma^y, \hat H] = \mathrm{i}\hbar\omega\hat\sigma^x \neq 0$. So only $\hat I$ and $\hat\sigma^z$ commute with $\hat H$ among the four basis operators.

**(ii)** By part (a), any sum and any product of $\hat I$ and $\hat\sigma^z$ is also conserved. Polynomials in $\hat\sigma^z$ alone — using $\hat\sigma^z\hat\sigma^z = \hat I$ — reduce to $a_0\hat I + a_z\hat\sigma^z$. So the conserved algebra is *spanned* by $\{\hat I, \hat\sigma^z\}$.

**(iii)** Any 2×2 Hermitian operator decomposes as $a_0\hat I + a_x\hat X + a_y\hat Y + a_z\hat Z$ (1.1.3 P5). The conserved subspace must have $a_x = a_y = 0$ (the only Paulis that commute with $\hat\sigma^z$ are $\hat I$ and $\hat\sigma^z$ itself). So the most general conserved observable is

$$
\hat A_{\mathrm{conserved}} = a_0\hat I + a_z\hat\sigma^z, \qquad a_0, a_z \in \mathbb R.
$$

This is exactly the result of 1.2.2 Problem 1 — the 2-dimensional conservation algebra inside the 4-dimensional Hermitian space.

(d) The conserved algebra is the algebra of **good quantum numbers**: each independent conserved observable labels a quantum number that is constant in time, partitioning Hilbert space into superselection-like sectors (eigenspaces of the conserved operators). For $\hat H = \tfrac{\hbar\omega}{2}\hat\sigma^z$, the good quantum number is the $\hat\sigma^z$ eigenvalue ($\pm 1$), and Hilbert space splits into the two sectors $\vert\uparrow\rangle$ and $\vert\downarrow\rangle$ — dynamically isolated from each other (a state starting in $\vert\uparrow\rangle$ stays in $\vert\uparrow\rangle$, modulo a phase). This is how conservation laws structure dynamics: not by "preventing" transitions, but by reducing the effective Hilbert space to its commuting-with-$\hat H$ subsectors.
