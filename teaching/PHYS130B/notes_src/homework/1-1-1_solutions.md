# 1.1.1 What is a Qubit
Worked solutions for the homework problems in the [1.1.1 What is a Qubit](../ch1_qubit/1-1-1-what-is-a-qubit) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Born rule and probabilities.** A qubit is in state $\vert\psi\rangle = \tfrac{3}{5}\vert 0\rangle + \tfrac{4}{5}\vert 1\rangle$.

(a) Use Born's rule to find $P(0)$ and $P(1)$.

(b) Verify that $P(0) + P(1) = 1$.

(c) Now consider $\vert\phi\rangle = \tfrac{3}{5}\vert 0\rangle - \tfrac{4}{5}\vert 1\rangle$. Are $\vert\psi\rangle$ and $\vert\phi\rangle$ the same physical state? Compute $P(+)$ and $P(-)$ in the $X$ basis $\{\vert\pm\rangle = \tfrac{1}{\sqrt{2}}(\vert 0\rangle \pm \vert 1\rangle)\}$ for both states, and use the result to justify your answer.

**Solution.**

(a) Born's rule states that the probability of outcome $m$ in a measurement in the $\{\vert 0\rangle,\vert 1\rangle\}$ basis is the squared modulus of the corresponding amplitude, $P(m)=\vert\langle m\vert\psi\rangle\vert^2$. Because $\vert 0\rangle$ and $\vert 1\rangle$ are orthonormal, $\langle 0\vert\psi\rangle=\tfrac35$ and $\langle 1\vert\psi\rangle=\tfrac45$, so

$$
P(0)=\left\vert\tfrac35\right\vert^2=\tfrac{9}{25}=0.36,\qquad
P(1)=\left\vert\tfrac45\right\vert^2=\tfrac{16}{25}=0.64.
$$

(b) Adding the two,

$$
P(0)+P(1)=\tfrac{9}{25}+\tfrac{16}{25}=\tfrac{25}{25}=1.
$$

The probabilities sum to one. This is the normalization condition $\vert\alpha\vert^2+\vert\beta\vert^2=1$ restated, and it expresses the physical requirement that the qubit must be found in *some* basis state.

(c) For both states, the $Z$-basis probabilities are identical: $P_\phi(0)=\vert 3/5\vert^2 = 9/25$ and $P_\phi(1)=\vert{-4/5}\vert^2 = 16/25$, matching $\psi$. So a $Z$-basis measurement cannot distinguish them.

In the $X$ basis, the amplitudes are

$$
\langle +\vert\psi\rangle = \tfrac{1}{\sqrt 2}\!\left(\tfrac35+\tfrac45\right) = \tfrac{7}{5\sqrt 2}, \qquad
\langle +\vert\phi\rangle = \tfrac{1}{\sqrt 2}\!\left(\tfrac35-\tfrac45\right) = -\tfrac{1}{5\sqrt 2}.
$$

The probabilities are

$$
P_\psi(+) = \tfrac{49}{50}=0.98, \qquad P_\psi(-) = \tfrac{1}{50}=0.02,
$$

$$
P_\phi(+) = \tfrac{1}{50}=0.02, \qquad P_\phi(-) = \tfrac{49}{50}=0.98.
$$

The $X$-basis statistics differ sharply. Therefore $\vert\psi\rangle$ and $\vert\phi\rangle$ are **not** the same physical state. They differ by a *relative* phase (a sign flip on the $\vert 1\rangle$ component only) — not by a *global* phase — and a relative phase is observable in any basis other than the one that diagonalises the populated levels. (Only a *global* phase, as in Problem 3, would be unobservable.)

<!-- ─── -->

**2. State reconstruction from probabilities.** Construct a qubit state $\vert\psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle$ whose measurement statistics satisfy:

- $Z$-basis: $P(0) = 0.3$, $P(1) = 0.7$.
- $X$-basis: $P(+) = 0.5$, where $\vert\pm\rangle = \tfrac{1}{\sqrt{2}}(\vert 0\rangle \pm \vert 1\rangle)$.

