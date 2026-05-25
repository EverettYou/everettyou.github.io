# 4.2.2 Aharonov-Bohm Effect
Worked solutions for the homework problems in the [4.2.2 Aharonov-Bohm Effect](../ch4_phase-and-gauge/4-2-2-aharonov-bohm-effect) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Invisible solenoid.** An electron double-slit experiment is performed around an extremely thin solenoid carrying flux $\Phi$. The electron never enters the solenoid, so $\boldsymbol{B} = 0$ everywhere on its path.

(a) Show that the fringe pattern shifts by $\Delta\Phi_{\mathrm{AB}}/(2\pi)$ fringes, where $\Delta\Phi_{\mathrm{AB}} = e\Phi/\hbar$. For $\Phi = h/(2e)$, how many fringes does the pattern shift?

(b) A skeptic says: "The solenoid has fringing fields that leak out and deflect the electron classically." Design an idealised experiment that rules out this objection. (Hint: what if the solenoid is enclosed in a superconducting shield?)

(c) If $\Phi$ is increased continuously from $0$ to $\Phi_0 = h/e$, the fringe pattern returns to its original position. Explain why the interference intensity is periodic in flux with period $\Phi_0$, while $\Phi$ itself remains a continuous parameter.

**Solution.**

**(a)** Each electron reaches the screen along two coherent paths; the intensity
at screen coordinate $\theta$ is the modulus-squared of their sum,

$$
I(\theta) \propto \bigl|\psi_{\text{upper}} + \psi_{\text{lower}}\bigr|^2 \propto 1 + \cos\bigl(\delta(\theta) + \Delta\Phi_{\mathrm{AB}}\bigr),
$$

where $\delta(\theta)$ is the ordinary geometric (optical-path) phase difference
between the two slits and $\Delta\Phi_{\mathrm{AB}} = e\Phi/\hbar$ is the extra
Aharonov-Bohm phase. With no flux, the bright fringes sit where
$\delta(\theta) = 2\pi m$ for integer $m$. Turning on the flux moves every
maximum to $\delta(\theta) + \Delta\Phi_{\mathrm{AB}} = 2\pi m$, i.e.
$\delta(\theta) = 2\pi m - \Delta\Phi_{\mathrm{AB}}$. Every fringe shifts by the
*same* amount $\Delta\delta = -\Delta\Phi_{\mathrm{AB}}$, so the whole pattern
translates rigidly without changing its shape or spacing. One full fringe
corresponds to $\Delta\delta = 2\pi$, so the shift measured in fringes is

$$
\text{shift} = \frac{|\Delta\delta|}{2\pi} = \frac{\Delta\Phi_{\mathrm{AB}}}{2\pi}.
$$

For $\Phi = h/(2e)$,

$$
\Delta\Phi_{\mathrm{AB}} = \frac{e\Phi}{\hbar} = \frac{e}{\hbar}\cdot\frac{h}{2e} = \frac{h}{2\hbar} = \pi,
$$

so the pattern shifts by $\Delta\Phi_{\mathrm{AB}}/(2\pi) = 1/2$ fringe. A
half-fringe shift is the maximal observable effect: every bright fringe lands
exactly where a dark fringe used to be. Half a flux quantum, $\Phi_0/2 = h/(2e)$,
produces the strongest possible contrast inversion.

**(b)** The objection is that a real solenoid is finite and leaks fringing field
near its ends, so the electron might pass through a region where
$\boldsymbol{B}\ne 0$ and be deflected classically. To rule this out, replace the
straight solenoid by a **toroidal** (donut-shaped) magnet: its field lines close
on themselves entirely inside the torus, so there are no ends and $\boldsymbol{B}=0$
everywhere outside. Then enclose the torus in a **superconducting shell**. Cooled
below its critical temperature, the superconductor expels magnetic field
(Meissner effect): $\boldsymbol{B}=0$ inside the shell, and screening currents pin
the flux inside the torus so none can escape. The electron now travels through a
region where $\boldsymbol{B}=0$ has been *verified* rather than assumed, so the
Lorentz force $\boldsymbol{F} = q\boldsymbol{v}\times\boldsymbol{B} = 0$ at every
point of its path. Any fringe shift cannot be a classical deflection. This is
exactly the electron-holography experiment of Tonomura et al. (1986), which
confirmed $\Delta\Phi_{\mathrm{AB}} = q\Phi/\hbar$.

**(c)** The AB phase enters the intensity only through the factor
$\mathrm{e}^{\mathrm{i}\Delta\Phi_{\mathrm{AB}}} = \mathrm{e}^{\mathrm{i}e\Phi/\hbar}$.
The intensity $I \propto 1 + \cos(\delta + e\Phi/\hbar)$ is therefore a
$2\pi$-periodic function of the combination $e\Phi/\hbar$, hence a periodic
function of $\Phi$ with period $\Phi_0 = h/e$:

$$
\frac{e\,\Phi_0}{\hbar} = \frac{e}{\hbar}\cdot\frac{h}{e} = 2\pi.
$$

