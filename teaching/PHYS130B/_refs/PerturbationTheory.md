# 130B Quantum Physics

Part 3. Perturbation Theory

## Time-Independent Perturbation

### A Toy Model of Qubit

#### General Ideas of Perturbation Theory

**Perturbation theory**: a set of *approximation* schemes that allows \
us to *extend* our knowledge about an *exactly solvable* quantum \
system to its *vicinity* (in the parameter space).

Why do we need perturbation theory?

* *Exact* solutions are *rare*. \[Implies] We have to rely on \
perturbation theory to go beyond exact solutions and make the most of \
them.

* *Separation* of *scales*: physics often takes place at different \
energy scales, e.g. \[Ellipsis] \[RightArrow] quarks (GeV) \
\[RightArrow] nucleus (MeV) \[RightArrow] atoms (eV) \[RightArrow] \
molecules (100meV) \[RightArrow] \[Ellipsis] \[Implies] We can refine \
our descriptions by adding *perturbative corrections* progressively.

What are the central problems in perturbation theory?

* **Time-independent perturbation**: given the *spectrum* \
(eigenstates and eigenenergies) of $$\\hat{H}_0$$, find the \
*spectrum* of $$\\hat{H}=\\hat{H}_0+\\lambda  \\hat{V}$$, in power \
series of $$\\lambda$$ (given that $$\\lambda$$ is small).

* **Time-dependent perturbation**: given the (bare) *propagator* \
$$\\hat{U}_0(t)=e^{-i \\hat{H}_0t}$$, find the *propagator*

```wl
$$\\hat{U}(t)=\\mathcal{T} \\exp \\left(-i \\int _0^tdt' \
\\hat{H}\\left(t'\\right)\\right),\\\\
\\hat{H}(t)=\\hat{H}_0+\\lambda  \\hat{V}(t),$$
```

in power series of \\[Lambda] (given that \\[Lambda] is small). [We \
will explain the notations in Eq. (XXX) later.]

How is perturbation theory useful?

* Conceptually: to establish effective Hamiltonians, to analyze \
renormalization group flows \[Ellipsis] (what theorists cares about)

* Practically: to calculate scattering amplitudes, response \
functions, spectral weights \[Ellipsis] (what experimentalists \
measures)

#### Qubit Model and its Exact Solution

Let us start with a toy model of a **single qubit**. Consider

```wl
$$\\hat{H}(\\lambda )=\\hat{H}_0+\\lambda  \\hat{V},$$
```

where $$\\hat{H}_0=\\hat{\\sigma }^z$$ and $$\\hat{V}=\\hat{\\sigma \
}^x$$, s.t. $$\\hat{H}(\\lambda )$$ can be more explicitly written as \
(in the $$\\{| 0\\rangle ,| 1\\rangle \\}$$ basis)

```wl
$$\\hat{H}(\\lambda )=\\hat{\\sigma }^z+\\lambda  \\hat{\\sigma }^x$$
$$\\bumpeq \\left(
\\begin{array}{cc}
 1 & \\lambda  \\\\
 \\lambda  & -1 \\\\
\\end{array}
\\right).$$
```

What are the eigenenergies and eigenstates of $$\\hat{H}(\\lambda )$$ ?

```wl
$$\\hat{H}(\\lambda )\\left| \\psi _{\\pm }(\\lambda )\\right\\rangle \
=E_{\\pm }(\\lambda )\\left| \\psi _{\\pm }(\\lambda )\\right\\rangle \
.$$
```

Exact solutions:

* Eigenenergies

```wl
$$E_{\\pm }(\\lambda )=\\pm \\sqrt{1+\\lambda ^2}.$$
```

* Eigenstates

```wl
$$\\left| \\psi _+(\\lambda )\\right\\rangle \
=\\frac{\\left(1+\\sqrt{1+\\lambda ^2}\\right)| 0\\rangle +\\lambda | \
1\\rangle }{\\sqrt{2\\left(1+\\lambda ^2+\\sqrt{1+\\lambda
^2}\\right)}},\\\\
\\left| \\psi _-(\\lambda )\\right\\rangle =\\frac{\\left(1+\\sqrt{1+\
\\lambda ^2}\\right)| 1\\rangle -\\lambda | 0\\rangle \
}{\\sqrt{2\\left(1+\\lambda ^2+\\sqrt{1+\\lambda
^2}\\right)}}.$$
```

#### Taylor Expansion

Assuming \\[Lambda] is small (i.e. \\[Lambda] \\[LessLess] 1), Eq. \
(XXX) and Eq. (XXX) can be expanded in power series of \\[Lambda]

* As a reminder, the **Taylor expansion** of a function $$f(\\lambda \
)$$ is given by

```wl
$$f(\\lambda )=\\sum _{k=0}^{\\infty } \\frac{\\partial _{\\lambda \
}^kf(0)}{k!}\\lambda ^k$$
$$=f(0)+f'(0)\\lambda +\\frac{f^{\\prime\\prime }(0)}{2}\\lambda \
^2+\\frac{f^{(3)}(0)}{6}\\lambda ^3+\\ldots .$$
```

* Applying Eq. (XXX) to Eq. (XXX) and Eq. (XXX), we get

```wl
$$E_{\\pm }=\\pm \\left(1+\\frac{\\lambda ^2}{2}-\\frac{\\lambda \
^4}{8}+\\ldots \\right),$$

$$\\left| \\psi _+(\\lambda )\\right\\rangle =| 0\\rangle \
+\\frac{\\lambda }{2}| 1\\rangle -\\frac{\\lambda ^2}{8}| 0\\rangle -\
\\frac{3 \\lambda ^3}{16}| 1\\rangle
+\\frac{11 \\lambda ^4}{128}| 0\\rangle +\\ldots ,\\\\
\\left| \\psi _-(\\lambda )\\right\\rangle =| 1\\rangle \
-\\frac{\\lambda }{2}| 0\\rangle -\\frac{\\lambda ^2}{8}| 1\\rangle +\
\\frac{3 \\lambda ^3}{16}| 0\\rangle
+\\frac{11 \\lambda ^4}{128}| 1\\rangle +\\ldots .$$
```

Goal: obtain these power series *without* first calculating the exact \
solution! - This can be done as long as we know how to evaluate the \
**derivatives** $$\\partial _{\\lambda }^nE(0)$$ and $$\\partial \
_{\\lambda }^n\\left| \\psi _{\\pm }(0)\\right\\rangle$$.

The **perturbation theory** is essentially an *iterative algorithm* \
to calculate these derivatives *order by order*, based on our \
knowledge about $$\\hat{H}_0$$ and $$\\hat{V}$$.

### Non-Degenerate Perturbation Theory

#### Problem Setup

The starting point is the following Hamiltonian (*linearly* \
parameterized by $$\\lambda$$)

```wl
$$\\hat{H}(\\lambda )=\\hat{H}_0+\\lambda  \\hat{V}.$$
```

* This implies

```wl
$$\\hat{H}(0)=\\hat{H}_0,\\\\
\\partial _{\\lambda }\\hat{H}(0)=\\hat{V},\\\\
\\partial _{\\lambda }^2\\hat{H}(0)=\\partial _{\\lambda \
}^3\\hat{H}(0)=\\ldots =0.$$
```

* To simplify the notation, we will suppress the argument \
$$\\lambda$$ if it is evaluated at $$\\lambda =0$$.

```wl
$$\\hat{H}=\\hat{H}_0,\\\\
\\partial _{\\lambda }\\hat{H}=\\hat{V},\\\\
\\partial _{\\lambda }^2\\hat{H}=\\partial _{\\lambda \
}^3\\hat{H}=\\ldots =0.$$
```

Rule: Everything depends on $$\\lambda$$. But if the dependence on $$\
\\lambda$$ is not spelt out explicitly, we assume it to be the \
evaluated at $$\\lambda =0$$, i.e. $$\\hat{H}\\equiv \
\\hat{H}|_{\\lambda =0}=\\hat{H}(0)$$.

Consider the **eigen equation**

```wl
$$\\hat{H}(\\lambda )| n(\\lambda )\\rangle =E_n(\\lambda )| \
n(\\lambda )\\rangle .$$
```

For each given $$\\lambda$$, there is a different $$\\hat{H}(\\lambda \
)$$, and hence a different set of $$E_n(\\lambda )$$ and $$| \
n(\\lambda )\\rangle$$, labeled by $$n=1,2,3,\\ldots$$.

* $$E_n(\\lambda )$$ is the $$n$$th energy level. It is a real number \
depending on $$\\lambda$$.

* $$| n(\\lambda )\\rangle$$ is the $$n$$th eigenstate (in \
correspondence to $$E_n(\\lambda )$$). It is a state vector in the \
Hilbert space that can change with $$\\lambda$$. Note: The notation \
$$| n(\\lambda )\\rangle$$ does *not* imply that the index $$n$$ is \
$$\\lambda$$ dependent, it should be understood as

```wl
$$| n(\\lambda )\\rangle =\\sum _m \\psi _{n\\, m}(\\lambda )| \
m\\rangle .$$
```

We assume a *discrete* spectrum *without degeneracy*, such that the \
\[OpenCurlyDoubleQuote]$$n$$th\[CloseCurlyDoubleQuote] level/state is \
*uniquely* defined. [The case with degeneracy will be discussed \
latter.]

Statement of the problem: suppose we know

* the eigenenergies and eigenstates *at and only at* $$\\lambda =0$$,

```wl
$$\\hat{H}| n\\rangle =E_n| n\\rangle ,$$
```

* and what the perturbation is: $$\\hat{V}=\\partial _{\\lambda \
}\\hat{H}$$,

```wl
$$V_{m\\, n}=\\langle m| \\hat{V}| n\\rangle =\\langle m| \\partial \
_{\\lambda }\\hat{H}| n\\rangle ,$$
```

we want to calculate $$E_n(\\lambda )$$ and $$| n(\\lambda \
)\\rangle$$ in power series of $$\\lambda$$ (to any desired order) in \
terms of $$E_n$$, $$V_{m\\, n}$$ and $$| n\\rangle$$ (at $$\\lambda \
=0$$).

#### Hellmann-Feynman Theorems

* Applying $$\\partial _{\\lambda }$$ to both sides of $$\\hat{H}| \
n\\rangle =E_n| n\\rangle$$,

```wl
$$\\partial _{\\lambda }\\hat{H}| n\\rangle +\\hat{H}\\left| \
\\partial _{\\lambda }n\\right\\rangle =\\partial _{\\lambda }E_n| \
n\\rangle +E_n\\left| \\partial
_{\\lambda }n\\right\\rangle .$$
```

	* Note: $$\\left| \\partial _{\\lambda }n\\right\\rangle$$ stands \
for the derivative of the state $$| n\\rangle$$ (not the index $$n$$)

```wl
$$\\left| \\partial _{\\lambda }n\\right\\rangle \\equiv \\partial _{\
\\lambda }| n\\rangle =\\left(\\sum _m \\partial _{\\lambda }\\psi \
_{n\\, m}(\\lambda )| m\\rangle
\\right)_{\\lambda =0}.$$
```

It does *not* imply that the integer index $$n$$ can be differentiated.

* Overlap with $$\\langle m|$$ from the left,

```wl
$$\\langle m| \\partial _{\\lambda }\\hat{H}| n\\rangle +\\langle m| \
\\hat{H}\\left| \\partial _{\\lambda }n\\right\\rangle =\\partial \
_{\\lambda }E_n\\langle m|n\\rangle
+E_n\\langle m|\\partial _{\\lambda }n\\rangle .$$
```

Using $$\\langle m| \\hat{H}=\\langle m| E_m$$,

```wl
$$\\langle m| \\partial _{\\lambda }\\hat{H}| n\\rangle +E_m\\langle \
m|\\partial _{\\lambda }n\\rangle =\\partial _{\\lambda }E_n\\langle \
m|n\\rangle +E_n\\langle
m|\\partial _{\\lambda }n\\rangle$$
$$\\Rightarrow \\langle m| \\partial _{\\lambda }\\hat{H}| n\\rangle \
=\\partial _{\\lambda }E_n\\langle m|n\\rangle \
+\\left(E_n-E_m\\right)\\langle m|\\partial
_{\\lambda }n\\rangle .$$
```

* Note that $$\\partial _{\\lambda }\\hat{H}=\\hat{V}$$ and \
$$\\langle m|n\\rangle =\\delta _{m\\, n}$$,

```wl
$$V_{m\\, n}=\\langle m| \\hat{V}| n\\rangle =\\partial _{\\lambda \
}E_n\\delta _{m\\, n}+\\left(E_n-E_m\\right)\\langle m|\\partial \
_{\\lambda }n\\rangle .$$
```

This establishes a relation between the matrix element $$V_{m\\, n}$$ \
(of the perturbation) and the derivatives $$\\partial _{\\lambda \
}E_n$$ and $$\\left| \\partial _{\\lambda }n\\right\\rangle$$.

* When m = n, Eq. (XXX) implies

```wl
$$\\partial _{\\lambda }E_n=V_{n\\, n}.$$
```

This is the **first Hellmann-Feynman** theorem.

* When m != n, Eq. (XXX) implies

```wl
$$\\langle m|\\partial _{\\lambda }n\\rangle =\\frac{V_{m\\, \
n}}{E_n-E_m},\\\\
\\left\\langle \\partial _{\\lambda }m\\right|n\\rangle \
=\\frac{V_{m\\, n}}{E_m-E_n}.$$
```

This is the **second Hellmann-Feynman** theorem. Tip: the **energy \
denominator** is always given by the energy of the state that is \
being *differentiated* minus the energy of the other state.

The **Hellmann-Feynman theorems** tell us how the **derivative** of \
the *energy* $$\\partial _{\\lambda }E_n$$ or the *state* $$\\left| \
\\partial _{\\lambda }n\\right\\rangle$$ and $$\\left\\langle \
\\partial _{\\lambda }m\\right|$$ can be expressed in terms of \
$$E_n$$ and $$V_{m\\, n}$$ which do not contain $$\\partial \
_{\\lambda }$$. \[Implies] This effectively *reduces* the order of $$\
\\partial _{\\lambda }$$ by one. \[Implies] Applying them \
*iteratively*, we will be able to calculate the derivatives **to any \
order** for both energies and states, which are all we need to \
construct the power series of the *perturbative expansion*.

#### Energy Corrections

According to the Taylor expansion,

```wl
$$E_n(\\lambda )=\\sum _{k=0}^{\\infty } \\frac{\\partial _{\\lambda \
}^kE_n}{k!}\\lambda ^k=E_n+\\left(\\partial _{\\lambda \
}E_n\\right)\\lambda +\\frac{1}{2}\\left(\\partial
_{\\lambda }^2E_n\\right)\\lambda ^2+\\ldots .$$
```

Applying Hellmann-Feynman theorems, the energy derivatives are

```wl
$$\\partial _{\\lambda }E_n=V_{n\\, n},\\\\
\\partial _{\\lambda }^2E_n=2\\sum _{m\\neq n} \\frac{V_{n\\, \
m}V_{m\\, n}}{E_n-E_m},\\\\
\\ldots$$
```

Evaluate Eq. (XXX).

* The 1st order derivative is directly given by the first \
Hellmann-Feynman theorem Eq. (XXX):

```wl
$$\\partial _{\\lambda }E_n=V_{n\\, n}=\\langle n| \\partial \
_{\\lambda }\\hat{H}| n\\rangle .$$
```

* Continue to evaluate the 2nd order derivative:

```wl
$$\\partial _{\\lambda }^2E_n=\\partial _{\\lambda }\\langle n| \
\\partial _{\\lambda }\\hat{H}| n\\rangle$$
$$=\\left\\langle \\partial _{\\lambda }n\\right| \\partial \
_{\\lambda }\\hat{H}| n\\rangle +\\langle n| \\partial _{\\lambda }^2\
\\hat{H}| n\\rangle +\\langle n|
\\partial _{\\lambda }\\hat{H}\\left| \\partial _{\\lambda \
}n\\right\\rangle .$$
```

Note that \\!\\(
\\*SubsuperscriptBox[\\(\\[PartialD]\\), \\(\\[Lambda]\\), \\(2\\)]
\\*OverscriptBox[\\(H\\), \\(^\\)]\\) = 0 according to the setup in \
Eq. (XXX), so all we need to calculate is the following

```wl
$$\\partial _{\\lambda }^2E_n=\\left\\langle \\partial _{\\lambda \
}n\\right| \\partial _{\\lambda }\\hat{H}| n\\rangle +\\langle n| \
\\partial _{\\lambda }\\hat{H}\\left|
\\partial _{\\lambda }n\\right\\rangle .$$
```

	* The key step is to insert the resolution of identity $$\\sum _m | \
m\\rangle \\langle m| =\\mathbf{1}$$ :