(a) Use the $Z$-basis probabilities to determine $\vert\alpha\vert$ and $\vert\beta\vert$.

(b) Show that $P(+) = 0.5$ pins down the relative phase between $\alpha$ and $\beta$. Find the allowed relative phase(s).

(c) Write down the most general such state up to a global phase. How many distinct physical states satisfy these constraints? In what sense are the $Z$ and $X$ measurements *not enough* to uniquely determine the state, and what additional measurement would suffice?

**Solution.**

(a) By Born's rule $P(0) = \vert\alpha\vert^2$ and $P(1) = \vert\beta\vert^2$, so

$$
\vert\alpha\vert = \sqrt{0.3}, \qquad \vert\beta\vert = \sqrt{0.7}.
$$

The moduli are fixed; the phases are not yet determined.

(b) Write $\alpha = \vert\alpha\vert\,\mathrm{e}^{\mathrm{i}\phi_\alpha}$ and $\beta = \vert\beta\vert\,\mathrm{e}^{\mathrm{i}\phi_\beta}$, and let $\varphi \equiv \phi_\beta - \phi_\alpha$ be the relative phase. The $+$-amplitude is

$$
\langle +\vert\psi\rangle = \tfrac{1}{\sqrt 2}(\alpha + \beta),
$$

so

$$
P(+) = \tfrac{1}{2}\vert\alpha + \beta\vert^2 = \tfrac{1}{2}\bigl(\vert\alpha\vert^2 + \vert\beta\vert^2 + 2\,\mathrm{Re}(\alpha^*\beta)\bigr) = \tfrac{1}{2}\bigl(1 + 2\vert\alpha\vert\vert\beta\vert\cos\varphi\bigr).
$$

Imposing $P(+) = 1/2$ gives $\cos\varphi = 0$, i.e.

$$
\varphi = \pm\tfrac{\pi}{2}.
$$

(c) Using global-phase freedom to make $\alpha$ real and positive, the two solutions are

$$
\vert\psi_\pm\rangle = \sqrt{0.3}\,\vert 0\rangle \pm \mathrm{i}\sqrt{0.7}\,\vert 1\rangle.
$$

These are **two physically distinct** states — they are not related by a global phase, since $\vert\psi_-\rangle = (\vert\psi_+\rangle)^*$ component-wise rather than $\mathrm{e}^{\mathrm{i}\gamma}\vert\psi_+\rangle$. On the Bloch sphere they sit at $\boldsymbol{n}_\pm = (0,\,\pm 2\sqrt{0.21},\,0.3 - 0.7) = (0,\,\pm 0.916,\,-0.4)$: reflections across the $xz$-plane.

The two Pauli measurements ($Z$ and $X$) supply two real numbers, but the Bloch sphere is two-dimensional and one of the supplied numbers is *insensitive* to the sign of $\langle\hat Y\rangle$. Adding a measurement of $P(\mathrm{i})$ in the $Y$ basis $\{\vert\mathrm{i}\rangle, \vert\bar{\mathrm{i}}\rangle\}$ would distinguish $\vert\psi_+\rangle$ from $\vert\psi_-\rangle$ and complete the state reconstruction. Measuring expectation values $\langle\hat X\rangle,\langle\hat Y\rangle,\langle\hat Z\rangle$ in all three Pauli bases is the standard recipe for **single-qubit state tomography**.

<!-- ─── -->

**3. Global phase invariance.** Show that two states differing by a global phase, $\vert\psi'\rangle = \mathrm{e}^{\mathrm{i}\gamma}\vert\psi\rangle$ (with $\gamma \in \mathbb{R}$), give identical measurement probabilities $\vert\langle m\vert\psi'\rangle\vert^2 = \vert\langle m\vert\psi\rangle\vert^2$ for every outcome $\vert m\rangle$ and every choice of measurement basis. In one sentence, contrast with Problem 1(c) and explain why the same argument **fails** for a relative phase between components.

