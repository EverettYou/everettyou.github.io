# 1.3.2 Schrödinger Picture
Worked solutions for the homework problems in the [1.3.2 Schrödinger Picture](../ch1_qubit/1-3-2-schrodinger-picture) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. General Bloch precession.** A qubit has Hamiltonian $\hat H = \tfrac{\hbar}{2}\,\boldsymbol\omega\cdot\hat{\boldsymbol\sigma}$ where $\boldsymbol\omega = (\omega_x, \omega_y, \omega_z)$ is a constant 3-vector with magnitude $\omega = \vert\boldsymbol\omega\vert$ and direction $\boldsymbol{\omega}/\omega = \boldsymbol\omega/\omega$.

(a) Using $(\hat{\boldsymbol n}\cdot\hat{\boldsymbol\sigma})^2 = \hat I$ from 1.1.3 Problem 7, show that the time-evolution operator has the closed form

$$
\hat U(t) = \cos(\omega t/2)\,\hat I - \mathrm{i}\sin(\omega t/2)\,(\boldsymbol{\omega}/\omega\cdot\hat{\boldsymbol\sigma}).
$$

(b) Using the result of 1.3.1 Problem 1 (conservation of observables commuting with $\hat H$), argue that $\langle\boldsymbol{\omega}/\omega\cdot\hat{\boldsymbol\sigma}\rangle$ is conserved in time on every state. Conclude that the Bloch vector's projection onto the rotation axis $\boldsymbol{\omega}/\omega$ is constant — the Bloch trajectory lies on a cone around $\boldsymbol{\omega}/\omega$.

(c) Verify two specializations of this picture against the lecture's worked examples: (i) $\boldsymbol\omega = \omega_0\boldsymbol{e}_z$ reproduces Larmor precession of the Bloch vector about $\boldsymbol{e}_z$ at angular speed $\omega_0$; (ii) $\boldsymbol\omega = \Omega\boldsymbol{e}_x$ reproduces resonant Rabi rotation about $\boldsymbol{e}_x$ at angular speed $\Omega$. State the rotation axis and angular speed in each case.

**Solution.**

(a) Set $\hat A = \boldsymbol{\omega}/\omega\cdot\hat{\boldsymbol\sigma}$ in the Hamiltonian: $\hat H = \tfrac{\hbar\omega}{2}\hat A$. Since $\hat A^2 = \hat I$ (1.1.3 P7), the Taylor series of $\hat U(t) = \mathrm{e}^{-\mathrm{i}\hat H t/\hbar} = \mathrm{e}^{-\mathrm{i}(\omega t/2)\hat A}$ splits into even and odd powers, exactly as in 1.3.1 Problem 2:

$$
\hat U(t) = \cos(\omega t/2)\,\hat I - \mathrm{i}\sin(\omega t/2)\,\hat A = \cos(\omega t/2)\,\hat I - \mathrm{i}\sin(\omega t/2)\,(\boldsymbol{\omega}/\omega\cdot\hat{\boldsymbol\sigma}).
$$

(b) The Hamiltonian is built from $\boldsymbol{\omega}/\omega\cdot\hat{\boldsymbol\sigma}$ (with a scalar prefactor), so it commutes with itself: $[\boldsymbol{\omega}/\omega\cdot\hat{\boldsymbol\sigma},\hat H] = 0$. By 1.3.1 Problem 1, the expectation value $\langle\boldsymbol{\omega}/\omega\cdot\hat{\boldsymbol\sigma}\rangle = \boldsymbol{\omega}/\omega\cdot\boldsymbol n$ is conserved on every state. The component of the Bloch vector along $\boldsymbol{\omega}/\omega$ stays fixed, so the trajectory lies in a plane perpendicular to $\boldsymbol{\omega}/\omega$ (a circle once the magnitude is fixed by $\vert\boldsymbol n\vert$). The full Bloch motion is **uniform rotation about $\boldsymbol{\omega}/\omega$ at angular speed $\omega$** — this can be verified by direct computation (Problem 2 does the $\boldsymbol{\omega}/\omega = \boldsymbol{e}_z$ case from a non-trivial starting state).

(c) **Specialization (i):** $\boldsymbol\omega = \omega_0\boldsymbol{e}_z$. The Hamiltonian is $\hat H = \tfrac{\hbar\omega_0}{2}\hat Z$, the lecture's static-field example. The Bloch vector rotates about $\boldsymbol{e}_z$ at angular speed $\omega_0$ — Larmor precession, as the lecture's "Bloch Vector Motion" calculation shows for the special initial state $\vert+\rangle$ (Problem 2 below repeats this for $\vert\mathrm{i}\rangle$).

**Specialization (ii):** $\boldsymbol\omega = \Omega\boldsymbol{e}_x$. The Hamiltonian is $\hat H = \tfrac{\hbar\Omega}{2}\hat X$, the lecture's resonant Rabi Hamiltonian (after the rotating-wave approximation). The Bloch vector rotates about $\boldsymbol{e}_x$ at angular speed $\Omega$. Starting from $\vert 0\rangle$ (north pole), this sweeps the Bloch vector down through $-\boldsymbol{e}_y$ at $\Omega t = \pi/2$, to $\vert 1\rangle$ (south pole) at $\Omega t = \pi$, and back — the lecture's population transfer formula $P_1(t) = \sin^2(\Omega t/2)$.

