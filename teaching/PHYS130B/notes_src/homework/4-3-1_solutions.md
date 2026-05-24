# 4.3.1 Cyclotron Motion
Worked solutions for the homework problems in the [4.3.1 Cyclotron Motion](../ch4_phase-and-gauge/4-3-1-cyclotron-motion) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Cyclotron drift in crossed fields.** A particle of charge $q$ moves in uniform fields $\boldsymbol{B} = B\hat{z}$ and $\boldsymbol{E} = E\hat{x}$.

(a) Solve $m\dot{\boldsymbol{v}} = q(\boldsymbol{E} + \boldsymbol{v}\times\boldsymbol{B})$ for the steady drift velocity. Show it equals $\boldsymbol{v}_d = \boldsymbol{E}\times\boldsymbol{B}/B^2$, *independent of charge or mass*.

(b) Show that the full motion is circular cyclotron orbits (radius set by initial perpendicular speed, frequency $\omega_c = |q|B/m$) superimposed on this drift.

(c) Explain why this drift is the classical analog of Hall transport: a steady current perpendicular to $\boldsymbol{E}$ with no acceleration. Why does it not dissipate energy?

**Solution.**

**(a)** In the steady state the drift velocity $\boldsymbol{v}_d$ is constant, so $\dot{\boldsymbol{v}} = 0$ and the Lorentz equation collapses to a pure force balance,

$$
\boldsymbol{E} + \boldsymbol{v}_d\times\boldsymbol{B} = 0.
$$

To solve for $\boldsymbol{v}_d$, cross both sides with $\boldsymbol{B}$ on the right:

$$
\boldsymbol{E}\times\boldsymbol{B} + (\boldsymbol{v}_d\times\boldsymbol{B})\times\boldsymbol{B} = 0.
$$

The double cross product expands by the BAC-CAB identity,

$$
(\boldsymbol{v}_d\times\boldsymbol{B})\times\boldsymbol{B} = \boldsymbol{B}\,(\boldsymbol{v}_d\cdot\boldsymbol{B}) - \boldsymbol{v}_d\,(\boldsymbol{B}\cdot\boldsymbol{B}).
$$

The crossed-field drift lies in the plane perpendicular to $\boldsymbol{B}$ — any velocity component along $\hat{z}$ is unaccelerated and decouples from the problem — so $\boldsymbol{v}_d\cdot\boldsymbol{B} = 0$. This leaves

$$
\boldsymbol{E}\times\boldsymbol{B} - B^2\,\boldsymbol{v}_d = 0
\quad\Longrightarrow\quad
\boldsymbol{v}_d = \frac{\boldsymbol{E}\times\boldsymbol{B}}{B^2}.
$$

For the given orientation $\boldsymbol{E} = E\hat{x}$, $\boldsymbol{B} = B\hat{z}$, and using $\hat{x}\times\hat{z} = -\hat{y}$,

$$
\boldsymbol{v}_d = \frac{EB\,(\hat{x}\times\hat{z})}{B^2} = -\frac{E}{B}\,\hat{y}.
$$

The result contains neither $q$ nor $m$. Physically, both terms in the force balance — the electric force $q\boldsymbol{E}$ and the magnetic force $q\,\boldsymbol{v}_d\times\boldsymbol{B}$ — are proportional to $q$, so the charge cancels out of the balance condition; and the mass never appears because it multiplies the acceleration, which vanishes in steady state. Every charged species, regardless of sign or mass, drifts together at the common velocity $\boldsymbol{E}\times\boldsymbol{B}/B^2$.

**(b)** Split the velocity into the constant drift plus a remainder, $\boldsymbol{v} = \boldsymbol{v}_d + \boldsymbol{u}$. Substituting into $m\dot{\boldsymbol{v}} = q(\boldsymbol{E} + \boldsymbol{v}\times\boldsymbol{B})$ and using $\dot{\boldsymbol{v}}_d = 0$,