**Solution.**

The factor $\mathrm{e}^{\mathrm{i}\gamma}$ is a complex number, so by linearity of the inner product

$$
\langle m\vert\psi'\rangle = \mathrm{e}^{\mathrm{i}\gamma}\,\langle m\vert\psi\rangle.
$$

Its modulus squared is

$$
\vert\langle m\vert\psi'\rangle\vert^2 = \vert\mathrm{e}^{\mathrm{i}\gamma}\vert^2\,\vert\langle m\vert\psi\rangle\vert^2 = \vert\langle m\vert\psi\rangle\vert^2,
$$

since $\vert\mathrm{e}^{\mathrm{i}\gamma}\vert^2 = \mathrm{e}^{\mathrm{i}\gamma}\mathrm{e}^{-\mathrm{i}\gamma} = 1$ for real $\gamma$. This holds for every $\vert m\rangle$ and every basis, and extends to operator expectation values: $\langle\psi'\vert\hat O\vert\psi'\rangle = \mathrm{e}^{-\mathrm{i}\gamma}\mathrm{e}^{\mathrm{i}\gamma}\langle\psi\vert\hat O\vert\psi\rangle = \langle\psi\vert\hat O\vert\psi\rangle$. So no measurement can detect $\gamma$, and the states $\vert\psi\rangle$ and $\mathrm{e}^{\mathrm{i}\gamma}\vert\psi\rangle$ represent the *same* physical state.

**Contrast with Problem 1(c).** A *relative* phase multiplies only one of the two amplitudes, so it does **not** factor out of $\langle m\vert\psi\rangle$ as a global prefactor: the cancellation $\vert\mathrm{e}^{\mathrm{i}\gamma}\vert^2 = 1$ used above does not apply, and the relative phase survives in *off-diagonal* measurement bases (the $X$ basis of Problem 1(c), where $\langle +\vert\psi\rangle$ is a *sum* of amplitudes whose relative phase changes the result).

<!-- ─── -->

**4. Bloch sphere parametrization.** A generic qubit state $\vert\psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle$ naively requires 4 real parameters $(\mathrm{Re}\,\alpha,\ \mathrm{Im}\,\alpha,\ \mathrm{Re}\,\beta,\ \mathrm{Im}\,\beta)$. Show that after imposing

(a) normalization $\vert\alpha\vert^2 + \vert\beta\vert^2 = 1$ and

(b) global phase freedom, only 2 real parameters remain. How does this explain why the space of qubit states maps to a 2-dimensional sphere?

**Solution.**

Begin with $\vert\psi\rangle=\alpha\vert 0\rangle+\beta\vert 1\rangle$, $\alpha,\beta\in\mathbb{C}$. Writing each amplitude in terms of its real and imaginary parts gives the four real numbers $(\mathrm{Re}\,\alpha,\mathrm{Im}\,\alpha,\mathrm{Re}\,\beta,\mathrm{Im}\,\beta)$ — a naive count of **4 real parameters**.

(a) *Normalization.* The condition $\vert\alpha\vert^2+\vert\beta\vert^2=1$ is a single real equation linking the four parameters; it removes one degree of freedom, leaving **3**. Geometrically, the four real numbers are confined to the unit sphere $S^3$ embedded in $\mathbb{R}^4$.

(b) *Global phase freedom.* By Problem 3, multiplying $\vert\psi\rangle$ by an overall phase $\mathrm{e}^{\mathrm{i}\gamma}$ does not change the physical state. We may spend this freedom to fix one parameter — for example, rotate the overall phase so that the amplitude $\alpha$ becomes real and non-negative. That removes one further degree of freedom, leaving **2**.

Concretely, normalization lets us set $\vert\alpha\vert=\cos(\theta/2)$ and $\vert\beta\vert=\sin(\theta/2)$ for some $\theta\in[0,\pi]$, since then $\vert\alpha\vert^2+\vert\beta\vert^2=\cos^2(\theta/2)+\sin^2(\theta/2)=1$ automatically. The global-phase choice makes $\alpha$ real, so only the *relative* phase $\varphi$ of $\beta$ survives:

$$
\vert\psi\rangle=\cos\tfrac{\theta}{2}\,\vert 0\rangle+\mathrm{e}^{\mathrm{i}\varphi}\sin\tfrac{\theta}{2}\,\vert 1\rangle,
\qquad \theta\in[0,\pi],\quad \varphi\in[0,2\pi).
$$

The two remaining parameters $(\theta,\varphi)$ are precisely the polar and azimuthal angles of a point on a 2-sphere — the **Bloch sphere**. The north pole ($\theta=0$) is $\vert 0\rangle$, the south pole ($\theta=\pi$) is $\vert 1\rangle$, and the equator ($\theta=\pi/2$) carries the equal-weight superpositions. The half-angle $\theta/2$ is essential: it makes the two orthogonal states $\vert 0\rangle$ and $\vert 1\rangle$, which differ by $\theta=\pi$, sit at *antipodal* points $180^\circ$ apart on the sphere.

This is why the space of qubit states is exactly 2-dimensional. Formally it is the quotient of the normalized states $S^3$ by the global-phase circle $U(1)$, namely $S^3/U(1)=S^2$ (the Hopf map), also denoted $\mathbb{CP}^1$. The naive count of $4$ real parameters is reduced by $1$ (normalization) and by $1$ (global phase) to give $2$ — the dimension of a sphere.

<!-- ─── -->

**5. Quantum information.** A qubit state $\vert\psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle$ is specified by two continuous real parameters — seemingly more information than a single classical bit (0 or 1). Does a qubit therefore store more information than a classical bit? Address the following:

(a) How much classical information is extracted by a single measurement of the qubit?

(b) Can repeated measurements on identical copies extract more? Name the reconstruction procedure and state the upper bound on the classical information accessible per measurement, as quoted in the lecture's comparison table.

(c) Identify the two quantum-mechanical resources beyond classical encoding — superposition (with interference) and entanglement — and name one example phenomenon or protocol that uses each.

**Solution.**

(a) A single projective measurement in a fixed basis returns one of two outcomes, $0$ or $1$. The result is a single binary symbol, so **one measurement extracts at most one classical bit**. The continuous amplitudes $\alpha,\beta$ are not read off directly — the measurement only draws one sample from the distribution $\{P(0),P(1)\}$, and a single sample cannot pin down a continuous parameter.

(b) With many *identically prepared* copies, the amplitudes (equivalently, the Bloch vector) can be estimated to arbitrary precision by **quantum state tomography**: measure batches of copies in the $X$, $Y$, and $Z$ bases and reconstruct the state from the three outcome frequencies. So the continuous parameters *are* accessible — but only as a property of an *ensemble*, never from one qubit. A single *unknown* qubit still yields at most one bit — the same upper bound stated in the lecture's classical-bit vs. qubit comparison table.

(c) Because no more than one bit can ever be retrieved from one qubit, the continuous parameters are not a classical-storage advantage. Two genuinely quantum resources go beyond that:

- **Superposition with interference.** Amplitudes — not probabilities — are the fundamental objects of quantum mechanics, and two physical paths from the same start to the same end can add constructively or destructively when their phases align or oppose. A classical bit is either $0$ or $1$ *before* measurement, with no notion of an "amplitude for $0$" and a separately-tracked phase; there is no classical analogue of this addition.
- **Entanglement** (to be developed in Chapter 2). Two or more qubits can be prepared in joint states whose correlations cannot be reproduced by any classical mixture of independent qubits.

Together with the **no-cloning** property already noted in the lecture's comparison table, superposition and entanglement are what make quantum information *genuinely* distinct from classical information — not the apparent abundance of continuous amplitudes, which any single measurement collapses back to one bit.

<!-- ─── -->

