# 5.2.2 Dyson Series
Worked solutions for the homework problems in the [5.2.2 Dyson Series](../ch5_perturbation-theory/5-2-2-dyson-series) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Volterra integral form.** Verify directly that the Volterra integral equation $\hat{U}_{\mathcal{I}}(t)=\hat{I}-(\mathrm{i}/\hbar)\int_0^t\mathrm{d}t'\,\hat{V}_{\mathcal{I}}(t')\hat{U}_{\mathcal{I}}(t')$ for $\hat{U}_{\mathcal{I}}(t)$ is equivalent to the IP operator EOM $\mathrm{i}\hbar\,\partial_t\hat{U}_{\mathcal{I}}(t)=\hat{V}_{\mathcal{I}}(t)\hat{U}_{\mathcal{I}}(t),\;\hat{U}_{\mathcal{I}}(0)=\hat{I}$ together with the initial condition $\hat{U}_{\mathcal{I}}(0)=\hat{I}$, by differentiating both sides.

**Solution.**

The two statements to be shown equivalent are the Volterra equation

$$
\hat{U}_{\mathcal{I}}(t)=\hat{I}-\frac{\mathrm{i}}{\hbar}\int_0^t\mathrm{d}t'\,\hat{V}_{\mathcal{I}}(t')\,\hat{U}_{\mathcal{I}}(t')
$$

and the operator EOM with initial condition

$$
\mathrm{i}\hbar\,\partial_t\hat{U}_{\mathcal{I}}(t)=\hat{V}_{\mathcal{I}}(t)\,\hat{U}_{\mathcal{I}}(t),
\qquad \hat{U}_{\mathcal{I}}(0)=\hat{I}.
$$

We prove equivalence in both directions.

**Volterra $\Rightarrow$ EOM $+$ initial condition.** Set $t=0$ in the Volterra
equation. The integral $\int_0^0$ has a vanishing domain, so it is the zero
operator, leaving

$$
\hat{U}_{\mathcal{I}}(0)=\hat{I}.
$$

The initial condition is therefore *built into* the Volterra form. Next
differentiate with respect to the upper limit $t$. The constant $\hat{I}$ drops,
and by the fundamental theorem of calculus
$\partial_t\int_0^t\mathrm{d}t'\,f(t')=f(t)$ applied to the integrand
$f(t')=\hat{V}_{\mathcal{I}}(t')\hat{U}_{\mathcal{I}}(t')$:

$$
\partial_t\hat{U}_{\mathcal{I}}(t)=-\frac{\mathrm{i}}{\hbar}\,\hat{V}_{\mathcal{I}}(t)\,\hat{U}_{\mathcal{I}}(t).
$$

Multiplying through by $\mathrm{i}\hbar$ gives
$\mathrm{i}\hbar\,\partial_t\hat{U}_{\mathcal{I}}=\hat{V}_{\mathcal{I}}\hat{U}_{\mathcal{I}}$,
which is the operator EOM.

**EOM $+$ initial condition $\Rightarrow$ Volterra.** Conversely, take the EOM
in the form
$\mathrm{i}\hbar\,\partial_{t'}\hat{U}_{\mathcal{I}}(t')=\hat{V}_{\mathcal{I}}(t')\hat{U}_{\mathcal{I}}(t')$
and integrate both sides over $t'$ from $0$ to $t$. The left side is an exact
differential:

$$
\int_0^t\mathrm{d}t'\,\mathrm{i}\hbar\,\partial_{t'}\hat{U}_{\mathcal{I}}(t')
=\mathrm{i}\hbar\bigl(\hat{U}_{\mathcal{I}}(t)-\hat{U}_{\mathcal{I}}(0)\bigr)
=\int_0^t\mathrm{d}t'\,\hat{V}_{\mathcal{I}}(t')\,\hat{U}_{\mathcal{I}}(t').
$$

Insert $\hat{U}_{\mathcal{I}}(0)=\hat{I}$ and divide by $\mathrm{i}\hbar$ (using
$1/\mathrm{i}=-\mathrm{i}$):

$$
\hat{U}_{\mathcal{I}}(t)=\hat{I}-\frac{\mathrm{i}}{\hbar}\int_0^t\mathrm{d}t'\,\hat{V}_{\mathcal{I}}(t')\,\hat{U}_{\mathcal{I}}(t').
$$

This is the Volterra equation. The two forms are therefore equivalent: the
Volterra equation packages the differential equation *and* its initial
condition into a single relation. (This is exactly why it is the better
starting point for iteration — there is no separate boundary condition to track
order by order.)

<!-- ─── -->

**2. Iteration to second order.** Substitute $\hat{U}_{\mathcal{I}}(t)=\hat{I}-(\mathrm{i}/\hbar)\int_0^t\mathrm{d}t'\,\hat{V}_{\mathcal{I}}(t')\hat{U}_{\mathcal{I}}(t')$ for $\hat{U}_{\mathcal{I}}(t')$ on its own right-hand side once, and verify the $k=2$ term of the Dyson series $\hat{U}_{\mathcal{I}}(t)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_0^t\!\mathrm{d}t_k\cdots\int_0^{t_2}\!\mathrm{d}t_1\;\hat{V}_{\mathcal{I}}(t_k)\cdots\hat{V}_{\mathcal{I}}(t_1)$. Pay attention to the ordering of the two integration variables and the signs.

**Solution.**

Start from the Volterra equation, writing the outer integration variable as
$t_1$:

$$
\hat{U}_{\mathcal{I}}(t)=\hat{I}-\frac{\mathrm{i}}{\hbar}\int_0^t\mathrm{d}t_1\,\hat{V}_{\mathcal{I}}(t_1)\,\hat{U}_{\mathcal{I}}(t_1).
$$

The factor $\hat{U}_{\mathcal{I}}(t_1)$ under the integral is itself given by the
Volterra equation, evaluated at upper limit $t_1$ and with inner variable
$t_2$:

$$
\hat{U}_{\mathcal{I}}(t_1)=\hat{I}-\frac{\mathrm{i}}{\hbar}\int_0^{t_1}\mathrm{d}t_2\,\hat{V}_{\mathcal{I}}(t_2)\,\hat{U}_{\mathcal{I}}(t_2).
$$

Substitute this into the previous line:

$$
\hat{U}_{\mathcal{I}}(t)=\hat{I}-\frac{\mathrm{i}}{\hbar}\int_0^t\mathrm{d}t_1\,\hat{V}_{\mathcal{I}}(t_1)\left[\hat{I}-\frac{\mathrm{i}}{\hbar}\int_0^{t_1}\mathrm{d}t_2\,\hat{V}_{\mathcal{I}}(t_2)\,\hat{U}_{\mathcal{I}}(t_2)\right].
$$