The unified statement: **any Hamiltonian of the form $\tfrac{\hbar}{2}\boldsymbol\omega\cdot\hat{\boldsymbol\sigma}$ is a Bloch rotation about $\boldsymbol{\omega}/\omega$ at speed $\omega$**. Larmor (along $\boldsymbol{e}_z$) and resonant Rabi (along $\boldsymbol{e}_x$) are the same physics in different orientations.

<!-- ─── -->

**2. Larmor evolution of a Y-basis eigenstate.** The lecture computes Larmor evolution starting from the $\hat X$ eigenstate $\vert+\rangle$. Repeat the computation with the same Hamiltonian $\hat H = \tfrac{\hbar\omega_0}{2}\hat Z$ but starting from the $\hat Y$ eigenstate

$$
\vert\mathrm{i}\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle + \mathrm{i}\vert 1\rangle).
$$

(a) Compute $\vert\psi(t)\rangle$.

(b) Compute the three Pauli expectation values $\langle\hat X\rangle(t),\,\langle\hat Y\rangle(t),\,\langle\hat Z\rangle(t)$, and identify the Bloch trajectory.

(c) Compare with the lecture's $\vert+\rangle$ initial-condition result: $\boldsymbol n_+(t) = (\cos\omega_0 t,\,\sin\omega_0 t,\,0)$. What's the same? What's the geometric difference between the two trajectories?

(d) Find the first time $t^*$ at which the Bloch vector reaches $-\boldsymbol{e}_x$, and identify the physical fraction of a Larmor period this represents.

**Solution.**

(a) The states $\vert 0\rangle,\vert 1\rangle$ are eigenstates of $\hat Z$ with eigenvalues $\pm 1$, so $\hat U(t) = \mathrm{e}^{-\mathrm{i}\omega_0 t\hat Z/2}$ multiplies each by its own phase:

$$
\vert\psi(t)\rangle = \tfrac{1}{\sqrt 2}\bigl(\mathrm{e}^{-\mathrm{i}\omega_0 t/2}\vert 0\rangle + \mathrm{i}\,\mathrm{e}^{+\mathrm{i}\omega_0 t/2}\vert 1\rangle\bigr).
$$

(b) With $c_0 = \tfrac{1}{\sqrt 2}\mathrm{e}^{-\mathrm{i}\omega_0 t/2}$ and $c_1 = \tfrac{\mathrm{i}}{\sqrt 2}\mathrm{e}^{+\mathrm{i}\omega_0 t/2}$, the cross term is

$$
c_0^* c_1 = \tfrac{1}{\sqrt 2}\mathrm{e}^{+\mathrm{i}\omega_0 t/2}\cdot\tfrac{\mathrm{i}}{\sqrt 2}\mathrm{e}^{+\mathrm{i}\omega_0 t/2} = \tfrac{\mathrm{i}}{2}\mathrm{e}^{\mathrm{i}\omega_0 t}.
$$

Using $\langle\hat X\rangle = 2\mathrm{Re}(c_0^*c_1)$, $\langle\hat Y\rangle = 2\mathrm{Im}(c_0^*c_1)$:

$$
\langle\hat X\rangle(t) = 2\mathrm{Re}\!\left[\tfrac{\mathrm{i}}{2}\mathrm{e}^{\mathrm{i}\omega_0 t}\right] = -\sin(\omega_0 t),
$$

$$
\langle\hat Y\rangle(t) = 2\mathrm{Im}\!\left[\tfrac{\mathrm{i}}{2}\mathrm{e}^{\mathrm{i}\omega_0 t}\right] = \cos(\omega_0 t),
$$

$$
\langle\hat Z\rangle(t) = \vert c_0\vert^2 - \vert c_1\vert^2 = \tfrac{1}{2} - \tfrac{1}{2} = 0.
$$

The Bloch trajectory is $\boldsymbol n_{\mathrm{i}}(t) = (-\sin\omega_0 t,\,\cos\omega_0 t,\,0)$ — also confined to the equatorial plane.

(c) Same as the lecture's $\vert+\rangle$ case: both trajectories lie in the equatorial ($xy$) plane, rotate counterclockwise about $\boldsymbol{e}_z$ at angular speed $\omega_0$, and have $\langle\hat Z\rangle = 0$ throughout. The difference is the **starting point**: the $\vert+\rangle$ case starts at $+\boldsymbol{e}_x$, the $\vert\mathrm{i}\rangle$ case starts at $+\boldsymbol{e}_y$. The two trajectories are related by an $\boldsymbol{e}_z$-axis rotation by $90^\circ$:

$$
\boldsymbol n_{\mathrm{i}}(t) = \boldsymbol n_+(t + \pi/2\omega_0),
$$

i.e. the $\vert\mathrm{i}\rangle$ trajectory is the $\vert+\rangle$ trajectory phase-shifted by a quarter period. Geometrically: rotating the *initial condition* by $90^\circ$ rotates the entire subsequent trajectory by the same $90^\circ$ — a direct consequence of the linearity of $\hat U(t)$.

(d) From part (b), $\boldsymbol n_{\mathrm{i}}(t)$ reaches $-\boldsymbol{e}_x$ when $-\sin\omega_0 t = -1$ and $\cos\omega_0 t = 0$, i.e. $\omega_0 t = \pi/2$:

