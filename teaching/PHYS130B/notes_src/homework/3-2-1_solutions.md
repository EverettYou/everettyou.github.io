# 3.2.1 Path Integral Formulation
Worked solutions for the homework problems in the [3.2.1 Path Integral Formulation](../ch3_path-integral/3-2-1-path-integral-formulation) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

★ **1. Wavepacket spreading.** A free particle begins in the Gaussian state $\psi(x,0) = (\pi\sigma^{2})^{-1/4}\exp(-x^{2}/(2\sigma^{2}))$ with width $\sigma$.

(a) Treat $\Delta x \sim \sigma$ and use $\Delta x\,\Delta p \gtrsim \hbar$ to estimate the momentum spread and the position spread after time $t$. Identify the characteristic time $\tau \sim m\sigma^{2}/\hbar$ at which the packet width is no longer $\mathcal{O}(\sigma)$.

(b) The free propagator is

$$
K(x,t;x',0) = \sqrt{\frac{m}{2\pi\mathrm{i}\hbar t}}\,\exp\!\left(\frac{\mathrm{i}m(x-x')^{2}}{2\hbar t}\right).
$$

Use $\psi(x,t)=\int K(x,t;x',0)\,\psi(x',0)\,\mathrm{d}x'$ to show that $|\psi(x,t)|^{2}$ remains Gaussian with $\sigma_{t} = \sigma\sqrt{1 + (t/\tau)^{2}}$.

(c) Evaluate $\tau$ for an electron with $\sigma = 1\,\text{Å}$.

**Solution.**

**(a) Uncertainty estimate.** The initial localization sets $\Delta x \sim \sigma$. The minimum-uncertainty relation $\Delta x\,\Delta p \gtrsim \hbar$ then gives a momentum spread $\Delta p \sim \hbar/\sigma$ (order of magnitude; a Gaussian saturates the bound up to factors of order unity). The corresponding velocity uncertainty is

$$
\Delta v \sim \frac{\Delta p}{m} \sim \frac{\hbar}{m\sigma}.
$$

After time $t$ a classical estimate of the extra spread is $\Delta x_{\mathrm{spread}} \sim \Delta v\,t \sim \hbar t/(m\sigma)$. The total width is therefore no longer $\mathcal{O}(\sigma)$ once this term is comparable to $\sigma$, i.e. when

$$
\frac{\hbar t}{m\sigma} \sim \sigma,
$$

i.e. $t \sim m\sigma^{2}/\hbar \equiv \tau$.

For $t \ll \tau$ the packet stays essentially at its initial width; for $t \gg \tau$ the width grows linearly, $\sigma_{t} \sim \hbar t/(m\sigma) = \sigma\,t/\tau$. The same scale $\tau$ will emerge exactly from the propagator in part (c). $\checkmark$

**(b) Propagator check.** The evolved wavefunction is the convolution