**6. Distinguishing non-orthogonal states.** A qubit is prepared in one of two states with equal prior probability $1/2$: either $\vert\psi_1\rangle = \vert 0\rangle$ or $\vert\psi_2\rangle = \tfrac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle)$. You perform a single projective measurement in a basis of your choice, then guess which state was prepared. The goal is to maximise the probability of guessing correctly.

(a) Compute the overlap $\vert\langle\psi_1\vert\psi_2\rangle\vert$. Are the two states orthogonal?

(b) Suppose you measure in the $\{\vert 0\rangle, \vert 1\rangle\}$ ($Z$) basis. What outcome — if any — uniquely identifies the state? What outcome is ambiguous, and which guess is more likely correct given that outcome?

(c) State the full $Z$-basis guessing rule from part (b) and compute the resulting probability of guessing correctly.

(d) Explain in one sentence why **no** measurement strategy can achieve guessing probability $1$, in contrast to the case of two *orthogonal* states.

**Solution.**

(a) The overlap is

$$
\langle\psi_1\vert\psi_2\rangle = \langle 0\vert\,\tfrac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle)\rangle = \tfrac{1}{\sqrt{2}}.
$$

Its modulus is $1/\sqrt{2}\neq 0$, so the two states are **not orthogonal**.

(b) Z-basis conditional probabilities:

$$
P(0\vert\psi_1) = 1, \quad P(1\vert\psi_1) = 0, \qquad P(0\vert\psi_2) = \tfrac{1}{2}, \quad P(1\vert\psi_2) = \tfrac{1}{2}.
$$

**Outcome 1** is impossible if the state was $\vert\psi_1\rangle$, so seeing $1$ definitively identifies the state as $\vert\psi_2\rangle$.

**Outcome 0** is possible from either state. Bayes' rule with equal priors gives

$$
P(\psi_1\vert 0) = \frac{1\cdot\tfrac12}{1\cdot\tfrac12 + \tfrac12\cdot\tfrac12} = \frac{2}{3}, \qquad P(\psi_2\vert 0) = \frac{1}{3}.
$$

Given outcome $0$, the more likely state is $\vert\psi_1\rangle$ (by 2:1 odds).

(c) Guessing rule: if outcome $0$, guess $\vert\psi_1\rangle$; if outcome $1$, guess $\vert\psi_2\rangle$. The success probability is the sum over true states of (prior $\times$ probability of getting the outcome that points to the correct guess):

$$
P_{\mathrm{success}} = \tfrac{1}{2}\,P(0\vert\psi_1) + \tfrac{1}{2}\,P(1\vert\psi_2) = \tfrac{1}{2}(1) + \tfrac{1}{2}\!\left(\tfrac{1}{2}\right) = \tfrac{3}{4}.
$$

So the Z-basis strategy succeeds **75 %** of the time — better than a coin flip, worse than perfect.

(d) Two orthogonal states $\vert\phi_1\rangle$, $\vert\phi_2\rangle$ are simultaneous eigenstates of a single observable (the projector $\vert\phi_1\rangle\langle\phi_1\vert$), so measuring that observable returns a deterministic outcome for each state — perfect discrimination. For non-orthogonal $\vert\psi_1\rangle, \vert\psi_2\rangle$ the overlap $\langle\psi_1\vert\psi_2\rangle\neq 0$ means **no** observable has them as simultaneous eigenstates; in any chosen basis, at least one outcome will be possible from both states with nonzero probability. That ambiguous outcome forces a guess, capping the success rate strictly below $1$. This is the operational reason behind the **no-cloning** property mentioned in the lecture's comparison table: if an unknown state could be perfectly identified by a single measurement, it could then be cloned by re-preparing the identified state.

<!-- ─── -->

**7. Photon polarization vs. transmon qubit.** A photon qubit uses polarization ($\vert 0\rangle = $ horizontal, $\vert 1\rangle = $ vertical). At room temperature ($T = 300\,\mathrm{K}$), thermal energy is $k_BT \approx 26\,\mathrm{meV}$. A visible photon at $\lambda = 800\,\mathrm{nm}$ has energy $E = hc/\lambda$ (use $hc = 1240\,\mathrm{eV\cdot nm}$).