$$
t^* = \frac{\pi}{2\omega_0} = \frac{T_{\mathrm{Larmor}}}{4},
$$

a **quarter** of the Larmor period $T_{\mathrm{Larmor}} = 2\pi/\omega_0$. The state has rotated $90^\circ$ from its initial $+\boldsymbol{e}_y$ orientation.

<!-- ─── -->

**3. Survival probability.** For a system with Hamiltonian $\hat H$ and initial state $\vert\psi_0\rangle$, the **survival probability** is

$$
P_s(t) = \vert\langle\psi_0\vert\psi(t)\rangle\vert^2.
$$

(a) Expand $\vert\psi_0\rangle = \sum_n c_n\vert E_n\rangle$ in energy eigenstates. Show that

$$
\langle\psi_0\vert\psi(t)\rangle = \sum_n \vert c_n\vert^2\,\mathrm{e}^{-\mathrm{i}E_n t/\hbar}.
$$

(b) Specialise to a two-level system with eigenvalues $E_\pm = \pm\Delta$, and initial state $\vert\psi_0\rangle = \cos(\theta_0/2)\vert E_+\rangle + \sin(\theta_0/2)\vert E_-\rangle$ (real coefficients). Compute $P_s(t)$ in closed form.

(c) For what initial states does the survival probability oscillate between $1$ and $0$? For what initial states is $P_s(t) = 1$ identically? Identify the angular frequency of the survival oscillation.

(d) Briefly interpret physically: $P_s(t)$ measures how much the evolved state has rotated away from its starting direction. What does the minimum survival probability $1 - \sin^2\theta_0$ tell us about the "distance" between $\vert\psi_0\rangle$ and the (orthogonal) state reached at the worst point of the oscillation?

**Solution.**

(a) Expand and use $\hat U(t)\vert E_n\rangle = \mathrm{e}^{-\mathrm{i}E_n t/\hbar}\vert E_n\rangle$:

$$
\vert\psi(t)\rangle = \sum_n c_n\,\mathrm{e}^{-\mathrm{i}E_n t/\hbar}\vert E_n\rangle.
$$

Take the inner product with $\vert\psi_0\rangle = \sum_m c_m\vert E_m\rangle$, using orthonormality $\langle E_m\vert E_n\rangle = \delta_{mn}$:

$$
\langle\psi_0\vert\psi(t)\rangle = \sum_{m,n} c_m^*c_n\,\mathrm{e}^{-\mathrm{i}E_n t/\hbar}\delta_{mn} = \sum_n \vert c_n\vert^2\,\mathrm{e}^{-\mathrm{i}E_n t/\hbar}.
$$

The survival amplitude is the energy-population-weighted sum of phase factors $\mathrm{e}^{-\mathrm{i}E_n t/\hbar}$.

(b) With $\vert c_+\vert^2 = \cos^2(\theta_0/2)$ and $\vert c_-\vert^2 = \sin^2(\theta_0/2)$, and $E_\pm = \pm\Delta$:

$$
\langle\psi_0\vert\psi(t)\rangle = \cos^2(\theta_0/2)\mathrm{e}^{-\mathrm{i}\Delta t/\hbar} + \sin^2(\theta_0/2)\mathrm{e}^{+\mathrm{i}\Delta t/\hbar}.
$$

Use Euler's formula to split the two exponentials:

$$
= \cos(\Delta t/\hbar)\bigl[\cos^2(\theta_0/2) + \sin^2(\theta_0/2)\bigr] - \mathrm{i}\sin(\Delta t/\hbar)\bigl[\cos^2(\theta_0/2) - \sin^2(\theta_0/2)\bigr]
$$

$$
= \cos(\Delta t/\hbar) - \mathrm{i}\sin(\Delta t/\hbar)\cos\theta_0.
$$

Modulus squared:

$$
P_s(t) = \cos^2(\Delta t/\hbar) + \sin^2(\Delta t/\hbar)\cos^2\theta_0 = 1 - \sin^2(\Delta t/\hbar)\,\sin^2\theta_0.
$$

(c) Inspecting the closed form:

