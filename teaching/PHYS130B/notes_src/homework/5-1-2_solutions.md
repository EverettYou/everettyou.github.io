# 5.1.2 Non-degenerate Perturbation Theory
Worked solutions for the homework problems in the [5.1.2 Non-degenerate Perturbation Theory](../ch5_perturbation-theory/5-1-2-non-degenerate-perturbation-theory) lecture. Each problem statement is reproduced verbatim, followed by a complete worked solution.

<!-- ─── -->

**1. Gauge choice and normalization convention.** Starting from $\langle n(\lambda)\vert n(\lambda)\rangle=1$, show that one can choose the phase convention so that

$$
\langle n^{(0)}\vert n^{(1)}\rangle=0.
$$

Explain why this choice simplifies perturbative state corrections.

**Solution.**

**Normalization forces the overlap to be imaginary.** The perturbed state is
normalized for every $\lambda$, $\langle n(\lambda)\vert n(\lambda)\rangle=1$.
Differentiate this identity with respect to $\lambda$:

$$
\langle\partial_\lambda n\vert n\rangle + \langle n\vert\partial_\lambda n\rangle = 0.
$$

The two terms are complex conjugates of each other, so their sum is
$2\,\mathrm{Re}\langle n\vert\partial_\lambda n\rangle$. Hence

$$
\mathrm{Re}\,\langle n\vert\partial_\lambda n\rangle = 0
\quad\Longrightarrow\quad
\langle n\vert\partial_\lambda n\rangle = \mathrm{i}\,\theta(\lambda),
$$

with $\theta(\lambda)$ real. Normalization alone does **not** kill the diagonal
overlap; it only constrains it to be purely imaginary. The overlap that the
problem asks about is exactly this object at $\lambda=0$, since $\vert
n^{(0)}\rangle=\vert n\rangle$ and $\vert n^{(1)}\rangle=\vert\partial_\lambda
n\rangle$, so $\langle n^{(0)}\vert n^{(1)}\rangle = \langle
n\vert\partial_\lambda n\rangle\big\vert_{\lambda=0} = \mathrm{i}\,\theta(0)$.

**The phase is free — use it.** An eigenstate is defined only up to a
$\lambda$-dependent phase: $\vert n(\lambda)\rangle$ and $\vert\tilde
n(\lambda)\rangle = \mathrm{e}^{\mathrm{i}\gamma(\lambda)}\vert n(\lambda)\rangle$
solve the same eigenvalue equation with the same energy. Under this rephasing,

$$
\langle\tilde n\vert\partial_\lambda\tilde n\rangle
= \mathrm{e}^{-\mathrm{i}\gamma}\langle n\vert\,\partial_\lambda\!\left(\mathrm{e}^{\mathrm{i}\gamma}\vert n\rangle\right)
= \langle n\vert\partial_\lambda n\rangle + \mathrm{i}\,\partial_\lambda\gamma
= \mathrm{i}\,\big(\theta(\lambda) + \partial_\lambda\gamma\big).
$$

