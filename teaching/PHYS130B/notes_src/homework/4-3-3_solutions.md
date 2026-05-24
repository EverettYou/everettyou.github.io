# 4.3.3 Quantum Hall Effect
Worked solutions for the homework problems in the [4.3.3 Quantum Hall Effect](../ch4_phase-and-gauge/4-3-3-quantum-hall-effect) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Filling factor.** A 2D electron system with density $n_e = 2.4\times 10^{15}\,\mathrm{m}^{-2}$ is placed in a perpendicular field $B = 5\,\mathrm{T}$.

(a) Compute the flux-quantum density $n_\Phi = eB/h$ and the filling factor $\nu = n_e/n_\Phi$.

(b) How many Landau levels are completely filled? Is the system at integer $\nu$?

(c) At what magnetic field $B^*$ would $\nu = 1$? At what field would $\nu = 1/3$?

**Solution.**

Throughout, $e = 1.602\times10^{-19}\,\mathrm{C}$ is the elementary-charge magnitude and $h = 6.626\times10^{-34}\,\mathrm{J\,s}$.

**(a)** The flux-quantum density is the number of flux quanta $\Phi_0 = h/e$ piercing unit area, $n_\Phi = B/\Phi_0 = eB/h$ — which is exactly the degeneracy per area of one Landau level. At $B = 5\,\mathrm{T}$,

$$
\begin{split}
n_\Phi &= \frac{eB}{h} = \frac{(1.602\times10^{-19})(5)}{6.626\times10^{-34}}\,\mathrm{m}^{-2} \approx 1.21\times10^{15}\,\mathrm{m}^{-2},\\
\nu &= \frac{n_e}{n_\Phi} = \frac{2.4\times10^{15}}{1.21\times10^{15}} \approx 1.99.
\end{split}
$$

Equivalently $\nu = n_e h/(eB)$, the form quoted in the lecture as Eq. `eq-filling-factor`.

**(b)** With $\nu \approx 1.99$, the lowest Landau level ($n = 0$) is completely filled — it holds exactly $n_\Phi$ states per area, contributing $1$ to $\nu$ — and the next level ($n = 1$) is filled to about $99\%$ of its capacity. So strictly **one** Landau level is completely filled, and the system is **not** exactly at integer $\nu$: it sits just below $\nu = 2$. (The slight shortfall is an artifact of the rounded input data; $\nu = 2$ exactly would need $n_e = 2 n_\Phi = 2.418\times10^{15}\,\mathrm{m}^{-2}$.) In a real disordered sample this distinction is largely cosmetic: because Hall plateaus have finite width in $B$ (Problem 2), a system this close to $\nu = 2$ would be measured squarely on the $\nu = 2$ plateau with $\sigma_{xy} = 2e^2/h$.

**(c)** Solve $\nu = n_e h/(eB)$ for the field, $B^* = n_e h/(e\nu)$. The density $n_e$ is held fixed; only $B$ is tuned.

$$
\begin{split}
B^*(\nu = 1) &= \frac{n_e h}{e} = \frac{(2.4\times10^{15})(6.626\times10^{-34})}{1.602\times10^{-19}}\,\mathrm{T} \approx 9.93\,\mathrm{T},\\
B^*(\nu = 1/3) &= 3\,\frac{n_e h}{e} \approx 29.8\,\mathrm{T}.
\end{split}
$$

Lowering $\nu$ from $2$ toward $1$ requires a *larger* field, because raising $B$ increases the per-level degeneracy $n_\Phi$ and so packs the fixed electrons into fewer levels. Reaching the fractional state $\nu = 1/3$ needs roughly $30\,\mathrm{T}$ — fields in this range, together with high-mobility samples, are exactly what the fractional quantum Hall regime demands.

<!-- ─── -->

**2. Disorder and plateau width.** Without disorder, the Hall conductance jumps at integer $\nu$ but spends zero "time" at each plateau as $B$ varies. With disorder, plateaus widen.