Increasing $\Phi$ by one flux quantum advances $\Delta\Phi_{\mathrm{AB}}$ by
exactly $2\pi$, returning the cosine — and with it every fringe — to its starting
position. The periodicity is a property of the **observable response** (the
interference pattern), not of the flux itself: $\Phi$ is fixed by the current in
the solenoid and can take any continuous real value; nothing constrains it. Only
the measurable consequence of $\Phi$ repeats. This is distinct from genuine flux
quantisation $\Phi = n\Phi_0$, which requires a macroscopic single-valued
wavefunction encircling the flux (as in a superconducting ring) — taken up in
§4.2.3.

<!-- ─── -->

**2. Which path matters.** Two paths $\mathcal{C}_1$ and $\mathcal{C}_2$ connect points $A$ and $B$ in a region where $\boldsymbol{B} = 0$.

(a) Show that the phase difference $\Delta\Phi_{\mathrm{AB}} = \Phi_{\mathrm{path}}[\mathcal{C}_1] - \Phi_{\mathrm{path}}[\mathcal{C}_2]$ depends only on whether the combined loop $\mathcal{C}_1 - \mathcal{C}_2$ encloses flux, not on the shapes of the individual paths.

(b) A third path $\mathcal{C}_3$ also connects $A$ to $B$ but winds twice around the solenoid. What is $\Phi_{\mathrm{path}}[\mathcal{C}_3] - \Phi_{\mathrm{path}}[\mathcal{C}_1]$ in terms of $\Phi$?

(c) Classify all paths from $A$ to $B$ by their winding number around the solenoid. How does this classification reflect the multiply-connected topology of the field-free region?

**Solution.**

**(a)** The single-path phase is $\Phi_{\mathrm{path}}[\mathcal{C}] = (q/\hbar)\int_{\mathcal{C}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}$, so

$$
\Delta\Phi_{\mathrm{AB}} = \frac{q}{\hbar}\left(\int_{\mathcal{C}_1}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l} - \int_{\mathcal{C}_2}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}\right).
$$

Both paths run from $A$ to $B$. Reversing the orientation of $\mathcal{C}_2$ gives
$-\mathcal{C}_2$ running from $B$ back to $A$, with
$-\int_{\mathcal{C}_2} = \int_{-\mathcal{C}_2}$. Then $\mathcal{C}_1$ followed by
$-\mathcal{C}_2$ is a single **closed** loop $\mathcal{C}_1 - \mathcal{C}_2$ based
at $A$:

$$
\Delta\Phi_{\mathrm{AB}} = \frac{q}{\hbar}\oint_{\mathcal{C}_1-\mathcal{C}_2}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}
= \frac{q}{\hbar}\int_{\mathcal{S}}(\nabla\times\boldsymbol{A})\cdot\mathrm{d}\boldsymbol{S}
= \frac{q}{\hbar}\int_{\mathcal{S}}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S},
$$

by Stokes' theorem — the flux enclosed by the combined loop. Now deform either
path while keeping the endpoints $A,B$ fixed and staying within the
$\boldsymbol{B}=0$ region (not crossing the solenoid). The area swept by the
deformation lies entirely where $\boldsymbol{B}=0$, so it contributes no flux and
$\Delta\Phi_{\mathrm{AB}}$ is unchanged. The phase difference depends only on the
flux captured by the closed loop $\mathcal{C}_1 - \mathcal{C}_2$ — i.e. on whether,
and how many times, that loop encircles the solenoid — and not on the detailed
shapes of $\mathcal{C}_1$ and $\mathcal{C}_2$ individually.

**(b)** The path $\mathcal{C}_3$ runs $A\to B$ but winds twice around the
solenoid. The closed loop $\mathcal{C}_3 - \mathcal{C}_1$ therefore encircles the
solenoid a net **two** times: any surface spanning it cuts the solenoid twice and
captures flux $2\Phi$. Hence

$$
\Phi_{\mathrm{path}}[\mathcal{C}_3] - \Phi_{\mathrm{path}}[\mathcal{C}_1]
= \frac{q}{\hbar}\oint_{\mathcal{C}_3-\mathcal{C}_1}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}
= \frac{q}{\hbar}\,(2\Phi) = \frac{2q\Phi}{\hbar} = 2\,\Delta\Phi_{\mathrm{AB}}.
$$

For an electron ($|q| = e$) the magnitude is $2e\Phi/\hbar$. Each extra turn
around the solenoid adds one more unit of $q\Phi/\hbar$.

**(c)** Fix a reference path $\mathcal{C}_0$ from $A$ to $B$. Any other path
$\mathcal{C}$ from $A$ to $B$ forms a closed loop $\mathcal{C} - \mathcal{C}_0$
whose net winding number $n\in\mathbb{Z}$ around the solenoid is a well-defined
integer (counterclockwise turns minus clockwise turns). Two paths can be
continuously deformed into one another within the field-free region (endpoints
fixed) **if and only if** they have the same $n$ — a deformation can never change
$n$ without crossing the solenoid. The paths thus fall into homotopy classes
labelled by $n\in\mathbb{Z}$, with

