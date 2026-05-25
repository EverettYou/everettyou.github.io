# 3.1.2 Physical Optics
Worked solutions for the homework problems in the [3.1.2 Physical Optics](../ch3_path-integral/3-1-2-physical-optics) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Refraction at an interface.** Light of frequency $f$ crosses from vacuum ($n=1$) into glass ($n=1.5$). Does the frequency change? Does the wavelength change? Compute the ratio $\lambda_{\text{glass}}/\lambda_{\text{vacuum}}$ and explain why the refractive index appears in the optical path length.

**Solution.**

*Frequency — unchanged.* When a monochromatic wave crosses an interface, the oscillating field on the two sides must stay continuously matched at the boundary at every instant. A point on the interface is driven by the incident wave at its frequency and re-radiates the transmitted wave at that same driving frequency. The frequency is fixed by the source, so

$$
f_{\text{glass}} = f_{\text{vacuum}} = f.
$$

*Wave speed and wavelength — changed.* The phase speed depends on the medium, $v = c/n$: in vacuum $v_{\text{vac}} = c$, in glass $v_{\text{glass}} = c/1.5$. Since $\lambda = v/f$ and $f$ is fixed,

$$
\lambda = \frac{v}{f} = \frac{c}{n f},
$$

so the wavelength **does change** — it shrinks in the denser medium. The ratio is

$$
\frac{\lambda_{\text{glass}}}{\lambda_{\text{vacuum}}} = \frac{c/(n_{\text{glass}}\,f)}{c/(n_{\text{vac}}\,f)} = \frac{n_{\text{vac}}}{n_{\text{glass}}} = \frac{1}{1.5} = \frac{2}{3} \approx 0.667.
$$

The wave is compressed to two-thirds of its vacuum wavelength inside the glass.

*Why $n$ appears in the optical path length.* Phase accumulates as $\mathrm{d}\Phi = k_{\text{loc}}\,\mathrm{d}s$, where $k_{\text{loc}} = 2\pi/\lambda$ is the *local* wave number. Because $\lambda = \lambda_0/n$ (with $\lambda_0$ the vacuum wavelength),

$$
k_{\text{loc}} = \frac{2\pi}{\lambda} = \frac{2\pi n}{\lambda_0} = n\,k_0,
$$

which is $n$ times the vacuum value $k_0 = 2\pi/\lambda_0$. The total phase along a ray is therefore

$$
\Phi = \int k_{\text{loc}}\,\mathrm{d}s = k_0\int n\,\mathrm{d}s \equiv k_0\,L, \qquad L \equiv \int n\,\mathrm{d}s.
$$

The optical path length $L = \int n\,\mathrm{d}s$ is the *vacuum-equivalent* distance: the distance one would travel in vacuum to accumulate the same phase. Each metre of glass packs in $n$ times as many wave crests as a metre of vacuum, so it counts as $n$ metres of optical path. That factor of $n$ — and only that factor — carries the medium's effect into the phase. Frequency, being shared across all media, cancels out of any phase *difference* between two paths; only the wavelength compression, encoded by $n$, survives.

<!-- ─── -->

**2. Reflection from wavefronts.** Using Huygens' principle and the wavefront envelope construction, derive the law of reflection for a plane wave hitting a flat mirror. Draw the incident and reflected wavefronts and label the angles.

**Solution.**

*Setup.* A monochromatic plane wave travels toward a flat mirror. Its **rays** are parallel straight lines; its **wavefronts** are the surfaces of constant phase, perpendicular to the rays. Let the rays make angle $\theta_i$ with the mirror normal; then the wavefronts make the same angle $\theta_i$ with the mirror surface.

Consider the moment when the leading edge of one wavefront first touches the mirror, at point $A$. Pick the ray, a transverse distance away, that will be the *next* to reach the mirror; call its strike point $C$. At the instant the wave touches $A$, that second ray still has its wavefront at a point $B$, a distance $\overline{BC}$ short of the mirror, with $B$ on the incident wavefront and the segment $BC$ running along the incident ray (hence perpendicular to the incident wavefront).

*Huygens construction.* The wave travels at speed $v = c/n$ in the single medium above the mirror — reflection does not change the medium. Let $\tau$ be the time for the second ray to cover $\overline{BC}$ and reach $C$:

$$
\overline{BC} = v\,\tau.
$$

During that same interval $\tau$, the point $A$ — touched first — has been acting as a Huygens source, emitting a secondary spherical wavelet. By the time the wave reaches $C$, that wavelet has expanded to radius