$$
\begin{split}
m\dot{\boldsymbol{u}} &= q\bigl(\boldsymbol{E} + (\boldsymbol{v}_d + \boldsymbol{u})\times\boldsymbol{B}\bigr)\\
&= q\,(\boldsymbol{E} + \boldsymbol{v}_d\times\boldsymbol{B}) + q\,\boldsymbol{u}\times\boldsymbol{B}\\
&= q\,\boldsymbol{u}\times\boldsymbol{B}.
\end{split}
$$

The bracket $\boldsymbol{E} + \boldsymbol{v}_d\times\boldsymbol{B}$ vanishes identically — that was the defining condition for $\boldsymbol{v}_d$ in part (a) — so the remainder $\boldsymbol{u}$ obeys the *pure* cyclotron equation $m\dot{\boldsymbol{u}} = q\,\boldsymbol{u}\times\boldsymbol{B}$, with the electric field entirely absorbed into the drift. This is exactly the equation solved in the lecture for $\boldsymbol{B} = B\hat{z}$: its in-plane solution is uniform circular motion at the cyclotron frequency $\omega_c = |q|B/m$, with radius

$$
r_c = \frac{u_\perp}{\omega_c},
$$

where $u_\perp$ is the magnitude of the in-plane part of $\boldsymbol{u}$ at $t = 0$ — that is, the initial velocity measured *relative to the drift frame*. The full trajectory is therefore a circular cyclotron orbit whose guiding centre is not stationary but translates uniformly at $\boldsymbol{v}_d$. Tracing a circle while its centre slides at constant velocity produces a cycloid.

**(c)** The drift velocity $\boldsymbol{v}_d = -(E/B)\hat{y}$ points *perpendicular* to the applied field $\boldsymbol{E} = E\hat{x}$. It carries a steady current density $\boldsymbol{j} = nq\boldsymbol{v}_d$ that flows transverse to the electric field rather than along it — precisely the geometry of Hall transport, in which a longitudinal field drives a transverse current. The guiding centre moves at constant velocity, so this is a true steady state with no acceleration, not a transient.

The motion does not dissipate energy. The rate at which the electric field does work on a carrier is $\boldsymbol{F}_E\cdot\boldsymbol{v} = q\,\boldsymbol{E}\cdot\boldsymbol{v}$. For the drift part, $\boldsymbol{E}\cdot\boldsymbol{v}_d \propto \hat{x}\cdot\hat{y} = 0$; for the cyclotron part $\boldsymbol{u}$, the velocity is purely oscillatory, so $\boldsymbol{E}\cdot\boldsymbol{u}$ averages to zero over each orbit. The magnetic force, being perpendicular to the velocity, does no work at all. Hence the carrier's kinetic energy stays bounded and the transverse current flows with no Joule heating. This collisionless $\boldsymbol{E}\times\boldsymbol{B}$ drift is the classical precursor of the *dissipationless* transverse transport realised on quantum Hall plateaus, where the longitudinal resistivity $\rho_{xx}$ drops to zero.

<!-- ─── -->

**2. Helical motion and scales.** A proton enters a $2\,\mathrm{T}$ field with velocity components $v_\perp=10^6\,\mathrm{m/s}$ and $v_\parallel=5\times10^5\,\mathrm{m/s}$.

(a) Compute cyclotron radius and period.

(b) Compute helix pitch.

(c) Repeat radius estimate for Earth field $B\sim 50\,\mu\mathrm{T}$ and compare qualitatively to laboratory scales.

**Solution.**

Treat the proton as a charge $q = e = 1.602\times10^{-19}\,\mathrm{C}$ of mass $m_p = 1.673\times10^{-27}\,\mathrm{kg}$, moving in $B = 2\,\mathrm{T}$.

**(a)** The cyclotron frequency is

$$
\omega_c = \frac{eB}{m_p} = \frac{(1.602\times10^{-19})(2)}{1.673\times10^{-27}}\,\mathrm{s^{-1}} = 1.92\times10^{8}\,\mathrm{s^{-1}}.
$$

The period and radius follow directly:

$$
\begin{split}
T_c &= \frac{2\pi}{\omega_c} = 3.28\times10^{-8}\,\mathrm{s} \approx 33\,\mathrm{ns},\\
r_c &= \frac{v_\perp}{\omega_c} = \frac{10^{6}\,\mathrm{m/s}}{1.92\times10^{8}\,\mathrm{s^{-1}}} = 5.2\times10^{-3}\,\mathrm{m} \approx 5.2\,\mathrm{mm}.
\end{split}
$$

Only the perpendicular speed $v_\perp$ enters $r_c$; the parallel motion is not bent by the field. Note also that $\omega_c$ and $T_c$ are independent of speed entirely — every proton at $2\,\mathrm{T}$ completes a turn in $33\,\mathrm{ns}$.

**(b)** The pitch is the axial distance advanced in one full cyclotron turn,

$$
p = v_\parallel\,T_c = (5\times10^{5}\,\mathrm{m/s})(3.28\times10^{-8}\,\mathrm{s}) = 1.6\times10^{-2}\,\mathrm{m} \approx 1.6\,\mathrm{cm}.
$$

The trajectory is a helix of radius $5.2\,\mathrm{mm}$ and pitch $1.6\,\mathrm{cm}$. The pitch is comparable to the orbit diameter ($\approx 1.0\,\mathrm{cm}$), a fairly "open" helix, as expected since $v_\parallel$ and $v_\perp$ differ only by a factor of two.

**(c)** Since $r_c = m_p v_\perp/(eB) \propto 1/B$, reducing the field from $2\,\mathrm{T}$ to the geomagnetic value $B \sim 50\,\mu\mathrm{T}$ — a drop by a factor of $4\times10^{4}$ — enlarges the radius by the same factor:

$$
r_c^{\,\mathrm{Earth}} = \frac{m_p v_\perp}{eB} = \frac{(1.673\times10^{-27})(10^{6})}{(1.602\times10^{-19})(5\times10^{-5})}\,\mathrm{m} \approx 2.1\times10^{2}\,\mathrm{m}.
$$

A proton that orbits within a few millimetres inside a laboratory magnet spirals over *hundreds of metres* in Earth's field. The contrast is the practical reason cyclotron physics is laboratory-accessible: strong lab fields squeeze cyclotron orbits down to sub-centimetre scales, small enough to fit inside an apparatus and — once the field is strong enough — small enough for Landau quantization to matter. In the weak geomagnetic field the same particle's orbit is macroscopic, the regime relevant to cosmic-ray trajectories and charged-particle confinement in the magnetosphere.

<!-- ─── -->

**3. Drude resistivity and Hall robustness.** In Drude theory at uniform $\boldsymbol{B} = B\hat{z}$ with relaxation time $\tau$, the steady-state equation of motion for a carrier of charge $q$ is $m\boldsymbol{v}/\tau = q(\boldsymbol{E} + \boldsymbol{v}\times\boldsymbol{B})$.

(a) Solve for $\boldsymbol{v}$ and compute the conductivity tensor $\sigma_{ij}$ from $\boldsymbol{j} = nq\boldsymbol{v} = \sigma\boldsymbol{E}$.

(b) Invert to find the resistivity tensor and show that $\rho_{xy}^{\mathrm{cl}} = B/(nq)$ — *independent of $\tau$*. Explain physically why disorder cannot affect the classical Hall resistivity.

(c) The longitudinal resistivity $\rho_{xx}$ does depend on $\tau$. Explain why this is consistent with the classical picture but inconsistent with the observed *vanishing* of $\rho_{xx}$ on quantum-Hall plateaus.

**Solution.**

**(a)** Keep the motion in the plane perpendicular to $\boldsymbol{B} = B\hat{z}$. With $\boldsymbol{v}\times\boldsymbol{B} = (v_y B)\hat{x} - (v_x B)\hat{y}$, the steady-state Drude equation has components

$$
\begin{split}
\frac{m}{\tau}\,v_x &= q E_x + q B v_y,\\
\frac{m}{\tau}\,v_y &= q E_y - q B v_x.
\end{split}
$$