- **Constant $P_s = 1$:** requires $\sin^2\theta_0 = 0$, i.e. $\theta_0 = 0$ or $\pi$. These are the eigenstates $\vert E_+\rangle$ and $\vert E_-\rangle$ themselves — stationary states that never leave their starting direction (consistent with the lecture's claim that energy eigenstates evolve by only a phase).
- **Oscillates between $1$ and $0$:** requires $\sin^2\theta_0 = 1$, i.e. $\theta_0 = \pi/2$. This is the equal-weight superposition $\vert\psi_0\rangle = \tfrac{1}{\sqrt 2}(\vert E_+\rangle + \vert E_-\rangle)$ — at peak departure, the evolved state is **orthogonal** to the starting state.

The oscillation frequency: $\sin^2(\Delta t/\hbar) = \tfrac{1}{2}(1 - \cos(2\Delta t/\hbar))$, so the survival probability oscillates at angular frequency

$$
\omega_{21} = \frac{2\Delta}{\hbar} = \frac{E_+ - E_-}{\hbar},
$$

the transition frequency between the two energy levels (cf. 1.3.1 P7).

(d) At the minimum, $P_s = 1 - \sin^2\theta_0 = \cos^2\theta_0 = \vert\langle E_+\vert\psi_0\rangle - \langle E_-\vert\psi_0\rangle\vert^2/(\ldots)$ — equivalently, $P_s^{\mathrm{min}}$ is the squared overlap between $\vert\psi_0\rangle$ and its phase-flipped partner $\cos(\theta_0/2)\vert E_+\rangle - \sin(\theta_0/2)\vert E_-\rangle$. When $\theta_0 = \pi/2$ (equal-weight superposition) this overlap is **zero** — the two states are orthogonal, and the dynamics swings the qubit from $\vert\psi_0\rangle$ to a perfectly distinguishable partner state, then back. The further the initial state from an energy eigenstate, the deeper the survival dip; the closer to an eigenstate, the shallower the dip.

<!-- ─── -->

**4. Two-pulse phase-accumulation sequence.** Apply the following three-step sequence to the initial state $\vert\psi(0)\rangle = \vert 0\rangle$:

1. A Rabi $\pi/2$-pulse: $\hat U_1 = \cos(\pi/4)\hat I - \mathrm{i}\sin(\pi/4)\hat X$.
2. Free evolution under $\hat H_0 = \tfrac{\hbar\omega_0}{2}\hat Z$ for time $T$: $\hat U_2(T) = \mathrm{e}^{-\mathrm{i}\omega_0 T\hat Z/2}$.
3. A second Rabi $\pi/2$-pulse, identical to step 1.

(a) Compute the state after each of the three steps.

(b) Show that $P_1$ — the probability of finding the qubit in $\vert 1\rangle$ at the end — is

$$
P_1(T) = \cos^2(\omega_0 T/2).
$$

(c) The free-evolution stage accumulated only an *unobservable* phase (it acts trivially on populations in the $\hat Z$ basis), yet the final $P_1$ depends on $T$. Explain how the two $\pi/2$-pulses *convert* the phase $\omega_0 T$ into a measurable population oscillation.

(d) Use this principle to estimate the precision with which the level splitting $\omega_0$ can be measured by varying $T$ and counting the population. Compare with measuring $\omega_0$ directly from a single Larmor precession (which would require measuring $\langle\hat X\rangle$ at one fixed time).

**Solution.**

(a) **Step 1.** Apply $\hat U_1 = \tfrac{1}{\sqrt 2}(\hat I - \mathrm{i}\hat X)$ to $\vert 0\rangle$:

$$
\vert\psi_1\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle - \mathrm{i}\vert 1\rangle).
$$

Bloch vector $-\boldsymbol{e}_y$ — the equator state $\vert\bar{\mathrm{i}}\rangle$.

**Step 2.** Apply $\hat U_2(T) = \mathrm{diag}(\mathrm{e}^{-\mathrm{i}\omega_0 T/2}, \mathrm{e}^{+\mathrm{i}\omega_0 T/2})$:

$$
\vert\psi_2\rangle = \tfrac{1}{\sqrt 2}\bigl(\mathrm{e}^{-\mathrm{i}\omega_0 T/2}\vert 0\rangle - \mathrm{i}\,\mathrm{e}^{+\mathrm{i}\omega_0 T/2}\vert 1\rangle\bigr) = \tfrac{\mathrm{e}^{-\mathrm{i}\omega_0 T/2}}{\sqrt 2}\bigl(\vert 0\rangle - \mathrm{i}\,\mathrm{e}^{\mathrm{i}\omega_0 T}\vert 1\rangle\bigr).
$$

The free evolution has added the relative phase $\mathrm{e}^{\mathrm{i}\omega_0 T}$ — the Bloch vector has rotated $\omega_0 T$ about $\boldsymbol{e}_z$, sweeping from $-\boldsymbol{e}_y$ to $(\sin\omega_0 T,\,-\cos\omega_0 T,\,0)$. Populations are unchanged ($P_0 = P_1 = 1/2$ throughout).

**Step 3.** Apply $\hat U_1$ again. Drop the global phase $\mathrm{e}^{-\mathrm{i}\omega_0 T/2}$ — it does not affect $P_1$. Using $\hat U_1\vert 0\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle - \mathrm{i}\vert 1\rangle)$ and $\hat U_1\vert 1\rangle = \tfrac{1}{\sqrt 2}(-\mathrm{i}\vert 0\rangle + \vert 1\rangle)$,

$$
\vert\psi_3\rangle \propto \tfrac{1}{2}\bigl[\vert 0\rangle - \mathrm{i}\vert 1\rangle - \mathrm{i}\,\mathrm{e}^{\mathrm{i}\omega_0 T}(-\mathrm{i}\vert 0\rangle + \vert 1\rangle)\bigr] = \tfrac{1}{2}\bigl[(1 - \mathrm{e}^{\mathrm{i}\omega_0 T})\vert 0\rangle - \mathrm{i}(1 + \mathrm{e}^{\mathrm{i}\omega_0 T})\vert 1\rangle\bigr].
$$

(b) The $\vert 1\rangle$ amplitude has modulus

$$
\vert\langle 1\vert\psi_3\rangle\vert = \tfrac{1}{2}\vert 1 + \mathrm{e}^{\mathrm{i}\omega_0 T}\vert.
$$

Using $\vert 1 + \mathrm{e}^{\mathrm{i}\phi}\vert^2 = 2 + 2\cos\phi = 4\cos^2(\phi/2)$:

$$
P_1(T) = \tfrac{1}{4}\cdot 4\cos^2(\omega_0 T/2) = \cos^2(\omega_0 T/2). \quad\checkmark
$$

$P_1$ oscillates between $1$ (at $T = 0, 2\pi/\omega_0, \ldots$) and $0$ (at $T = \pi/\omega_0, 3\pi/\omega_0, \ldots$) as $T$ is varied.

(c) The first $\pi/2$-pulse rotates the Bloch vector from $+\boldsymbol{e}_z$ down to $-\boldsymbol{e}_y$ — an *equator* state that has equal populations of $\vert 0\rangle$ and $\vert 1\rangle$ but a definite relative phase. During free evolution, the equator state spins about $\boldsymbol{e}_z$, *winding* its relative phase at rate $\omega_0$ — invisible to any Z-basis population measurement, but stored in the phase. The second $\pi/2$-pulse converts that wound-up phase **back into a population**: rotating the equator state back through $\boldsymbol{e}_z$ depends on which point of the equator it was at when the second pulse fired, and that depends on the accumulated phase $\omega_0 T$. The $\pi/2$ pulses are *phase-to-population* transducers; the free evolution between them is the phase-accumulation stage.

(d) The fringe spacing (one full oscillation of $P_1$) corresponds to $\omega_0 \Delta T = 2\pi$. By varying $T$ and recording the fringe positions, $\omega_0$ can be measured to a precision limited by how accurately the fringe-period $2\pi/\omega_0$ can be timed — typically the resolution of the time delay $T$, not of any single-shot quantum measurement. For a single-shot Larmor measurement at fixed $t$, the precision is limited by the inverse square root of the number of samples (since $\langle\hat X\rangle$ must be statistically estimated). The phase-accumulation strategy is far more precise: by letting the phase accumulate for a long $T$ before reading it out, very small frequency uncertainties produce large counted-fringe differences. This is the principle behind extremely precise frequency standards.

<!-- ─── -->

**5. Pi-pulse implements the NOT gate.** From the lecture, the Rabi evolution operator is $\hat U(t) = \cos(\Omega t/2)\hat I - \mathrm{i}\sin(\Omega t/2)\hat X$.

(a) Evaluate $\hat U(\pi/\Omega)$ and show $\hat U(\pi/\Omega) = -\mathrm{i}\hat X$.

(b) Apply $\hat U(\pi/\Omega)$ to each of $\vert 0\rangle$, $\vert 1\rangle$, $\vert+\rangle$, and $\vert-\rangle$. For each input, identify the output and confirm it equals $\hat X$ applied to that state (up to a global phase $-\mathrm{i}$).

(c) Compute $\hat U(2\pi/\Omega)$. Show that the result is $-\hat I$, not $+\hat I$. Reference 1.3.1 Problem 6: explain why the half-angle $\Omega t/2$ in the exponent produces this sign, and why the $-\hat I$ is unobservable for a single qubit but can become physical in interferometric setups built later.

**Solution.**

(a) At $t = \pi/\Omega$, the half-angle is $\Omega t/2 = \pi/2$, so $\cos(\pi/2) = 0$ and $\sin(\pi/2) = 1$:

$$
\hat U(\pi/\Omega) = 0\cdot\hat I - \mathrm{i}\cdot 1\cdot\hat X = -\mathrm{i}\hat X.
$$

(b) Action of $-\mathrm{i}\hat X$ on each input, using $\hat X\vert 0\rangle = \vert 1\rangle$, $\hat X\vert 1\rangle = \vert 0\rangle$, $\hat X\vert\pm\rangle = \pm\vert\pm\rangle$:

$$
\vert 0\rangle \to -\mathrm{i}\vert 1\rangle, \quad \vert 1\rangle \to -\mathrm{i}\vert 0\rangle, \quad \vert+\rangle \to -\mathrm{i}\vert+\rangle, \quad \vert-\rangle \to +\mathrm{i}\vert-\rangle.
$$

In each case the output equals $\hat X$ applied to the input, multiplied by the global phase $-\mathrm{i}$ (which is $-\mathrm{i}\cdot\hat X\vert\psi\rangle = -\mathrm{i}\,\hat X\vert\psi\rangle$, and for the $\hat X$ eigenstates with $\hat X\vert\pm\rangle = \pm\vert\pm\rangle$, the eigenvalue $\pm 1$ rides along giving $\mp\mathrm{i}\vert\pm\rangle$).

**Population check.** Starting from $\vert 0\rangle$, the final state is $-\mathrm{i}\vert 1\rangle$, so $P_1 = \vert{-\mathrm{i}}\vert^2 = 1$ — complete population inversion. This is the lecture's "$\pi$-pulse: complete inversion." The action of the pulse on $\vert 0\rangle/\vert 1\rangle$ states is *bit-flip* (the NOT gate); on the $\hat X$-eigenstates $\vert\pm\rangle$ the bit-flip leaves them invariant (those are the rotation axis of the $\pi$-pulse). The global phase $-\mathrm{i}$ is unobservable on a single qubit (1.1.1 Problem 3).

(c) At $t = 2\pi/\Omega$, the half-angle is $\Omega t/2 = \pi$, so $\cos\pi = -1$ and $\sin\pi = 0$:

$$
\hat U(2\pi/\Omega) = -\hat I.
$$