Choosing the phase to satisfy $\partial_\lambda\gamma = -\theta(\lambda)$ — that
is, $\gamma(\lambda) = -\int_0^\lambda\theta(\lambda')\,\mathrm{d}\lambda'$ —
makes $\langle\tilde n\vert\partial_\lambda\tilde n\rangle = 0$ for all
$\lambda$. Dropping the tilde, this is the **parallel-transport gauge**, and in
particular at $\lambda=0$:

$$
\langle n^{(0)}\vert n^{(1)}\rangle = \langle n\vert\partial_\lambda n\rangle = 0.
$$

**Why this simplifies the state corrections.** Expand $\vert\partial_\lambda
n\rangle$ in the unperturbed basis:

$$
\vert\partial_\lambda n\rangle
= \vert n\rangle\langle n\vert\partial_\lambda n\rangle
+ \sum_{m\neq n}\vert m\rangle\langle m\vert\partial_\lambda n\rangle.
$$

The off-diagonal coefficients are fixed by physics — the second
Hellmann-Feynman identity gives $\langle m\vert\partial_\lambda n\rangle =
V_{mn}/(E_n-E_m)$. The diagonal coefficient $\langle n\vert\partial_\lambda
n\rangle$ is *not* fixed by physics: it is pure phase, carrying no observable
content (an overall phase of a state is unmeasurable). Setting it to zero by
gauge choice removes a bookkeeping term that would otherwise propagate through
every order, and leaves the clean result

$$
\vert n^{(1)}\rangle = \sum_{m\neq n}\vert m\rangle\,\frac{V_{mn}}{E_n-E_m}.
$$

The first-order correction then lives *entirely* in the orthogonal complement
of $\vert n\rangle$: it is pure "sideways" mixing into other levels, with no
component along $\vert n\rangle$ itself. Equivalently, the gauge enforces
intermediate normalization $\langle n^{(0)}\vert n(\lambda)\rangle = 1 +
O(\lambda^2)$, so projecting any perturbative equation onto $\langle
n^{(0)}\vert$ isolates energies, while projecting onto $\langle m^{(0)}\vert$
($m\neq n$) isolates state coefficients — the two problems decouple order by
order.

<!-- ─── -->

★ **2. Three-level perturbation.** Find the perturbative corrections to the energies and to the ground state of $\hat H(\lambda) = \hat H_0 + \lambda\hat V$ with

$$
\hat H_0=\begin{pmatrix}1&0&0\\0&2&0\\0&0&4\end{pmatrix},
\qquad
\hat V=\begin{pmatrix}1&1&1\\1&0&1\\1&1&-1\end{pmatrix}.
$$

(a) Apply the first-order energy formula $E_n^{(1)} = \langle n^{(0)}\vert\hat V\vert n^{(0)}\rangle$ to obtain $E_n^{(1)}$ for all three states.

(b) Apply the first-order state formula

$$
\vert n^{(1)}\rangle = \sum_{m\neq n}\frac{V_{mn}}{E_n^{(0)} - E_m^{(0)}}\,\vert m^{(0)}\rangle
$$

to assemble $\vert 1^{(1)}\rangle$ for the ground state.

(c) Apply the second-order energy formula $E_n^{(2)} = \sum_{m\neq n}\vert V_{mn}\vert^{2}/(E_n^{(0)} - E_m^{(0)})$ to compute $E_1^{(2)}$. Verify the perturbative expansion by diagonalising $\hat H(\lambda)$ at $\lambda = 0.01$ and comparing the exact $E_1(0.01)$ with $E_1^{(0)} + \lambda E_1^{(1)} + \lambda^{2} E_1^{(2)}$.

**Solution.**

Label the unperturbed eigenstates $\vert 1\rangle,\vert 2\rangle,\vert 3\rangle$ with $E_1^{(0)}=1$, $E_2^{(0)}=2$, $E_3^{(0)}=4$. They are the standard basis vectors because $\hat H_0$ is already diagonal, so the matrix elements $V_{mn} = \langle m\vert\hat V\vert n\rangle$ are simply the $(m,n)$ entries of $\hat V$.

**(a)** First-order energy corrections read off the diagonal of $\hat V$:

$$
E_1^{(1)} = V_{11} = 1,
\qquad
E_2^{(1)} = V_{22} = 0,
\qquad
E_3^{(1)} = V_{33} = -1.
$$

**(b)** First-order state correction for $n=1$. The relevant off-diagonal matrix elements are $V_{21} = 1$ and $V_{31} = 1$; the unperturbed energy denominators are $E_1^{(0)} - E_2^{(0)} = -1$ and $E_1^{(0)} - E_3^{(0)} = -3$. Therefore

$$
\vert 1^{(1)}\rangle = \frac{V_{21}}{E_1^{(0)} - E_2^{(0)}}\vert 2\rangle + \frac{V_{31}}{E_1^{(0)} - E_3^{(0)}}\vert 3\rangle = -\vert 2\rangle - \tfrac{1}{3}\vert 3\rangle.
$$

The perturbed ground branch tilts strongly toward $\vert 2\rangle$ (small gap of magnitude $1$) and weakly toward $\vert 3\rangle$ (larger gap of magnitude $3$) — coupling-over-gap at work.

**(c)** Second-order energy correction for $n=1$:

$$
E_1^{(2)} = \frac{\vert V_{21}\vert^{2}}{E_1^{(0)} - E_2^{(0)}} + \frac{\vert V_{31}\vert^{2}}{E_1^{(0)} - E_3^{(0)}} = \frac{1}{-1} + \frac{1}{-3} = -\frac{4}{3}.
$$

The perturbative expansion to second order is

$$
E_1(\lambda) \approx E_1^{(0)} + \lambda E_1^{(1)} + \lambda^{2}E_1^{(2)} = 1 + \lambda - \tfrac{4}{3}\lambda^{2}.
$$

At $\lambda = 0.01$,

$$
1 + 0.01 - \tfrac{4}{3}(0.01)^{2} = 1 + 0.01 - 0.000133 = 1.009867.
$$

Numerical diagonalisation of $\hat H(0.01) = \hat H_0 + 0.01\hat V$ gives the lowest eigenvalue $E_1(0.01) = 1.00986612$, matching the second-order prediction to six decimal places. The remaining $O(\lambda^{3})$ discrepancy ($\sim 10^{-6}$) is the next perturbative correction. The standard formulas $E_n^{(1)} = V_{nn}$, $E_n^{(2)} = \sum_{m\ne n}\vert V_{mn}\vert^{2}/(E_n^{(0)} - E_m^{(0)})$, and $\vert n^{(1)}\rangle = \sum_{m\ne n}V_{mn}/(E_n^{(0)} - E_m^{(0)})\,\vert m^{(0)}\rangle$ all check out.

<!-- ─── -->

**3. Coupling over gap.** Two two-level systems share the same coupling magnitude $\vert V_{12}\vert=\hbar\omega_c$ but different gaps. System A has $E_2-E_1=10\hbar\omega_c$; system B has $E_2-E_1=2\hbar\omega_c$. Set $\lambda=1$ in both.

(a) Compute the first-order state correction $\vert 1^{(1)}\rangle=\sum_{m\neq 1}\vert m\rangle V_{m1}/(E_1-E_m)$ for each system.

(b) Compute the second-order energy correction $E_1^{(2)}$ for each.

(c) Estimate the largest coupling magnitude $\vert V_{12}\vert$ for which the perturbative expansion is well-behaved (next correction small compared to the gap). Comment on which system is "more perturbative" and why.

**Solution.**

Each system is a two-level problem, so the sums over $m\neq 1$ collapse to the
single term $m=2$. Take the coupling real and positive, $V_{21}=V_{12}=\hbar\omega_c$
(an overall phase of $V_{21}$ only rephases $\vert 1^{(1)}\rangle$ and drops out
of every energy, which depends on $\vert V_{12}\vert^2$).

**(a) First-order state correction.** With $\lambda=1$,

$$
\vert 1^{(1)}\rangle = \vert 2\rangle\,\frac{V_{21}}{E_1-E_2}.
$$

System A: $\dfrac{V_{21}}{E_1-E_2} = \dfrac{\hbar\omega_c}{-10\hbar\omega_c} =
-\dfrac{1}{10}$, so $\vert 1^{(1)}\rangle_A = -\tfrac{1}{10}\vert 2\rangle$.

System B: $\dfrac{V_{21}}{E_1-E_2} = \dfrac{\hbar\omega_c}{-2\hbar\omega_c} =
-\dfrac{1}{2}$, so $\vert 1^{(1)}\rangle_B = -\tfrac{1}{2}\vert 2\rangle$.

System B mixes the upper state in five times more strongly than A, purely
because its gap is five times smaller.

**(b) Second-order energy correction.** With $E_1^{(2)} = \vert
V_{21}\vert^2/(E_1-E_2)$ and $\lambda=1$,

$$
E_{1,A}^{(2)} = \frac{(\hbar\omega_c)^2}{-10\hbar\omega_c} = -\frac{\hbar\omega_c}{10},
\qquad
E_{1,B}^{(2)} = \frac{(\hbar\omega_c)^2}{-2\hbar\omega_c} = -\frac{\hbar\omega_c}{2}.
$$

Both shifts are negative — the lower level is pushed down by the level above it
(Problem 4) — and B's shift is five times larger.

**(c) When is the expansion well-behaved.** The dimensionless expansion
parameter is the coupling-over-gap ratio

$$
r = \frac{\vert V_{12}\vert}{\vert E_1-E_2\vert}.
$$

It controls both the state mixing ($\vert 1^{(1)}\rangle$ has amplitude $r$) and
the relative energy shift ($E_1^{(2)}/\text{gap}$ scales as $r^2$). The exact
two-level energies are $E_\pm = \bar E\pm\sqrt{(\Delta/2)^2+\vert V_{12}\vert^2}$
with $\Delta=E_2-E_1$; the square root has a branch point at $\vert
V_{12}\vert=\Delta/2$, so the perturbative series in $\vert V_{12}\vert$
**converges only for** $\vert V_{12}\vert<\Delta/2$ — the half-gap is the hard
radius of convergence. "Well-behaved," in the stronger sense that the next
correction is genuinely *small* compared to the gap, requires comfortably
beating that bound, say $\vert V_{12}\vert\lesssim\Delta/4$ ($r\lesssim
\tfrac14$).

- System A: $\Delta=10\hbar\omega_c$, half-gap $5\hbar\omega_c$. The series
  converges up to $\vert V_{12}\vert\approx5\hbar\omega_c$; "well-behaved" up to
  $\vert V_{12}\vert\approx2.5\hbar\omega_c$. The actual coupling $\hbar\omega_c$
  gives $r=0.1$ — deep in the perturbative regime, with a comfortable margin.
- System B: $\Delta=2\hbar\omega_c$, half-gap $\hbar\omega_c$. The actual
  coupling $\hbar\omega_c$ sits *exactly at* the convergence boundary, $r=0.5$.
  The expansion is marginal at best: corrections do not shrink quickly, and a
  slightly larger coupling would make the series diverge.

**System A is "more perturbative."** With the same coupling, its larger gap
makes $r$ five times smaller, so its state corrections and energy shifts are
small, the series converges fast, and truncation at low order is accurate. The
lesson is the recurring theme of the chapter: what governs perturbation theory
is never the coupling alone, but the coupling *relative to* the gap.

<!-- ─── -->

**4. Second-order energy correction and sign.** Starting from

$$
E_n^{(2)}=\sum_{m\neq n}\frac{\vert V_{mn}\vert^2}{E_n-E_m},
$$

(a) show $E_0^{(2)}\le 0$ for the non-degenerate ground state,

(b) interpret the result as level repulsion,

(c) connect it to the variational principle.

**Solution.**

**(a)** Let $n=0$ label the non-degenerate ground state, so $E_0<E_m$ for every
$m\neq 0$. Examine a single term of the sum:

$$
\frac{\vert V_{m0}\vert^2}{E_0-E_m}.
$$

The numerator $\vert V_{m0}\vert^2\ge 0$ is a squared modulus. The denominator
$E_0-E_m<0$ strictly, because the ground state is non-degenerate and lowest.
Each term is therefore (non-positive number) $=$ (non-negative) $/$ (negative)
$\le 0$. A sum of non-positive terms is non-positive:

$$
E_0^{(2)} = \sum_{m\neq 0}\frac{\vert V_{m0}\vert^2}{E_0-E_m} \le 0.
$$

It is strictly negative as soon as at least one coupling $V_{m0}$ is nonzero.

**(b) Level repulsion.** Each excited state $m$ contributes a downward push
$-\vert V_{m0}\vert^2/(E_m-E_0)$ to the ground energy. Physically, the
perturbation $\hat V$ admixes higher states into the ground state ("virtual
transitions" up to $\vert m\rangle$ and back); the net effect of every such
virtual excursion is to *lower* the ground level. Viewed as a pair of
interacting levels, $\vert 0\rangle$ and $\vert m\rangle$ are driven apart: the
lower one ($\vert 0\rangle$) goes down, and by the same formula the upper one
goes up ($E_m^{(2)}$ receives a positive contribution $+\vert
V_{m0}\vert^2/(E_m-E_0)$ from $\vert 0\rangle$). The off-diagonal coupling
**repels** levels — it never lets them cross, and it always increases the
ground state's separation from the manifold above it.

**(c) Variational connection.** The Rayleigh-Ritz variational principle states
that for any normalized trial state $\vert\psi\rangle$,

$$
E_0(\lambda) \le \langle\psi\vert\hat H(\lambda)\vert\psi\rangle,
$$

since the true ground energy is the minimum of the energy functional. Choose
the *unperturbed* ground state as the trial state, $\vert\psi\rangle=\vert
0\rangle$. Then

$$
\langle 0\vert\hat H(\lambda)\vert 0\rangle
= \langle 0\vert\hat H_0\vert 0\rangle + \lambda\langle 0\vert\hat V\vert 0\rangle
= E_0 + \lambda V_{00}
= E_0 + \lambda E_0^{(1)}.
$$

So the variational principle gives the exact bound

$$
E_0(\lambda) \le E_0 + \lambda E_0^{(1)}.
$$

On the other hand, the perturbative expansion is $E_0(\lambda) = E_0 + \lambda
E_0^{(1)} + \lambda^2 E_0^{(2)} + O(\lambda^3)$. Subtracting,

$$
\lambda^2 E_0^{(2)} + O(\lambda^3) \le 0.
$$

Dividing by $\lambda^2>0$ and letting $\lambda\to 0$ yields $E_0^{(2)}\le 0$
again — now as a corollary of the variational principle rather than by
inspecting the sum. The two viewpoints reinforce each other: $E_0 + \lambda
E_0^{(1)}$ is precisely the variational estimate obtained by *not letting the
state relax*, and the true ground energy can only sit lower. The gap between
the rigid first-order estimate and the truth is the second-and-higher-order
correction, which the bound forces to be non-positive. Level repulsion is the
energetic statement that "letting the ground state mix downhill always helps."

<!-- ─── -->

**5. Toy-model consistency check.** For $\hat H=\hat Z+\lambda \hat X$:

(a) compute $E_\pm^{(1)}$ and $E_\pm^{(2)}$ by perturbation theory,

(b) compute $\vert\pm^{(1)}\rangle$,

(c) compare with the exact expansion of $E_\pm(\lambda)=\pm\sqrt{1+\lambda^2}$ and comment on agreement order-by-order.

**Solution.**

Work in the $\hat Z$ eigenbasis $\{\vert 0\rangle,\vert 1\rangle\}$ with $\hat
Z\vert 0\rangle=+\vert 0\rangle$, $\hat Z\vert 1\rangle=-\vert 1\rangle$, so
$\hat H_0=\hat Z$ has $E_0=+1$, $E_1=-1$. The "$+$" branch is the one connected
to $\vert 0\rangle$ at $\lambda=0$, the "$-$" branch to $\vert 1\rangle$. The
perturbation is $\hat V=\hat X$, whose matrix elements are

$$
V_{00}=\langle 0\vert\hat X\vert 0\rangle = 0,
\quad
V_{11}=0,
\quad
V_{01}=V_{10}=1.
$$

**(a) Energies.** First order is the diagonal element:

$$
E_+^{(1)} = V_{00} = 0,
\qquad
E_-^{(1)} = V_{11} = 0.
$$

Second order is the single virtual term:

$$
E_+^{(2)} = \frac{\vert V_{10}\vert^2}{E_0-E_1} = \frac{1}{1-(-1)} = \frac{1}{2},
$$

$$
E_-^{(2)} = \frac{\vert V_{01}\vert^2}{E_1-E_0} = \frac{1}{-1-1} = -\frac{1}{2}.
$$

So perturbation theory predicts

$$
E_+(\lambda) = 1 + \tfrac{1}{2}\lambda^2 + O(\lambda^3),
\qquad
E_-(\lambda) = -1 - \tfrac{1}{2}\lambda^2 + O(\lambda^3).
$$

**(b) States.** The first-order correction is coupling over gap:

$$
\vert +^{(1)}\rangle = \vert 1\rangle\,\frac{V_{10}}{E_0-E_1} = \tfrac{1}{2}\vert 1\rangle,
$$

$$
\vert -^{(1)}\rangle = \vert 0\rangle\,\frac{V_{01}}{E_1-E_0} = -\tfrac{1}{2}\vert 0\rangle.
$$

Hence $\vert +(\lambda)\rangle = \vert 0\rangle + \tfrac{\lambda}{2}\vert
1\rangle + O(\lambda^2)$ and $\vert -(\lambda)\rangle = \vert 1\rangle -
\tfrac{\lambda}{2}\vert 0\rangle + O(\lambda^2)$.

**(c) Comparison with the exact result.** The exact energies are
$E_\pm(\lambda)=\pm\sqrt{1+\lambda^2}$. Taylor-expanding,

$$
\sqrt{1+\lambda^2} = 1 + \tfrac{1}{2}\lambda^2 - \tfrac{1}{8}\lambda^4 + O(\lambda^6),
$$

so $E_+ = 1 + \tfrac12\lambda^2 - \tfrac18\lambda^4+\cdots$ and $E_- = -1 -
\tfrac12\lambda^2 + \tfrac18\lambda^4-\cdots$. Matching order by order:

- $O(\lambda^0)$: exact $\pm 1$ equals the unperturbed $E_\pm^{(0)}$. ✓
- $O(\lambda^1)$: the exact expansion has **no** linear term, matching
  $E_\pm^{(1)}=0$. ✓
- $O(\lambda^2)$: exact coefficient $\pm\tfrac12$ equals $E_\pm^{(2)}$. ✓

For the states, the exact "$+$" eigenvector of $\hat H=\begin{pmatrix}1 &
\lambda\\\lambda & -1\end{pmatrix}$ is $\vert +(\lambda)\rangle =
\cos\tfrac\theta2\vert 0\rangle + \sin\tfrac\theta2\vert 1\rangle$ with
$\tan\theta=\lambda$. For small $\lambda$, $\theta=\lambda+O(\lambda^3)$, so
$\cos\tfrac\theta2 = 1+O(\lambda^2)$ and $\sin\tfrac\theta2 =
\tfrac\lambda2+O(\lambda^3)$, giving $\vert +(\lambda)\rangle = \vert 0\rangle +
\tfrac\lambda2\vert 1\rangle + O(\lambda^2)$ — exactly the perturbative result.
A numerical check confirms it: at $\lambda=0.3$ the exact eigenvalues are
$\pm1.04403$ while the truncation gives $\pm(1+\tfrac12(0.09))=\pm1.045$,
agreeing to better than $0.1\%$.

The agreement is **order-by-order**, and that is the whole point: perturbation
theory *is* the Taylor expansion of the exact answer, reconstructed without ever
diagonalizing $\hat H$. Each perturbative coefficient is the corresponding
Taylor coefficient; the only error is the truncation, here $O(\lambda^4)$,
because the model's parity (Sec. 5.1.1) kills all odd powers.

<!-- ─── -->

★ **6. Harmonic oscillator with linear perturbation.** Let

$$
\hat H_0=\hbar\omega\left(\hat a^\dagger \hat a+\frac12\right),
$$

$$
\hat V=\lambda \hat{x},
$$

$$
\hat{x}=\sqrt{\frac{\hbar}{2m\omega}}(\hat a+\hat a^\dagger).
$$

(a) Compute $V_{nn}$, $V_{n+1,n}$, $V_{n-1,n}$.

(b) Use non-degenerate perturbation theory to obtain $E_n$ up to second order.

(c) Solve the full Hamiltonian by completing the square and compare with perturbation theory.

**Solution.**

Write $x_0\equiv\sqrt{\hbar/2m\omega}$ for the oscillator length scale, so $\hat{x} = x_0(\hat a+\hat a^\dagger)$ and $\hat V=\lambda x_0(\hat a+\hat a^\dagger)$.
The unperturbed levels are $E_n=\hbar\omega(n+\tfrac12)$. Here $\hat V$ is the
*full* perturbation (it already contains $\lambda$), so the perturbative series
is organized in powers of $\lambda$ with $V_{mn}$ the matrix elements of
$\lambda x_0(\hat a+\hat a^\dagger)$.

**(a) Matrix elements.** Using $\hat a\vert n\rangle=\sqrt n\,\vert n-1\rangle$
and $\hat a^\dagger\vert n\rangle=\sqrt{n+1}\,\vert n+1\rangle$,

$$
V_{mn} = \langle m\vert\hat V\vert n\rangle
= \lambda x_0\left(\sqrt n\,\delta_{m,n-1} + \sqrt{n+1}\,\delta_{m,n+1}\right).
$$

The ladder operators have no diagonal part, so

$$
V_{nn} = 0,
\qquad
V_{n+1,n} = \lambda x_0\sqrt{n+1},
\qquad
V_{n-1,n} = \lambda x_0\sqrt{n}.
$$

$\hat{x}$ connects a level only to its immediate neighbors — the harmonic
oscillator's selection rule $\Delta n=\pm1$.

**(b) Energy to second order.** The first-order shift vanishes,
$E_n^{(1)}=V_{nn}=0$. The second-order sum has only the two neighbor terms:

$$
E_n^{(2)\text{-sum}}
= \frac{V_{n,n+1}V_{n+1,n}}{E_n-E_{n+1}} + \frac{V_{n,n-1}V_{n-1,n}}{E_n-E_{n-1}}.
$$

Since $\hat V$ is Hermitian and real here, $V_{n,n+1}=V_{n+1,n}=\lambda
x_0\sqrt{n+1}$ and $V_{n,n-1}=V_{n-1,n}=\lambda x_0\sqrt n$. The energy
denominators are $E_n-E_{n+1}=-\hbar\omega$ and $E_n-E_{n-1}=+\hbar\omega$.
Therefore

$$
E_n^{(2)\text{-sum}}
= \frac{\lambda^2 x_0^2(n+1)}{-\hbar\omega} + \frac{\lambda^2 x_0^2\,n}{+\hbar\omega}
= \frac{\lambda^2 x_0^2}{\hbar\omega}\big[-(n+1)+n\big]
= -\frac{\lambda^2 x_0^2}{\hbar\omega}.
$$

The $n$-dependence cancels: the upward neighbor ($\Delta n=+1$, negative
denominator) and the downward neighbor ($\Delta n=-1$, positive denominator)
contribute with opposite sign, and the difference is a constant. Substituting
$x_0^2=\hbar/2m\omega$,

$$
E_n = \hbar\omega\left(n+\tfrac12\right) - \frac{\lambda^2}{2m\omega^2} + O(\lambda^3).
$$

Every level drops by the *same* amount $\lambda^2/2m\omega^2$.

**(c) Exact solution by completing the square.** Restore the position-space
form $\hat H_0=\hat p^2/2m + \tfrac12 m\omega^2\hat{x}^2$, so the full
Hamiltonian is

$$
\hat H = \frac{\hat p^2}{2m} + \frac12 m\omega^2\hat{x}^2 + \lambda\hat{x}.
$$

Complete the square in the potential:

$$
\frac12 m\omega^2\hat{x}^2 + \lambda\hat{x}
= \frac12 m\omega^2\left(\hat{x}^2 + \frac{2\lambda}{m\omega^2}\hat{x}\right)
= \frac12 m\omega^2\left(\hat{x} + \frac{\lambda}{m\omega^2}\right)^2 - \frac{\lambda^2}{2m\omega^2}.
$$

Define the shifted operator $\hat{x}' = \hat{x} + \lambda/m\omega^2$. Shifting by
a c-number does not change the commutator, $[\hat{x}',\hat p]=[\hat{x},\hat p]=\mathrm{i}\hbar$, so $\hat{x}'$ and $\hat p$ are a perfectly good
canonical pair. In their terms,

$$
\hat H = \frac{\hat p^2}{2m} + \frac12 m\omega^2\hat{x}'^2 - \frac{\lambda^2}{2m\omega^2}.
$$

This is an identical harmonic oscillator — same mass, same $\omega$ — in the
displaced coordinate $\hat{x}'$, rigidly lowered by the constant
$\lambda^2/2m\omega^2$. Its exact spectrum is therefore

$$
E_n = \hbar\omega\left(n+\tfrac12\right) - \frac{\lambda^2}{2m\omega^2}.
$$

**Comparison.** The exact energies coincide with the second-order perturbative
result *with no remainder* — there is no $O(\lambda^3)$ term, and no correction
at any higher order. The reason is structural: $\hat H_0$ is quadratic in $\hat{x}$, and a linear perturbation only shifts the equilibrium position. Completing
the square shows the entire effect is (i) a displacement of the oscillator,
which changes no energy, and (ii) a constant offset that is exactly quadratic in
$\lambda$. Second-order perturbation theory captures the full $\lambda^2$
dependence, so for a linear perturbation of a harmonic oscillator it is not an
approximation — it is exact.

<!-- ─── -->

**7. Selection rules and parity.** For a 1D parity-symmetric potential with odd perturbation $\hat V=\lambda \hat{x}$:

(a) show $E_n^{(1)}=0$ for all $n$,

(b) identify which matrix elements contribute to $E_n^{(2)}$,

(c) explain how symmetry controls which virtual transitions are allowed.

**Solution.**

Let $\hat\Pi$ be the parity operator, $\hat\Pi\,\psi(x)=\psi(-x)$. A
parity-symmetric potential obeys $V_0(-x)=V_0(x)$, so $[\hat\Pi,\hat H_0]=0$.
Because the bound spectrum of a 1D potential is non-degenerate, every
unperturbed eigenstate is *also* an eigenstate of parity:

$$
\hat\Pi\,\vert n\rangle = \pi_n\,\vert n\rangle,
\qquad \pi_n = \pm 1,
$$

i.e. each $\psi_n(x)$ is either even or odd. The perturbation operator $\hat{x}$ is parity-odd: $\hat\Pi\,\hat{x}\,\hat\Pi^\dagger=-\hat{x}$ (equivalently
$\hat\Pi\hat{x}=-\hat{x}\hat\Pi$), since $\hat\Pi^\dagger=\hat\Pi$ and
$\hat\Pi^2=\hat 1$.

**(a) First-order shift vanishes.** $E_n^{(1)}=V_{nn}=\lambda\langle n\vert\hat{x}\vert n\rangle$. Insert $\hat\Pi^\dagger\hat\Pi=\hat 1$ on both sides of $\hat{x}$ and use the parity-odd property:

$$
\langle n\vert\hat{x}\vert n\rangle
= \langle n\vert\hat\Pi^\dagger\,(\hat\Pi\hat{x}\hat\Pi^\dagger)\,\hat\Pi\vert n\rangle
= \pi_n^*\,(-1)\,\pi_n\,\langle n\vert\hat{x}\vert n\rangle
= -\langle n\vert\hat{x}\vert n\rangle,
$$

using $\pi_n^*\pi_n=\pi_n^2=1$. A number equal to its own negative is zero, so
$\langle n\vert\hat{x}\vert n\rangle=0$ and hence

$$
E_n^{(1)} = 0 \quad\text{for all } n.
$$

In position language: $\vert\psi_n(x)\vert^2$ is even (parity eigenstate), so
$x\,\vert\psi_n(x)\vert^2$ is odd, and its integral over the symmetric domain
vanishes.

**(b) Which matrix elements feed $E_n^{(2)}$.** The second-order shift is
$E_n^{(2)}=\sum_{m\neq n}\vert V_{mn}\vert^2/(E_n-E_m)$ with
$V_{mn}=\lambda\langle m\vert\hat{x}\vert n\rangle$. Repeat the parity argument
for the *off-diagonal* element:

$$
\langle m\vert\hat{x}\vert n\rangle
= -\,\pi_m\pi_n\,\langle m\vert\hat{x}\vert n\rangle.
$$

If $\pi_m=\pi_n$ (same parity) the prefactor is $-1$ and the matrix element is
forced to zero; if $\pi_m=-\pi_n$ (opposite parity) the prefactor is $+1$ and
the element is unconstrained — generically nonzero. So **only opposite-parity
states contribute** to $E_n^{(2)}$:

$$
E_n^{(2)} = \sum_{\substack{m\neq n\\ \pi_m=-\pi_n}}\frac{\vert V_{mn}\vert^2}{E_n-E_m}.
$$

Half of the would-be sum — every same-parity intermediate state — drops out
before any integral is evaluated. (For the harmonic oscillator specifically the
ladder structure tightens this further to $m=n\pm1$, but the parity rule
$\pi_m=-\pi_n$ holds for *any* parity-symmetric potential.)

**(c) How symmetry controls virtual transitions.** Parity is a conserved
quantum number of the unperturbed problem: $[\hat\Pi,\hat H_0]=0$ means each
unperturbed level carries a definite parity label. A "virtual transition"
$n\to m$ in second-order perturbation theory is mediated by a *single* factor of
$\hat V\propto\hat{x}$. Because $\hat{x}$ is parity-odd, acting with it *flips*
the parity label. Therefore the only intermediate states $\vert m\rangle$ that
$\hat V$ can reach from $\vert n\rangle$ are those with the opposite parity;
transitions that would preserve parity have zero amplitude. The diagonal element
$V_{nn}$ vanishes for the same reason — it would require $\hat{x}$ to connect a
state to itself, i.e. to *not* flip parity, which a parity-odd operator cannot
do. This is the essence of a **selection rule**: a symmetry of $\hat H_0$,
together with the transformation property of $\hat V$ under that symmetry,
forbids entire classes of matrix elements *a priori*. One never has to compute
the suppressed integrals — symmetry guarantees they vanish, which is why
$E_n^{(1)}=0$ exactly and why only opposite-parity virtual states populate the
$E_n^{(2)}$ sum.

<!-- ─── -->

**8. Near-degeneracy and breakdown.** A 3-level system has unperturbed energies $E_1=0$, $E_2=\Delta$, $E_3=10\Delta$, with nonzero couplings $V_{12}$ and $V_{23}$.

(a) Write $E_1^{(2)}$ explicitly.

(b) Analyze $\Delta\to 0$ and identify which term causes the breakdown.

(c) Give the correct next-step method (basis choice and effective subspace treatment) instead of applying non-degenerate formulas blindly.

**Solution.**

The only nonzero off-diagonal couplings are $V_{12}$ (between levels 1 and 2)
and $V_{23}$ (between levels 2 and 3); in particular $V_{13}=0$, so level 1
couples *directly* only to level 2.

**(a) Second-order shift of level 1.** The general formula gives

$$
E_1^{(2)} = \sum_{m\neq 1}\frac{\vert V_{m1}\vert^2}{E_1-E_m}
= \frac{\vert V_{21}\vert^2}{E_1-E_2} + \frac{\vert V_{31}\vert^2}{E_1-E_3}.
$$

Since $V_{31}=0$, the second term drops, leaving the single contribution

$$
E_1^{(2)} = \frac{\vert V_{12}\vert^2}{E_1-E_2} = \frac{\vert V_{12}\vert^2}{0-\Delta} = -\frac{\vert V_{12}\vert^2}{\Delta}.
$$

**(b) The $\Delta\to0$ limit.** As $\Delta\to0$, levels 1 and 2 become
degenerate and

$$
E_1^{(2)} = -\frac{\vert V_{12}\vert^2}{\Delta}\;\longrightarrow\;-\infty.
$$

The divergence comes entirely from the **$m=2$ term**, whose energy denominator
$E_1-E_2=-\Delta$ vanishes. The state-mixing coefficient
$V_{12}/(E_1-E_2)=-V_{12}/\Delta$ diverges in the same way, so the perturbed
state $\vert 1(\lambda)\rangle$ is no longer a small correction to $\vert
1\rangle$. The level-3 term is harmless: its denominator $E_1-E_3=-10\Delta$
stays large relative to $V_{23}$ as long as $\Delta$ is not pathologically
small, and in any case $V_{13}=0$ removes it from $E_1^{(2)}$ outright. The
breakdown is local — it is the near-degenerate pair $\{1,2\}$, not the remote
level 3, that destroys the expansion. The formal symptom is exactly the one
flagged in the lecture: a coupling-over-gap ratio $\vert V_{12}\vert/\Delta$ of
order one or larger means the perturbative series no longer converges.

**(c) Correct next step — divide and conquer.** Do not push the non-degenerate
formulas through a vanishing denominator. Instead:

1. **Identify the (near-)degenerate subspace.** Group the levels whose
   mutual gaps are comparable to or smaller than their couplings. Here that is
   $\mathcal D=\mathrm{span}\{\vert 1\rangle,\vert 2\rangle\}$, because
   $\vert V_{12}\vert\gtrsim\Delta$. Level 3 stays *outside*: its gap
   $10\Delta$ to the pair is large compared with $V_{23}$.

2. **Diagonalize $\hat H$ exactly inside $\mathcal D$.** Treat the $2\times2$
   block

   $$
   \hat H_{\mathcal D} = \begin{pmatrix} E_1 & V_{12} \\ V_{21} & E_2 \end{pmatrix}
   = \begin{pmatrix} 0 & V_{12} \\ V_{12}^* & \Delta \end{pmatrix}
   $$

   without expanding in $V_{12}$. Its exact eigenvalues

   $$
   E_\pm = \frac{\Delta}{2} \pm \sqrt{\left(\frac{\Delta}{2}\right)^2 + \vert V_{12}\vert^2}
   $$

   are smooth and finite even at $\Delta=0$ (where $E_\pm=\pm\vert V_{12}\vert$).
   The eigenvectors of the block are the new "good" basis states — the correct
   zeroth-order states for the degenerate manifold. This is **degenerate
   perturbation theory**: diagonalize first within the troubled subspace, ask
   perturbative questions afterward.

3. **Fold in the remote level perturbatively.** Level 3 is well separated, so
   its coupling $V_{23}$ to the subspace is handled by ordinary non-degenerate
   perturbation theory — or, more systematically, by constructing an effective
   Hamiltonian on $\mathcal D$ (Löwdin downfolding / Schrieffer-Wolff) that
   projects level 3 out and adds corrections of order $\vert
   V_{23}\vert^2/(E-E_3)$. These denominators never vanish, so this part of the
   expansion is well-behaved.

In short: the appearance of a small denominator is not a failure of quantum
mechanics but a signal to *change basis*. Treat the resonant block exactly,
keep perturbation theory for the genuinely off-resonant couplings, and the
divergence disappears. This is precisely the program developed in Sec. 5.1.3.