$$
\overline{AD} = v\,\tau = \overline{BC}.
$$

The reflected wavefront at this instant is the **envelope** of all the secondary wavelets emitted along $AC$: the straight line through $C$ tangent to the wavelet centred at $A$. Tangency means the radius $\overline{AD}$ to the contact point $D$ is perpendicular to the reflected wavefront $DC$.

*Two triangles.* Examine the two right triangles that share the hypotenuse $\overline{AC}$ lying along the mirror:

- Triangle $ABC$, right-angled at $B$. The incident wavefront makes angle $\theta_i$ with the mirror, so the angle at $A$ is $\theta_i$ and

$$
\overline{BC} = \overline{AC}\,\sin\theta_i.
$$

- Triangle $ADC$, right-angled at $D$. The reflected wavefront makes angle $\theta_r$ with the mirror, so the angle at $C$ is $\theta_r$ and

$$
\overline{AD} = \overline{AC}\,\sin\theta_r.
$$

*Conclusion.* The two radii are equal, $\overline{AD} = \overline{BC}$ (both equal $v\tau$). Therefore

$$
\overline{AC}\,\sin\theta_r = \overline{AC}\,\sin\theta_i,
$$

so $\sin\theta_r = \sin\theta_i$, and hence $\theta_r = \theta_i$. $\checkmark$

The angle of reflection equals the angle of incidence. The whole construction lies in the single plane spanned by the incident ray and the normal, so the reflected ray lies in that plane too — incident ray, reflected ray, and normal are coplanar.

*The sketch.* Draw the mirror as a horizontal line carrying the two strike points $A$ and $C$. The incident wavefronts are a family of parallel lines tilted at $\theta_i$ to the mirror, marching down toward it; the last one before reflection runs from $B$ down to $A$. The reflected wavefronts are the mirror-image family tilted at $\theta_r$, marching away from it; the first one runs from $C$ up to $D$. The Huygens wavelet centred at $A$, of radius $\overline{AD}$, is tangent to the reflected wavefront $DC$. The angle $\theta_i$ sits between the incident ray and the normal at $A$; the angle $\theta_r$ sits between the reflected ray and the normal at $C$; the equal-radius construction shows them equal.

*Equivalent statement (lecture form).* This is the boundary-spacing argument of the lecture: the spacing of phase-matched points along the mirror is $\lambda_\parallel = \lambda/\sin\theta_i$ for the incident wave and $\lambda/\sin\theta_r$ for the reflected wave. Reflection keeps the wave in the same medium, so $\lambda$ is unchanged, and matching the spacings gives $\sin\theta_i = \sin\theta_r$ at once.

<!-- ─── -->

**3. Layered medium ray tracing.** A light ray enters a stack of three parallel slabs with refractive indices $n_{1} = 1.0$ (above), $n_{2} = 1.5$, $n_{3} = 1.2$, $n_{4} = 1.0$ (below), at incidence angle $\theta_{1} = 60^{\circ}$ from the surface normal in $n_{1}$.

(a) Apply Snell's law at each interface to compute $\theta_{2}, \theta_{3}, \theta_{4}$.

(b) Show that $\theta_{4}$ depends only on $n_{1}, n_{4}$ and $\theta_{1}$ — independent of the intermediate $n_{2}, n_{3}$. Explain why the intermediate layers cannot change the exit direction.

(c) Find the entry angle $\theta_{1}^{\text{crit}}$ above which total internal reflection occurs *somewhere* in the stack, and identify which interface fails first.

**Solution.**

*Geometry and the ray invariant.* The stack has four labelled regions $n_1, n_2, n_3, n_4$ separated by three parallel interfaces, with $\theta_i$ the angle to the (common) normal in region $i$. At every interface Snell's law reads $n_{\text{in}}\sin\theta_{\text{in}} = n_{\text{out}}\sin\theta_{\text{out}}$. Across parallel interfaces this chains into a single conserved quantity, the **ray invariant**

$$
\mathcal{I} \equiv n\sin\theta = \text{const through the whole stack}.
$$

Physically $\mathcal I$ is proportional to the component of the wave vector parallel to the interfaces; parallel interfaces share one orientation, so that component is preserved at each crossing. Here $\mathcal I$ is fixed by the entry conditions:

$$
\mathcal I = n_1\sin\theta_1 = (1.0)\sin 60^\circ = \frac{\sqrt3}{2} \approx 0.8660.
$$

