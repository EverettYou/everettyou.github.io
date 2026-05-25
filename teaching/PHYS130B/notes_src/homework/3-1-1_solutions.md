# 3.1.1 Geometric Optics
Worked solutions for the homework problems in the [3.1.1 Geometric Optics](../ch3_path-integral/3-1-1-geometric-optics) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Reflection from Fermat.** Use Fermat's principle to derive the law of reflection. Consider a ray from $A$ to $B$ reflecting off a flat mirror. Show that the angle of incidence equals the angle of reflection.

**Solution.**

*Setup.* Place the mirror in the plane $y = 0$ and put source and target on the same side of it, $A = (0, a)$ and $B = (d, b)$ with $a, b > 0$. The ray travels through a single uniform medium of constant refractive index $n$, strikes the mirror at the point $P = (x, 0)$, and the only freedom is the crossing coordinate $x$. Because $n$ is constant, the optical path length is just $n$ times the geometric length,

$$
L(x) = n\,\ell(x), \qquad \ell(x) = \overline{AP} + \overline{PB} = \sqrt{x^2 + a^2} + \sqrt{(d-x)^2 + b^2},
$$

so extremizing $L$ is the same as extremizing $\ell$.

*Fermat's condition.* Differentiate and set $\mathrm{d}L/\mathrm{d}x = 0$:

$$
\frac{1}{n}\frac{\mathrm{d}L}{\mathrm{d}x} = \frac{\mathrm{d}\ell}{\mathrm{d}x} = \frac{x}{\sqrt{x^2 + a^2}} - \frac{d - x}{\sqrt{(d-x)^2 + b^2}} = 0.
$$

*Read off the angles.* Measure angles from the **normal** to the mirror (the vertical direction). The incident segment $AP$ descends from height $a$ over a horizontal run $x$, so the angle of incidence $\theta_i$ satisfies

$$
\sin\theta_i = \frac{x}{\sqrt{x^2 + a^2}}.
$$

The reflected segment $PB$ rises to height $b$ over a horizontal run $d - x$, so the angle of reflection $\theta_r$ satisfies

$$
\sin\theta_r = \frac{d - x}{\sqrt{(d-x)^2 + b^2}}.
$$

Fermat's condition is therefore $\sin\theta_i = \sin\theta_r$, and since both angles lie in $[0, \pi/2)$,

$$
\theta_i = \theta_r. \qquad\checkmark
$$

*It is a genuine minimum.* The second derivative is

$$
\frac{\mathrm{d}^2\ell}{\mathrm{d}x^2} = \frac{a^2}{(x^2 + a^2)^{3/2}} + \frac{b^2}{((d-x)^2 + b^2)^{3/2}} > 0,
$$

so the stationary path is the shortest path — for a flat mirror the reflected ray genuinely minimizes the optical path length.