(a) Explain how disorder broadens each Landau level into a band, with localized states in the tails and extended states near the center.

(b) As $B$ decreases from a value where $\nu = 2$ exactly, why does $\sigma_{xy}$ remain at $2\,e^2/h$ over a finite interval rather than dropping continuously?

(c) Where in the level structure do plateau-to-plateau transitions occur? What role do extended states play?

**Solution.**

**(a)** In a perfectly clean 2D system every Landau level is a single sharp energy $E_n = (n + \tfrac{1}{2})\hbar\omega_c$ carrying a macroscopic degeneracy $N_\Phi$ — the density of states is a row of delta functions. A static disorder potential $V(\boldsymbol{r})$ shifts the energy of each localized cyclotron orbit by the local value of $V$ at its guiding center. Orbits sitting in deep valleys of $V$ are pushed below $E_n$; orbits on hills are pushed above. The single delta function therefore spreads into a **band** of width $\Gamma$ set by the disorder strength.

The character of the states depends on where they land in the band. A state in the **tail** has an energy far from the typical potential value; classically its guiding center drifts along a closed equipotential contour encircling a single puddle (a deep minimum) or a single hilltop. That contour is small and closed, so the state is **localized** — its wavefunction is confined to a finite region and decays exponentially outside it. A state near the **band center** has an energy close to the percolation threshold of the random landscape: its equipotential contour is a single connected curve that snakes across the entire sample. That state is **extended** — it spans the system from edge to edge.

**(b)** As $B$ decreases at fixed electron number, the per-level degeneracy $N_\Phi = eBA/h$ shrinks, so the filling factor $\nu = N_e/N_\Phi$ *rises* above $2$ and the Fermi level $E_F$ must climb into the $n = 2$ band. But it enters that band through the **lower tail**, which is populated by localized states. Putting electrons into localized states changes the total electron count, yet localized states carry no current from one edge of the sample to the other — they are tied to local puddles. The current-carrying capacity of the sample is therefore unchanged, and $\sigma_{xy}$ stays pinned at $2\,e^2/h$.

The plateau persists for the whole interval of $B$ over which $E_F$ traverses localized states — first the upper localized tail of the $n = 1$ band, then the lower localized tail of the $n = 2$ band. Only when $E_F$ finally reaches the *extended* states at the $n = 2$ band center does the Hall conductance move. The width of that localized-state window, measured in $B$, is the **plateau width**. With no disorder there are no localized states, the window has zero width, and $\sigma_{xy}$ would jump discontinuously — "spending zero time" at each plateau.

**(c)** Plateau-to-plateau transitions happen precisely when $E_F$ sweeps through the **extended states at a Landau-level band center**. Those are the only states that conduct charge across the sample, so they are the only states whose occupation can change the Hall conductance. Each time $E_F$ crosses a band of extended states, one more set of current-carrying states becomes filled and $\sigma_{xy}$ steps by $e^2/h$. Between two such crossings $E_F$ lies among localized states only, and $\sigma_{xy}$ is exactly constant. In this picture the extended states act as the "switches" of the staircase: razor-thin in energy, they carry the topological jump, while the broad surrounding sea of localized states supplies the flat treads of finite width.

<!-- ─── -->

**3. Charge pumping in detail.** Laughlin's argument threads flux $\Phi$ through a Corbino disk at filling $\nu$.

(a) Compute the EMF around the inner edge as $\Phi$ ramps from $0$ to $\Phi_0$ over time $T$.

(b) The Hall response converts the azimuthal EMF into a radial current. Show that the total charge transferred from inner to outer edge over the cycle is $Q = \sigma_{xy}\,\Phi_0$.

(c) Single-valuedness of the many-body state forces $Q$ to be an integer multiple of $e$. Use this to derive $\sigma_{xy} = N e^2/h$, then identify $N = \nu$ from particle-counting.

(d) Extend the argument heuristically to $\nu = 1/3$: why must $Q = e/3$ per flux quantum, and what does this imply about quasiparticle charge?

