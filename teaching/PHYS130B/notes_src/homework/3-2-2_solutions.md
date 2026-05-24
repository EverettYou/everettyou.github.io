# 3.2.2 Schrödinger Equation
Worked solutions for the homework problems in the [3.2.2 Schrödinger Equation](../ch3_path-integral/3-2-2-schrodinger-equation) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Zeroth Gaussian moment.** Use the polar-coordinate trick to derive $\int\mathrm{e}^{-r^{2}}\mathrm{d}^{2}r = \pi$ in the plane.

(a) From this, derive $\int\mathrm{e}^{-bx^{2}}\,\mathrm{d}x = \sqrt{\pi/b}$ for $\operatorname{Re}b>0$ by separating the 2D integral and rescaling.

(b) Analytically continue $b\to-\mathrm{i}\alpha$ with $\alpha>0$ (rotate the contour by $\pi/4$ and check convergence) to obtain $M_{0} = \sqrt{\mathrm{i}\pi/\alpha}$.

**Solution.**

**The polar trick.** Consider the 2D integral over the whole plane,

$$
J = \int_{\mathbb{R}^{2}}\mathrm{e}^{-r^{2}}\,\mathrm{d}^{2}r = \int_{-\infty}^{\infty}\!\!\int_{-\infty}^{\infty}\mathrm{e}^{-(x^{2}+y^{2})}\,\mathrm{d}x\,\mathrm{d}y,
$$

where $r^{2} = x^{2}+y^{2}$. Switch to polar coordinates $(r,\theta)$ with area element $\mathrm{d}^{2}r = r\,\mathrm{d}r\,\mathrm{d}\theta$:

$$
J = \int_{0}^{2\pi}\mathrm{d}\theta\int_{0}^{\infty}\mathrm{e}^{-r^{2}}\,r\,\mathrm{d}r = 2\pi\left[-\tfrac{1}{2}\mathrm{e}^{-r^{2}}\right]_{0}^{\infty} = 2\pi\cdot\tfrac{1}{2} = \pi.
$$

The substitution $u = r^{2}$, $\mathrm{d}u = 2r\,\mathrm{d}r$ makes the radial integral elementary. Hence $\int\mathrm{e}^{-r^{2}}\mathrm{d}^{2}r = \pi$.

**(a) Reduction to 1D and rescaling.** Because the integrand factorizes, $\mathrm{e}^{-(x^{2}+y^{2})} = \mathrm{e}^{-x^{2}}\mathrm{e}^{-y^{2}}$, the 2D integral is the square of a single 1D integral:

$$
\pi = J = \left(\int_{-\infty}^{\infty}\mathrm{e}^{-x^{2}}\,\mathrm{d}x\right)^{2},
$$

so $\int_{-\infty}^{\infty}\mathrm{e}^{-x^{2}}\,\mathrm{d}x = \sqrt{\pi}$.

The positive root is correct since the integrand is positive. Now rescale: for $\operatorname{Re}b>0$ substitute $x = u/\sqrt{b}$ (principal branch of the root), so $\mathrm{d}x = \mathrm{d}u/\sqrt{b}$ and $bx^{2} = u^{2}$:

$$
\int_{-\infty}^{\infty}\mathrm{e}^{-bx^{2}}\,\mathrm{d}x = \frac{1}{\sqrt{b}}\int_{-\infty}^{\infty}\mathrm{e}^{-u^{2}}\,\mathrm{d}u = \sqrt{\frac{\pi}{b}}.
$$

The condition $\operatorname{Re}b>0$ guarantees the original integrand decays at infinity so the integral converges and the substitution is legitimate.

**(b) Analytic continuation to the oscillatory Gaussian.** We want $M_{0} = \int_{-\infty}^{\infty}\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}\,\mathrm{d}(\delta x)$ with $\alpha>0$, i.e. the formula above evaluated at $b = -\mathrm{i}\alpha$ (since $-bx^{2} = \mathrm{i}\alpha x^{2}$). This value of $b$ sits on the boundary $\operatorname{Re}b = 0$, so we must justify the continuation by an explicit contour rotation.

Treat $\delta x$ as complex and write $\delta x = \mathrm{e}^{\mathrm{i}\pi/4}u$ with $u$ real. Then

$$
\mathrm{i}\alpha(\delta x)^{2} = \mathrm{i}\alpha\,\mathrm{e}^{\mathrm{i}\pi/2}u^{2} = \mathrm{i}\alpha\cdot\mathrm{i}\,u^{2} = -\alpha u^{2},
$$

which is a convergent *real* Gaussian for $\alpha>0$. The integrand $\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}$ is entire, so by Cauchy's theorem the integral over the real axis equals the integral over the ray $\arg(\delta x) = \pi/4$, provided the connecting circular arcs at infinity contribute nothing. On an arc $\delta x = R\mathrm{e}^{\mathrm{i}\phi}$ the exponent has real part

$$
\operatorname{Re}\!\left[\mathrm{i}\alpha R^{2}\mathrm{e}^{2\mathrm{i}\phi}\right] = -\alpha R^{2}\sin(2\phi) \le 0
\quad\text{for } 0\le\phi\le\tfrac{\pi}{4},
$$

with strict decay in the interior, so the arc contribution vanishes as $R\to\infty$. Therefore

$$
M_{0} = \int_{-\infty}^{\infty}\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}\,\mathrm{d}(\delta x)
= \mathrm{e}^{\mathrm{i}\pi/4}\int_{-\infty}^{\infty}\mathrm{e}^{-\alpha u^{2}}\,\mathrm{d}u
= \mathrm{e}^{\mathrm{i}\pi/4}\sqrt{\frac{\pi}{\alpha}}.
$$