```wl
$$\\partial _{\\lambda }^2E_n=\\sum _m \\left(\\left\\langle \
\\partial _{\\lambda }n\\right|m\\rangle \\langle m| \\partial \
_{\\lambda }\\hat{H}| n\\rangle +\\langle
n| \\partial _{\\lambda }\\hat{H}| m\\rangle \\langle m|\\partial \
_{\\lambda }n\\rangle \\right)$$
$$=\\sum _m \\left(\\frac{V_{n\\, m}}{E_n-E_m}V_{m\\, n}+V_{n\\, \
m}\\frac{V_{m\\, n}}{E_n-E_m}\\right)$$
$$=2\\sum _m \\frac{V_{n\\, m}V_{m\\, n}}{E_n-E_m}.$$
```

But, wait a moment \\[Ellipsis] The energy denominator diverges when \
m = n, what is wrong? - Note that Eq. (XXX) only holds for m != n, so \
we must be careful.

	* Let us be more careful with $$m,n$$ summation this time

```wl
$$\\partial _{\\lambda }^2E_n=\\sum _m \\left(\\left\\langle \
\\partial _{\\lambda }n\\right|m\\rangle \\langle m| \\partial \
_{\\lambda }\\hat{H}| n\\rangle +\\langle
n| \\partial _{\\lambda }\\hat{H}| m\\rangle \\langle m|\\partial \
_{\\lambda }n\\rangle \\right)$$
$$=\\sum _{m\\neq n} \\left(\\left\\langle \\partial _{\\lambda \
}n\\right|m\\rangle \\langle m| \\partial _{\\lambda }\\hat{H}| \
n\\rangle +\\langle n| \\partial
_{\\lambda }\\hat{H}| m\\rangle \\langle m|\\partial _{\\lambda \
}n\\rangle \\right)+\\left(\\left\\langle \\partial _{\\lambda \
}n\\right|n\\rangle \\langle n| \\partial
_{\\lambda }\\hat{H}| n\\rangle +\\langle n| \\partial _{\\lambda \
}\\hat{H}| n\\rangle \\langle n|\\partial _{\\lambda }n\\rangle \
\\right)$$
$$=2\\sum _{m\\neq n} \\frac{V_{n\\, m}V_{m\\, n}}{E_n-E_m}+V_{n\\, \
n}\\left(\\left\\langle \\partial _{\\lambda }n\\right|n\\rangle \
+\\langle n|\\partial _{\\lambda
}n\\rangle \\right)$$
$$=2\\sum _{m\\neq n} \\frac{V_{n\\, m}V_{m\\, n}}{E_n-E_m}+V_{n\\, \
n}\\partial _{\\lambda }\\langle n|n\\rangle .$$
```

Given that $$\\langle n|n\\rangle =1$$, taking $$\\partial _{\\lambda \
}$$ on both sides, $$\\partial _{\\lambda }\\langle n|n\\rangle \
=\\partial _{\\lambda }1=0$$.

So we arrive at the desired result

```wl
$$\\partial _{\\lambda }^2E_n=2\\sum _{m\\neq n} \\frac{V_{n\\, \
m}V_{m\\, n}}{E_n-E_m}.$$
```

so the perturbative correction to the eigenenergy is given by

```wl
$$E_n(\\lambda )=E_n+V_{n\\, n}\\lambda +\\sum _{m\\neq n} \
\\frac{V_{n\\, m}V_{m\\, n}}{E_n-E_m}\\lambda ^2+\\ldots .$$
```

#### State Corrections

According to the Taylor expansion,

```wl
$$| n(\\lambda )\\rangle =\\sum _{k=0}^{\\infty } \\frac{\\left| \
\\partial _{\\lambda }^kn\\right\\rangle }{k!}\\lambda ^k=| n\\rangle \
+\\left| \\partial _{\\lambda
}n\\right\\rangle \\lambda +\\frac{1}{2}\\left| \\partial _{\\lambda \
}^2n\\right\\rangle \\lambda ^2+\\ldots .$$
```

Applying Hellmann-Feynman theorems, the state derivatives are

```wl
$$\\left| \\partial _{\\lambda }n\\right\\rangle =\\sum _{m\\neq n} | \
m\\rangle \\frac{V_{m\\, n}}{E_n-E_m},\\\\
\\left| \\partial _{\\lambda }^2n\\right\\rangle =\\sum _{m\\neq n} \
\\left(\\sum _{l\\neq n} 2| m\\rangle \\frac{V_{m\\, l}V_{l\\, \
n}}{\\left(E_n-E_m\\right)\\left(E_n-E_l\\right)}-2|
m\\rangle \\frac{V_{m\\, n}V_{n\\, n}}{\\left(E_n-E_m\\right){}^2}-| \
n\\rangle \\frac{V_{n\\, m}V_{m\\, \
n}}{\\left(E_n-E_m\\right){}^2}\\right),\\\\
\\ldots$$
```

Evaluate Eq. (XXX).

By Eq. (XXX), we know the 1st order derivative is

```wl
$$\\left| \\partial _{\\lambda }n\\right\\rangle =\\sum _{m\\neq n} | \
m\\rangle \\langle m|\\partial _{\\lambda }n\\rangle =\\sum _{m\\neq \
n} | m\\rangle \\frac{V_{m\\,
n}}{E_n-E_m}.$$
```

Let us continue to calculate the 2nd order derivative [Please bear \
with me ...]

```wl
$$\\left| \\partial _{\\lambda }^2n\\right\\rangle =\\partial \
_{\\lambda }\\sum _{m\\neq n} | m\\rangle \\frac{\\langle m| \
\\partial _{\\lambda }\\hat{H}| n\\rangle
}{E_n-E_m}$$
$$=\\sum _{m\\neq n} \\left(\\left| \\partial _{\\lambda \
}m\\right\\rangle \\frac{\\langle m| \\partial _{\\lambda }\\hat{H}| \
n\\rangle }{E_n-E_m}+| m\\rangle \\frac{\\left\\langle
\\partial _{\\lambda }m\\right| \\partial _{\\lambda }\\hat{H}| \
n\\rangle }{E_n-E_m}+| m\\rangle \\frac{\\langle m| \\partial \
_{\\lambda }\\hat{H}\\left| \\partial
_{\\lambda }n\\right\\rangle }{E_n-E_m}-| m\\rangle \\frac{\\langle \
m| \\partial _{\\lambda }\\hat{H}| n\\rangle \
}{\\left(E_n-E_m\\right){}^2}\\left(\\partial
_{\\lambda }E_n-\\partial _{\\lambda }E_m\\right)\\right)$$
$$=\\sum _{m\\neq n} \\left(\\sum _{l\\neq m} | l\\rangle \\frac{V_{l\
\\, m}}{E_m-E_l}\\frac{V_{m\\, n}}{E_n-E_m}+\\sum _{l\\neq m} | \
m\\rangle \\frac{V_{m\\, l}}{E_m-E_l}\\frac{V_{l\\,
n}}{E_n-E_m}+\\sum _{l\\neq n} | m\\rangle \\frac{V_{m\\, \
l}}{E_n-E_m}\\frac{V_{l\\, n}}{E_n-E_l}-| m\\rangle \\frac{V_{m\\, \
n}}{\\left(E_n-E_m\\right){}^2}\\left(V_{n\\,
n}-V_{m\\, m}\\right)\\right)$$
```

Push $$l=m$$ or $$l=n$$ terms out of the summation, so as to combine \
the first three summations under $$\\sum _{l\\neq m,n}$$ (sum over \
$$l$$ excluding both $$m$$ and $$n$$),

```wl
$$\\left| \\partial _{\\lambda }^2n\\right\\rangle =\\sum _{m\\neq n} \
\\left(\\sum _{l\\neq m,n} \\left(| l\\rangle \\frac{V_{l\\, \
m}}{E_m-E_l}\\frac{V_{m\\, n}}{E_n-E_m}+|
m\\rangle \\frac{V_{m\\, l}}{E_m-E_l}\\frac{V_{l\\, n}}{E_n-E_m}+| \
m\\rangle \\frac{V_{m\\, l}}{E_n-E_m}\\frac{V_{l\\, \
n}}{E_n-E_l}\\right)+| n\\rangle \\frac{V_{n\\,
m}}{E_m-E_n}\\frac{V_{m\\, n}}{E_n-E_m}+\\right.\\\\
\\left.| m\\rangle \\frac{V_{m\\, n}}{E_m-E_n}\\frac{V_{n\\, \
n}}{E_n-E_m}+| m\\rangle \\frac{V_{m\\, m}}{E_n-E_m}\\frac{V_{m\\, \
n}}{E_n-E_m}-| m\\rangle \\frac{V_{m\\,
n}V_{n\\, n}}{\\left(E_n-E_m\\right){}^2}+| m\\rangle \\frac{V_{m\\, \
n}V_{m\\, m}}{\\left(E_n-E_m\\right){}^2}\\right)$$
$$=\\sum _{m\\neq n} \\left(\\sum _{l\\neq m,n} \\left(| l\\rangle \
\\frac{V_{l\\, m}}{E_m-E_l}\\frac{V_{m\\, n}}{E_n-E_m}+| m\\rangle \
\\frac{V_{m\\, l}}{E_m-E_l}\\frac{V_{l\\,
n}}{E_n-E_m}+| m\\rangle \\frac{V_{m\\, l}}{E_n-E_m}\\frac{V_{l\\, \
n}}{E_n-E_l}\\right)-\\right.\\\\
\\left.| n\\rangle \\frac{V_{n\\, m}V_{m\\, \
n}}{\\left(E_n-E_m\\right){}^2}-2| m\\rangle \\frac{V_{m\\, n}V_{n\\, \
n}}{\\left(E_n-E_m\\right){}^2}+2| m\\rangle
\\frac{V_{m\\, n}V_{m\\, m}}{\\left(E_n-E_m\\right){}^2}\\right)$$
```

The double summation 
\\!\\(\\*UnderscriptBox[\\(\\[Sum]\\), \\(m \\[NotEqual] n\\)]\\)
\\!\\(\\*UnderscriptBox[\\(\\[Sum]\\), \\(l \\[NotEqual] m, n\\)]\\) \
means to sum over l and m, under the constraint that l, m, n are \
mutually exclusive. The summation is symmetric under the exchange of \
l and m. So for the first term in Eq. (XXX),

```wl
$$\\sum _{m\\neq n} \\sum _{l\\neq m,n} | l\\rangle \\frac{V_{l\\, \
m}}{E_m-E_l}\\frac{V_{m\\, n}}{E_n-E_m}=\\sum _{m\\neq n} \\sum \
_{l\\neq m,n} | m\\rangle \\frac{V_{m\\,
l}}{E_l-E_m}\\frac{V_{l\\, n}}{E_n-E_l},$$
```

therefore

```wl
$$\\left| \\partial _{\\lambda }^2n\\right\\rangle =\\sum _{m\\neq n} \
\\left(\\sum _{l\\neq m,n} | m\\rangle V_{m\\, l}V_{l\\, \
n}\\left(\\frac{1}{\\left(E_l-E_m\\right)\\left(E_n-E_l\\right)}+\\\
frac{1}{\\left(E_m-E_l\\right)\\left(E_n-E_m\\right)}+\\frac{1}{\\\
left(E_n-E_m\\right)\\left(E_n-E_l\\right)}\\right)-\\right.\\\\
\\left.| n\\rangle \\frac{V_{n\\, m}V_{m\\, \
n}}{\\left(E_n-E_m\\right){}^2}-2| m\\rangle \\frac{V_{m\\, n}V_{n\\, \
n}}{\\left(E_n-E_m\\right){}^2}+2| m\\rangle
\\frac{V_{m\\, n}V_{m\\, m}}{\\left(E_n-E_m\\right){}^2}\\right)$$
$$=\\sum _{m\\neq n} \\left(\\sum _{l\\neq m,n} 2| m\\rangle \
\\frac{V_{m\\, l}V_{l\\, \
n}}{\\left(E_n-E_m\\right)\\left(E_n-E_l\\right)}-| n\\rangle \
\\frac{V_{n\\,
m}V_{m\\, n}}{\\left(E_n-E_m\\right){}^2}-2| m\\rangle \\frac{V_{m\\, \
n}V_{n\\, n}}{\\left(E_n-E_m\\right){}^2}+2| m\\rangle \\frac{V_{m\\, \
n}V_{m\\, m}}{\\left(E_n-E_m\\right){}^2}\\right)$$
```

Finally we absorb the last term to the summation $$\\sum _{l=m,n}$$ \
to eliminate the constraint of $$l\\neq m$$,

```wl
$$\\left| \\partial _{\\lambda }^2n\\right\\rangle =\\sum _{m\\neq n} \
\\left(\\sum _{l\\neq n} 2| m\\rangle \\frac{V_{m\\, l}V_{l\\, \
n}}{\\left(E_n-E_m\\right)\\left(E_n-E_l\\right)}-2|
m\\rangle \\frac{V_{m\\, n}V_{n\\, n}}{\\left(E_n-E_m\\right){}^2}-| \
n\\rangle \\frac{V_{n\\, m}V_{m\\, \
n}}{\\left(E_n-E_m\\right){}^2}\\right).$$
```

so the perturbative correction to the eigenstate is given by

```wl
$$| n(\\lambda )\\rangle =| n\\rangle +\\sum _{m\\neq n} | m\\rangle \
\\frac{V_{m\\, n}}{E_n-E_m}\\lambda +\\left(\\sum _{m\\neq n} \\sum \
_{l\\neq n} | m\\rangle
\\frac{V_{m\\, l}V_{l\\, \
n}}{\\left(E_n-E_m\\right)\\left(E_n-E_l\\right)}-\\sum _{m\\neq n} | \
m\\rangle \\frac{V_{m\\, n}V_{n\\, \
n}}{\\left(E_n-E_m\\right){}^2}-\\frac{1}{2}\\sum
_{m\\neq n} | n\\rangle \\frac{V_{n\\, m}V_{m\\, \
n}}{\\left(E_n-E_m\\right){}^2}\\right)\\lambda ^2+\\ldots .$$
```

Following this procedure, one can calculate the perturbative \
correction order by order. Higher order results can be found on \
Wikipedia under [Perturbation Theory (Quantum \
Mechanics)](https://en.wikipedia.org/wiki/Perturbation_theory_(\
quantum_mechanics)).

#### Summary of Results

Sometimes, it is simpler to redefine $$\\lambda  \\hat{V}$$ as \
$$\\hat{V}$$

```wl
$$\\hat{H}(\\lambda )=\\hat{H}_0+\\lambda  \\hat{V}\\rightarrow \
\\hat{H}_0+\\hat{V}.$$
```

Rule: whenever we encounter $$\\lambda  V_{m\\, n}$$ we rewrite it as \
$$V_{m\\, n}$$.

Instead of thinking that the *parameter* $$\\lambda$$ is small, we \
can think that the *operator* $$\\hat{V}$$ is small (i.e. all matrix \
elements $$V_{m\\, n}\\to 0$$ uniformly). The perturbative \
corrections are actually in power series of $$\\hat{V}$$,

```wl
$$E_n(V)=E_n+V_{n\\, n}+\\sum _{m\\neq n} \\frac{V_{n\\, m}V_{m\\, \
n}}{E_n-E_m}+\\ldots ,\\\\
| n(V)\\rangle =| n\\rangle +\\sum _{m\\neq n} | m\\rangle \
\\frac{V_{m\\, n}}{E_n-E_m}+\\ldots .$$
```

To summarize, given the unperturbed Hamiltonian $$\\hat{H}_0$$ and \
the perturbation $$\\hat{V}$$ (represented in the eigenbasis of \
$$\\hat{H}_0$$),

```wl
$$\\hat{H}_0=\\sum _n | n\\rangle E_n\\langle n| , \\hat{V}=\\sum \
_{m,n} | m\\rangle V_{m\\, n}\\langle n| ,$$
```

the **perturbation theory** allows us to construct the *spectral \
decomposition* of the *perturbed* Hamiltonian $$\\hat{H}_0+\\hat{V}$$ \
(i.e. its corrected eigenenergies and eigenstates)

```wl
$$\\hat{H}_0+\\hat{V}=\\sum _n | n(V)\\rangle E_n(V)\\langle n(V)| \
.$$
```

#### Physical Intuitions

In matrix form, $$\\hat{H}_0$$ is diagonal in its eigenbasis, but \
$$\\hat{V}$$ is not.