**Solution.**

**(a)** Faraday's law states that the electromotive force around any closed loop equals minus the rate of change of the flux it encloses, $\mathcal{E} = -\,\mathrm{d}\Phi/\mathrm{d}t$. The flux is threaded through the central hole, so every loop in the annulus — including the inner edge — encloses the full $\Phi(t)$. Ramping it linearly, $\Phi(t) = \Phi_0\,t/T$, gives a constant rate, hence a constant EMF of magnitude

$$
\vert\mathcal{E}\vert = \frac{\mathrm{d}\Phi}{\mathrm{d}t} = \frac{\Phi_0}{T} = \frac{h}{eT}.
$$

The EMF is azimuthal (it drives charge *around* the annulus) and is the same around the inner edge, the outer edge, or any circle in between, since all enclose the same threaded flux.

**(b)** On a quantum Hall plateau the longitudinal conductivity vanishes ($\sigma_{xx} = 0$, the bulk is gapped), so the only response to the azimuthal field is a *transverse* — here radial — current, governed by the Hall law $j_r = \sigma_{xy}\,E_\varphi$. Integrate this around a circle of radius $r$ in the annulus. The total radial current crossing that circle is

$$
I_r = 2\pi r\,j_r = \sigma_{xy}\,\bigl(2\pi r\,E_\varphi\bigr) = \sigma_{xy}\,\frac{\mathrm{d}\Phi}{\mathrm{d}t},
$$

because the line integral of the azimuthal field, $2\pi r\,E_\varphi$, is exactly the EMF $\mathrm{d}\Phi/\mathrm{d}t$ from part (a) — independent of $r$. Integrating the current over the full ramp gives the charge carried from the inner edge to the outer edge:

$$
Q = \int_0^T I_r\,\mathrm{d}t = \sigma_{xy}\int_0^T \frac{\mathrm{d}\Phi}{\mathrm{d}t}\,\mathrm{d}t = \sigma_{xy}\,\bigl[\Phi(T) - \Phi(0)\bigr] = \sigma_{xy}\,\Phi_0.
$$

The transferred charge depends only on the *total* flux change $\Phi_0$, not on the ramp profile — a first hint that the result is topological.

**(c)** Threading exactly one flux quantum $\Phi_0 = h/e$ is a **large gauge transformation**: the extra Aharonov-Bohm phase it imprints on every electron, $e\Phi_0/\hbar = 2\pi$, is unobservable, so the Hamiltonian at $\Phi = \Phi_0$ is identical to the one at $\Phi = 0$. The adiabatic theorem then guarantees that the many-body state returns to a state physically indistinguishable from the start. The only thing such a cycle can leave behind is an integer number of *whole electrons* moved from one edge to the other — single-valuedness of the many-body wavefunction permits nothing less than a complete electron. Hence

$$
Q = N e, \qquad N \in \mathbb{Z}.
$$

Combining with $Q = \sigma_{xy}\,\Phi_0$ from part (b) and $\Phi_0 = h/e$,

$$
\sigma_{xy}\,\frac{h}{e} = N e \qquad\Longrightarrow\qquad \sigma_{xy} = N\,\frac{e^2}{h}.
$$

To identify $N$, count electrons. The lecture's pumping argument (Eq. `eq-pumping-radius`, Step 2) shows that within *one* completely filled Landau level, threading $\Phi_0$ shifts every guiding-center orbit inward by exactly one slot ($r_m \to r_{m-1}$), transporting precisely one electron across. With $\nu$ Landau levels completely filled, $\nu$ electrons are pumped in parallel, one per level, so $N = \nu$ and

$$
\sigma_{xy} = \nu\,\frac{e^2}{h}.
$$

**(d)** At $\nu = 1/3$ the system is no longer a stack of filled single-particle levels — it is a strongly-correlated incompressible *fluid* with an interaction-induced gap. Two pieces of the argument survive unchanged because neither used the single-particle picture: the cycle that threads $\Phi_0$ is still a large gauge transformation, so the state still returns to itself; and the Hall response still gives $Q = \sigma_{xy}\,\Phi_0$ from part (b). With the fractional value $\sigma_{xy} = (1/3)\,e^2/h$,