Divide through by $m/\tau$ and abbreviate the mobility $\mu = q\tau/m$ and the dimensionless parameter $\omega_c\tau = qB\tau/m$:

$$
\begin{split}
v_x &= \mu E_x + \omega_c\tau\,v_y,\\
v_y &= \mu E_y - \omega_c\tau\,v_x.
\end{split}
$$

Substituting the second equation into the first and solving the resulting linear pair,

$$
\begin{split}
v_x &= \frac{\mu}{1+(\omega_c\tau)^2}\bigl(E_x + \omega_c\tau\,E_y\bigr),\\
v_y &= \frac{\mu}{1+(\omega_c\tau)^2}\bigl(E_y - \omega_c\tau\,E_x\bigr).
\end{split}
$$

The current density is $\boldsymbol{j} = nq\boldsymbol{v}$, so reading off $j_i = \sigma_{ij}E_j$ and writing the zero-field Drude conductivity $\sigma_0 = nq\mu = nq^2\tau/m$,

$$
\sigma = \frac{\sigma_0}{1+(\omega_c\tau)^2}
\begin{pmatrix} 1 & \omega_c\tau \\ -\omega_c\tau & 1 \end{pmatrix},
\qquad
\sigma_0 = \frac{nq^2\tau}{m}.
$$

**(b)** Invert the conductivity tensor. Write $w = \omega_c\tau$, so that $\sigma$ is the scalar prefactor $\sigma_0/(1+w^2)$ times the matrix $M = \begin{pmatrix} 1 & w \\ -w & 1 \end{pmatrix}$. The inverse of $M$ is

$$
M^{-1} = \frac{1}{1+w^2}\begin{pmatrix} 1 & -w \\ w & 1 \end{pmatrix},
$$

and the prefactor inverts to $(1+w^2)/\sigma_0$. The two factors of $(1+w^2)$ cancel, leaving the resistivity tensor

$$
\rho = \sigma^{-1} = \frac{1}{\sigma_0}\begin{pmatrix} 1 & -w \\ w & 1 \end{pmatrix}.
$$

Its independent components are

$$
\begin{split}
\rho_{xx} &= \frac{1}{\sigma_0} = \frac{m}{nq^2\tau},\\
\rho_{xy}^{\mathrm{cl}} &= \frac{w}{\sigma_0} = \frac{(qB/m)\,\tau}{nq^2\tau/m} = \frac{B}{nq},
\end{split}
$$

where $\rho_{xy}^{\mathrm{cl}}$ is the off-diagonal Hall component — in the lecture's convention $E_y/j_x$ measured with the current driven along $x$. The relaxation time $\tau$ enters $\rho_{xy}^{\mathrm{cl}}$ in two places, once through $w = \omega_c\tau$ in the numerator and once through $\sigma_0 \propto \tau$ in the denominator, and the two cancel exactly: $\rho_{xy}^{\mathrm{cl}} = B/(nq)$ is the lecture result and carries no dependence on $\tau$.

Physically, the Hall resistivity is fixed by transverse force balance, not by scattering. A carrier drifting at speed $v_x$ feels a transverse magnetic force $qv_xB$; in steady state this must be cancelled by the transverse Hall field, $qE_y = qv_xB$. That balance is a *kinematic* condition — it holds for each carrier regardless of how often it collides. Scattering relaxes longitudinal momentum, and therefore sets the longitudinal resistivity $\rho_{xx}$, but it has no handle on the transverse balance. The classical Hall resistivity $B/(nq)$ counts only the field strength $B$ and the carrier density $n$ (and charge sign $q$); it is blind to disorder because disorder enters only through $\tau$, which has cancelled.

**(c)** The longitudinal resistivity $\rho_{xx} = m/(nq^2\tau)$ does depend on $\tau$, and this is exactly right classically: longitudinal resistance *is* the momentum-relaxing friction of scattering, so dirtier samples (shorter $\tau$) have larger $\rho_{xx}$. Crucially, for any normal conductor with finite $\tau$ the Drude $\rho_{xx}$ is strictly positive — it can never reach zero.