```wl
$$\\hat{H}_0+\\hat{V}\\bumpeq \\left(
\\begin{array}{ccccc}
   & \\vdots  &   & \\vdots  &   \\\\
 \\cdots  & E_n+V_{n\\, n} & \\cdots  & V_{n\\, m} & \\cdots  \\\\
   & \\vdots  &   & \\vdots  &   \\\\
 \\cdots  & V_{m\\, n} & \\cdots  & E_m+V_{m\\, m} & \\cdots  \\\\
   & \\vdots  &   & \\vdots  &   \\\\
\\end{array}
\\right),$$
```

we will need to **re-diagonalize** the new Hamiltonian \
$$\\hat{H}_0+\\hat{V}$$. But if the off-diagonal elements are weak \
($$V\\rightarrow 0$$), $$\\hat{H}_0+\\hat{V}$$ is *close to* \
diagonal, such that re-diagonalization only requires a small effort, \
that is why the new eigenenergies and eigenstates can be obtained \
from *perturbative corrections* based on eigensystem of $$\\hat{H}_0$$.

* To the 1st order, $$E_n(V)$$ simply takes out the *diagonal* matrix \
element of $$\\hat{H}_0+\\hat{V}$$, which amounts to re-evaluating \
the **energy expectation value** on the old eigenstate $$| \
n\\rangle$$ :

```wl
$$E_n+V_{n\\, n}=\\langle n| \\hat{H}_0+\\hat{V}| n\\rangle .$$
```

* **State hybridization**: the 1st order correction of $$| \
n(V)\\rangle$$ *hybridizes* (mixes) the original state $$| \
n\\rangle$$ with all the other $$| m\\rangle$$ states that are \
*connected* to $$| n\\rangle$$ by non-vanishing $$V_{m\\, n}$$.

```wl
$$| n(V)\\rangle =| n\\rangle +\\sum _{m\\neq n} | m\\rangle \
\\frac{V_{m\\, n}}{E_n-E_m}$$
```

The **hybridization coefficient** is

	* proportional to the **transition rate** $$V_{m\\, n}$$,

	* inversely proportional to the energy **level spacing** \
$$\\left(E_n-E_m\\right)$$.

```wl
In[337]:=
Row[Block[{a = 0.5, En = 0, Em = #, lev}, 
	lev[id_] := {Line[{#, 0}& /@ { - a, a}], Text[\"\
\\!\\(\[LeftBracketingBar]\" <> id <> \"\[RightAngleBracket]\\)\", \
{0, 0}, {0,  - 1}], Text[\"\\!\\(E\\_\" <> id <> \"\\)\", {a, 0}, { - \
1.5, 0}]};
	Graphics[{Translate[lev[\"n\"], { - 1, En}], Translate[lev[\"m\"], \
{1, Em}], {Arrowheads[{{0.1, 0.5}}], Dashed, AbsoluteThickness[1], \
Arrow[{{ - 1 + a, En}, {1 - a, Em}}]}, Text[V
 m\[VeryThinSpace]n, {0, (En + Em) / 2}, { - 1.2Sign[#], 0}]}, \
ImageSize -> 100]]& /@ {2,  - 2}, Spacer[20]]

Out[337]=
\\!\\(\\*GraphicsBox[{GeometricTransformationBox[{LineBox[{{-0.5, 0}, \
{0.5, 0}}], 
    InsetBox[FormBox[\"\\\"\\\\!\\\\(\[LeftBracketingBar]n\
\[RightAngleBracket]\\\\)\\\"\", TraditionalForm], {0, 0}, {0, -1}], 
    InsetBox[FormBox[\"\\\"\\\\!\\\\(E\\\\_n\\\\)\\\"\", \
TraditionalForm], {0.5, 0}, {-1.5, 0}]}, {-1, 0}] ...  {-1.5, 0}]}, \
{1, -2}], 
  {Arrowheads[{{0.1, 0.5}}], Dashing[{Small, Small}], \
AbsoluteThickness[1], 
   ArrowBox[{{-0.5, 0}, {0.5, -2}}]}, \
InsetBox[FormBox[\"\\\"\\\\!\\\\(V\\\\_\\\\(m\[VeryThinSpace]n\\\\)\\\
\\)\\\"\", 
    TraditionalForm], {0, -1}, {1.2, 0}]}, ImageSize -> 100]\\)
```

	* When $$E_n-E_m\\to 0$$ (energy levels become degenerated) \
\[Implies] the hybridization coefficient diverges \[Implies] \
signifies the breakdown of the non-degenerate perturbation theory. \
This scenario is called a **level resonance**.

* **Level repulsion**: the 2nd order energy correction always repel \
the levels apart (by making the higher level higher and the lower \
level lower).

```wl
$$E_n+\\sum _m \\frac{\\left| V_{n\\, m}\\right| {}^2}{E_n-E_m}
\\begin{array}{ll}
 \\{ & 
\\begin{array}{ll}
 <E_n & \\text{if} E_n<E_m, \\\\
 >E_n & \\text{if} E_n>E_m. \\\\
\\end{array}
 \\\\
\\end{array}$$

In[360]:=
Block[{a = 0.5, En = 0, Em = 2, lev}, 
	lev[id_] := {Line[{#, 0}& /@ { - a, a}], Text[\"\
\\!\\(\[LeftBracketingBar]\" <> id <> \"\[RightAngleBracket]\\)\", \
{0, 0}, {0,  - 1}], Text[\"\\!\\(E\\_\" <> id <> \"\\)\", {a, 0}, { - \
1.5, 0}]};
	Graphics[{Translate[lev[\"n\"], { - 1, En}], Translate[lev[\"m\"], \
{1, Em}], {Arrowheads[{{0.08, 0.5}}], Dashed, AbsoluteThickness[1], \
Arrow@BSplineCurve[{{ - 1 + a, En}, {0, Em}, {1 - a, Em}}], \
Arrow@BSplineCurve[{{1 - a, Em}, {0, En}, { - 1 + a, En}}]}, Text[V
 m\[VeryThinSpace]n, { - 1 + a, (En + Em) / 2}, {0,  - 1.2}], Text[V
 n\[VeryThinSpace]m, {1 - a, (En + Em) / 2}, {0, 1.2}]}, ImageSize -> \
120]]

Out[360]=
\\!\\(\\*GraphicsBox[{GeometricTransformationBox[{LineBox[{{-0.5, 0}, \
{0.5, 0}}], 
    InsetBox[\"\\\"\\\\!\\\\(\[LeftBracketingBar]n\[RightAngleBracket]\
\\\\)\\\"\", {0, 0}, {0, -1}], \
InsetBox[\"\\\"\\\\!\\\\(E\\\\_n\\\\)\\\"\", {0.5, 0}, 
     {-1.5, 0}]}, {-1, 0}], \
GeometricTransformationBox[{LineBox[{{-0.5, 0}, { ... veBox[{{-0.5, \
0}, {0, 2}, {0.5, 2}}]], 
   ArrowBox[BSplineCurveBox[{{0.5, 2}, {0, 0}, {-0.5, 0}}]]}, 
  InsetBox[\"\\\"\\\\!\\\\(V\\\\_\\\\(m\[VeryThinSpace]n\\\\)\\\\)\\\"\
\", {-0.5, 1}, {0, -1.2}], 
  InsetBox[\"\\\"\\\\!\\\\(V\\\\_\\\\(n\[VeryThinSpace]m\\\\)\\\\)\\\"\
\", {0.5, 1}, {0, 1.2}]}, ImageSize -> 120]\\)
```

#### Application: the Qubit Model

```wl
$$\\hat{H}_0+\\hat{V}\\bumpeq \\left(
\\begin{array}{cc}
 1 & \\lambda  \\\\
 \\lambda  & -1 \\\\
\\end{array}
\\right).$$
```

* Unperturbed spectrum. $$| 0\\rangle$$: $$E_0=+1$$, $$| 1\\rangle$$: \
$$E_1=-1$$.

* State hybridization:

```wl
$$| 0\\rangle '=| 0\\rangle +\\frac{V_{10}}{E_0-E_1}| 1\\rangle \
+\\ldots =| 0\\rangle +\\frac{\\lambda }{2}| 1\\rangle +\\ldots ,\\\\
| 1\\rangle '=| 1\\rangle +\\frac{V_{01}}{E_1-E_0}| 0\\rangle \
+\\ldots =| 1\\rangle -\\frac{\\lambda }{2}| 0\\rangle +\\ldots .$$
```

* Level repulsion:

```wl
$$E_0^{\\prime }=E_0+\\frac{V_{01}V_{10}}{E_0-E_1}+\\ldots \
=+1+\\frac{\\lambda ^2}{2}+\\ldots ,\\\\
E_1^{\\prime }=E_1+\\frac{V_{10}V_{01}}{E_1-E_0}+\\ldots \
=-1-\\frac{\\lambda ^2}{2}+\\ldots .$$
```

Here we use a $$\\prime$$ to denote the *corrected* states $$| \
n\\rangle '\\equiv | n(V)\\rangle$$ and energies $$E_n^{\\prime \
}\\equiv E_n(V)$$.

Consider a quantum harmonic oscillator with rescaled operators \
$$\\left[\\hat{x},\\hat{p}\\right]=i \\mathbf{1}$$, and Hamiltonian: 
$$\\hat{H}_0=\\frac{1}{2}\\hbar  \\omega  \
\\left(\\hat{x}^2+\\hat{p}^2\\right)$$, 
whose eigenstates $$| n\\rangle$$ of the energies $$E_n=\\hbar  \
\\omega  (n+1/2)$$. 
Now add a linear potential perturbation: $$\\hat{V}=\\lambda  \
\\hat{x}$$, where $$\\lambda \\in \\mathbb{R}$$ is a small parameter.
(i) Express $$\\hat{V}$$ in terms of the annihilation and creation \
operators: 
$$\\hat{a}=\\frac{1}{\\sqrt{2}}\\left(\\hat{x}+i \\hat{p}\\right)$$, \
$$\\hat{a}^{\\dagger }=\\frac{1}{\\sqrt{2}}\\left(\\hat{x}-i \\hat{p}\
\\right)$$, 
and compute the matrix element $$V_{mn}=\\langle m| \\hat{V}| \
n\\rangle$$. In particular, find $$V_{nn}$$, $$V_{n+1,n}$$, and \
$$V_{n-1,n}$$.
(ii) Use perturbation theory to find the perturbed energy levels \
$$E_n(V)$$  up to 2nd order in $$\\lambda$$.
(iii) Complete the square in the full Hamiltonian \
$$\\hat{H}=\\hat{H}_0+\\hat{V}$$ to determine the exact energy \
levels. [Hint: consider defining a shifted position operator \
$$\\hat{x}'=\\hat{x}+\\lambda /(\\hbar  \\omega )\\mathbf{1}$$, check \
$$\\left[\\hat{x}',\\hat{p}\\right]$$ commutation relation and \
express $$\\hat{H}$$ in terms of $$\\hat{x}'$$ and $$\\hat{p}$$.]
(iv) Compare the perturbative result from (ii) and the exact result \
from (iii), what can you conclude?

Solution (HW XXX)

(i) Express $$\\hat{x}$$ in terms of $$\\hat{a}$$ and \
$$\\hat{a}^{\\dagger }$$,

```wl
$$\\hat{x}=\\frac{1}{\\sqrt{2}}\\left(\\hat{a}+\\hat{a}^{\\dagger \
}\\right), \\Rightarrow  \\hat{V}=\\lambda  \\hat{x}=\\frac{\\lambda \
}{\\sqrt{2}}\\left(\\hat{a}+\\hat{a}^{\\dagger
}\\right).$$
```

Matrix elements:

```wl
$$\\langle m| \\hat{a}| n\\rangle =\\sqrt{n}\\delta _{m,n-1},\\langle \
m| \\hat{a}^{\\dagger }| n\\rangle =\\sqrt{n+1}\\delta _{m,n+1},$$
```

therefore

```wl
$$V_{mn}=\\langle m| \\hat{V}| n\\rangle =\\frac{\\lambda \
}{\\sqrt{2}}\\left(\\sqrt{n}\\delta _{m,n-1}+\\sqrt{n+1}\\delta \
_{m,n+1}\\right),$$
```

In particular

* $$V_{nn}=0$$,

* $$V_{n+1,n}=\\frac{\\lambda }{\\sqrt{2}}\\sqrt{n+1}$$,

* $$V_{n-1,n}=\\frac{\\lambda }{\\sqrt{2}}\\sqrt{n}$$.

(ii) By perturbation theory, to the 2nd order,

```wl
$$E_n(V)=E_n+V_{n\\, n}+\\sum _{m\\neq n} \\frac{V_{n\\, m}V_{m\\, \
n}}{E_n-E_m}+\\ldots$$
$$=E_n+V_{nn}+\\frac{V_{n\\, ,n+1}V_{n+1,n}}{E_n-E_{n+1}}+\\frac{V_{n\
\\, ,n-1}V_{n-1,n}}{E_n-E_{n-1}}+\\ldots$$
$$=\\hbar  \\omega \\left(n+\\frac{1}{2}\\right)+0+\\frac{\\lambda \
^2}{2}\\frac{n+1}{-\\hbar  \\omega }+\\frac{\\lambda ^2}{2}\\frac{n}{\
\\hbar  \\omega }+\\ldots$$
$$=\\hbar  \\omega \\left(n+\\frac{1}{2}\\right)-\\frac{\\lambda \
^2}{2 \\hbar  \\omega }+\\ldots .$$
```

(iii) Define a shifted position operator \
$$\\hat{x}'=\\hat{x}+\\lambda /(\\hbar  \\omega )\\mathbf{1}$$. First \
check that it still satisfy the canonical commutation relation with \
$$\\hat{p}$$ :

```wl
$$\\left[\\hat{x}',\\hat{p}\\right]=\\left[\\hat{x}+\\frac{\\lambda \
}{\\hbar  \\omega }\\mathbf{1},\\hat{p}\\right]$$
$$=\\left[\\hat{x},\\hat{p}\\right]+\\frac{\\lambda }{\\hbar  \\omega \
}\\left[\\mathbf{1},\\hat{p}\\right]$$
$$=\\left[\\hat{x},\\hat{p}\\right]=i \\mathbf{1}.$$
```

The full Hamiltonian can be written as

```wl
$$\\hat{H}=\\hat{H}_0+\\hat{V}$$
$$=\\frac{1}{2}\\hbar  \\omega  \\left(\\hat{x}^2+\\hat{p}^2\\right)+\
\\lambda  \\hat{x}$$
$$=\\frac{1}{2}\\hbar  \\omega  \\left(\\hat{x}^2+\\frac{2\\lambda }{\
\\hbar  \\omega }\\hat{x}+\\hat{p}^2\\right)$$
$$=\\frac{1}{2}\\hbar  \\omega  \\left(\\hat{x}^2+\\frac{2\\lambda }{\
\\hbar  \\omega }\\hat{x}+\\frac{\\lambda ^2}{\\hbar ^2 \\omega \
^2}\\mathbf{1}-\\frac{\\lambda
^2}{\\hbar ^2 \\omega ^2}\\mathbf{1}+\\hat{p}^2\\right)$$
$$=\\frac{1}{2}\\hbar  \\omega  \
\\left(\\left(\\hat{x}+\\frac{\\lambda }{\\hbar  \\omega }\\mathbf{1}\
\\right)^2-\\frac{\\lambda ^2}{\\hbar ^2 \\omega \
^2}\\mathbf{1}+\\hat{p}^2\\right)$$
$$=\\frac{1}{2}\\hbar  \\omega  \\left(\\hat{x}^{\\text{$\\prime \
$2}}+\\hat{p}^2\\right)-\\frac{\\lambda ^2}{2 \\hbar  \\omega \
}\\mathbf{1},$$
```

which is a new harmonic oscillator in terms of $$\\hat{x}'$$ and \
$$\\hat{p}$$ but with every energy level shifted by $$E_n\\rightarrow \
E_n-\\left.\\lambda ^2\\right/(2 \\hbar  \\omega )$$. Therefore the \
exact energy spectrum is

```wl
$$E_n=\\hbar  \\omega \\left(n+\\frac{1}{2}\\right)-\\frac{\\lambda \
^2}{2 \\hbar  \\omega }.$$
```

(iv) The perturbation result matches the exact result perfectly to \
the 2nd order in $$\\lambda$$. Because harmonic oscillator is a \
quadratic system, a linear perturbation has no effect beyond the \
quadratic order, such that 2nd order perturbation theory already \
gives the exact result.

### Degenerate Perturbation Theory

#### General Ideas

How do we deal with degeneracies in $$\\hat{H}_0$$ spectrum?

Strategy: **divide and conquer**.