$$
Q = \sigma_{xy}\,\Phi_0 = \frac{1}{3}\,\frac{e^2}{h}\,\frac{h}{e} = \frac{e}{3}.
$$

So threading one flux quantum pumps only **one third of an electron charge** across the sample. The pumped object therefore cannot be an ordinary electron; it is an emergent **quasiparticle of charge $e/3$**. The single-valuedness constraint that forced $Q$ to be a whole electron in the integer case is now satisfied by a fractional charge, because the elementary excitation of the correlated fluid is itself fractional. This fractional charge — together with anyonic exchange statistics — is the defining signature of the fractional quantum Hall effect, developed in §2.3.2.

<!-- ─── -->

**4. Edge states and Hall transport.** The lecture explains the integer plateau through *bulk* arguments — Laughlin charge pumping, the Kubo formula, and bulk localized states. An equivalent and complementary picture, not developed in the lecture body, attributes the transport instead to *chiral edge channels*: at integer $\nu$ the gapped bulk carries no current, while each sample edge supports $\nu$ chiral 1D channels. This problem develops that edge picture and reconciles it with the bulk description.

(a) Each chiral channel has conductance $e^2/h$. Argue that $\nu$ such channels give a total Hall conductance $\sigma_{xy} = \nu e^2/h$, consistent with the bulk result.

(b) "Chiral" means edge electrons on a given edge travel in only one direction. Explain why impurity backscattering is suppressed, and discuss how this edge-channel account of robustness complements the lecture's bulk localized-state explanation rather than replacing it.

(c) Compare an edge state at $\nu = 2$ to an ordinary 1D wire with the same impurity profile. Explain why the 1D wire shows Anderson localization while the chiral edge state retains quantized conductance.

**Solution.**

This problem builds the *edge* picture of the IQHE as a transfer/extension of the lecture, which derives the same plateau from purely *bulk* reasoning. The two descriptions are complementary faces of one gapped state, linked by the bulk-edge correspondence.

**(a)** A single chiral edge channel is a one-dimensional conductor in which electrons move in one direction only. By the Landauer picture, a 1D channel that transmits perfectly carries a current set by the electrochemical potential of the reservoir feeding it, with conductance quantum $e^2/h$ (the value stated in the problem; spin is counted as a separate channel). At integer filling $\nu$ the bulk is gapped and inert, so all current flows along the edges, and each edge carries $\nu$ such channels running side by side.

In a Hall measurement the two edges are held at electrochemical potentials differing by $e V_H$, where $V_H$ is the Hall voltage. The $\nu$ co-propagating channels along one edge each emanate from the same reservoir, so together they carry a current $I = \nu\,(e^2/h)\,V_H$. The Hall conductance is the ratio

$$
\sigma_{xy} = \frac{I}{V_H} = \nu\,\frac{e^2}{h},
$$

identical to the bulk Laughlin and Kubo results. The integer $\nu$ now appears as the *number of edge channels*, rather than as the number of filled bulk Landau levels — but bulk-edge correspondence guarantees these two integers coincide.

**(b)** Impurity backscattering means an electron reverses its direction of propagation after hitting a defect. On a single quantum Hall edge that is impossible: every state on that edge moves the *same* way. The only states with the opposite velocity live on the *other* edge, a macroscopic sample-width away. A realistic impurity is short-ranged and cannot connect two points separated by the whole sample, so it has essentially zero matrix element to reverse an electron's motion. An impurity can only deflect the electron *forward* along the same edge — it cannot turn it around. With backscattering forbidden, each channel transmits with unit probability and the conductance stays locked at $e^2/h$ per channel.