Distribute $\hat{V}_{\mathcal{I}}(t_1)$ across the bracket:

$$
\begin{split}
\hat{U}_{\mathcal{I}}(t)
&=\hat{I}-\frac{\mathrm{i}}{\hbar}\int_0^t\mathrm{d}t_1\,\hat{V}_{\mathcal{I}}(t_1)\\
&\quad+\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_0^t\mathrm{d}t_1\int_0^{t_1}\mathrm{d}t_2\;\hat{V}_{\mathcal{I}}(t_1)\,\hat{V}_{\mathcal{I}}(t_2)\,\hat{U}_{\mathcal{I}}(t_2).
\end{split}
$$

The first two terms are the $k=0$ and $k=1$ pieces of the Dyson series. The
third term still contains the unknown $\hat{U}_{\mathcal{I}}(t_2)$; truncating it
at $\hat{U}_{\mathcal{I}}(t_2)\to\hat{I}$ (its leading value) isolates the
**$k=2$ term**:

$$
\hat{U}_{\mathcal{I}}^{(2)}(t)=\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_0^t\mathrm{d}t_1\int_0^{t_1}\mathrm{d}t_2\;\hat{V}_{\mathcal{I}}(t_1)\,\hat{V}_{\mathcal{I}}(t_2).
$$

Compare with the general Dyson term in $\hat{U}_{\mathcal{I}}(t)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_0^t\!\mathrm{d}t_k\cdots\int_0^{t_2}\!\mathrm{d}t_1\;\hat{V}_{\mathcal{I}}(t_k)\cdots\hat{V}_{\mathcal{I}}(t_1)$, which for
$k=2$ reads

$$
\hat{U}_{\mathcal{I}}^{(2)}(t)=\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\;\hat{V}_{\mathcal{I}}(t_2)\,\hat{V}_{\mathcal{I}}(t_1).
$$

These are the *same expression* — only the dummy labels differ. In the
iteration result $t_2$ runs over $[0,t_1]$, so $t_2\le t_1$; the operator
product $\hat{V}_{\mathcal{I}}(t_1)\hat{V}_{\mathcal{I}}(t_2)$ has the **later**
time $t_1$ on the **left**. Renaming $t_1\leftrightarrow t_2$ turns the iteration
result into the Dyson form verbatim:
$\hat{V}_{\mathcal{I}}(t_2)\hat{V}_{\mathcal{I}}(t_1)$ with $t_1\le t_2$, again
later-on-the-left.

Two points to note, as flagged in the problem:

- **Ordering of integration variables.** The inner integral's upper limit is
  the outer variable, not $t$. This nesting is what restricts the domain to the
  *ordered simplex* $0\le t_2\le t_1\le t$ rather than the full square — and it
  is the simplex that produces the time ordering.
- **Signs.** Each substitution brings down one factor of $-\mathrm{i}/\hbar$, so
  the $k$-th term carries $(-\mathrm{i})^k$. For $k=2$ this is
  $(-\mathrm{i}/\hbar)^2=-1/\hbar^2$ — a real, negative prefactor; the
  individual minus signs do *not* cancel against the $\mathrm{i}^2$ in a way
  that flips the result, they combine to $-1/\hbar^2$.

<!-- ─── -->

**3. Time-ordering identity.** For an integrand symmetric in $(t_1,t_2)$, show that

$$
\int_0^t\!\mathrm{d}t_2\!\int_0^t\!\mathrm{d}t_1\,F(t_1,t_2)
=2\!\int_0^t\!\mathrm{d}t_2\!\int_0^{t_2}\!\mathrm{d}t_1\,F(t_1,t_2).
$$

Use this to rewrite the $k=2$ Dyson term with the time-ordering operator $\mathcal{T}$ as

$$
\frac{1}{2!}\Bigl(-\frac{\mathrm{i}}{\hbar}\Bigr)^{\!2}\,\mathcal{T}\!\int_0^t\!\mathrm{d}t_2\!\int_0^t\!\mathrm{d}t_1\,\hat{V}_{\mathcal{I}}(t_2)\hat{V}_{\mathcal{I}}(t_1),
$$

and explain why the $1/k!$ from the Taylor expansion of $\mathcal{T}\exp$ matches the simplex factor from time ordering.

**Solution.**

**The identity.** The double integral runs over the full square
$S=[0,t]\times[0,t]$ in the $(t_1,t_2)$ plane. The diagonal $t_1=t_2$ has zero
area, so it splits $S$ into two triangles:

$$
S_{<}=\{0\le t_1\le t_2\le t\},\qquad
S_{>}=\{0\le t_2\le t_1\le t\}.
$$

Hence

$$
\int_S F
=\underbrace{\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\,F(t_1,t_2)}_{\text{over }S_{<}}
+\underbrace{\int_0^t\mathrm{d}t_1\int_0^{t_1}\mathrm{d}t_2\,F(t_1,t_2)}_{\text{over }S_{>}}.
$$

In the second integral rename the dummy variables $t_1\leftrightarrow t_2$. The
domain $S_{>}$ becomes $S_{<}$, and the integrand becomes $F(t_2,t_1)$. By the
assumed symmetry $F(t_2,t_1)=F(t_1,t_2)$, so the second integral *equals* the
first:

$$
\int_0^t\mathrm{d}t_1\int_0^{t_1}\mathrm{d}t_2\,F(t_1,t_2)
=\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\,F(t_1,t_2).
$$

Therefore

$$
\int_0^t\mathrm{d}t_2\int_0^t\mathrm{d}t_1\,F(t_1,t_2)
=2\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\,F(t_1,t_2).
$$

**Applying it to the $k=2$ Dyson term.** The $k=2$ term from Problem 2 is

$$
\hat{U}_{\mathcal{I}}^{(2)}(t)=\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\;\hat{V}_{\mathcal{I}}(t_2)\,\hat{V}_{\mathcal{I}}(t_1).
$$

The bare integrand $\hat{V}_{\mathcal{I}}(t_2)\hat{V}_{\mathcal{I}}(t_1)$ is *not*
symmetric — the operators need not commute. But the **time-ordered** product
*is*. Define

$$
\mathcal{T}\bigl[\hat{V}_{\mathcal{I}}(t_2)\hat{V}_{\mathcal{I}}(t_1)\bigr]
=\begin{cases}
\hat{V}_{\mathcal{I}}(t_2)\hat{V}_{\mathcal{I}}(t_1), & t_2\ge t_1,\\[4pt]
\hat{V}_{\mathcal{I}}(t_1)\hat{V}_{\mathcal{I}}(t_2), & t_1\ge t_2.
\end{cases}
$$