$$
\Phi_{\mathrm{path}}[\mathcal{C}_n] - \Phi_{\mathrm{path}}[\mathcal{C}_0] = \frac{n\,q\Phi}{\hbar}.
$$

This integer labelling is the signature of the **multiply-connected** topology of
the field-free region. Around an (infinitely long) solenoid that region is
topologically an annulus, or punctured plane, whose fundamental group is
$\pi_1 = \mathbb{Z}$ — generated by a single loop encircling the solenoid once.
The AB phase is a homomorphism from this group to phase factors,
$n \mapsto \mathrm{e}^{\mathrm{i}nq\Phi/\hbar}$. In a simply connected region
($\pi_1$ trivial) every loop bounds a flux-free surface and all path phases would
be equal — there would be no AB effect.

<!-- ─── -->

**3. Gauge dependence of single paths.** Under a gauge transformation $\boldsymbol{A} \to \boldsymbol{A} + \nabla\alpha$, the phase accumulated along a single path $\mathcal{C}$ from $P$ to $Q$ changes.

(a) Show that $\Phi_{\mathrm{path}}'[\mathcal{C}] = \Phi_{\mathrm{path}}[\mathcal{C}] + (q/\hbar)[\alpha(Q) - \alpha(P)]$.

(b) Explain why this makes the single-path phase unobservable, but the relative phase between two paths sharing endpoints remains gauge-invariant.

(c) One might claim: "I can always choose a gauge in which $\boldsymbol{A} = 0$ outside the solenoid, so there is no AB effect." Find the flaw. Can $\boldsymbol{A}$ be set to zero everywhere in a multiply-connected region with nonzero enclosed flux by a single-valued gauge function?

**Solution.**

**(a)** Under $\boldsymbol{A} \to \boldsymbol{A} + \nabla\alpha$,

$$
\Phi_{\mathrm{path}}'[\mathcal{C}] = \frac{q}{\hbar}\int_{\mathcal{C}}(\boldsymbol{A} + \nabla\alpha)\cdot\mathrm{d}\boldsymbol{l}
= \frac{q}{\hbar}\int_{\mathcal{C}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l} + \frac{q}{\hbar}\int_{\mathcal{C}}\nabla\alpha\cdot\mathrm{d}\boldsymbol{l}.
$$

The first term is $\Phi_{\mathrm{path}}[\mathcal{C}]$. For the second, the gradient
theorem (the fundamental theorem of calculus for line integrals) gives, for a
path from $P$ to $Q$,

$$
\int_{P}^{Q}\nabla\alpha\cdot\mathrm{d}\boldsymbol{l} = \alpha(Q) - \alpha(P),
$$

which depends only on the endpoints, not on the path. Hence

$$
\Phi_{\mathrm{path}}'[\mathcal{C}] = \Phi_{\mathrm{path}}[\mathcal{C}] + \frac{q}{\hbar}\bigl[\alpha(Q) - \alpha(P)\bigr].
$$

**(b)** The shift $(q/\hbar)[\alpha(Q) - \alpha(P)]$ depends on the gauge function
$\alpha$, which is arbitrary: any smooth single-valued $\alpha$ defines a
legitimate gauge. By choosing $\alpha$ one can give the single-path phase any
value one likes, so $\Phi_{\mathrm{path}}[\mathcal{C}]$ has no gauge-invariant
value — a quantity that changes under a physically empty relabelling cannot be
measured, so the single-path phase is **not an observable**. Interference,
however, compares *two* paths $\mathcal{C}_1, \mathcal{C}_2$ that share the same
endpoints $P, Q$. Both single-path phases shift by the *identical* amount
$(q/\hbar)[\alpha(Q) - \alpha(P)]$, so the shift cancels in the difference:

$$
\Delta\Phi' = \Phi_{\mathrm{path}}'[\mathcal{C}_1] - \Phi_{\mathrm{path}}'[\mathcal{C}_2]
= \Phi_{\mathrm{path}}[\mathcal{C}_1] - \Phi_{\mathrm{path}}[\mathcal{C}_2] = \Delta\Phi.
$$

The relative phase is gauge-invariant, and it is exactly what the fringe position
measures. The unobservable common part drops out.

**(c)** The flaw: a single-valued gauge function that sets $\boldsymbol{A}=0$
everywhere does **not exist** in a multiply-connected region with nonzero enclosed
flux. Locally — in any *simply connected* patch where
$\boldsymbol{B} = \nabla\times\boldsymbol{A} = 0$ — one can indeed solve
$\nabla\alpha = -\boldsymbol{A}$ and gauge $\boldsymbol{A}$ to zero. But suppose a
single-valued $\alpha$ did this throughout the *whole* field-free region. Take any
loop $\mathcal{C}$ encircling the solenoid:

$$
\oint_{\mathcal{C}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}
= -\oint_{\mathcal{C}}\nabla\alpha\cdot\mathrm{d}\boldsymbol{l}
= -\bigl[\alpha(\text{end}) - \alpha(\text{start})\bigr] = 0,
$$

because for a single-valued $\alpha$ the start and end points of a closed loop
coincide. But Stokes' theorem fixes $\oint_{\mathcal{C}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l} = \Phi \ne 0$.
Contradiction. Therefore **no single-valued gauge function can set
$\boldsymbol{A}=0$ everywhere** in a multiply-connected region threaded by flux.
One can only either (i) gauge $\boldsymbol{A}$ away inside a simply connected
patch — a region cut so that it no longer encircles the solenoid — or (ii) use a
**multi-valued** $\alpha$ that increases by $\Phi$ on each circuit of the
solenoid, in which case the gauge phase $\mathrm{e}^{\mathrm{i}q\alpha/\hbar}$ is
itself multi-valued and carries precisely the AB phase. The holonomy
$\oint\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}$ cannot be removed by any
legitimate (single-valued) gauge transformation; the AB effect survives.

<!-- ─── -->

**4. Surface independence.** Stokes' theorem turns the AB loop integral into a magnetic flux through any surface $\mathcal{S}$ that spans the loop $\mathcal{C}$. The result should not depend on which surface one chooses.

(a) Let $\mathcal{S}_1$ and $\mathcal{S}_2$ be two oriented surfaces that both span the same loop $\mathcal{C}$, together enclosing a volume $V$ with $\mathcal{S}_1 - \mathcal{S}_2 = \partial V$. Use the divergence theorem to show

$$
\int_{\mathcal{S}_1}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} - \int_{\mathcal{S}_2}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = \int_V \nabla\cdot\boldsymbol{B}\,\mathrm{d}V.
$$

(b) Maxwell's equation $\nabla\cdot\boldsymbol{B} = 0$ forces the two flux integrals to agree. Conclude that the AB phase is well-defined independently of the surface used in Stokes' theorem.

(c) Suppose a magnetic monopole of charge $g$ sat between $\mathcal{S}_1$ and $\mathcal{S}_2$, so that $\nabla\cdot\boldsymbol{B} = \mu_0\rho_m$ with a delta-function source. Compute the discrepancy in terms of $g$ and explain why the AB phase would be ambiguous absent the Dirac quantization condition introduced in [4.4.2 Dirac Monopole](../ch4_phase-and-gauge/4-4-2-dirac-monopole).

**Solution.**

**(a)** The two oriented surfaces $\mathcal{S}_1$ and $\mathcal{S}_2$ share the
boundary loop $\mathcal{C}$. To assemble them into the closed boundary of the
volume $V$ they enclose, keep $\mathcal{S}_1$ with its given (outward) orientation
and reverse $\mathcal{S}_2$; the closed surface is then
$\partial V = \mathcal{S}_1 - \mathcal{S}_2$, with the outward normal everywhere.
The divergence theorem applied to $\boldsymbol{B}$ over $V$ reads

$$
\oint_{\partial V}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = \int_V\nabla\cdot\boldsymbol{B}\,\mathrm{d}V.
$$

Splitting the closed surface into its two pieces — and noting that reversing the
orientation of $\mathcal{S}_2$ flips the sign of its flux integral —

$$
\oint_{\partial V}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}
= \int_{\mathcal{S}_1}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} - \int_{\mathcal{S}_2}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}.
$$

Equating the two expressions,

$$
\int_{\mathcal{S}_1}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} - \int_{\mathcal{S}_2}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = \int_V\nabla\cdot\boldsymbol{B}\,\mathrm{d}V.
$$

**(b)** Maxwell's equation $\nabla\cdot\boldsymbol{B} = 0$ holds everywhere when
there is no magnetic charge, so the right-hand side vanishes and

$$
\int_{\mathcal{S}_1}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = \int_{\mathcal{S}_2}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}.
$$

The flux through any cap spanning the loop $\mathcal{C}$ is the same — it is
**surface-independent**. The AB phase $\Delta\Phi_{\mathrm{AB}} = (q/\hbar)\int_{\mathcal{S}}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}$
is therefore a well-defined function of the loop alone, independent of which
spanning surface is used in Stokes' theorem. Physically: magnetic field lines are
continuous, with no sources or sinks, so any two surfaces sharing the same rim are
pierced by exactly the same set of field lines.

**(c)** Place a magnetic monopole of charge $g$ between $\mathcal{S}_1$ and
$\mathcal{S}_2$, hence inside $V$. Maxwell's law becomes
$\nabla\cdot\boldsymbol{B} = \mu_0\rho_m$ with point source
$\rho_m = g\,\delta^3(\boldsymbol{r} - \boldsymbol{r}_0)$. The volume integral now
picks up the source:

$$
\int_{\mathcal{S}_1}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} - \int_{\mathcal{S}_2}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}
= \int_V\mu_0\rho_m\,\mathrm{d}V = \mu_0 g.
$$