**(a) Angle in each layer.** Solve $\sin\theta_i = \mathcal I / n_i$ layer by layer:

$$
\sin\theta_2 = \frac{\mathcal I}{n_2} = \frac{0.8660}{1.5} = 0.5774,
$$

so $\theta_2 = \arcsin 0.5774 \approx 35.3^\circ$.

$$
\sin\theta_3 = \frac{\mathcal I}{n_3} = \frac{0.8660}{1.2} = 0.7217,
$$

so $\theta_3 = \arcsin 0.7217 \approx 46.2^\circ$.

$$
\sin\theta_4 = \frac{\mathcal I}{n_4} = \frac{0.8660}{1.0} = 0.8660,
$$

so $\theta_4 = \arcsin 0.8660 = 60.0^\circ$.

The ray bends *toward* the normal in the densest layer $n_2$ (smallest $\theta$), then back *away* from the normal as the index drops through $n_3$ and $n_4$.

**(b) Exit angle independent of the inner layers.** Write Snell's law at all three interfaces and chain them:

$$
n_1\sin\theta_1 = n_2\sin\theta_2, \qquad n_2\sin\theta_2 = n_3\sin\theta_3, \qquad n_3\sin\theta_3 = n_4\sin\theta_4.
$$

Each middle term ($n_2\sin\theta_2$ and $n_3\sin\theta_3$) appears once as a right-hand side and once as a left-hand side, so it cancels and the chain telescopes:

$$
n_1\sin\theta_1 = n_4\sin\theta_4,
$$

so $\sin\theta_4 = (n_1/n_4)\sin\theta_1$.

The exit angle depends only on the *entry* index $n_1$, the *exit* index $n_4$, and $\theta_1$ — the intermediate $n_2, n_3$ have dropped out. Here $n_1 = n_4 = 1.0$, so $\theta_4 = \theta_1 = 60^\circ$: the ray leaves **parallel** to the way it came in, merely shifted sideways by a lateral displacement.

The intermediate layers cannot change the exit direction because they redirect the ray only *temporarily*. What is conserved at each parallel interface is $n\sin\theta$, not $\theta$ itself; each inner layer bends the ray one way on entry and bends it back by exactly the same amount on exit. Only the first and last media — where the ray actually begins and ends — set the net deflection. (A *non-parallel* interface would tilt the local normal and break the chaining; that is how a prism deflects light.)

**(c) Where total internal reflection could occur.** TIR happens at an interface only when the ray passes from higher to lower index and the would-be transmitted angle exceeds $90^\circ$ — that is, when Snell's law demands $\sin\theta_{\text{out}} > 1$. In stack language, TIR at the interface into medium $n_{\text{out}}$ requires

$$
\sin\theta_{\text{out}} = \frac{\mathcal I}{n_{\text{out}}} > 1,
$$

which is equivalent to $\mathcal I > n_{\text{out}}$.

So the ray is trapped only if the invariant $\mathcal I$ exceeds some downstream index. But the invariant is bounded by the entry medium:

$$
\mathcal I = n_1\sin\theta_1 \le n_1 = 1.0,
$$

since $\sin\theta_1 \le 1$. TIR is possible only at the *descending* steps — into $n_3$ (needs $\mathcal I > 1.2$) and into $n_4$ (needs $\mathcal I > 1.0$); the step into $n_2$ is index-increasing and never reflects. Both thresholds sit at or above the maximum attainable $\mathcal I = 1.0$. Therefore:

**No entry angle below grazing produces total internal reflection anywhere in this stack.** Formally $\theta_1^{\text{crit}} = 90^\circ$ — the invariant reaches the smallest downstream index, $n_4 = 1.0$, only in the grazing limit $\sin\theta_1 \to 1$.

The interface that "fails first" — the one with the lowest TIR threshold, hence closest to trapping the ray — is the **last one, $n_3 \to n_4$** ($1.2 \to 1.0$), because $n_4 = 1.0$ is the smallest index downstream. It would reflect the ray totally only at the marginal value $\theta_1 = 90^\circ$.

The underlying reason is structural: the entry medium $n_1 = 1.0$ is the lowest index in the whole problem. A ray launched from the rarest medium always finds a real refraction angle into any medium with $n \ge n_1$, so it can never be totally trapped — it can always escape. TIR somewhere in the stack would require some layer with index *below* $n_1$. (If, for instance, the bottom medium were $n_4 = 0.90 < n_1$, the $n_3 \to n_4$ interface would trap the ray once $\mathcal I > 0.90$, i.e. for $\sin\theta_1^{\text{crit}} = n_4/n_1 = 0.90$, giving $\theta_1^{\text{crit}} \approx 64.2^\circ$.)