```wl
In[605]:=
Block[{L = 5, Jacobi, mask, K, V, H0, H1, H2, cmp}, 
	SeedRandom[2];
	mask = Normal@SparseArray[{i_, j_} /; i > 2 && j \[LessEqual] 2 \
\[RuleDelayed] 1, {L, L}];
	Jacobi[H_] := Block[{m, n, r, \[Phi], \[Theta], G}, {m, n} = \
First@Position[#, Max@#]&@Abs[mask H];
	r = H\[LeftDoubleBracket]m, n\[RightDoubleBracket] / (H\
\[LeftDoubleBracket]n, n\[RightDoubleBracket] - \
H\[LeftDoubleBracket]m, m\[RightDoubleBracket]);
	\[Phi] = Arg[r];
	\[Theta] = ArcTan[2 Abs[r]] / 2;
	G = IdentityMatrix@Dimensions@H;
	G\[LeftDoubleBracket]n, n\[RightDoubleBracket] = G\
\[LeftDoubleBracket]m, m\[RightDoubleBracket] = Cos[\[Theta]];
	G\[LeftDoubleBracket]m, n\[RightDoubleBracket] =  - \
Sin[\[Theta]]Exp[I \[Phi]];
	G\[LeftDoubleBracket]n, m\[RightDoubleBracket] = Sin[\[Theta]]Exp[ - \
I \[Phi]];
	Chop[G.H.ConjugateTranspose[G]]];
	K = DiagonalMatrix[{ - 1,  - 1, 1, 1, 1}];V = \
Chop[Hermitianize[RandomVariate[NormalDistribution[], {L, L, 2}].{1, \
I}]];
	V = V - DiagonalMatrix@Diagonal@V;
	H0 = K + 0.3V;
	H1 = Nest[Jacobi, H0, 25];
	mask = Normal@SparseArray[{i_, j_} /; i > j && !(i > 2 && j \
\[LessEqual] 2) \[RuleDelayed] 1, Dimensions[H1]];
	H2 = Nest[Jacobi, H1, 7];
	cmp = ComplexMatrixPlot[#, Mesh -> Block[{mesh = {{0, \
AbsoluteThickness[1]}, {1, AbsoluteThickness[0.3]}, {2, \
AbsoluteThickness[1]}, {3, AbsoluteThickness[0.3]}, {4, \
AbsoluteThickness[0.3]}, {5, AbsoluteThickness[1]}}}, {mesh, mesh}], \
FrameTicks -> None, ImageSize -> 60]&;
	Style[Row[{Column[{cmp[K], \"+       \", Row[{\"\[Lambda] \", \
cmp[V]}]}, Alignment -> Right], \" = \", Row[cmp /@ {H0, H1, H2}, \"\
\[RightArrow]\"]}], FontFamily -> \"CMU\"]]

Out[605]=
\\!\\(\\*
StyleBox[
TemplateBox[{
TagBox[
GridBox[{{
GraphicsBox[{
RasterBox[CompressedData[\"1:eJ ... eM8=\"], {{0, 0}, {5, 5}}, {0, \
1}], {{Antialiasing -> False, 
Directive[
GrayLevel[0], 
AbsoluteThickness[1]], {{
AbsoluteThickness[1], 
LineBox[{{0, 5} ... ntSize[4], 
AbsoluteThickness[1.5]]}, \"DomainPadding\" -> Scaled[0.02], 
        \"RangePadding\" -> Scaled[0.05]}, TicksStyle -> Directive[
GrayLevel[0], FontSize -> 12]]}, \"RowWithSeparators\"]},
\"RowDefault\"],
StripOnInput->False,
FontFamily->\"CMU\"]\\)
```

The degenerated states span a Hilbert *subspace*, called the \
**degenerate subspace**.

* First apply *non-degenerate* perturbation theory to bring the \
Hamiltonian to **diagonal blocks** in the *degenerate subspaces*.

	* Each *diagonal block* represents an **effective Hamiltonian** \
within the *degenerated subspace.*

	* **previously**: perturbative correction to each *energy level* \
\[RightArrow] **now**: perturbative correction to each *effective \
Hamiltonian*.

* Then go on with each *effective Hamiltonian* :

	* If the degeneracy has been lifted (typically), we proceed with \
*non-degenerate* perturbation in each block.

	* If the diagonal elements are still fully degenerated, we proceed \
with *exact diagonalization* (no perturbative approach available in \
this case).

The **degenerate **perturbation theory: applying *non-degenerate* \
perturbation theory in *hierarchies.* It progressively focus on lower \
and lower *energy scales* \[Implies] A key idea of the \
**renormalization group** approach in quantum field theory.

#### Generalized Hellmann-Feynman Theorems

We can generalize the **Hellmann-Feynman theorems** to generic \
spectrum with *degeneracies*. When the *unperturbed Hamiltonian* \
$$\\hat{H}_0$$ has degenerate levels, we use *two* indices to label \
the basis state

```wl
$$| n\\rangle \\overset{\\text{generalize}}{\\longrightarrow }| n\\, \
\\alpha \\rangle$$
```

* $$n$$: **principal **quantum number, labels degenerate subspaces.

* $$\\alpha$$: **secondary** quantum number, labels orthogonal \
degenerate state within each subspace.

The states with the same index $$n$$ are degenerated:

```wl
$$\\hat{H}_0| n\\, \\alpha \\rangle =E_n| n\\, \\alpha \\rangle ,$$
```

such that the eigenenergy $$E_n$$ only depends on $$n$$.

* $$| n\\, \\alpha \\rangle$$ form a set of *orthonormal* basis: \
$$\\langle m\\, \\alpha |n\\, \\beta \\rangle =\\delta _{m\\, \
n}\\delta _{\\alpha \\, \\beta }$$.

* The *perturbation operator* $$V$$ can be represented in this basis:

```wl
$$\\hat{V}=\\sum _{m\\, \\alpha ,n\\, \\beta } | m\\, \\alpha \
\\rangle V_{m\\, \\alpha ,n\\, \\beta }\\langle n\\, \\beta | .$$
```

However, once the perturbation $$\\hat{V}$$ is included,

```wl
$$\\hat{H}(\\lambda )=\\hat{H}_0+\\lambda  \\hat{V},$$
```

the degeneracy in each subspace can no longer be maintained in \
general. Instead, we will only require the perturbed Hamiltonian \
$$\\hat{H}(\\lambda )$$ to be *block-diagonalized* in the $$| n\\, \
\\alpha (\\lambda )\\rangle$$ basis, meaning that

```wl
$$\\hat{H}(\\lambda )| n\\, \\beta (\\lambda )\\rangle =\\sum \
_{\\alpha } | n\\, \\alpha (\\lambda )\\rangle E_{n,\\alpha \\, \
\\beta }(\\lambda ).$$
```

* $$E_{n,\\alpha \\, \\beta }(\\lambda )$$ is the matrix element of \
the **effective Hamiltonian** in the $$n$$th degenerate subspace.

	* When $$\\lambda =0$$, $$E_{n,\\alpha \\, \\beta }(\\lambda )$$ \
should fall back to

```wl
$$E_{n,\\alpha \\, \\beta }\\equiv E_{n,\\alpha \\, \\beta \
}(0)=E_n\\delta _{\\alpha \\, \\beta },$$
```

to recover Eq. (XXX) in the unperturbed limit.

* The Hermitian conjugate version of Eq. (XXX) reads

```wl
$$\\langle m\\, \\gamma (\\lambda )| \\hat{H}(\\lambda )=\\sum \
_{\\delta } \\langle m\\, \\delta (\\lambda )| E_{m,\\delta \\, \
\\gamma }^*(\\lambda )=\\sum _{\\delta
} E_{m,\\gamma \\, \\delta }(\\lambda )\\langle m\\, \\delta \
(\\lambda )| ,$$
```

where we have assumed that the effective Hamiltonian is  *Hermitian*: \
$$E_{m,\\delta \\, \\gamma }^*(\\lambda )=E_{m,\\gamma \\, \\delta }(\
\\lambda )$$.

Applying Subscript[\\[PartialD], \\[Lambda]] on both sides of Eq. \
(XXX) and overlapping with Bra[{m \\[Gamma]}], we obtain

```wl
$$\\langle m\\, \\gamma | \\partial _{\\lambda }\\hat{H}| n\\, \\beta \
\\rangle =\\sum _{\\alpha } \\partial _{\\lambda }E_{n,\\alpha \\, \
\\beta }\\langle m\\, \\gamma
|n\\, \\alpha \\rangle +\\sum _{\\alpha } \\langle m\\, \\gamma \
|\\partial _{\\lambda }n\\, \\alpha \\rangle E_{n,\\alpha \\, \\beta \
}-\\sum _{\\delta } E_{m,\\gamma
\\, \\delta }\\langle m\\, \\delta |\\partial _{\\lambda }n\\, \\beta \
\\rangle$$
$$=\\partial _{\\lambda }E_{n,\\gamma \\, \\beta }\\delta _{m\\, \
n}+\\left(E_n-E_m\\right)\\langle m\\, \\gamma |\\partial _{\\lambda \
}n\\, \\beta \\rangle$$
```

* When $$m=n$$, the **first Hellmann-Feynman** theorem:

```wl
$$\\partial _{\\lambda }E_{n,\\alpha \\, \\beta }=\\langle n\\, \
\\alpha | \\partial _{\\lambda }\\hat{H}| n\\, \\beta \\rangle \
=V_{n\\, \\alpha ,n\\, \\beta }.$$
```

* When $$m\\neq n$$, the **second Hellmann-Feynman** theorem:

```wl
$$\\langle m\\, \\alpha |\\partial _{\\lambda }n\\, \\beta \\rangle =\
\\frac{\\langle m\\, \\alpha | \\partial _{\\lambda }\\hat{H}| n\\, \
\\beta \\rangle }{E_n-E_m}=\\frac{V_{m\\,
\\alpha ,n\\, \\beta }}{E_n-E_m},\\\\
\\left\\langle \\partial _{\\lambda }m\\, \\alpha \\right|n\\, \\beta \
\\rangle =\\frac{\\langle m\\, \\alpha | \\partial _{\\lambda \
}\\hat{H}| n\\, \\beta \\rangle }{E_m-E_n}=\\frac{V_{m\\,
\\alpha ,n\\, \\beta }}{E_m-E_n}.$$
```

#### Effective Hamiltonian

Using Eq. (XXX), Eq. (XXX) and the techniques we have developed \
previously, the following derivatives can be calculated

```wl
$$\\partial _{\\lambda }E_{n,\\alpha \\, \\beta }=V_{n\\, \\alpha \
,n\\, \\beta },\\\\
\\partial _{\\lambda }^2E_{n,\\alpha \\, \\beta }=2\\sum _{m\\neq n} \
\\sum _{\\gamma } \\frac{V_{n\\, \\alpha ,m\\, \\gamma }V_{m\\, \
\\gamma ,n\\, \\beta }}{E_n-E_m},\\\\
\\left| \\partial _{\\lambda }n\\, \\alpha \\right\\rangle =\\sum _{m\
\\neq n} \\sum _{\\beta } | m\\, \\beta \\rangle \\frac{V_{m\\, \
\\beta ,n\\, \\alpha }}{E_n-E_m}.$$
```

With these, we can obtain:

* (the matrix element of) the **effective Hamiltonian** to the 2nd \
order in $$\\lambda$$

```wl
$$E_{n,\\alpha \\, \\beta }(\\lambda )=E_n\\delta _{\\alpha \\, \
\\beta }+V_{n\\, \\alpha ,n\\, \\beta }\\lambda +\\sum _{m\\neq n} \
\\sum _{\\gamma } \\frac{V_{n\\,
\\alpha ,m\\, \\gamma }V_{m\\, \\gamma ,n\\, \\beta \
}}{E_n-E_m}\\lambda ^2+\\ldots ,$$
```

* the corrected **basis state** to the 1st order in $$\\lambda$$

```wl
$$| n\\, \\alpha (\\lambda )\\rangle =| n\\, \\alpha \\rangle +\\sum \
_{m\\neq n} \\sum _{\\beta } | m\\, \\beta \\rangle \\frac{V_{m\\, \
\\beta ,n\\, \\alpha }}{E_n-E_m}\\lambda
+\\ldots .$$
```

Note that the *summation range* of the *secondary* index will depend \
on the choice of the *primary* index, which can be inferred easily.

Eq. (XXX) and Eq. (XXX) allow us to construct the effective \
Hamiltonian in operator form

```wl
$$\\hat{H}_n^{\\text{eff}}(\\lambda )=\\sum _{\\alpha ,\\beta } | \
n\\, \\alpha (\\lambda )\\rangle E_{n,\\alpha \\, \\beta }(\\lambda )\
\\langle n\\, \\beta (\\lambda
)| .$$
```

The **full Hamiltonian**: summation of effective Hamiltonians over \
degenerate subspaces $$\\hat{H}(\\lambda )=\\oplus \
_n\\hat{H}_n^{\\text{eff}}(\\lambda )$$.

Consider a three-level quantum system with basis states $$| \
1\\rangle$$, $$| 2\\rangle$$, and $$| 3\\rangle$$. The unperturbed \
Hamiltonian is 
$$\\hat{H}_0=\\Delta | 3\\rangle \\langle 3|$$,
with $$\\Delta >0$$. The degenerate subspace is spanned by $$| \
1\\rangle$$ and $$| 2\\rangle$$ at zero energy, while $$| 3\\rangle$$ \
is an excited state at energy $$\\Delta$$. A perturbation couples the \
degenerated states to the excited state as 
$$\\hat{V}=\\lambda _1| 1\\rangle \\langle 3| +\\lambda _2| 2\\rangle \
\\langle 3| +h.c.$$, 
where $$\\left| \\lambda _1\\right| ,\\left| \\lambda _2\\right| \\ll \
\\Delta$$ are small parameters.
(i) Use degenerate perturbation theory to compute effective \
Hamiltonian in the degenerate subspace, up to second order in \
$$\\lambda _1$$, $$\\lambda _2$$.
(ii) Diagonalize the effective Hamiltonian to find the new energy \
eigenvalues and eigenstates. 
The state remaining at zero energy is identified as the **dark \
state**.
(iii) Show that the dark state is an exact eigenstate of the full \
Hamiltonian $$\\hat{H}=\\hat{H}_0+\\hat{V}$$ with zero energy (to all \
orders in $$\\lambda _{1,2}$$).

Solution (HW XXX)

(i) The 2nd order effective Hamiltonian is

```wl
$$\\hat{H}_{\\text{eff}}\\bumpeq -\\frac{1}{\\Delta }\\left(
\\begin{array}{cc}
 \\left| \\lambda _1\\right| {}^2 & \\lambda _1\\lambda _2^* \\\\
 \\lambda _2\\lambda _1^* & \\left| \\lambda _2\\right| {}^2 \\\\
\\end{array}
\\right)=-\\frac{1}{\\Delta }| \\lambda \\rangle \\langle \\lambda | \
,$$
```

where $$| \\lambda \\rangle =\\lambda _1| 1\\rangle +\\lambda _2| \
2\\rangle$$.

(ii) Diagonalize $$\\hat{H}_{\\text{eff}}$$, we found

```wl
$$E_{\\pm }=-\\frac{1}{\\Delta }\\left(\\frac{\\left| \\lambda \
_1\\right| {}^2+\\left| \\lambda _2\\right| {}^2}{2}\\pm \
\\sqrt{\\left(\\frac{\\left| \\lambda _1\\right|
{}^2-\\left| \\lambda _2\\right| {}^2}{2}\\right){}^2+\\left| \
\\lambda _1\\right| {}^2\\left| \\lambda _2\\right| {}^2}\\right)$$
$$=-\\frac{1}{\\Delta }\\left(\\frac{\\left| \\lambda _1\\right| \
{}^2+\\left| \\lambda _2\\right| {}^2}{2}\\pm \\frac{\\left| \\lambda \
_1\\right| {}^2+\\left| \\lambda
_2\\right| {}^2}{2}\\right),$$
```

meaning that

```wl
$$E_+=-\\frac{1}{\\Delta }\\left(\\left| \\lambda _1\\right| \
{}^2+\\left| \\lambda _2\\right| {}^2\\right),\\\\
E_-=0.$$
```

The corresponding eigenstates can be found by solving

```wl
$$\\hat{H}_{\\text{eff}}| \\pm \\rangle =E_{\\pm }| \\pm \\rangle ,$$
```

such that

```wl
$$| +\\rangle =\\frac{1}{\\sqrt{\\left| \\lambda _1\\right| \
{}^2+\\left| \\lambda _2\\right| {}^2}}\\left(\\lambda _1| 1\\rangle \
+\\lambda _2| 2\\rangle \\right),\\\\
| -\\rangle =\\frac{1}{\\sqrt{\\left| \\lambda _1\\right| \
{}^2+\\left| \\lambda _2\\right| {}^2}}\\left(\\lambda _2^*| \
1\\rangle -\\lambda _1^*| 2\\rangle \\right).$$
```

$$| -\\rangle$$ is the dark state.