The two spanning surfaces give magnetic fluxes that differ by $\mu_0 g$ — the
total flux emitted by the monopole. The AB phase would correspondingly differ by

$$
\delta(\Delta\Phi_{\mathrm{AB}}) = \frac{q}{\hbar}\,\mu_0 g
$$

depending on which side of the monopole the spanning surface passes — an apparent
ambiguity in a quantity meant to be physical. The resolution is that the AB phase
is only ever observable modulo $2\pi$, since it enters through
$\mathrm{e}^{\mathrm{i}\Delta\Phi_{\mathrm{AB}}}$. The ambiguity is harmless
precisely when the two surface choices differ by an integer multiple of $2\pi$:

$$
\frac{q\,\mu_0 g}{\hbar} = 2\pi n,\qquad n\in\mathbb{Z},
$$

which is the **Dirac quantization condition**, $q\,(\mu_0 g) = 2\pi n\hbar$ — the
monopole's total flux must be an integer number of flux quanta $\Phi_0 = h/q$.
(In the flux-defined convention used in §4.4.2, the magnetic charge is identified
directly with the total flux, $\nabla\cdot\boldsymbol{B} = \rho_m$, and the same
condition reads $qg = 2\pi n\hbar$.) Without Dirac quantization the AB phase would
genuinely depend on an arbitrary choice of spanning surface, and quantum mechanics
in the presence of monopoles would be inconsistent; with it, the two choices
differ by a multiple of $2\pi$, $\mathrm{e}^{\mathrm{i}\Delta\Phi_{\mathrm{AB}}}$
is unambiguous, and consistency is restored.

<!-- ─── -->

**5. AB phase as Berry phase.** The AB phase is the closed-loop Berry phase of a charged particle whose parameter happens to be its own position.

(a) Identify the parameter space: as the electron's position $\boldsymbol{r}$ winds around the solenoid, what plays the role of the parameter $\boldsymbol{R}$ in the Berry-phase formalism of [4.2.1 Berry Phase](../ch4_phase-and-gauge/4-2-1-berry-phase)?