This edge account *complements* rather than *replaces* the lecture's bulk explanation. The lecture attributes plateau robustness to **bulk localized states**: as $B$ varies, the Fermi level moves through localized states that absorb the density change without altering the current, so $\sigma_{xy}$ stays constant over a finite plateau. The edge account instead explains *where the current physically flows* and *why it is dissipationless* (chiral channels, no backscattering). Both are correct because they describe the same incompressible state from two sides: the bulk gap is precisely what protects the edge channels (no gap, no robust edge modes), and the count of chiral edge channels is fixed by the same bulk topological integer $\nu$ that the Laughlin argument quantizes. The bulk localized states explain the *width* of the plateau in $B$; the chiral edge channels explain the *quantized value and dissipationless nature* of the current on it.

**(c)** An ordinary 1D wire hosts, at the Fermi level, both right-moving and left-moving states. Any impurity couples these counter-propagating states, so an electron can be scattered backward. With many impurities the backward-scattered amplitudes interfere coherently, and the result — for a wire longer than the localization length — is **Anderson localization**: the transmission probability falls off exponentially with length and the wire becomes an insulator. Backscattering is the essential ingredient; without it there is no localization.

A chiral edge state at $\nu = 2$ has, on each edge, only forward-moving channels — there is no counter-propagating partner at the same edge to scatter into. The matrix element for reversing an electron's direction vanishes, so the very process that drives Anderson localization is absent. The interference that would localize an ordinary wire never gets started. Consequently, faced with the *same* impurity profile, the ordinary wire localizes and goes insulating while the chiral edge keeps transmitting every channel perfectly, holding the conductance at exactly $\nu e^2/h$ regardless of edge length or (non-magnetic, short-range) disorder strength. The decisive difference is not the disorder but the **chirality** imposed by the magnetic field and the bulk topology: it removes the backscattering channel that localization requires.

<!-- ─── -->

**5. Landau-level gap and temperature.** The cyclotron gap is $\hbar\omega_c = \hbar eB/m^*$.

(a) For GaAs ($m^* = 0.067\,m_e$) at $B = 10\,\mathrm{T}$, compute $\hbar\omega_c$ in meV and the equivalent temperature $T^* = \hbar\omega_c/k_B$.

(b) Why does the IQHE require $k_B T \ll \hbar\omega_c$? Why is GaAs preferred over Si ($m^* \approx 0.2\,m_e$)?

(c) Disorder broadens Landau levels by $\Gamma$. To resolve plateaus, $\Gamma < \hbar\omega_c$. Estimate the maximum scattering rate $1/\tau$ and the minimum mobility $\mu = e\tau/m^*$.

**Solution.**

Constants used: $\hbar = 1.055\times10^{-34}\,\mathrm{J\,s}$, $e = 1.602\times10^{-19}\,\mathrm{C}$, $m_e = 9.109\times10^{-31}\,\mathrm{kg}$, $k_B = 1.381\times10^{-23}\,\mathrm{J\,K}^{-1}$.

**(a)** It is cleanest to compute the bare-electron cyclotron energy at $B = 10\,\mathrm{T}$ first, then scale by the effective mass:

$$
\begin{split}
\frac{\hbar e B}{m_e} &= \frac{(1.055\times10^{-34})(1.602\times10^{-19})(10)}{9.109\times10^{-31}}\,\mathrm{J} \approx 1.86\times10^{-22}\,\mathrm{J} \approx 1.16\,\mathrm{meV},\\
\hbar\omega_c &= \frac{\hbar e B}{m^*} = \frac{1.16\,\mathrm{meV}}{0.067} \approx 17.3\,\mathrm{meV}.
\end{split}
$$

The equivalent temperature uses $1\,\mathrm{meV} \leftrightarrow 11.6\,\mathrm{K}$:

$$
T^* = \frac{\hbar\omega_c}{k_B} \approx (17.3\,\mathrm{meV})(11.6\,\mathrm{K/meV}) \approx 200\,\mathrm{K}.
$$

So a $10\,\mathrm{T}$ field opens a cyclotron gap in GaAs equivalent to about $200\,\mathrm{K}$.

