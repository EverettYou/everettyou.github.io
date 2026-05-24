# 4.3.2 Landau Quantization
Worked solutions for the homework problems in the [4.3.2 Landau Quantization](../ch4_phase-and-gauge/4-3-2-landau-quantization) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Lowest Landau level wavefunctions.** In symmetric gauge $\boldsymbol{A} = \frac{B}{2}(-y, x, 0)$, the lowest Landau level (LLL) states are

$$
\begin{split}
\psi_m(\boldsymbol{r}) &\propto z^m\,\mathrm{e}^{-\vert z\vert^2/(4\ell_B^2)},\\
z &= x + \mathrm{i}y,\\
m &= 0,1,2,\ldots
\end{split}
$$

(a) Verify by direct computation that $\hat{a}\,\psi_m = 0$, where $\hat{a} = (\ell_B/(\sqrt{2}\,\hbar))(\hat{\pi}_x + \mathrm{i}\hat{\pi}_y)$.

(b) Compute $\langle\hat{r}^2\rangle$ for $\psi_m$ and show it grows linearly with $m$. Interpret as the squared distance of the guiding center from the origin.

(c) Show that $\psi_m$ is an eigenstate of $\hat{L}_z$ with eigenvalue $m\hbar$. Connect $m$ to the guiding-center quantum number from the lecture.

**Solution.**

**(a)** Work in the complex coordinate $z = x + \mathrm{i}y$ together with its conjugate $\bar{z} = x - \mathrm{i}y$. The associated derivatives are

$$
\begin{split}
\partial_z &= \tfrac{1}{2}(\partial_x - \mathrm{i}\partial_y),\\
\partial_{\bar{z}} &= \tfrac{1}{2}(\partial_x + \mathrm{i}\partial_y),
\end{split}
$$

so that $\partial_x + \mathrm{i}\partial_y = 2\partial_{\bar{z}}$, and $z$ is *holomorphic*: $\partial_{\bar{z}}\,z = 0$, hence $\partial_{\bar{z}}\,z^m = 0$.

In symmetric gauge the kinetic momenta are $\hat{\pi}_x = \hat{p}_x + \tfrac{qB}{2}\hat{y}$ and $\hat{\pi}_y = \hat{p}_y - \tfrac{qB}{2}\hat{x}$, with $\hat{p}_j = -\mathrm{i}\hbar\partial_j$. Combine them into the cyclotron annihilation operator, grouping the momentum terms and the position terms separately:

$$
\begin{split}
\hat{\pi}_x + \mathrm{i}\hat{\pi}_y
&= (\hat{p}_x + \mathrm{i}\hat{p}_y) + \tfrac{qB}{2}(\hat{y} - \mathrm{i}\hat{x})\\
&= -\mathrm{i}\hbar(\partial_x + \mathrm{i}\partial_y) - \mathrm{i}\tfrac{qB}{2}(\hat{x} + \mathrm{i}\hat{y})\\
&= -2\mathrm{i}\hbar\,\partial_{\bar{z}} - \mathrm{i}\tfrac{qB}{2}\,z\\
&= -2\mathrm{i}\hbar\left(\partial_{\bar{z}} + \frac{z}{4\ell_B^2}\right),
\end{split}
$$

where the second line uses $\hat{y} - \mathrm{i}\hat{x} = -\mathrm{i}(\hat{x} + \mathrm{i}\hat{y})$, the third line uses $\partial_x + \mathrm{i}\partial_y = 2\partial_{\bar{z}}$ and $\hat{x} + \mathrm{i}\hat{y} = z$, and the last line uses $\tfrac{qB}{2} = \tfrac{\hbar}{2\ell_B^2}$ from $\ell_B^2 = \hbar/(qB)$. The annihilation operator is therefore the first-order differential operator

$$
\hat{a} = \frac{\ell_B}{\sqrt{2}\,\hbar}\,(\hat{\pi}_x + \mathrm{i}\hat{\pi}_y) = -\mathrm{i}\sqrt{2}\,\ell_B\left(\partial_{\bar{z}} + \frac{z}{4\ell_B^2}\right).
$$

Now apply it to $\psi_m \propto z^m\,\mathrm{e}^{-z\bar{z}/(4\ell_B^2)}$ (note $\vert z\vert^2 = z\bar{z}$). The factor $z^m$ is holomorphic, so $\partial_{\bar{z}}$ sees only the Gaussian:

$$
\begin{split}
\partial_{\bar{z}}\,\psi_m
&= z^m\,\partial_{\bar{z}}\,\mathrm{e}^{-z\bar{z}/(4\ell_B^2)}\\
&= z^m\left(-\frac{z}{4\ell_B^2}\right)\mathrm{e}^{-z\bar{z}/(4\ell_B^2)}\\
&= -\frac{z}{4\ell_B^2}\,\psi_m.
\end{split}
$$

Substituting into $\hat{a}$,

$$
\hat{a}\,\psi_m = -\mathrm{i}\sqrt{2}\,\ell_B\left(-\frac{z}{4\ell_B^2}\,\psi_m + \frac{z}{4\ell_B^2}\,\psi_m\right) = 0.
$$

The derivative of the Gaussian produces exactly $-z/(4\ell_B^2)$, which cancels the explicit $+z/(4\ell_B^2)$ term. This holds for *every* $m$, because the holomorphic prefactor $z^m$ is invisible to $\partial_{\bar{z}}$ — it is precisely the freedom to multiply by any power of $z$ that makes the lowest Landau level infinitely degenerate. Annihilation by $\hat{a}$ is the statement $\hat{a}^\dagger\hat{a}\,\psi_m = 0$, i.e. cyclotron quantum number $n = 0$: all the $\psi_m$ sit in the lowest Landau level.