$$
\psi(x,t) = \sqrt{\frac{m}{2\pi\mathrm{i}\hbar t}}\,(\pi\sigma^{2})^{-1/4}\int_{-\infty}^{\infty}\exp\!\left[\frac{\mathrm{i}m(x-x')^{2}}{2\hbar t} - \frac{x'^{2}}{2\sigma^{2}}\right]\mathrm{d}x'.
$$

Collect the exponent as a quadratic in the integration variable $x'$. Writing $\alpha \equiv \mathrm{i}m/(2\hbar t)$, the bracket is

$$
\alpha(x-x')^{2} - \frac{x'^{2}}{2\sigma^{2}} = -\beta\,x'^{2} - 2\alpha x\,x' + \alpha x^{2}, \qquad \beta \equiv \frac{1}{2\sigma^{2}} - \alpha.
$$

Because $\mathrm{Re}\,\beta = 1/(2\sigma^{2}) > 0$, the Gaussian integral converges. Using $\int_{-\infty}^{\infty}\mathrm{e}^{-\beta x'^{2} + \gamma x'}\,\mathrm{d}x' = \sqrt{\pi/\beta}\;\mathrm{e}^{\gamma^{2}/(4\beta)}$ with $\gamma = -2\alpha x$,

$$
\int_{-\infty}^{\infty}\exp[\cdots]\,\mathrm{d}x' = \sqrt{\frac{\pi}{\beta}}\;\exp\!\left[\alpha x^{2} + \frac{\alpha^{2}x^{2}}{\beta}\right] = \sqrt{\frac{\pi}{\beta}}\;\exp\!\left[\frac{\alpha(\beta+\alpha)}{\beta}\,x^{2}\right].
$$

The combination $\beta + \alpha = 1/(2\sigma^{2})$ collapses the exponent to $\alpha x^{2}/(2\sigma^{2}\beta)$.

It is cleanest to introduce the **spreading time scale** $\tau \equiv m\sigma^{2}/\hbar$ now and simplify. The prefactor becomes

$$
\sqrt{\frac{m}{2\pi\mathrm{i}\hbar t}}\,\sqrt{\frac{\pi}{\beta}} = \sqrt{\frac{m}{2\mathrm{i}\hbar t\,\beta}}, \qquad 2\mathrm{i}\hbar t\,\beta = \frac{\mathrm{i}\hbar t}{\sigma^{2}} + m = m\!\left(1 + \mathrm{i}\,t/\tau\right),
$$

so the prefactor is $(1+\mathrm{i}t/\tau)^{-1/2}$. The exponent simplifies the same way: with $2\sigma^{2}\beta = 1 - \mathrm{i}\tau/t$,

$$
\frac{\alpha x^{2}}{2\sigma^{2}\beta} = \frac{\mathrm{i}m\,x^{2}}{2\hbar(t - \mathrm{i}\tau)} = \frac{-x^{2}/(2\sigma^{2})}{1 + \mathrm{i}t/\tau}.
$$

Collecting everything,

$$
\psi(x,t) = \frac{(\pi\sigma^{2})^{-1/4}}{\sqrt{1 + \mathrm{i}t/\tau}}\,\exp\!\left[\frac{-x^{2}/(2\sigma^{2})}{1 + \mathrm{i}t/\tau}\right], \qquad \tau \equiv \frac{m\sigma^{2}}{\hbar}.
$$

At $t=0$ this reduces to the initial state, as it must. The wavepacket stays Gaussian — the free propagator is itself a Gaussian (in $x-x'$), and a Gaussian convolved with a Gaussian is again Gaussian.

Take the square modulus for the probability density. The prefactor contributes $\vert 1+\mathrm{i}t/\tau\vert^{-1} = [1+(t/\tau)^{2}]^{-1/2}$. For the exponential, multiply numerator and denominator of the exponent by the conjugate $(1-\mathrm{i}t/\tau)$:

$$
\frac{-x^{2}/(2\sigma^{2})}{1+\mathrm{i}t/\tau} = \frac{-x^{2}/(2\sigma^{2})\,(1-\mathrm{i}t/\tau)}{1+(t/\tau)^{2}}, \qquad \mathrm{Re} = \frac{-x^{2}/(2\sigma^{2})}{1+(t/\tau)^{2}}.
$$

Since $\vert\mathrm{e}^{z}\vert^{2} = \mathrm{e}^{2\,\mathrm{Re}\,z}$,

$$
\vert\psi(x,t)\vert^{2} = \frac{(\pi\sigma^{2})^{-1/2}}{\sqrt{1+(t/\tau)^{2}}}\,\exp\!\left[\frac{-x^{2}}{\sigma^{2}\,[1+(t/\tau)^{2}]}\right].
$$

Define $\sigma_{t}^{2} \equiv \sigma^{2}\,[1+(t/\tau)^{2}]$. Then $\vert\psi\vert^{2} = (\sqrt{\pi}\,\sigma_{t})^{-1}\exp(-x^{2}/\sigma_{t}^{2})$ — a properly normalized Gaussian ($\int\vert\psi\vert^{2}\,\mathrm{d}x = 1$) of width

$$
\sigma_{t} = \sigma\sqrt{1 + (t/\tau)^{2}} = \sigma\sqrt{1 + \left(\frac{\hbar t}{m\sigma^{2}}\right)^{2}},
$$

since $t/\tau = \hbar t/(m\sigma^{2})$. This is exactly the stated result. $\checkmark$ The packet broadens monotonically; for $t \gg \tau$ the width grows linearly, $\sigma_{t}\approx\sigma\,t/\tau = \hbar t/(m\sigma)$, matching the uncertainty estimate in part (a).

**(c) Numerical spreading time.** The width has doubled in the area sense (set $\sigma_{t}=\sqrt{2}\,\sigma$) precisely when $t = \tau$, so $\tau = m\sigma^{2}/\hbar$ is the natural spreading time: a wavepacket localized to $\sigma$ stays roughly that localized only for times short compared with $\tau$.

For an electron with $\sigma = 1\,\text{Å} = 10^{-10}\,\text{m}$, using $m_{e} = 9.109\times10^{-31}\,\text{kg}$ and $\hbar = 1.055\times10^{-34}\,\mathrm{J\cdot s}$,

$$
\tau = \frac{m_{e}\sigma^{2}}{\hbar} = \frac{(9.109\times10^{-31})(10^{-10})^{2}}{1.055\times10^{-34}}\,\text{s} \approx 8.6\times10^{-17}\,\text{s}.
$$

So $\tau \approx 8.6\times10^{-17}\,\text{s} \approx 86\,\text{as}$ for this electron wavepacket.

<!-- ─── -->

**2. Composition test.** For the free propagator in Problem 1(b), verify the composition property by direct computation.

(a) Compute $\int K(x,t;x_{1},t/2)\,K(x_{1},t/2;x',0)\,\mathrm{d}x_{1}$ by completing the square in $x_{1}$, and show that the result equals $K(x,t;x',0)$.

(b) Repeat with two intermediate times to verify $\iint K(x,t;x_{2},2t/3)\,K(x_{2},2t/3;x_{1},t/3)\,K(x_{1},t/3;x',0)\,\mathrm{d}x_{1}\,\mathrm{d}x_{2} = K(x,t;x',0)$.

(c) Argue by induction that any uniform partition of $[0,t]$ into $N$ slices reproduces the same $K(x,t;x',0)$. This is the explicit verification that the time-sliced path integral converges to the propagator.

**Solution.**

**(a) Two equal slices.** The two factors have duration $t/2$ each:

$$
K(x,t;x_{1},t/2)\,K(x_{1},t/2;x',0) = \frac{m}{\pi\mathrm{i}\hbar t}\,\exp\!\left[\frac{\mathrm{i}m}{\hbar t}\Big((x-x_{1})^{2} + (x_{1}-x')^{2}\Big)\right],
$$

using $2\hbar(t/2) = \hbar t$ in each exponent and $\sqrt{m/(2\pi\mathrm{i}\hbar(t/2))}^{\,2} = m/(\pi\mathrm{i}\hbar t)$ for the prefactor. Complete the square in $x_{1}$:

$$
(x-x_{1})^{2} + (x_{1}-x')^{2} = 2\left(x_{1} - \frac{x+x'}{2}\right)^{2} + \frac{(x-x')^{2}}{2}.
$$

The second term carries no $x_{1}$, so the integral is a single Fresnel integral. With $\int_{-\infty}^{\infty}\mathrm{e}^{-\lambda u^{2}}\,\mathrm{d}u = \sqrt{\pi/\lambda}$ (principal branch, valid as a Fresnel integral for the imaginary $\lambda = -2\mathrm{i}m/(\hbar t)$),

$$
\int_{-\infty}^{\infty}\exp\!\left[\frac{2\mathrm{i}m}{\hbar t}\Big(x_{1}-\tfrac{x+x'}{2}\Big)^{2}\right]\mathrm{d}x_{1} = \sqrt{\frac{\pi\hbar t}{-2\mathrm{i}m}} = \sqrt{\frac{\pi\mathrm{i}\hbar t}{2m}}.
$$

Therefore

$$
\int K(x,t;x_{1},t/2)\,K(x_{1},t/2;x',0)\,\mathrm{d}x_{1} = \frac{m}{\pi\mathrm{i}\hbar t}\sqrt{\frac{\pi\mathrm{i}\hbar t}{2m}}\;\exp\!\left[\frac{\mathrm{i}m(x-x')^{2}}{2\hbar t}\right].
$$

The exponent is already that of $K(x,t;x',0)$. For the prefactor, square it: $\left(\tfrac{m}{\pi\mathrm{i}\hbar t}\right)^{2}\tfrac{\pi\mathrm{i}\hbar t}{2m} = \tfrac{m}{2\pi\mathrm{i}\hbar t}$, so (with the consistent principal branch) the prefactor equals $\sqrt{m/(2\pi\mathrm{i}\hbar t)}$. Hence

$$
\int K(x,t;x_{1},t/2)\,K(x_{1},t/2;x',0)\,\mathrm{d}x_{1} = K(x,t;x',0). \qquad \checkmark
$$

**The general composition lemma.** The same square-completion works for *any* intermediate time, not just the midpoint. Let a slice of duration $t_{1}$ be followed by one of duration $t_{2}$, with total $T = t_{1}+t_{2}$. Then

$$
\int_{-\infty}^{\infty} K(x,T;y,t_{1})\,K(y,t_{1};x',0)\,\mathrm{d}y = K(x,T;x',0).
$$

*Proof.* The exponent is $\tfrac{\mathrm{i}m}{2\hbar}\big[(x-y)^{2}/t_{2} + (y-x')^{2}/t_{1}\big]$. Writing the bracket as $A y^{2} - 2By + (x^{2}/t_{2} + x'^{2}/t_{1})$ with $A = 1/t_{1}+1/t_{2} = T/(t_{1}t_{2})$ and $B = x/t_{2}+x'/t_{1}$, completion of the square gives a $y$-integral plus a remainder $-B^{2}/A + x^{2}/t_{2} + x'^{2}/t_{1}$. Algebra collapses the remainder to $(x-x')^{2}/T$ (the $x^{2}$ and $x'^{2}$ coefficients each reduce to $1/T$, and the cross term to $-2/T$). The Gaussian integral over $y$ contributes $\sqrt{2\pi\mathrm{i}\hbar/(mA)}$, and the prefactors multiply to $\sqrt{m/(2\pi\mathrm{i}\hbar\,t_{1}t_{2}A)} = \sqrt{m/(2\pi\mathrm{i}\hbar T)}$, since $t_{1}t_{2}A = T$. The result is exactly $K(x,T;x',0)$. Part (a) is the case $t_{1}=t_{2}=t/2$. $\square$

**(b) Two intermediate times.** Apply the lemma twice. First integrate over $x_{1}$ — this composes the slices $[0,t/3]$ and $[t/3,2t/3]$, both reaching the time $2t/3$:

$$
\int K(x_{2},2t/3;x_{1},t/3)\,K(x_{1},t/3;x',0)\,\mathrm{d}x_{1} = K(x_{2},2t/3;x',0).
$$

Then integrate over $x_{2}$ — this composes $[0,2t/3]$ with the slice $[2t/3,t]$:

$$
\int K(x,t;x_{2},2t/3)\,K(x_{2},2t/3;x',0)\,\mathrm{d}x_{2} = K(x,t;x',0).
$$

So the double integral equals $K(x,t;x',0)$. $\checkmark$

**(c) Induction.** Claim: for every $N\ge1$, the uniform $N$-slice product integrated over the $N-1$ intermediate points reproduces $K(x,t;x',0)$:

$$
\int\!\Big[\prod_{n=1}^{N-1}\mathrm{d}x_{n}\Big]\prod_{n=0}^{N-1}K_{\delta t}(x_{n+1},x_{n}) = K(x,t;x',0), \qquad \delta t = t/N.
$$

*Base case* $N=1$: the product is the single factor $K_{\delta t}(x,x') = K(x,t;x',0)$, with no integration. *Inductive step:* assume the statement for $N$ slices (over any interval). For $N+1$ slices, perform the integration over the last intermediate point $x_{N}$. By the general composition lemma it merges the final slice $[t_{N},t]$ with its neighbour into one propagator spanning their combined duration, reducing the configuration to $N$ slices; the inductive hypothesis then collapses the rest to $K(x,t;x',0)$. Hence the statement holds for all $N$. $\square$

A stronger conclusion is worth noting: for the free particle the slicing formula is *exact at every finite $N$* — there is no discretization error — because the Fresnel/Gaussian kernel is closed under convolution. The $N\to\infty$ limit that *defines* the path integral is therefore trivial here; it is only for a non-quadratic action (a general potential) that the slice propagator is approximate and the limit does genuine work.

<!-- ─── -->

**3. Free-particle slice action.** Verify $S_{\mathrm{slice}} = m(x_{n+1}-x_n)^2/(2\delta t)$ by evaluating $S = \int_{t_n}^{t_{n+1}}\tfrac{1}{2}m\dot{x}^2\,\mathrm{d}\tau$ along the straight-line path $x(\tau) = x_n + (x_{n+1}-x_n)(\tau-t_n)/\delta t$.

**Solution.**

Differentiate the straight-line path. Its velocity is constant:

$$
\dot{x}(\tau) = \frac{\mathrm{d}}{\mathrm{d}\tau}\left[x_{n} + (x_{n+1}-x_{n})\frac{\tau-t_{n}}{\delta t}\right] = \frac{x_{n+1}-x_{n}}{\delta t} \equiv v_{n}.
$$

The integrand $\tfrac{1}{2}m\dot{x}^{2} = \tfrac{1}{2}m v_{n}^{2}$ is therefore constant over the slice, and the integral is just the constant times the slice duration $t_{n+1}-t_{n} = \delta t$:

$$
S = \int_{t_{n}}^{t_{n+1}}\tfrac{1}{2}m v_{n}^{2}\,\mathrm{d}\tau = \tfrac{1}{2}m v_{n}^{2}\,\delta t = \tfrac{1}{2}m\,\frac{(x_{n+1}-x_{n})^{2}}{\delta t^{2}}\,\delta t = \frac{m(x_{n+1}-x_{n})^{2}}{2\,\delta t}.
$$

This is $S_{\mathrm{slice}} = m(x_{n+1}-x_n)^2/(2\delta t)$. $\checkmark$ The result is exact for the straight-line path because a free particle covers it at constant speed; on the slice the straight line is in fact the *classical* trajectory (no force), so $S$ here is also the on-shell action.

<!-- ─── -->

**4. Slice action with a potential.** For the Lagrangian $L = \tfrac{1}{2}m\dot{x}^2 - V(x)$, repeat the straight-line estimate over a single slice and show that, to first order in $\delta t$,

$$
S_{\text{slice}} \;=\; \frac{m\,(x_{n+1}-x_n)^2}{2\,\delta t} \;-\; V\!\left(\tfrac{x_n+x_{n+1}}{2}\right)\delta t \;+\; O(\delta t^{\,2}).
$$

(a) Approximate $x(\tau)$ by the straight-line segment.

(b) Estimate $\int_{t_n}^{t_{n+1}} V(x(\tau))\,\mathrm{d}\tau$ using the midpoint value of $x(\tau)$ and explain why corrections are $O(\delta t^{\,2})$.

**Solution.**

**(a) Straight-line segment.** Take the same trial path as Problem 3, $x(\tau) = x_{n} + v_{n}(\tau-t_{n})$ with $v_{n} = (x_{n+1}-x_{n})/\delta t$. The slice action splits into kinetic and potential pieces,

$$
S_{\text{slice}} = \int_{t_{n}}^{t_{n+1}}\tfrac{1}{2}m\dot{x}^{2}\,\mathrm{d}\tau \;-\; \int_{t_{n}}^{t_{n+1}}V(x(\tau))\,\mathrm{d}\tau.
$$

The kinetic part is exactly the Problem 3 result, $\tfrac{1}{2}mv_{n}^{2}\,\delta t = m(x_{n+1}-x_{n})^{2}/(2\,\delta t)$.

**(b) The potential integral, midpoint estimate.** Parametrize the slice by $s = \tau - t_{n} \in [0,\delta t]$, so $x(\tau) = x_{n} + v_{n}s$. The midpoint $s = \delta t/2$ sits at

$$
x\big(t_{n}+\tfrac{\delta t}{2}\big) = x_{n} + v_{n}\frac{\delta t}{2} = \frac{x_{n}+x_{n+1}}{2} \equiv \bar{x}.
$$

Taylor-expand $V(x(\tau))$ along the segment about this midpoint, in powers of $(s-\delta t/2)$:

$$
V(x(\tau)) = V(\bar{x}) + V'(\bar{x})\,v_{n}\big(s-\tfrac{\delta t}{2}\big) + \tfrac{1}{2}V''(\bar{x})\,v_{n}^{2}\big(s-\tfrac{\delta t}{2}\big)^{2} + \cdots
$$

Integrate term by term over $s\in[0,\delta t]$, an interval symmetric about $s=\delta t/2$:

- the constant term gives $V(\bar{x})\,\delta t$;
- the linear term integrates to **zero** — it is odd about the midpoint;
- the quadratic term gives $\tfrac{1}{2}V''(\bar{x})v_{n}^{2}\int_{-\delta t/2}^{\delta t/2}u^{2}\,\mathrm{d}u = \dfrac{V''(\bar{x})\,v_{n}^{2}\,(\delta t)^{3}}{24}$.

Hence

$$
\int_{t_{n}}^{t_{n+1}}V(x(\tau))\,\mathrm{d}\tau = V(\bar{x})\,\delta t + \frac{V''(\bar{x})}{24}\,v_{n}^{2}(\delta t)^{3} + \cdots
$$

Combining the two pieces yields the stated result,

$$
S_{\text{slice}} = \frac{m(x_{n+1}-x_{n})^{2}}{2\,\delta t} - V(\bar{x})\,\delta t + O(\delta t^{2}). \qquad \checkmark
$$

*Why the correction is higher order.* Choosing the **midpoint** value $V(\bar{x})$ — rather than an endpoint value $V(x_{n})$ — is what makes the linear term cancel by symmetry; an endpoint estimate would leave a surviving $O(V' v_{n}\,\delta t^{2})$ error. The leading correction is then set by the curvature $V''$ and equals $\tfrac{1}{24}V''(\bar{x})\,v_{n}^{2}(\delta t)^{3}$. Rewriting $v_{n}\,\delta t = x_{n+1}-x_{n}$, this is $\tfrac{1}{24}V''(\bar{x})(x_{n+1}-x_{n})^{2}\,\delta t$. The slice displacement obeys $(x_{n+1}-x_{n})^{2} = O(\delta t)$ for the paths that contribute coherently to the path integral (Problem 7: $\vert x_{n+1}-x_{n}\vert \sim \sqrt{\hbar\,\delta t/m}$). Therefore the correction scales as $O(\delta t^{2})$ — one full power of $\delta t$ smaller than the retained $-V(\bar{x})\,\delta t$ term — and may be dropped to the order claimed. (Even for a smooth classical path with bounded $v_{n}$, the correction is $O(\delta t^{3})$, still within the $O(\delta t^{2})$ bound.) Physically: over an infinitesimal slice the particle barely moves, so the potential is nearly constant and its average is captured by the single midpoint value.

<!-- ─── -->

**5. Phase difference between nearby slices.** Two slice paths share the initial point $x_n$ but end at $x_{n+1}$ and $x_{n+1} + \Delta$ respectively, with $\vert\Delta\vert$ small.

(a) Compute the difference $\Delta S_{\text{slice}}$ between their free-particle slice actions to first order in $\Delta$.

(b) Identify the slice momentum $p_n = m(x_{n+1}-x_n)/\delta t$ and rewrite $\Delta S_{\text{slice}}/\hbar$ as $p_n\,\Delta/\hbar$.

(c) Comment on this result in light of the de Broglie relation $p = \hbar k$: what is the effective wavelength of the slice propagator as a function of $x_{n+1}$?

**Solution.**

**(a) Action difference.** Write the slice displacement as $d \equiv x_{n+1}-x_{n}$. The free-particle slice action (Problem 3) is $S_{\text{slice}}(x_{n+1}) = m d^{2}/(2\,\delta t)$. Shifting the endpoint by $\Delta$ replaces $d$ by $d+\Delta$:

$$
\Delta S_{\text{slice}} = \frac{m}{2\,\delta t}\Big[(d+\Delta)^{2} - d^{2}\Big] = \frac{m}{2\,\delta t}\big(2d\,\Delta + \Delta^{2}\big) = \frac{m\,d}{\delta t}\,\Delta + \frac{m}{2\,\delta t}\Delta^{2}.
$$

To first order in $\Delta$,

$$
\Delta S_{\text{slice}} = \frac{m\,(x_{n+1}-x_{n})}{\delta t}\,\Delta + O(\Delta^{2}).
$$

This is just $\Delta S_{\text{slice}} = (\partial S_{\text{slice}}/\partial x_{n+1})\,\Delta$ — the on-shell relation that the derivative of the action with respect to the final endpoint is the final momentum.

**(b) Slice momentum.** The coefficient is exactly the slice momentum $p_{n} = m(x_{n+1}-x_{n})/\delta t = m v_{n}$ (mass times the constant slice velocity). Hence

$$
\Delta S_{\text{slice}} = p_{n}\,\Delta, \qquad \frac{\Delta S_{\text{slice}}}{\hbar} = \frac{p_{n}\,\Delta}{\hbar}. \qquad \checkmark
$$

**(c) Effective wavelength and de Broglie.** The slice propagator carries the phase $\mathrm{e}^{\mathrm{i}S_{\text{slice}}/\hbar}$. Viewed as a function of the endpoint $x_{n+1}$, moving that endpoint by $\Delta$ advances the phase by $\Delta S_{\text{slice}}/\hbar = p_{n}\Delta/\hbar$. So locally the slice propagator oscillates in $x_{n+1}$ as a plane wave $\mathrm{e}^{\mathrm{i}p_{n}x_{n+1}/\hbar}$, with wave number

$$
k = \frac{p_{n}}{\hbar},
$$

so $\lambda = 2\pi/k = 2\pi\hbar/p_{n} = h/p_{n}$.

This is precisely the de Broglie relation $p = \hbar k = h/\lambda$. Substituting $p_{n} = m(x_{n+1}-x_{n})/\delta t$, the effective wavelength as a function of the endpoint is

$$
\lambda(x_{n+1}) = \frac{h}{p_{n}} = \frac{h\,\delta t}{m\,(x_{n+1}-x_{n})}.
$$

It depends on $x_{n+1}$: a larger slice displacement means a larger slice momentum and a *shorter* wavelength — a "faster" slice carries a finer matter wave. The path integral thus encodes de Broglie automatically: the principle "phase $= S/\hbar$" makes the local wavelength of the kernel equal to $h/p$. (This position-dependent local wavelength is the seed of the WKB picture, where $\lambda(x) = h/p(x)$ varies across a slowly changing potential.)

<!-- ─── -->

**6. Functional equation from composition.** Suppose the slice propagator depends on its arguments only through the displacement: $K_{\delta t}(x',x) = A(\delta t)\,F(x'-x;\delta t)$.

(a) Apply the composition property $K(x,t;x',t') = \int K(x,t;x_m,t_m)\,K(x_m,t_m;x',t')\,\mathrm{d}x_m$ to two consecutive slices of duration $\delta t$ each and show that

$$
F(x'-x;2\delta t) \;=\; A(\delta t)\int F(x'-y;\delta t)\,F(y-x;\delta t)\,\mathrm{d}y.
$$

(b) Verify dimensional consistency. (We do not yet know $A$ or $F$; the eventual closed form derived in §3.2.2 must satisfy this constraint.)

**Solution.**

**(a) Composition of two slices.** The composition property applied to two consecutive slices of duration $\delta t$, with intermediate point $y$, gives the duration-$2\delta t$ kernel

$$
K_{2\delta t}(x',x) = \int K_{\delta t}(x',y)\,K_{\delta t}(y,x)\,\mathrm{d}y.
$$

Insert the assumed displacement form $K_{\delta t} = A(\delta t)\,F(\,\cdot\,;\delta t)$ on the right:

$$
K_{2\delta t}(x',x) = A(\delta t)^{2}\int F(x'-y;\delta t)\,F(y-x;\delta t)\,\mathrm{d}y.
$$

The doubled slice is itself a propagator of the same kind, so it too has the form (prefactor)$\times$(displacement profile): $K_{2\delta t}(x',x) = A(2\delta t)\,F(x'-x;2\delta t)$. Equating the two expressions gives the exact constraint

$$
A(2\delta t)\,F(x'-x;2\delta t) = A(\delta t)^{2}\int F(x'-y;\delta t)\,F(y-x;\delta t)\,\mathrm{d}y.
$$

Solving for the doubled-slice profile,

$$
F(x'-x;2\delta t) = \frac{A(\delta t)^{2}}{A(2\delta t)}\int F(x'-y;\delta t)\,F(y-x;\delta t)\,\mathrm{d}y.
$$

This is the quoted relation, written with the normalization-bookkeeping convention that the doubled slice is assigned the *same elementary* prefactor $A(\delta t)$ — the residual ratio $A(\delta t)/A(2\delta t)$ is then absorbed into the redefined profile $F(\,\cdot\,;2\delta t)$, leaving exactly one power of $A(\delta t)$ outside the integral. The convention-independent content is the **convolution law**: *the convolution of two slice kernels of duration $\delta t$ is again a slice kernel, of duration $2\delta t$.* This is the self-consistency constraint that the closed-form $K_{\delta t}$ derived in §3.2.2 must satisfy. (For the free-particle answer $A(\delta t)\propto\delta t^{-1/2}$ found there, the explicit ratio is $A(\delta t)^{2}/A(2\delta t) = \sqrt{2}\,A(\delta t)$.)

**(b) Dimensional consistency.** From the one-step evolution $\psi(x,t+\delta t) = \int K_{\delta t}(x,x')\,\psi(x',t)\,\mathrm{d}x'$ and the 1D normalization $\int\vert\psi\vert^{2}\,\mathrm{d}x = 1$ (so $[\psi] = L^{-1/2}$), matching dimensions gives

$$
[K_{\delta t}]\cdot L \cdot L^{-1/2} = L^{-1/2},
$$

so $[K_{\delta t}] = L^{-1}$.

In the convolution equation, the right-hand side carries $[A]^{2}\,[F]^{2}\,L$ (the extra $L$ from $\mathrm{d}y$), the left-hand side $[A]\,[F]$. For the free particle $F = \exp[\mathrm{i}m u^{2}/(2\hbar\,\delta t)]$ is a pure phase, hence dimensionless; then $[A] = [K_{\delta t}] = L^{-1}$, and the equation reads $L^{-1} = L^{-2}\cdot L = L^{-1}$ — consistent. $\checkmark$

Dimensional analysis combined with the convolution law even fixes the *scaling* of $A$. The Fresnel convolution $\int F(\,\cdot\,;\delta t)F(\,\cdot\,;\delta t)\,\mathrm{d}y$ runs over a kernel of effective width $\sim\sqrt{\hbar\,\delta t/m}$, contributing a factor $\propto\delta t^{1/2}$. The constraint $A(2\delta t)\,F(\,\cdot\,;2\delta t) = A(\delta t)^{2}\,[\,\propto\delta t^{1/2}\,]\,F(\,\cdot\,;2\delta t)$ then requires $A(2\delta t)\propto A(\delta t)^{2}\,\delta t^{1/2}$. Trying $A(\delta t) = C\,\delta t^{-p}$ and matching powers of $\delta t$ gives $-p = -2p + \tfrac{1}{2}$, i.e. $p = \tfrac{1}{2}$:

$$
A(\delta t) \propto \delta t^{-1/2}.
$$

This anticipates the §3.2.2 result $A(\delta t) = \sqrt{m/(2\pi\mathrm{i}\hbar\,\delta t)}$ — the normalization the phase-action principle left undetermined is pinned down, up to a dimensionless constant, by composition plus dimensions alone.