(b) Show that, for a wavefunction $\psi(\boldsymbol{r}) = \mathrm{e}^{\mathrm{i}q\int^{\boldsymbol{r}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}'/\hbar}\tilde\psi(\boldsymbol{r})$ with $\tilde\psi$ the gauge-rotated background state, the Berry connection $\boldsymbol{A}_\text{Berry} = \mathrm{i}\langle\psi(\boldsymbol{r})\vert\nabla_{\boldsymbol{r}}\vert\psi(\boldsymbol{r})\rangle$ reduces to $(q/\hbar)\boldsymbol{A}(\boldsymbol{r})$.

(c) Verify that the closed-loop Berry phase is $\oint\boldsymbol{A}_\text{Berry}\cdot\mathrm{d}\boldsymbol{r} = q\Phi/\hbar$ and that this answer is independent of the gauge chosen for $\boldsymbol{A}$.

**Solution.**

**(a)** In the Berry-phase formalism of §4.2.1, a state $\vert n(\boldsymbol{R})\rangle$
depends on an external parameter $\boldsymbol{R}$, and the Berry phase is the
holonomy accumulated as $\boldsymbol{R}$ traverses a closed loop in *parameter
space*. In the AB problem there is no external knob: the role of the parameter
$\boldsymbol{R}$ is played by the **electron's own position** $\boldsymbol{r}$. The
parameter space is the field-free region in which the electron moves — the
multiply-connected annulus (punctured plane) surrounding the solenoid. As the
electron's position winds once around the solenoid, $\boldsymbol{R} = \boldsymbol{r}$
traces a closed loop in that space, and the wavefunction's phase is the
corresponding holonomy. The locally gauge-rotated family of states
$\vert\psi(\boldsymbol{r})\rangle$ — the background state $\tilde\psi$ dressed by
the position-dependent electromagnetic phase — is the parameter-dependent state
whose Berry connection we compute.

**(b)** Write the position-dependent phase as
$\Lambda(\boldsymbol{r}) = \int^{\boldsymbol{r}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}'$,
so that $\psi(\boldsymbol{r}) = \mathrm{e}^{\mathrm{i}q\Lambda(\boldsymbol{r})/\hbar}\,\tilde\psi(\boldsymbol{r})$
and, by the fundamental theorem of calculus, $\nabla_{\boldsymbol{r}}\Lambda = \boldsymbol{A}(\boldsymbol{r})$.
Differentiating,

$$
\nabla_{\boldsymbol{r}}\vert\psi\rangle = \mathrm{e}^{\mathrm{i}q\Lambda/\hbar}\left(\frac{\mathrm{i}q}{\hbar}(\nabla\Lambda)\vert\tilde\psi\rangle + \nabla\vert\tilde\psi\rangle\right)
= \mathrm{e}^{\mathrm{i}q\Lambda/\hbar}\left(\frac{\mathrm{i}q}{\hbar}\boldsymbol{A}\,\vert\tilde\psi\rangle + \nabla\vert\tilde\psi\rangle\right).
$$

The bra is $\langle\psi\vert = \langle\tilde\psi\vert\,\mathrm{e}^{-\mathrm{i}q\Lambda/\hbar}$,
and the two scalar phase factors cancel in the overlap:

$$
\langle\psi\vert\nabla_{\boldsymbol{r}}\vert\psi\rangle = \frac{\mathrm{i}q}{\hbar}\boldsymbol{A}\,\langle\tilde\psi\vert\tilde\psi\rangle + \langle\tilde\psi\vert\nabla\vert\tilde\psi\rangle.
$$

The background state $\tilde\psi$ is the wavefunction in the locally-$\boldsymbol{A}=0$
gauge: it is normalized, $\langle\tilde\psi\vert\tilde\psi\rangle = 1$, and carries
no geometric phase of its own, so its connection vanishes,
$\langle\tilde\psi\vert\nabla\vert\tilde\psi\rangle = 0$ (it can be chosen real).
Hence

$$
\langle\psi\vert\nabla_{\boldsymbol{r}}\vert\psi\rangle = \frac{\mathrm{i}q}{\hbar}\,\boldsymbol{A}(\boldsymbol{r}).
$$

Multiplying by $\mathrm{i}$ converts this purely imaginary quantity into the real
Berry connection:

$$
\boldsymbol{A}_\text{Berry} = \mathrm{i}\,\langle\psi\vert\nabla_{\boldsymbol{r}}\vert\psi\rangle = \mathrm{i}\cdot\frac{\mathrm{i}q}{\hbar}\boldsymbol{A} = -\frac{q}{\hbar}\,\boldsymbol{A}(\boldsymbol{r}).
$$

Up to the overall sign, the Berry connection on the position parameter space is
exactly the electromagnetic vector potential rescaled by $q/\hbar$:

$$
\boldsymbol{A}_\text{Berry} = \pm\frac{q}{\hbar}\,\boldsymbol{A}(\boldsymbol{r}).
$$

*Sign convention.* The overall sign of the Berry connection is conventional. With
the definition $\boldsymbol{A}_\text{Berry} = \mathrm{i}\langle\psi\vert\nabla\psi\rangle$
(the convention of §4.2.1) and the phase factor $\mathrm{e}^{+\mathrm{i}q\Lambda/\hbar}$
appearing in $\psi$, the literal result is $-q\boldsymbol{A}/\hbar$. The opposite
convention $\boldsymbol{A}_\text{Berry} = -\mathrm{i}\langle\psi\vert\nabla\psi\rangle$
— equivalently, reading the accumulated phase straight off the explicit factor
$\mathrm{e}^{+\mathrm{i}q\Lambda/\hbar}$ in $\psi$ — gives $+q\boldsymbol{A}/\hbar$,
the value quoted in the problem and consistent with the lecture's
$\Delta\Phi_{\mathrm{AB}} = +q\Phi/\hbar$. What is convention-independent: the
magnitude $\vert\boldsymbol{A}_\text{Berry}\vert = (q/\hbar)\vert\boldsymbol{A}\vert$,
so the position is the Berry parameter and $q\boldsymbol{A}/\hbar$ is the gauge
connection on it; the closed-loop holonomy has magnitude $q\Phi/\hbar$.

**(c)** The closed-loop Berry phase is the holonomy of $\boldsymbol{A}_\text{Berry}$
around the loop the position traces. Taking the convention that fixes the sign as
in the lecture box,

$$
\Phi_\text{Berry} = \oint_{\mathcal{C}}\boldsymbol{A}_\text{Berry}\cdot\mathrm{d}\boldsymbol{r}
= \frac{q}{\hbar}\oint_{\mathcal{C}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{r}
= \frac{q}{\hbar}\int_{\mathcal{S}}(\nabla\times\boldsymbol{A})\cdot\mathrm{d}\boldsymbol{S}
= \frac{q}{\hbar}\int_{\mathcal{S}}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = \frac{q\Phi}{\hbar},
$$

which is precisely the Aharonov-Bohm phase $\Delta\Phi_{\mathrm{AB}}$. (The other
sign convention flips the overall sign; the magnitude $q\Phi/\hbar$ is unchanged.)

Gauge independence: under $\boldsymbol{A} \to \boldsymbol{A} + \nabla\alpha$ with
$\alpha$ single-valued,

$$
\oint_{\mathcal{C}}\boldsymbol{A}_\text{Berry}\cdot\mathrm{d}\boldsymbol{r}
\to \frac{q}{\hbar}\oint_{\mathcal{C}}(\boldsymbol{A} + \nabla\alpha)\cdot\mathrm{d}\boldsymbol{r}
= \frac{q}{\hbar}\oint_{\mathcal{C}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{r} + \frac{q}{\hbar}\oint_{\mathcal{C}}\nabla\alpha\cdot\mathrm{d}\boldsymbol{r},
$$

and the last integral vanishes because the line integral of a gradient around a
closed loop is zero for any single-valued $\alpha$. Equivalently,
$\Phi_\text{Berry} = (q/\hbar)\int_{\mathcal{S}}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S}$
depends only on $\boldsymbol{B} = \nabla\times\boldsymbol{A}$, which is itself
gauge-invariant. The closed-loop Berry phase $q\Phi/\hbar$ is therefore a
gauge-invariant physical observable, even though the connection
$\boldsymbol{A}_\text{Berry}$ — like $\boldsymbol{A}$ — is not.

<!-- ─── -->

**6. Electric Aharonov-Bohm.** A charged particle passes through a region of zero electric field, but the scalar potential $\phi$ is nonzero and time-dependent.

(a) Two electron wavepackets travel through two tubes at different electrostatic potentials $V_1$ and $V_2$ for a time $T$, with $\boldsymbol{E} = 0$ everywhere the electrons travel. Show that the relative phase is $\Delta\Phi = eT(V_1 - V_2)/\hbar$.

(b) Explain why this is analogous to the magnetic AB effect: the potential produces a measurable phase even though no force acts on the particle.

(c) Is the electric AB effect topological in the same sense as the magnetic one? What role does the multiply-connected geometry play in each case?

**Solution.**

**(a)** Each electron travels inside a long conducting tube (a Faraday cage) held
at a uniform electrostatic potential $V_i$. Inside such a cavity the field
vanishes, $\boldsymbol{E} = -\nabla\phi = 0$, because a spatially constant
potential has zero gradient; no electric force acts and the electron's motion is
undisturbed. The only effect of the potential is the potential-energy term it
adds to the Hamiltonian, $\hat{H} = \hat{H}_0 + q\phi$, with $\phi = V_i$ constant
in the $i$-th tube while the electron is inside. Time evolution over the interval
$T$ multiplies the wavepacket by

$$
\mathrm{e}^{-\mathrm{i}\hat{H}T/\hbar} = \mathrm{e}^{-\mathrm{i}\hat{H}_0 T/\hbar}\,\mathrm{e}^{-\mathrm{i}qV_i T/\hbar},
$$

where the factorisation is exact because $\hat{H}_0$ and the c-number $qV_i$
commute. The factor $\mathrm{e}^{-\mathrm{i}\hat{H}_0 T/\hbar}$ is common to both
tubes (identical free evolution); the extra, tube-dependent phase is

$$
\Phi_i = -\frac{qV_i T}{\hbar}.
$$

The relative phase of the two recombined packets is therefore

$$
\Delta\Phi = \Phi_1 - \Phi_2 = -\frac{qT}{\hbar}(V_1 - V_2).
$$

For an electron, $q = -e$, so

$$
\Delta\Phi = \frac{eT}{\hbar}(V_1 - V_2),
$$

as required. (The potentials are arranged to differ only while both packets are
deep inside the tubes — i.e. while $\boldsymbol{E} = 0$ along each trajectory —
with any switching done when no electron is near a tube end.)

**(b)** In the magnetic AB effect the *spatial* part of the gauge potential,
$\boldsymbol{A}$, is nonzero along the path while the *field*
$\boldsymbol{B} = \nabla\times\boldsymbol{A}$ vanishes there; the electron feels no
magnetic force yet acquires the phase $(q/\hbar)\int\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}$.
The electric AB effect is the exact time-component analogue: the *scalar*
potential $\phi$ is nonzero while the *field*
$\boldsymbol{E} = -\nabla\phi - \partial_t\boldsymbol{A}$ vanishes along the path;
the electron feels no electric force yet acquires the phase
$-(q/\hbar)\int\phi\,\mathrm{d}t$. Both are instances of one statement: in quantum
mechanics a charged particle couples to the gauge *potential*, not directly to the
*field strength*. The wavefunction's phase responds to the four-potential
$A^\mu = (\phi/c, \boldsymbol{A})$ through the minimal-coupling term, and the
gauge-invariant observable is the holonomy
$\oint(\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l} - \phi\,\mathrm{d}t)$ of $A^\mu$
around a closed loop in spacetime. A potential can thus produce a measurable
interference shift even where it exerts no force at all.