**(b)** The probability density is $\vert\psi_m\vert^2 \propto \vert z^m\vert^2\,\mathrm{e}^{-\vert z\vert^2/(2\ell_B^2)} = \vert z\vert^{2m}\,\mathrm{e}^{-\vert z\vert^2/(2\ell_B^2)}$ — the modulus-squared of the holomorphic factor is $\vert z\vert^{2m}$, and the Gaussian exponent doubles. Writing $\vert z\vert = r$ and using the planar measure $\mathrm{d}^2r = r\,\mathrm{d}r\,\mathrm{d}\varphi$, the angular integral is identical in numerator and denominator and cancels:

$$
\langle\hat{r}^2\rangle = \frac{\displaystyle\int_0^\infty r^2\cdot r^{2m}\,\mathrm{e}^{-r^2/(2\ell_B^2)}\,r\,\mathrm{d}r}{\displaystyle\int_0^\infty r^{2m}\,\mathrm{e}^{-r^2/(2\ell_B^2)}\,r\,\mathrm{d}r}.
$$

Substitute $u = r^2/(2\ell_B^2)$, so that $r^2 = 2\ell_B^2 u$ and $r\,\mathrm{d}r = \ell_B^2\,\mathrm{d}u$. Each integral collapses to a Gamma function, $\int_0^\infty u^k\,\mathrm{e}^{-u}\,\mathrm{d}u = \Gamma(k+1) = k!$:

$$
\begin{split}
\langle\hat{r}^2\rangle
&= 2\ell_B^2\;\frac{\displaystyle\int_0^\infty u^{\,m+1}\,\mathrm{e}^{-u}\,\mathrm{d}u}{\displaystyle\int_0^\infty u^{\,m}\,\mathrm{e}^{-u}\,\mathrm{d}u}\\
&= 2\ell_B^2\;\frac{\Gamma(m+2)}{\Gamma(m+1)}\\
&= 2\ell_B^2\,(m+1).
\end{split}
$$

So $\langle\hat{r}^2\rangle = 2(m+1)\,\ell_B^2$ — strictly linear in $m$, with slope $2\ell_B^2$ per unit of $m$.

To read the result physically, split the position into the guiding center plus the cyclotron offset. The lecture's guiding-center operators give $\hat{x} - \hat{X} = -\hat{\pi}_y/(qB)$ and $\hat{y} - \hat{Y} = +\hat{\pi}_x/(qB)$, so the squared cyclotron offset is

$$
(\hat{\boldsymbol{r}} - \hat{\boldsymbol{R}})^2 = \frac{\hat{\pi}_x^2 + \hat{\pi}_y^2}{(qB)^2} = \frac{\hat{\boldsymbol{\pi}}^2}{(qB)^2}.
$$

From the lecture's Hamiltonian relation $\hat{\boldsymbol{\pi}}^2 = (2\hbar^2/\ell_B^2)(\hat{a}^\dagger\hat{a} + \tfrac{1}{2})$, an LLL state ($\hat{a}^\dagger\hat{a} = 0$) has $\langle\hat{\boldsymbol{\pi}}^2\rangle = \hbar^2/\ell_B^2$, and with $qB = \hbar/\ell_B^2$,

$$
\langle(\hat{\boldsymbol{r}} - \hat{\boldsymbol{R}})^2\rangle = \frac{\hbar^2/\ell_B^2}{(\hbar/\ell_B^2)^2} = \ell_B^2.
$$

Meanwhile the lecture's guiding-center radius operator is $\hat{X}^2 + \hat{Y}^2 = \ell_B^2(2\hat{b}^\dagger\hat{b} + 1)$, so a state with guiding-center quantum number $m$ has $\langle\hat{X}^2 + \hat{Y}^2\rangle = (2m+1)\ell_B^2$. The cross terms between guiding center and cyclotron offset vanish (the two sets of operators commute, and the cyclotron offset has zero mean in a Landau-level eigenstate), so

$$
\langle\hat{r}^2\rangle = \underbrace{(2m+1)\,\ell_B^2}_{\text{guiding center}} + \underbrace{\ell_B^2}_{\text{cyclotron zero-point}} = 2(m+1)\,\ell_B^2,
$$

reproducing the integral. The linear growth in $m$ is therefore *entirely* the guiding center marching outward: each unit of $m$ steps the orbit center onto a ring whose squared radius is larger by $2\ell_B^2$. The constant $\ell_B^2$ that distinguishes $\langle\hat{r}^2\rangle$ from the pure guiding-center value is just the fixed zero-point size of the cyclotron orbit, the same for every $m$ in the lowest Landau level.

**(c)** The $z$-component of orbital angular momentum is $\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x = -\mathrm{i}\hbar(x\partial_y - y\partial_x)$, which in plane polar coordinates is the generator of rotations about the origin,

$$
\hat{L}_z = -\mathrm{i}\hbar\,\partial_\varphi.
$$

Write $\psi_m$ in polar form. With $z = r\,\mathrm{e}^{\mathrm{i}\varphi}$ one has $z^m = r^m\,\mathrm{e}^{\mathrm{i}m\varphi}$ and $\vert z\vert^2 = r^2$, so

$$
\psi_m \propto r^m\,\mathrm{e}^{\mathrm{i}m\varphi}\,\mathrm{e}^{-r^2/(4\ell_B^2)}.
$$

The only factor that depends on the azimuth is $\mathrm{e}^{\mathrm{i}m\varphi}$; the radial profile $r^m$ and the Gaussian are rotationally invariant. Hence $\partial_\varphi\psi_m = \mathrm{i}m\,\psi_m$ and