A *full* Rabi cycle returns the populations to their original values ($P_1 = \sin^2\pi = 0$), but the **state vector** acquires the sign $-1$ — exactly the situation analysed in 1.3.1 Problem 6. The half-angle $\Omega t/2$ in the exponent means a full Bloch-sphere rotation ($\Omega t = 2\pi$) is only *half* a cycle in the unitary's exponent, leaving $\hat U = -\hat I$ rather than $+\hat I$. The minus sign is a global phase, invisible to single-qubit measurements, but in a setup where this qubit is part of an interferometric superposition with a reference path, the global sign becomes a *relative* phase against the reference and IS observable — the empirical signature of the half-angle convention. A genuine return to the identity requires $\Omega t = 4\pi$, i.e. *two* full Bloch revolutions: $\hat U(4\pi/\Omega) = +\hat I$.

<!-- ─── -->

**6. Sequential pulses about different axes.** Two pulse sequences are applied to the initial state $\vert 0\rangle$:

- **Sequence A.** First a $\pi/2$-pulse about $\boldsymbol{e}_x$ ($\hat R_x = \tfrac{1}{\sqrt 2}(\hat I - \mathrm{i}\hat X)$), then a $\pi/2$-pulse about $\boldsymbol{e}_z$ ($\hat R_z = \tfrac{1}{\sqrt 2}(\hat I - \mathrm{i}\hat Z)$).
- **Sequence B.** The same two pulses in the opposite order: $\hat R_z$ first, then $\hat R_x$.

(a) Compute the final state under sequence A.

(b) Compute the final state under sequence B.

(c) Identify the Bloch vector for each final state. What is the angle between the two final Bloch directions?

(d) Conclude: rotations about different axes do **not** commute as quantum gates. Why does this matter for the construction of arbitrary qubit operations?

**Solution.**

(a) Sequence A. Step 1: $\hat R_x\vert 0\rangle = \tfrac{1}{\sqrt 2}(\vert 0\rangle - \mathrm{i}\vert 1\rangle)$ (Bloch vector $-\boldsymbol{e}_y$, state $\vert\bar{\mathrm{i}}\rangle$).

Step 2: $\hat R_z$ on this. Using $\hat R_z\vert 0\rangle = \tfrac{1-\mathrm{i}}{\sqrt 2}\vert 0\rangle$ and $\hat R_z\vert 1\rangle = \tfrac{1+\mathrm{i}}{\sqrt 2}\vert 1\rangle$:

$$
\hat R_z\hat R_x\vert 0\rangle = \tfrac{1}{\sqrt 2}\!\left[\tfrac{1-\mathrm{i}}{\sqrt 2}\vert 0\rangle - \mathrm{i}\cdot\tfrac{1+\mathrm{i}}{\sqrt 2}\vert 1\rangle\right] = \tfrac{1}{2}\bigl[(1-\mathrm{i})\vert 0\rangle - \mathrm{i}(1+\mathrm{i})\vert 1\rangle\bigr] = \tfrac{1}{2}\bigl[(1-\mathrm{i})\vert 0\rangle + (1-\mathrm{i})\vert 1\rangle\bigr] = \tfrac{1-\mathrm{i}}{\sqrt 2}\vert+\rangle.
$$

(Using $-\mathrm{i}(1+\mathrm{i}) = -\mathrm{i} - \mathrm{i}^2 = 1-\mathrm{i}$.) Final state: $\vert+\rangle$ (up to global phase $\mathrm{e}^{-\mathrm{i}\pi/4} = (1-\mathrm{i})/\sqrt 2$). Bloch vector $+\boldsymbol{e}_x$.

(b) Sequence B. Step 1: $\hat R_z\vert 0\rangle = \tfrac{1-\mathrm{i}}{\sqrt 2}\vert 0\rangle$ — only a global phase, Bloch vector stays at $+\boldsymbol{e}_z$. (Rotation about $\boldsymbol{e}_z$ fixes $\boldsymbol{e}_z$-eigenstates.)

Step 2: $\hat R_x$ on $\tfrac{1-\mathrm{i}}{\sqrt 2}\vert 0\rangle = \tfrac{1-\mathrm{i}}{\sqrt 2}\cdot\tfrac{1}{\sqrt 2}(\vert 0\rangle - \mathrm{i}\vert 1\rangle) = \tfrac{1-\mathrm{i}}{2}(\vert 0\rangle - \mathrm{i}\vert 1\rangle)$. Up to global phase, this is $\vert\bar{\mathrm{i}}\rangle$. Bloch vector $-\boldsymbol{e}_y$.

(c) Final Bloch vectors: $\boldsymbol n_A = +\boldsymbol{e}_x$, $\boldsymbol n_B = -\boldsymbol{e}_y$. The angle between them is $90^\circ$ — they are **orthogonal**. The two sequences send $\vert 0\rangle$ to physically distinguishable states.

(d) Rotation about $\boldsymbol{e}_x$ does not commute with rotation about $\boldsymbol{e}_z$: $\hat R_x\hat R_z \neq \hat R_z\hat R_x$. This is the operator-level signature of the non-commutativity $[\hat X, \hat Z] \neq 0$ from 1.2.2.