(iii) Action of $$\\hat{H}_0$$ on $$| -\\rangle$$ :

```wl
$$\\hat{H}_0| -\\rangle =\\Delta | 3\\rangle \\langle 3|-\\rangle =0,$$
```

because $$| -\\rangle$$ has no component in $$| 3\\rangle$$.

Action of $$\\hat{V}$$ on $$| -\\rangle$$ :

* Note that $$\\hat{V}$$ can be written as

```wl
$$\\hat{V}=\\lambda _1| 1\\rangle \\langle 3| +\\lambda _2| 2\\rangle \
\\langle 3| +h.c.\\\\
=\\left(\\lambda _1| 1\\rangle +\\lambda _2| 2\\rangle \
\\right)\\langle 3| +| 3\\rangle \\left(\\lambda _1^*\\langle 1| \
+\\lambda _2^*\\langle 2| \\right),$$
```

* So action of $$\\hat{V}$$ on $$| -\\rangle$$ reads

```wl
$$\\hat{V}| -\\rangle =\\left(\\lambda _1| 1\\rangle +\\lambda _2| \
2\\rangle \\right)\\langle 3|-\\rangle +\\frac{1}{\\sqrt{\\left| \
\\lambda _1\\right| {}^2+\\left|
\\lambda _2\\right| {}^2}}| 3\\rangle \\left(\\lambda _1^*\\langle 1| \
+\\lambda _2^*\\langle 2| \\right)\\left(\\lambda _2^*| 1\\rangle \
-\\lambda _1^*| 2\\rangle
\\right)$$
$$=0+\\frac{1}{\\sqrt{\\left| \\lambda _1\\right| {}^2+\\left| \
\\lambda _2\\right| {}^2}}| 3\\rangle \\left(\\lambda _1^*\\lambda \
_2^*-\\lambda _2^*\\lambda _1^*\\right)$$
$$=0+0=0,$$
```

where we have used the fact that $$\\langle 3|-\\rangle =0$$.

Since $$\\hat{H}_0| -\\rangle =\\hat{V}| -\\rangle =0$$, we conclude

```wl
$$\\hat{H}| -\\rangle =\\hat{H}_0| -\\rangle +\\hat{V}| -\\rangle =0.$$
```

Therefore $$| -\\rangle$$ is an exact eigenstate of $$\\hat{H}$$ with \
eigenvalue 0 regardless of $$\\lambda _{1,2}$$.

#### Application: A Spin-1 Model\\*

Consider a spin-1 system (3-dimensional Hilbert space).

* Basis: $$| +1\\rangle ,| 0\\rangle ,| -1\\rangle$$.

* The matrix representations for spin operators $$\\hat{S}^x$$ and $$\
\\hat{S}^z$$

```wl
$$\\hat{S}^x\\bumpeq \\frac{1}{\\sqrt{2}}\\left(
\\begin{array}{ccc}
 0 & 1 & 0 \\\\
 1 & 0 & 1 \\\\
 0 & 1 & 0 \\\\
\\end{array}
\\right),\\hat{S}^z\\bumpeq \\left(
\\begin{array}{ccc}
 1 & 0 & 0 \\\\
 0 & 0 & 0 \\\\
 0 & 0 & -1 \\\\
\\end{array}
\\right).$$
```

Hamiltonian

```wl
$$\\hat{H}(\\lambda )=\\hat{H}_0+\\lambda  \\hat{V},\\\\
\\hat{H}_0=\\left(\\hat{S}^z\\right)^2\\bumpeq \\left(
\\begin{array}{ccc}
 1 & 0 & 0 \\\\
 0 & 0 & 0 \\\\
 0 & 0 & 1 \\\\
\\end{array}
\\right),\\\\
\\hat{V}=\\hat{S}^x+\\hat{S}^z\\bumpeq \\left(
\\begin{array}{ccc}
 1 & \\frac{1}{\\sqrt{2}} & 0 \\\\
 \\frac{1}{\\sqrt{2}} & 0 & \\frac{1}{\\sqrt{2}} \\\\
 0 & \\frac{1}{\\sqrt{2}} & -1 \\\\
\\end{array}
\\right).$$
```

Degenerate subspaces

```wl
$$\\begin{array}{ccc}
 n & \\text{states} & \\text{energy} \\\\
 1 & | +1\\rangle ,| -1\\rangle  & E_1=1 \\\\
 0 & | 0\\rangle  & E_0=0 \\\\
\\end{array}$$
```

* Corrected basis (use $$\\prime$$ to denote the perturbed result)

```wl
$$| \\pm 1\\rangle '=| \\pm 1\\rangle +| 0\\rangle \\frac{V_{0,\\pm \
1}}{E_1-E_0}\\lambda +\\ldots =| \\pm 1\\rangle +\\frac{\\lambda \
}{\\sqrt{2}}| 0\\rangle +\\ldots
,\\\\
| 0\\rangle '=| 0\\rangle +| +1\\rangle \
\\frac{V_{+1,0}}{E_0-E_1}\\lambda +| -1\\rangle \
\\frac{V_{-1,0}}{E_0-E_1}\\lambda +\\ldots$$
$$=| 0\\rangle -\\frac{\\lambda }{\\sqrt{2}}(| +1\\rangle +| \
-1\\rangle )+\\ldots .$$
```

* Effective Hamiltonian

	* $$n=1$$ subspace

```wl
$$\\hat{H}_1^{\\text{eff}}=| +1\\rangle '\\left(E_1+V_{+1,+1}\\lambda \
+\\frac{V_{+1,0}V_{0,+1}}{E_1-E_0}\\lambda ^2\\right)\\langle +1| '+| \
-1\\rangle '\\left(E_1+V_{-1,-1}\\lambda
+\\frac{V_{-1,0}V_{0,-1}}{E_1-E_0}\\lambda ^2\\right)\\langle -1| \
'+\\\\
| +1\\rangle '\\left(V_{+1,-1}\\lambda \
+\\frac{V_{+1,0}V_{0,-1}}{E_1-E_0}\\lambda ^2\\right)\\langle -1| '+| \
-1\\rangle '\\left(V_{-1,+1}\\lambda \
+\\frac{V_{-1,0}V_{0,+1}}{E_1-E_0}\\lambda
^2\\right)\\langle +1| '+\\ldots$$
$$=| +1\\rangle '\\left(1+\\lambda +\\frac{\\lambda \
^2}{2}\\right)\\langle +1| '+| -1\\rangle '\\left(1-\\lambda +\\frac{\
\\lambda ^2}{2}\\right)\\langle -1| '+|
+1\\rangle '\\frac{\\lambda ^2}{2}\\langle -1| '+| -1\\rangle \
'\\frac{\\lambda ^2}{2}\\langle +1| '+\\ldots$$
```

On the corrected basis $$| +1\\rangle ',| -1\\rangle '$$, \
$$H_1^{\\text{eff}}$$ can be represented as a $$2\\times 2$$ matrix

```wl
$$\\hat{H}_1^{\\text{eff}}\\bumpeq \\left(
\\begin{array}{cc}
 1+\\lambda +\\frac{\\lambda ^2}{2} & \\frac{\\lambda ^2}{2} \\\\
 \\frac{\\lambda ^2}{2} & 1-\\lambda +\\frac{\\lambda ^2}{2} \\\\
\\end{array}
\\right).$$
```

The degeneracy is lifted \[Implies] we can proceed with \
non-degenerate perturbation in the next iteration.

	* $$n=0$$ subspace

```wl
$$\\hat{H}_0^{\\text{eff}}=| 0\\rangle '\\left(E_0+V_{0,0}\\lambda \
+\\frac{V_{0,+1}V_{+1,0}+V_{0,-1}V_{-1,0}}{E_0-E_1}\\lambda \
^2\\right)\\langle 0| '+\\ldots$$
$$=| 0\\rangle '\\left(-\\lambda ^2\\right)\\langle 0| '+\\ldots$$
```

We can use another round of the non-degenerate perturbation theory to \
further diagonalize $$\\hat{H}_1^{\\text{eff}}$$. We start with

```wl
$$\\hat{H}_1^{\\text{eff}}=| +1\\rangle 'E_{+1}^{\\prime }\\langle \
+1| '+| -1\\rangle 'E_{-1}^{\\prime }\\langle -1| '+| +1\\rangle \
'V_{+1,-1}^{\\prime }\\langle
-1| '+| -1\\rangle 'V_{-1,+1}^{\\prime }\\langle +1| ',\\\\
E_{\\pm 1}^{\\prime }=1\\pm \\lambda +\\frac{\\lambda ^2}{2},\\\\
V_{+1,-1}^{\\prime }=V_{-1,+1}^{\\prime }=\\frac{\\lambda ^2}{2}, \
V_{+1,+1}^{\\prime }=V_{-1,-1}^{\\prime }=0.$$
```

* Corrected states

```wl
$$| +1\\rangle ^{\\prime\\prime }=| +1\\rangle '+| -1\\rangle \
'\\frac{V_{-1,+1}^{\\prime }}{E_{+1}^{\\prime }-E_{-1}^{\\prime \
}}+\\ldots =| +1\\rangle '+\\frac{\\lambda
}{4}| -1\\rangle '+\\ldots$$
$$| -1\\rangle ^{\\prime\\prime }=| -1\\rangle '+| +1\\rangle \
'\\frac{V_{+1,-1}^{\\prime }}{E_{-1}^{\\prime }-E_{+1}^{\\prime \
}}+\\ldots =| -1\\rangle '-\\frac{\\lambda
}{4}| +1\\rangle '+\\ldots$$
```

Plugging in Eq. (XXX),

```wl
$$| +1\\rangle ^{\\prime\\prime }=| +1\\rangle +\\frac{\\lambda \
}{\\sqrt{2}}| 0\\rangle +\\frac{\\lambda }{4}| -1\\rangle \
+\\frac{\\lambda ^2}{4\\sqrt{2}}| 0\\rangle
+\\ldots$$
$$| -1\\rangle ^{\\prime\\prime }=| -1\\rangle +\\frac{\\lambda \
}{\\sqrt{2}}| 0\\rangle -\\frac{\\lambda }{4}| +1\\rangle \
-\\frac{\\lambda ^2}{4\\sqrt{2}}| 0\\rangle
+\\ldots$$
```

The $$\\lambda ^2$$ terms should not be included, because the \
expansion is only reliable to the 1st order in $$\\lambda$$.

* Corrected energies

```wl
$$E_{+1}^{\\prime\\prime }=E_{+1}^{\\prime }+V_{+1,+1}^{\\prime \
}+\\frac{V_{+1,-1}^{\\prime }V_{-1,+1}^{\\prime \
}}{E_{+1}-E_{-1}}=1+\\lambda +\\frac{\\lambda
^2}{2}+\\frac{\\lambda ^3}{8}+\\ldots$$
$$E_{-1}^{\\prime\\prime }=E_{-1}^{\\prime }+V_{-1,-1}^{\\prime \
}+\\frac{V_{-1,+1}^{\\prime }V_{+1,-1}^{\\prime \
}}{E_{-1}-E_{+1}}=1-\\lambda +\\frac{\\lambda
^2}{2}-\\frac{\\lambda ^3}{8}+\\ldots$$
```

The $$\\lambda ^3$$ terms should not be included, because the \
expansion is only reliable to the 2nd order in $$\\lambda$$.

In conclusion, we found following perturbative expansions for the \
spin-1 model given in Eq. (XXX)

```wl
$$\\begin{array}{cc}
 \\text{eigenenergies} & \\text{eigenstates} \\\\
 E_{+1}^{\\prime\\prime }=1+\\lambda +\\frac{\\lambda \
^2}{2}+\\mathcal{O}\\left(\\lambda ^3\\right) & | +1\\rangle \
^{\\prime\\prime }=| +1\\rangle +\\frac{\\lambda
}{\\sqrt{2}}| 0\\rangle +\\frac{\\lambda }{4}| -1\\rangle \
+\\mathcal{O}\\left(\\lambda ^2\\right) \\\\
 E_0^{\\prime }=-\\lambda ^2+\\mathcal{O}\\left(\\lambda ^3\\right) & \
| 0\\rangle '=| 0\\rangle -\\frac{\\lambda }{\\sqrt{2}}(| +1\\rangle \
+| -1\\rangle )+\\mathcal{O}\\left(\\lambda
^2\\right) \\\\
 E_{-1}^{\\prime\\prime }=1-\\lambda +\\frac{\\lambda \
^2}{2}+\\mathcal{O}\\left(\\lambda ^3\\right) & | -1\\rangle \
^{\\prime\\prime }=| -1\\rangle +\\frac{\\lambda
}{\\sqrt{2}}| 0\\rangle -\\frac{\\lambda }{4}| +1\\rangle \
+\\mathcal{O}\\left(\\lambda ^2\\right) \\\\
\\end{array}$$
```

If we exactly diagonalize $$\\hat{H}(\\lambda )$$ and perform the \
Taylor expansion, the above results can be verified.

```wl
In[617]:= Grid[{Series[#1, {\[Lambda], 0, 2}], PowerExpand@Series[#2 \
/ Sqrt[#2.#2], {\[Lambda], 0, 1}].(Ket /@ {\"+1\", \"0\", \
\"-1\"})}&@@@Thread@Eigensystem[{{1, 0, 0}, {0, 0, 0}, {0, 0, 1}} + \
\[Lambda]{{1, 1 / Sqrt[2], 0}, {1 / Sqrt[2], 0, 1 / Sqrt[2]}, {0, 1 / \
Sqrt[2],  - 1}}]]

During evaluation of In[617]:=
2           2           2     3
Because of branch cuts, the series may represent a different root of \
8 \[Lambda]  + (4 - 8 \[Lambda] ) #1 - 4 #1  + #1  & for some values \
of \[Lambda].

During evaluation of In[617]:=
2           2           2     3
Because of branch cuts, the series may represent a different root of \
8 \[Lambda]  + (4 - 8 \[Lambda] ) #1 - 4 #1  + #1  & for some values \
of \[Lambda].

During evaluation of In[617]:=
2           2           2     3
Because of branch cuts, the series may represent a different root of \
8 \[Lambda]  + (4 - 8 \[Lambda] ) #1 - 4 #1  + #1  & for some values \
of \[Lambda].

During evaluation of In[617]:= Further output of Root :: sbr will be \
suppressed during this calculation.

Out[617]=
|                                         |                           \
                                                    |
| --------------------------------------- | \
-----------------------------------------------------------------------------\
 |
|  ...  |
| SeriesData[\[Lambda], 0, {1, -1, 1/2}, 0, 3, 1] | SeriesData[\
\[Lambda], 0, {Ket[\"-1\"], Ket[\"0\"]/Sqrt[2] - Ket[\"+1\"]/4}, 0, \
2, 1]        |
| SeriesData[\[Lambda], 0, {1, 1, 1/2}, 0, 3, 1]  | SeriesData[\
\[Lambda], 0, {Ket[\"+1\"], Ket[\"0\"]/Sqrt[2] + Ket[\"-1\"]/4}, 0, \
2, 1]        |
```

## Time-Dependent Perturbation

### Time-Dependent Perturbation Theory

#### Problem Setup

Two schemes of the perturbation theory:

* **Time-independent perturbation**: corrections to energy levels, \
states, effective Hamiltonians.

* **Time-dependent perturbation**: corrections to time-evolution \
operators (propagators, Green\[CloseCurlyQuote]s functions).

The *time-dependent* perturbation theory is more general (because we \
can always set the perturbation to be time-independent afterwards).

Consider the Hamiltonian

```wl
$$\\hat{H}(t)=\\hat{H}_0+\\hat{V}(t).$$
```

* The spectrum of $$\\hat{H}_0$$ is known

```wl
$$\\hat{H}_0| n\\rangle =E_n| n\\rangle .$$
```

The basis states $$| n\\rangle$$ are fixed (time-independent), \
because $$\\hat{H}_0$$ is time-independent.

* All the time dependence is ascribed to the operator \
$$\\hat{V}(t)$$, which can be represented in the eigenbasis of \
$$\\hat{H}_0$$

```wl
$$\\hat{V}(t)=\\sum _{m,n} | m\\rangle V_{m\\, n}(t)\\langle n| .$$
```

$$V_{m\\, n}(t)$$ is expected to be small (compared to the energy \
scale of $$\\hat{H}_0$$) through out the time $$t$$.

Time-evolution of quantum states in the **Schrödinger picture** is \
governed by the **Schrödinger equation** (set $$\\hbar =1$$ for \
simplicity):

```wl
$$i\\partial _t| \\psi (t)\\rangle _{\\mathcal{S}}=\\hat{H}(t)| \\psi \
(t)\\rangle _{\\mathcal{S}}=\\left(\\hat{H}_0+\\hat{V}(t)\\right)| \
\\psi (t)\\rangle _{\\mathcal{S}}.$$
```