This is where the classical picture breaks against experiment. On a quantum-Hall plateau the measured $\rho_{xx}$ drops to *zero* while $\rho_{xy}$ sits on a quantized value. A vanishing $\rho_{xx}$ means current flowing with no longitudinal dissipation, which the Drude model structurally cannot produce: its entire resistive mechanism is dissipative scattering, and $\rho_{xx} = m/(nq^2\tau) \to 0$ only in the unphysical limit $\tau\to\infty$ (no scattering at all). The actual resolution is quantum. When the Fermi level lies in a gap between Landau levels — or among the localized states that fill the gap in a disordered sample — there are no available final states into which a carrier can backscatter at low energy. Momentum relaxation is frozen out, so $\rho_{xx}\to 0$ even though the sample is disordered. The Drude model has neither a Landau-level ladder nor an energy gap, so its longitudinal resistivity is incapable of vanishing; the plateau regime lies outside classical transport theory altogether.

<!-- ─── -->

**4. Misconception: heavier particle, larger orbit.** One might claim: "A heavier particle in the same magnetic field has a larger cyclotron radius because it 'wants to go straight more.'" Test this claim by computing $r_c$ as a function of mass $m$ at fixed (i) speed $v_\perp$, (ii) momentum $p_\perp$, (iii) kinetic energy $K = mv_\perp^2/2$. Which framing supports the claim and which contradicts it? Explain why the right framing depends on what is held fixed.

**Solution.**

The cyclotron radius is $r_c = mv_\perp/(qB)$. Its dependence on mass is *not* absolute — it depends entirely on which other quantity is held fixed while $m$ is varied.

**(i) Fixed perpendicular speed $v_\perp$.** Then $r_c = mv_\perp/(qB) \propto m$. Doubling the mass doubles the radius. **This framing supports the claim.**

**(ii) Fixed perpendicular momentum $p_\perp = mv_\perp$.** Rewriting the radius in terms of momentum,

$$
r_c = \frac{mv_\perp}{qB} = \frac{p_\perp}{qB},
$$

which contains no $m$ at all. A heavier particle traces the *same* circle. **This framing contradicts the claim.**

**(iii) Fixed kinetic energy $K = \tfrac{1}{2}mv_\perp^2$.** Here $v_\perp = \sqrt{2K/m}$, so the momentum is $p_\perp = mv_\perp = \sqrt{2mK}$ and

$$
r_c = \frac{\sqrt{2mK}}{qB} \propto \sqrt{m}.
$$

A heavier particle has a larger radius, though only as $\sqrt{m}$ rather than linearly. **This framing supports the claim**, more weakly.

The deciding fact is that the cyclotron radius is set by *momentum*, not by mass. Balancing the magnetic force against the centripetal requirement, $qv_\perp B = mv_\perp^2/r_c$, gives $r_c = mv_\perp/(qB) = p_\perp/(qB)$ — a clean statement with no leftover mass. Whether "heavier" implies "bigger orbit" therefore reduces to a single question: does making the particle heavier also raise its momentum? At fixed speed it does, and proportionally ($p_\perp\propto m$); at fixed energy it does, but only as $\sqrt{m}$; at fixed momentum, by construction, it does not. The intuition "it wants to go straight more" appeals to inertia — mass — but the cyclotron radius does not care about mass except through the momentum. The honest one-line summary is $r_c = p_\perp/(qB)$: the cyclotron radius is a disguised momentum, and the claim is true only when the comparison holds speed or energy fixed, and false when it holds momentum fixed.

<!-- ─── -->

**5. Bridge to quantum scales.** Use simple estimates to identify when the classical picture should fail.

(a) Estimate $\hbar\omega_c$ at $B=10\,\mathrm{T}$ for an electron, and convert it to kelvin via $k_B T$.

(b) Compute $\ell_B=\sqrt{\hbar/(eB)}$ at $1\,\mathrm{T}$ and $10\,\mathrm{T}$.

(c) Explain why the pair $(\omega_c,\ell_B)$ already suggests a quantum state-counting picture, to be derived in §4.3.2.