$$
\hat{L}_z\,\psi_m = -\mathrm{i}\hbar\,(\mathrm{i}m)\,\psi_m = m\hbar\,\psi_m.
$$

So $\psi_m$ is an $\hat{L}_z$ eigenstate with eigenvalue $m\hbar$.

This pins down what $m$ means. Part (a) showed $\psi_m$ has cyclotron index $n = 0$; part (b) showed its guiding-center radius is $\langle\hat{X}^2 + \hat{Y}^2\rangle = (2m+1)\ell_B^2$, which is exactly the eigenvalue of $\ell_B^2(2\hat{b}^\dagger\hat{b} + 1)$ at $\hat{b}^\dagger\hat{b} = m$. Therefore $\psi_m$ is the lecture's joint eigenstate $\vert n=0,\,m\rangle$, and its angular-momentum label is identical to the guiding-center quantum number $m = \hat{b}^\dagger\hat{b}$. The general operator statement is that angular momentum splits across the two ladders, $\hat{L}_z = \hbar(\hat{b}^\dagger\hat{b} - \hat{a}^\dagger\hat{a})$ — the guiding-center revolution and the cyclotron rotation carry opposite-sign angular momentum — and on the lowest Landau level the cyclotron term drops out, leaving $\hat{L}_z = \hbar\,\hat{b}^\dagger\hat{b}$. Larger $m$ means a larger orbit center, a larger angular momentum, and a wider ring-shaped wavefunction, all the same statement.

<!-- ─── -->

**2. Cyclotron resonance.** A circularly polarized electric field $\boldsymbol{E}(t) = E_0(\cos\omega t,\, -\sin\omega t,\, 0)$ couples to a Landau-quantized particle of charge $q$ via $\hat{V}(t) = q\boldsymbol{E}(t)\cdot\hat{\boldsymbol{r}}$.

(a) Express $\hat{x}$ and $\hat{y}$ in terms of the cyclotron and guiding-center ladder operators $\hat{a}, \hat{a}^\dagger, \hat{b}, \hat{b}^\dagger$. Show that the $\hat{b}, \hat{b}^\dagger$ pieces leave the Landau-level index $n$ unchanged, so $\hat{V}(t)$ couples $n$ only to $n\pm 1$.

(b) Compute $\vert\langle n+1\vert\hat{V}\vert n\rangle\vert^2$ at resonance ($\omega = \omega_c$). Show that it grows with $n$.

(c) The absorption peaks sharply at $\omega = \omega_c$ regardless of which Landau level is initially occupied. Explain how this *cyclotron-resonance* peak is used experimentally to measure effective mass.

**Solution.**

**(a)** Invert the ladder-operator definitions of the lecture. From $\hat{a} = (\ell_B/\sqrt{2}\,\hbar)(\hat{\pi}_x + \mathrm{i}\hat{\pi}_y)$ and its conjugate,

$$
\begin{split}
\hat{\pi}_x &= \frac{\hbar}{\sqrt{2}\,\ell_B}\,(\hat{a} + \hat{a}^\dagger),\\
\hat{\pi}_y &= -\,\frac{\mathrm{i}\hbar}{\sqrt{2}\,\ell_B}\,(\hat{a} - \hat{a}^\dagger),
\end{split}
$$

and from $\hat{b} = (\hat{X} - \mathrm{i}\hat{Y})/(\sqrt{2}\,\ell_B)$ and its conjugate,

$$
\begin{split}
\hat{X} &= \frac{\ell_B}{\sqrt{2}}\,(\hat{b} + \hat{b}^\dagger),\\
\hat{Y} &= \frac{\mathrm{i}\ell_B}{\sqrt{2}}\,(\hat{b} - \hat{b}^\dagger).
\end{split}
$$

The position is the guiding center minus the cyclotron offset, $\hat{x} = \hat{X} - \hat{\pi}_y/(qB)$ and $\hat{y} = \hat{Y} + \hat{\pi}_x/(qB)$. Using $1/(qB) = \ell_B^2/\hbar$, the offset prefactors simplify, e.g. $\hat{\pi}_x/(qB) = (\ell_B/\sqrt{2})(\hat{a} + \hat{a}^\dagger)$, and likewise for $\hat{\pi}_y$. Collecting terms,

$$
\begin{split}
\hat{x} &= \frac{\ell_B}{\sqrt{2}}\Big[(\hat{b} + \hat{b}^\dagger) + \mathrm{i}(\hat{a} - \hat{a}^\dagger)\Big],\\
\hat{y} &= \frac{\ell_B}{\sqrt{2}}\Big[\mathrm{i}(\hat{b} - \hat{b}^\dagger) + (\hat{a} + \hat{a}^\dagger)\Big].
\end{split}
$$