*Time-evolution* is **unitary**: the solution of $$| \\psi \
(t)\\rangle _{\\mathcal{S}}$$ must take the form of

```wl
$$| \\psi (t)\\rangle _{\\mathcal{S}}=\\hat{U}(t)| \\psi (0)\\rangle \
_{\\mathcal{S}}.$$
```

* This defines the *unitary* operator $$\\hat{U}(t)$$, called the \
**time-evolution operator**. Once we know $$\\hat{U}(t)$$, we can \
apply it to any initial state $$| \\psi (0)\\rangle _{\\mathcal{S}}$$ \
to obtain the final state $$| \\psi (t)\\rangle _{\\mathcal{S}}$$ (we \
don\[CloseCurlyQuote]t need to solve the Schrödinger equation over \
and over again).

Plug Eq. (XXX) to Eq. (XXX) leads to an equation for 
\\!\\(\\*OverscriptBox[\\(U\\), \\(^\\)]\\)(t),

```wl
$$i\\partial _t\\hat{U}(t)=\\hat{H}(t)\\hat{U}(t),$$
```

subject to the *initial condition*: $$\\hat{U}(0)=\\mathbf{1}$$. \
Note: this is *matrix* (or *operator*) equation, which has *many* \
*more* variables to solve than the Schrödinger equation.

This is a hard problem in general. But we know the solution for a \
special case: the **unperturbed case** when $$\\hat{V}(t)=0$$, where

```wl
$$i\\partial _t\\hat{U}_0(t)=\\hat{H}_0\\hat{U}_0(t).$$
```

The solution is given by

```wl
$$\\hat{U}_0(t)=e^{-i \\hat{H}_0t}=\\sum _n | n\\rangle e^{-i \
E_nt}\\langle n| .$$
```

Now suppose $$\\hat{V}(t)$$ is *small* (as a perturbation), \
$$\\hat{H}(t)$$ is only slightly modified from $$\\hat{H}_0$$, thus \
we expect that $$\\hat{U}(t)$$ is also close to $$\\hat{U}_0(t)$$ up \
to perturbative corrections. The goal of the **time-dependent \
perturbation theory** is to calculate these *corrections* in *power \
series* of $$\\hat{V}(t)$$.

```wl
$$\\begin{array}{ccc}
 \\hat{H}_0 & \\overset{+\\hat{V}(t)}{\\longrightarrow } & \
\\hat{H}(t) \\\\
 \\downarrow  &   & \\downarrow  \\\\
 \\hat{U}_0(t) & \\overset{+\\pmb{\\text{??}?}}{\\longrightarrow } & \
\\hat{U}(t) \\\\
\\end{array}$$
```

#### Interaction Picture

Strategy: changing the **frame of reference**. Switch to the \
*comoving* frame with the state (following the *unperturbed* \
evolution), so as to focus on the effect of the $$\\hat{V}(t)$$ \
perturbation.

Use $$\\hat{U}_0(t)$$ to transform everything to the **Interaction \
picture**.

* **State-level **formalism.

```wl
$$| \\psi (t)\\rangle _{\\mathcal{I}}=\\hat{U}_0^{\\dagger }(t)| \
\\psi (t)\\rangle _{\\mathcal{S}}=e^{i H_0t}| \\psi (t)\\rangle \
_{\\mathcal{S}},$$
```

Define the perturbation in the interaction picture:

```wl
$$V_{\\mathcal{I}}(t)=U_0^{\\dagger }(t)V(t)U_0(t)=\\sum _{m,n} | \
m\\rangle V_{m\\, n}(t)e^{i\\left(E_m-E_n\\right)t}\\langle n| .$$
```

The time-evolution of $$| \\psi (t)\\rangle _{\\mathcal{I}}$$ is \
described by

```wl
$$i\\partial _t| \\psi (t)\\rangle \
_{\\mathcal{I}}=V_{\\mathcal{I}}(t)| \\psi (t)\\rangle \
_{\\mathcal{I}}.$$
```

Show Eq. (XXX).

```wl
$$i\\partial _t| \\psi (t)\\rangle _{\\mathcal{I}}=i\\partial \
_t\\left(e^{i \\hat{H}_0t}| \\psi (t)\\rangle _{\\mathcal{S}}\\right)$$
$$=i\\partial _t\\left(e^{i \\hat{H}_0t}\\right)| \\psi (t)\\rangle \
_{\\mathcal{S}}+e^{i \\hat{H}_0t}i\\partial _t| \\psi (t)\\rangle \
_{\\mathcal{S}}$$
$$=e^{i \\hat{H}_0t}\\left(-\\hat{H}_0\\right)| \\psi (t)\\rangle \
_{\\mathcal{S}}+e^{i \
\\hat{H}_0t}\\left(\\hat{H}_0+\\hat{V}(t)\\right)| \\psi (t)\\rangle \
_{\\mathcal{S}}$$
$$=e^{i \\hat{H}_0t}\\hat{V}(t)| \\psi (t)\\rangle _{\\mathcal{S}}$$
$$=\\hat{U}_0^{\\dagger }(t)\\hat{V}(t)| \\psi (t)\\rangle \
_{\\mathcal{S}}$$
$$=\\hat{U}_0^{\\dagger \
}(t)\\hat{V}(t)\\hat{U}_0(t)\\hat{U}_0^{\\dagger }(t)| \\psi \
(t)\\rangle _{\\mathcal{S}}$$
$$=V_{\\mathcal{I}}(t)| \\psi (t)\\rangle _{\\mathcal{I}}.$$
```

* **Operator-level **formalism.

```wl
$$\\hat{U}_{\\mathcal{I}}(t)=\\hat{U}_0^{\\dagger }(t)\\hat{U}(t).$$

In[631]:=
Block[{r = 0.05}, Graphics[{{Arrowheads[0.06], AbsoluteThickness[1], \
Arrow[{{ - 0.2, 0}, {1.2, 0}}], Line[{0, # r / 3}& /@ { - 1, 1}]}, \
{Text[\[VeryThinSpace]t, {1.2, 0}, { - 1, 0}], Text[0, {0, 0}, {1, \
1}]}, {Arrowheads[{{0.05, 0.5}}], {Red, Arrow@BSplineCurve[{{0, r}, \
{1, r}, {1 + r / 2, r}, {1 + r, r / 2}, {1 + r, 0}}], Text[^
U (t), {0.5, r}, {0,  - 1}]}, {Blue, Arrow@BSplineCurve[{{1 + r, 0}, \
{1 + r,  - r / 2}, {1 + r / 2,  - r}, {1,  - r}, {0,  - r}}], Text[^\
\[Dagger]
U  (t)
 0, {0.5,  - r}, {0, 1}]}}}, ImageSize -> 180]]

Out[631]=
\\!\\(\\*GraphicsBox[{{AbsoluteThickness[1], Arrowheads[0.06], \
ArrowBox[{{-0.2, 0}, {1.2, 0}}], 
   LineBox[{{0, -0.016}, {0, 0.016}}]}, 
  {InsetBox[\"\\\"\\\\!\\\\(\[VeryThinSpace]t\\\\)\\\"\", {1.2, 0}, \
NCache[ImageScaled[{0, 1/2}], ImageScaled[{0, 0.5}]]], 
   InsetBox[\"\\\"\\\\! ... 7], 
    ArrowBox[BSplineCurveBox[{{1.05, 0}, {1.05, -0.025}, {1.025, \
-0.05}, {1, -0.05}, {0, -0.05}}]], 
    InsetBox[\"\\\"\\\\!\\\\(U\\\\&^\\\\_0\\\\%\[Dagger](t)\\\\)\\\"\"\
, {0.5, -0.05}, NCache[ImageScaled[{1/2, 1}], 
      ImageScaled[{0.5, 1}]]]}}}, ImageSize -> 180]\\)
```

Subscript[
\\!\\(\\*OverscriptBox[\\(U\\), \\(^\\)]\\), \\[ScriptCapitalI]](t) \
captures the \"additional\" unitary evolution implemented by 
\\!\\(\\*OverscriptBox[\\(U\\), \\(^\\)]\\)(t) compared to the \
reference Subscript[
\\!\\(\\*OverscriptBox[\\(U\\), \\(^\\)]\\), 0](t). Following the \
similar derivation in Eq. (XXX), we can show that Subscript[
\\!\\(\\*OverscriptBox[\\(U\\), \\(^\\)]\\), \\[ScriptCapitalI]](t) \
is governed by

```wl
$$i\\partial \
_t\\hat{U}_{\\mathcal{I}}(t)=\\hat{V}_{\\mathcal{I}}(t)\\hat{U}_{\\\
mathcal{I}}(t),$$
```

subject to the initial condition: \
$$\\hat{U}_{\\mathcal{I}}(0)=\\mathbf{1}$$. The solution of \
$$\\hat{U}_{\\mathcal{I}}(t)$$ can be used

	* to provide the universal solution for $$| \\psi (t)\\rangle \
_{\\mathcal{I}}=\\hat{U}_{\\mathcal{I}}(t)| \\psi (0)\\rangle \
_{\\mathcal{I}}$$,

	* and to construct \
$$\\hat{U}(t)=\\hat{U}_0(t)\\hat{U}_{\\mathcal{I}}(t)$$.

There is no explicit dependence on Subscript[
\\!\\(\\*OverscriptBox[\\(H\\), \\(^\\)]\\), 0] in either Eq. (XXX) \
or Eq. (XXX), which allows us to focus on the perturbation Subscript[
\\!\\(\\*OverscriptBox[\\(V\\), \\(^\\)]\\), \\[ScriptCapitalI]](t).

#### Dyson Series

Integrating both sides of Eq. (XXX) in time

```wl
$$i\\hat{U}_{\\mathcal{I}}(t)-i\\hat{U}_{\\mathcal{I}}(0)=i\\int \
_0^tdt'\\partial _{t'}\\hat{U}_{\\mathcal{I}}\\left(t'\\right)=\\int \
_0^tdt'\\hat{V}_{\\mathcal{I}}\\left(t'\\right)\\hat{U}_{\\mathcal{I}}\
\\left(t'\\right),$$
```

plugging in the initial condition Subscript[
\\!\\(\\*OverscriptBox[\\(U\\), \\(^\\)]\\), \\[ScriptCapitalI]](
  0) = \\[DoubleStruckOne], we obtain an integral equation, \
equivalent to the differential equation Eq. (XXX),

```wl
$$\\hat{U}_{\\mathcal{I}}(t)=\\mathbf{1}-i\\int \
_0^tdt'\\hat{V}_{\\mathcal{I}}\\left(t'\\right)\\hat{U}_{\\mathcal{I}}\
\\left(t'\\right).$$
```