**Solution.**

Use electron values $e = 1.602\times10^{-19}\,\mathrm{C}$, $m_e = 9.109\times10^{-31}\,\mathrm{kg}$, $\hbar = 1.055\times10^{-34}\,\mathrm{J\,s}$, and $k_B = 1.381\times10^{-23}\,\mathrm{J/K}$.

**(a)** At $B = 10\,\mathrm{T}$ the cyclotron frequency is

$$
\omega_c = \frac{eB}{m_e} = \frac{(1.602\times10^{-19})(10)}{9.109\times10^{-31}}\,\mathrm{s^{-1}} = 1.76\times10^{12}\,\mathrm{s^{-1}},
$$

so the cyclotron energy quantum — the spacing of the Landau ladder anticipated in lecture — is

$$
\hbar\omega_c = (1.055\times10^{-34})(1.76\times10^{12})\,\mathrm{J} = 1.85\times10^{-22}\,\mathrm{J} \approx 1.2\,\mathrm{meV}.
$$

Converting to a temperature through $\hbar\omega_c = k_B T$,

$$
T = \frac{\hbar\omega_c}{k_B} = \frac{1.85\times10^{-22}}{1.381\times10^{-23}}\,\mathrm{K} \approx 13\,\mathrm{K}.
$$

At $10\,\mathrm{T}$ the cyclotron quantum corresponds to roughly $13\,\mathrm{K}$. The classical continuous Hall response holds only while thermal smearing dominates, $k_B T \gg \hbar\omega_c$; the discrete Landau structure becomes resolved once $T \lesssim 13\,\mathrm{K}$. This is the quantitative reason the quantum Hall effect is observed at liquid-helium temperatures and strong fields, not at room temperature.

**(b)** The magnetic length $\ell_B = \sqrt{\hbar/(eB)}$ evaluates to

$$
\begin{split}
\ell_B(1\,\mathrm{T}) &= \sqrt{\frac{1.055\times10^{-34}}{(1.602\times10^{-19})(1)}}\,\mathrm{m} = 2.57\times10^{-8}\,\mathrm{m} \approx 26\,\mathrm{nm},\\
\ell_B(10\,\mathrm{T}) &= \frac{\ell_B(1\,\mathrm{T})}{\sqrt{10}} \approx 8.1\,\mathrm{nm},
\end{split}
$$

using $\ell_B \propto B^{-1/2}$. These are nanometre-scale lengths — far larger than an atomic spacing, but small compared with a micron-scale device.

**(c)** The two scales together already force a quantum state-counting picture, before any detailed calculation. The frequency $\omega_c$ supplies a discrete *energy* quantum $\hbar\omega_c$: a charged particle in a magnetic field is, dynamically, a harmonic oscillator (the lecture shows each velocity component obeys $\ddot{v} = -\omega_c^2 v$), and the harmonic oscillator is the prototype of an evenly spaced energy ladder. One therefore expects discrete Landau levels $E_n = (n+\tfrac{1}{2})\hbar\omega_c$ rather than a continuum. The length $\ell_B$ supplies a discrete *spatial* quantum: each quantum state occupies an area of order $\ell_B^2$, so a finite sample of area $A$ can hold only a *finite* number of states per level,

$$
N_\Phi = \frac{A}{2\pi\ell_B^2} = \frac{BA}{\Phi_0}, \qquad \Phi_0 = \frac{h}{e},
$$

that is, the degeneracy of each Landau level equals the number of magnetic flux quanta threading the sample. A discrete energy ladder with a finite, countable degeneracy on every rung is exactly a state-counting picture: fill an integer number of levels and the transport acquires an integer label. The decisive clue is that $\hbar$ appears in *both* $\hbar\omega_c$ and $\ell_B$, whereas the purely classical scales $\omega_c$ and $r_c$ contain no $\hbar$ — the quantum constant entering both the energy and the length signals that the correct description is a countable set of quantum states. The lecture defers the quantitative derivation of the Landau levels and the degeneracy $N_\Phi$ to §4.3.2.