**(c)** Not in quite the same sense. The magnetic AB effect is topological in a
*spatial* sense: the field-free region is multiply connected, the loop cannot be
shrunk to a point because the solenoid (the region of nonzero $\boldsymbol{B}$)
physically blocks it, and the phase depends only on the winding number — a
homotopy invariant of a *static* spatial geometry. The electric AB effect, by
contrast, normally uses tubes that are *spatially simply connected*; what
separates the two interfering branches is not a spatial hole but a *time*
interval during which the potentials are held unequal. The relevant closed loop
lives in **spacetime** — the $(t, \boldsymbol{x})$ plane — and it encircles a
spacetime region where the field strength $F^{\mu\nu}$ is nonzero (the
time-dependent electric field generated when the potentials are switched on or
off). So both effects are holonomies of the gauge potential $A^\mu$ around closed
spacetime loops that enclose field strength — that is the common, unifying sense
in which they are "topological." The difference is *where the obstruction lives*:
the magnetic case realises it as a permanent, static, multiply-connected spatial
geometry, whereas the electric case realises it through time-dependence, with no
spatial multiple-connectivity required. For this reason the electric AB effect is
often regarded as topological in the weaker, spacetime sense rather than the clean
static-spatial sense of the magnetic effect.

<!-- ─── -->