**Why this matters for gate construction.** If all qubit rotations commuted, then composing pulses about $\boldsymbol{e}_x$ and $\boldsymbol{e}_z$ would produce only $\hat I$-axis rotations — a one-parameter set. The non-commutativity is exactly what makes pulse sequences cover the full 3-parameter set of single-qubit rotations: any element of the rotation group can be built by composing rotations about two non-parallel axes (the **Euler decomposition**). A controllable Hamiltonian along $\boldsymbol{e}_x$ plus a controllable Hamiltonian along $\boldsymbol{e}_z$ — exactly what the lecture's static field and resonant drive provide — gives complete control over single-qubit gates. Non-commutativity is *necessary* for universal control, not a bug.

<!-- ─── -->

**7. Larmor precession vs Rabi oscillation.** Compare Larmor precession (static field $B_0$ along $\boldsymbol{e}_z$) and Rabi oscillation (resonant drive along $\boldsymbol{e}_x$ in the rotating frame).

(a) In what sense are both Bloch-sphere rotations? Identify the rotation axis and angular speed for each.

(b) Larmor precession occurs even with no external control — it is the *free* evolution of a qubit in a static field. Rabi oscillation requires an *applied* resonant drive. State, in one sentence, why a static field alone (Larmor) cannot drive population transfer between $\vert 0\rangle$ and $\vert 1\rangle$, whereas a resonant drive (Rabi) can.

(c) The two rotations have very different angular speeds in typical experiments: $\omega_0 \gg \Omega$. Describe the physical separation of these scales — what does $\omega_0$ measure, and what does $\Omega$ measure? Why is the small-$\Omega$ limit ($\Omega \ll \omega_0$) the regime in which the rotating-wave approximation is justified?

**Solution.**

(a) Both evolution operators have the form $\mathrm{e}^{-\mathrm{i}\boldsymbol{n}\cdot\hat{\boldsymbol\sigma}\,\theta/2}$ — by Problem 1, a rotation of the Bloch vector about $\boldsymbol{n}$ at angular speed $\dot\theta$:

$$
\hat U_{\mathrm{Larmor}}(t) = \mathrm{e}^{-\mathrm{i}\omega_0 t\hat Z/2} \quad(\text{axis }\boldsymbol{e}_z,\text{ speed }\omega_0),
$$

$$
\hat U_{\mathrm{Rabi}}(t) = \mathrm{e}^{-\mathrm{i}\Omega t\hat X/2} \quad(\text{axis }\boldsymbol{e}_x,\text{ speed }\Omega).
$$

The only geometric difference is the rotation axis.

(b) Larmor precession is rotation about $\boldsymbol{e}_z$, which leaves the $\vert 0\rangle, \vert 1\rangle$ populations unchanged (they are $\boldsymbol{e}_z$-eigenstates — rotation about $\boldsymbol{e}_z$ keeps them on their respective poles). It can only rotate equatorial superpositions, not transfer populations. Rabi rotation is about $\boldsymbol{e}_x$, perpendicular to the $\vert 0\rangle/\vert 1\rangle$ axis; it actively transfers populations *between* $\vert 0\rangle$ and $\vert 1\rangle$. In short: rotation about the qubit's own quantisation axis cannot drive population transfer; rotation about a perpendicular axis can.

(c) **$\omega_0$** is the bare qubit splitting — the difference between the two energy eigenvalues divided by $\hbar$ ($\omega_0 = \gamma B_0$ for a spin in a static field; the transition frequency for any two-level system). Typical scales: GHz for superconducting qubits, MHz–GHz for atomic spins. **$\Omega$** is proportional to the *amplitude* of the applied resonant drive — it sets the rate at which the drive can transfer population between the two levels. Typical scales: kHz–MHz.

The separation $\Omega \ll \omega_0$ is what justifies the **rotating-wave approximation** (RWA): when the drive is much weaker than the bare splitting, the rapid carrier oscillation at frequency $\omega_0$ averages away on the timescale $1/\Omega$ over which the drive does meaningful work, leaving only the slow envelope (the $\hat X$ term in the rotating frame). If $\Omega$ were comparable to $\omega_0$, the carrier and the drive would mix on similar timescales and the RWA would fail. Physically: the Larmor frequency is the "carrier"; the Rabi frequency is the "envelope" of population transfer that the carrier modulates.

<!-- ─── -->

★ **8. Three-state evolution.** Consider a 3-level system with basis $\{\vert 1\rangle, \vert 2\rangle, \vert 3\rangle\}$ and Hamiltonian $\hat{H} = \vert 1\rangle\langle 2\vert + \vert 2\rangle\langle 1\vert - \vert 1\rangle\langle 3\vert - \vert 3\rangle\langle 1\vert$ (in units where the coupling is 1, and $\hbar = 1$).

(a) Find the eigenvalues and eigenstates of $\hat{H}$.

(b) The system starts in $\vert\psi(0)\rangle = \vert 1\rangle$. Compute $\vert\psi(t)\rangle$.

(c) What is the probability of finding the system in $\vert 3\rangle$ at time $t$?

(d) For a measurement of $\hat{H}^2$ (note: **not** $\hat{H}$) on $\vert\psi(t)\rangle$, list the possible outcomes and their corresponding probabilities.

**Solution.**

In the ordered basis $\{\vert 1\rangle, \vert 2\rangle, \vert 3\rangle\}$, the outer products give matrix entries $H_{12} = H_{21} = 1$ and $H_{13} = H_{31} = -1$, so

$$
\hat{H} = \begin{pmatrix} 0 & 1 & -1 \\ 1 & 0 & 0 \\ -1 & 0 & 0 \end{pmatrix}.
$$