Since $\mathrm{e}^{\mathrm{i}\pi/4} = \sqrt{\mathrm{i}}$, this is exactly

$$
M_{0} = \sqrt{\frac{\mathrm{i}\pi}{\alpha}},
$$

in agreement with the naive substitution $\sqrt{\pi/(-\mathrm{i}\alpha)} = \sqrt{\mathrm{i}\pi/\alpha}$ (using $1/(-\mathrm{i}) = \mathrm{i}$). Substituting $\alpha = m/(2\hbar\,\delta t)$ gives the form used in the lecture, $M_{0} = \sqrt{2\pi\mathrm{i}\hbar\,\delta t/m}$.

<!-- ─── -->

**2. Second Gaussian moment.** Starting from $M_{0}(\alpha) = \sqrt{\mathrm{i}\pi/\alpha}$, use the derivative trick $\partial_{\alpha}M_{0} = \mathrm{i}M_{2}$ to compute $M_{2}$ and verify the result $M_{2} = (\mathrm{i}\hbar\,\delta t/m)\,M_{0}$ stated in $M_0 = \sqrt{2\pi\mathrm{i}\hbar\delta t/m},\; M_1=0,\;M_2 = (\mathrm{i}\hbar\delta t/m)\,M_0$.

**Solution.**

The moment $M_{0}(\alpha) = \int\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}\,\mathrm{d}(\delta x)$ depends on $\alpha$ only through the exponent. Differentiating under the integral sign brings down a factor $\mathrm{i}(\delta x)^{2}$:

$$
\frac{\partial M_{0}}{\partial\alpha}
= \int_{-\infty}^{\infty}\mathrm{i}(\delta x)^{2}\,\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}\,\mathrm{d}(\delta x)
= \mathrm{i}\int_{-\infty}^{\infty}(\delta x)^{2}\,\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}\,\mathrm{d}(\delta x)
= \mathrm{i}\,M_{2}.
$$

On the other hand, differentiating the closed form $M_{0} = \sqrt{\mathrm{i}\pi}\;\alpha^{-1/2}$ directly,

$$
\frac{\partial M_{0}}{\partial\alpha} = \sqrt{\mathrm{i}\pi}\left(-\tfrac{1}{2}\right)\alpha^{-3/2}
= -\frac{1}{2\alpha}\,\sqrt{\mathrm{i}\pi}\;\alpha^{-1/2}
= -\frac{1}{2\alpha}\,M_{0}.
$$

Equate the two expressions for $\partial_{\alpha}M_{0}$ and solve for $M_{2}$:

$$
\mathrm{i}\,M_{2} = -\frac{M_{0}}{2\alpha},
$$

so $M_{2} = -(1/\mathrm{i})\,M_{0}/(2\alpha) = \mathrm{i}\,M_{0}/(2\alpha)$,

using $-1/\mathrm{i} = \mathrm{i}$. Finally substitute the kinetic-phase coefficient $\alpha = m/(2\hbar\,\delta t)$, so that $1/(2\alpha) = \hbar\,\delta t/m$:

$$
M_{2} = \frac{\mathrm{i}}{2\alpha}\,M_{0} = \frac{\mathrm{i}\hbar\,\delta t}{m}\,M_{0},
$$

which is exactly the result quoted in $M_0 = \sqrt{2\pi\mathrm{i}\hbar\delta t/m},\; M_1=0,\;M_2 = (\mathrm{i}\hbar\delta t/m)\,M_0$. Note the physically important feature: $M_{2}/M_{0} = \mathrm{i}\hbar\,\delta t/m$ is *linear* in $\delta t$. After multiplication by the normalization $A = 1/M_{0}$, the second moment contributes a term of order $\delta t$ — exactly the order that survives to build the kinetic term of the Schrödinger equation.

<!-- ─── -->

**3. Verifying the slice normalization.** For the closed-form free slice propagator $K_{\delta t}^{\mathrm{free}}(x,x') = \sqrt{m/(2\pi\mathrm{i}\hbar\,\delta t)}\,\exp\!\bigl[\mathrm{i}\,m(x-x')^2/(2\hbar\delta t)\bigr]$, evaluate $\int K_{\delta t}^{\text{free}}(x,x')\,\mathrm{d}x'$ by Gaussian integration. Show that the result equals $1$, independent of $x$ and $\delta t$. What does this say about how a constant initial wavefunction evolves over one slice?

**Solution.**

The free slice propagator is

$$
K_{\delta t}^{\text{free}}(x,x') = \sqrt{\frac{m}{2\pi\mathrm{i}\hbar\,\delta t}}\;\exp\!\left[\frac{\mathrm{i}\,m\,(x-x')^{2}}{2\hbar\,\delta t}\right].
$$

Integrate over the source point $x'$. Substitute $u = x'-x$, so $\mathrm{d}x' = \mathrm{d}u$ and $(x-x')^{2} = u^{2}$. The kinetic exponent becomes $\mathrm{i}\alpha u^{2}$ with $\alpha = m/(2\hbar\,\delta t)$:

$$
\int_{-\infty}^{\infty}K_{\delta t}^{\text{free}}(x,x')\,\mathrm{d}x'
= \sqrt{\frac{m}{2\pi\mathrm{i}\hbar\,\delta t}}\int_{-\infty}^{\infty}\mathrm{e}^{\mathrm{i}\alpha u^{2}}\,\mathrm{d}u
= \sqrt{\frac{m}{2\pi\mathrm{i}\hbar\,\delta t}}\;M_{0}.
$$

The remaining integral is precisely the zeroth Gaussian moment from Problem 1,

$$
M_{0} = \sqrt{\frac{\mathrm{i}\pi}{\alpha}} = \sqrt{\frac{2\pi\mathrm{i}\hbar\,\delta t}{m}}.
$$

Multiplying the two square roots, the entire $\delta t$- and $m$-dependence cancels:

$$
\int_{-\infty}^{\infty}K_{\delta t}^{\text{free}}(x,x')\,\mathrm{d}x'
= \sqrt{\frac{m}{2\pi\mathrm{i}\hbar\,\delta t}}\cdot\sqrt{\frac{2\pi\mathrm{i}\hbar\,\delta t}{m}}
= 1.
$$

The result is $1$ for every $x$ and every $\delta t$ — the integral does not depend on either.

**Physical interpretation.** Consider a spatially uniform initial wavefunction $\psi(x',t) = c$ (a constant). One slice later,

$$
\psi(x,t+\delta t) = \int_{-\infty}^{\infty}K_{\delta t}^{\text{free}}(x,x')\,\psi(x',t)\,\mathrm{d}x'
= c\int_{-\infty}^{\infty}K_{\delta t}^{\text{free}}(x,x')\,\mathrm{d}x' = c.
$$

A constant wavefunction is left exactly unchanged by the free slice propagator, for any slice duration. This is precisely the self-consistency condition $A(\delta t)\,M_{0} = 1$ that was used in the lecture to *fix* the normalization $A(\delta t) = 1/M_{0}$. The condition was imposed only in the limit $\delta t\to 0$ to fix one constant; this computation shows it actually holds at finite $\delta t$ as well. Consistency check against the free Schrödinger equation $\mathrm{i}\hbar\,\partial_{t}\psi = -(\hbar^{2}/2m)\,\partial_{x}^{2}\psi$: a constant $\psi$ has $\partial_{x}^{2}\psi = 0$, hence $\partial_{t}\psi = 0$ — a uniform wave is stationary, exactly as the slice integral confirms.

<!-- ─── -->

**4. Slice propagator approaches a delta function.** As the slice duration $\delta t \to 0$, the slice propagator $K_{\delta t}^{\mathrm{free}}(x, x')$ should reduce to the identity: $\psi(x, t + \delta t) \to \psi(x, t)$. Make this precise.

(a) Show that $\int_{-\infty}^{\infty} K_{\delta t}^{\mathrm{free}}(x, x')\, f(x')\, \mathrm{d}x' \to f(x)$ as $\delta t \to 0$ for any smooth, bounded test function $f$.

(b) Compute $\int_{-\infty}^{\infty} K_{\delta t}^{\mathrm{free}}(x, x')\, x'\, \mathrm{d}x'$ exactly. Show it equals $x$ — the slice propagator preserves the mean position.

(c) Compute $\int_{-\infty}^{\infty} K_{\delta t}^{\mathrm{free}}(x, x')\, x'^{2}\, \mathrm{d}x'$. Show that it equals $x^{2} + \mathrm{i}\hbar\,\delta t/m$ — a *complex* number, signalling that the slice propagator is a *phase-distribution* kernel rather than a probability distribution. Interpret physically.

**Solution.**

(a) The free slice propagator is

$$
K_{\delta t}^{\mathrm{free}}(x, x') = \sqrt{\frac{m}{2\pi\mathrm{i}\hbar\,\delta t}}\,\exp\!\left[\frac{\mathrm{i}m(x-x')^{2}}{2\hbar\,\delta t}\right].
$$

Substitute $u = x - x'$. The exponent's coefficient is $\alpha = m/(2\hbar\,\delta t)$, which diverges as $\delta t \to 0$. Writing the kernel as $K = \sqrt{\alpha/(\mathrm{i}\pi)}\,\mathrm{e}^{\mathrm{i}\alpha u^{2}}$, this is a Fresnel-Gaussian peak: the oscillations become arbitrarily rapid as $\alpha \to \infty$, and only the immediate neighborhood $\vert u\vert \lesssim 1/\sqrt\alpha = \sqrt{\hbar\,\delta t/m}$ contributes coherently to the integral. The width of the coherent region shrinks as $\sqrt{\delta t} \to 0$, while Problem 3 showed the normalization stays $1$. These are the defining properties of a delta function:

$$
\int K_{\delta t}^{\mathrm{free}}(x, x') f(x')\,\mathrm{d}x' \xrightarrow{\delta t \to 0} f(x).
$$

Explicit verification by Taylor-expanding $f$: with $f(x') = f(x - u) = \sum_n \frac{(-u)^n}{n!} \partial_x^n f(x)$, the moment expansion (from Problem 6) gives $\sum_k \frac{A M_{2k}}{(2k)!}\partial_x^{2k}f(x)$. As $\delta t \to 0$, only the $k=0$ term ($A M_0 = 1$) survives; every higher $k$ vanishes as $O(\delta t^k)$. So the integral collapses to $f(x)$.

(b) Compute the first moment using $u = x - x'$, so $x' = x - u$:

$$
\int K_{\delta t}^{\mathrm{free}}(x, x')\, x'\, \mathrm{d}x' = \int K(x, x - u)\,(x - u)\,\mathrm{d}u = x\int K\,\mathrm{d}u - \int K\,u\,\mathrm{d}u.
$$

The first integral is $x \cdot A\,M_0 = x \cdot 1 = x$ (Problem 3). The second integral has integrand $u\,\mathrm{e}^{\mathrm{i}\alpha u^2}$ which is odd in $u$, so it vanishes: $A\,M_1 = 0$. Therefore

$$
\int K_{\delta t}^{\mathrm{free}}(x, x')\, x'\, \mathrm{d}x' = x. \quad\checkmark
$$

The slice propagator preserves the mean position — consistent with a free particle (no force, no drift).

(c) Same substitution:

$$
\int K\,x'^{2}\,\mathrm{d}x' = \int K(x-u)^{2}\,\mathrm{d}u = \int K\,(x^{2} - 2xu + u^{2})\,\mathrm{d}u = x^{2} \cdot 1 - 2x\cdot 0 + A\,M_{2}.
$$

From Problem 2, $A\,M_{2} = M_{2}/M_{0} = \mathrm{i}\hbar\,\delta t/m$. Hence

$$
\int K_{\delta t}^{\mathrm{free}}(x, x')\, x'^{2}\, \mathrm{d}x' = x^{2} + \frac{\mathrm{i}\hbar\,\delta t}{m}. \quad\checkmark
$$

This is a *complex* number. A genuine probability distribution always has a *real* mean and a *real* (non-negative) variance, so the slice kernel cannot be a probability distribution — it is the *amplitude* kernel that defines the propagation of wavefunctions, not the diffusion kernel of a stochastic process.

**Physical interpretation.** The imaginary $\mathrm{i}\hbar\,\delta t/m$ in the second moment is the seed of the Schrödinger equation's kinetic term. Compared with a real diffusion kernel — where $\langle (\Delta x)^{2}\rangle = 2D\,\delta t$ generates the heat equation $\partial_{t}\rho = D\,\partial_{x}^{2}\rho$ — the substitution $D \to \mathrm{i}\hbar/(2m)$ converts the heat equation into the free-particle Schrödinger equation $\mathrm{i}\hbar\,\partial_{t}\psi = -(\hbar^{2}/2m)\,\partial_{x}^{2}\psi$. **Quantum evolution is "imaginary-time" diffusion.** The factor of $\mathrm{i}$ is not cosmetic: it flips real exponential decay (broadening of a heat distribution) into pure phase rotation (oscillations of a wavefunction at fixed amplitude), which is why $\vert\psi\vert^{2}$ stays normalized while a heat distribution spreads. The imaginary-time substitution $t \to -\mathrm{i}\tau$ would convert Schrödinger evolution to diffusion and vice versa, and this duality underlies many computational techniques (imaginary-time path integral, ground-state Monte Carlo, etc.) that map quantum problems to statistical ones.

<!-- ─── -->

**5. Probability conservation.** Starting from $\mathrm{i}\hbar\,\partial_t\psi = \hat{H}\psi,\quad\hat{H} = -(\hbar^2/2m)\partial_x^2 + V(x)$ with real $V(x)$, derive the continuity equation $\partial_{t}\rho + \partial_{x}j = 0$ with $\rho = \vert\psi\vert^{2}$ and $j = (\hbar/m)\operatorname{Im}(\psi^{*}\partial_{x}\psi)$.

(a) Compute $\partial_{t}\vert\psi\vert^{2}$ using the Schrödinger equation and its complex conjugate.

(b) Identify the probability current $j$ and verify $\partial_{t}\rho + \partial_{x}j = 0$.

(c) Integrate over all $x$, assuming $\psi\to 0$ at infinity, to conclude that $\frac{\mathrm{d}}{\mathrm{d}t}\int\vert\psi\vert^{2}\,\mathrm{d}x = 0$.

**Solution.**

The Schrödinger equation and its complex conjugate (with $V(x)$ real, so $V^{*} = V$) are

$$
\mathrm{i}\hbar\,\partial_{t}\psi = -\frac{\hbar^{2}}{2m}\,\partial_{x}^{2}\psi + V\psi,
\qquad
-\mathrm{i}\hbar\,\partial_{t}\psi^{*} = -\frac{\hbar^{2}}{2m}\,\partial_{x}^{2}\psi^{*} + V\psi^{*}.
$$

Solve each for the time derivative:

$$
\partial_{t}\psi = \frac{\mathrm{i}\hbar}{2m}\,\partial_{x}^{2}\psi - \frac{\mathrm{i}}{\hbar}\,V\psi,
\qquad
\partial_{t}\psi^{*} = -\frac{\mathrm{i}\hbar}{2m}\,\partial_{x}^{2}\psi^{*} + \frac{\mathrm{i}}{\hbar}\,V\psi^{*}.
$$

**(a) Time derivative of the density.** With $\rho = \vert\psi\vert^{2} = \psi^{*}\psi$, the product rule gives

$$
\partial_{t}\rho = \psi^{*}\,\partial_{t}\psi + \psi\,\partial_{t}\psi^{*}.
$$

Substitute the two expressions above:

$$
\begin{split}
\partial_{t}\rho &= \psi^{*}\!\left(\frac{\mathrm{i}\hbar}{2m}\,\partial_{x}^{2}\psi - \frac{\mathrm{i}}{\hbar}V\psi\right)
+ \psi\!\left(-\frac{\mathrm{i}\hbar}{2m}\,\partial_{x}^{2}\psi^{*} + \frac{\mathrm{i}}{\hbar}V\psi^{*}\right)\\
&= \frac{\mathrm{i}\hbar}{2m}\left(\psi^{*}\,\partial_{x}^{2}\psi - \psi\,\partial_{x}^{2}\psi^{*}\right)
- \frac{\mathrm{i}}{\hbar}V\,\psi^{*}\psi + \frac{\mathrm{i}}{\hbar}V\,\psi\psi^{*}.
\end{split}
$$

The two potential terms are equal and opposite — they cancel exactly. This cancellation is *why $V$ must be real*: a real potential contributes no source or sink of probability. Hence

$$
\partial_{t}\rho = \frac{\mathrm{i}\hbar}{2m}\left(\psi^{*}\,\partial_{x}^{2}\psi - \psi\,\partial_{x}^{2}\psi^{*}\right).
$$

**(b) The probability current.** The bracket is a total spatial derivative. Indeed,

$$
\partial_{x}\!\left(\psi^{*}\,\partial_{x}\psi - \psi\,\partial_{x}\psi^{*}\right)
= \underbrace{\partial_{x}\psi^{*}\,\partial_{x}\psi + \psi^{*}\,\partial_{x}^{2}\psi}_{\partial_{x}(\psi^{*}\partial_{x}\psi)}
- \underbrace{\partial_{x}\psi\,\partial_{x}\psi^{*} - \psi\,\partial_{x}^{2}\psi^{*}}_{\partial_{x}(\psi\partial_{x}\psi^{*})}
= \psi^{*}\,\partial_{x}^{2}\psi - \psi\,\partial_{x}^{2}\psi^{*},
$$

since the cross terms $\partial_{x}\psi^{*}\,\partial_{x}\psi$ cancel. Therefore

$$
\partial_{t}\rho = \frac{\mathrm{i}\hbar}{2m}\,\partial_{x}\!\left(\psi^{*}\,\partial_{x}\psi - \psi\,\partial_{x}\psi^{*}\right)
= -\,\partial_{x}\!\left[\,\frac{\mathrm{i}\hbar}{2m}\!\left(\psi\,\partial_{x}\psi^{*} - \psi^{*}\,\partial_{x}\psi\right)\right].
$$

Define the probability current as the quantity inside the spatial derivative,

$$
j \;\equiv\; -\frac{\mathrm{i}\hbar}{2m}\left(\psi^{*}\,\partial_{x}\psi - \psi\,\partial_{x}\psi^{*}\right),
$$

so that $\partial_{t}\rho = -\partial_{x}j$, i.e. the continuity equation

$$
\partial_{t}\rho + \partial_{x}j = 0.
$$

To bring $j$ to the stated form, note that $\psi\,\partial_{x}\psi^{*} = (\psi^{*}\,\partial_{x}\psi)^{*}$, so the bracket is a number minus its own complex conjugate:

$$
\psi^{*}\,\partial_{x}\psi - \psi\,\partial_{x}\psi^{*}
= \psi^{*}\,\partial_{x}\psi - (\psi^{*}\,\partial_{x}\psi)^{*}
= 2\mathrm{i}\,\operatorname{Im}\!\left(\psi^{*}\,\partial_{x}\psi\right).
$$

Hence

$$
j = -\frac{\mathrm{i}\hbar}{2m}\cdot 2\mathrm{i}\,\operatorname{Im}\!\left(\psi^{*}\,\partial_{x}\psi\right)
= \frac{\hbar}{m}\,\operatorname{Im}\!\left(\psi^{*}\,\partial_{x}\psi\right),
$$

exactly as stated.

**(c) Global conservation.** Integrate the continuity equation over all space and exchange the order of $\partial_{t}$ and $\int\mathrm{d}x$:

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int_{-\infty}^{\infty}\vert\psi\vert^{2}\,\mathrm{d}x
= \int_{-\infty}^{\infty}\partial_{t}\rho\,\mathrm{d}x
= -\int_{-\infty}^{\infty}\partial_{x}j\,\mathrm{d}x
= -\,\bigl[\,j(x,t)\,\bigr]_{x=-\infty}^{x=+\infty}.
$$

For a normalizable state $\psi\to 0$ as $x\to\pm\infty$ (and its derivative is bounded), so the current $j = (\hbar/m)\operatorname{Im}(\psi^{*}\partial_{x}\psi)$ vanishes at both endpoints. Therefore

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int_{-\infty}^{\infty}\vert\psi\vert^{2}\,\mathrm{d}x = 0.
$$

The total probability is constant in time: if $\psi$ is normalized once, it stays normalized under Schrödinger evolution. Probability is locally conserved (continuity equation) and globally conserved (constant norm) — this is the statement that Schrödinger time evolution is unitary.

<!-- ─── -->

**6. Higher moments do not matter.** The Taylor expansion $\psi(x-\delta x,t) = \psi(x,t) - \delta x\,\partial_x\psi + \tfrac{1}{2}(\delta x)^2\partial_x^2\psi + O((\delta x)^3)$ produces moments $M_{n}$ for $n = 0, 1, 2, 3, 4, \ldots$.

(a) Use the derivative trick repeatedly to show that $M_{2k} = c_{k}\,M_{0}\,\alpha^{-k}$ for some dimensionless constants $c_{k}$.

(b) Substituting $\alpha = m/(2\hbar\,\delta t)$, conclude that $A\,M_{2k} = O(\delta t^{\,k})$. Why does the small-$\delta t$ limit therefore truncate exactly at the second moment?

**Solution.**

**(a) All even moments from repeated differentiation.** Each $\alpha$-derivative of a moment lowers an extra $(\delta x)^{2}$ from the exponent:

$$
\partial_{\alpha}M_{n} = \int\mathrm{i}(\delta x)^{2}\,(\delta x)^{n}\,\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}\,\mathrm{d}(\delta x) = \mathrm{i}\,M_{n+2}.
$$

Applying this $k$ times starting from $M_{0}$,

$$
M_{2k} = \frac{1}{\mathrm{i}^{k}}\,\partial_{\alpha}^{k}M_{0}.
$$

(Odd moments need not be tracked: $M_{2k+1} = 0$ by parity, since the integrand $(\delta x)^{2k+1}\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}$ is odd.) With $M_{0} = \sqrt{\mathrm{i}\pi}\;\alpha^{-1/2}$, the repeated power-rule derivative is

$$
\partial_{\alpha}^{k}\,\alpha^{-1/2}
= \left(-\tfrac{1}{2}\right)\!\left(-\tfrac{3}{2}\right)\cdots\!\left(-\tfrac{2k-1}{2}\right)\alpha^{-1/2-k}
= (-1)^{k}\,\frac{(2k-1)!!}{2^{k}}\;\alpha^{-1/2-k},
$$

where $(2k-1)!! = 1\cdot 3\cdot 5\cdots(2k-1)$ and $(-1)!! \equiv 1$. Hence

$$
\partial_{\alpha}^{k}M_{0} = (-1)^{k}\,\frac{(2k-1)!!}{2^{k}}\;M_{0}\,\alpha^{-k},
$$

and therefore

$$
M_{2k} = \frac{1}{\mathrm{i}^{k}}\,(-1)^{k}\,\frac{(2k-1)!!}{2^{k}}\;M_{0}\,\alpha^{-k}
= \left(\frac{-1}{\mathrm{i}}\right)^{\!k}\frac{(2k-1)!!}{2^{k}}\;M_{0}\,\alpha^{-k}.
$$

Using $-1/\mathrm{i} = \mathrm{i}$, this is

$$
\boxed{\;M_{2k} = c_{k}\,M_{0}\,\alpha^{-k},\qquad
c_{k} = \left(\frac{\mathrm{i}}{2}\right)^{\!k}(2k-1)!!\;}
$$

The constants $c_{k}$ are pure numbers — dimensionless — independent of $m$, $\hbar$, $\delta t$. Check: $c_{0} = 1$ (so $M_{0} = M_{0}$); $c_{1} = \mathrm{i}/2$, reproducing $M_{2} = (\mathrm{i}/2\alpha)M_{0}$ from Problem 2; $c_{2} = (\mathrm{i}/2)^{2}\cdot 3 = -3/4$.

**(b) The order in $\delta t$ and the exact truncation.** The kinetic-phase coefficient is $\alpha = m/(2\hbar\,\delta t)$, so

$$
\alpha^{-k} = \left(\frac{2\hbar\,\delta t}{m}\right)^{\!k} = \left(\frac{2\hbar}{m}\right)^{\!k}\delta t^{\,k}.
$$

Each inverse power of $\alpha$ carries one power of $\delta t$. The normalization fixed in the lecture is $A = 1/M_{0}$, so

$$
A\,M_{2k} = \frac{M_{2k}}{M_{0}} = c_{k}\,\alpha^{-k} = c_{k}\left(\frac{2\hbar}{m}\right)^{\!k}\delta t^{\,k} = O(\delta t^{\,k}).
$$

The factor $M_{0}$ — the only piece with awkward $\delta t$-dependence — cancels against $A$, leaving a clean power $\delta t^{k}$.

Now recall the moment expansion of one slice. Taylor-expanding the source wave $\psi(x-\delta x,t) = \psi(x,t) - \delta x\,\partial_x\psi + \tfrac{1}{2}(\delta x)^2\partial_x^2\psi + O((\delta x)^3)$ and integrating term by term gives

$$
\psi(x,t+\delta t) = A\sum_{n\ge 0}\frac{(-1)^{n}}{n!}\,M_{n}\,\partial_{x}^{n}\psi(x,t)
= \sum_{k\ge 0}\frac{A\,M_{2k}}{(2k)!}\,\partial_{x}^{2k}\psi(x,t),
$$

where odd terms dropped out ($M_{2k+1}=0$). Substituting $A\,M_{2k} = O(\delta t^{k})$, the $k$-th term is $O(\delta t^{k})\,\partial_{x}^{2k}\psi$. To extract the Schrödinger equation we form

$$
\partial_{t}\psi = \lim_{\delta t\to 0}\frac{\psi(x,t+\delta t) - \psi(x,t)}{\delta t}.
$$

Examine each $k$:

- **$k=0$:** the term is $A\,M_{0}\,\psi = \psi$, which cancels the $-\psi(x,t)$ in the numerator. It contributes nothing to the difference.
- **$k=1$:** the term is $O(\delta t^{1})$; divided by $\delta t$ it gives a *finite, nonzero* limit — this is the kinetic term $\tfrac{\mathrm{i}\hbar}{2m}\partial_{x}^{2}\psi$.
- **$k\ge 2$:** the term is $O(\delta t^{k})$ with $k\ge 2$; divided by $\delta t$ it is $O(\delta t^{\,k-1})\to 0$.

So in the limit $\delta t\to 0$ only $k=0$ (trivial) and $k=1$ (the second moment $M_{2}$) survive; every higher even moment is suppressed by at least one extra power of $\delta t$ and vanishes. The expansion truncates *exactly* at the second moment — not approximately. This is the deep reason the Schrödinger equation is first order in $\partial_{t}$ and exactly second order in $\partial_{x}$: the slice kernel's Gaussian width scales as $\delta x\sim\alpha^{-1/2}\sim\sqrt{\delta t}$, so the $2k$-th moment scales as $(\delta x)^{2k}\sim\delta t^{k}$, and only $k=1$ matches the single power of $\delta t$ removed by the time derivative.

<!-- ─── -->

**7. Phase-space spreading: loss of minimum uncertainty.** A free particle starts in the minimum-uncertainty Gaussian state $\psi(x, 0) = (\pi\sigma^{2})^{-1/4}\exp(-x^{2}/(2\sigma^{2}))$, for which $\sigma_{x}(0)\,\sigma_{p}(0) = \hbar/2$ exactly.

(a) Compute $\sigma_{x}(t)$ from the propagator (or quote the result of HW 3.2.1.1).

(b) Argue from momentum conservation that $\sigma_{p}(t) = \sigma_{p}(0) = \hbar/(2\sigma)$ for all $t > 0$.

(c) Combine (a) and (b) to show

$$
\sigma_{x}(t)\,\sigma_{p}(t) = \frac{\hbar}{2}\sqrt{1 + (t/\tau)^{2}}, \qquad \tau = \frac{m\sigma^{2}}{\hbar}.
$$

The product grows monotonically with time: the state begins at minimum uncertainty and *loses* this status under free evolution.

(d) Identify the physical reason. The free Hamiltonian $\hat H = \hat p^{2}/(2m)$ is a function of $\hat p$ alone, so it commutes with $\hat p$ but not with $\hat{x}$. Use this to explain why $\sigma_{p}$ is preserved while $\sigma_{x}$ is not. Comment on what initial state would *maintain* minimum uncertainty under free evolution (hint: there isn't one — minimum-uncertainty states are not stable under free flight).

**Solution.**

(a) From HW 3.2.1.1, the free Gaussian wavepacket has

$$
\sigma_{x}(t) = \sigma\sqrt{1 + (t/\tau)^{2}}, \qquad \tau = \frac{m\sigma^{2}}{\hbar}.
$$

(b) The free Hamiltonian $\hat H = \hat p^{2}/(2m)$ is a function of $\hat p$, so $[\hat H, \hat p] = 0$. By 1.3.1 Problem 1 (conservation theorem for observables commuting with $\hat H$), all moments of $\hat p$ are time-independent:

$$
\langle\hat p\rangle(t) = \langle\hat p\rangle(0), \qquad \langle\hat p^{2}\rangle(t) = \langle\hat p^{2}\rangle(0).
$$

Therefore $\sigma_{p}(t) = \sigma_{p}(0)$. For the initial Gaussian, the Fourier transform is also Gaussian, with width $\sigma_{p}(0) = \hbar/(2\sigma)$ — saturating the Heisenberg bound at $t = 0$.

(c) Combine the two results:

$$
\sigma_{x}(t)\,\sigma_{p}(t) = \sigma\sqrt{1 + (t/\tau)^{2}}\cdot\frac{\hbar}{2\sigma} = \frac{\hbar}{2}\sqrt{1 + (t/\tau)^{2}}.
$$

At $t = 0$: $\sigma_{x}\sigma_{p} = \hbar/2$, the **minimum uncertainty**. For $t > 0$ the square root exceeds $1$ and the product strictly grows. For $t \gg \tau$ the product grows linearly with $t$, signalling unbounded loss of phase-space locality.

(d) **Why $\sigma_{p}$ is conserved.** Momentum is a constant of free motion: $\hat p$ generates translations, and a translationally-invariant Hamiltonian (no $\hat{x}$ dependence) preserves $\hat p$. So the momentum distribution is frozen.

**Why $\sigma_{x}$ grows.** Different momentum components travel at different velocities $v = p/m$. A wavepacket that started narrowly localized in $x$ contained a wide spread of momenta (Heisenberg), and those momenta carry their portions of the wavefunction apart. The position uncertainty therefore grows; the rate is set by the velocity spread $\sigma_{p}/m = \hbar/(2m\sigma)$, giving the linear-in-$t$ growth $\sigma_{x}(t \gg \tau) \approx \sigma_{p}t/m$.

**No minimum-uncertainty steady state.** A stationary minimum-uncertainty state would require both $\sigma_{x}$ and $\sigma_{p}$ to be time-independent. For a free particle this is impossible: $\sigma_{p}$ is fixed by initial conditions, but the position spread *must* grow because of the velocity dispersion just argued. The minimum-uncertainty Gaussian is a fleeting initial condition, not a steady state.

The situation is qualitatively different for the harmonic oscillator (2.1.3 P3): there, coherent states maintain minimum uncertainty *forever*, because the oscillator periodically refocuses what free flight would spread. The harmonic restoring force is precisely what keeps the wavepacket gathered — a free particle has no such mechanism, and minimum-uncertainty is irreversibly lost.

This is the operator-level statement that under any non-trivial unitary evolution, the *phase-space volume* explored by an initially localized state can only grow, never shrink. Quantum free flight is one explicit, exactly-solvable example.

<!-- ─── -->

**8. Potential placement freedom.** Repeat the derivation of the full Schrödinger equation, but evaluate the slice potential at the source point $x' = x - \delta x$ instead of the endpoint $x$.

(a) Show that the additional slice phase becomes $\exp[-\mathrm{i}V(x-\delta x)\,\delta t/\hbar]$.

(b) Expand $V(x-\delta x) = V(x) - \delta x\,V'(x) + O((\delta x)^{2})$ and use the Gaussian moments to show that the difference relative to evaluating $V$ at $x$ contributes only at $O(\delta t^{\,2})$.

(c) Conclude that the Schrödinger equation is independent of where $V$ is sampled within the slice, and explain in one sentence why this freedom matches the analogous freedom for the slice action (HW 3.2.1.4).

**Solution.**

**(a) The slice phase with $V$ at the source.** For the Lagrangian $L = \tfrac{1}{2}m\dot x^{2} - V(x)$, the slice action over a step of duration $\delta t$ is the kinetic part plus a potential contribution $-V\,\delta t$, where $V$ is evaluated at *some* point of the slice. If we choose the source point $x' = x-\delta x$ rather than the endpoint $x$, the potential contributes action $\Delta S_{V} = -V(x-\delta x)\,\delta t$. By the path-integral rule, action enters the amplitude as a phase $\mathrm{e}^{\mathrm{i}\Delta S/\hbar}$, so the slice propagator picks up the extra factor

$$
\exp\!\left[\frac{\mathrm{i}\,\Delta S_{V}}{\hbar}\right]
= \exp\!\left[-\frac{\mathrm{i}\,V(x-\delta x)\,\delta t}{\hbar}\right],
$$

multiplying the free kinetic kernel $K_{\delta t}^{\text{free}}$. This is the analogue of $K_{\delta t}(x,x') = K_{\delta t}^{\mathrm{free}}(x,x')\,\exp[-\mathrm{i}V(x)\delta t/\hbar]$ with $V(x)\to V(x-\delta x)$.

**(b) The difference is $O(\delta t^{2})$.** Because the slice integral always carries one explicit $\delta t$ in the potential phase, expand it to first order:

$$
\exp\!\left[-\frac{\mathrm{i}V(x-\delta x)\,\delta t}{\hbar}\right]
= 1 - \frac{\mathrm{i}\,\delta t}{\hbar}\,V(x-\delta x) + O(\delta t^{2}).
$$

Taylor-expand the potential about the endpoint $x$:

$$
V(x-\delta x) = V(x) - \delta x\,V'(x) + \tfrac{1}{2}(\delta x)^{2}V''(x) + O((\delta x)^{3}).
$$

The difference between sampling $V$ at the source and at the endpoint is therefore, inside the slice integral,

$$
\Delta\bigl[\text{phase}\bigr] = -\frac{\mathrm{i}\,\delta t}{\hbar}\Bigl[\,-\delta x\,V'(x) + \tfrac{1}{2}(\delta x)^{2}V''(x)\,\Bigr] + O(\delta t^{2}).
$$

This correction multiplies $\psi_{\text{kin}}$ and must be integrated against the kinetic Gaussian, $\psi(x,t+\delta t)\supset A\!\int\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}\,\Delta[\text{phase}]\,\psi(x-\delta x,t)\,\mathrm{d}(\delta x)$. Take the two pieces in turn, using $\psi(x-\delta x)\approx\psi(x) - \delta x\,\partial_{x}\psi + \cdots$ and the moment values $A\,M_{0} = 1$, $M_{1}=0$, $A\,M_{2} = O(\delta t)$:

*Linear piece* $\propto\delta x\,V'(x)$. The leading term pairs $\delta x$ with $\psi(x)$, giving a factor $A\,M_{1} = 0$ by parity. The first nonzero term pairs $\delta x$ with the $-\delta x\,\partial_{x}\psi$ piece of the Taylor expansion of $\psi$, producing $\int(\delta x)^{2}\mathrm{e}^{\mathrm{i}\alpha(\delta x)^{2}}\mathrm{d}(\delta x) = M_{2}$. Its contribution is

$$
\frac{\mathrm{i}\,\delta t}{\hbar}\,V'(x)\,\bigl(-\partial_{x}\psi\bigr)\,A\,M_{2}
= \underbrace{\frac{\mathrm{i}\,\delta t}{\hbar}}_{O(\delta t)}\times\underbrace{A\,M_{2}}_{O(\delta t)} \times(\cdots) = O(\delta t^{2}).
$$

*Quadratic piece* $\propto(\delta x)^{2}V''(x)$. The leading term pairs $(\delta x)^{2}$ with $\psi(x)$, giving $A\,M_{2} = O(\delta t)$:

$$
-\frac{\mathrm{i}\,\delta t}{\hbar}\cdot\tfrac{1}{2}V''(x)\,\psi(x)\,A\,M_{2}
= \underbrace{\frac{\mathrm{i}\,\delta t}{\hbar}}_{O(\delta t)}\times\underbrace{A\,M_{2}}_{O(\delta t)}\times(\cdots) = O(\delta t^{2}).
$$

In both cases the explicit $\delta t$ from the potential phase multiplies a quantity that is itself at least $O(\delta t)$ — because every surviving even moment obeys $A\,M_{2k} = O(\delta t^{k})$ and the odd moment $M_{1}$ vanishes. Hence the *entire* difference between evaluating $V$ at $x-\delta x$ and at $x$ is

$$
\psi^{(x')}(x,t+\delta t) - \psi^{(x)}(x,t+\delta t) = O(\delta t^{2}).
$$

**(c) Conclusion.** The Schrödinger equation is built from the $O(\delta t)$ part of the slice evolution: one divides $\psi(x,t+\delta t)-\psi(x,t)$ by $\delta t$ and lets $\delta t\to 0$. Any difference that enters only at $O(\delta t^{2})$ becomes $O(\delta t)$ after the division and vanishes in the limit. Since sampling $V$ at the source point instead of the endpoint changes the result only at $O(\delta t^{2})$ — and the same estimate covers the midpoint or any interior point — the resulting equation

$$
\mathrm{i}\hbar\,\partial_{t}\psi = -\frac{\hbar^{2}}{2m}\,\partial_{x}^{2}\psi + V(x)\,\psi
$$

is identical regardless of where $V$ is sampled within the slice. This matches the freedom found for the slice action in HW 3.2.1.4: the coherent paths have displacements only of order $\delta x\sim\sqrt{\hbar\,\delta t/m}$, so across one slice $V$ is effectively constant and the choice of reference point shifts the slice action by merely $O(\delta t^{2})$ — negligible in the continuum limit.