<!-- ─── -->

**4. Interference of two paths.** Two paths from $A$ to $B$ through a medium have optical path lengths $L_{1}$ and $L_{2}$. The phase difference is $\Delta\Phi = k_{0}(L_{1} - L_{2})$ where $k_{0} = 2\pi/\lambda_{0}$. For what values of $\Delta\Phi$ is the interference constructive? Destructive?

**Solution.**

When two coherent waves of intensities $I_1, I_2$ recombine at $B$, the total intensity is

$$
I = I_1 + I_2 + 2\sqrt{I_1 I_2}\,\cos(\Delta\Phi),
$$

so the interference term is governed entirely by $\cos\Delta\Phi$ with $\Delta\Phi = k_0(L_1 - L_2)$.

*Constructive interference* — the intensity is a **maximum** — when the two amplitudes add in phase, $\cos\Delta\Phi = +1$:

$$
\Delta\Phi = 2\pi m, \qquad m = 0, \pm1, \pm2, \dots
$$

Equivalently, with $k_0 = 2\pi/\lambda_0$, the optical path difference is a whole number of vacuum wavelengths:

$$
L_1 - L_2 = m\,\lambda_0.
$$

*Destructive interference* — the intensity is a **minimum** — when the amplitudes are exactly out of phase, $\cos\Delta\Phi = -1$:

$$
\Delta\Phi = (2m + 1)\,\pi, \qquad m = 0, \pm1, \pm2, \dots
$$

an odd multiple of $\pi$, corresponding to a half-integer number of wavelengths:

$$
L_1 - L_2 = \left(m + \tfrac12\right)\lambda_0.
$$

If $I_1 = I_2$ the minima are completely dark, $I_{\min} = 0$; otherwise $I_{\min} = \left(\sqrt{I_1} - \sqrt{I_2}\right)^2 > 0$, while the maxima reach $I_{\max} = \left(\sqrt{I_1} + \sqrt{I_2}\right)^2$.

*Remark.* It is essential that $L_1, L_2$ are **optical** path lengths, $L = \int n\,\mathrm{d}s$, and that the wavelength in these conditions is the **vacuum** wavelength $\lambda_0$. The factor of $n$ inside $L$ already accounts for the wavelength compression in every medium the paths traverse, so the interference condition can be stated once and for all in terms of $\lambda_0$, regardless of what materials the two paths pass through.

<!-- ─── -->

**5. Slab in an interferometer.** A slab of thickness $d$ and refractive index $n$ is inserted into one arm of an interferometer. By how much does the optical path length change compared to the same thickness of vacuum? Express your answer in terms of $d$, $n$, and $\lambda_{0}$.

**Solution.**

Optical path length is $L = \int n\,\mathrm{d}s$. Over a geometric thickness $d$ of a uniform medium of index $n$, this is simply $L = n\,d$.

*With the slab.* The light crosses thickness $d$ of index-$n$ material:

$$
L_{\text{slab}} = n\,d.
$$

*Without the slab (same thickness of vacuum).* The same geometric gap $d$ is now vacuum, $n = 1$:

$$
L_{\text{vacuum}} = (1)\,d = d.
$$

*Change in optical path length.* Inserting the slab lengthens the optical path of that arm by

$$
\Delta L = L_{\text{slab}} - L_{\text{vacuum}} = n d - d = (n - 1)\,d.
$$

The geometric thickness is unchanged — it is the *optical* path that grows, because each layer of glass packs in $n$ times as many wave crests as the vacuum it replaced.

*Phase shift and fringe count.* The vacuum wavelength $\lambda_0$ enters once $\Delta L$ is converted to a phase. The extra phase the slab introduces in that arm is

$$
\Delta\Phi = k_0\,\Delta L = \frac{2\pi\,(n - 1)\,d}{\lambda_0},
$$

and the number of interference fringes that sweep across the field as the slab is inserted is

$$
N = \frac{\Delta\Phi}{2\pi} = \frac{(n - 1)\,d}{\lambda_0}.
$$

This is the working principle of precision-refractometry interferometers: counting the fringe shift $N$ for a known thickness $d$ measures $n - 1$ to high precision, since even a tiny index difference produces a countable number of fringes when $d \gg \lambda_0$.