**(b)** The IQHE relies on the Fermi level sitting *inside* the gap, with the levels below it full and those above it empty — the incompressible state of the lecture. At temperature $T$, thermal excitation promotes electrons across the gap with Boltzmann weight $\sim\mathrm{e}^{-\hbar\omega_c/(k_B T)}$, partially emptying the highest filled level and populating the lowest empty one. When $k_B T \ll \hbar\omega_c$ this weight is exponentially small: the sharp $T = 0$ occupancy survives, $\sigma_{xx}$ stays near zero, and the plateaus remain precisely quantized. When $k_B T$ becomes comparable to $\hbar\omega_c$, the gap is thermally smeared, both levels carry partial population, $\sigma_{xx}$ turns on, and the quantization is lost. Hence the requirement $k_B T \ll \hbar\omega_c$.

GaAs is preferred over Si because the cyclotron gap scales inversely with effective mass, $\hbar\omega_c = \hbar e B/m^* \propto 1/m^*$. Silicon's $m^* \approx 0.2\,m_e$ is about three times the GaAs value $0.067\,m_e$, so at the same field its gap is roughly three times smaller — about $5.8\,\mathrm{meV}$ at $10\,\mathrm{T}$ instead of $17.3\,\mathrm{meV}$. A smaller gap means quantization is destroyed at a lower temperature and is more easily washed out by disorder broadening. The lighter carriers of GaAs give a wider gap and hence a more robust, more easily observed integer quantum Hall effect. (Silicon's conduction-band valley degeneracy further complicates its level structure, an additional disadvantage.)

**(c)** Plateaus are resolved only if adjacent Landau levels do not overlap, i.e. the disorder broadening must be smaller than the level spacing, $\Gamma < \hbar\omega_c$. Estimating the broadening as the lifetime (collision) broadening $\Gamma \sim \hbar/\tau$, the condition becomes

$$
\frac{\hbar}{\tau} < \hbar\omega_c \qquad\Longrightarrow\qquad \frac{1}{\tau} < \omega_c = \frac{eB}{m^*}.
$$

At $B = 10\,\mathrm{T}$ with $m^* = 0.067\,m_e$,

$$
\omega_c = \frac{eB}{m^*} \approx 2.6\times10^{13}\,\mathrm{s}^{-1},
$$

so the scattering rate must satisfy $1/\tau \lesssim 2.6\times10^{13}\,\mathrm{s}^{-1}$, equivalently $\tau \gtrsim 1/\omega_c \approx 3.8\times10^{-14}\,\mathrm{s}$. The corresponding minimum mobility is

$$
\mu_{\min} = \frac{e\,\tau_{\min}}{m^*} = \frac{e}{m^*\omega_c} = \frac{e}{m^*}\,\frac{m^*}{eB} = \frac{1}{B} = 0.1\,\mathrm{m^2\,V^{-1}\,s^{-1}} = 10^{3}\,\mathrm{cm^2\,V^{-1}\,s^{-1}}.
$$

The criterion is neatly mass-independent: $\Gamma < \hbar\omega_c$ is equivalent to $\omega_c\tau > 1$, and since $\omega_c\tau = \mu B$, it is just $\mu B > 1$ — the cyclotron orbit must complete at least one full turn between collisions. Real quantum Hall samples reach $\mu \sim 10^{6}$–$10^{7}\,\mathrm{cm^2\,V^{-1}\,s^{-1}}$, three to four orders of magnitude above this minimum, which is why the plateaus are so cleanly resolved.

<!-- ─── -->

**6. Von Klitzing constant.** $R_K \equiv h/e^2 \approx 25\,812.807\,\Omega$.

(a) Why is the Hall resistivity at $\nu = 1$ exactly $\rho_{xy} = R_K$, independent of sample, geometry, or disorder? Cite the topological argument from the lecture.

(b) Since 2019 the SI ohm is realized via the QHE rather than via a physical artifact. Explain the metrological logic.