**(a) Eigenvalues and eigenstates.** The characteristic polynomial is

$$
\det(\hat H - \lambda\hat I) = -\lambda^3 + 2\lambda = -\lambda(\lambda^2 - 2),
$$

so $\lambda = 0,\,\pm\sqrt 2$. Solving $(\hat H - \lambda\hat I)\vert v\rangle = 0$ for each eigenvalue:

$$
\vert E_0\rangle = \frac{1}{\sqrt 2}\bigl(\vert 2\rangle + \vert 3\rangle\bigr), \qquad \vert E_\pm\rangle = \frac{1}{2}\bigl(\pm\sqrt 2\,\vert 1\rangle + \vert 2\rangle - \vert 3\rangle\bigr),
$$

with $\hat H\vert E_0\rangle = 0$ and $\hat H\vert E_\pm\rangle = \pm\sqrt 2\,\vert E_\pm\rangle$. Direct check confirms mutual orthogonality and unit norm. The state $\vert E_0\rangle$ is a **dark state**: a coherent superposition of $\vert 2\rangle$ and $\vert 3\rangle$ with no $\vert 1\rangle$ component, dynamically decoupled from $\vert 1\rangle$ by the sign cancellation in $\hat H$.

**(b) Time evolution.** Expand $\vert 1\rangle$ in the energy basis. Note $\langle E_0\vert 1\rangle = 0$ (the dark state has no $\vert 1\rangle$ component), while $\langle E_\pm\vert 1\rangle = \pm\sqrt 2/2 = \pm 1/\sqrt 2$:

$$
\vert 1\rangle = \frac{1}{\sqrt 2}\vert E_+\rangle - \frac{1}{\sqrt 2}\vert E_-\rangle.
$$

Each component evolves by its own phase $\mathrm{e}^{-\mathrm{i}E_n t}$:

$$
\vert\psi(t)\rangle = \frac{1}{\sqrt 2}\mathrm{e}^{-\mathrm{i}\sqrt 2\,t}\vert E_+\rangle - \frac{1}{\sqrt 2}\mathrm{e}^{+\mathrm{i}\sqrt 2\,t}\vert E_-\rangle.
$$

Substituting the explicit eigenvectors and collecting terms in the original basis,

$$
\vert\psi(t)\rangle = \cos(\sqrt 2\,t)\vert 1\rangle - \frac{\mathrm{i}}{\sqrt 2}\sin(\sqrt 2\,t)\vert 2\rangle + \frac{\mathrm{i}}{\sqrt 2}\sin(\sqrt 2\,t)\vert 3\rangle.
$$

Sanity check: at $t=0$ this is $\vert 1\rangle$, and the norm is $\cos^2 + \tfrac{1}{2}\sin^2 + \tfrac{1}{2}\sin^2 = 1$ for all $t$. $\checkmark$

**(c) Probability in $\vert 3\rangle$.** Read off the $\vert 3\rangle$ amplitude and square:

$$
P_3(t) = \left\vert\frac{\mathrm{i}}{\sqrt 2}\sin(\sqrt 2\,t)\right\vert^2 = \frac{1}{2}\sin^2(\sqrt 2\,t).
$$

Population sloshes from $\vert 1\rangle$ into the pair $\vert 2\rangle, \vert 3\rangle$ and back, with the $\vert 3\rangle$ share never exceeding $1/2$.

**(d) Measuring $\hat{H}^2$.** The eigenvalues of $\hat H^2$ are the squares of those of $\hat H$: from $\lambda \in \{0,\,+\sqrt 2,\,-\sqrt 2\}$ we get $\lambda^2 \in \{0,\,2,\,2\}$. So $\hat H^2$ has **two distinct outcomes** — $0$ (eigenstate $\vert E_0\rangle$) and $2$ (the **degenerate** eigenspace spanned by $\vert E_+\rangle$ and $\vert E_-\rangle$).

The evolved state $\vert\psi(t)\rangle$ is built only from $\vert E_+\rangle$ and $\vert E_-\rangle$ — time evolution merely rephases each — so its overlap with $\vert E_0\rangle$ stays zero. The Born-rule probabilities are

$$
P(\hat H^2 = 0) = \vert\langle E_0\vert\psi(t)\rangle\vert^2 = 0,
$$

$$
P(\hat H^2 = 2) = \vert\langle E_+\vert\psi(t)\rangle\vert^2 + \vert\langle E_-\vert\psi(t)\rangle\vert^2 = \tfrac{1}{2} + \tfrac{1}{2} = 1.
$$

A measurement of $\hat H^2$ yields $2$ with certainty for all time $t$. The instructive point: $\hat H$ itself does **not** have a definite value in $\vert\psi(t)\rangle$ — the state is a coherent superposition of $\vert E_+\rangle$ and $\vert E_-\rangle$ — yet $\hat H^2$ is perfectly sharp, because the two distinct eigenvalues $\pm\sqrt 2$ of $\hat H$ collapse to the same $\lambda^2 = 2$ of $\hat H^2$. Direct verification: $\hat H^2\vert\psi(t)\rangle = 2\vert\psi(t)\rangle$. The state lies entirely within the degenerate eigenspace of $\hat H^2$, making that observable a conserved quantity with a definite value even as the system oscillates among the three basis levels.