**7. Toroidal magnet.** Tonomura's electron-holography test of the AB effect used a toroidal magnet (donut), not an infinite solenoid: the magnetic field is fully confined to the toroid's interior, with zero field everywhere outside.

(a) An electron beam threads the central hole of the toroid; a reference beam bypasses it externally; the two recombine on a detector. Sketch the geometry, identify the loop $\mathcal{C}$ that contributes to the AB phase, and show that $\Delta\Phi_{\mathrm{AB}} = q\Phi_\text{inside}/\hbar$, where $\Phi_\text{inside}$ is the flux through the toroid's interior.

(b) Why is the toroidal geometry — with no field anywhere outside — a cleaner experimental test than the original infinite-solenoid geometry?

(c) Tonomura further coated the toroid with a superconducting shell to flux-trap the field inside. Using the Meissner effect (field expulsion by a superconductor), explain how this rules out the residual objection of stray fringing fields and makes the AB phase fully isolated from any local Lorentz force.

**Solution.**

**(a)** *Geometry.* A toroidal magnet is a donut whose magnetic field circulates
*around* the ring, confined entirely within the torus body; outside the torus
$\boldsymbol{B} = 0$ everywhere. Picture the donut lying flat in a plane. The
electron beam passes straight through the central hole, threading the donut like
one link of a chain; the reference beam passes outside, well clear of the donut,
not linking it. Both beams leave a common source and are brought back together at
a detector:

```
            reference beam
        ___________________
       /                   \
      |     _________        |
      |    /  torus  \       |
   ---+---(  ( hole ) )------ +--->  electron beam (through the hole)
      |    \_________/        |
      |                       |
       \_____________________/
```

The AB phase comes from the closed loop $\mathcal{C}$ formed by the
through-the-hole path minus the external path,
$\mathcal{C} = \mathcal{C}_\text{hole} - \mathcal{C}_\text{ref}$. This loop
*links* the torus: it cannot be contracted to a point without passing through the
torus body. Any oriented surface $\mathcal{S}$ spanning $\mathcal{C}$ must
therefore puncture the torus body exactly once, and so captures the full magnetic
flux $\Phi_\text{inside}$ circulating inside the donut. The reference path,
linking no flux, contributes nothing. By Stokes' theorem,

$$
\Delta\Phi_{\mathrm{AB}} = \frac{q}{\hbar}\oint_{\mathcal{C}}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}
= \frac{q}{\hbar}\int_{\mathcal{S}}\boldsymbol{B}\cdot\mathrm{d}\boldsymbol{S} = \frac{q\,\Phi_\text{inside}}{\hbar}.
$$

**(b)** An infinite solenoid is an idealisation; a real solenoid is finite and has
*ends*, and near those ends magnetic field leaks out into the region outside (the
"fringing field"). An electron passing nearby therefore moves through a region
where $\boldsymbol{B} \ne 0$, and a skeptic can attribute the observed fringe
shift to an ordinary classical Lorentz force $q\boldsymbol{v}\times\boldsymbol{B}$
from that stray field, rather than to the vector potential. A torus has *no ends*:
its field lines close on themselves entirely inside the donut, so
$\boldsymbol{B} = 0$ everywhere outside — exactly, not merely approximately. With
genuinely zero field along the whole electron trajectory there is no Lorentz
force anywhere on the path, and the fringe shift can only be a response to the
vector potential. The toroidal geometry thus closes the loophole that the
infinite-solenoid idealisation leaves open.

**(c)** Coating the toroid with a superconducting shell and cooling it below its
critical temperature exploits the **Meissner effect**: a superconductor expels
magnetic field from its interior, maintaining $\boldsymbol{B} = 0$ inside the
superconducting material by spontaneously generating surface screening currents
that cancel any field attempting to penetrate. The shell therefore does two
things. First, it confines the field rigidly inside the torus — the flux is
*trapped*, pinned by the screening currents, and cannot leak out even through
material imperfections. Second, the shell is itself a region of provably zero
field. Combined with the toroidal geometry's already-zero external field, this
guarantees $\boldsymbol{B} = 0$ along *every* part of the electron's path —
verified, not assumed. The electron experiences zero Lorentz force at every point,
yet the interference pattern still shifts by $q\Phi_\text{inside}/\hbar$. The
phase is then *fully isolated* from any local field: it cannot be anything but a
response to the vector potential, whose closed-loop holonomy equals the trapped
flux. This is the configuration of Tonomura et al.'s 1986 electron-holography
experiment, which provided the definitive confirmation of the Aharonov-Bohm
effect.