This $F(t_1,t_2):=\mathcal{T}[\hat{V}_{\mathcal{I}}(t_2)\hat{V}_{\mathcal{I}}(t_1)]$
is symmetric by construction: $\mathcal{T}$ reorders factors by their time
arguments and is indifferent to the order in which they are written. On the
simplex $t_1\le t_2$ the operator $\mathcal{T}$ acts trivially, since
$\hat{V}_{\mathcal{I}}(t_2)\hat{V}_{\mathcal{I}}(t_1)$ is *already* time-ordered.
So

$$
\hat{U}_{\mathcal{I}}^{(2)}(t)
=\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\;\mathcal{T}\bigl[\hat{V}_{\mathcal{I}}(t_2)\hat{V}_{\mathcal{I}}(t_1)\bigr].
$$

Now apply the identity with $F=\mathcal{T}[\hat{V}_{\mathcal{I}}(t_2)\hat{V}_{\mathcal{I}}(t_1)]$,
in the form $\int_{S_{<}}F=\tfrac12\int_S F$:

$$
\hat{U}_{\mathcal{I}}^{(2)}(t)
=\frac{1}{2!}\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\,\mathcal{T}\int_0^t\mathrm{d}t_2\int_0^t\mathrm{d}t_1\;\hat{V}_{\mathcal{I}}(t_2)\,\hat{V}_{\mathcal{I}}(t_1),
$$

where $\mathcal{T}$ has been pulled outside the integral (it acts on whatever
operator product sits inside, ordering it by time argument). This is the
required form, with $2!=2$.

**Why $1/k!$ matches the simplex factor.** The argument generalizes
immediately. For the $k$-th order term, the hypercube $[0,t]^k$ decomposes into
$k!$ ordered simplices — one for each of the $k!$ permutations of
$\{t_1,\dots,t_k\}$ (the lower-dimensional boundaries where two times coincide
have zero measure). The time-ordering operator $\mathcal{T}$ makes the integrand
*totally symmetric*, so each of the $k!$ simplices contributes the **same**
integral. Hence

$$
\mathcal{T}\int_{[0,t]^k}\hat{V}_{\mathcal{I}}\cdots\hat{V}_{\mathcal{I}}
=k!\int_{0\le t_1\le\cdots\le t_k\le t}\hat{V}_{\mathcal{I}}(t_k)\cdots\hat{V}_{\mathcal{I}}(t_1).
$$

The Dyson series integrates over **one** simplex, with no explicit factorial:

$$
\hat{U}_{\mathcal{I}}(t)=\sum_{k=0}^{\infty}\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!k}\int_{\text{simplex}}\hat{V}_{\mathcal{I}}(t_k)\cdots\hat{V}_{\mathcal{I}}(t_1)
=\sum_{k=0}^{\infty}\frac{1}{k!}\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!k}\mathcal{T}\!\left(\int_0^t\mathrm{d}t'\,\hat{V}_{\mathcal{I}}(t')\right)^{\!k}.
$$

The last sum is precisely the Taylor expansion of the exponential, so

$$
\hat{U}_{\mathcal{I}}(t)=\mathcal{T}\exp\!\left(-\frac{\mathrm{i}}{\hbar}\int_0^t\mathrm{d}t'\,\hat{V}_{\mathcal{I}}(t')\right).
$$

The $1/k!$ in $\exp$ is the ratio of volumes
$\mathrm{vol(simplex)}/\mathrm{vol(hypercube)}=(t^k/k!)/t^k=1/k!$. Equivalently:
the Dyson series carries no $1/k!$ because it already restricts to a single
ordered simplex; the time-ordered exponential carries $1/k!$ because it
integrates over the whole hypercube and over-counts each ordering $k!$ times.
The two factors are the same number, viewed from the two sides of the identity.

<!-- ─── -->

**4. Bare Green's function.** From $\hat{G}_0(t,t')=\hat{U}_0(t)\hat{U}_0^{\dagger}(t')=\sum_n |n\rangle\,\mathrm{e}^{-\mathrm{i}E_n(t-t')/\hbar}\,\langle n|$,

(a) Show $\hat{G}_0(t,t'')\hat{G}_0(t'',t')=\hat{G}_0(t,t')$ using the spectral form.

(b) Show $\hat{G}_0(t,t')^{\dagger}=\hat{G}_0(t',t)$, i.e. $\hat{G}_0$ is unitary.

(c) Compute the matrix element $\langle m\vert\hat{G}_0(t,t')\vert n\rangle$ and identify the **Bohr phase**.

**Solution.**

The bare Green's function is, in the eigenbasis $\{\vert n\rangle\}$ of
$\hat{H}_0$ with $\hat{H}_0\vert n\rangle=E_n\vert n\rangle$,

$$
\hat{G}_0(t,t')=\sum_n\vert n\rangle\,\mathrm{e}^{-\mathrm{i}E_n(t-t')/\hbar}\,\langle n\vert,
$$

with $\langle m\vert n\rangle=\delta_{mn}$ and $\sum_n\vert n\rangle\langle n\vert=\hat{I}$.

**(a) Composition.** Multiply two bare propagators and use orthonormality to
collapse the inner sum:

$$
\begin{split}
\hat{G}_0(t,t'')\,\hat{G}_0(t'',t')
&=\sum_{m,n}\vert m\rangle\,\mathrm{e}^{-\mathrm{i}E_m(t-t'')/\hbar}\,\langle m\vert n\rangle\,\mathrm{e}^{-\mathrm{i}E_n(t''-t')/\hbar}\,\langle n\vert\\
&=\sum_{n}\vert n\rangle\,\mathrm{e}^{-\mathrm{i}E_n(t-t'')/\hbar}\,\mathrm{e}^{-\mathrm{i}E_n(t''-t')/\hbar}\,\langle n\vert\\
&=\sum_{n}\vert n\rangle\,\mathrm{e}^{-\mathrm{i}E_n(t-t')/\hbar}\,\langle n\vert
=\hat{G}_0(t,t').
\end{split}
$$

The intermediate time $t''$ cancels because the two exponents add:
$(t-t'')+(t''-t')=t-t'$. Free propagation composes by simply adding elapsed
times — the system has no memory of the intermediate instant.

**(b) Unitarity.** Take the Hermitian adjoint. Each $E_n$ is real (eigenvalue of
the Hermitian $\hat{H}_0$) and each $\vert n\rangle\langle n\vert$ is
self-adjoint, so only the scalar phase conjugates:

$$
\hat{G}_0(t,t')^{\dagger}
=\sum_n\vert n\rangle\,\bigl(\mathrm{e}^{-\mathrm{i}E_n(t-t')/\hbar}\bigr)^{\!*}\,\langle n\vert
=\sum_n\vert n\rangle\,\mathrm{e}^{+\mathrm{i}E_n(t-t')/\hbar}\,\langle n\vert.
$$

Rewrite the sign of the exponent as a swap of the two time arguments,
$+\,(t-t')=-(t'-t)$:

$$
\hat{G}_0(t,t')^{\dagger}=\sum_n\vert n\rangle\,\mathrm{e}^{-\mathrm{i}E_n(t'-t)/\hbar}\,\langle n\vert=\hat{G}_0(t',t).
$$

That $\hat{G}_0$ is **unitary** now follows from (a). Combining the two results,

$$
\hat{G}_0(t,t')^{\dagger}\,\hat{G}_0(t,t')=\hat{G}_0(t',t)\,\hat{G}_0(t,t')=\hat{G}_0(t',t'),
$$

and $\hat{G}_0(t',t')=\sum_n\vert n\rangle\,\mathrm{e}^{0}\,\langle n\vert=\sum_n\vert n\rangle\langle n\vert=\hat{I}$
by completeness. The same computation with the factors reversed gives
$\hat{G}_0(t,t')\hat{G}_0(t,t')^{\dagger}=\hat{I}$. Hence
$\hat{G}_0^{\dagger}=\hat{G}_0^{-1}$: the bare propagator is unitary, as it must
be, since it is the genuine time-evolution operator of the *closed*
unperturbed system.

**(c) Matrix element and Bohr phase.** Sandwich $\hat{G}_0$ between two
eigenstates and use orthonormality twice:

$$
\langle m\vert\hat{G}_0(t,t')\vert n\rangle
=\sum_k\langle m\vert k\rangle\,\mathrm{e}^{-\mathrm{i}E_k(t-t')/\hbar}\,\langle k\vert n\rangle
=\delta_{mn}\,\mathrm{e}^{-\mathrm{i}E_n(t-t')/\hbar}.
$$

So the bare propagator is **diagonal** in the $\hat{H}_0$ eigenbasis: it never
mixes levels — which is exactly the statement that the *unperturbed* system has
no transitions. Its only action on level $n$ is to multiply by the phase
factor

$$
\mathrm{e}^{-\mathrm{i}E_n(t-t')/\hbar},
$$

the **Bohr phase** of level $n$ accumulated over the interval $t-t'$. Each
eigenstate winds at its own Bohr angular frequency $E_n/\hbar$; the
*relative* Bohr phase between two levels rotates at the Bohr (transition)
frequency $\omega_{mn}=(E_m-E_n)/\hbar$. It is this relative winding,
re-expressed inside $\hat{V}_{\mathcal{I}}=\hat{U}_0^{\dagger}\hat{V}\hat{U}_0$,
that drives the resonance physics of the next section.

<!-- ─── -->

**5. Schrödinger-picture Dyson series.** Starting from $\hat{U}(t)=\hat{U}_0(t)\hat{U}_{\mathcal{I}}(t)$ and the second-order term of $\hat{U}_{\mathcal{I}}(t)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_0^t\!\mathrm{d}t_k\cdots\int_0^{t_2}\!\mathrm{d}t_1\;\hat{V}_{\mathcal{I}}(t_k)\cdots\hat{V}_{\mathcal{I}}(t_1)$, derive the second-order term of $\hat{U}(t)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_0^t\!\mathrm{d}t_k\cdots\int_0^{t_2}\!\mathrm{d}t_1\;\hat{G}_0(t,t_k)\hat{V}(t_k)\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\hat{G}_0(t_1,0)$ explicitly. Show step by step where each $\hat{G}_0$ link comes from.

**Solution.**

The $k=2$ term of the interaction-picture Dyson series (Problem 2) is

$$
\hat{U}_{\mathcal{I}}^{(2)}(t)=\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\;\hat{V}_{\mathcal{I}}(t_2)\,\hat{V}_{\mathcal{I}}(t_1).
$$

The Schrödinger-picture propagator is $\hat{U}(t)=\hat{U}_0(t)\hat{U}_{\mathcal{I}}(t)$,
so its second-order part is obtained by left-multiplying with $\hat{U}_0(t)$:

$$
\hat{U}^{(2)}(t)=\hat{U}_0(t)\,\hat{U}_{\mathcal{I}}^{(2)}(t)
=\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\;\hat{U}_0(t)\,\hat{V}_{\mathcal{I}}(t_2)\,\hat{V}_{\mathcal{I}}(t_1).
$$

Now expand each interaction-picture vertex with its definition
$\hat{V}_{\mathcal{I}}(t_j)=\hat{U}_0^{\dagger}(t_j)\,\hat{V}(t_j)\,\hat{U}_0(t_j)$:

$$
\hat{U}_0(t)\,\hat{V}_{\mathcal{I}}(t_2)\,\hat{V}_{\mathcal{I}}(t_1)
=\hat{U}_0(t)\;\hat{U}_0^{\dagger}(t_2)\hat{V}(t_2)\hat{U}_0(t_2)\;\hat{U}_0^{\dagger}(t_1)\hat{V}(t_1)\hat{U}_0(t_1).
$$

Reading left to right, the free-evolution operators pair up into bare
propagators wherever a $\hat{U}_0$ meets a $\hat{U}_0^{\dagger}$ across the
gaps between vertices. Using
$\hat{G}_0(t_a,t_b)=\hat{U}_0(t_a)\hat{U}_0^{\dagger}(t_b)$:

- **Left link.** $\hat{U}_0(t)\,\hat{U}_0^{\dagger}(t_2)=\hat{G}_0(t,t_2)$ —
  free propagation from the last vertex at $t_2$ up to the final time $t$.
- **Middle link.** $\hat{U}_0(t_2)\,\hat{U}_0^{\dagger}(t_1)=\hat{G}_0(t_2,t_1)$
  — free propagation between the two vertices.
- **Right link.** The trailing factor is $\hat{U}_0(t_1)$ alone. Since
  $\hat{U}_0(0)=\hat{I}$, write $\hat{U}_0(t_1)=\hat{U}_0(t_1)\hat{U}_0^{\dagger}(0)=\hat{G}_0(t_1,0)$
  — free propagation from the initial time $0$ up to the first vertex at $t_1$.

Substituting all three:

$$
\hat{U}_0(t)\,\hat{V}_{\mathcal{I}}(t_2)\,\hat{V}_{\mathcal{I}}(t_1)
=\hat{G}_0(t,t_2)\,\hat{V}(t_2)\,\hat{G}_0(t_2,t_1)\,\hat{V}(t_1)\,\hat{G}_0(t_1,0).
$$

Therefore

$$
\hat{U}^{(2)}(t)=\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\;\hat{G}_0(t,t_2)\,\hat{V}(t_2)\,\hat{G}_0(t_2,t_1)\,\hat{V}(t_1)\,\hat{G}_0(t_1,0),
$$

which is exactly the $k=2$ term of $\hat{U}(t)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_0^t\!\mathrm{d}t_k\cdots\int_0^{t_2}\!\mathrm{d}t_1\;\hat{G}_0(t,t_k)\hat{V}(t_k)\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\hat{G}_0(t_1,0)$. Each $\hat{G}_0$
link is a free-propagation segment; each $\hat{V}$ is an instantaneous
scattering. The expression reads, right to left along the ket,
**free $\to$ scatter at $t_1$ $\to$ free $\to$ scatter at $t_2$ $\to$ free** —
the propagate-scatter-propagate structure with the *interaction*-picture
vertices traded for *Schrödinger*-picture vertices $\hat{V}$ at the cost of
inserting $\hat{G}_0$ links between them.

<!-- ─── -->

**6. Recursive Dyson equation.** Show that $\hat{G}(t,t_0)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_{t_0}^{t}\!\mathrm{d}t_k\cdots\int_{t_0}^{t_2}\!\mathrm{d}t_1\;\hat{G}_0(t,t_k)\hat{V}(t_k)\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\hat{G}_0(t_1,t_0)$ is equivalent to the closed recursion

$$
\hat{G}(t,t_0)=\hat{G}_0(t,t_0)
-\frac{\mathrm{i}}{\hbar}\!\int_{t_0}^{t}\!\mathrm{d}t_1\,\hat{G}_0(t,t_1)\,\hat{V}(t_1)\,\hat{G}(t_1,t_0).
$$

Iterate this recursion once and verify the $k=1$ and $k=2$ terms of $\hat{G}(t,t_0)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_{t_0}^{t}\!\mathrm{d}t_k\cdots\int_{t_0}^{t_2}\!\mathrm{d}t_1\;\hat{G}_0(t,t_k)\hat{V}(t_k)\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\hat{G}_0(t_1,t_0)$.

**Solution.**

**Dyson series $\Rightarrow$ recursion.** The Dyson series for the dressed
propagator is

$$
\hat{G}(t,t_0)=\sum_{k=0}^{\infty}\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!k}\int_{t_0}^{t}\mathrm{d}t_k\cdots\int_{t_0}^{t_2}\mathrm{d}t_1\;\hat{G}_0(t,t_k)\,\hat{V}(t_k)\cdots\hat{V}(t_1)\,\hat{G}_0(t_1,t_0).
$$

Separate the $k=0$ term, which is $\hat{G}_0(t,t_0)$, from the rest. In every
$k\ge1$ term the **latest** interaction time is the outermost variable $t_k$,
integrated over $[t_0,t]$, and it is preceded (on the left) by the single link
$\hat{G}_0(t,t_k)$ and the vertex $\hat{V}(t_k)$. Factor those out:

$$
\hat{G}(t,t_0)=\hat{G}_0(t,t_0)
-\frac{\mathrm{i}}{\hbar}\int_{t_0}^{t}\mathrm{d}t_k\;\hat{G}_0(t,t_k)\,\hat{V}(t_k)\;\Bigl[\,\cdots\,\Bigr],
$$

where the bracket collects everything to the right of $\hat{V}(t_k)$, summed
over all $k\ge1$:

$$
\Bigl[\,\cdots\,\Bigr]=\sum_{k=1}^{\infty}\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!k-1}\int_{t_0}^{t_k}\mathrm{d}t_{k-1}\cdots\int_{t_0}^{t_2}\mathrm{d}t_1\;\hat{G}_0(t_k,t_{k-1})\,\hat{V}(t_{k-1})\cdots\hat{V}(t_1)\,\hat{G}_0(t_1,t_0).
$$

Set $j=k-1$. The bracket becomes a sum over $j\ge0$ of exactly the Dyson-series
terms for a dressed propagator that runs from $t_0$ to $t_k$ — that is, it *is*
$\hat{G}(t_k,t_0)$. Hence

$$
\hat{G}(t,t_0)=\hat{G}_0(t,t_0)-\frac{\mathrm{i}}{\hbar}\int_{t_0}^{t}\mathrm{d}t_k\;\hat{G}_0(t,t_k)\,\hat{V}(t_k)\,\hat{G}(t_k,t_0).
$$

Renaming the dummy variable $t_k\to t_1$ gives the stated recursion. (The
recursion simply says: in any history, peel off the last scatter — free
propagation from $t_1$ to $t$, one vertex at $t_1$, and a *fully dressed*
history from $t_0$ to $t_1$ before it.)

**Iterating the recursion.** Write the recursion compactly with a generic
latest-vertex time $s$:

$$
\hat{G}(t,t_0)=\hat{G}_0(t,t_0)-\frac{\mathrm{i}}{\hbar}\int_{t_0}^{t}\mathrm{d}s\;\hat{G}_0(t,s)\,\hat{V}(s)\,\hat{G}(s,t_0).
$$

The factor $\hat{G}(s,t_0)$ on the right is, by the same recursion (now with
upper limit $s$ and a new latest-vertex time $s'$),

$$
\hat{G}(s,t_0)=\hat{G}_0(s,t_0)-\frac{\mathrm{i}}{\hbar}\int_{t_0}^{s}\mathrm{d}s'\;\hat{G}_0(s,s')\,\hat{V}(s')\,\hat{G}(s',t_0).
$$

Substitute:

$$
\begin{split}
\hat{G}(t,t_0)=\;&\hat{G}_0(t,t_0)\\
&-\frac{\mathrm{i}}{\hbar}\int_{t_0}^{t}\mathrm{d}s\;\hat{G}_0(t,s)\,\hat{V}(s)\,\hat{G}_0(s,t_0)\\
&+\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_{t_0}^{t}\mathrm{d}s\int_{t_0}^{s}\mathrm{d}s'\;\hat{G}_0(t,s)\,\hat{V}(s)\,\hat{G}_0(s,s')\,\hat{V}(s')\,\hat{G}(s',t_0).
\end{split}
$$

Now read off the orders in $\hat{V}$:

- **$k=0$:** $\hat{G}_0(t,t_0)$ — matches the zeroth term of $\hat{G}(t,t_0)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_{t_0}^{t}\!\mathrm{d}t_k\cdots\int_{t_0}^{t_2}\!\mathrm{d}t_1\;\hat{G}_0(t,t_k)\hat{V}(t_k)\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\hat{G}_0(t_1,t_0)$.
- **$k=1$:** with $s\to t_1$,
  $-\dfrac{\mathrm{i}}{\hbar}\displaystyle\int_{t_0}^{t}\mathrm{d}t_1\;\hat{G}_0(t,t_1)\,\hat{V}(t_1)\,\hat{G}_0(t_1,t_0)$
  — exactly the $k=1$ term of $\hat{G}(t,t_0)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_{t_0}^{t}\!\mathrm{d}t_k\cdots\int_{t_0}^{t_2}\!\mathrm{d}t_1\;\hat{G}_0(t,t_k)\hat{V}(t_k)\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\hat{G}_0(t_1,t_0)$.
- **$k=2$:** the last line is already $O(\hat{V}^2)$ *before* counting the
  $\hat{G}(s',t_0)$ tail; to isolate the pure $k=2$ term, replace that tail by
  its leading piece $\hat{G}(s',t_0)\to\hat{G}_0(s',t_0)$. Renaming
  $s\to t_2,\;s'\to t_1$ (so that $t_0\le t_1\le t_2\le t$):

  $$
  \left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_{t_0}^{t}\mathrm{d}t_2\int_{t_0}^{t_2}\mathrm{d}t_1\;\hat{G}_0(t,t_2)\,\hat{V}(t_2)\,\hat{G}_0(t_2,t_1)\,\hat{V}(t_1)\,\hat{G}_0(t_1,t_0),
  $$

  which is the $k=2$ term of $\hat{G}(t,t_0)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_{t_0}^{t}\!\mathrm{d}t_k\cdots\int_{t_0}^{t_2}\!\mathrm{d}t_1\;\hat{G}_0(t,t_k)\hat{V}(t_k)\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\hat{G}_0(t_1,t_0)$.

Each further substitution of the recursion peels off one more vertex and raises
the order by one, regenerating the full Dyson series term by term. The
recursion and the series are therefore equivalent.

<!-- ─── -->

**7. Two-level Feynman diagrams.** Take

$$
\begin{split}
\hat{H}_0&=\frac{\hbar\omega_0}{2}\hat{Z},\\
\hat{V}&=\hbar\Omega\,\hat{X},
\end{split}
$$

with $\hat{V}$ time-independent.

(a) Write the second-order amplitude $\langle 1\vert\hat{U}(t)\vert 0\rangle$ from $\hat{U}(t)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_0^t\!\mathrm{d}t_k\cdots\int_0^{t_2}\!\mathrm{d}t_1\;\hat{G}_0(t,t_k)\hat{V}(t_k)\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\hat{G}_0(t_1,0)$.

(b) Identify which intermediate states contribute and draw the corresponding Feynman diagram.

(c) Argue physically why this term is *not* the dominant contribution to $\vert 0\rangle\to\vert 1\rangle$ at small $\Omega t$ (compare with the first-order amplitude).

**Solution.**

The unperturbed Hamiltonian is diagonal in the computational basis:
$\hat{Z}\vert 0\rangle=+\vert 0\rangle$, $\hat{Z}\vert 1\rangle=-\vert 1\rangle$,
so

$$
E_0=+\frac{\hbar\omega_0}{2},\qquad E_1=-\frac{\hbar\omega_0}{2}.
$$

The bare propagator is diagonal,

$$
\hat{G}_0(t,t')=\mathrm{e}^{-\mathrm{i}\omega_0(t-t')/2}\,\vert 0\rangle\langle 0\vert
+\mathrm{e}^{+\mathrm{i}\omega_0(t-t')/2}\,\vert 1\rangle\langle 1\vert,
$$

and the perturbation is a pure spin-flip,
$\hat{V}=\hbar\Omega\,\hat{X}=\hbar\Omega\bigl(\vert 0\rangle\langle 1\vert+\vert 1\rangle\langle 0\vert\bigr)$.

**(a) Second-order amplitude.** The $k=2$ term of $\hat{U}(t)=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_0^t\!\mathrm{d}t_k\cdots\int_0^{t_2}\!\mathrm{d}t_1\;\hat{G}_0(t,t_k)\hat{V}(t_k)\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\hat{G}_0(t_1,0)$,
sandwiched between $\langle 1\vert$ and $\vert 0\rangle$, is

$$
\langle 1\vert\hat{U}^{(2)}(t)\vert 0\rangle
=\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\;
\langle 1\vert\hat{G}_0(t,t_2)\,\hat{V}\,\hat{G}_0(t_2,t_1)\,\hat{V}\,\hat{G}_0(t_1,0)\vert 0\rangle.
$$

Evaluate the operator string acting on $\vert 0\rangle$, right to left. The bare
propagators only attach phases; each $\hat{V}=\hbar\Omega\hat{X}$ flips the
qubit:

$$
\vert 0\rangle
\xrightarrow{\;\hat{G}_0(t_1,0)\;}\mathrm{e}^{-\mathrm{i}\omega_0 t_1/2}\vert 0\rangle
\xrightarrow{\;\hat{V}\;}\hbar\Omega\,\mathrm{e}^{-\mathrm{i}\omega_0 t_1/2}\vert 1\rangle
\xrightarrow{\;\hat{G}_0(t_2,t_1)\;}\cdots\vert 1\rangle
\xrightarrow{\;\hat{V}\;}\cdots\vert 0\rangle
\xrightarrow{\;\hat{G}_0(t,t_2)\;}\cdots\vert 0\rangle.
$$

Two flips return the qubit to $\vert 0\rangle$. The surviving ket is
proportional to $\vert 0\rangle$, and $\langle 1\vert 0\rangle=0$, so **every
term in the integrand vanishes**:

$$
\boxed{\;\langle 1\vert\hat{U}^{(2)}(t)\vert 0\rangle=0.\;}
$$

This is a selection rule: $\hat{V}\propto\hat{X}$ flips the qubit exactly once
per vertex, so the $k$-th order term connects $\vert 0\rangle$ to $\vert 1\rangle$
only when $k$ is **odd**. The second-order amplitude for $0\to1$ is identically
zero.

**(b) Intermediate states and diagram.** A non-vanishing second-order process
*does* exist — but it returns to the starting level. The single intermediate
state available is $\vert 1\rangle$ (the only state $\hat{X}$ connects to
$\vert 0\rangle$), and the surviving second-order matrix element is the
*diagonal* one:

$$
\langle 0\vert\hat{U}^{(2)}(t)\vert 0\rangle
=\left(-\frac{\mathrm{i}}{\hbar}\right)^{\!2}(\hbar\Omega)^2\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\;
\mathrm{e}^{-\mathrm{i}\omega_0(t-t_2)/2}\,\mathrm{e}^{+\mathrm{i}\omega_0(t_2-t_1)/2}\,\mathrm{e}^{-\mathrm{i}\omega_0 t_1/2}.
$$

Its Feynman diagram has the internal segment running on level $\vert 1\rangle$:

```
   |0>          |1>          |0>
 0 ====●========●==== t
       t1        t2
   G0(t1,0)  V  G0(t2,t1)  V  G0(t,t2)
```

a $\hat{G}_0$ line on $\vert 0\rangle$ from $0$ to the first vertex at $t_1$, a
$\hat{G}_0$ line on the **intermediate** state $\vert 1\rangle$ from $t_1$ to
$t_2$, and a $\hat{G}_0$ line back on $\vert 0\rangle$ from $t_2$ to $t$. For the
*requested* transition $\vert 0\rangle\to\vert 1\rangle$ there is **no**
second-order diagram at all: two flips cannot connect $\vert 0\rangle$ to
$\vert 1\rangle$, so the diagram simply does not close on $\langle 1\vert$.

**(c) Why second order is not the dominant $0\to1$ contribution.** Compute the
first-order amplitude for comparison:

$$
\langle 1\vert\hat{U}^{(1)}(t)\vert 0\rangle
=-\frac{\mathrm{i}}{\hbar}\int_0^t\mathrm{d}t_1\;\langle 1\vert\hat{G}_0(t,t_1)\,\hat{V}\,\hat{G}_0(t_1,0)\vert 0\rangle.
$$

Here a *single* flip lands on $\vert 1\rangle$, so the amplitude is non-zero:

$$
\langle 1\vert\hat{U}^{(1)}(t)\vert 0\rangle
=-\mathrm{i}\Omega\int_0^t\mathrm{d}t_1\;\mathrm{e}^{+\mathrm{i}\omega_0(t-t_1)/2}\,\mathrm{e}^{-\mathrm{i}\omega_0 t_1/2}
=-\mathrm{i}\Omega\,\mathrm{e}^{\mathrm{i}\omega_0 t/2}\int_0^t\mathrm{d}t_1\;\mathrm{e}^{-\mathrm{i}\omega_0 t_1}.
$$

The integral is $(1-\mathrm{e}^{-\mathrm{i}\omega_0 t})/(\mathrm{i}\omega_0)$, and
$\mathrm{e}^{\mathrm{i}\omega_0 t/2}(1-\mathrm{e}^{-\mathrm{i}\omega_0 t})=\mathrm{e}^{\mathrm{i}\omega_0 t/2}-\mathrm{e}^{-\mathrm{i}\omega_0 t/2}=2\mathrm{i}\sin(\omega_0 t/2)$,
so

$$
\langle 1\vert\hat{U}^{(1)}(t)\vert 0\rangle=-\frac{2\mathrm{i}\Omega}{\omega_0}\sin\!\left(\frac{\omega_0 t}{2}\right)
\;\xrightarrow[\;\Omega t,\,\omega_0 t\ll 1\;]{}\;-\mathrm{i}\,\Omega t.
$$

The first-order amplitude is $O(\Omega t)$ — linear in the coupling and
*non-zero*. The second-order amplitude for $0\to1$ is exactly zero, by the
flip-parity selection rule of part (a). The first correction to $0\to1$ beyond
first order is therefore the **third**-order term, of size $O((\Omega t)^3)$.

So at small $\Omega t$ the hierarchy of $0\to1$ contributions is

$$
\underbrace{O(\Omega t)}_{k=1}\;\gg\;\underbrace{0}_{k=2}\;,\qquad
\text{next correction }O\!\bigl((\Omega t)^3\bigr)\ \text{at }k=3.
$$

The second-order term is not "subdominant" in the usual sense — it is
identically absent. The physical reason is the parity of spin flips: reaching
$\vert 1\rangle$ from $\vert 0\rangle$ requires an **odd** number of $\hat{X}$
vertices, and order $k=2$ supplies an even number. Even orders dress the
*survival* amplitude $\langle 0\vert\hat{U}\vert 0\rangle$; odd orders carry the
*transition* amplitude $\langle 1\vert\hat{U}\vert 0\rangle$.

<!-- ─── -->

★ **8. Three-level virtual transition.** Let $\hat{H}_0=\Delta\vert 3\rangle\langle 3\vert$ with $E_1=E_2=0$ and $E_3=\Delta$. Take a perturbation that connects $\vert 1\rangle\leftrightarrow\vert 3\rangle\leftrightarrow\vert 2\rangle$ but has no direct $\vert 1\rangle\leftrightarrow\vert 2\rangle$ matrix element:

$$
\begin{split}
\hat{V}(t)&=\lambda(t)\bigl[(\vert 1\rangle+\vert 2\rangle)\langle 3\vert+\mathrm{h.c.}\bigr],\\
\lambda(t)&=\lambda_0\cos(\omega t).
\end{split}
$$

At $t=0$ the system is prepared in $\vert 1\rangle$; we compute the amplitude $\langle 2\vert\hat{G}(t,0)\vert 1\rangle$ to find it in $\vert 2\rangle$ at time $t$. Work in units with $\hbar=1$ throughout this problem, so $\Delta$ is the level-3 angular frequency and the Dyson factor at order $k$ is $(-\mathrm{i})^k$.

(a) Write down $\hat{G}_0(t,t')$ explicitly using the spectral form.

(b) Argue from the Dyson series

$$
\begin{split}
\hat{G}(t,t_0)&=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_{t_0}^{t}\!\mathrm{d}t_k\cdots\int_{t_0}^{t_2}\!\mathrm{d}t_1\\
&\quad\hat{G}_0(t,t_k)\,\hat{V}(t_k)\,\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\,\hat{G}_0(t_1,t_0)
\end{split}
$$

that the leading nonzero contribution to $\langle 2\vert\hat{G}(t,0)\vert 1\rangle$ is **second order** in $\lambda_0$, and identify which Feynman diagram it corresponds to.

(c) Write the second-order amplitude explicitly as a double time integral; leave it unevaluated here (that comes in 5.2.3 once we know how to handle long-time limits).

**Solution.**

Spelling out the Hermitian conjugate, the perturbation is

$$
\hat{V}(t)=\lambda(t)\Bigl[(\vert 1\rangle+\vert 2\rangle)\langle 3\vert+\vert 3\rangle(\langle 1\vert+\langle 2\vert)\Bigr].
$$

Its only nonzero matrix elements are $\langle 1\vert\hat{V}\vert 3\rangle=\langle 3\vert\hat{V}\vert 1\rangle=\lambda(t)$
and $\langle 2\vert\hat{V}\vert 3\rangle=\langle 3\vert\hat{V}\vert 2\rangle=\lambda(t)$;
in particular $\langle 1\vert\hat{V}\vert 2\rangle=\langle 2\vert\hat{V}\vert 1\rangle=0$.
Level $\vert 3\rangle$ is the only doorway between $\vert 1\rangle$ and
$\vert 2\rangle$.

**(a) Bare Green's function.** With $E_1=E_2=0$ and $E_3=\Delta$, the spectral
form $\hat{G}_0(t,t')=\sum_n\vert n\rangle\,\mathrm{e}^{-\mathrm{i}E_n(t-t')}\,\langle n\vert$
gives

$$
\hat{G}_0(t,t')=\vert 1\rangle\langle 1\vert+\vert 2\rangle\langle 2\vert+\mathrm{e}^{-\mathrm{i}\Delta(t-t')}\,\vert 3\rangle\langle 3\vert.
$$

The two zero-energy states do not wind; only $\vert 3\rangle$ carries a phase,
at its Bohr frequency $\Delta$.

**(b) Leading order is $\lambda_0^2$.** Examine the Dyson series

$$
\begin{split}
\hat{G}(t,t_0)&=\sum_{k=0}^{\infty}(-\mathrm{i})^k\int_{t_0}^{t}\!\mathrm{d}t_k\cdots\int_{t_0}^{t_2}\!\mathrm{d}t_1\\
&\quad\hat{G}_0(t,t_k)\,\hat{V}(t_k)\,\hat{G}_0(t_k,t_{k-1})\cdots\hat{V}(t_1)\,\hat{G}_0(t_1,t_0)
\end{split}
$$

for $\langle 2\vert\hat{G}(t,0)\vert 1\rangle$ order by order; each vertex
$\hat{V}$ carries one power of $\lambda_0$.

- **$k=0$:** $\langle 2\vert\hat{G}_0(t,0)\vert 1\rangle$. Since $\hat{G}_0$ is
  diagonal, this is $\propto\langle 2\vert 1\rangle=0$. **Vanishes.**
- **$k=1$:** $-\mathrm{i}\int_0^t\mathrm{d}t_1\,\langle 2\vert\hat{G}_0(t,t_1)\,\hat{V}(t_1)\,\hat{G}_0(t_1,0)\vert 1\rangle$.
  The bare propagators are diagonal, so this reduces to
  $\langle 2\vert\hat{V}(t_1)\vert 1\rangle$ — which is zero, because $\hat{V}$
  has **no direct** $\vert 1\rangle\leftrightarrow\vert 2\rangle$ element.
  **Vanishes.**
- **$k=2$:** the integrand contains
  $\langle 2\vert\hat{V}(t_2)\cdots\hat{V}(t_1)\vert 1\rangle$. Now there is a
  non-zero path: the first vertex takes $\vert 1\rangle\to\vert 3\rangle$, the
  second takes $\vert 3\rangle\to\vert 2\rangle$. **Nonzero.**

The leading nonzero contribution is therefore **second order in $\lambda_0$**.
Physically, $\vert 1\rangle$ and $\vert 2\rangle$ are not directly coupled; the
system can only get from one to the other by a *virtual* excursion through the
intermediate state $\vert 3\rangle$. The corresponding Feynman diagram is the
single second-order graph

```
   |1>          |3>          |2>
 0 ====●========●==== t
       t1        t2
  G0(t1,0)  V   G0(t2,t1)  V   G0(t,t2)
       |1>→|3>      |3>→|2>
```

a bare line on $\vert 1\rangle$ from $0$ to the vertex at $t_1$, a bare line on
the **virtual** state $\vert 3\rangle$ from $t_1$ to $t_2$ (this internal line
carries the only nontrivial phase, $\mathrm{e}^{-\mathrm{i}\Delta(t_2-t_1)}$),
and a bare line on $\vert 2\rangle$ from $t_2$ to $t$. It is the unique
$1\to3\to2$ second-order diagram.

**(c) Second-order amplitude as a double integral.** Specializing the Dyson
series at $k=2$ (with $t_0=0$):

$$
\begin{split}
\langle 2\vert\hat{G}(t,0)\vert 1\rangle
&\approx(-\mathrm{i})^{2}\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\\
&\quad\langle 2\vert\hat{G}_0(t,t_2)\,\hat{V}(t_2)\,\hat{G}_0(t_2,t_1)\,\hat{V}(t_1)\,\hat{G}_0(t_1,0)\vert 1\rangle.
\end{split}
$$

Evaluate the matrix element, reading the operator string right to left:

$$
\begin{split}
\hat{G}_0(t_1,0)\vert 1\rangle&=\vert 1\rangle, &&(E_1=0)\\
\hat{V}(t_1)\vert 1\rangle&=\lambda(t_1)\,\vert 3\rangle, &&\\
\hat{G}_0(t_2,t_1)\vert 3\rangle&=\mathrm{e}^{-\mathrm{i}\Delta(t_2-t_1)}\,\vert 3\rangle, &&\\
\hat{V}(t_2)\vert 3\rangle&=\lambda(t_2)\,(\vert 1\rangle+\vert 2\rangle), &&\\
\langle 2\vert\hat{G}_0(t,t_2)&=\langle 2\vert, &&(E_2=0)
\end{split}
$$

and $\langle 2\vert(\vert 1\rangle+\vert 2\rangle)=1$. The matrix element is
therefore $\lambda(t_2)\,\lambda(t_1)\,\mathrm{e}^{-\mathrm{i}\Delta(t_2-t_1)}$.
With $(-\mathrm{i})^{2}=-1$,

$$
\begin{split}
\langle 2\vert\hat{G}(t,0)\vert 1\rangle
&\approx-\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\\
&\quad\lambda(t_2)\,\lambda(t_1)\;\mathrm{e}^{-\mathrm{i}\Delta(t_2-t_1)}.
\end{split}
$$

Inserting the drive $\lambda(t)=\lambda_0\cos(\omega t)$:

$$
\boxed{\;
\begin{split}
\langle 2\vert\hat{G}(t,0)\vert 1\rangle
&\approx-\lambda_0^{2}\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\\
&\quad\cos(\omega t_2)\,\cos(\omega t_1)\;\mathrm{e}^{-\mathrm{i}\Delta(t_2-t_1)}.
\end{split}
\;}
$$

The amplitude is manifestly $O(\lambda_0^2)$, as argued in (b). The double
integral is left unevaluated; expanding the cosines into exponentials splits it
into four nested integrals of the form
$\int_0^t\mathrm{d}t_2\int_0^{t_2}\mathrm{d}t_1\,\mathrm{e}^{\mathrm{i}\Omega_1 t_1}\mathrm{e}^{\mathrm{i}\Omega_2 t_2}$,
whose resonant long-time behavior (and the resulting transition rate) is the
subject of 5.2.3.