(c) The fine-structure constant satisfies $\alpha = e^2/(4\pi\epsilon_0\hbar c)$, so $R_K = 1/(2\alpha\epsilon_0 c)$. How does a high-precision measurement of $R_K$ constrain $\alpha$?

**Solution.**

**(a)** At $\nu = 1$ the lecture gives $\sigma_{xy} = e^2/h$ and, since the bulk is gapped ($\sigma_{xx} = 0$), $\rho_{xy} = 1/\sigma_{xy} = h/e^2 = R_K$. The reason this is *exact* and universal is Laughlin's charge-pumping argument. That argument derives $\sigma_{xy} = \nu e^2/h$ using only three ingredients: flux quantization in units of $\Phi_0 = h/e$, the existence of a mobility gap, and integer counting of the electrons pumped when one flux quantum is threaded. It never invokes the microscopic Hamiltonian, the sample shape, the disorder configuration, or the host material. Threading $\Phi_0$ is a large gauge transformation, and single-valuedness of the many-body state forces an *integer* number of electrons across — an integer cannot drift continuously under a smooth deformation. That integer is a topological invariant: it is unchanged by any perturbation that keeps the gap open. Sample geometry, disorder strength, and material chemistry are all such smooth deformations, so $\rho_{xy}$ at $\nu = 1$ is locked to $h/e^2$, fixed by the two fundamental constants $h$ and $e$ alone — which is what makes it reproducible to better than one part in $10^9$.

**(b)** A good standard must be reproducible by any laboratory, at any time, without reliance on a unique physical object that can drift, age, or be damaged. Before 2019 electrical units were tied to material artifacts and to a definition of the ampere that was hard to realize directly. The 2019 SI redefinition fixed the *numerical values* of $h$ and $e$ exactly. As a consequence $R_K = h/e^2$ became an **exactly defined constant** — no longer something to be measured, but a fixed number.

The quantum Hall effect then turns that exact constant into a working laboratory standard. A QHE device on the $\nu$ plateau exhibits $\rho_{xy} = R_K/\nu$, a resistance that depends only on $R_K$ and an integer, and is — by the topological argument of part (a) — independent of the particular device. Any lab can therefore *realize* the ohm by fabricating a quantum Hall sample, putting it on a plateau, and reading off $R_K/\nu$, reproducibly to nine digits, with no artifact to store or transport and no drift over time. The QHE supplies a universal, quantum-mechanical embodiment of the ohm.

**(c)** Combining $\alpha = e^2/(4\pi\epsilon_0\hbar c) = e^2/(2\epsilon_0 h c)$ with $R_K = h/e^2$ gives the exact relation

$$
R_K = \frac{h}{e^2} = \frac{1}{2\alpha\epsilon_0 c} \qquad\Longrightarrow\qquad \alpha = \frac{1}{2\,R_K\,\epsilon_0\,c}.
$$

Because $\epsilon_0$ and $c$ are constants known with negligible (or, for $c$, zero) uncertainty, $\alpha$ is inversely proportional to $R_K$ alone. A measurement of $R_K$ therefore transfers its fractional uncertainty *one-to-one* onto $\alpha$: $\delta\alpha/\alpha = \delta R_K/R_K$. Historically this made the quantum Hall effect one of the most precise routes to the fine-structure constant — one compares the QHE plateau resistance against a calculable resistance standard (a Thompson-Lampard calculable capacitor), obtaining $R_K$ and hence $\alpha$, and the value can be checked against independent determinations from the electron anomalous magnetic moment ($g - 2$) and from atom-recoil measurements. (In the post-2019 SI the logic can also be read in reverse: with $h$ and $e$ fixed, $R_K$ is exact and the QHE *realizes* the ohm; but the relation $\alpha = 1/(2R_K\epsilon_0 c)$ still expresses the deep equivalence between a precision resistance measurement and a determination of $\alpha$.) Numerically, $R_K \approx 25\,812.807\,\Omega$ corresponds to $\alpha \approx 1/137.036$.