(a) Compute $E$ in $\mathrm{eV}$.

(b) Using a Boltzmann argument, argue whether the photon polarization qubit is susceptible to thermal noise at room temperature. State the relevant comparison of scales explicitly.

(c) A superconducting transmon qubit at $5\,\mathrm{GHz}$ has energy gap $\hbar\omega \approx 0.021\,\mathrm{meV}$. At what temperature $T^*$ does $k_BT^* = \hbar\omega$? Estimate the operating temperature needed to keep the excited-state thermal population below $1\,\%$, and compare to the typical dilution-refrigerator scale ($\sim 10\text{--}20\,\mathrm{mK}$).

**Solution.**

(a) Using $E=hc/\lambda$ with $hc=1240\,\mathrm{eV\cdot nm}$ and $\lambda=800\,\mathrm{nm}$:

$$
E=\frac{1240\ \mathrm{eV\cdot nm}}{800\ \mathrm{nm}}=1.55\ \mathrm{eV}.
$$

(b) The relevant comparison is between the level splitting $E$ and the thermal energy $k_BT$. At $T=300\,\mathrm{K}$, $k_BT \approx 26\,\mathrm{meV}=0.026\,\mathrm{eV}$, so

$$
\frac{E}{k_BT}=\frac{1.55\ \mathrm{eV}}{0.026\ \mathrm{eV}}\approx 60.
$$

By Boltzmann, the chance of thermally populating an optical mode at this frequency is suppressed by $\bar n=1/(\mathrm{e}^{E/k_BT}-1)\approx\mathrm{e}^{-E/k_BT}\approx\mathrm{e}^{-60}\approx 10^{-26}$ — utterly negligible. Furthermore, the qubit information is stored in *polarization*, and the two polarization states $\vert H\rangle$ and $\vert V\rangle$ are degenerate ($\Delta E \approx 0$), so there is no level splitting for thermal energy to drive. **The photon polarization qubit is therefore not susceptible to thermal noise at room temperature**, which is why photonic qubits can operate without cryogenic cooling.

(c) Setting $k_BT^*=\hbar\omega$ with $\hbar\omega\approx 0.021\,\mathrm{meV}$ and $k_B \approx 8.62\times10^{-2}\,\mathrm{meV/K}$:

$$
T^*=\frac{\hbar\omega}{k_B}=\frac{0.021\ \mathrm{meV}}{0.0862\ \mathrm{meV/K}}\approx 0.24\ \mathrm{K}.
$$

For a two-level system in thermal equilibrium, Boltzmann statistics give the excited-state probability

$$
P(\text{excited})=\frac{\mathrm{e}^{-\hbar\omega/k_BT}}{1+\mathrm{e}^{-\hbar\omega/k_BT}}\approx \mathrm{e}^{-\hbar\omega/k_BT} \quad \text{for } k_BT \ll \hbar\omega.
$$

Requiring $P(\text{excited}) < 0.01$ gives $\hbar\omega/(k_BT) > \ln(100) \approx 4.6$, i.e.

$$
T < \frac{T^*}{4.6} \approx 50\,\mathrm{mK}.
$$

In practice transmons are operated in dilution refrigerators at $\sim 10\text{--}20\,\mathrm{mK}$ — comfortably below this estimate, with $\hbar\omega/(k_BT)\sim 12\text{--}24$ giving $P(\text{excited}) \sim 10^{-5}$ to $10^{-10}$.

The contrast with part (b) is the central lesson: a tiny level splitting ($\sim\mu\mathrm{eV}$) demands deep cryogenic cooling to suppress thermal occupation, whereas an optical photon's enormous energy ($\sim\mathrm{eV}$) makes it intrinsically immune to thermal noise at room temperature. The same Boltzmann factor is the named approximation principle in both cases; only the energy scale differs by nine orders of magnitude.