Each coordinate splits into a *guiding-center* part (built from $\hat{b}, \hat{b}^\dagger$) and a *cyclotron* part (built from $\hat{a}, \hat{a}^\dagger$). The Landau-level index is $n = \hat{a}^\dagger\hat{a}$. Because the lecture established $[\hat{a}, \hat{b}] = [\hat{a}, \hat{b}^\dagger] = 0$, the guiding-center operators commute with $\hat{a}^\dagger\hat{a}$ and therefore act *within* a fixed-$n$ subspace: $\langle n', m'\vert\hat{b}\vert n, m\rangle \propto \delta_{n'n}$, and similarly for $\hat{b}^\dagger$. They move only the guiding-center label $m$. The cyclotron operators, by contrast, are genuine ladder operators on $n$: $\hat{a}$ lowers $n$ by one, $\hat{a}^\dagger$ raises it by one. Consequently $\hat{x}$ and $\hat{y}$ — and hence $\hat{V}(t) = qE_0(\hat{x}\cos\omega t - \hat{y}\sin\omega t)$ — connect a Landau level only to itself (the $\hat{b}$ pieces) or to its immediate neighbours $n \pm 1$ (the $\hat{a}, \hat{a}^\dagger$ pieces). No term changes $n$ by two or more. The only *level-changing*, and therefore energy-changing, transitions are $n \to n \pm 1$.

**(b)** A transition $n \to n+1$ picks out exactly the $\hat{a}^\dagger$ content of $\hat{V}$: the $\hat{b}, \hat{b}^\dagger$ pieces give $\langle n+1\vert\cdots\vert n\rangle = 0$ (they preserve $n$), and the $\hat{a}$ piece lowers $n$. From part (a), the $\hat{a}^\dagger$ coefficients are $-\mathrm{i}\ell_B/\sqrt{2}$ in $\hat{x}$ and $+\ell_B/\sqrt{2}$ in $\hat{y}$, so the raising part of the perturbation is

$$
\begin{split}
\hat{V}_\uparrow(t)
&= qE_0\left[\cos\omega t\left(-\frac{\mathrm{i}\ell_B}{\sqrt{2}}\right) - \sin\omega t\left(\frac{\ell_B}{\sqrt{2}}\right)\right]\hat{a}^\dagger\\
&= -\,\frac{qE_0\ell_B}{\sqrt{2}}\,\big(\mathrm{i}\cos\omega t + \sin\omega t\big)\,\hat{a}^\dagger\\
&= -\,\frac{qE_0\ell_B}{\sqrt{2}}\;\mathrm{i}\,\mathrm{e}^{-\mathrm{i}\omega t}\,\hat{a}^\dagger,
\end{split}
$$

where the last line uses $\mathrm{i}\cos\omega t + \sin\omega t = \mathrm{i}(\cos\omega t - \mathrm{i}\sin\omega t) = \mathrm{i}\,\mathrm{e}^{-\mathrm{i}\omega t}$. The chosen circular polarization rotates in step with the cyclotron motion, so it collapses to a single rotating term proportional to $\hat{a}^\dagger$ — there is no counter-rotating piece. With $\langle n+1\vert\hat{a}^\dagger\vert n\rangle = \sqrt{n+1}$,

$$
\langle n+1\vert\hat{V}\vert n\rangle = -\,\frac{qE_0\ell_B}{\sqrt{2}}\;\mathrm{i}\,\mathrm{e}^{-\mathrm{i}\omega t}\,\sqrt{n+1}.
$$

The factor $\mathrm{i}\,\mathrm{e}^{-\mathrm{i}\omega t}$ has unit modulus, so the squared matrix element is time-independent:

$$
\vert\langle n+1\vert\hat{V}\vert n\rangle\vert^2 = \frac{q^2 E_0^2\,\ell_B^2}{2}\,(n+1).
$$

It grows *linearly* with the initial Landau index, $\propto (n+1)$, because the matrix element itself scales as $\sqrt{n+1}$ — the same $\sqrt{n+1}$ enhancement that any harmonic-oscillator raising operator carries. Setting $\omega = \omega_c$ does not change this magnitude; resonance enters through energy conservation (the drive photon $\hbar\omega$ must match the level gap $\hbar\omega_c$ for the transition rate, via Fermi's golden rule, to be appreciable), while the coupling strength above is fixed by $\hat{a}^\dagger$ alone.

**(c)** The Landau ladder is perfectly uniform: $E_{n+1} - E_n = \hbar\omega_c$ for *every* $n$, an exact consequence of the harmonic-oscillator spectrum $E_n = \hbar\omega_c(n + \tfrac{1}{2})$. Every allowed absorption transition $n \to n+1$ therefore costs the same photon energy $\hbar\omega_c$, no matter which level the particle starts in. Whatever the temperature or filling — whichever levels happen to be occupied — all the transitions pile up at one and the same frequency, and the absorption spectrum shows a single sharp line at $\omega = \omega_c$. (The matrix element grows with $n$, so higher levels absorb more strongly, but they absorb at the *same* frequency; the peak position does not move.)

This is what makes cyclotron resonance a clean metrology tool. The resonance condition is $\omega_c = qB/m^\ast$, where $m^\ast$ is the (effective) mass of the carrier — in a crystal, the band effective mass rather than the bare electron mass. One applies a known magnetic field $B$, sweeps the microwave/far-infrared frequency $\omega$, and locates the sharp absorption peak at $\omega = \omega_c$. The effective mass then follows directly,

$$
m^\ast = \frac{qB}{\omega_c}.
$$

The sharpness is essential: because every transition contributes at exactly $\omega_c$, the line is narrow (limited only by scattering, $\omega_c\tau \gg 1$), and its centre can be located precisely. A non-uniform ladder would spread the transitions over a band of frequencies and blur the measurement. Cyclotron resonance is the standard technique for measuring carrier effective masses — and their anisotropy — in semiconductors and metals.

<!-- ─── -->

**3. Degeneracy and filling factor.** Each Landau level has degeneracy $N_\Phi = BA/\Phi_0$ on a sample of area $A$.

(a) Show that doubling $B$ doubles $N_\Phi$ and halves $\ell_B^2$. Interpret each effect physically (more states per level; tighter wavefunction).

(b) For a sample with fixed electron density $n_e = N_e/A$, define the **filling factor** $\nu = N_e/N_\Phi = n_e h/(qB)$. Why does $\nu$ decrease as $B$ increases?

(c) At $\nu = 1$, one full Landau level is occupied. Adding one more electron costs the gap $\hbar\omega_c$. Why does this gap make the system *incompressible* and produce a Hall-resistance plateau (anticipating §4.3.3)?

**Solution.**

**(a)** Both quantities are simple powers of $B$. The degeneracy $N_\Phi = BA/\Phi_0$ is linear in $B$ at fixed area $A$ and flux quantum $\Phi_0 = h/q$, so

$$
B \to 2B \quad\Longrightarrow\quad N_\Phi \to 2N_\Phi.
$$

The squared magnetic length $\ell_B^2 = \hbar/(qB)$ is inversely proportional to $B$, so

$$
B \to 2B \quad\Longrightarrow\quad \ell_B^2 \to \tfrac{1}{2}\ell_B^2.
$$

The two effects are the same fact seen twice. Each guiding-center state occupies an area of order $2\pi\ell_B^2$, and the number of such states tiling a sample of area $A$ is $N_\Phi = A/(2\pi\ell_B^2)$. Doubling $B$ halves $\ell_B^2$, which (i) shrinks each wavefunction — the cyclotron orbit and the guiding-center cell both tighten, since $\ell_B$ is the only intrinsic length — and (ii) therefore packs twice as many states into the same area, doubling $N_\Phi$. More flux threading the sample means more flux quanta, and each Landau level holds exactly one state per flux quantum: a stronger field literally creates more seats per level while squeezing each occupant into a smaller area.

**(b)** The filling factor is the ratio of electrons to available seats in one Landau level. With $N_e = n_e A$ and $N_\Phi = BA/\Phi_0$,

$$
\nu = \frac{N_e}{N_\Phi} = \frac{n_e A}{BA/\Phi_0} = \frac{n_e\,\Phi_0}{B} = \frac{n_e\,h}{qB},
$$

using $\Phi_0 = h/q$. At fixed density $n_e$, this is $\nu \propto 1/B$: raising the field lowers the filling factor. Physically, the electron count $N_e$ is held fixed, but the capacity per Landau level $N_\Phi \propto B$ grows with the field. The same electrons are spread over ever more degenerate states, so the *fraction* of states occupied — which is what $\nu$ measures — falls. Equivalently, $\nu$ counts how many Landau levels' worth of electrons are present; pushing $B$ up enlarges each level until the fixed population fills less and less of it.

**(c)** At $\nu = 1$ the lowest Landau level is exactly full and the next is entirely empty. The lowest unoccupied state does not sit just above the highest occupied one — it lies a full gap $\hbar\omega_c$ higher, in the next Landau level. Adding one more electron forces it into that next level at an energy cost $\hbar\omega_c$, which stays finite no matter how large the sample is.

*Incompressibility.* The (inverse) compressibility is governed by $\partial\mu/\partial N_e$, the energy needed per added particle. Within a partially filled level this is essentially zero — extra electrons cost nothing but Pauli reshuffling among degenerate states — but at $\nu = 1$ it jumps to $\hbar\omega_c$. The chemical potential is then free to sit anywhere in the gap without the electron number responding: $\partial N_e/\partial\mu = 0$. A system that refuses to change its density as the chemical potential is varied is, by definition, *incompressible*. The vanishing density of states at the Fermi level — no available states inside the gap — is the microscopic signature.

*Hall plateau.* The Hall conductivity counts filled Landau levels, $\sigma_{xy} = \nu\, e^2/h$, and at $\nu = 1$ it equals $e^2/h$. Because the system is gapped, small changes in $B$ (or in $n_e$) that merely move the Fermi level *within* the gap do not change the integer number of filled levels — so $\sigma_{xy}$ stays pinned at $e^2/h$ over a finite range of field rather than varying continuously. That flat stretch is the quantized Hall plateau. At the same time the longitudinal resistivity drops toward zero: with no states at the Fermi level, there is nothing for carriers to scatter into, so dissipation is frozen out. §4.3.3 develops how disorder broadens each level into a band of localized states, which is what *widens* the plateau into the experimentally observed finite range — but the seed of the plateau is exactly this energy gap at integer filling.

<!-- ─── -->

**4. Gauge equivalence.** The Landau gauge $\boldsymbol{A}_L = (0, Bx, 0)$ and the symmetric gauge $\boldsymbol{A}_S = \tfrac{B}{2}(-y, x, 0)$ both produce $\boldsymbol{B} = B\hat{z}$.

(a) Find the gauge function $\alpha(x, y)$ relating them, $\boldsymbol{A}_S = \boldsymbol{A}_L + \nabla\alpha$.

(b) Eigenstates in the Landau gauge are labeled by $\hat{p}_y$ (continuous translation in $y$); eigenstates in the symmetric gauge are labeled by $\hat{L}_z$ (rotation about origin). Both label the same Landau-level degeneracy $N_\Phi$. Explain how two different conserved quantities can label the *same* set of states.

(c) The combination $\hat{X}^2 + \hat{Y}^2 = \ell_B^2(2\hat{b}^\dagger\hat{b} + 1)$ measures the squared distance of the guiding center from the origin. Use this to argue that the symmetric-gauge $\hat{b}^\dagger\hat{b}$ quantum number is essentially $\hat{L}_z/\hbar$ in the lowest Landau level.

**Solution.**

**(a)** Take the difference of the two vector potentials:

$$
\boldsymbol{A}_S - \boldsymbol{A}_L = \frac{B}{2}(-y,\, x,\, 0) - (0,\, Bx,\, 0) = \left(-\frac{B}{2}y,\; -\frac{B}{2}x,\; 0\right).
$$

This must equal $\nabla\alpha$, i.e. $\partial_x\alpha = -\tfrac{B}{2}y$ and $\partial_y\alpha = -\tfrac{B}{2}x$. Integrating the first equation in $x$ gives $\alpha = -\tfrac{B}{2}xy + f(y)$; the second then requires $\partial_y\alpha = -\tfrac{B}{2}x + f'(y) = -\tfrac{B}{2}x$, so $f'(y) = 0$ and $f$ is an irrelevant constant. Hence

$$
\alpha(x, y) = -\frac{B}{2}\,xy.
$$

As a check, $\nabla\alpha = (-\tfrac{B}{2}y, -\tfrac{B}{2}x, 0)$ reproduces the difference above, and $\nabla\times\nabla\alpha = 0$ confirms that the change is pure gauge — both potentials yield the same $\boldsymbol{B} = B\hat{z}$. Accompanying this, the wavefunctions are related by the rephasing $\psi_S = \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\,\psi_L$.

**(b)** A Landau level is a single degenerate eigenspace of $\hat{H}$: an $N_\Phi$-dimensional subspace, every vector of which has the same energy $E_n = \hbar\omega_c(n + \tfrac{1}{2})$. Degeneracy means $\hat{H}$ alone does not pick out a basis — it is blind to any direction within that subspace. To *label* the states one needs a second operator that commutes with $\hat{H}$ and resolves the degeneracy, and the choice of that operator is exactly a choice of basis.

The two gauges supply two different such operators because they preserve two different symmetries. The Landau gauge $\boldsymbol{A}_L = (0, Bx, 0)$ is independent of $y$, so the Hamiltonian is invariant under translation in $y$; its generator $\hat{p}_y$ commutes with $\hat{H}_L$ and labels the eigenstates (strips of plane wave running along $y$). The symmetric gauge $\boldsymbol{A}_S = \tfrac{B}{2}(-y, x, 0)$ is invariant under rotation about the origin, so $\hat{L}_z$ commutes with $\hat{H}_S$ and labels *its* eigenstates (rings centered on the origin).

These two label operators do not commute with each other — translations and rotations are incompatible — so they diagonalize the degenerate subspace in *different* bases. But it is the *same* subspace: the Landau level, as a set of states, is gauge-invariant and basis-independent. The count $N_\Phi$ is a property of the subspace (its dimension), not of the labeling. Changing gauge is the unitary map $\psi \to \mathrm{e}^{\mathrm{i}q\alpha/\hbar}\psi$ of part (a); it rotates one basis into the other while leaving the spanned subspace, and hence $N_\Phi$, untouched. The situation is the familiar one of a spin multiplet that can be quantized along $\hat{z}$ or along $\hat{x}$: two incompatible labels, two bases, one and the same space of states.

**(c)** In the lowest Landau level the cyclotron motion is frozen in its ground state, $\hat{a}^\dagger\hat{a} = 0$ (this is what part (a) of Problem 1 verified for the states $\psi_m$). The particle's displacement from the origin is then the guiding-center displacement plus only a fixed zero-point cyclotron smear of size $\ell_B$ — the orbit sits essentially *at* its guiding center. The radial quantum number of the state is thus carried entirely by the guiding-center operator $\hat{X}^2 + \hat{Y}^2 = \ell_B^2(2\hat{b}^\dagger\hat{b} + 1)$, whose eigenvalue $(2m+1)\ell_B^2$ steps outward by $2\ell_B^2$ each time $\hat{b}^\dagger\hat{b} = m$ increases by one.

Now compare with angular momentum. An LLL state of guiding-center index $m$ is the ring-shaped $\psi_m \propto z^m\,\mathrm{e}^{-\vert z\vert^2/(4\ell_B^2)}$ of Problem 1, and there $\hat{L}_z\psi_m = m\hbar\,\psi_m$. So both $\hat{b}^\dagger\hat{b}$ and $\hat{L}_z/\hbar$ are non-negative-integer operators, both have the LLL states $\{\psi_m\}$ as their common eigenbasis, and both return the *same* eigenvalue $m$ on $\psi_m$. Two operators with the same eigenbasis and the same spectrum are the same operator on that space:

$$
\hat{b}^\dagger\hat{b} = \hat{L}_z/\hbar \qquad\text{(restricted to the lowest Landau level)}.
$$

Raising $\hat{L}_z$ by one unit of $\hbar$, raising $\hat{b}^\dagger\hat{b}$ by one, and pushing the guiding center one quantum of area $2\pi\ell_B^2$ farther from the origin are three descriptions of the single operation $\psi_m \to \psi_{m+1}$. Outside the LLL the identification fails, because the cyclotron rotation then carries angular momentum of its own; the general relation is $\hat{L}_z = \hbar(\hat{b}^\dagger\hat{b} - \hat{a}^\dagger\hat{a})$, and $\hat{b}^\dagger\hat{b} = \hat{L}_z/\hbar$ holds precisely where $\hat{a}^\dagger\hat{a} = 0$.

<!-- ─── -->

**5. Numerical scales.** Use $\ell_B = \sqrt{\hbar/(qB)} \approx 25.66\,\mathrm{nm}\,(1\,\mathrm{T}/B)^{1/2}$ for an electron.

(a) Compute $\ell_B$ at $B = 1\,\mathrm{T}$ and at $B = 10\,\mathrm{T}$.

(b) Compute $\hbar\omega_c$ at $B = 10\,\mathrm{T}$ for an electron, and convert to kelvin via $k_B T$. Comment on whether the QHE should be observable at $T = 4\,\mathrm{K}$.

(c) For a $1\,\mathrm{mm}^2$ sample at $B = 10\,\mathrm{T}$, compute $N_\Phi$ and compare to typical 2D electron densities $n_e \sim 10^{11}\,\mathrm{cm}^{-2}$ to estimate the filling factor.

**Solution.**

Throughout, use the electron values $e = 1.602\times10^{-19}\,\mathrm{C}$, $m_e = 9.109\times10^{-31}\,\mathrm{kg}$, $\hbar = 1.055\times10^{-34}\,\mathrm{J\,s}$, $h = 6.626\times10^{-34}\,\mathrm{J\,s}$, and $k_B = 1.381\times10^{-23}\,\mathrm{J/K}$.

**(a)** The magnetic length scales as $\ell_B \propto B^{-1/2}$. Reading off the given prefactor,

$$
\begin{split}
\ell_B(1\,\mathrm{T}) &\approx 25.66\,\mathrm{nm},\\
\ell_B(10\,\mathrm{T}) &\approx \frac{25.66\,\mathrm{nm}}{\sqrt{10}} \approx 8.11\,\mathrm{nm}.
\end{split}
$$

Both are nanometre-scale lengths — far larger than an atomic spacing ($\sim 0.3\,\mathrm{nm}$), yet far smaller than a micron-scale device. A tenfold increase in field shrinks $\ell_B$ only by $\sqrt{10} \approx 3.16$, the mild square-root dependence.

**(b)** The cyclotron frequency for an electron (bare mass) at $B = 10\,\mathrm{T}$ is

$$
\omega_c = \frac{eB}{m_e} = \frac{(1.602\times10^{-19})(10)}{9.109\times10^{-31}}\,\mathrm{s^{-1}} = 1.76\times10^{12}\,\mathrm{s^{-1}},
$$

so the Landau-level spacing is

$$
\hbar\omega_c = (1.055\times10^{-34})(1.76\times10^{12})\,\mathrm{J} = 1.85\times10^{-22}\,\mathrm{J} \approx 1.16\,\mathrm{meV}.
$$

Converting to a temperature through $\hbar\omega_c = k_B T$,

$$
T = \frac{\hbar\omega_c}{k_B} = \frac{1.85\times10^{-22}}{1.381\times10^{-23}}\,\mathrm{K} \approx 13.4\,\mathrm{K}.
$$

At $4\,\mathrm{K}$ the thermal energy is $k_B T \approx \hbar\omega_c/3.4$ — the Landau gap is about $3.4$ times the thermal energy. Thermal excitation across the gap is suppressed by the Boltzmann factor $\mathrm{e}^{-\hbar\omega_c/k_B T} \approx \mathrm{e}^{-3.4} \approx 0.03$, so the Landau levels are reasonably well resolved and the QHE should be observable at $4\,\mathrm{K}$ and $10\,\mathrm{T}$, with the cleanest plateaus appearing as the temperature is lowered further. (This estimate uses the *bare* electron mass; in a real GaAs device the band effective mass $m^\ast \approx 0.067\,m_e$ makes $\hbar\omega_c$ roughly fifteen times larger, putting the gap well above $4\,\mathrm{K}$ — the regime where the integer QHE is routinely seen.)

**(c)** The number of flux quanta through the sample is $N_\Phi = BA/\Phi_0$ with $\Phi_0 = h/e$. First the flux quantum,

$$
\Phi_0 = \frac{h}{e} = \frac{6.626\times10^{-34}}{1.602\times10^{-19}}\,\mathrm{Wb} = 4.14\times10^{-15}\,\mathrm{Wb}.
$$

For $A = 1\,\mathrm{mm}^2 = 10^{-6}\,\mathrm{m^2}$ at $B = 10\,\mathrm{T}$,

$$
N_\Phi = \frac{BA}{\Phi_0} = \frac{(10)(10^{-6})}{4.14\times10^{-15}} \approx 2.4\times10^{9}.
$$

Each Landau level holds about $2.4$ billion electron states. The electron count comes from the density $n_e \sim 10^{11}\,\mathrm{cm^{-2}} = 10^{15}\,\mathrm{m^{-2}}$:

$$
N_e = n_e A = (10^{15}\,\mathrm{m^{-2}})(10^{-6}\,\mathrm{m^2}) = 10^{9}.
$$

The filling factor is therefore

$$
\nu = \frac{N_e}{N_\Phi} = \frac{10^{9}}{2.4\times10^{9}} \approx 0.41,
$$

which agrees with the direct formula $\nu = n_e h/(eB) = n_e\Phi_0/B$. A filling factor below one means the electrons do not even fill the lowest Landau level — at $10\,\mathrm{T}$ such a sample sits in the strongly quantized regime, deep inside the lowest level, exactly where the rich physics of the (fractional) quantum Hall effect lives.

<!-- ─── -->

**6. Landau levels in graphene.** Specialize to electron carriers ($q = -e$ with $e > 0$) throughout this problem. Graphene's low-energy electrons obey a Dirac-like equation with linear dispersion $E = \hbar v_F k$, leading to Landau levels $E_n = \mathrm{sgn}(n)\,v_F\sqrt{2e\hbar\vert n\vert B}$ for $n = 0, \pm 1, \pm 2, \ldots$.

(a) Show the level spacing is *not* uniform: $E_1 - E_0 \neq E_2 - E_1$. For $B = 10\,\mathrm{T}$ and $v_F = 10^6\,\mathrm{m/s}$, compute $E_1$ in meV.

(b) The $n = 0$ level sits at exactly zero energy. Explain why this leads to a *half-integer* quantum Hall effect $\sigma_{xy} = (n + 1/2)\,4e^2/h$ (the factor 4 accounts for spin and valley).

(c) Compare $E_1$ in graphene to $\hbar\omega_c$ in GaAs at the same field. Why is the QHE observable at room temperature in graphene but requires millikelvins in GaAs?

**Solution.**

**(a)** For the positive branch the levels go as the *square root* of the index: $E_n = v_F\sqrt{2e\hbar n B} = E_1\sqrt{n}$ with $E_1 \equiv v_F\sqrt{2e\hbar B}$. The first few are $E_0 = 0$, $E_1$, $E_2 = \sqrt{2}\,E_1$, $E_3 = \sqrt{3}\,E_1$. The successive spacings are then

$$
\begin{split}
E_1 - E_0 &= E_1,\\
E_2 - E_1 &= (\sqrt{2} - 1)\,E_1 \approx 0.41\,E_1,
\end{split}
$$

which are manifestly unequal — the spacing *shrinks* as one climbs the ladder. This is the hallmark of the relativistic (Dirac) dispersion: the ordinary massive Landau ladder $E_n = \hbar\omega_c(n+\tfrac{1}{2})$ is evenly spaced because $E_n \propto n$, whereas graphene's $E_n \propto \sqrt{n}$ ladder is not.

Numerically, with $B = 10\,\mathrm{T}$, $v_F = 10^6\,\mathrm{m/s}$, $e = 1.602\times10^{-19}\,\mathrm{C}$, $\hbar = 1.055\times10^{-34}\,\mathrm{J\,s}$:

$$
\begin{split}
2e\hbar B &= 2(1.602\times10^{-19})(1.055\times10^{-34})(10) = 3.38\times10^{-52}\,\mathrm{(SI)},\\
E_1 &= v_F\sqrt{2e\hbar B} = (10^{6})\sqrt{3.38\times10^{-52}}\,\mathrm{J} = 1.84\times10^{-20}\,\mathrm{J}.
\end{split}
$$

Dividing by $e$ to convert,

$$
E_1 \approx \frac{1.84\times10^{-20}}{1.602\times10^{-19}}\,\mathrm{eV} \approx 0.115\,\mathrm{eV} = 115\,\mathrm{meV}.
$$

**(b)** Graphene's $n = 0$ Landau level sits exactly at the Dirac point, $E_0 = 0$. Unlike every other level it is shared symmetrically between the electron (conduction) and hole (valence) sides of the spectrum: it is half electron-like and half hole-like, and at the charge-neutrality point it is exactly half-filled.

The Hall conductivity counts the carriers in completely filled levels. In an ordinary 2D gas the levels lie entirely above the band bottom, and filling $N$ of them gives $\sigma_{xy} = N\cdot g\,e^2/h$ ($g$ the degeneracy). In graphene the zero-energy level straddles the neutrality point, so as the density is tuned away from neutrality the *first* plateau is reached after filling only the electron half of that shared level plus whichever higher levels follow. The whole integer staircase is consequently shifted by one half-step. Including the fourfold spin-and-valley degeneracy $g = 4$,

$$
\sigma_{xy} = \pm\Big(n + \tfrac{1}{2}\Big)\frac{4e^2}{h} = \pm\frac{2e^2}{h},\;\pm\frac{6e^2}{h},\;\pm\frac{10e^2}{h},\;\ldots
$$

The plateaus land at *half-integer* multiples of $4e^2/h$, and — crucially — there is no plateau at $\sigma_{xy} = 0$: the zero-energy level guarantees a step right at neutrality. This shifted, half-integer sequence is the experimental fingerprint of the Dirac zero-mode and is exactly what distinguishes graphene's "anomalous" quantum Hall effect from the conventional one.

**(c)** Put the two energy scales side by side at $B = 10\,\mathrm{T}$. Graphene's first Landau gap was found above, $E_1 \approx 115\,\mathrm{meV}$. For GaAs the spacing is the ordinary cyclotron value $\hbar\omega_c = \hbar e B/m^\ast$ with effective mass $m^\ast = 0.067\,m_e$:

$$
\hbar\omega_c^{\,\mathrm{GaAs}} = \frac{\hbar e B}{0.067\,m_e} \approx \frac{1.16\,\mathrm{meV}}{0.067} \approx 17\,\mathrm{meV},
$$

reusing the bare-electron $\hbar\omega_c = 1.16\,\mathrm{meV}$ from Problem 5(b). Graphene's gap is roughly *seven times* larger than GaAs's at the same field — and the difference is structural, not incidental. GaAs has a massive ladder with gap $\hbar\omega_c \propto B$, set by a small but finite effective mass; graphene has a relativistic ladder with $E_1 \propto \sqrt{B}$, set by the Fermi velocity, and the square-root law delivers a very large first gap even at modest fields.

Convert to temperature. Graphene's $E_1 \approx 115\,\mathrm{meV}$ corresponds to $E_1/k_B \approx 1300\,\mathrm{K}$, far above room temperature ($k_B\cdot300\,\mathrm{K} \approx 26\,\mathrm{meV}$); thermal smearing across the gap at $300\,\mathrm{K}$ is suppressed by $\mathrm{e}^{-115/26} \approx \mathrm{e}^{-4.4} \approx 0.01$. The Landau levels stay sharply resolved, and the integer QHE is indeed observed in graphene at room temperature. GaAs's $\sim 17\,\mathrm{meV}$ gap is comparable to room-temperature thermal energy and, more importantly, is easily washed out by disorder broadening of the levels, so well-defined plateaus demand cryogenic temperatures. The *fractional* QHE is more stringent still: it relies on interaction-generated gaps of only a fraction of a meV, which is why the delicate fractional states in GaAs are resolved only at millikelvin temperatures. The single linear-dispersion fact — graphene electrons are effectively massless Dirac particles — is what lifts its quantum Hall physics from the millikelvin lab bench to the tabletop at $300\,\mathrm{K}$.