*Geometric picture (the mirror-image trick).* The same result follows without calculus. Reflect the target across the mirror to its image $B' = (d, -b)$. Every candidate path obeys $\overline{PB} = \overline{PB'}$, so $\ell = \overline{AP} + \overline{PB'}$ is the length of a two-segment broken line from $A$ to $B'$. This is shortest when $A$, $P$, $B'$ are collinear — a single straight line. Along that straight line the angle $AP$ makes with the normal equals the angle $PB'$ makes with it; since $PB'$ is the mirror image of $PB$, that second angle equals $\theta_r$. Collinearity therefore gives $\theta_i = \theta_r$, with incident ray, reflected ray, and normal all lying in one plane.

<!-- ─── -->

**2. Total internal reflection.** Light travels from glass ($n=1.5$) into air ($n=1.0$).

(a) Find the critical angle $\theta_c$ beyond which total internal reflection occurs.

(b) Explain physically, using Snell's law, why no refracted ray exists for $\theta > \theta_c$.

**Solution.**

*Setup.* Snell's law at the glass–air interface relates the angle in the glass ($n_1 = 1.5$) to the angle in the air ($n_2 = 1.0$):

$$
n_1 \sin\theta_1 = n_2 \sin\theta_2.
$$

Since $n_1 > n_2$, the ray bends *away* from the normal on crossing into air: $\sin\theta_2 = (n_1/n_2)\sin\theta_1 > \sin\theta_1$, so $\theta_2 > \theta_1$.

**(a) Critical angle.** As $\theta_1$ increases, $\theta_2$ grows faster and reaches its largest possible value $\theta_2 = 90^\circ$ — the refracted ray grazing along the interface — while $\theta_1$ is still below $90^\circ$. The incidence angle at which this happens is the critical angle $\theta_c$, fixed by $\sin\theta_2 = 1$:

$$
n_1 \sin\theta_c = n_2 \sin 90^\circ = n_2,
$$

so $\sin\theta_c = n_2/n_1 = 1.0/1.5 = 2/3$.

Hence

$$
\theta_c = \arcsin\frac{2}{3} \approx 41.8^\circ.
$$

**(b) Why no refracted ray exists for $\theta > \theta_c$.** For an incidence angle beyond critical, Snell's law would demand

$$
\sin\theta_2 = \frac{n_1}{n_2}\sin\theta_1 > \frac{n_1}{n_2}\sin\theta_c = 1.
$$

But $\sin\theta_2 \le 1$ for every real angle — there is no real $\theta_2$ that solves the equation. Physically, the transmitted ray would have to bend *past* the grazing direction, which is geometrically impossible: the air offers no propagation direction into which the light could refract. With the transmission channel closed, energy conservation forces **all** the incident light back into the glass, and the boundary behaves as a perfect mirror. This is total internal reflection — the principle behind optical fibers, in which light is trapped in the core by striking the core–cladding boundary at angles that always exceed $\theta_c$.

<!-- ─── -->

**3. Stratified index gradient.** A medium has refractive index $n(z) = n_0(1 + \alpha z)$ for small $\alpha > 0$, with $z$ a fixed vertical coordinate in the laboratory (larger $z$ means larger $n$). A light ray travels nearly horizontally along the $x$ direction. Using Fermat's principle, show that the ray **curves toward larger $z$**.

**Solution.**

Larger $z$ means larger $n$. Fermat's principle varies the path $z(x)$:

$$
L[z] = \int_0^d n(z)\,\sqrt{1 + z'^2}\,\mathrm{d}x, \qquad n(z) = n_0(1 + \alpha z), \qquad \delta L = 0.
$$

*Step 1 — variation to the Euler–Lagrange equation.* Write the integrand as a **Lagrangian density** $\ell$ (a function of $z$ and $z'=\mathrm{d}z/\mathrm{d}x$):

$$
\ell(z,z') = n(z)\sqrt{1+z'^2}, \qquad L[z] = \int_0^d \ell(z,z')\,\mathrm{d}x.
$$

**Perturb the path.** Let $z(x)$ be the trial path and $\delta z(x)$ a small displacement with **fixed endpoints** ($\delta z(0)=\delta z(d)=0$). Then $z\to z+\delta z$ and $z'\to z'+\delta z'$, with $\delta z' = \mathrm{d}(\delta z)/\mathrm{d}x$.

**First-order change in $L$.** To linear order in $\delta z$,

$$
\delta L = \int_0^d \left(\frac{\partial\ell}{\partial z}\,\delta z + \frac{\partial\ell}{\partial z'}\,\delta z'\right)\mathrm{d}x.
$$

**Integration by parts** on the $z'$ term (write $\delta z' = \mathrm{d}(\delta z)/\mathrm{d}x$):

$$
\int_0^d \frac{\partial\ell}{\partial z'}\,\delta z'\,\mathrm{d}x
= \int_0^d \frac{\partial\ell}{\partial z'}\,\frac{\mathrm{d}(\delta z)}{\mathrm{d}x}\,\mathrm{d}x
= \left[\frac{\partial\ell}{\partial z'}\,\delta z\right]_0^d - \int_0^d \frac{\mathrm{d}}{\mathrm{d}x}\!\left(\frac{\partial\ell}{\partial z'}\right)\delta z\,\mathrm{d}x.
$$

The **boundary term vanishes** because $\delta z(0)=\delta z(d)=0$. Collecting terms,

$$
\delta L = \int_0^d \left(\frac{\partial\ell}{\partial z} - \frac{\mathrm{d}}{\mathrm{d}x}\frac{\partial\ell}{\partial z'}\right)\delta z\,\mathrm{d}x.
$$

**Stationarity.** Fermat's principle $\delta L = 0$ must hold for every admissible $\delta z$ on the interior, so the bracket must vanish pointwise. This is the **Euler–Lagrange equation**

$$
\frac{\partial\ell}{\partial z} = \frac{\mathrm{d}}{\mathrm{d}x}\!\left(\frac{\partial\ell}{\partial z'}\right) \qquad \text{(LHS $= \partial\ell/\partial z$, RHS $= \mathrm{d}(\partial\ell/\partial z')/\mathrm{d}x$)}.
$$

*Step 2 — compute both sides.* For $n(z)=n_0(1+\alpha z)$,

$$
\frac{\partial\ell}{\partial z} = n_0\alpha\sqrt{1+z'^2}, \qquad
\frac{\partial\ell}{\partial z'} = n_0(1+\alpha z)\,\frac{z'}{\sqrt{1+z'^2}}.
$$

*Step 3 — horizontal launch at $x=0$.* Take $z(0)=0$ and $z'(0)=0$. Then $\partial\ell/\partial z'|_{x=0}=0$, but the Euler–Lagrange equation still relates the **$x$-derivative** of $\partial\ell/\partial z'$ to $\partial\ell/\partial z$. Label the two members **LHS** $= \partial\ell/\partial z$ and **RHS** $= \mathrm{d}(\partial\ell/\partial z')/\mathrm{d}x$, and evaluate each at $x=0$.

**Left-hand side (LHS):** $\partial\ell/\partial z$, evaluated at $x=0$ (with $z'(0)=0$):

$$
\text{LHS} = n_0\alpha\sqrt{1+z'^2}\,\Big|_{z'=0} = n_0\alpha.
$$

**Right-hand side (RHS):** $\mathrm{d}(\partial\ell/\partial z')/\mathrm{d}x$, evaluated at $x=0$:

$$
\text{RHS} = n_0\,\frac{\mathrm{d}}{\mathrm{d}x}\!\left[(1+\alpha z)\,\frac{z'}{\sqrt{1+z'^2}}\right]\bigg|_{x=0}.
$$

At $z(0)=0$ and $z'(0)=0$, the product $(1+\alpha z)\,z'/\sqrt{1+z'^2}$ vanishes but has nonzero slope; only the factor $z'/\sqrt{1+z'^2}$ contributes at linear order:

$$
\text{RHS} = n_0\,\frac{\mathrm{d}}{\mathrm{d}x}\!\left[\frac{z'}{\sqrt{1+z'^2}}\right]\bigg|_{x=0}
= n_0 z''(0).
$$

Equating LHS $=$ RHS,

$$
n_0\alpha = n_0 z''(0),
$$

so $z''(0) = \alpha > 0$.

That is the conclusion: immediately after a horizontal launch, the path curves toward **larger $z$** (positive $z''$ at $x=0$).

<!-- ─── -->

**4. Stationary versus minimum.** In the standard Snell's law geometry, the source $A$ is at $(0,-h_1)$, the target $B$ at $(d,h_2)$, and the ray crosses the interface at $(x,0)$. The optical path length is $L(x) = n_1\sqrt{x^2+h_1^2} + n_2\sqrt{(d-x)^2+h_2^2}$. Show that $\mathrm{d}^2 L/\mathrm{d}x^2 > 0$, confirming the stationary path is a minimum, not a maximum.

**Solution.**

*The function.* With source $A = (0, -h_1)$, interface crossing at $(x, 0)$, and target $B = (d, h_2)$, the optical path length is

$$
L(x) = n_1\sqrt{x^2 + h_1^2} + n_2\sqrt{(d-x)^2 + h_2^2}.
$$

*First derivative.* Using $\dfrac{\mathrm{d}}{\mathrm{d}x}\sqrt{x^2+h_1^2} = \dfrac{x}{\sqrt{x^2+h_1^2}}$ and the chain rule on the second term,

$$
\frac{\mathrm{d}L}{\mathrm{d}x} = n_1\frac{x}{\sqrt{x^2 + h_1^2}} - n_2\frac{d - x}{\sqrt{(d-x)^2 + h_2^2}}.
$$

Setting this to zero reproduces Snell's law, $n_1\sin\theta_1 = n_2\sin\theta_2$, with $\sin\theta_1 = x/\sqrt{x^2+h_1^2}$ and $\sin\theta_2 = (d-x)/\sqrt{(d-x)^2+h_2^2}$.

*Second derivative.* Differentiate each term again. For the first, the quotient rule gives

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left[\frac{x}{\sqrt{x^2 + h_1^2}}\right] = \frac{\sqrt{x^2+h_1^2} - x\cdot\dfrac{x}{\sqrt{x^2+h_1^2}}}{x^2 + h_1^2} = \frac{(x^2 + h_1^2) - x^2}{(x^2 + h_1^2)^{3/2}} = \frac{h_1^2}{(x^2 + h_1^2)^{3/2}}.
$$

For the second term, write $u = d - x$ so that $\mathrm{d}u/\mathrm{d}x = -1$; the same computation applied to $u/\sqrt{u^2+h_2^2}$, together with the chain-rule sign, gives

$$
\frac{\mathrm{d}}{\mathrm{d}x}\left[-\,n_2\frac{d-x}{\sqrt{(d-x)^2 + h_2^2}}\right] = -\,n_2\cdot(-1)\cdot\frac{h_2^2}{((d-x)^2 + h_2^2)^{3/2}} = +\,n_2\frac{h_2^2}{((d-x)^2 + h_2^2)^{3/2}}.
$$

Collecting the two pieces,

$$
\frac{\mathrm{d}^2 L}{\mathrm{d}x^2} = \frac{n_1 h_1^2}{(x^2 + h_1^2)^{3/2}} + \frac{n_2 h_2^2}{((d-x)^2 + h_2^2)^{3/2}}.
$$

*Sign.* Every factor is non-negative: $n_1, n_2 > 0$, the heights $h_1^2, h_2^2 \ge 0$, and the denominators are positive. In any genuine refraction geometry $A$ and $B$ lie off the interface ($h_1, h_2 \neq 0$), so both terms are strictly positive and

$$
\frac{\mathrm{d}^2 L}{\mathrm{d}x^2} > 0.
$$

Thus $L(x)$ is strictly convex; its single stationary point is a **minimum**, and the Snell's-law ray is the path of *least* optical path length. (Equivalently: each term $\sqrt{x^2 + h^2}$ is a convex function of $x$, and a positive-coefficient sum of convex functions is convex.) For this flat-interface geometry "stationary" and "minimum" coincide — the distinction in Fermat's principle becomes important only for curved interfaces and caustics, where the second derivative can change sign and the true ray can be a saddle point or a local maximum.

<!-- ─── -->

**5. Corpuscle versus wave speed.** Newton's corpuscle theory predicts that light speeds up when entering a denser medium (the particles are attracted inward). The wave theory predicts light slows down: $v = c/n < c$ for $n > 1$. The Foucault experiment (1850) measured the speed of light in water and found it less than $c$.

(a) Which theory does this experimental result support?

(b) Snell's law $n_1 \sin\theta_1 = n_2 \sin\theta_2$ follows from Fermat's principle regardless of whether light speeds up or slows down in the denser medium. Does Fermat's principle depend on the direction of the speed change, or only on the value of $n$?

**Solution.**

**(a) Which theory the Foucault result supports.** The two theories make *opposite* predictions for the speed of light inside a dense medium. Newton's corpuscle theory accounts for refraction by having the denser medium attract the light particles as they cross the boundary, increasing their velocity component along the normal — so corpuscles travel *faster* in the denser medium. The wave theory has $v = c/n < c$ for $n > 1$ — light travels *slower* in the denser medium. Foucault's 1850 measurement found the speed of light in water to be **less** than its vacuum value $c$. This matches $v = c/n$ and contradicts the corpuscle prediction, so the experiment supports the **wave theory**. Historically it was regarded as a decisive blow against the corpuscular picture.

**(b) Does Fermat's principle care about the direction of the speed change?** No — in the form used to derive Snell's law, it depends only on the *value* of the refractive index. Snell's law was obtained by extremizing the optical path length

$$
L = \int n(\boldsymbol{r})\,\mathrm{d}s,
$$

in which $n(\boldsymbol{r})$ appears purely as a position-dependent weight. The derivation never refers to how $n$ is related to a propagation speed, so it yields $n_1\sin\theta_1 = n_2\sin\theta_2$ whether light speeds up or slows down in the denser medium.

The direction of the speed change matters only when one adopts the *least-time* reading of Fermat's principle, $T = \int \mathrm{d}s / v$. That form reproduces $L = \int n\,\mathrm{d}s$ — and hence the correct Snell's law — only if $v = c/n$, i.e. light slows in the denser medium. Had light instead sped up there ($v \propto n$), the least-time path would obey the *inverted* relation $\sin\theta_1/\sin\theta_2 = n_2/n_1$, which disagrees with experiment. So Fermat's principle *as a statement about the optical path length* is blind to the sign of the speed change; it is the physical mechanism behind the index — and equivalently the least-time interpretation — that the Foucault experiment pins down.

<!-- ─── -->

**6. Curved mirror focusing.** A concave spherical mirror of curvature radius $R$ has its vertex at the origin and its axis along $z$. A point light source sits on the axis at distance $u$ from the vertex. A reflected ray leaves the source, hits the mirror at a point $P$ that is height $h$ above the axis, and returns to an image point on the axis at distance $v$ from the vertex.

(a) In the paraxial regime ($h \ll R$), show that the mirror surface at height $h$ is displaced from the vertex by approximately $h^2/(2R)$ along the axis.

(b) Expand the total optical path length $L(h) = d_1(h) + d_2(h)$ — where $d_1$ is the source-to-$P$ distance and $d_2$ is the $P$-to-image distance — to second order in $h$, and show that

$$
L(h) \approx (u + v) + \frac{h^2}{2}\!\left(\frac{1}{u} + \frac{1}{v} - \frac{2}{R}\right).
$$

(c) Apply Fermat's principle: require that $L$ is stationary with respect to $h$ for every paraxial ray. Derive the mirror equation $1/u + 1/v = 2/R$.

**Solution.**

*Geometry.* Put the vertex of the mirror at the origin with its axis along $z$, and let the centre of curvature lie on the axis at $(0,0,R)$, so the spherical surface satisfies

$$
\rho^2 + (z - R)^2 = R^2,
$$

with $\rho$ the distance from the axis. The source sits on the axis at distance $u$ from the vertex and the image at distance $v$.

**(a) Sagitta of the mirror.** A point $P$ on the mirror at height $\rho = h$ has axial coordinate $z_P$ fixed by $h^2 + (z_P - R)^2 = R^2$, i.e.

$$
z_P = R - \sqrt{R^2 - h^2}
$$

(the root near the vertex, with $z_P \to 0$ as $h \to 0$). For a paraxial ray $h \ll R$, expand the square root:

$$
\sqrt{R^2 - h^2} = R\sqrt{1 - \frac{h^2}{R^2}} = R\left(1 - \frac{h^2}{2R^2} + \cdots\right) = R - \frac{h^2}{2R} + \cdots.
$$

Hence

$$
z_P = R - \left(R - \frac{h^2}{2R}\right) = \frac{h^2}{2R}.
$$

The mirror surface at height $h$ is displaced from the vertex by $h^2/(2R)$ along the axis — the *sagitta* of a shallow spherical cap. $\checkmark$

**(b) Optical path length to second order.** Take $P = (h, 0, z_P)$ with $z_P = h^2/2R$. The source-to-$P$ distance is

$$
d_1 = \sqrt{h^2 + (u - z_P)^2} = \sqrt{h^2 + \left(u - \tfrac{h^2}{2R}\right)^2}.
$$

Square it and keep terms through order $h^2$ (the $z_P^2 \propto h^4$ term is dropped):

$$
d_1^2 = h^2 + u^2 - 2u\cdot\frac{h^2}{2R} + O(h^4) = u^2 + h^2\left(1 - \frac{u}{R}\right) + O(h^4).
$$

Therefore

$$
d_1 = u\sqrt{1 + \frac{h^2}{u^2}\left(1 - \frac{u}{R}\right)} = u\left[1 + \frac{h^2}{2u^2}\left(1 - \frac{u}{R}\right) + \cdots\right] = u + \frac{h^2}{2}\left(\frac{1}{u} - \frac{1}{R}\right).
$$

The $P$-to-image distance $d_2$ has exactly the same form with $u \to v$:

$$
d_2 = v + \frac{h^2}{2}\left(\frac{1}{v} - \frac{1}{R}\right).
$$

The mirror sits in a single medium ($n$ constant), so the optical path length is proportional to $d_1 + d_2$; dropping the common factor,

$$
L(h) = d_1 + d_2 = (u + v) + \frac{h^2}{2}\left(\frac{1}{u} + \frac{1}{v} - \frac{2}{R}\right). \qquad\checkmark
$$

**(c) The mirror equation.** Fermat's principle requires the optical path length to be stationary. Here

$$
\frac{\mathrm{d}L}{\mathrm{d}h} = h\left(\frac{1}{u} + \frac{1}{v} - \frac{2}{R}\right).
$$

A point source produces a sharp image at distance $v$ only if *every* paraxial ray — every value of $h$ — leaves the source and arrives at the image along a stationary path. Equivalently, all these rays must share the same optical path length, so $L(h)$ must be independent of $h$ to this order. Either statement forces the coefficient of $h^2$ to vanish:

$$
\frac{1}{u} + \frac{1}{v} - \frac{2}{R} = 0,
$$

i.e. $\dfrac{1}{u} + \dfrac{1}{v} = \dfrac{2}{R}$.

This is the mirror equation; the focal length is $f = R/2$ (a parallel beam, $u \to \infty$, focuses at $v = R/2$). The deeper reading: once the mirror equation holds, $L(h) = u + v$ for *all* paraxial rays — every ray path is not merely stationary but *equal in length*, which is exactly the condition for the reflected wavefronts to reconverge in phase at the image. A spherical mirror meets this condition only approximately; the leading correction is the $O(h^4)$ term, which is spherical aberration. A paraboloidal mirror meets it exactly for a beam from infinity.

<!-- ─── -->

**7. Optics-mechanics dictionary.** The optical path length $L = \int n \,\mathrm{d}s$ plays the role of action for light, and Fermat's principle ($\delta L = 0$) mirrors Hamilton's principle ($\delta S = 0$).

(a) In a uniform medium ($n = \text{const}$), Fermat's principle reduces to finding the shortest geometric path. What is the analogous statement for a free particle under Hamilton's principle?

(b) In a medium with spatially varying $n(\boldsymbol{r})$, light curves toward regions of higher $n$ (cf. Problem 3). What mechanical system exhibits analogous behavior — a particle curving toward regions of lower potential energy — and what quantity plays the role of $n$?

**Solution.**

**(a) The free-particle analog of a straight ray.** In a uniform medium Fermat's principle reduces $L = \int n\,\mathrm{d}s = n\int\mathrm{d}s$ to "make the geometric length stationary," whose solution is a straight line. The mechanical counterpart is Hamilton's principle $\delta S = 0$, with $S = \int L_{\text{mech}}\,\mathrm{d}t$, applied to a **free particle** (constant potential), for which $L_{\text{mech}} = \tfrac12 m\dot{\boldsymbol{r}}^2$. Extremizing the action gives the Euler–Lagrange equation $m\ddot{\boldsymbol{r}} = 0$: the particle travels in a **straight line at constant speed** — uniform rectilinear motion, Newton's first law. So "uniform medium $\Rightarrow$ straight ray" corresponds to "no force $\Rightarrow$ straight, uniform-speed trajectory." In each case the path is a geodesic — the straightest line available — because nothing in the medium, or in the potential, distinguishes one region from another.

**(b) Curving toward higher $n$, and what plays the role of $n$.** The mechanical analog is a **particle of fixed energy $E$ moving in a potential $V(\boldsymbol{r})$**. The precise form of the analogy is the **abbreviated-action form** of Hamilton's principle: at fixed energy, the trajectory extremizes the *abbreviated action*

$$
W = \int p\,\mathrm{d}s, \qquad p = \sqrt{2m\,(E - V(\boldsymbol{r}))}.
$$

This has exactly the structure of $L = \int n\,\mathrm{d}s$, with the **momentum magnitude $p$ playing the role of the refractive index $n$**. The dictionary is

$$
n(\boldsymbol{r}) \;\longleftrightarrow\; p(\boldsymbol{r}) = \sqrt{2m\,(E - V(\boldsymbol{r}))}, \qquad L = \int n\,\mathrm{d}s \;\longleftrightarrow\; W = \int p\,\mathrm{d}s.
$$

Where the potential $V$ is *lower*, the kinetic energy $E - V$ is larger, so the momentum $p$ is larger. By the same Fermat trade-off as in Problem 3, the trajectory bends toward the region of larger $p$ — that is, toward **lower potential energy**. A particle crossing a landscape veers toward the valleys, just as a light ray veers toward high refractive index. The two behaviors are the *same* variational statement, $\delta\int n\,\mathrm{d}s = 0 \leftrightarrow \delta\int p\,\mathrm{d}s = 0$ — an analogy so close that it later guided the construction of wave mechanics, where this optical–mechanical correspondence becomes literal rather than merely formal.