This provides a *self-consistent* equation for \
$$\\hat{U}_{\\mathcal{I}}(t)$$. If we take this expression and \
substitute $$\\hat{U}_{\\mathcal{I}}\\left(t'\\right)$$ under the \
integrand, we obtain

```wl
$$\\hat{U}_{\\mathcal{I}}(t)=\\mathbf{1}-i\\int \
_0^tdt'\\hat{V}_{\\mathcal{I}}\\left(t'\\right)+(-i)^2\\int \
_0^tdt'\\hat{V}_{\\mathcal{I}}\\left(t'\\right)\\int
_0^{t'}dt^{\\prime\\prime \
}\\hat{V}_{\\mathcal{I}}\\left(t^{\\prime\\prime \
}\\right)\\hat{U}_{\\mathcal{I}}\\left(t^{\\prime\\prime }\\right).$$
```

Iterating this procedure, we obtain a formal solution in power series \
of $$\\hat{V}_{\\mathcal{I}}$$, known as the **Dyson series** :

```wl
$$\\hat{U}_{\\mathcal{I}}(t)=\\sum _{k=0}^{\\infty } (-i)^k\\int \
_0^tdt_k\\int _0^{t_k}dt_{k-1}\\ldots \\int \
_0^{t_2}dt_1\\hat{V}_{\\mathcal{I}}\\left(t_k\\right)\\hat{V}_{\\\
mathcal{I}}\\left(t_{k-1}\\right)\\ldots
\\hat{V}_{\\mathcal{I}}\\left(t_1\\right).$$
```

where the $$k=0$$ term corresponds to $$\\mathbf{1}$$. The operators \
$$\\hat{V}_{\\mathcal{I}}(t)$$ are organized in a *time-ordered* \
sequence with $$0\\leq t_1\\leq \\ldots \\leq t_{k-1}\\leq t_k\\leq \
t$$. Rule: *earlier* operator on the *right*, *later* operator on the \
*left*.

#### Green\[CloseCurlyQuote]s Function

Let us take a closer look at the product of \
$$\\hat{V}_{\\mathcal{I}}$$ in the Dyson series. By definition \
$$\\hat{V}_{\\mathcal{I}}(t)=\\hat{U}_0^{\\dagger \
}(t)\\hat{V}(t)\\hat{U}_0(t)$$,

```wl
$$\\hat{V}_{\\mathcal{I}}\\left(t_k\\right)\\hat{V}_{\\mathcal{I}}\\\
left(t_{k-1}\\right)\\ldots \\hat{V}_{\\mathcal{I}}\\left(t_1\\right)$$
$$=\\hat{U}_0^{\\dagger }\\left(t_k\\right)\\hat{V}\\left(t_k\\right)\
\\hat{U}_0\\left(t_k\\right)\\hat{U}_0^{\\dagger \
}\\left(t_{k-1}\\right)\\hat{V}\\left(t_{k-1}\\right)\\hat{U}_0\\left(\
t_{k-1}\\right)\\ldots
\\hat{U}_0^{\\dagger \
}\\left(t_1\\right)\\hat{V}\\left(t_1\\right)\\hat{U}_0\\left(t_1\\\
right).$$
```

This motivates us to introduce the unitary operator \
$$\\hat{G}_0\\left(t,t'\\right)$$, known as the **bare Green\
\[CloseCurlyQuote]s function** or the **bare propagator**,

```wl
$$\\hat{G}_0\\left(t,t'\\right)=\\hat{U}_0(t)\\hat{U}_0^{\\dagger \
}\\left(t'\\right)=\\sum _n | n\\rangle e^{-i E_n\\left(t-t'\\right)}\
\\langle n| ,$$
```

which propagates the state from time $$t'$$ to $$t$$. In terms of the \
bare Green\[CloseCurlyQuote]s function,

```wl
$$\\hat{V}_{\\mathcal{I}}\\left(t_k\\right)\\hat{V}_{\\mathcal{I}}\\\
left(t_{k-1}\\right)\\ldots \\hat{V}_{\\mathcal{I}}\\left(t_1\\right)$$
$$=\\hat{U}_0^{\\dagger \
}(t)\\hat{G}_0\\left(t,t_k\\right)\\hat{V}\\left(t_k\\right)\\hat{G}_\
0\\left(t_k,t_{k-1}\\right)\\hat{V}\\left(t_{k-1}\\right)\\ldots  \
\\hat{G}_0\\left(t_2,t_1\\right)\\hat{V}\\left(t_1\\right)\\hat{G}_0\\\
left(t_1,0\\right).$$
```

The left most \\!\\(
\\*SubsuperscriptBox[
OverscriptBox[\\(U\\), \\(^\\)], \\(0\\), \\(\\[Dagger]\\)](t)\\) can \
be canceled out if we consider the time-evolution operator in the \
Schrödinger picture, i.e. 
\\!\\(\\*OverscriptBox[\\(U\\), \\(^\\)]\\)(t) = Subscript[
\\!\\(\\*OverscriptBox[\\(U\\), \\(^\\)]\\), 0](t) Subscript[
\\!\\(\\*OverscriptBox[\\(U\\), \\(^\\)]\\), \\[ScriptCapitalI]](t). \
According to Eq. (XXX) and Eq. (XXX), we have

```wl
$$\\hat{U}(t)=\\sum _{k=0}^{\\infty } (-i)^k\\int _0^tdt_k\\int \
_0^{t_k}dt_{k-1}\\ldots \\int \
_0^{t_2}dt_1\\hat{G}_0\\left(t,t_k\\right)\\hat{V}\\left(t_k\\right)\\\
hat{G}_0\\left(t_k,t_{k-1}\\right)\\hat{V}\\left(t_{k-1}\\right)\\ldots
 \\hat{G}_0\\left(t_2,t_1\\right)\\hat{V}\\left(t_1\\right)\\hat{G}_0\
\\left(t_1,0\\right).$$
```

Further define the **dressed Green\[CloseCurlyQuote]s function** (or \
the **dressed propagator**) as

```wl
$$\\hat{G}\\left(t,t'\\right)=\\hat{U}(t)\\hat{U}^{\\dagger \
}\\left(t'\\right),$$
```

then Eq. (XXX) can be written as

```wl
$$\\hat{G}\\left(t,t_0\\right)=\\sum _{k=0}^{\\infty } (-i)^k\\int \
_{t_0}^tdt_k\\int _{t_0}^{t_k}dt_{k-1}\\ldots \\int \
_{t_0}^{t_2}dt_1\\hat{G}_0\\left(t,t_k\\right)\\hat{V}\\left(t_k\\\
right)\\hat{G}_0\\left(t_k,t_{k-1}\\right)\\hat{V}\\left(t_{k-1}\\\
right)\\ldots
 \\hat{G}_0\\left(t_2,t_1\\right)\\hat{V}\\left(t_1\\right)\\hat{G}_0\
\\left(t_1,t_0\\right),$$
```

where we have generalized the initial time to $$t_0$$. This is the \
**Dyson series** for Green\[CloseCurlyQuote]s function.

* $$\\hat{G}\\left(t,t'\\right)$$ can be calculated in *power series* \
of $$\\hat{V}(t)$$ given $$\\hat{G}_0\\left(t,t'\\right)$$.

* Since $$\\hat{U}(t)=\\hat{G}(t,0)$$, we also know how to calculate \
$$\\hat{U}(t)$$ in power series of $$\\hat{V}(t)$$.

So we have reached our goal!

#### Feynman Diagrams

However, the formula Eq. (XXX) looks complicated. Let us develop some \
physical intuitions using Feynman diagrams.

* A directed *single-line* link: the *bare* Green\[CloseCurlyQuote]s \
function from one time to another,

```wl
$$=\\hat{G}_0\\left(t,t'\\right).$$
```

The arrow specifies the direction of time (from past to future).

* A solid node: the perturbation operator at a particular time,

```wl
$$_t=-i \\hat{V}(t).$$
```

* Connecting links and nodes: identifying the time together

```wl
$$\\underset{
\\begin{array}{ccccc}
 t_0 &   & t_1 &   & t_2 \\\\
\\end{array}
}{}=\\hat{G}_0\\left(t_2,t_1\\right)\\left(-i \
\\hat{V}\\left(t_1\\right)\\right)\\hat{G}_0\\left(t_1,t_0\\right).$$
```

Note: in the diagram, the time flows along the arrow from left to \
right; but in the operator product, the operator acts in sequence \
from right to left. Things are *mirror image* (left-right reversed) \
to each other with respect to the \[OpenCurlyDoubleQuote]$$=$$\
\[CloseCurlyDoubleQuote] sign.

* If the time is not labeled explicitly, then

	* the time of the *outmost* node (the initial and final nodes) is \
*fixed*, (convention: $$t_0$$ - the initial time, $$t$$ - the final \
time),

	* the time of the *internal* node will be automatically integrated \
over, and the integration goes through all possible arrangements \
preserving the *time-ordering*.

```wl
$$=\\hat{G}_0\\left(t,t_0\\right),\\\\
=(-i )\\int \
_{t_0}^tdt_1\\hat{G}_0\\left(t,t_1\\right)\\hat{V}\\left(t_1\\right)\\\
hat{G}_0\\left(t_1,t_0\\right),\\\\
=(-i )^2\\int _{t_0}^tdt_2\\int \
_{t_0}^{t_2}dt_1\\hat{G}_0\\left(t,t_2\\right)\\hat{V}\\left(t_2\\\
right)\\hat{G}_0\\left(t_2,t_1\\right)\\hat{V}\\left(t_1\\right)\\hat{\
G}_0\\left(t_1,t_0\\right),\\\\
\\ldots$$
```

* A directed *double-line* link: the *dressed* \
Green\[CloseCurlyQuote]s function from one time to another,

```wl
$$=\\hat{G}\\left(t,t_0\\right).$$
```

With the diagrammatic representations in Eq. (XXX) and Eq. (XXX), we \
can rewrite Eq. (XXX) as

```wl
$$=+++\\ldots .$$
```

* If we turn off the perturbation, i.e.V(t) = 0 or \
DiagramEditor`Diagram[{{}, {}, {
   1}}, {}, {}, {}, {}, {1 -> {0., 0.}}, {1 -> {{\"Dot\"}}}] = 0, Eq. \
(XXX) reduces to

```wl
$$=,$$
```

as all the diagrams containing the node will vanish. This simply \
restores \
$$\\hat{G}\\left(t,t_0\\right)=\\hat{G}_0\\left(t,t_0\\right)$$ in \
the absence of perturbation.

* In the presence of $$V(t)$$, the propagator is dressed \
order-by-order by *scattering* with the perturbation \
DiagramEditor`Diagram[{{}, {}, {1}}, {}, {}, {}, {}, {1 -> {0., 0.}}, \
{1 -> {{\"Dot\"}}}]. For example, DiagramEditor`Diagram[{{}, {1, 2}, \
{3, 4, 5}}, {1 -> {3, 5}, 2 -> {5, 4}}, {}, {}, 
 {1 -> 0, 2 -> 0}, {3 -> {-0.4, 0.}, 4 -> {0.4, 0.}, 5 -> {0., 0.}}, 
 {1 -> {{\"Line\"}, {\"Arrow\"}}, 2 -> {{\"Line\"}, {\"Arrow\"}}, 3 -> \
{{\"None\"}}, 4 -> {{\"None\"}}, 
  5 -> {{\"Dot\"}}}] describes that the system is first propagated to \
an intermediate time, acted by the perturbation operator, and then \
continued to propagate to the final time. Other diagrams describe \
higher order processes. The full propagation is the sum of all \
possible processes.

### Energy Level Transitions

#### Transition Probability

If a system is prepared in an **initial state** $$| i\\rangle$$ at \
time $$t_0$$, at a subsequent time $$t$$, the initial state will \
evolve to $$\\hat{G}\\left(t,t_0\\right)| i\\rangle$$. Then the \
*probability* to find the system in a **final state** $$| f\\rangle$$ \
should be given by

```wl
$$P_{i\\rightarrow f}=\\left| \\langle f| \
\\hat{G}\\left(t,t_0\\right)| i\\rangle \\right| {}^2.$$
```

$$P_{i\\to f}$$ is known as the **transition probability**.

To the 1st order in $$\\hat{V}(t)$$, for $$i\\neq f$$, the transition \
probability reads

```wl
$$P_{i\\rightarrow f}\\left(t,t_0\\right)=\\left| \\int \
_{t_0}^tdt_1\\langle f| \\hat{V}\\left(t_1\\right)| i\\rangle e^{i \
\\omega _{f\\, i}t_1}\\right| {}^2,$$
```

where $$\\omega _{f\\, i}=E_f-E_i$$ is the energy difference.

Prove Eq. (XXX)

To the 1st order in 
\\!\\(\\*OverscriptBox[\\(V\\), \\(^\\)]\\)(t), Eq. (XXX) reads

```wl
$$\\hat{G}\\left(t,t_0\\right)\\simeq \
\\hat{G}_0\\left(t,t_0\\right)-i \\int \
_{t_0}^tdt_1\\hat{G}_0\\left(t,t_1\\right)\\hat{V}\\left(t_1\\right)\\\
hat{G}_0\\left(t_1,t_0\\right)+\\ldots
,$$
```

where Subscript[
\\!\\(\\*OverscriptBox[\\(G\\), \\(^\\)]\\), 0](t, Derivative[1][t]) = 
\\!\\(\\*UnderscriptBox[\\(\\[Sum]\\), \\(n\\)]\\)Ket[{n}] E^(-I \
Subscript[E, 
     n](t - Derivative[1][t])) Bra[{n}] is given in Eq. (XXX). \
Suppose Ket[{i}] and Ket[{f}] are eigenstates of Subscript[H, 0], we \
have

```wl
$$\\langle f| \\hat{G}\\left(t,t_0\\right)| i\\rangle \\simeq \
\\langle f| \\hat{G}_0\\left(t,t_0\\right)| i\\rangle -i \\int \
_{t_0}^tdt_1\\langle f| \
\\hat{G}_0\\left(t,t_1\\right)\\hat{V}\\left(t_1\\right)\\hat{G}_0\\\
left(t_1,t_0\\right)|
i\\rangle$$
$$=e^{-i\\left(E_ft+E_it_0\\right)}\\delta _{f\\, i}-i\\int \
_{t_0}^tdt_1e^{-i E_f\\left(t-t_1\\right)}\\langle f| \
\\hat{V}\\left(t_1\\right)| i\\rangle e^{-i
E_i\\left(t_1-t_0\\right)}$$
$$=e^{-i\\left(E_ft+E_it_0\\right)}\\left(\\delta _{f\\, i}-i\\int \
_{t_0}^tdt_1\\langle f| \\hat{V}\\left(t_1\\right)| i\\rangle \
e^{i\\left(E_f-E_i\\right)t_1}\\right)$$
```

#### Fermi\[CloseCurlyQuote]s Golden Rule

Consider a system prepared in an initial state $$| i\\rangle$$ and \
perturbed by a periodic operator abruptly switched on at time \
$$t_0=0$$.

```wl
$$\\hat{V}(t)=
\\begin{array}{ll}
 \\{ & 
\\begin{array}{ll}
 \\hat{V} e^{-i \\omega  t} & t>0 \\\\
 0 & t\\leq 0 \\\\
\\end{array}
 \\\\
\\end{array}
.$$
```

What is the probability that, at some later time t, the system is \
found to be in the state Ket[{f}]. From Eq. (XXX), we have

```wl
$$P_{i\\rightarrow f}(t)=\\left| \\int _0^tdt_1\\langle f| \\hat{V}| \
i\\rangle e^{i\\left(\\omega _{f\\, i}-\\omega \\right)t_1}\\right| \
{}^2$$
$$=\\left| \\langle f| \\hat{V}| i\\rangle \\frac{e^{i\\left(\\omega \
_{f\\, i}-\\omega \\right)t}-1}{i\\left(\\omega _{f\\, i}-\\omega \
\\right)}\\right| {}^2$$
$$=\\left| \\langle f| \\hat{V}| i\\rangle \\right| \
^2\\left(\\frac{\\sin \\left(\\left(\\omega _{f\\, i}-\\omega \
\\right)t/2\\right)}{\\left.\\left(\\omega _{f\\,
i}-\\omega \\right)\\right/2}\\right){}^2$$
```

Setting $$\\alpha =\\left.\\left(\\omega _{f\\, i}-\\omega \
\\right)\\right/2$$, the transition probability takes the form of $$(\
\\sin (\\alpha  t)/\\alpha )^2$$ with a peak at $$\\alpha =0$$, with \
maximum value $$t^2$$ and width of order $$1/t$$ giving a total \
weight of order $$t$$.

```wl
In[60]:=
Plot[Sinc[\[Alpha]] ^ 2, {\[Alpha],  - 15, 15}, Epilog -> {Text[t = \
1, Scaled@{1, 1}, {1.5, 1.5}]}, FrameLabel -> {\[Alpha] = (\[Omega]   \
 - \[Omega])/2
      f\[VeryThinSpace]i,             2
(sin (\[Alpha]t)/\[Alpha])}, PlotStyle -> Black, PlotRange -> All, \
ImageSize -> 200]

Out[60]=
\\!\\(\\*GraphicsBox[{{{}, {}, TagBox[{GrayLevel[0], \
AbsolutePointSize[4], AbsoluteThickness[1.6], 
     Opacity[1.], LineBox[{{-14.999, 0.001}, {-14.990, 
      0.001}, {-14.981, 0.001}, {-14.963, 
      0.002}, {-14.926, 0.002}, {-14.852, 
      0.002 ... & )[#1[[2]]]} & )}}, 
 PlotRange -> {All, All}, PlotRangeClipping -> True, 
 PlotRangePadding -> {{Scaled[0.02], Scaled[0.02]}, {Scaled[0.05], \
Scaled[0.05]}}, 
 Ticks -> {Automatic, Automatic}, TicksStyle -> \
Directive[GrayLevel[0], FontSize -> 12]]\\)
```

In the **long-time limit** of $$t\\to \\infty$$,

```wl
$$\\lim_{t\\rightarrow \\infty } \\frac{1}{t}\\left(\\frac{\\sin  \
\\alpha  t}{\\alpha }\\right)^2=\\pi  \\delta (\\alpha )=2\\pi  \
\\delta (2\\alpha ).$$
```

This leads to the following expression for the **transition rate**,

```wl
$$W_{i\\rightarrow f}=\\lim_{t\\to \\infty } \\frac{P_{i\\to \
f}(t)}{t}=2\\pi \\left| \\langle f| \\hat{V}| i\\rangle \\right| \
^2\\delta \\left(E_f-E_i-\\omega \\right).$$
```

This is known as **Fermi\[CloseCurlyQuote]s golden rule**.

* One might worry that in the $$t\\to \\infty$$ limit, the transition \
probability is in fact diverging. How can we justify the use of \
perturbation theory? For a transition with $$\\omega _{f\\, i}\\neq \
\\omega$$, the \[OpenCurlyDoubleQuote]long time\
\[CloseCurlyDoubleQuote] limit is reached when $$t\\gg \
1\\left/\\left(\\omega _{f\\, i}-\\omega \\right)\\right.$$, a value \
that can still be very short compared with the mean transition time, \
which is set by the matrix element $$1\\left/\\left| \\langle f| \
\\hat{V}| i\\rangle \\right| \\right.$$.

* Energy conservation is enforced in the long-time limit

```wl
$$E_f-E_i=\\omega ,$$
```

such that transition occurs between levels in resonant with the the \
frequency of the perturbation.

#### Adiabatic Process

Consider the perturbation is gradually turn on following an \
exponential grow from the infinite past (and switch off after $$t=0$$)

```wl
$$\\hat{V}(t)=
\\begin{array}{ll}
 \\{ & 
\\begin{array}{ll}
 \\hat{V} e^{t/\\tau } & t<0 \\\\
 0 & t\\geq 0 \\\\
\\end{array}
 \\\\
\\end{array}
.$$

In[68]:= Plot[Exp[t]UnitStep[ - t], {t,  - 5, 2}, PlotStyle -> Black, \
PlotRange -> All, FrameLabel -> {\[VeryThinSpace]t, V (t)}, ImageSize \
-> 180]

Out[68]=
\\!\\(\\*GraphicsBox[{{{{}, {}, TagBox[{GrayLevel[0], \
AbsolutePointSize[4], AbsoluteThickness[1.6], 
      Opacity[1.], LineBox[{{-4.999, 0.006}, {-4.997, 
       0.006}, {-4.995, 0.006}, {-4.991, 
       0.006}, {-4.982, 0.006}, {-4.965, 
       0.006} ... & )[#1[[2]]]} & )}}, 
 PlotRange -> {All, All}, PlotRangeClipping -> True, 
 PlotRangePadding -> {{Scaled[0.02], Scaled[0.02]}, {Scaled[0.05], \
Scaled[0.05]}}, 
 Ticks -> {Automatic, Automatic}, TicksStyle -> \
Directive[GrayLevel[0], FontSize -> 12]]\\)
```

Suppose the system is prepared in state $$| i\\rangle$$ in the \
infinite past ($$t_0\\to -\\infty$$), what is the probability for the \
system to transit to the state $$| f\\rangle$$ at $$t=0$$ ?

According to Eq. (XXX),

```wl
$$P_{i\\rightarrow f}=\\left| \\int _{-\\infty }^0dt_1\\langle f| \
\\hat{V}| i\\rangle e^{\\left.t_1\\right/\\tau }e^{i \\omega _{f\\, \
i}t_1}\\right| {}^2$$
$$=\\frac{\\left| \\langle f| \\hat{V}| i\\rangle \\right| \
^2}{\\left(E_f-E_i\\right){}^2+1\\left/\\tau ^2\\right.}.$$
```

The transition probability exhibits a resonance around $$\\omega \
_f=\\omega _i$$: states are more likely to hybridize when they are \
closer in energy.

```wl
In[639]:=
Plot[1 / (\[Omega] ^ 2 + 1), {\[Omega],  - 5, 5}, PlotStyle -> Black, \
FrameLabel -> {(E  - E ) \[Tau]
  f    i,                2
P     /\[LeftBracketingBar] V    \[RightBracketingBar]
 i \[RightArrow] f    f\[VeryThinSpace]i}, ImageSize -> 200]

Out[639]=
\\!\\(\\*GraphicsBox[{{{}, {}, TagBox[{GrayLevel[0], \
AbsolutePointSize[4], AbsoluteThickness[1.6], 
     Opacity[1.], LineBox[{{-4.999, 0.038}, {-4.996, 
      0.038}, {-4.993, 0.038}, {-4.987, 
      0.038}, {-4.975, 0.038}, {-4.950, 
      0.039}, {-4 ... } & )}}, 
 PlotRange -> {{-5, 5}, {0., 0.999}}, PlotRangeClipping -> True, 
 PlotRangePadding -> {{Scaled[0.02], Scaled[0.02]}, {Scaled[0.05], \
Scaled[0.05]}}, 
 Ticks -> {Automatic, Automatic}, TicksStyle -> \
Directive[GrayLevel[0], FontSize -> 12]]\\)
```

In the **adiabatic limit** of $$\\tau \\to \\infty$$, the \
perturbation is turned on *very slowly*, such that the $$\\hat{H}_0$$ \
eigenstate $$| i\\rangle$$ simply evolves to the corresponding \
eigenstate of $$\\hat{H}=\\hat{H}_0+\\hat{V}$$, which is given by

```wl
$$| i(V)\\rangle =| i\\rangle +\\sum _{m\\neq i} | m\\rangle \
\\frac{V_{m\\, i}}{E_i-E_m}+\\ldots ,$$
```

according to the time-independent perturbation, c.f. Eq. (XXX). Then \
the probability to observe the system in the state Ket[{f}] will be

```wl
$$| \\langle f|i(V)\\rangle | ^2=\\frac{\\left| V_{f\\, i}\\right| \
{}^2}{\\left(E_i-E_f\\right){}^2},$$
```

which matches the result of time-dependent perturbation Eq. (XXX) in \
the limit of \\[Tau] -> \\[Infinity]. Thus we have verified that the \
time-dependent perturbation falls back to the time-independent \
perturbation if the perturbation changes slow enough in time.

On the other hand, for any realistic physical process, the time scale \
$$\\tau$$ can not be infinitely long. A finite $$\\tau$$ sets an \
*energy resolution* $$\\tau ^{-1}$$ (due to the *uncertainty \
principle*), below which the energy level resonance is smoothed out. \
So the singularity of the energy denominator in the time-independent \
perturbation do not actually occur in reality.

Consider a three-level quantum system with orthonormal basis states \
$$| 1\\rangle$$, $$| 2\\rangle$$, $$| 3\\rangle$$. The unperturbed \
Hamiltonian is 
$$\\hat{H}_0=\\Delta | 3\\rangle \\langle 3|$$,
with $$\\Delta >0$$. The states $$| 1\\rangle$$ and $$| 2\\rangle$$ \
are degenerated at zero energy, while $$| 3\\rangle$$ lies at energy \
$$\\Delta$$. At time $$t=0$$, the system is initially prepared in \
state $$| 1\\rangle$$.
Now introduce a time-dependent perturbation 
$$\\hat{V}(t)=\\lambda (t)((| 1\\rangle +| 2\\rangle )\\langle 3| \
+h.c.)$$,
where $$\\lambda (t)=\\lambda _0\\cos (\\omega  t)$$ with $$\\lambda \
_0\\in \\mathbb{R}$$ being a small parameter.
(i) Construct the bare Green\[CloseCurlyQuote]s function $$\\hat{G}_0\
\\left(t,t'\\right)$$.
(ii) Analyze the Dyson series and determine the lowest nonzero order \
in $$\\lambda _0$$ that contributes to the transition amplitude \
$$\\langle 2| \\hat{G}(t,0)| 1\\rangle$$.
(iii) Compute this leading-order behavior of the transition amplitude \
$$\\langle 2| \\hat{G}(t,0)| 1\\rangle$$ in the long-time limit as $$\
\\omega ^{-1},\\Delta ^{-1}\\ll t\\ll \\lambda _0^{-1}$$.
(iv) Analyze the behavior of the transition rate \
$$P_{1\\text{-$>$}2}(t)=\\left| \\langle 2| \\hat{G}(t,0)| 1\\rangle \
\\right| ^2$$. How does it scales with $$t$$? How does it depend on \
the frequency ratio $$\\omega /\\Delta$$ ?

Solution (HW XXX)

(i) Bare Green\[CloseCurlyQuote]s function

```wl
$$\\hat{G}_0\\left(t,t'\\right)=\\sum _{n=1}^3 | n\\rangle e^{-i \
E_n\\left(t-t'\\right)}\\langle n| ,$$
```

where $$E_1=E_2=0$$ and $$E_3=\\Delta$$. Thus,

```wl
$$\\hat{G}_0\\left(t,t'\\right)=| 1\\rangle \\langle 1| +| 2\\rangle \
\\langle 2| +e^{-i \\Delta  \\left(t-t'\\right)}| 3\\rangle \\langle \
3| .$$
```

(ii) We are interested in the transition amplitude $$\\langle 2| \
\\hat{G}(t,0)| 1\\rangle$$, which is given by the Dyson series as

```wl
$$\\langle 2| \\hat{G}(t,0)| 1\\rangle =\\langle 2| \
\\hat{G}_0\\left(t,t_0\\right)| 1\\rangle +(-i )\\int \
_{t_0}^tdt_1\\langle 2| \
\\hat{G}_0\\left(t,t_1\\right)\\hat{V}\\left(t_1\\right)\\hat{G}_0\\\
left(t_1,t_0\\right)|
1\\rangle +\\\\
(-i )^2\\int _{t_0}^tdt_2\\int _{t_0}^{t_2}dt_1\\langle 2| \\hat{G}_0\
\\left(t,t_2\\right)\\hat{V}\\left(t_2\\right)\\hat{G}_0\\left(t_2,t_\
1\\right)\\hat{V}\\left(t_1\\right)\\hat{G}_0\\left(t_1,t_0\\right)|
1\\rangle +\\ldots$$
```

* $$\\langle 2| \\hat{G}_0\\left(t,t'\\right)| 1\\rangle =0$$, so the \
0th order term vanishes.

* $$\\langle 2| \\hat{V}(t)| 1\\rangle =0$$, so the 1st order term \
also vanishes.

* The first non-vanishing contribution arises from the 2nd order \
term, via the perturbation that connects $$| 1\\rangle \
\\leftrightarrow | 3\\rangle \\leftrightarrow | 2\\rangle$$, \
involving intermediate (virtual) transition through $$| 3\\rangle$$.

Therefore the leading order contribution is at 2nd order in \
$$\\lambda _0$$ :

```wl
$$\\langle 2| \\hat{G}(t,0)| 1\\rangle \\approx (-i )^2\\int _0^tdt_2\
\\int _0^{t_2}dt_1\\langle 2| \
\\hat{G}_0\\left(t,t_2\\right)\\hat{V}\\left(t_2\\right)\\hat{G}_0\\\
left(t_2,t_1\\right)\\hat{V}\\left(t_1\\right)\\hat{G}_0\\left(t_1,0\\\
right)|
1\\rangle$$
$$=-\\int _0^tdt_2\\int _0^{t_2}dt_1\\langle 2| \
\\hat{V}\\left(t_2\\right)\\hat{G}_0\\left(t_2,t_1\\right)\\hat{V}\\\
left(t_1\\right)| 1\\rangle ,$$
```

where the only non-trivial perturbation path is

```wl
$$=-\\int _0^tdt_2\\int _0^{t_2}dt_1\\langle 2| \
\\hat{V}\\left(t_2\\right)| 3\\rangle \\langle 3| \
\\hat{G}_0\\left(t_2,t_1\\right)| 3\\rangle \\langle 3| \
\\hat{V}\\left(t_1\\right)|
1\\rangle .$$
```

The relevant matrix elements are

```wl
$$\\langle 3| \\hat{V}\\left(t_1\\right)| 1\\rangle =\\lambda \
\\left(t_1\\right),\\\\
\\langle 2| \\hat{V}\\left(t_2\\right)| 3\\rangle =\\lambda \
\\left(t_2\\right),\\\\
\\langle 3| \\hat{G}_0\\left(t_2,t_1\\right)| 3\\rangle =e^{-i \
\\Delta  \\left(t_2-t_1\\right)},$$
```

So

```wl
$$\\langle 2| \\hat{G}(t,0)| 1\\rangle \\approx -\\int _0^tdt_2\\int \
_0^{t_2}dt_1\\lambda \\left(t_1\\right)\\lambda \
\\left(t_2\\right)e^{-i \\Delta  \\left(t_2-t_1\\right)}.$$
```

(iii) Substitute $$\\lambda (t)=\\lambda _0 \\cos (\\omega  t)$$, then

```wl
$$\\langle 2| \\hat{G}(t,0)| 1\\rangle \\approx -\\lambda _0^2\\int \
_0^tdt_2\\int _0^{t_2}dt_1\\cos \\left(\\omega  t_1\\right)\\cos \
\\left(\\omega  t_2\\right)e^{-i
\\Delta  \\left(t_2-t_1\\right)}$$
$$=-\\frac{\\lambda _0^2}{4}\\int _0^tdt_2\\int \
_0^{t_2}dt_1\\left(e^{i (\\Delta +\\omega ) t_1}e^{i (-\\Delta \
+\\omega ) t_2}+e^{i (\\Delta -\\omega ) t_1}e^{i
(-\\Delta +\\omega ) t_2}+e^{i (\\Delta +\\omega ) t_1}e^{i (-\\Delta \
-\\omega ) t_2}+e^{i (\\Delta -\\omega ) t_1}e^{i (-\\Delta -\\omega \
) t_2}\\right),$$
```

which splits to four integrals. The integrals all takes the following \
form, which can be evaluated as

```wl
$$\\int _0^tdt_2\\int _0^{t_2}dt_1e^{i \\Omega _1t_1}e^{i \\Omega \
_2t_2}$$
$$=\\int _0^tdt_2\\frac{e^{i \\Omega _1t_2}-1}{i \\Omega _1}e^{i \
\\Omega _2t_2}$$
$$=\\frac{1}{i \\Omega _1}\\int _0^tdt_2\\left(e^{i \\left(\\Omega \
_1+\\Omega _2\\right)t_2}-e^{i \\Omega _2t_2}\\right)$$
$$=\\frac{1}{i \\Omega _1}\\left(\\frac{e^{i \\left(\\Omega \
_1+\\Omega _2\\right)t}-1}{i \\left(\\Omega _1+\\Omega \
_2\\right)}-\\frac{e^{i \\Omega _2t}-1}{i \\Omega
_2}\\right)$$
$$=\\frac{\\left(\\Omega _1+\\Omega _2\\right)\\left(e^{i \\Omega \
_2t}-1\\right)-\\Omega _2\\left(e^{i \\left(\\Omega _1+\\Omega \
_2\\right)t}-1\\right)}{\\Omega
_1\\Omega _2\\left(\\Omega _1+\\Omega _2\\right)}$$
$$=\\frac{1}{\\Omega _1\\Omega _2\\left(\\Omega _1+\\Omega \
_2\\right)}\\left(\\Omega _1\\left(e^{i \\Omega \
_2t}-1\\right)-\\Omega _2\\left(e^{i \\Omega _1t}-1\\right)e^{i
\\Omega _2t}\\right).$$
```

In the long-time limit, when $$t\\gg 1$$,

* The phase factors $$e^{i \\Omega _1t}$$ or $$e^{i \\Omega _2t}$$ \
simply oscillates on the complex unit circle. In general, the result \
will be of order 1, unless $$\\Omega _1\\text{-$>$}0$$, $$\\Omega \
_2\\text{-$>$}0$$, or $$\\Omega _1+\\Omega _2\\text{-$>$}0$$ (causing \
the denominator to diverge).

* Specifically, $$\\Omega _1=\\Delta \\pm \\omega$$ and $$\\Omega \
_2=-\\Delta \\pm \\omega$$ might not vanish in general, but their sum \
$$\\Omega _1+\\Omega _2$$ can vanish in two of the four integrals.

* When $$\\Omega _1+\\Omega _2\\text{-$>$}0$$, the integral becomes

```wl
$$\\int _0^tdt_2\\int _0^{t_2}dt_1e^{i \\Omega _1t_1}e^{-i \\Omega \
_1t_2}$$
$$=\\int _0^tdt_2\\frac{e^{i \\Omega _1t_2}-1}{i \\Omega _1}e^{-i \
\\Omega _1t_2}$$
$$=\\frac{1}{i \\Omega _1}\\int _0^tdt_2\\left(1-e^{-i \\Omega _1t_2}\
\\right)$$
$$=\\frac{1}{i \\Omega _1}\\left(t-\\frac{e^{-i \\Omega _1t}-1}{-i \
\\Omega _1}\\right)$$
$$=\\frac{t}{i \\Omega _1}-\\frac{e^{-i \\Omega _1t}-1}{\\Omega \
_1^2},$$
```

which is dominated by the first term in the long-time limit as \
$$t\\gg 1$$.

Therefore, in the long-time limit, we should look for integrals of \
the following form

```wl
$$\\int _0^tdt_2\\int _0^{t_2}dt_1e^{i \\Omega _1t_1}e^{-i \\Omega \
_1t_2}\\overset{t\\rightarrow \\infty }{\\rightarrow }\\frac{t}{i \
\\Omega _1},$$
```

which corresponds to the 2nd and 3rd terms ($$\\Omega _1=\\Delta \
-\\omega$$ and $$\\Delta +\\omega$$) in the transition amplitude

```wl
$$\\langle 2| \\hat{G}(t,0)| 1\\rangle \\approx -\\frac{\\lambda \
_0^2}{4}\\int _0^tdt_2\\int _0^{t_2}dt_1\\left(e^{i (\\Delta -\\omega \
) t_1}e^{i (-\\Delta +\\omega
) t_2}+e^{i (\\Delta +\\omega ) t_1}e^{i (-\\Delta -\\omega ) \
t_2}\\right)$$
$$\\overset{t\\rightarrow \\infty }{\\rightarrow }-\\frac{\\lambda \
_0^2}{4}\\left(\\frac{t}{i (\\Delta -\\omega )}+\\frac{t}{i (\\Delta \
+\\omega )}\\right)$$
$$=\\frac{i \\lambda _0^2t}{4}\\left(\\frac{2\\Delta }{\\Delta \
^2-\\omega ^2}\\right)$$
$$=\\frac{i \\lambda _0^2t}{2}\\frac{\\Delta }{\\Delta ^2-\\omega \
^2}.$$
```

In conclusion, the leading order behavior of the transition amplitude \
in the long-time limit is

```wl
$$\\langle 2| \\hat{G}(t,0)| 1\\rangle \\approx \\frac{i \\lambda \
_0^2t}{2}\\frac{\\Delta }{\\Delta ^2-\\omega ^2}.$$
```

(iv) The transition rate is then given by

```wl
$$P_{1\\text{-$>$}2}(t)=\\left| \\langle 2| \\hat{G}(t,0)| 1\\rangle \
\\right| ^2$$
$$=\\left| \\frac{i \\lambda _0^2t}{2}\\frac{\\Delta }{\\Delta \
^2-\\omega ^2}\\right| {}^2$$
$$=\\frac{\\lambda _0^4t^2}{4\\Delta ^2}\\left(\\frac{\\Delta \
^2}{\\Delta ^2-\\omega ^2}\\right)^2.$$
```

Therefore,

* Time scaling:

```wl
$$P_{1\\text{-$>$}2}(t)\\propto t^2,$$
```

indicating **coherent quadratic growth** due to two-photon (Raman) \
transition.

* Frequency dependence:

```wl
$$P_{1\\text{-$>$}2}(t)\\propto \\left(1-(\\omega /\\Delta \
)^2\\right)^{-2},$$
```

which is **resonantly enhanced** near $$\\omega /\\Delta \\rightarrow \
1$$, and **suppressed** when $$\\omega /\\Delta \\gg 1$$ or $$\\omega \
/\\Delta \\ll 1$$.

```wl
In[99]:=
Plot[(1 / (1 - \[Omega] ^ 2)) ^ 2 / 4, {\[Omega], 0, 3}, PlotStyle -> \
Black, FrameLabel -> {\[Omega]/\[CapitalDelta],              4  2  -2
P      (t)/(\[Lambda]  t  \[CapitalDelta]  )
 1 \[RightArrow] 2       0}, ImageSize -> 180]

Out[99]=
\\!\\(\\*GraphicsBox[{{{}, {}, TagBox[{GrayLevel[0], \
AbsolutePointSize[4], AbsoluteThickness[1.5], 
     Opacity[1.], LineBox[{{6.122*^-8, 0.250}, {0.000, 
      0.250}, {0.001, 0.250}, {0.002, 
      0.250}, {0.003, 0.250}, {0.004, 
      0.250}, {0.00 ... ]} & )}}, 
 PlotRange -> {{0, 3}, {0., 2.428}}, PlotRangeClipping -> True, 
 PlotRangePadding -> {{Scaled[0.02], Scaled[0.02]}, {Scaled[0.05], \
Scaled[0.05]}}, 
 Ticks -> {Automatic, Automatic}, TicksStyle -> \
Directive[GrayLevel[0], FontSize -> 12]]\\)

