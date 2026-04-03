# 130B Quantum Physics

Part 4. Phase and Gauge

## Gauge Principles

### Gauge Structure and Berry Phase

#### Phase Ambiguities

At its core, quantum mechanics is a **probability theory**. It \
postulate to *model* the probability density $$p(\\pmb{x})$$ by a \
*squared norm*

```wl
$$p(\\pmb{x})=| \\psi (\\pmb{x})| ^2,$$
```

just to ensure the *positive semi-definite* property \
$$p(\\pmb{x})\\text{$>$=}0$$.

The wavefunction $$\\psi (\\pmb{x})$$  itself serves as a \
**mathematical parameter** of the probability model, *not* a \
**physical observable**, and is therefore subject to some degree of \
ambiguity or redundancy.

* **Global phase ambiguity**. A *global* phase rotation of the \
wavefunction (where \[OpenCurlyDoubleQuote]global\
\[CloseCurlyDoubleQuote] means $$\\alpha$$ does not depend on \
$$\\pmb{x}$$)

```wl
$$\\psi (\\pmb{x})\\rightarrow e^{i \\alpha }\\psi (\\pmb{x})$$
```

has no consequence on the expectation value $$\\langle O\\rangle$$ of \
any physical observable $$O$$ in any case

```wl
$$\\langle O\\rangle =\\int \\psi \
^*(\\pmb{x})O\\left(\\pmb{x},\\pmb{x}'\\right)\\psi \
\\left(\\pmb{x}'\\right)d^D\\pmb{x}d^D\\pmb{x}'.$$
```

Conclusion: quantum states \[Element] **projective Hilbert space**, \
where global phase is always *unphysical*.

* **Local phase ambiguity** (**Gauge redundancy**). We can push this \
idea further: if we restrict ourself to *diagonal* observables in the \
*position* basis, i.e., functions $$f(\\pmb{x})$$ that depends only \
on $$\\pmb{x}$$ (but not $$\\pmb{p}$$), then any *local* phase rotation

```wl
$$\\psi (\\pmb{x})\\text{-$>$}e^{i \\chi (\\pmb{x})}\\psi \
(\\pmb{x})$$
```

will leave all expectation values $$\\langle f(\\pmb{x})\\rangle$$ \
invariant,

```wl
$$\\langle f(\\pmb{x})\\rangle \\text{:=}\\int f(\\pmb{x})| \\psi \
(\\pmb{x})| ^2d^D\\pmb{x}=\\int f(\\pmb{x})p(\\pmb{x})d^D\\pmb{x}$$
```

since the probability density $$p(\\pmb{x})$$ is unchanged.

	* If p(x) = \\[LeftBracketingBar]\\[Psi](x)\\[RightBracketingBar]^2 \
was the only physical probability distribution to be modeled, any \
\\[Psi](x) related by local phase rotation Eq. (XXX) should be \
treated as equivalent.

	* This represents a **gauge redundancy**: multiple *mathematical \
descriptions* (e.g. wavefunctions) describing the same *physical \
reality* (e.g. position distribution).

🤔 **Quantum decoherence** provides a deeper reason of why only \
*diagonal* observables are measurable.

	* **Environmental monitoring**: The environment has a natural \
tendency to monitor the **local density** $$p(\\pmb{x})$$ of \
particles in the space.

		* Effectively performing *weak continuous* **measurement** of \
$$\\pmb{x}$$.

		* Inducing **decoherence** in the position basis: rapid decay of \
*off-diagonal* coherence $$\\rho \\left(\\pmb{x},\\pmb{x}'\\right)$$ \
of the density matrix for $$\\pmb{x}\\neq \\pmb{x}'$$.

	* Consequence 1: **Dephasing noise**.

		* The measurement *randomizes* the **phase** of $$\\psi \
(\\pmb{x})$$ at every position *independently*.

		* Relative phase between \\[Psi](x) and \\[Psi](Derivative[1][x]) \
no longer comparable, allowing local phase rotation as Eq. (XXX) to \
become a redundancy.

	* Consequence 2: **Gauge projection**.

		* The measurement *collapse* the system towards the **particle \
number** eigenstates, suppressing the *number fluctuations*.

		* Effectively imposing a *gauge constraint* (like Gauss law), that \
couples the particle to an *emergent* **gauge field**, allowing \
particles to interact with each other through *emergent* **gauge \
forces**.

#### Gauge Transformation

If the gauge freedom is an (emergent) *redundancy*, it should have no \
*physical consequence*. For example, it should not affect the \
**quantum dynamics** governed by the **Schrödinger equation**.

However, the standard Schrödinger equation is *not* invariant under \
the **gauge transformation**

```wl
$$\\psi (\\pmb{x},t)\\rightarrow e^{i \\chi (\\pmb{x},t)}\\psi \
(\\pmb{x},t),$$
```

unless we modify it appropriately.

* Start from the free Schrödinger equation

```wl
$$i \\hbar \\partial _t\\psi (\\pmb{x},t)=-\\frac{\\hbar \
^2}{2m}\\nabla ^2\\psi (\\pmb{x},t),$$
```

under gauge transformation \\[Psi] \\[RightArrow] E^(I \\[Chi]) \
\\[Psi] in Eq. (XXX), the derivative operators picks up extra terms \
involving \\!\\(
\\*SubscriptBox[\\(\\[PartialD]\\), \\(t\\)]\\[Chi]\\) and \
\\[Del]\\[Chi],

```wl
$$i \\hbar  \\left(\\partial _t+i \\partial _t\\chi \
(\\pmb{x},t)\\right)\\psi (\\pmb{x},t)=-\\frac{\\hbar ^2}{2m}(\\nabla \
+i \\nabla \\chi (\\pmb{x},t))^2\\psi (\\pmb{x},t),$$
```

and the equation does *not* remain invariant.

Show that Eq. (XXX) becomes to Eq. (XXX) under gauge transformation.

Under gauge transformation, the derivatives transforms as

```wl
$$\\begin{array}{lll}
 \\partial _t\\psi  & \\rightarrow  & \\partial _t\\left(e^{i \\chi }\
\\psi \\right) \\\\
   & = & \\partial _te^{i \\chi }\\psi +e^{i \\chi }\\partial _t\\psi \
 \\\\
   & = & i \\partial _t\\chi  e^{i \\chi }\\psi +e^{i \\chi \
}\\partial _t\\psi  \\\\
   & = & e^{i \\chi }\\left(\\partial _t+i \\partial _t\\chi \\right)\
\\psi , \\\\
\\end{array}$$

$$\\begin{array}{lll}
 \\nabla \\psi  & \\rightarrow  & \\nabla \\left(e^{i \\chi }\\psi \
\\right) \\\\
   & = & \\nabla e^{i \\chi }\\psi +e^{i \\chi }\\nabla \\psi  \\\\
   & = & i \\nabla \\chi  e^{i \\chi }\\psi +e^{i \\chi }\\nabla \
\\psi  \\\\
   & = & e^{i \\chi }(\\nabla +i \\nabla \\chi )\\psi . \\\\
\\end{array}$$
```

This means when the derivative operators $$\\partial _t$$ or \
$$\\nabla$$ commutes through the gauge transformation $$e^{i \\chi \
}$$, they will pick up extra pieces $$\\partial _t\\chi$$ or \
$$\\nabla \\chi$$ as

```wl
$$e^{-i \\chi }\\partial _te^{i \\chi }=\\partial _t+i \\partial \
_t\\chi ,\\\\
e^{-i \\chi }\\nabla e^{i \\chi }=\\nabla +i \\nabla \\chi .$$
```

Start with the Schrödinger equation

```wl
$$i \\hbar \\partial _t\\psi =-\\frac{\\hbar ^2}{2m}\\nabla ^2\\psi .$$
```

* Under gauge transformation, replace $$\\psi \\rightarrow e^{i \\chi \
}\\psi$$,

```wl
$$i \\hbar \\partial _t\\left(e^{i \\chi }\\psi \
\\right)=-\\frac{\\hbar ^2}{2m}\\nabla ^2\\left(e^{i \\chi }\\psi \
\\right).$$
```

* Commute $$e^{i \\chi }$$ through the derivative operators

```wl
$$i \\hbar  e^{i \\chi } \\left(\\partial _t+i \\partial _t\\chi \
\\right)\\psi =-\\frac{\\hbar ^2}{2m}e^{i \\chi }(\\nabla +i \\nabla \
\\chi )^2\\psi .$$
```

* Cancel $$e^{i \\chi }$$ from both sides, we arrive at the \
Schrödinger equation after the transform

```wl
$$i \\hbar  \\left(\\partial _t+i \\partial _t\\chi \\right)\\psi \
=-\\frac{\\hbar ^2}{2m}(\\nabla +i \\nabla \\chi )^2\\psi .$$
```

* To restore the **gauge invariance**, we introduce **gauge fields** :

	* **Scalar potential**: $$\\Phi (\\pmb{x},t)$$ - a scalar field in \
the spacetime

	* **Vector potential**: $$\\pmb{A}(\\pmb{x},t)$$ - a vector field in \
the spacetime

and replace derivatives by **covariant derivatives** :

```wl
$$\\partial _t\\rightarrow D_t\\text{:=}\\partial _t+\\frac{i}{\\hbar \
}\\Phi (\\pmb{x},t),\\\\
\\nabla \\rightarrow \\pmb{D}\\text{:=}\\nabla -\\frac{i}{\\hbar \
}\\pmb{A}(\\pmb{x},t),$$
```

Then Eq. (XXX) can be recast into the gauge-invariant Schrödinger \
equation

```wl
$$i \\hbar  D_t\\psi (\\pmb{x},t)=\\frac{1}{2m}(-i \\hbar  \
\\pmb{D})^2\\psi (\\pmb{x},t),$$
```

or more explicitly,

```wl
$$i \\hbar \\partial _t\\psi (\\pmb{x},t)=\\left(\\frac{1}{2m}(-i \
\\hbar \\nabla -\\pmb{A}(\\pmb{x},t))^2+\\Phi \
(\\pmb{x},t)\\right)\\psi (\\pmb{x},t).$$
```

Under **gauge transformation**, the wavefunction $$\\psi$$ and the \
gauge fields $$(\\Phi ,\\pmb{A})$$ must transform together as

```wl
$$\\psi (\\pmb{x},t)\\rightarrow e^{i \\chi (\\pmb{x},t)}\\psi \
(\\pmb{x},t),\\\\
\\Phi (\\pmb{x},t)\\text{-$>$}\\Phi (\\pmb{x},t)-\\hbar \\partial \
_t\\chi (\\pmb{x},t),\\\\
\\pmb{A}(\\pmb{x},t)\\rightarrow \\pmb{A}(\\pmb{x},t)+\\hbar \\nabla \
\\chi (x,t),$$
```

to ensure the covariance of the quantum dynamics.

#### Semiclassical Interpretation

In the WKB approximation, we write the wavefunction as

```wl
$$\\psi =A e^{i S/\\hbar }.$$
```

Plugging the WKB ansatz into the gauge-invariant Schrödinger equation \
Eq. (XXX) yields:

```wl
$$\\left(-\\partial _tS-\\Phi \\right)=\\frac{1}{2m}(\\nabla \
S-\\pmb{A})^2.$$
```

Given that the spacetime derivatives of the action S is associated to \
energy E = -\\!\\(
\\*SubscriptBox[\\(\\[PartialD]\\), \\(t\\)]S\\) and momentum p = \
\\[Del]S, Eq. (XXX) can be written as

```wl
$$(E-\\Phi )=\\frac{1}{2m}(\\pmb{p}-\\pmb{A})^2.$$
```

This reveals the physical meaning of gauge fields:

* Scalar potential $$\\Phi$$: **potential energy**,

* Vector potential $$\\pmb{A}$$: **potential momentum**.

Note: Energy and Momentum each have *three* distinct forms

```wl
$$\\begin{array}{c|ccccc}
   & \\pmb{\\text{Total}} & = & \\pmb{\\text{Kinetic}} & + & \
\\pmb{\\text{Potential}} \\\\
\\hline
 \\text{Energy} & E & = & \
\\frac{1}{2}m\\pmb{\\overset{.}{\\pmb{x}}}^2 & + & \\Phi  \\\\
 \\text{Momentum} & \\pmb{p} & = & m\\pmb{\\overset{.}{\\pmb{x}}} & + \
& \\pmb{A} \\\\
\\end{array}$$
```

Show that both equations in Eq. (XXX) are consistent with Eq. (XXX).

Simply by setting \
$$m\\pmb{\\overset{.}{\\pmb{x}}}=\\pmb{p}-\\pmb{A}$$, we have on one \
hand

```wl
$$\\pmb{p}=m\\pmb{\\overset{.}{\\pmb{x}}}+\\pmb{A},$$
```

and on the other hand

```wl
$$E=\\frac{1}{2m}(\\pmb{p}-\\pmb{A})^2+\\Phi$$
$$=\\frac{1}{2m}\\left(m\\pmb{\\overset{.}{\\pmb{x}}}\\right)^2+\\Phi$$
$$=\\frac{1}{2}m\\pmb{\\overset{.}{\\pmb{x}}}^2+\\Phi .$$
```

* **Total** (or **Canonical**): appear directly in *conservation \
laws* and determine the *action* accumulated in spacetime.

* **Kinetic**: directly linked to the particle\[CloseCurlyQuote]s \
*motion* (velocity $$\\dot{\\pmb{x}}$$).

* **Potential**: exist independently of particle motion, contributing \
even when the particle is *at rest* ($$\\dot{\\pmb{x}}=0$$), \
representing the *interaction* with the *background field* in the \
spacetime.

Question: What are their dynamical consequences?

**Newton\[CloseCurlyQuote]s 2nd law** \[LongDash] the *force \
*$$\\pmb{F}$$ causes the *kinetic momentum* $$\\left(m\\dot{\\pmb{x}}\
\\right)$$ to change in time:

```wl
$$\\pmb{F}=\\frac{d}{dt}\\left(m \
\\dot{\\pmb{x}}\\right)=\\frac{d\\pmb{p}}{dt}-\\frac{d\\pmb{A}}{dt},$$\

```

in two distinct ways:

* $$d\\pmb{p}/dt=\\partial _t\\pmb{p}+\\dot{\\pmb{x}}\\cdot \\nabla \
\\pmb{p}$$, in which

	* $$\\nabla \\pmb{p}=0$$, as $$\\pmb{x}$$ and $$\\pmb{p}$$ are \
independent variables,

	* **Maxwell relation**: $$\\partial _t\\nabla S=\\nabla \\partial \
_tS$$ implies

```wl
$$\\partial _t\\pmb{p}=-\\nabla E=(\\nabla \\pmb{A})\\cdot \
\\dot{\\pmb{x}}-\\nabla \\Phi .$$
```

* $$d\\pmb{A}/dt=\\partial _t\\pmb{A}+\\dot{\\pmb{x}}\\cdot \\nabla \
\\pmb{A}$$.

Put together, $$\\pmb{F}$$ takes the form as the **Lorentz force** \
(on a charge $$q=1$$ particle)

```wl
$$\\pmb{F}=-\\nabla \\Phi -\\partial _t\\pmb{A}+(\\nabla \
\\pmb{A})\\cdot \\dot{\\pmb{x}}-\\dot{\\pmb{x}}\\cdot \\nabla \
\\pmb{A}$$
$$=\\pmb{E}+\\dot{\\pmb{x}}\\times \\pmb{B},$$
```

as long as we define

```wl
$$\\pmb{E}=-\\nabla \\Phi -\\partial _t\\pmb{A},\\\\
\\pmb{B}=\\nabla \\times \\pmb{A}.$$
```

Justify Eq. (XXX) and Eq. (XXX).

* Eq. (XXX):

```wl
$$\\partial _t\\pmb{p}=-\\nabla E$$
$$=-\\nabla \\left(\\frac{1}{2}m\\pmb{\\overset{.}{\\pmb{x}}}^2+\\Phi \
\\right)$$
$$=-\\nabla \
\\left(\\frac{1}{2}m\\pmb{\\overset{.}{\\pmb{x}}}^2\\right)-\\nabla \
\\Phi$$
$$=-m\\left(\\nabla \\pmb{\\overset{.}{\\pmb{x}}}\\right)\\cdot \
\\pmb{\\overset{.}{\\pmb{x}}}-\\nabla \\Phi$$
$$=-\\left(\\nabla \
\\left(m\\pmb{\\overset{.}{\\pmb{x}}}\\right)\\right)\\cdot \
\\pmb{\\overset{.}{\\pmb{x}}}-\\nabla \\Phi$$
$$=-(\\nabla (\\pmb{p}-\\pmb{A}))\\cdot \
\\pmb{\\overset{.}{\\pmb{x}}}-\\nabla \\Phi$$
$$=(-\\nabla \\pmb{p}+\\nabla \\pmb{A})\\cdot \
\\pmb{\\overset{.}{\\pmb{x}}}-\\nabla \\Phi$$
$$=(\\nabla \\pmb{A})\\cdot \\pmb{\\overset{.}{\\pmb{x}}}-\\nabla \
\\Phi .$$
```

* Eq. (XXX): the first term E = -\\[Del]\\[CapitalPhi] - \\!\\(
\\*SubscriptBox[\\(\\[PartialD]\\), \\(t\\)]\\*
StyleBox[\"A\",
FontWeight->\"Bold\"]\\) is a simple substitution, so we focus on the \
second term 
\\!\\(\\*OverscriptBox[
StyleBox[\"x\",
FontWeight->\"Bold\"], \\(.\\)]\\)*B and show that

```wl
$$\\left(\\dot{\\pmb{x}}\\times \
\\pmb{B}\\right)_i=\\left(\\dot{\\pmb{x}}\\times (\\nabla \\times \
\\pmb{A})\\right)_i$$
$$=\\epsilon ^{i\\, j\\, k}\\dot{x}_j\\epsilon ^{k\\, l\\, \
m}\\partial _lA_m$$
$$=\\left(\\delta ^{i\\, l}\\delta ^{j\\, m}-\\delta ^{i\\, m}\\delta \
^{j\\, l}\\right)\\dot{x}_j\\partial _lA_m$$
$$=\\dot{x}_j\\partial _iA_j-\\dot{x}_j\\partial _jA_i$$
$$=\\left((\\nabla \\pmb{A})\\cdot \
\\dot{\\pmb{x}}-\\dot{\\pmb{x}}\\cdot \\nabla \\pmb{A}\\right)_i.$$
```

Obviously, $$\\pmb{E}$$ and $$\\pmb{B}$$ should be interpreted as \
**electric** and **magnetic** fields, allowing $$\\pmb{F}$$ to be \
consistently identified as the force exerted by the *electromagnetic \
field* on a *charged* particle.

Conclusion: **Gauge fields** $$(\\Phi ,\\pmb{A})$$ are not merely \
mathematical constructs to maintain *gauge invariance*; they give \
rise to the physical *electromagnetic interactions* among quantum \
particles. Remarkably, the **electromagnetic forces** familiar from \
our everyday *classical* experience emerge profoundly from the \
**local phase ambiguity** of matter at the *quantum* level.

#### Math Interlude: Lorentz Vectors

It is more convenient to unify time and space, as well as energy and \
momentum.

* **Spacetime**: Introduce $$x=\\left(x^0,x^1,x^2,x^3\\right)$$ to \
denote the coordinate of a spacetime point,

	* $$t=x^0$$: time,

	* $$\\pmb{x}=\\left(x^1,x^2,x^3\\right)$$: space,

and denote these components as $$x^{\\mu }$$($$\\mu =0,1,2,3$$) \
jointly. $$x$$ is said to be a **Lorentz vector**.

* **Spacetime derivatives**: Partial derivatives in the spacetime are \
defined as

```wl
$$\\partial _{\\mu }f(x)=\\lim_{\\delta x\\text{-$>$}0} \
\\frac{f(x+\\delta x)-f(x)}{\\delta x^{\\mu }},$$
```

	* $$\\partial _t=\\partial _0$$: temporal derivative,

	* $$\\nabla =\\left(\\partial _1,\\partial _2,\\partial \
_3\\right)$$: spatial derivatives.

* **Energy-momentum**: Introduce $$p=\\left(p^0,p^1,p^2,p^3\\right)$$ \
to denote the energy and momentum,

	* $$E=p^0=-p_0$$: energy,

	* $$\\pmb{p}=\\left(p^1,p^2,p^3\\right)=\\left(p_1,p_2,p_3\\right)$$:\
 momentum.

* **Gauge field**: Introduce $$A=\\left(A^0,A^1,A^2,A^3\\right)$$ to \
denote the gauge field,

	* $$\\Phi =A^0=-A_0$$: scalar potential,

	* $$\\pmb{A}=\\left(A^1,A^2,A^3\\right)=\\left(A_1,A_2,A_3\\right)$$:\
 vector potential.

* Covariant derivatives: Operators in Eq. (XXX) can now be unified as \
a single Lorentz vector operator

```wl
$$D_{\\mu }=\\partial _{\\mu }-\\frac{i}{\\hbar }A_{\\mu },$$
```

	* $$D_t=D_0$$: covariant temporal derivative,

	* $$\\pmb{D}=\\left(D_1,D_2,D_3\\right)$$: covariant spatial \
derivative.

**Raising** and **lowering** the index of a Lorentz vector is done by \
the** Lorentz metric** $$g_{\\mu \\, \\nu }$$ or $$g^{\\mu \\, \\nu \
}$$,

```wl
$$a_{\\mu }=g_{\\mu \\, \\nu }a^{\\nu },a^{\\mu }=g^{\\mu \\, \\nu \
}a_{\\nu },$$
```

where *repeated* indices are automatically summed over (**contracted**) \
following the **Einstein sum rule**. The Lorentz metric is given by

```wl
$$g_{\\mu \\, \\nu }=g^{\\mu \\, \\nu }=\\text{diag}(-1,+1,+1,+1).$$
```

Rule of thumb: In **index contraction**, the *upper* index can only \
contract with the *lower* index and vice versa.

```wl
$$\\begin{array}{ccc}
 a^{\\mu }b_{\\mu } & \\checkmark  & \\text{ok} \\\\
 a^{\\mu }b^{\\mu } & \\times  & \\text{no}! \\\\
 a_{\\mu }b_{\\mu } & \\times  & \\text{no}! \\\\
\\end{array}$$
```

More explicitly, the following expressions are all valid and equal

```wl
$$a^{\\mu }b_{\\mu }=a^0b_0+a^1b_1+a^2b_2+a^3b_3$$
$$=a^{\\mu }g_{\\mu \\, \\nu }b^{\\nu \
}=-a^0b^0+a^1b^1+a^2b^2+a^3b^3$$
$$=a_{\\mu }g^{\\mu \\, \\nu }b_{\\nu }=-a_0b_0+a_1b_1+a_2b_2+a_3b_3.$$
```

#### Berry Phase

**Berry phase** is the *phase* accumulated by the wavefunction as a \
particle travels through the spacetime *adiabatically*.

* A processes is said to be **adiabatic**, if it happens *slowly* \
over a long time, i.e. the rates of change in physical observables \
tend to zero. In terms of the motion of a particle, it means the \
*velocity* of the particle is *almost zero* throughout the process:

```wl
$$\\pmb{\\overset{.}{\\pmb{x}}}\\text{-$>$}0.$$
```

Eq. (XXX) is also called the adiabatic limit.

* In the adiabatic limit, the **action** of the particle is \
accumulated by the **potential** energy and momentum

```wl
$$-\\partial _tS=E=\\Phi ,\\\\
\\nabla S=\\pmb{p}=\\pmb{A}.$$
```

as the *kinetic* energy and momentum *vanishes* when \
$$\\pmb{\\overset{.}{\\pmb{x}}}\\text{-$>$}0$$.

* Given that phase is related to action, the **Berry phase** that a \
particle accumulates along a spacetime trajectory $$\\mathcal{C}$$ is \
given by the **path integral** that computes the accumulated action

```wl
$$\\Theta _{\\mathcal{C}}=\\frac{S_{\\mathcal{C}}}{\\hbar \
}=\\frac{1}{\\hbar }\\int _{\\mathcal{C}}-\\Phi dt+\\pmb{A}\\cdot \
d\\pmb{x}=\\frac{1}{\\hbar }\\int _{\\mathcal{C}}A_{\\mu
}dx^{\\mu }.$$
```

Justify Eq. (XXX).

```wl
$$S_{\\mathcal{C}}=\\int _{\\mathcal{C}}dS=\\int \
_{\\mathcal{C}}\\partial _tSdt+\\nabla S\\cdot d\\pmb{x}$$
$$=\\int _{\\mathcal{C}}-\\Phi dt+\\pmb{A}\\cdot d\\pmb{x}.$$
```

Such that *adiabatically propagating* the **wave amplitude** \
$$\\psi$$ along trajectory $$\\mathcal{C}$$ will acquire the **Berry \
phase** shift:

```wl
$$\\psi \\overset{\\mathcal{C}}{\\rightarrow }e^{i \\Theta \
_{\\mathcal{C}}}\\psi =\\exp \\left(\\frac{i}{\\hbar }\\int \
_{\\mathcal{C}}A_{\\mu }dx^{\\mu }\\right)\\psi
.$$

In[590]:=
Graphics[{{AbsoluteThickness[1], Arrowheads[0.06], Arrow[{{0, 0}, {1, \
0}}], Arrow[{{0, 0}, {0, 1}}]}, {Text[\"\\!\\(\[VeryThinSpace]**x\
**\\)\", {1, 0}, { - 1.5, 0}], Text[\[VeryThinSpace]t, {0, 1}, { - \
0.2,  - 0.5}]}, 
	GraphicsComplex[{{0.2, 0.18}, {0.3, 0.4}, {0.62, 0.52}, {0.8, 0.64}, \
{0.84, 0.75}, {0.8, 0.86}, {0.64, 0.94}}, {{Arrowheads[{{0.08, \
0.6}}], Arrow[BSplineCurve[{1, 2, 3, 4, 5, 6, 7}]]}, {Point[{1, 7}]}, \
{Text[\[Psi], 1, {1.8,  - 0.5}], Text[ I \[CapitalTheta]
    \[ScriptCapitalC]
E     \[Psi], 7, {1,  - 0.5}]}}], Text[\"\[ScriptCapitalC]\", {0.6, \
0.45}]}, ImageSize -> 140]

Out[590]=
\\!\\(\\*GraphicsBox[{{AbsoluteThickness[1], Arrowheads[0.06], \
ArrowBox[{{0, 0}, {1, 0}}], 
   ArrowBox[{{0, 0}, {0, 1}}]}, 
  {InsetBox[\"\\\"\\\\!\\\\(\[VeryThinSpace]\\\\!\\\\(\\\\*StyleBox[\\\
\\\\\"x\\\\\\\",FontWeight->\\\\\\\"Bold\\\\\\\"]\\\\)\\\\)\\\"\", \
{1, 0}, 
    NCache[ImageScaled[{-0.25, 1/ ... rveBox[{1, 2, 3, 4, 5, 6, \
7}]]}, PointBox[{1, 7}], 
    {InsetBox[\"\\\"\\\\!\\\\(\[Psi]\\\\)\\\"\", 1, ImageScaled[{1.4, \
0.25}]], 
     InsetBox[\"\\\"\\\\!\\\\(E\\\\^\\\\(I \[CapitalTheta]\\\\_\
\[ScriptCapitalC]\\\\)\[Psi]\\\\)\\\"\", 7, ImageScaled[{1, \
0.25}]]}}], 
  InsetBox[\"\\\"\[ScriptCapitalC]\\\"\", {0.6, 0.45}]}, ImageSize -> \
140]\\)
```

* For infinitesimal transportation $$\\mathcal{C}:x\\rightarrow \
x+\\delta x$$,

```wl
$$\\psi \\text{-$>$}e^{\\frac{i}{\\hbar }A_{\\mu }\\delta x^{\\mu \
}}\\psi .$$
```

* Under gauge transformation

```wl
$$A_{\\mu }(x)\\rightarrow A_{\\mu }(x)+\\hbar \\partial _{\\mu \
}\\chi (x),$$
```

	* the Berry phase along an **open trajectory** $$\\mathcal{C}$$ is \
*not* gauge invariant (hence not a physical observable):

```wl
$$\\Theta _{\\mathcal{C}}\\text{-$>$}\\Theta _{\\mathcal{C}}+\\chi \
\\left(x_{\\text{end}}\\right)-\\chi \
\\left(x_{\\text{start}}\\right),$$
```

where $$x_{\\text{start}},x_{\\text{end}}=\\partial \\mathcal{C}$$ \
are the starting and ending point of $$\\mathcal{C}$$.

	* the Berry phase around a **closed loop** (Wilson loop) is gauge \
invariant, and is a physical observable.

### Gauge Field and Electromagnetism

#### Gauge Connection

Previously, we have introduced the *covariant derivative* $$D_{\\mu \
}$$ to make the Schrödinger equation *gauge invariant*, but is there \
a deeper motivation behind this? In calculus, the **derivative** of a \
function tells us how much the function changes between nearby points

```wl
$$\\partial _xf(x)=\\lim_{\\delta x\\text{-$>$}0} \\frac{f(x+\\delta \
x)-f(x)}{\\delta x}.$$
```

But this assumes we can *compare* the values of the function at \
different points directly.

* Problem: If the wavefunction $$\\psi (x)$$ has **local phase \
ambiguity**,

```wl
$$\\psi (x)\\rightarrow e^{i \\chi (x)}\\psi (x),$$
```

meaning that $$\\psi (x)$$ at each point $$x$$ is defined *up to a \
phase rotation*, there will be *no basis to compare* wavefunctions \
between *distinct points*.

☞ There is a similar issue in **finance**: you cannot directly \
compare currencies from different countries by their face values!

	* Are the following amounts of money the same?

```wl
In[609]:=
Row[{Spacer[20], Graphics[{Inset[#1, {#2, \
0}]&@@@{{\\!\\(\\*GraphicsBox[TagBox[RasterBox[..., {{0, 256.}, \
{256., 0}}, {0, 255}, 
   ColorFunction -> RGBColor, ImageResolution -> {72., 72.}, \
RasterInterpolation -> \"High\"], 
  BoxForm`ImageTag[\"Byte\", ColorSpace -> \"RGB\", Interleaving -> \
True], Selectable -> False], 
 DefaultBaseStyle -> \"ImageGraphics\", ImageSize -> {29.644, \
Automatic}, 
 ImageSizeRaw -> {256., 256.}, PlotRange -> {{0, 256.}, {0, \
256.}}]\\),  - 1}, {\\!\\(\\*GraphicsBox[TagBox[RasterBox[..., {{0, \
256.}, {256., 0}}, {0, 255}, 
   ColorFunction -> RGBColor, ImageResolution -> {72., 72.}, \
RasterInterpolation -> \"High\"], 
  BoxForm`ImageTag[\"Byte\", ColorSpace -> \"RGB\", Interleaving -> \
True], Selectable -> False], 
 DefaultBaseStyle -> \"ImageGraphics\", ImageSize -> {30.050, \
Automatic}, 
 ImageSizeRaw -> {256., 256.}, PlotRange -> {{0, 256.}, {0, \
256.}}]\\), 0}, {\\!\\(\\*GraphicsBox[TagBox[RasterBox[..., {{0, \
256.}, {256., 0}}, {0, 255}, 
   ColorFunction -> RGBColor, ImageResolution -> {72., 72.}, \
RasterInterpolation -> \"High\"], 
  BoxForm`ImageTag[\"Byte\", ColorSpace -> \"RGB\", Interleaving -> \
True], Selectable -> False], 
 DefaultBaseStyle -> \"ImageGraphics\", ImageSize -> {30.195, \
Automatic}, 
 ImageSizeRaw -> {256., 256.}, PlotRange -> {{0, 256.}, {0, \
256.}}]\\), 1}}, Translate[{Text[#1, #2]&@@@{{\"¥100\", { - 1, 0}}, {\
\"$100\", {0, 0}}, {\"€100\", {1, 0}}}}, {0,  - 0.3}]}, ImageSize -> \
180]}]

Out[609]= \\!\\(\\*GraphicsBox[«2»]\\)
```

	* You should first *move* (parallel transport) the money to the same \
place before comparing.

```wl
In[610]:=
Row[{Spacer[20], Graphics[{Inset[#1, {#2, \
0}]&@@@{{\\!\\(\\*GraphicsBox[TagBox[RasterBox[..., {{0, 256.}, \
{256., 0}}, {0, 255}, 
   ColorFunction -> RGBColor, ImageResolution -> {72., 72.}, \
RasterInterpolation -> \"High\"], 
  BoxForm`ImageTag[\"Byte\", ColorSpace -> \"RGB\", Interleaving -> \
True], Selectable -> False], 
 DefaultBaseStyle -> \"ImageGraphics\", ImageSize -> {29.644, \
Automatic}, 
 ImageSizeRaw -> {256., 256.}, PlotRange -> {{0, 256.}, {0, \
256.}}]\\),  - 1}, {\\!\\(\\*GraphicsBox[TagBox[RasterBox[..., {{0, \
256.}, {256., 0}}, {0, 255}, 
   ColorFunction -> RGBColor, ImageResolution -> {72., 72.}, \
RasterInterpolation -> \"High\"], 
  BoxForm`ImageTag[\"Byte\", ColorSpace -> \"RGB\", Interleaving -> \
True], Selectable -> False], 
 DefaultBaseStyle -> \"ImageGraphics\", ImageSize -> {30.050, \
Automatic}, 
 ImageSizeRaw -> {256., 256.}, PlotRange -> {{0, 256.}, {0, \
256.}}]\\), 0}, {\\!\\(\\*GraphicsBox[TagBox[RasterBox[..., {{0, \
256.}, {256., 0}}, {0, 255}, 
   ColorFunction -> RGBColor, ImageResolution -> {72., 72.}, \
RasterInterpolation -> \"High\"], 
  BoxForm`ImageTag[\"Byte\", ColorSpace -> \"RGB\", Interleaving -> \
True], Selectable -> False], 
 DefaultBaseStyle -> \"ImageGraphics\", ImageSize -> {30.195, \
Automatic}, 
 ImageSizeRaw -> {256., 256.}, PlotRange -> {{0, 256.}, {0, \
256.}}]\\), 1}}, Translate[{Text[#1, #2]&@@@{{\"$13.3\", {0,  - \
0.4}}, {\"$100\", {0,  - 0.2}}, {\"$108\", {0, 0}}}, GrayLevel[0.7], \
Arrowheads[0.06], Arrow[{#,  - 0.4}& /@ { - 0.7,  - 0.3}], Arrow[{#, \
0}& /@ {0.7, 0.3}], Text[#1, #2]&@@@{{\"¥100\", { - 1,  - 0.4}}, \
{\"€100\", {1, 0}}}}, {0,  - 0.3}], Text[Style[\"03/27/2025\", 10, \
LightGray, \"ConcreteText\"], {1,  - 0.8}, {0.3,  - 1}]}, ImageSize -> \
180]}]

Out[610]= \\!\\(\\*GraphicsBox[«2»]\\)
```

During the conversion, the money will be multiplied by the *exchange \
rate* (exponential gauge connection), e.g.

```wl
$$e^{0.076961}\\matkfrac{E}100=\\$108, e^{-2.01741}\\yen 100=\\$13.3.$$
```

* Solution: Similarly, to define a meaningful derivative for the \
wavefunction, we have to introduce a **gauge connection **$$A_{\\mu \
}(x)$$ to keep track of the *phase rotation* needed to transport \
$$\\psi (x+\\delta x)$$ back to the point $$x$$ for comparison, for \
every point $$x$$ along any direction $$\\mu$$.

This allows us to (re)define the **covariant derivative** :

```wl
$$D_{\\mu }\\psi (x)=\\lim_{\\delta x\\text{-$>$}0} \
\\frac{e^{-\\frac{i}{\\hbar }A_{\\nu }(x)\\delta x^{\\nu }}\\psi \
(x+\\delta x)-\\psi (x)}{\\delta x^{\\mu }}.$$
```

* Interpretation: $$\\psi (x+\\delta x)$$ has accumulated a Berry \
phase of $$\\exp \\left(\\frac{i}{\\hbar }A_{\\nu }(x)\\delta x^{\\nu \
}\\right)$$ compare to $$\\psi (x)$$ as the particle travels \
adiabatically. So when pulling $$\\psi (x+\\delta x)$$ back to the \
point $$x$$, this phase should be compensated by the opposite phase \
factor $$\\exp \\left(-\\frac{i}{\\hbar }A_{\\nu }(x)\\delta x^{\\nu \
}\\right)$$ before comparing.

* Expressed in terms of the usual partial derivative modified by the \
gauge connection,

```wl
$$D_{\\mu }=\\partial _{\\mu }-\\frac{i}{\\hbar }A_{\\mu }(x),$$
```

which exactly reproduces Eq. (XXX).

Show Eq. (XXX) follows from Eq. (XXX) by taking the limit.

Use Taylor expansion to the leading order in $$\\delta x^{\\mu }$$,

```wl
$$D_{\\mu }\\psi (x)=\\lim_{\\delta x^{\\mu }\\text{-$>$}0} \
\\frac{e^{-\\frac{i}{\\hbar }A_{\\nu }(x)\\delta x^{\\nu }}\\psi \
(x+\\delta x)-\\psi (x)}{\\delta x^{\\mu
}}$$
$$=\\lim_{\\delta x^{\\mu }\\text{-$>$}0} \
\\frac{\\left(1-\\frac{i}{\\hbar }A_{\\nu }(x)\\delta x^{\\nu \
}+\\mathcal{O}\\left(\\delta x^2\\right)\\right)\\left(\\psi
(x)+\\partial _{\\nu }\\psi (x)\\delta x^{\\nu \
}+\\mathcal{O}\\left(\\delta x^2\\right)\\right)-\\psi (x)}{\\delta \
x^{\\mu }}$$
$$=\\lim_{\\delta x^{\\mu }\\text{-$>$}0} \\frac{\\psi (x)+\\partial \
_{\\nu }\\psi (x)\\delta x^{\\nu }-\\frac{i}{\\hbar }A_{\\nu \
}(x)\\delta x^{\\nu }\\psi (x)+\\mathcal{O}\\left(\\delta
x^2\\right)-\\psi (x)}{\\delta x^{\\mu }}$$
$$=\\lim_{\\delta x^{\\mu }\\text{-$>$}0} \\left(\\partial _{\\nu \
}\\psi (x)-\\frac{i}{\\hbar }A_{\\nu }(x)\\psi \
(x)\\right)\\frac{\\delta x^{\\nu }}{\\delta x^{\\mu
}}+\\mathcal{O}(\\delta x)$$
$$=\\left(\\partial _{\\nu }\\psi (x)-\\frac{i}{\\hbar }A_{\\nu \
}(x)\\psi (x)\\right)\\delta _{\\mu }^{\\nu }$$
$$=\\left(\\partial _{\\mu }-\\frac{i}{\\hbar }A_{\\mu \
}(x)\\right)\\psi (x).$$
```

* The covariant derivative commute with the **gauge transformation**

```wl
$$\\psi (x)\\rightarrow e^{i \\chi (x)}\\psi (x),\\\\
A_{\\mu }(x)\\rightarrow A_{\\mu }(x)+\\hbar \\partial _{\\mu }\\chi \
(x),$$
```

as adapted from Eq. (XXX).

* The **apparent** deformation of the wavefunction $$\\psi$$ from \
$$x$$ to $$x+\\delta x$$ can be expressed as

```wl
$$\\psi (x+\\delta x)=e^{\\frac{i}{\\hbar }A_{\\mu }(x)\\delta \
x^{\\mu }}e^{\\delta x^{\\mu }D_{\\mu }}\\psi (x),$$
```

which contains two contributions

	* the **intrinsic** deformation under **parallel transport** $$\\psi \
\\rightarrow e^{\\delta x^{\\mu }D_{\\mu }}\\psi$$, which is \
*generated* by the *covariant derivative* $$D_{\\mu }$$,

	* the **background** deformation in terms of the Berry phase $$\\psi \
\\rightarrow e^{(i/\\hbar )A_{\\mu }(x)\\delta x^{\\mu }}\\psi$$ \
accumulated along the *gauge connection* $$A_{\\mu }$$.

#### Gauge Curvature

Exchanging currencies in cycles typically results in a loss. Why?

```wl
In[611]:=
Row[{Spacer[20], Graphics[{Inset[#1, \
#2]&@@@Thread@{{\\!\\(\\*GraphicsBox[TagBox[RasterBox[..., {{0, \
256.}, {256., 0}}, {0, 255}, 
   ColorFunction -> RGBColor, ImageResolution -> {72., 72.}, \
RasterInterpolation -> \"High\"], 
  BoxForm`ImageTag[\"Byte\", ColorSpace -> \"RGB\", Interleaving -> \
True], Selectable -> False], 
 DefaultBaseStyle -> \"ImageGraphics\", ImageSize -> {29.644, \
Automatic}, 
 ImageSizeRaw -> {256., 256.}, PlotRange -> {{0, 256.}, {0, \
256.}}]\\), \\!\\(\\*GraphicsBox[TagBox[RasterBox[..., {{0, 256.}, \
{256., 0}}, {0, 255}, 
   ColorFunction -> RGBColor, ImageResolution -> {72., 72.}, \
RasterInterpolation -> \"High\"], 
  BoxForm`ImageTag[\"Byte\", ColorSpace -> \"RGB\", Interleaving -> \
True], Selectable -> False], 
 DefaultBaseStyle -> \"ImageGraphics\", ImageSize -> {30.050, \
Automatic}, 
 ImageSizeRaw -> {256., 256.}, PlotRange -> {{0, 256.}, {0, \
256.}}]\\), \\!\\(\\*GraphicsBox[TagBox[RasterBox[..., {{0, 256.}, \
{256., 0}}, {0, 255}, 
   ColorFunction -> RGBColor, ImageResolution -> {72., 72.}, \
RasterInterpolation -> \"High\"], 
  BoxForm`ImageTag[\"Byte\", ColorSpace -> \"RGB\", Interleaving -> \
True], Selectable -> False], 
 DefaultBaseStyle -> \"ImageGraphics\", ImageSize -> {30.195, \
Automatic}, 
 ImageSizeRaw -> {256., 256.}, PlotRange -> {{0, 256.}, {0, \
256.}}]\\)}, CirclePoints[3]}, GraphicsComplex[CirclePoints[3], \
{Text[\"$100\", 2, {0, 2}], Text[\"¥716\", 1, {0,  - 2}], \
Text[\"€88.3\", 3, {0,  - 2}], Text[\"$95.3\", 2, {0, 3.5}]}], \
{Arrowheads[0.08], Arrow[{{0.27, 0.7}, {0.86, 0}}], Arrow[{{0.55,  - \
0.12}, { - 0.55,  - 0.12}}], Arrow[{{ - 0.86, 0}, { - 0.3, 0.46}}]}, \
Text[Style[\"!?!\", Bold, 18], {0, 0.1}], Text[Style[\"03/27/2025\", \
10, LightGray, \"ConcreteText\"], {0,  - 0.45}, {0, 1}]}, ImageSize -> \
140]}]

Out[611]= \\!\\(\\*GraphicsBox[«2»]\\)
```

Because the global foreign exchange market is not *flat *\[LongDash] \
the mismatch around a *closed loop* is a measure of **curvature**.

In gauge theory, the **gauge curvature** $$F_{\\mu \\, \\nu }$$ \
measures the adiabatic *action* accumulated *per area* when \
transporting the wavefunction around the *area boundary* in spacetime.

```wl
$$S=\\oint _{\\partial \\Omega }A_{\\mu }dx^{\\mu }=\\int _{\\Omega \
}F_{\\mu \\, \\nu }dx^{\\mu }dx^{\\nu }.$$
```

* Operational definition :  Mathematically, the gauge curvature $$F_{\
\\mu \\, \\nu }$$ is defined by the *commutator* of *covariant \
derivatives*

```wl
$$\\left[D_{\\mu },D_{\\nu }\\right]\\psi =-\\frac{i}{\\hbar } \
F_{\\mu \\, \\nu }\\psi ,$$
```

which measures the amount of non-commutativity to transport the \
wavefunction along two distinct spacetime directions $$\\mu$$ and \
$$\\nu$$.

```wl
In[551]:=
Graphics[{{AbsoluteThickness[1], Arrowheads[0.06], Arrow[{{0, 0}, {1, \
0}}], Arrow[{{0, 0}, {0, 1}}]}, {Text[ \[Mu]
x, {1, 0}, { - 1.5, 0}], Text[ \[Nu]
x, {0, 1}, { - 0.5,  - 0.5}]}, Translate[Block[{a = 0.5}, \
{{Lighter[Purple, 0.85], Rectangle[{0, 0}, {a, a}]}, {Purple, Text[\"\
\[CapitalOmega]\", {a / 2, a / 2}]}, Arrowheads[{{0.08, 0.6}}], {Red, \
Arrow[{{0, 0}, {a, 0}}], Arrow[{{a, 0}, {a, a}}], Text[     \[Mu]
\[Delta] \[InvisibleComma] x, {a / 2, 0}, {0, 1.2}], Text[     \[Nu]
\[Delta] \[InvisibleComma] x, {a, a / 2}, { - 1.5, 0}]}, {Blue, \
Arrow[{{0, 0}, {0, a}}], Arrow[{{0, a}, {a, a}}], Text[     \[Mu]
\[Delta] \[InvisibleComma] x, {a / 2, a}, {0,  - 1}], Text[     \[Nu]
\[Delta] \[InvisibleComma] x, {0, a / 2}, {1.2, 0}]}, 
	{Point[{{0, 0}, {a, a}}], Text[\[Psi] (x), {0, 0}, {1, 1}], Text[    \
        \[Mu]        \[Nu]
\[Psi] (x + \[Delta] \[InvisibleComma] x  + \[Delta] \
\[InvisibleComma] x ), {a, a}, { - 0.9,  - 1}]}}], {0.3, 0.3}]}, \
ImageSize -> 170]

Out[551]=
\\!\\(\\*GraphicsBox[{{AbsoluteThickness[1], Arrowheads[0.06], \
ArrowBox[{{0, 0}, {1, 0}}], 
   ArrowBox[{{0, 0}, {0, 1}}]}, {InsetBox[\"\\\"\\\\!\\\\(x\\\\^\[Mu]\
\\\\)\\\"\", {1, 0}, 
    NCache[ImageScaled[{-0.25, 1/2}], ImageScaled[{-0.25, 0.5}]]], 
   InsetBox[\"\\\"\\\\!\\\\ ... {1.1, 0.5}]]]}, 
     {PointBox[{{0, 0}, {0.5, 0.5}}], \
InsetBox[\"\\\"\\\\!\\\\(\[Psi](x)\\\\)\\\"\", {0, 0}, \
ImageScaled[{1, 1}]], 
      InsetBox[\"\\\"\\\\!\\\\(\[Psi](x+\[Delta]\[InvisibleComma]x\\\\\
^\[Mu]+\[Delta]\[InvisibleComma]x\\\\^\[Nu])\\\\)\\\"\", {0.5, 0.5}, 
       ImageScaled[{0.049, 0}]]}}}, {0.3, 0.3}]}, ImageSize -> 170]\\)
```

Using Eq. (XXX), prove Eq. (XXX) by comparing the above two paths to \
transport \\[Psi](x) to \\[Psi](x + \
\\[Delta]\\[InvisibleComma]x^\\[Mu] + \\[Delta]\\
\\[InvisibleComma]x^\\[Nu]).

Consider transporting from $$x$$ to $$x+\\delta x^{\\mu }+\\delta x^{\
\\nu }$$ through two paths (red v.s. blue), there are two ways to \
interpret the change of $$\\psi \\left(x+\\delta x^{\\mu }+\\delta \
x^{\\nu }\\right)$$ relative to $$\\psi (x)$$ :

* Red path:

```wl
$$\\psi \\left(x+\\delta x^{\\mu }+\\delta x^{\\nu \
}\\right)=e^{\\frac{i}{\\hbar }A_{\\nu }\\left(x+\\delta x^{\\mu \
}\\right)\\delta x^{\\nu }}e^{\\delta x^{\\nu }D_{\\nu
}}\\psi \\left(x+\\delta x^{\\mu }\\right)$$
$$=e^{\\frac{i}{\\hbar }A_{\\nu }\\left(x+\\delta x^{\\mu \
}\\right)\\delta x^{\\nu }}e^{\\frac{i}{\\hbar }A_{\\mu }(x)\\delta \
x^{\\mu }}e^{\\delta x^{\\mu }D_{\\mu
}}e^{\\delta x^{\\nu }D_{\\nu }}\\psi (x)$$
$$=\\exp \\left(\\frac{i}{\\hbar }\\left(A_{\\nu }(x)\\delta x^{\\nu \
}+A_{\\mu }(x)\\delta x^{\\mu }+\\partial _{\\mu }A_{\\nu }(x)\\delta \
x^{\\mu }\\delta x^{\\nu
}+\\ldots \\right)\\right)\\exp \\left(\\delta x^{\\mu }D_{\\mu \
}+\\delta x^{\\nu }D_{\\nu }+\\frac{1}{2}\\delta x^{\\mu }\\delta x^{\
\\nu }\\left[D_{\\mu },D_{\\nu
}\\right]+\\ldots \\right)\\psi (x)$$
```

* Blue path:

```wl
$$\\psi \\left(x+\\delta x^{\\mu }+\\delta x^{\\nu \
}\\right)=e^{\\frac{i}{\\hbar }A_{\\mu }\\left(x+\\delta x^{\\nu \
}\\right)\\delta x^{\\mu }}e^{\\delta x^{\\mu }D_{\\mu
}}\\psi \\left(x+\\delta x^{\\nu }\\right)$$
$$=e^{\\frac{i}{\\hbar }A_{\\mu }\\left(x+\\delta x^{\\nu \
}\\right)\\delta x^{\\mu }}e^{\\frac{i}{\\hbar }A_{\\nu }(x)\\delta \
x^{\\nu }}e^{\\delta x^{\\nu }D_{\\nu
}}e^{\\delta x^{\\mu }D_{\\mu }}\\psi (x)$$
$$=\\exp \\left(\\frac{i}{\\hbar }\\left(A_{\\mu }(x)\\delta x^{\\mu \
}+A_{\\nu }(x)\\delta x^{\\nu }+\\partial _{\\nu }A_{\\mu }(x)\\delta \
x^{\\mu }\\delta x^{\\nu
}+\\ldots \\right)\\right)\\exp \\left(\\delta x^{\\nu }D_{\\nu \
}+\\delta x^{\\mu }D_{\\mu }+\\frac{1}{2}\\delta x^{\\nu }\\delta x^{\
\\mu }\\left[D_{\\nu },D_{\\mu
}\\right]+\\ldots \\right)\\psi (x)$$
```

The two paths should match for any $$\\psi (x)$$, thus we must \
require the operator-level identity

```wl
$$\\exp \\left(\\frac{i}{\\hbar }\\left(A_{\\nu }(x)\\delta x^{\\nu \
}+A_{\\mu }(x)\\delta x^{\\mu }+\\partial _{\\mu }A_{\\nu }(x)\\delta \
x^{\\mu }\\delta x^{\\nu
}+\\ldots \\right)\\right)\\exp \\left(\\delta x^{\\mu }D_{\\mu \
}+\\delta x^{\\nu }D_{\\nu }+\\frac{1}{2}\\delta x^{\\mu }\\delta x^{\
\\nu }\\left[D_{\\mu },D_{\\nu
}\\right]+\\ldots \\right)=\\\\
\\exp \\left(\\frac{i}{\\hbar }\\left(A_{\\mu }(x)\\delta x^{\\mu \
}+A_{\\nu }(x)\\delta x^{\\nu }+\\partial _{\\nu }A_{\\mu }(x)\\delta \
x^{\\mu }\\delta x^{\\nu }+\\ldots
\\right)\\right)\\exp \\left(\\delta x^{\\nu }D_{\\nu }+\\delta \
x^{\\mu }D_{\\mu }+\\frac{1}{2}\\delta x^{\\nu }\\delta x^{\\mu \
}\\left[D_{\\nu },D_{\\mu }\\right]+\\ldots
\\right).$$
```

Rearrange terms,

```wl
$$\\exp \\left(\\frac{i}{\\hbar }\\left(\\partial _{\\mu }A_{\\nu \
}-\\partial _{\\nu }A_{\\mu }\\right)\\delta x^{\\mu }\\delta x^{\\nu \
}+\\ldots \\right)=\\exp \\left(-\\delta
x^{\\mu }\\delta x^{\\nu }\\left[D_{\\mu },D_{\\nu }\\right]+\\ldots \
\\right).$$
```

The left-hand-side is accumulated phase factor around the loop. Thus \
the adiabatic action is

```wl
$$\\delta S=\\left(\\partial _{\\mu }A_{\\nu }-\\partial _{\\nu \
}A_{\\mu }\\right)\\delta x^{\\mu }\\delta x^{\\nu },$$
```

which should be related to the curvature $$F_{\\mu \\, \\nu }$$ by $$\
\\delta S=F_{\\mu \\, \\nu }\\delta x^{\\mu }\\delta x^{\\nu }$$ by \
definition. By further matching the right-hand-side, we have

```wl
$$-\\frac{i}{\\hbar }F_{\\mu \\, \\nu }=\\left[D_{\\mu },D_{\\nu \
}\\right]$$
```

as an operator identity.

* Physical meaning :  In electromagnetism, $$F_{\\mu \\, \\nu }$$ \
corresponds to the **electromagnetic field strength tensor**,

```wl
$$F_{\\mu \\, \\nu }=\\partial _{\\mu }A_{\\nu }-\\partial _{\\nu \
}A_{\\mu }.$$
```

Derive Eq. (XXX) from Eq. (XXX).

The commutation of covariant derivative is

```wl
$$\\left[D_{\\mu },D_{\\nu }\\right]\\psi =\\left(D_{\\mu }D_{\\nu \
}-D_{\\nu }D_{\\mu }\\right)\\psi$$
$$=\\left(\\partial _{\\mu }-\\frac{i}{\\hbar }A_{\\mu \
}\\right)\\left(\\partial _{\\nu }-\\frac{i}{\\hbar }A_{\\nu \
}\\right)\\psi -\\left(\\partial _{\\nu }-\\frac{i}{\\hbar
}A_{\\nu }\\right)\\left(\\partial _{\\mu }-\\frac{i}{\\hbar }A_{\\mu \
}\\right)\\psi$$
$$=\\partial _{\\mu }\\left(\\partial _{\\nu }\\psi -\\frac{i}{\\hbar \
}A_{\\nu }\\psi \\right)-\\frac{i}{\\hbar }A_{\\mu }\\left(\\partial \
_{\\nu }\\psi -\\frac{i}{\\hbar
}A_{\\nu }\\psi \\right)-\\partial _{\\nu }\\left(\\partial _{\\mu \
}\\psi -\\frac{i}{\\hbar }A_{\\mu }\\psi \\right)+\\frac{i}{\\hbar \
}A_{\\nu }\\left(\\partial _{\\mu
}\\psi -\\frac{i}{\\hbar }A_{\\mu }\\psi \\right)$$
$$=\\partial _{\\mu }\\partial _{\\nu }\\psi -\\frac{i}{\\hbar \
}\\partial _{\\mu }A_{\\nu }\\psi -\\frac{i}{\\hbar }A_{\\nu \
}\\partial _{\\mu }\\psi -\\frac{i}{\\hbar
}A_{\\mu }\\partial _{\\nu }\\psi -\\frac{1}{\\hbar ^2}A_{\\mu \
}A_{\\nu }\\psi -\\partial _{\\nu }\\partial _{\\mu }\\psi \
+\\frac{i}{\\hbar }\\partial _{\\nu }A_{\\mu
}\\psi +\\frac{i}{\\hbar }A_{\\mu }\\partial _{\\nu }\\psi \
+\\frac{i}{\\hbar }A_{\\nu }\\partial _{\\mu }\\psi +\\frac{1}{\\hbar \
^2}A_{\\nu }A_{\\mu }\\psi$$
$$=-\\frac{i}{\\hbar }\\left(\\partial _{\\mu }A_{\\nu }-\\partial _{\
\\nu }A_{\\mu }\\right)\\psi .$$
```

To match the definition Eq. (XXX),

```wl
$$\\left[D_{\\mu },D_{\\nu }\\right]\\psi =-\\frac{i}{\\hbar } \
F_{\\mu \\, \\nu }\\psi ,$$
```

the gauge curvature $$F_{\\mu \\, \\nu }$$ can be identified as

```wl
$$F_{\\mu \\, \\nu }=\\partial _{\\mu }A_{\\nu }-\\partial _{\\nu \
}A_{\\mu }.$$
```

	* **Electric field**: $$\\pmb{E}=\\left(E^1,E^2,E^3\\right)$$, with \
$$E^i\\text{:=}-F_{0i}$$.

```wl
$$\\pmb{E}=-\\nabla \\Phi -\\partial _t\\pmb{A}.$$
```

	* **Magnetic field**: $$\\pmb{B}=\\left(B^1,B^2,B^3\\right)$$, with \
$$B^i\\text{:=}\\frac{1}{2}\\epsilon ^{i\\, j\\, k}F_{j\\, k}$$.

```wl
$$\\pmb{B}=\\nabla \\times \\pmb{A}.$$
```

Check that $$\\pmb{E}$$ and $$\\pmb{B}$$ are gauge invariant. \
Therefore, they are physical observables.

Under gauge transformation

```wl
$$\\Phi \\text{-$>$}\\Phi -\\partial _t\\chi ,\\\\
\\pmb{A}\\rightarrow \\pmb{A}+\\nabla \\chi ,$$
```

plugging into Eq. (XXX) and Eq. (XXX),

```wl
$$\\pmb{E}=-\\nabla \\Phi -\\partial _t\\pmb{A}$$
$$\\rightarrow -\\nabla \\left(\\Phi -\\partial _t\\chi \
\\right)-\\partial _t(\\pmb{A}+\\nabla \\chi )$$
$$=-\\nabla \\Phi +\\nabla \\partial _t\\chi -\\partial \
_t\\pmb{A}-\\partial _t\\nabla \\chi$$
$$=-\\nabla \\Phi -\\partial _t\\pmb{A}$$
$$=\\pmb{E}$$

$$\\pmb{B}=\\nabla \\times \\pmb{A}$$
$$\\rightarrow \\nabla \\times (\\pmb{A}+\\nabla \\chi )$$
$$=\\nabla \\times \\pmb{A}+\\nabla \\times \\nabla \\chi$$
$$=\\nabla \\times \\pmb{A}$$
$$=\\pmb{B}$$
```

#### Charged Particle in Gauge Field

In quantum mechanics, the time-evolution is generated by the \
Hamiltonian operator $$\\hat{H}$$.

* **Schrödinger picture**: *state* evolves in time, operator remains \
fixed.

```wl
$$i \\hbar \\partial _t\\psi =\\hat{H} \\psi .$$
```

* **Heisenberg picture**: *operator* evolves in time, state remains \
fixed.

```wl
$$i \\hbar \\partial _t\\hat{O}=\\left[\\hat{O},\\hat{H}\\right].$$
```

Note: Eq. (XXX) assumes 
\\!\\(\\*OverscriptBox[\\(O\\), \\(^\\)]\\) has no explicit time \
dependence, if not, its explicit time derivative will also contribute \
to the rate of change of 
\\!\\(\\*OverscriptBox[\\(O\\), \\(^\\)]\\).

Compare Eq. (XXX) with Eq. (XXX), we conclude that the Hamiltonian of \
the gauge-invariant Schrödinger equation is

```wl
$$\\hat{H}=-\\frac{\\hbar ^2}{2m}\\pmb{D}^2+\\Phi ,$$
```

or more explicitly as

```wl
$$\\hat{H}=H\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{x}}},\\hat{\\\
pmb{p}},t\\right)=\\frac{1}{2m}\\left(\\hat{\\pmb{p}}-\\pmb{A}\\left(\
\\pmb{\\overset{{}^{\\wedge}}{\\pmb{x}}},t\\right)\\right)^2+\\Phi
\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{x}}},t\\right),$$
```

where

* $$\\hat{\\pmb{x}}$$ is the **coordinate operator**.

* $$\\hat{\\pmb{p}}=-i \\hbar \\nabla$$ is the **momentum operator**.

* They satisfy the **canonical commutation relation**

```wl
$$\\left[\\hat{x}_i,\\hat{p}_j\\right]=i \\hbar  \\delta _{i\\, \
j}\\mathbf{1}.$$
```

Verify Eq. (XXX).

```wl
$$\\left[\\hat{x}_i,\\hat{p}_j\\right]\\psi =\\left[x_i,-i \\hbar \
\\partial _j\\right]\\psi$$
$$=-i \\hbar  x_i\\partial _j\\psi +i \\hbar \\partial \
_j\\left(x_i\\psi \\right)$$
$$=-i \\hbar  x_i\\partial _j\\psi +i \\hbar  \\delta _{i\\, j}\\psi \
+i \\hbar  x_i\\partial _j\\psi$$
$$=i \\hbar  \\delta _{i\\, j}\\psi .$$
```

Since the above equation holds for any state $$\\psi$$, we obtain an \
operator identity

```wl
$$\\left[\\hat{x}_i,\\hat{p}_j\\right]=i \\hbar  \\delta _{i\\, \
j}\\mathbf{1}.$$
```

* $$\\hat{\\Phi }=\\Phi \
\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{x}}},t\\right)$$ and \
$$\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}=\\pmb{A}\\left(\\pmb{\\\
overset{{}^{\\wedge}}{\\pmb{x}}},t\\right)$$ are **operator functions** \
of $$\\hat{\\pmb{x}}$$, with *explicit* time $$t$$ dependence.

Using the Heisenberg equation Eq. (XXX), we can compute time \
derivatives of the particle position operator 
\\!\\(\\*OverscriptBox[
StyleBox[\"x\",
FontWeight->\"Bold\"], \\(^\\)]\\)

* 1st order (velocity operator)

```wl
$$\\partial _t\\hat{\\pmb{x}}=\\frac{1}{i \\hbar \
}\\left[\\hat{\\pmb{x}},\\hat{H}\\right]=\\frac{\\hat{\\pmb{p}}-\\pmb{\
\\overset{{}^{\\wedge}}{\\pmb{A}}}}{m}.$$
```

* 2nd order (acceleration operator)

```wl
$$\\partial _t^2\\hat{\\pmb{x}}=-\\frac{1}{m}\\partial \
_t\\hat{\\pmb{A}}+\\frac{1}{i \\hbar }\\left[\\partial \
_t\\hat{\\pmb{x}},\\hat{H}\\right]$$
$$=\\frac{1}{m}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{E}}}+\\frac{\
1}{2}\\left(\\partial _t\\hat{\\pmb{x}}\\times \\hat{\\pmb{B}}-\\hat{\
\\pmb{B}}\\times \\partial
_t\\hat{\\pmb{x}}\\right)\\right),$$
```

where $$\\hat{\\pmb{E}}$$ and $$\\hat{\\pmb{B}}$$ operators are \
defined by

```wl
$$\\pmb{\\overset{{}^{\\wedge}}{\\pmb{E}}}=-\\nabla \\hat{\\Phi \
}-\\partial _t\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}},\\\\
\\pmb{\\overset{{}^{\\wedge}}{\\pmb{B}}}=\\nabla \\times \
\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}.$$
```

Derive Eq. (XXX) and Eq. (XXX).

Calculate the following useful commutators

* $$\\left[\\hat{\\pmb{x}},\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\
\\wedge}}{\\pmb{A}}}\\right)^2\\right]$$ :

```wl
$$\\left[\\hat{\\pmb{x}},\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\\
wedge}}{\\pmb{A}}}\\right)^2\\right]=\\left[\\hat{x}_i,\\left(\\hat{p_\
j}-\\pmb{\\overset{{}^{\\wedge}}{A_j}}\\right)\\left(\\hat{p_j}-\\pmb{\
\\overset{{}^{\\wedge}}{A_j}}\\right)\\right]$$
$$=\\left(\\hat{p_j}-\\pmb{\\overset{{}^{\\wedge}}{A_j}}\\right)\\\
left[\\hat{x}_i,\\left(\\hat{p_j}-\\pmb{\\overset{{}^{\\wedge}}{A_j}}\
\\right)\\right]+\\left[\\hat{x}_i,\\left(\\hat{p_j}-\\pmb{\\overset{{\
}^{\\wedge}}{A_j}}\\right)\\right]\\left(\\hat{p_j}-\\pmb{\\overset{{}\
^{\\wedge}}{A_j}}\\right)$$
$$=\\left(\\hat{p_j}-\\pmb{\\overset{{}^{\\wedge}}{A_j}}\\right)\\\
left[\\hat{x}_i,\\hat{p_j}\\right]+\\left[\\hat{x}_i,\\hat{p_j}\\\
right]\\left(\\hat{p_j}-\\pmb{\\overset{{}^{\\wedge}}{A_j}}\\right)$$
$$=\\left(\\hat{p_j}-\\pmb{\\overset{{}^{\\wedge}}{A_j}}\\right)i \
\\hbar  \\delta _{i\\, j}+i \\hbar  \\delta _{i\\, \
j}\\left(\\hat{p_j}-\\pmb{\\overset{{}^{\\wedge}}{A_j}}\\right)$$
$$=2i \\hbar  \\left(\\hat{p_i}-\\hat{A}_i\\right)$$
$$=2i \\hbar  \
\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\\
right).$$
```

* $$\\left[\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}},\\\
hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right]$$ :

```wl
$$\\left[\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}},\\\
hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right]=\\left[\
\\hat{p}_i-\\hat{A}_i,\\hat{p}_j-\\hat{A}_j\\right]$$
$$=-\\left[\\hat{p}_i,\\hat{A}_j\\right]-\\left[\\hat{A}_i,\\hat{p}_j\
\\right]$$
$$=-\\left[\\hat{p}_i,\\hat{x}_k\\right]\\partial \
_k\\hat{A}_j-\\partial \
_k\\hat{A}_i\\left[\\hat{x}_k,\\hat{p}_j\\right]$$
$$=i \\hbar  \\left(\\delta _{i\\, k}\\partial _k\\hat{A}_j-\\partial \
_k\\hat{A}_i\\delta _{k\\, j}\\right)$$
$$=i \\hbar  \\left(\\partial _i\\hat{A}_j-\\partial \
_j\\hat{A}_i\\right)$$
$$=i \\hbar  \\epsilon ^{i\\, j\\, k}\\epsilon ^{k\\, l\\, \
m}\\partial _l\\hat{A}_m$$
$$=i \\hbar  \\epsilon ^{i\\, j\\, k}\\hat{B}_k,$$
```

where we have introduced $$\\hat{B}_i=\\epsilon ^{i\\, j\\, \
k}\\partial _j\\hat{A}_k$$, or $$\\hat{\\pmb{B}}=\\nabla \\times \
\\hat{\\pmb{A}}$$.

* $$\\left[\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}},\\\
left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right)^\
2\\right]$$ :

```wl
$$\\left[\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}},\\\
left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right)^\
2\\right]=\\left[\\hat{p}_i-\\hat{A}_i,\\left(\\hat{p}_j-\\hat{A}_j\\\
right)\\left(\\hat{p}_j-\\hat{A}_j\\right)\\right]$$
$$=\\left(\\hat{p}_j-\\hat{A}_j\\right)\\left[\\hat{p}_i-\\hat{A}_i,\\\
hat{p}_j-\\hat{A}_j\\right]+\\left[\\hat{p}_i-\\hat{A}_i,\\hat{p}_j-\\\
hat{A}_j\\right]\\left(\\hat{p}_j-\\hat{A}_j\\right)$$
$$=i \\hbar  \\epsilon ^{i\\, j\\, k} \
\\left(\\left(\\hat{p}_j-\\hat{A}_j\\right)\\hat{B}_k+\\hat{B}_k \
\\left(\\hat{p}_j-\\hat{A}_j\\right)\\right)$$
$$=i \\hbar  \
\\left(\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\
\\right)\\times \\hat{\\pmb{B}}-\\hat{\\pmb{B}}\\times \
\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\\
right)\\right).$$
```

* $$\\left[\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}},\\\
hat{\\Phi }\\right]$$ :

```wl
$$\\left[\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}},\\\
hat{\\Phi }\\right]=\\left[\\hat{\\pmb{p}},\\hat{\\Phi }\\right]$$
$$=\\left[\\hat{p}_i,\\hat{x}_j\\right]\\partial _j\\hat{\\Phi }$$
$$=-i \\hbar  \\delta _{i\\, j}\\partial _j\\hat{\\Phi }$$
$$=-i \\hbar  \\nabla \\hat{\\Phi }.$$
```

Using these results, we can evaluate

* 1st order

```wl
$$\\partial _t\\hat{\\pmb{x}}=\\frac{1}{i \\hbar \
}\\left[\\hat{\\pmb{x}},\\hat{H}\\right]$$
$$=\\frac{1}{i \\hbar \
}\\left[\\hat{\\pmb{x}},\\frac{1}{2m}\\left(\\hat{\\pmb{p}}-\\pmb{\\\
overset{{}^{\\wedge}}{\\pmb{A}}}\\right)^2+\\hat{\\Phi }\\right]$$
$$=\\frac{1}{2i \\hbar  \
m}\\left[\\hat{\\pmb{x}},\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\\
wedge}}{\\pmb{A}}}\\right)^2\\right]$$
$$=\\frac{1}{2i \\hbar  m}2i \\hbar  \
\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\\
right)$$
$$=\\frac{\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}}{m}\
.$$
```

* 2nd order

```wl
$$\\partial _t^2\\hat{\\pmb{x}}=-\\frac{1}{m}\\partial \
_t\\hat{\\pmb{A}}+\\frac{1}{i \\hbar }\\left[\\partial \
_t\\hat{\\pmb{x}},\\hat{H}\\right]$$
$$=-\\frac{1}{m}\\partial _t\\hat{\\pmb{A}}+\\frac{1}{i \\hbar  \
m}\\left[\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}},\\\
frac{1}{2m}\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{\
A}}}\\right)^2+\\hat{\\Phi
}\\right]$$
$$=\\frac{1}{m}\\left(-\\partial _t\\hat{\\pmb{A}}+\\frac{1}{i \\hbar \
}\\left(\\frac{1}{2m}\\left[\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\\
wedge}}{\\pmb{A}}},\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}\
}{\\pmb{A}}}\\right)^2\\right]+\\left[\\hat{\\pmb{p}}-\\pmb{\\overset{\
{}^{\\wedge}}{\\pmb{A}}},\\hat{\\Phi
}\\right]\\right)\\right)$$
$$=\\frac{1}{m}\\left(-\\partial _t\\hat{\\pmb{A}}+\\frac{1}{i \\hbar \
}\\left(\\frac{i \\hbar \
}{2m}\\left(\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\\
pmb{A}}}\\right)\\times
\\hat{\\pmb{B}}-\\hat{\\pmb{B}}\\times \
\\left(\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\\
right)\\right)-i \\hbar  \\nabla \\hat{\\Phi }\\right)\\right)$$
$$=\\frac{1}{m}\\left(-\\partial \
_t\\hat{\\pmb{A}}+\\frac{1}{2}\\left(\\left(\\frac{\\hat{\\pmb{p}}-\\\
pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}}{m}\\right)\\times \
\\hat{\\pmb{B}}-\\hat{\\pmb{B}}\\times
\\left(\\frac{\\hat{\\pmb{p}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\
}{m}\\right)\\right)-\\nabla \\hat{\\Phi }\\right)$$
$$=\\frac{1}{m}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{E}}}+\\frac{\
1}{2}\\left(\\partial _t\\hat{\\pmb{x}}\\times \\hat{\\pmb{B}}-\\hat{\
\\pmb{B}}\\times \\partial
_t\\hat{\\pmb{x}}\\right)\\right).$$
```

where we introduce \
$$\\pmb{\\overset{{}^{\\wedge}}{\\pmb{E}}}=-\\nabla \\hat{\\Phi \
}-\\partial _t\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}$$.

Eq. (XXX) describes the quantum dynamics of a charged particle in an \
electromagnetic field in the Heisenberg picture:

```wl
$$m \\partial \
_t^2\\hat{\\pmb{x}}=\\pmb{\\overset{{}^{\\wedge}}{\\pmb{E}}}+\\frac{1}\
{2}\\left(\\partial _t\\hat{\\pmb{x}}\\times \
\\hat{\\pmb{B}}-\\hat{\\pmb{B}}\\times
\\partial _t\\hat{\\pmb{x}}\\right).$$
```

In contrast, the **classical dynamics** is described by

```wl
$$m \\ddot{\\pmb{x}}=\\pmb{F}=\\pmb{E}+\\dot{\\pmb{x}}\\times \
\\pmb{B},$$
```

where all quantities commute. In the quantum case, however, \\!\\(
\\*SubscriptBox[\\(\\[PartialD]\\), \\(t\\)]\\*
OverscriptBox[
StyleBox[\"x\",
FontWeight->\"Bold\"], \"^\"]\\) and 
\\!\\(\\*OverscriptBox[
StyleBox[\"B\",
FontWeight->\"Bold\"], \\(^\\)]\\) generally do not commute, so their \
cross product must be symmetrized as in Eq. (XXX).

#### Aharonov-Bohm Effect

In quantum mechanics, the *motion* of a charged particle can be \
*influenced* by the **gauge fields** $$\\Phi$$ and $$\\pmb{A}$$ \
through **quantum interference**, even in the *absence* of \
electromagnetic fields (i.e. $$\\pmb{E}=\\pmb{B}=0$$) when there is \
no Lorentz force acting on the particle at all!

* Setup: Aharonov-Bohm Experiment

	* **Physical Arrangement**: Consider a long, thin solenoid carrying \
a magnetic flux $$\\phi _B$$. Outside the solenoid, the magnetic \
field $$\\pmb{B}$$ is zero, but the vector potential $$\\pmb{A}$$ is \
nonzero. For any surface $$\\mathcal{S}$$ that fully covers the \
solenoid, we have

```wl
$$\\phi _B=\\int _{\\mathcal{S}}\\pmb{B}\\cdot d\\pmb{\\sigma \
}=\\oint _{\\partial \\mathcal{S}}\\pmb{A}\\cdot d\\pmb{l}.$$

In[14]:=
Block[{sol, gauge, traj}, 
	sol = Block[{lt = 0.9}, {{EdgeForm[Black], Lighter[Green, lt], \
Disk[]}, {Green, Point[Cases[Tuples[Range[ - 1, 1, 0.4], 2], p_ /; \
Norm[p] < 1]]}, {{{Lighter[Green, lt], Table[Translate[#, r], {r, \
0.08CirclePoints[24]}]}, {Green, \
#}}&@Text[\"\\!\\(\[VeryThinSpace]**B**\\)\", {0, 0}]}}];
	gauge := Block[{a = 0.2, b = 0.5, rs}, 
	rs = Table[Piecewise[{{Exp[1 / 2(2x - 1)], x > 1 / 2}, {Sqrt[2x], \
True}}], {x, a, 2, 0.5}];{Red, Arrowheads[{0.01, #, \
Graphics[{Line[Offset /@ {{ - 5, 3}, {0, 0}, { - 5,  - 3}}]}]}& /@ \
{0, 0.5}], Table[Arrow[ReIm[r Exp[I (b Log[r] + Range[0, 2\[Pi], \
\[Pi] / 32])]]], {r, rs}], Text[\"\\!\\(\[VeryThinSpace]**A**\\)\", \
{1.5, 0.4}]}];
	traj = {Blue, {Arrowheads[{{0.06, 0.53}}], AbsoluteThickness[2], \
Scale[Arrow[BSplineCurve[Block[{h1 = 0.15, h2 = 2.6}, {{ - 5, 0}, { - \
4.9, h1}, { - 2, h2}, {2, h2}, {4.9, h1}, {5, 0}}]]], {1, #}, {0, \
0}]& /@ {1,  - 1}}, {Text[\[ScriptCapitalC]
 1, {0,  - 2.4}, {0, 1}], Text[\[ScriptCapitalC]
 2, {0, 2.4}, {0,  - 0.8}]}, Translate[Block[{a = 0.2}, {Disk[{0, 0}, \
a], AbsoluteThickness[1], Table[Line[ReIm[{1.6, 2.2}a Exp[I \
\[Theta]]]], {\[Theta], \[Pi] / 6, 2\[Pi], \[Pi] / 6}], Text[\"source\
\", {0,  - 0.8}, {0, 1}]}], { - 5, 0}], Translate[Block[{h = 0.8, \
\[Alpha] = 0.3}, {Line[{0, #}& /@ { - h, h}], AbsoluteThickness[1], \
Table[Line[{{0, y}, {\[Alpha] h / 2, y - \[Alpha] h / 2}}], {y,  - h \
+ \[Alpha] h, h, \[Alpha] h}], Text[\"screen\", {0,  - 0.8}, {0, \
1}]}], {5, 0}]};
	Graphics[{sol, gauge, traj}, ImageSize -> 220]]

Out[14]=
\\!\\(\\*GraphicsBox[{{{RGBColor[0.9, 0.96, 0.915], \
EdgeForm[GrayLevel[0]], DiskBox[{0, 0}]}, 
   {RGBColor[0, 0.6, 0.15], PointBox[{{-0.6, -0.6}, {-0.6, -0.199}, \
{-0.6, 
     0.200}, {-0.6, 0.600}, {-0.199, -0.6}, 
     {-0.199, -0.199}, {-0.199, 0.200 ... .159}, {0.12, 0.039}}], 
       LineBox[{{0, 0.399}, {0.12, 0.279}}], 
       LineBox[{{0, 0.639}, {0.12, 0.519}}]}, 
      InsetBox[\"\\\"screen\\\"\", {0, -0.8}, \
NCache[ImageScaled[{1/2, 1}], ImageScaled[{0.5, 1}]]]}}, 
    {5, 0}]}}, ImageSize -> 220]\\)
```

	* **Interferometry**: A beam of electrons is split into two paths \
that *encircle* the solenoid in opposite directions and then \
recombine to produce an *interference* pattern.

* Key idea: Even when $$\\pmb{B}=0$$ outside the solenoid, the \
**vector potential** $$\\pmb{A}$$ influences the *phase* of the \
wavefunction.

	* When an electron travels along a path $$\\mathcal{C}$$, the \
wavefunction acquires a **Berry phase** :

```wl
$$\\psi \\overset{\\mathcal{C}}{\\rightarrow }\\psi  e^{i \\Theta \
_{\\mathcal{C}}}=\\psi  \\exp \\left(\\frac{i q}{\\hbar }\\int \
_{\\mathcal{C}}\\pmb{A}\\cdot d\\pmb{x}\\right),$$
```

where $$q=-e$$ is recovered to represent the electron charge.

	* The **phase difference** between the two paths is

```wl
$$\\Delta \\Theta =\\Theta _{\\mathcal{C}_1}-\\Theta \
_{\\mathcal{C}_2}=\\frac{q}{\\hbar }\\left(\\int \
_{\\mathcal{C}_1}\\pmb{A}\\cdot d\\pmb{x}-\\int \
_{\\mathcal{C}_2}\\pmb{A}\\cdot
d\\pmb{x}\\right).$$
```

	* By applying Stokes\[CloseCurlyQuote] theorem over the surface \
$$\\mathcal{S}$$ enclosed by the loop \
$$\\mathcal{C}=\\mathcal{C}_1-\\mathcal{C}_2=\\partial \\mathcal{S}$$,

```wl
$$\\Delta \\Theta =\\frac{q}{\\hbar }\\int _{\\mathcal{S}}(\\nabla \
\\times \\pmb{A})\\cdot d\\pmb{\\sigma }=\\frac{q \\phi _B}{\\hbar },$$
```

where $$\\phi _B$$ is the **magnetic flux** through $$\\mathcal{S}$$ \
(which equals to the flux inside the solenoid as long as \
$$\\mathcal{S}$$ covers the solenoid fully).

This phase shift manifests as a *shift* in the *interference fringes* \
when the two parts of the beam are *recombined*.

* Application: **Superconducting Quantum Interference Device** (SQUID)

	* A SQUID consists of a *superconducting loop* containing a \
*Josephson junction* (serving as the screen) and exploit quantum \
interference to detect extremely subtle changes in *magnetic flux* \
inside the loop.

	* By harnessing the *quantum-level sensitivity* of the Aharonov-Bohm \
(AB) effect, SQUIDs can measure magnetic fields as faint as \
$$5\\times 10^{-18}$$T at *microscopic* scales.

	* SQUIDs also play a pivotal role in *quantum computing*, as an \
approach towards *superconducting qubits*.

* Question: What Is Physical about Gauge Fields?

	* **Gauge Potentials vs. Field Strengths**: Traditionally, one might \
think only the fields $$\\pmb{E}$$ and $$\\pmb{B}$$ are *physical* \
since they are *gauge invariant* and can be measured directly by \
*forces*. However, the AB effect shows that the potentials $$\\Phi$$ \
and $$\\pmb{A}$$ also have direct physical \
consequences\[LongDash]they affect the phase of a quantum wavefunction.

	* **Holonomy and Berry Phase**: The Berry phase around any *closed \
loop* is gauge invariant, and should be *physical*. All such \
**closed-loop Berry phases** (aka. the **holonomies**) form the \
*complete* set of physical observables of a gauge theory. The AB \
phase is an example of a holonomy: the phase accumulated around a \
closed loop depends on the *curvature* (here, the magnetic flux \
$$\\phi _B$$) enclosed by the loop.

## Uniform Magnetic Field

### Classical Dynamics

#### Cyclotron Motion

The motion of a **charged particle** in the electromagnetic field is \
governed by the **Lorentz force** :

```wl
$$m \\ddot{\\pmb{x}}=\\pmb{F}=q \
\\left(\\pmb{E}+\\dot{\\pmb{x}}\\times \\pmb{B}\\right).$$
```

* $$m$$ - particle **mass**,

* $$q$$ - particle **charge**.

Consider the case: **uniform magnetic field** only,

```wl
$$\\pmb{E}=0, \\pmb{B}=B \\pmb{e}^z.$$

In[557]:=
Block[{a = 0.15, R = 2.6, r = 1.4, \[Theta] =  - \[Pi] / 6}, 
	Graphics[{{Green, AbsolutePointSize[3], Translate[{Circle[{0, 0}, \
a], Point[{0, 0}]}, #]& /@ Cases[Tuples[Range[ - #, #]&@Ceiling[R], \
2].{{1, 0}, { - 1 / 2, Sqrt[3] / 2}}, p_ /; Norm[p] < R], Text[\"\
\\!\\(\[VeryThinSpace]**B**\\)\", {1.9, 0.9}]}, {Black, \
Arrowheads[{0.01, # / 4, Graphics[Line[Offset /@ {{ - 4, 3}, {0, 0}, \
{ - 4,  - 3}}]]}& /@ Range[0, 3]], Arrow[r ReIm@Exp[I Range[2\[Pi], \
0,  - \[Pi] / 32]]], Dashed, Line[ReIm@{0, r Exp[I \[Theta]]}], \
Text[r
 c, ReIm[r / 2 Exp[I \[Theta]]], {0.8, 0.3}], Text[v
 c, {0, r}, {0, 1}], Point[{0, 0}], Text[\"\\!\\(**\[Xi]**\\)\", {0, \
0}, {2.5, 0}]}}, ImageSize -> 120]]

Out[557]=
\\!\\(\\*GraphicsBox[{{RGBColor[0, 0.6, 0.15], AbsolutePointSize[3], 
   {GeometricTransformationBox[{CircleBox[{0, 0}, 0.15], PointBox[{0, \
0}]}, 
     NCache[{-1, -Sqrt[3]}, {-1, -1.732}]], GeometricTransformationBox[
     {CircleBox[{0, 0}, 0.15], Poi ... ImageScaled[{1/2, 1}], \
ImageScaled[{0.5, 1}]]], PointBox[{0, 0}], 
    InsetBox[\"\\\"\\\\!\\\\(\\\\!\\\\(\\\\*StyleBox[\\\\\\\"\[Xi]\\\\\
\\\",FontWeight->\\\\\\\"Bold\\\\\\\"]\\\\)\\\\)\\\"\", {0, 0}, 
     NCache[ImageScaled[{1.75, 1/2}], ImageScaled[{1.75, 0.5}]]]}}}, \
ImageSize -> 120]\\)
```

Circular motion in $$x-y$$ plane:

```wl
$$\\dot{\\pmb{x}}=v_c\\left(\\cos \\left(\\omega \
_ct\\right)\\pmb{e}^x-\\sin \\left(\\omega \
_ct\\right)\\pmb{e}^y\\right),\\\\
\\pmb{x}=r_c\\left(\\sin \\left(\\omega _ct\\right)\\pmb{e}^x+\\cos \
\\left(\\omega _ct\\right)\\pmb{e}^y\\right)+\\pmb{\\xi },$$
```

Demonstrate Eq. (XXX) by solving the equation of motion Eq. (XXX).

Substitute Eq. (XXX) into Eq. (XXX), the equation of motion reads

```wl
$$\\ddot{\\pmb{x}}=\\frac{q B}{m} \\dot{\\pmb{x}}\\times \
\\pmb{e}^z.$$
```

In terms of components,

```wl
$$\\frac{d}{dt}\\dot{x}=\\frac{q B}{m}\\dot{y},\\\\
\\frac{d}{dt}\\dot{y}=-\\frac{q B}{m}\\dot{x}.$$
```

Therefore $$\\dot{x}$$ satisfies oscillatory equation

```wl
$$\\frac{d^2}{dt^2}\\dot{x}=-\\left(\\frac{q B}{m}\\right)^2\\dot{x},$$
```

which can be solved by

```wl
$$\\dot{x}=v_c\\cos \\left(\\omega _ct\\right),$$
```

with $$\\omega _c=q B/m$$. Thus

```wl
$$\\dot{y}=\\frac{m}{q B}\\frac{d}{dt}\\dot{x}=\\frac{1}{\\omega \
_c}\\frac{d}{dt}\\dot{x}=-v_c\\sin \\left(\\omega _ct\\right).$$
```

Put together,

```wl
$$\\dot{\\pmb{x}}=v_c\\left(\\cos \\left(\\omega \
_ct\\right)\\pmb{e}^x-\\sin \\left(\\omega \
_ct\\right)\\pmb{e}^y\\right).$$
```

Integrate with respect to $$t$$ on both sides,

```wl
$$\\pmb{x}=\\int dt \\dot{\\pmb{x}}=r_c\\left(\\sin \\left(\\omega \
_ct\\right)\\pmb{e}^x+\\cos \\left(\\omega \
_ct\\right)\\pmb{e}^y\\right)+\\pmb{\\xi },$$
```

where $$r_c=v_c/\\omega _c$$ and $$\\pmb{\\xi }$$ emerges as the \
integration constant.

* $$\\omega _c$$ - **cyclotron frequency** :

```wl
$$\\omega _c=\\frac{q B}{m}.$$
```

* $$v_c$$ - **cyclotron velocity**, set by the initial velocity of \
the particle,

* $$r_c$$ - **cyclotron radius**,

```wl
$$r_c=\\frac{v_c}{\\omega _c}=\\frac{m v_c}{q B}.$$
```

* $$\\pmb{\\xi }=\\xi _x\\pmb{e}^x+\\xi _y\\pmb{e}^y$$ - **guiding \
center** (the center of the cyclotron motion). It can be \
reconstructed from

```wl
$$\\pmb{\\xi }=\\pmb{x}-\\frac{r_c}{v_c}\\pmb{e}^z\\times \
\\dot{\\pmb{x}}=\\pmb{x}-\\frac{1}{q B}\\pmb{e}^z\\times \\pmb{\\pi \
},$$
```

where $$\\pmb{\\pi }=m \\dot{\\pmb{x}}$$ denotes the **kinetic \
momentum**.

Verify Eq. (XXX).

We first verify that

```wl
$$\\pmb{x}-\\frac{r_c}{v_c}\\pmb{e}^z\\times \\dot{\\pmb{x}}$$
$$=r_c\\left(\\sin \\left(\\omega _ct\\right)\\pmb{e}^x+\\cos \\left(\
\\omega _ct\\right)\\pmb{e}^y\\right)+\\pmb{\\xi \
}-\\frac{r_c}{v_c}\\pmb{e}^z\\times v_c\\left(\\cos
\\left(\\omega _ct\\right)\\pmb{e}^x-\\sin \\left(\\omega _ct\\right)\
\\pmb{e}^y\\right)$$
$$=r_c\\left(\\sin \\left(\\omega _ct\\right)\\pmb{e}^x+\\cos \\left(\
\\omega _ct\\right)\\pmb{e}^y-\\cos \\left(\\omega \
_ct\\right)\\pmb{e}^z\\times \\pmb{e}^x+\\sin
\\left(\\omega _ct\\right)\\pmb{e}^z\\times \\pmb{e}^y\\right)+\\pmb{\
\\xi }$$
$$=r_c\\left(\\sin \\left(\\omega _ct\\right)\\pmb{e}^x+\\cos \\left(\
\\omega _ct\\right)\\pmb{e}^y-\\cos \\left(\\omega \
_ct\\right)\\pmb{e}^y-\\sin \\left(\\omega \
_ct\\right)\\pmb{e}^x\\right)+\\pmb{\\xi
}$$
$$=\\pmb{\\xi }.$$
```

Introduce the kinetic momentum $$\\pmb{\\pi }=m \\dot{\\pmb{x}}$$,

```wl
$$\\pmb{\\xi }=\\pmb{x}-\\frac{r_c}{v_c}\\pmb{e}^z\\times \
\\dot{\\pmb{x}}$$
$$=\\pmb{x}-\\frac{r_c}{m v_c}\\pmb{e}^z\\times m\\dot{\\pmb{x}}$$
$$=\\pmb{x}-\\frac{1}{q B}\\pmb{e}^z\\times \\pmb{\\pi }.$$
```

#### Hall Effect

Consider the case: **uniform electric field** *perpendicular* to \
**uniform magnetic field**,

```wl
$$\\pmb{E}=E \\pmb{e}^y, \\pmb{B}=B \\pmb{e}^z.$$

In[547]:=
Block[{a = 0.15, R = 2.6, h = 0.5}, 
	Graphics[{{Green, AbsolutePointSize[3], Translate[{Circle[{0, 0}, \
a], Point[{0, 0}]}, #]& /@ Cases[Tuples[Range[ - #, #]&@Ceiling[R], \
2].{{1, 0}, { - 1 / 2, Sqrt[3] / 2}}, p_ /; Norm[p] < R], Text[\"\
\\!\\(\[VeryThinSpace]**B**\\)\", {1.55, 1.22}]}, 
	{Blue, Arrowheads[0.07], Translate[Arrow[{0, Sqrt[3]# / 2}& /@ { - \
R, R}], {#, 0}]& /@ Range[ - #, #]&@Floor[R], Text[\"\
\\!\\(\[VeryThinSpace]**E**\\)\", { - 1.68, 1.9}]}, {Black, \
Arrowheads[{0.01, # / 3, Graphics[Line[Offset /@ {{ - 4, 3}, {0, 0}, \
{ - 4,  - 3}}]]}& /@ Range[1, 2]], Translate[{Arrow[{0.82#, 0}& /@ { \
- R, R}], Text[v
 d, {0.24R, 0}, {0, 1}]}, {0, h}]}}, ImageSize -> 120]]

Out[547]=
\\!\\(\\*GraphicsBox[{{RGBColor[0, 0.6, 0.15], AbsolutePointSize[3], 
   {GeometricTransformationBox[{CircleBox[{0, 0}, 0.15], PointBox[{0, \
0}]}, 
     NCache[{-1, -Sqrt[3]}, {-1, -1.732}]], GeometricTransformationBox[
     {CircleBox[{0, 0}, 0.15], Poi ...  0}], 
         Offset[{-4, -3}]}]]}}], \
GeometricTransformationBox[{ArrowBox[{{-2.132, 0}, {2.132, 0}}], 
     InsetBox[\"\\\"\\\\!\\\\(v\\\\_d\\\\)\\\"\", {0.624, 0}, \
NCache[ImageScaled[{1/2, 1}], 
       ImageScaled[{0.5, 1}]]]}, {0, 0.5}]}}, ImageSize -> 120]\\)
```

The Lorentz force is balanced if

```wl
$$\\dot{\\pmb{x}}=\\frac{\\pmb{E}\\times \
\\pmb{B}}{B^2}=v_d\\pmb{e}^x.$$
```

* **Drift velocity** of charge:

```wl
$$v_d=\\frac{E}{B}.$$
```

* Corresponding **current density** :

```wl
$$\\pmb{j}=n q v_d\\pmb{e}^x,$$
```

where

	* $$n$$ - carrier** density**, number of charge carriers per unit \
area.

	* $$q$$ - carrier **charge**.

Justify Eq. (XXX).

Within the time interval $$dt$$, every charge will uniformly drift by

```wl
$$dx=v_ddt.$$

In[54]:=
Block[{Lx = 2, Ly = 1, dt = 0.5}, 
	Graphics[{{GrayLevel[0.9], Rectangle[{ - Lx,  - Ly}, {Lx, Ly}], \
Lighter[Red, 0.8], Rectangle[{ - Lx,  - Ly}, {dt, Ly}], Lighter[Red, \
0.6], Rectangle[{ - Lx,  - Ly}, {0, Ly}]}, {Arrowheads[0.05], Red, \
Translate[Arrow[{#, 0}& /@ {0, dt}], {0, # Ly / 4}]& /@ Range[ - 3, \
3]}, Translate[{{AbsoluteThickness[1], Arrowheads[{ - 0.001( - 1) ^ \
#, #, Graphics[Line[Offset /@ {{ - 4,  - 3}, {0, 0}, { - 4, 3}}]]}& /@ \
{0, 1}], Arrow[{0, #}& /@ { - Ly, Ly}]}, {{GrayLevel[0.9], \
Table[Translate[#, r], {r, 0.07CirclePoints[32]}]}, #}&@Text[L
 y]}, {0.8Lx, 0}], {Black, Translate[Line[{#, 0}& /@ { - Lx, Lx}], \
{0, #}]& /@ { - Ly, Ly}, Dashed, Red, Translate[Line[{0, #}& /@ { - \
Ly, Ly}], {#, 0}]& /@ {0, dt}}, Translate[{Text[v  \[DifferentialD] t
 d, {dt / 2, 0}, {0, 1}]}, {0,  - Ly}]}, ImageSize -> 160]]

Out[54]=
\\!\\(\\*GraphicsBox[{{{GrayLevel[0.9], RectangleBox[{-2, -1}, {2, \
1}]}, 
   {RGBColor[0.958, 0.840, 0.8], RectangleBox[{-2, -1}, {0.5, 1}]}, 
   {RGBColor[0.916, 0.679, 0.6], RectangleBox[{-2, -1}, {0, 1}]}}, 
  {RGBColor[0.79, 0.2, 0], Arrowheads[0.05 ... }}], {0, 0}], \
GeometricTransformationBox[LineBox[{{0, -1}, {0, 1}}], 
     {0.5, 0}]}}, \
GeometricTransformationBox[InsetBox[\"\\\"\\\\!\\\\(v\\\\_d \
\[DifferentialD]t\\\\)\\\"\", {0.25, 0}, 
    NCache[ImageScaled[{1/2, 1}], ImageScaled[{0.5, 1}]]], {0, -1}]}, \
ImageSize -> 160]\\)
```

This causes all charges within an *area* of $$L_ydx$$ to be \
transferred across a given *vertical cross-section*. The *total \
charge* in this area is

```wl
$$dQ=q n L_y dx,$$
```

so the transported *current* is

```wl
$$I_x=\\frac{dQ}{dt}=q n L_y\\frac{dx}{dt}=n q v_d L_y.$$
```

Therefore, the *current density*, i.e. the current passing through \
the cross-section per unit length, is

```wl
$$j_x=\\frac{I_x}{L_y}=n q v_d.$$
```

* **Hall conductivity** :

```wl
$$\\sigma _H\\text{:=}\\frac{j_x}{E_y}=\\frac{n q}{B}.$$
```

* **Hall resistivity** :

```wl
$$\\rho _H\\text{:=}\\frac{E_y}{j_x}=\\frac{B}{n q}.$$

In[531]:=
Block[{\[Beta] = 80., \[Mu] = 1., \[Sigma]H}, 
	\[Sigma]H[B_ ? NumericQ] := Block[{c = 5., nmin, nmax}, 
	{nmin, nmax} = (2{ - 1, 1}c - B \[Beta] + 2\[Beta] \[Mu]) / (2B \
\[Beta]);
	nmin = Max[0, Floor[nmin]];
	nmax = Ceiling[nmax];
	nmin + If[nmax - nmin < 10, NSum[LogisticSigmoid[\[Beta](\[Mu] - (n \
+ 1 / 2)B)], {n, nmin, nmax}], 1 / 2 + NIntegrate[LogisticSigmoid[\
\[Beta](\[Mu] - (n + 1 / 2)B)], {n, nmin, nmax}]]];
	Plot[{B, 1 / \[Sigma]H[B]}, {B, 0.001, 1}, GridLines -> {None, 1 / \
Range[6]}, PlotStyle -> {Directive[AbsoluteThickness[1.2], Dashed, \
LightGray], Black}, FrameTicks -> {{Automatic, {1 / #, If[# == 1, \"1\
\", If[MemberQ[{2, 3, 6}, #], Style[StringTemplate[\"1/`1`\"][#], \
10], \"\"]]}& /@ Range[6]}, {Automatic, Automatic}}, FrameLabel -> {\
\[VeryThinSpace]B [a.u.],        2
\[Rho]  [h/e ]
 H}, ImageSize -> 180]]

Out[531]=
\\!\\(\\*GraphicsBox[{{{}, {}, TagBox[{GrayLevel[0.85], \
AbsolutePointSize[4], AbsoluteThickness[1.2], 
     Opacity[1.], Dashing[{Small, Small}], LineBox[{{0.001, 0.001}, 
      {0.001, 0.001}, {0.001, 0.001}, 
      {0.002, 0.002}, {0.003, 0.003}, 
    ... } & )}}, 
 PlotRange -> {{0.001, 1}, {0., 1.}}, PlotRangeClipping -> True, 
 PlotRangePadding -> {{Scaled[0.02], Scaled[0.02]}, {Scaled[0.05], \
Scaled[0.05]}}, 
 Ticks -> {Automatic, Automatic}, TicksStyle -> \
Directive[GrayLevel[0], FontSize -> 12]]\\)
```

	* Classical expectation: given *fixed* carrier (electron) density \
$$n$$, $$\\rho _H\\propto B$$ should scale *linearly* with $$B$$.

	* **Quantum Hall effect**: when $$B$$ is large enough, $$\\sigma _H=\
\\rho _H^{-1}$$ exhibits *steps* at *quantized* values:

```wl
$$\\sigma _H=\\frac{\\nu  e^2}{h}\\text{  }(\\nu =1,2,3,\\ldots ).$$
```

		* $$h$$ - Planck constant,

		* $$e$$ - electron charge ($$q=-e$$ as charge carrier).

### Landau Level Quantization

#### Gauge Field

Two-dimensional electron system in the $$x-y$$ plane, with a \
**uniform magnetic field** perpendicular to the plane

```wl
$$\\pmb{B}=B \\pmb{e}^z=\\nabla \\times \\pmb{A}.$$
```

* The **vector potential** (gauge field) $$\\pmb{A}$$ circulates in \
the $$x-y$$ plane,

```wl
In[549]:=
Block[{a = 0.15, R = 2.6, \[Theta] =  - \[Pi] / 4}, 
	Graphics[{{Green, AbsolutePointSize[3], Translate[{Circle[{0, 0}, \
a], Point[{0, 0}]}, #]& /@ Cases[Tuples[Range[ - #, #]&@Ceiling[R], \
2].{{1, 0}, { - 1 / 2, Sqrt[3] / 2}}, p_ /; Norm[p] < R], Text[\"\
\\!\\(\[VeryThinSpace]**B**\\)\", {1.9, 0.9}]}, {Red, \
Arrowheads[{0.01, # / 4, Graphics[Line[Offset /@ {{ - 4, 3}, {0, 0}, \
{ - 4,  - 3}}]]}& /@ Range[0, 3]], Table[Arrow[r ReIm@Exp[I (Range[0, \
2\[Pi], \[Pi] / 32] + \[Theta])]], {r, Sqrt[Range[1, 3]]}], Text[\"\
\\!\\(\[VeryThinSpace]**A**\\)\", ReIm[ - I Sqrt[3]Exp[I \[Theta]]], \
{1, 1}]}}, ImageSize -> 120]]

Out[549]=
\\!\\(\\*GraphicsBox[{{RGBColor[0, 0.6, 0.15], AbsolutePointSize[3], 
   {GeometricTransformationBox[{CircleBox[{0, 0}, 0.15], PointBox[{0, \
0}]}, 
     NCache[{-1, -Sqrt[3]}, {-1, -1.732}]], GeometricTransformationBox[
     {CircleBox[{0, 0}, 0.15], Poi ...    -1.440}, {1.098, -1.338}, \
{1.224, 
       -1.224}}]]}, 
   InsetBox[\"\\\"\\\\!\\\\(\[VeryThinSpace]\\\\!\\\\(\\\\*StyleBox[\\\
\\\\\"A\\\\\\\",FontWeight->\\\\\\\"Bold\\\\\\\"]\\\\)\\\\)\\\"\", 
    NCache[{-Sqrt[3/2], -Sqrt[3/2]}, {-1.224, -1.224}], 
    ImageScaled[{1, 1}]]}}, ImageSize -> 120]\\)

$$\\pmb{A}=\\left(A_x,A_y\\right)=\\frac{B}{2}(-y, x),$$
```

known as the **symmetric gauge**.

Verify Eq. (XXX) reproduces Eq. (XXX).

```wl
$$\\nabla \\times \\pmb{A}=\\left(\\partial _xA_y-\\partial \
_yA_x\\right)\\pmb{e}^z$$
$$=\\frac{B}{2}\\left(\\partial _xx+\\partial _yy\\right)\\pmb{e}^z$$
$$=\\frac{B}{2}(1+1)\\pmb{e}^z$$
$$=B \\pmb{e}^z=\\pmb{B}.$$
```

Therefore the gauge choice in Eq. (XXX) is indeed consistent with the \
setting of the uniform magnetic field.

* However, the gauge choice is not unique. For example, the following \
gauge choice is also valid:

```wl
$$\\pmb{A}=\\left(A_x,A_y\\right)=(0, B x),$$
```

known as the **Landau gauge**.

We will mostly work with the circular gauge Eq. (XXX), following \
Ref. [XXX].

David Tong. [The Quantum Hall \
Effect](https://courses.physics.ucsd.edu/2019/Spring/physics230/\
GOODIES/Tong_QHE.pdf) (TIFR Infosys Lectures), (2016).

#### Hamiltonian

Following Eq. (XXX), the Hamiltonian of the gauge-invariant \
Schrödinger equation reads

```wl
$$\\hat{H}=-\\frac{\\hbar ^2}{2m}\\pmb{D}^2=-\\frac{\\hbar \
^2}{2m}\\left(\\nabla -\\frac{i q}{\\hbar \
}\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right)^2.$$
```

* Unit choice:

	* charge $$q=1$$,

	* mass $$m=1$$,

	* Planck constant $$\\hbar =1$$.

Eq. (XXX) can be simplified to

```wl
$$\\hat{H}=\\frac{1}{2}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}\
-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right)^2=\\frac{1}{2}\\hat{\
\\pmb{\\pi }}^2.$$
```

* $$\\hat{\\pmb{p}}=-i \\nabla =\\left(-i \\partial _x,-i\\partial _y\
\\right)$$ - **canonical momentum** operator.

	* **Canonical commutation** relation with **coordinate** operator $$\
\\hat{\\pmb{x}}=\\left(\\hat{x},\\hat{y}\\right)$$ :

```wl
$$\\left[\\hat{x}_i,\\hat{p}_j\\right]=i \\delta _{i\\, j}\\text{    \
}(\\text{for}).$$
```

* \\!\\(\\*OverscriptBox[
StyleBox[\"A\",
FontWeight->\"Bold\"], 
StyleBox[\"^\",
FontWeight->\"Plain\"]]\\) = A(
\\!\\(\\*OverscriptBox[
StyleBox[\"x\",
FontWeight->\"Bold\"], \\(^\\)]\\)) = (Subscript[
\\!\\(\\*OverscriptBox[\\(A\\), \\(^\\)]\\), x], Subscript[
\\!\\(\\*OverscriptBox[\\(A\\), \\(^\\)]\\), y]) - potential momentum \
operator (electromagnetic vector potential). Under symmetric gauge \
Eq. (XXX),

```wl
$$\\hat{A}_x=-\\frac{B}{2}\\hat{y}, \
\\hat{A}_y=\\frac{B}{2}\\hat{x}.$$
```

* $$\\hat{\\pmb{\\pi }}=\\left(\\hat{\\pi }_x,\\hat{\\pi \
}_y\\right)\\,$$ - **kinetic momentum** operator,

```wl
$$\\hat{\\pmb{\\pi }}=\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}-\\pmb{\
\\overset{{}^{\\wedge}}{\\pmb{A}}}=-i \\nabla \
-\\pmb{A}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{x}}}\\right)=-i
\\pmb{D},$$
```

or, in terms of components

```wl
$$\\hat{\\pi }_x=\\hat{p}_x-\\hat{A}_x=-i \\partial \
_x-\\hat{A}_x,\\\\
\\hat{\\pi }_y=\\hat{p}_y-\\hat{A}_y=-i \\partial _y-\\hat{A}_y.$$
```

	* They satisfy the following commutation relation

```wl
$$\\left[\\hat{\\pi }_x,\\hat{\\pi }_y\\right]=i B,$$
```

which follows from the definition of gauge curvature in Eq. (XXX).

Verify Eq. (XXX).

```wl
$$\\left[\\hat{\\pi }_x,\\hat{\\pi }_y\\right]=\\left[-i \\partial \
_x-A_x,-i \\partial _y-A_y\\right]$$
$$=-\\left[\\partial _x,\\partial _y\\right]+i \\left[\\partial \
_x,A_y\\right]+i \\left[A_x,\\partial \
_y\\right]+\\left[A_x,A_y\\right]$$
$$=0+i \\partial _xA_y-i \\partial _yA_x+0$$
$$=i \\left(\\partial _xA_y-\\partial _yA_x\\right)$$
$$=i B.$$
```

	* They also inherit the commutation relation with the coordinate \
operator,

```wl
$$\\left[\\hat{x}_i,\\hat{\\pi }_j\\right]=i \\delta _{i\\, j}\\text{ \
 }(\\text{for}).$$
```

#### Guiding Center

Following Eq. (XXX), the guiding center operator 
\\!\\(\\*OverscriptBox[
StyleBox[\"\\[Xi]\",
FontWeight->\"Bold\"], \\(^\\)]\\) = (Subscript[\\[Xi], x], \
Subscript[\\[Xi],
   y]) is defined as

```wl
$$\\hat{\\pmb{\\xi }}=\\hat{\\pmb{x}}-\\frac{1}{B}\\pmb{e}^z\\times \
\\hat{\\pmb{\\pi }}.$$
```

* Under symmetric gauge Eq. (XXX),

```wl
$$\\hat{\\pmb{\\xi \
}}=\\frac{1}{B}\\left(\\hat{\\pmb{p}}+\\hat{\\pmb{A}}\\right)\\times \
\\pmb{e}^z,$$
```

Verify Eq. (XXX).

On one hand,

```wl
$$\\hat{\\pmb{\\xi }}=\\hat{\\pmb{x}}-\\frac{1}{B}\\pmb{e}^z\\times \
\\hat{\\pmb{\\pi }}$$
$$=\\hat{x}\\pmb{e}^x+\\hat{y}\\pmb{e}^y-\\frac{1}{B}\\pmb{e}^z\\\
times \\left(\\left(\\hat{p}_x-\\hat{A}_x\\right)\\pmb{e}^x+\\left(\\\
hat{p}_y-\\hat{A}_y\\right)\\pmb{e}^y\\right)$$
$$=\\hat{x}\\pmb{e}^x+\\hat{y}\\pmb{e}^y-\\frac{1}{B}\\left(\\left(\\\
hat{p}_x+\\frac{B}{2}\\hat{y}\\right)\\pmb{e}^z\\times \
\\pmb{e}^x+\\left(\\hat{p}_y-\\frac{B}{2}\\hat{x}\\right)\\pmb{e}^z\\\
times
\\pmb{e}^y\\right)$$
$$=\\frac{1}{B}\\left(B\\hat{x}\\pmb{e}^x+B\\hat{y}\\pmb{e}^y-\\left(\
\\hat{p}_x+\\frac{B}{2}\\hat{y}\\right)\\pmb{e}^y+\\left(\\hat{p}_y-\\\
frac{B}{2}\\hat{x}\\right)\\pmb{e}^x\\right)$$
$$=\\frac{1}{B}\\left(\\left(\\hat{p}_y+\\frac{B}{2}\\hat{x}\\right)\\\
pmb{e}^x-\\left(\\hat{p}_x-\\frac{B}{2}\\hat{y}\\right)\\pmb{e}^y\\\
right).$$
```

On the other hand,

```wl
$$\\frac{1}{B}\\left(\\hat{\\pmb{p}}+\\hat{\\pmb{A}}\\right)\\times \
\\pmb{e}^z$$
$$=\\frac{1}{B}\\left(\\left(\\hat{p}_x+\\hat{A}_x\\right)\\pmb{e}^x+\
\\left(\\hat{p}_y+\\hat{A}_y\\right)\\pmb{e}^y\\right)\\times \
\\pmb{e}^z$$
$$=\\frac{1}{B}\\left(\\left(\\hat{p}_x-\\frac{B}{2}\\hat{y}\\right)\\\
pmb{e}^x\\times \
\\pmb{e}^z+\\left(\\hat{p}_y+\\frac{B}{2}\\hat{x}\\right)\\pmb{e}^y\\\
times \\pmb{e}^z\\right)$$
$$=\\frac{1}{B}\\left(-\\left(\\hat{p}_x-\\frac{B}{2}\\hat{y}\\right)\
\\pmb{e}^y+\\left(\\hat{p}_y+\\frac{B}{2}\\hat{x}\\right)\\pmb{e}^x\\\
right).$$
```

Comparing the results, we conclude that

```wl
$$\\hat{\\pmb{\\xi \
}}=\\frac{1}{B}\\left(\\hat{\\pmb{p}}+\\hat{\\pmb{A}}\\right)\\times \
\\pmb{e}^z.$$
```

or, in terms of components

```wl
$$\\hat{\\xi }_x=\\hat{x}+\\frac{1}{B}\\hat{\\pi \
}_y=\\frac{1}{B}\\left(\\hat{p}_y+\\hat{A}_y\\right),\\\\
\\hat{\\xi }_y=\\hat{y}-\\frac{1}{B}\\hat{\\pi \
}_x=-\\frac{1}{B}\\left(\\hat{p}_x+\\hat{A}_x\\right).$$
```

* They satisfy the following commutation relation

```wl
$$\\left[\\hat{\\xi }_x,\\hat{\\xi }_y\\right]=\\frac{1}{i B}.$$
```

Prove Eq. (XXX).

```wl
$$\\left[\\hat{\\xi }_x,\\hat{\\xi \
}_y\\right]=\\left[\\hat{x}+\\frac{1}{B}\\hat{\\pi \
}_y,\\hat{y}-\\frac{1}{B}\\hat{\\pi }_x\\right]$$
$$=\\left[\\hat{x},\\hat{y}\\right]+\\frac{1}{B}\\left[\\hat{\\pi \
}_y,\\hat{y}\\right]-\\frac{1}{B}\\left[\\hat{x},\\hat{\\pi \
}_x\\right]-\\frac{1}{B^2}\\left[\\hat{\\pi
}_y,\\hat{\\pi }_x\\right]$$
$$=0-\\frac{1}{B}\\left[\\hat{y},\\hat{\\pi \
}_y\\right]-\\frac{1}{B}\\left[\\hat{x},\\hat{\\pi \
}_x\\right]+\\frac{1}{B^2}\\left[\\hat{\\pi }_x,\\hat{\\pi \
}_y\\right]$$
$$=-\\frac{i}{B}-\\frac{i}{B}+\\frac{1}{B^2}(i B),\\\\
=\\frac{1}{i B}.$$
```

* Guiding center and kinetic momentum operators commute.

```wl
$$\\left[\\hat{\\xi }_i,\\hat{\\pi }_j\\right]=0\\text{      \
}(\\text{for} i,j=x,y).$$
```

Prove Eq. (XXX).

Check the commutation relations one by one:

```wl
$$\\left[\\hat{\\xi }_x,\\hat{\\pi \
}_x\\right]=\\left[\\hat{x}+\\frac{1}{B}\\hat{\\pi }_y,\\hat{\\pi }_x\
\\right]$$
$$=\\left[\\hat{x},\\hat{\\pi \
}_x\\right]+\\frac{1}{B}\\left[\\hat{\\pi }_y,\\hat{\\pi \
}_x\\right]$$
$$=i+\\frac{1}{B}(-i B)=0.$$

$$\\left[\\hat{\\xi }_y,\\hat{\\pi \
}_y\\right]=\\left[\\hat{y}-\\frac{1}{B}\\hat{\\pi }_x,\\hat{\\pi }_y\
\\right]$$
$$=\\left[\\hat{y},\\hat{\\pi \
}_y\\right]-\\frac{1}{B}\\left[\\hat{\\pi }_x,\\hat{\\pi \
}_y\\right]$$
$$=i-\\frac{1}{B}(i B)=0.$$

$$\\left[\\hat{\\xi }_x,\\hat{\\pi \
}_y\\right]=\\left[\\hat{x}+\\frac{1}{B}\\hat{\\pi }_y,\\hat{\\pi }_y\
\\right]$$
$$=\\left[\\hat{x},\\hat{\\pi \
}_y\\right]+\\frac{1}{B}\\left[\\hat{\\pi }_y,\\hat{\\pi \
}_y\\right]$$
$$=0+0=0.$$

$$\\left[\\hat{\\xi }_y,\\hat{\\pi \
}_x\\right]=\\left[\\hat{y}-\\frac{1}{B}\\hat{\\pi }_x,\\hat{\\pi }_x\
\\right]$$
$$=\\left[\\hat{y},\\hat{\\pi \
}_x\\right]-\\frac{1}{B}\\left[\\hat{\\pi }_x,\\hat{\\pi \
}_x\\right]$$
$$=0+0=0.$$
```

Therefore,

```wl
$$\\left[\\hat{\\xi }_x,\\hat{\\pi }_x\\right]=\\left[\\hat{\\xi }_y,\
\\hat{\\pi }_y\\right]=\\left[\\hat{\\xi }_x,\\hat{\\pi \
}_y\\right]=\\left[\\hat{\\xi }_y,\\hat{\\pi
}_x\\right]=0.$$
```

#### Annihilation and Creation Operators

Define two sets of annihilation and creation operators.

* **Cyclotron annihilation and creation** operators:

```wl
$$\\hat{a}=\\frac{1}{\\sqrt{2B}}\\left(\\hat{\\pi }_x+i \\hat{\\pi \
}_y\\right), \\hat{a}^{\\dagger \
}=\\frac{1}{\\sqrt{2B}}\\left(\\hat{\\pi }_x-i \\hat{\\pi \
}_y\\right),$$
```

such that

```wl
$$\\hat{a}^{\\dagger }\\hat{a}+\\frac{1}{2}=\\frac{1}{2B}\\hat{\\pmb{\
\\pi }}^2=\\frac{1}{2B}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}\
-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right)^2.$$
```

Verify Eq. (XXX).

```wl
$$\\hat{a}^{\\dagger \
}\\hat{a}+\\frac{1}{2}=\\frac{1}{2B}\\left(\\hat{\\pi }_x-i \
\\hat{\\pi }_y\\right)\\left(\\hat{\\pi }_x+i \\hat{\\pi }_y\\right)+\
\\frac{1}{2}$$
$$=\\frac{1}{2B}\\left(\\hat{\\pi }_x^2+\\hat{\\pi }_y^2-i \\hat{\\pi \
}_y\\hat{\\pi }_x+i \\hat{\\pi }_x\\hat{\\pi }_y\\right)+\\frac{1}{2}$$
$$=\\frac{1}{2B}\\left(\\hat{\\pi }_x^2+\\hat{\\pi \
}_y^2\\right)+\\frac{1}{2B}i \\left[\\hat{\\pi }_x,\\hat{\\pi \
}_y\\right]+\\frac{1}{2}$$
$$=\\frac{1}{2B}\\hat{\\pmb{\\pi }}^2+\\frac{1}{2B}i (i \
B)+\\frac{1}{2}$$
$$=\\frac{1}{2B}\\hat{\\pmb{\\pi }}^2-\\frac{1}{2}+\\frac{1}{2}$$
$$=\\frac{1}{2B}\\hat{\\pmb{\\pi }}^2.$$
```

By Eq. (XXX), 
\\!\\(\\*OverscriptBox[
StyleBox[\"\\[Pi]\",
FontWeight->\"Bold\"], \\(^\\)]\\) = 
\\!\\(\\*OverscriptBox[
StyleBox[\"p\",
FontWeight->\"Bold\"], 
StyleBox[\"^\",
FontWeight->\"Plain\"]]\\) - 
\\!\\(\\*OverscriptBox[
StyleBox[\"A\",
FontWeight->\"Bold\"], 
StyleBox[\"^\",
FontWeight->\"Plain\"]]\\),

```wl
$$\\hat{a}^{\\dagger }\\hat{a}+\\frac{1}{2}=\\frac{1}{2B}\\hat{\\pmb{\
\\pi }}^2=\\frac{1}{2B}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}\
-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right)^2.$$
```

* **Guiding center annihilation and creation** operators:

```wl
$$\\hat{b}=\\sqrt{\\frac{B}{2}}\\left(\\hat{\\xi }_x-i \\hat{\\xi }_y\
\\right), \\hat{b}^{\\dagger }=\\sqrt{\\frac{B}{2}}\\left(\\hat{\\xi \
}_x+i \\hat{\\xi }_y\\right),$$
```

such that

```wl
$$\\hat{b}^{\\dagger \
}\\hat{b}+\\frac{1}{2}=\\frac{B}{2}\\hat{\\pmb{\\xi \
}}^2=\\frac{1}{2B}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}+\\\
pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right)^2.$$
```

Verify Eq. (XXX).

```wl
$$\\hat{b}^{\\dagger }\\hat{b}+\\frac{1}{2}=\\frac{B}{2}\\left(\\hat{\
\\xi }_x+i \\hat{\\xi }_y\\right)\\left(\\hat{\\xi }_x-i \\hat{\\xi \
}_y\\right)+\\frac{1}{2}$$
$$=\\frac{B}{2}\\left(\\hat{\\xi }_x^2+\\hat{\\xi }_y^2+i \\hat{\\xi \
}_y\\hat{\\xi }_x-i \\hat{\\xi }_x\\hat{\\xi }_y\\right)+\\frac{1}{2}$$
$$=\\frac{B}{2}\\left(\\hat{\\xi }_x^2+\\hat{\\xi \
}_y^2\\right)-\\frac{B}{2}i \\left[\\hat{\\xi }_x,\\hat{\\xi \
}_y\\right]+\\frac{1}{2}$$
$$=\\frac{B}{2}\\hat{\\pmb{\\xi }}^2-\\frac{B}{2}\\frac{i}{i \
B}+\\frac{1}{2}$$
$$=\\frac{B}{2}\\hat{\\pmb{\\xi }}^2-\\frac{1}{2}+\\frac{1}{2}$$
$$=\\frac{B}{2}\\hat{\\pmb{\\xi }}^2.$$
```

By Eq. (XXX), 
\\!\\(\\*OverscriptBox[
StyleBox[\"\\[Xi]\",
FontWeight->\"Bold\"], \\(^\\)]\\) = 1/B (
\\!\\(\\*OverscriptBox[
StyleBox[\"p\",
FontWeight->\"Bold\"], \\(^\\)]\\) + 
\\!\\(\\*OverscriptBox[
StyleBox[\"A\",
FontWeight->\"Bold\"], \\(^\\)]\\))*e^z,

```wl
$$\\hat{b}^{\\dagger \
}\\hat{b}+\\frac{1}{2}=\\frac{B}{2}\\hat{\\pmb{\\xi }}^2$$
$$=\\frac{B}{2}\\frac{1}{B^2}\\left(\\left(\\hat{\\pmb{p}}+\\hat{\\\
pmb{A}}\\right)\\times \\pmb{e}^z\\right)^2$$
$$=\\frac{1}{2B}\\left(\\hat{\\pmb{p}}+\\hat{\\pmb{A}}\\right)^2.$$
```

They satisfy the following commutation relations

```wl
$$\\left[\\hat{a},\\hat{a}^{\\dagger }\\right]=1, \
\\left[\\hat{b},\\hat{b}^{\\dagger }\\right]=1,\\\\
\\left[\\hat{a},\\hat{b}\\right]=\\left[\\hat{a},\\hat{b}^{\\dagger }\
\\right]=\\left[\\hat{a}^{\\dagger \
},\\hat{b}\\right]=\\left[\\hat{a}^{\\dagger },\\hat{b}^{\\dagger
}\\right]=0.$$
```

Prove Eq. (XXX).

First check the commutators $$\\left[\\hat{a},\\hat{a}^{\\dagger \
}\\right]$$ and $$\\left[\\hat{b},\\hat{b}^{\\dagger }\\right]$$.

```wl
$$\\left[\\hat{a},\\hat{a}^{\\dagger \
}\\right]=\\frac{1}{2B}\\left[\\hat{\\pi }_x+i \\hat{\\pi \
}_y,\\hat{\\pi }_x-i \\hat{\\pi }_y\\right]$$
$$=\\frac{1}{2B}\\left(\\left[\\hat{\\pi }_x,\\hat{\\pi }_x\\right]+i \
\\left[\\hat{\\pi }_y,\\hat{\\pi }_x\\right]-i \\left[\\hat{\\pi }_x,\
\\hat{\\pi }_y\\right]+\\left[\\hat{\\pi
}_y,\\hat{\\pi }_y\\right]\\right)$$
$$=\\frac{1}{2B}\\left(0-i \\left[\\hat{\\pi }_x,\\hat{\\pi \
}_y\\right]-i \\left[\\hat{\\pi }_x,\\hat{\\pi \
}_y\\right]+0\\right)$$
$$=\\frac{1}{2B}(-2i)(i B)$$
$$=1.$$

$$\\left[\\hat{b},\\hat{b}^{\\dagger \
}\\right]=\\frac{B}{2}\\left[\\hat{\\xi }_x-i \\hat{\\xi \
}_y,\\hat{\\xi }_x+i \\hat{\\xi }_y\\right]$$
$$=\\frac{B}{2}\\left(\\left[\\hat{\\xi }_x,\\hat{\\xi }_x\\right]-i \
\\left[\\hat{\\xi }_y,\\hat{\\xi }_x\\right]+i \\left[\\hat{\\xi }_x,\
\\hat{\\xi }_y\\right]+\\left[\\hat{\\xi
}_y,\\hat{\\xi }_y\\right]\\right)$$
$$=\\frac{B}{2}\\left(0+i \\left[\\hat{\\xi }_x,\\hat{\\xi \
}_y\\right]+i \\left[\\hat{\\xi }_x,\\hat{\\xi \
}_y\\right]+0\\right)$$
$$=\\frac{B}{2}(2i)\\frac{1}{i B}$$
$$=1.$$
```

Then by Eq. (XXX), [Subscript[
\\!\\(\\*OverscriptBox[\\(\\[Xi]\\), \\(^\\)]\\), i], Subscript[
\\!\\(\\*OverscriptBox[\\(\\[Pi]\\), \\(^\\)]\\), j]] = 0, any linear \
combination of Subscript[
\\!\\(\\*OverscriptBox[\\(\\[Pi]\\), \\(^\\)]\\), j] (such as 
\\!\\(\\*OverscriptBox[\\( ... ger[
\\!\\(\\*OverscriptBox[\\(a\\), \\(^\\)]\\)]) must commute with \
linear combination of Subscript[
\\!\\(\\*OverscriptBox[\\(\\[Xi]\\), \\(^\\)]\\), i] (such as 
\\!\\(\\*OverscriptBox[\\(b\\), \\(^\\)]\\) and SuperDagger[
\\!\\(\\*OverscriptBox[\\(b\\), \\(^\\)]\\)]), so we have

```wl
$$\\left[\\hat{a},\\hat{b}\\right]=\\left[\\hat{a},\\hat{b}^{\\dagger \
}\\right]=\\left[\\hat{a}^{\\dagger \
},\\hat{b}\\right]=\\left[\\hat{a}^{\\dagger },\\hat{b}^{\\dagger
}\\right]=0.$$
```

* Implication: $$\\hat{a}$$ and $$\\hat{b}$$ are *annihilation \
operators* for two *independent* **harmonic oscillator** degrees of \
freedom.

* $$\\hat{a}^{\\dagger }\\hat{a}$$ and $$\\hat{b}^{\\dagger \
}\\hat{b}$$ are commuting **number operators**, and can be \
diagonalized *simultaneously*. Their eigenvalues correspond to two \
*separate* sets of **quantum numbers**, denoted as $$n$$ and $$m$$ \
respectively:

```wl
$$\\hat{a}^{\\dagger }\\hat{a}| n,m\\rangle =n| n,m\\rangle ,\\\\
\\hat{b}^{\\dagger }\\hat{b}| n,m\\rangle =m| n,m\\rangle ,$$
```

$$n,m=0,1,2,\\ldots \\in \\mathbb{N}$$.

#### Landau Levels

The system has two important physical observables:

* Hamiltonian: using Eq. (XXX), Eq. (XXX) can be written as

```wl
$$\\hat{H}=\\frac{1}{2}\\hat{\\pmb{\\pi }}^2=B \
\\left(\\hat{a}^{\\dagger }\\hat{a}+\\frac{1}{2}\\right).$$
```

* **Angular momentum** :

```wl
$$\\hat{L}_z=\\left(\\hat{\\pmb{x}}\\times \
\\hat{\\pmb{p}}\\right)\\cdot \\pmb{e}^z=\\hat{b}^{\\dagger \
}\\hat{b}-\\hat{a}^{\\dagger }\\hat{a}.$$
```

Verify Eq. (XXX) under symmetric gauge.

According to Eq. (XXX) and Eq. (XXX),

```wl
$$\\hat{b}^{\\dagger }\\hat{b}-\\hat{a}^{\\dagger \
}\\hat{a}=\\frac{1}{2B}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}\
+\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\right)^2-\\frac{1}{2B}\\\
left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}-\\pmb{\\overset{{}^{\\\
wedge}}{\\pmb{A}}}\\right)^2$$
$$=\\frac{1}{2B}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}^2+\\\
pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}\\cdot \
\\hat{\\pmb{A}}+\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\cdot
\\hat{\\pmb{p}}+\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}^2\\right)-\\\
frac{1}{2B}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}^2-\\pmb{\\\
overset{{}^{\\wedge}}{\\pmb{p}}}\\cdot
\\hat{\\pmb{A}}-\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\cdot \\hat{\
\\pmb{p}}+\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}^2\\right)$$
$$=\\frac{1}{B}\\left(\\pmb{\\overset{{}^{\\wedge}}{\\pmb{p}}}\\cdot \
\\hat{\\pmb{A}}+\\pmb{\\overset{{}^{\\wedge}}{\\pmb{A}}}\\cdot \\hat{\
\\pmb{p}}\\right)$$
$$=\\frac{1}{B}\\left(\\hat{p}_x\\hat{A}_x+\\hat{p}_y\\hat{A}_y+\\hat{\
A}_x\\hat{p}_x+\\hat{A}_y\\hat{p}_y\\right)$$
$$=\\frac{1}{B}\\left(\\hat{p}_x\\left(-\\frac{B}{2}\\hat{y}\\right)+\
\\hat{p}_y\\left(\\frac{B}{2}\\hat{x}\\right)+\\left(-\\frac{B}{2}\\\
hat{y}\\right)\\hat{p}_x+\\left(\\frac{B}{2}\\hat{x}\\right)\\hat{p}_\
y\\right)$$
$$=\\frac{1}{2}\\left(-\\hat{p}_x\\hat{y}+\\hat{p}_y\\hat{x}-\\hat{y}\
\\hat{p}_x+\\hat{x}\\hat{p}_y\\right)$$
$$=\\frac{1}{2}\\left(-\\hat{y}\\hat{p}_x+\\hat{x}\\hat{p}_y-\\hat{y}\
\\hat{p}_x+\\hat{x}\\hat{p}_y\\right)$$
$$=\\hat{x}\\hat{p}_y-\\hat{y}\\hat{p}_x$$
$$=\\left(\\hat{\\pmb{x}}\\times \\hat{\\pmb{p}}\\right)\\cdot \
\\pmb{e}^z$$
$$=\\hat{L}_z.$$
```

Obviously, $$\\left[\\hat{H},\\hat{L}_z\\right]=0$$, i.e. \
$$\\hat{H}$$ and $$\\hat{L}_z$$ can be simultaneously diagonalized.

* Their common eigenstates are $$| n,m\\rangle$$ :

```wl
$$\\hat{H}| n,m\\rangle =B \\left(n+\\frac{1}{2}\\right)| n,m\\rangle \
,\\\\
\\hat{L}_z| n,m\\rangle =(m-n)| n,m\\rangle ,$$
```

which are labeled by two quantum numbers:

	* $$n$$: **Landau level** index (energy level index),

	* $$m$$: **angular momentum** index (degeneracy within a Landau \
level).

* The energy levels are quantized

```wl
$$E_n=B \\left(n+\\frac{1}{2}\\right),$$
```

with $$n=0,1,2,\\ldots \\in \\mathbb{N}$$.

	* After restoring the energy unit,

```wl
$$E_n=\\frac{\\hbar  q B}{m} \\left(n+\\frac{1}{2}\\right)=\\hbar  \
\\omega _c\\left(n+\\frac{1}{2}\\right).$$
```

where $$\\omega _c=q B/m$$ is the **cyclotron frequency**.

	* Each level is called a **Landau level**. The $$n=0$$ level is \
called the **lowest Landau level** (LLL).

* The angular momentum is also quantized. After restoring the unit,

```wl
$$L_{z,nm}=\\hbar  (m-n).$$
```

Eigenstates $$| n,m\\rangle$$ arranged by energy v.s. angular momentum.

```wl
In[575]:=
Graphics[Table[Point[{m - n, n + 1 / 2}], {n, 0, 5}, {m, 0, n + 5}], \
PlotRange -> {{ - 5.5, 5.5}, {0, 6}}, GridLines -> {Range[ - 5, 5], \
Range[0, 5] + 1 / 2}, Frame -> True, FrameLabel -> {L        /\[HBar]
 z, n \[InvisibleComma] m, E /\[HBar] \[Omega]
 n    c}, ImageSize -> 180]

Out[575]=
\\!\\(\\*GraphicsBox[{{PointBox[NCache[{0, 1/2}, {0, 0.5}]], \
PointBox[NCache[{1, 1/2}, {1, 0.5}]], 
   PointBox[NCache[{2, 1/2}, {2, 0.5}]], PointBox[NCache[{3, 1/2}, \
{3, 0.5}]], 
   PointBox[NCache[{4, 1/2}, {4, 0.5}]], PointBox[NCache[{5, 1/2}, \
{5, 0. ... aditionalForm]}, 
 GridLines -> NCache[{{-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}, {1/2, \
3/2, 5/2, 7/2, 9/2, 11/2}}, 
   {{-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}, {0.5, 1.5, 2.5, 3.5, 4.5, \
5.5}}], ImageSize -> 180, 
 PlotRange -> {{-5.5, 5.5}, {0, 6}}]\\)
```

* **Landau level degeneracy** :

	* In an *infinite* system, each Landau level is *infinitely* \
degenerated.

		* Argument: The quantum number $$m=0,1,2,\\ldots \\in \\mathbb{N}$$ \
is unbounded. \[Implies] Infinitely many orthogonal states $$| \
n,m\\rangle$$ within the same energy level $$n$$.

	* In a realistic system of *finite* size, the Landau level \
degeneracy becomes *finite*, and is determined by the *total magnetic \
flux* measured in units of the *flux quantum*.

		* Consider electrons confined within a disk of radius $$R$$. \
\[Implies] The *guiding center* radius \[Xi] must satisfy $$\\xi \
\\lesssim R$$.

		* This puts a constraint on the operator

```wl
$$\\hat{b}^{\\dagger \
}\\hat{b}+\\frac{1}{2}=\\frac{B}{2}\\hat{\\pmb{\\xi }}^2\\lesssim \
\\frac{B R^2}{2},$$
```

in terms of its eigenvalues. \[Implies] $$m\\lesssim B \
\\left.R^2\\right/2$$, restoring the physical units:

```wl
$$m\\lesssim \\frac{e B R^2}{2\\hbar }.$$
```

		* A **flux quantum** is the amount of magnetic flux $$\\phi _0$$ \
that induces a $$2\\pi$$ **Berry phase** for an electron braiding \
around it.

```wl
$$\\text{phase}=\\frac{\\text{action}}{\\hbar }=\\frac{e \\phi \
_0}{\\hbar }=2\\pi ,$$
```

meaning that

```wl
$$\\phi _0=\\frac{h}{e}.$$
```

		* Then Eq. (XXX) can be written as

```wl
$$m\\lesssim \\frac{\\phi _B}{\\phi _0},$$
```

where $$\\phi _B=\\pi  R^2 B$$ is the **total magnetic flux** through \
the disk.

Thus the Landau level degeneracy is set by $$\\phi _B/\\phi _0$$ \
\[LongDash] the conclusion generalizes to any shape of the system.

#### Complex Coordinate

Instead of using $$\\pmb{x}=(x,y)$$ to coordinate the position of the \
particle, it is more convenient to introduce:

* the **complex coordinate**

```wl
$$z=\\sqrt{\\frac{B}{2}}(x+i y), \\bar{z}=\\sqrt{\\frac{B}{2}}(x-i \
y),$$
```

* and the **complex derivative**

```wl
$$\\partial _z=\\frac{1}{\\sqrt{2B}}\\left(\\partial _x-i\\partial _y\
\\right), \\partial _{\\bar{z}}=\\frac{1}{\\sqrt{2B}}\\left(\\partial \
_x+i\\partial _y\\right).$$
```

Derive Eq. (XXX) from Eq. (XXX).

Eq. (XXX) implies

```wl
$$x=\\frac{z+\\bar{z}}{\\sqrt{2B}}, \
y=\\frac{z-\\bar{z}}{i\\sqrt{2B}}.$$
```

Therefore,

```wl
$$\\partial _z=\\frac{\\partial x}{\\partial z}\\frac{\\partial \
}{\\partial x}+\\frac{\\partial y}{\\partial z}\\frac{\\partial \
}{\\partial y}$$


$$=\\frac{1}{\\sqrt{2B}}\\partial _x+\\frac{1}{i\\sqrt{2B}}\\partial \
_y$$


$$=\\frac{1}{\\sqrt{2B}}\\left(\\partial _x-i\\partial _y\\right).$$

$$\\partial _{\\bar{z}}=\\frac{\\partial x}{\\partial \
\\bar{z}}\\frac{\\partial }{\\partial x}+\\frac{\\partial \
y}{\\partial \\bar{z}}\\frac{\\partial }{\\partial
y}$$


$$=\\frac{1}{\\sqrt{2B}}\\partial _x+\\frac{-1}{i\\sqrt{2B}}\\partial \
_y$$


$$=\\frac{1}{\\sqrt{2B}}\\left(\\partial _x+i\\partial _y\\right).$$
```

Using the complex notation, the creation and annihilation operators \
can be represented as

```wl
$$\\hat{a}=-i\\, \\left(\\frac{1}{2}z+\\partial \
_{\\bar{z}}\\right),\\hat{a}^{\\dagger }=i\\, \
\\left(\\frac{1}{2}\\bar{z}-\\partial _z\\right);$$
$$\\hat{b}=\\frac{1}{2}\\bar{z}+\\partial _z,\\hat{b}^{\\dagger \
}=\\frac{1}{2}z-\\partial _{\\bar{z}}.$$
```

Verify Eq. (XXX).

First verify the annihilation operators

```wl
$$\\hat{a}=\\frac{1}{\\sqrt{2B}}\\left(\\hat{\\pi }_x+i \\hat{\\pi \
}_y\\right)$$
$$=\\frac{1}{\\sqrt{2B}}\\left(\\left(\\hat{p}_x-\\hat{A}_x\\right)+i \
\\left(\\hat{p}_y-\\hat{A}_y\\right)\\right)$$
$$=\\frac{1}{\\sqrt{2B}}\\left(\\left(-i \\partial \
_x+\\frac{B}{2}y\\right)+i \\left(-i\\partial \
_y-\\frac{B}{2}x\\right)\\right)$$
$$=-i \\frac{1}{2}\\sqrt{\\frac{B}{2}}(x+i \
y)-i\\frac{1}{\\sqrt{2B}}\\left(\\partial _x+i \\partial _y\\right)$$
$$=-i\\, \\left(\\frac{1}{2}z+\\partial _{\\bar{z}}\\right).$$

$$\\hat{b}=\\sqrt{\\frac{B}{2}}\\left(\\hat{\\xi }_x-i \\hat{\\xi }_y\
\\right)$$
$$=\\sqrt{\\frac{B}{2}}\\frac{1}{B}\\left(\\left(\\hat{p}_y+\\hat{A}_\
y\\right)+i \\left(\\hat{p}_x+\\hat{A}_x\\right)\\right)$$
$$=\\frac{1}{\\sqrt{2B}}\\left(\\left(-i\\partial \
_y+\\frac{B}{2}x\\right)+i \\left(-i\\partial \
_x-\\frac{B}{2}y\\right)\\right)$$
$$=\\frac{1}{2}\\sqrt{\\frac{B}{2}}(x-i \
y)+\\frac{1}{\\sqrt{2B}}\\left(\\partial _x-i\\partial _y\\right)$$
$$=\\frac{1}{2}\\bar{z}+\\partial _z.$$
```

Then the creation operators can be obtained by Hermitian conjugate

```wl
$$\\hat{a}^{\\dagger }=\\left(-i\\, \\left(\\frac{1}{2}z+\\partial _{\
\\bar{z}}\\right)\\right){}^{\\dagger }$$
$$=i\\, \\left(\\frac{1}{2}\\bar{z}-\\partial _z\\right).$$

$$\\hat{b}^{\\dagger }=\\left(\\frac{1}{2}\\bar{z}+\\partial \
_z\\right){}^{\\dagger }$$
$$=\\frac{1}{2}z-\\partial _{\\bar{z}}.$$
```

#### Wave Functions

$$| 0,0\\rangle$$ is the **vacuum state** for both $$\\hat{a}$$ and \
$$\\hat{b}$$ bosons, defined by the condition

```wl
$$\\hat{a}| 0,0\\rangle =\\hat{b}| 0,0\\rangle =0.$$
```

so the vacuum state *wave function* $$\\psi \
_{0,0}\\left(z,\\bar{z}\\right)$$ should satisfy

```wl
$$\\left(\\frac{1}{2}z+\\partial _{\\bar{z}}\\right)\\psi \
_{0,0}\\left(z,\\bar{z}\\right)=\\left(\\frac{1}{2}\\bar{z}+\\partial \
_z\\right)\\psi _{0,0}\\left(z,\\bar{z}\\right)=0.$$
```

* Consider the ansatz

```wl
$$\\psi _{0,0}\\left(z,\\bar{z}\\right)=f\\left(z,\\bar{z}\\right)e^{-\
\\bar{z}z/2},$$
```

Eq. (XXX) implies

```wl
$$\\partial _zf\\left(z,\\bar{z}\\right)=\\partial \
_{\\bar{z}}f\\left(z,\\bar{z}\\right)=0,$$
```

Derive Eq. (XXX).

Substitute Eq. (XXX) into Eq. (XXX), we have

```wl
$$\\left(\\frac{1}{2}z+\\partial _{\\bar{z}}\\right)\\psi \
_{0,0}\\left(z,\\bar{z}\\right)$$
$$=\\left(\\frac{1}{2}z+\\partial \
_{\\bar{z}}\\right)\\left(f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}\\\
right)$$
$$=\\frac{1}{2}z f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}+\\partial \
_{\\bar{z}}\\left(f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}\\right)$$\

$$=\\frac{1}{2}z f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}+\\partial \
_{\\bar{z}}f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}+f\\left(z,\\bar{\
z}\\right)\\partial
_{\\bar{z}}e^{-\\bar{z}z/2}$$
$$=\\frac{1}{2}z f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}+\\partial \
_{\\bar{z}}f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}-\\frac{1}{2}z f\
\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}$$
$$=\\partial _{\\bar{z}}f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}=0,$$
```

and

```wl
$$\\left(\\frac{1}{2}\\bar{z}+\\partial _z\\right)\\psi \
_{0,0}\\left(z,\\bar{z}\\right)$$
$$=\\left(\\frac{1}{2}\\bar{z}+\\partial \
_z\\right)\\left(f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}\\right)$$
$$=\\frac{1}{2}\\bar{z} \
f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}+\\partial \
_z\\left(f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}\\right)$$
$$=\\frac{1}{2}\\bar{z} \
f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}+\\partial \
_zf\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}+f\\left(z,\\bar{z}\\\
right)\\partial _ze^{-\\bar{z}z/2}$$
$$=\\frac{1}{2}\\bar{z} \
f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}+\\partial \
_zf\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}-\\frac{1}{2}\\bar{z} \
f\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}$$
$$=\\partial _zf\\left(z,\\bar{z}\\right)e^{-\\bar{z}z/2}=0.$$
```

Given that $$e^{-\\bar{z}z/2}>0$$, we must have

```wl
$$\\partial _zf\\left(z,\\bar{z}\\right)=\\partial \
_{\\bar{z}}f\\left(z,\\bar{z}\\right)=0.$$
```

meaning that $$f\\left(z,\\bar{z}\\right)$$ must be *independent* of \
both $$z$$ and $$\\bar{z}$$, i.e. it is a constant function, i.e.

```wl
$$f\\left(z,\\bar{z}\\right)=\\text{const}.$$
```

* Therefore, the vacuum state wave function reads

```wl
$$\\psi _{0,0}\\left(z,\\bar{z}\\right)=\\frac{1}{\\sqrt{\\pi \
}}e^{-\\bar{z}z/2},$$
```

which is normalized to ensure $$\\int dzd\\bar{z}\\left| \\psi _{0,0}\
\\left(z,\\bar{z}\\right)\\right| {}^2=1$$.

Any other state $$| n,m\\rangle$$ can be raised from the vacuum state \
$$| 0,0\\rangle$$ by applying creation operators

```wl
$$| n,m\\rangle =\\frac{1}{\\sqrt{n!m!}}\\left(\\hat{a}^{\\dagger \
}\\right)^n\\left(\\hat{b}^{\\dagger }\\right)^m| 0,0\\rangle ,$$
```

for $$n,m=0,1,2,\\ldots$$.

* **Lowest Landau level** (LLL): The wave functions with $$n=0$$ are

```wl
$$\\psi _{0,m}\\left(z,\\bar{z}\\right)=\\frac{1}{\\sqrt{\\pi  \
m!}}z^me^{-\\bar{z}z/2}.$$
```

Derive Eq. (XXX).

Note that

```wl
$$\\left(\\frac{1}{2}z-\\partial \
_{\\bar{z}}\\right)e^{-\\bar{z}z/2}$$
$$=\\frac{1}{2}z e^{-\\bar{z}z/2}-\\partial \
_{\\bar{z}}e^{-\\bar{z}z/2}$$
$$=\\frac{1}{2}z \
e^{-\\bar{z}z/2}-\\left(-\\frac{z}{2}\\right)e^{-\\bar{z}z/2}$$
$$=z e^{-\\bar{z}z/2},$$
```

and $$\\left(\\frac{1}{2}z-\\partial _{\\bar{z}}\\right)$$ commute \
with $$z$$, thus

```wl
$$\\left(\\frac{1}{2}z-\\partial \
_{\\bar{z}}\\right){}^me^{-\\bar{z}z/2}$$
$$=\\left(\\frac{1}{2}z-\\partial _{\\bar{z}}\\right){}^{m-1}z \
e^{-\\bar{z}z/2}$$
$$=z \\left(\\frac{1}{2}z-\\partial \
_{\\bar{z}}\\right){}^{m-1}e^{-\\bar{z}z/2}$$
$$=z \\left(\\frac{1}{2}z-\\partial _{\\bar{z}}\\right){}^{m-2}z e^{-\
\\bar{z}z/2}$$
$$=z^2 \\left(\\frac{1}{2}z-\\partial _{\\bar{z}}\\right){}^{m-2} \
e^{-\\bar{z}z/2}$$
$$=\\ldots$$
$$=z^m e^{-\\bar{z}z/2}.$$
```

Therefore,

```wl
$$\\psi _{0,m}\\left(z,\\bar{z}\\right)=\\frac{1}{\\sqrt{m!}}\\left(\\\
hat{b}^{\\dagger }\\right)^m\\psi _{0,0}\\left(z,\\bar{z}\\right)$$
$$=\\frac{1}{\\sqrt{\\pi  m!}}\\left(\\frac{1}{2}z-\\partial \
_{\\bar{z}}\\right){}^me^{-\\bar{z}z/2}$$
$$=\\frac{1}{\\sqrt{\\pi  m!}}z^me^{-\\bar{z}z/2}.$$
```

The wave functions has circular symmetry, taking the **ring shape**.

```wl
In[140]:=
DynamicModule[{cfun}, 
	cfun = Darker[Blend[{RGBColor[0.91, 0.36, 0.46], RGBColor[1., 0.59, \
0.4], RGBColor[0.97, 0.76, 0], RGBColor[0.72, 0.8, 0.46], \
RGBColor[0.25, 0.73, 0.3], RGBColor[0, 0.76, 0.93], RGBColor[0.43, \
0.58, 0.99], RGBColor[0.72, 0.53, 0.995], RGBColor[0.91, 0.36, \
0.46]}, Mod[#2 + 1 / 2, 1]], 1 - #1]&;
	Manipulate[
	ComplexPlot[Evaluate[Nest[(Conjugate[z] # - D[#, z] /. Conjugate'[z] \
-> 0)&, z ^ m, n] Exp[ - Abs[z] ^ 2 / 2] / Sqrt[\[Pi] n! m!]], {z,  - \
5 - 5I, 5 + 5I}, Epilog -> {White, Dashed, Opacity[0.5], If[m + n > \
0, Circle[{0, 0}, Sqrt[(n + m)]], Nothing]}, ColorFunction -> \
{cfun[#7, #8]&, None}, FrameLabel -> {Rez = Sqrt[B/2] \
\[VeryThinSpace]x, Imz = Sqrt[B/2] \[VeryThinSpace]y}, PlotLabel -> \
StringTemplate[\[LeftBracketingBar] `1`, `2` \[RightAngleBracket]][n, \
m], ImageSize -> 180], {{n, 0, Style[\[VeryThinSpace]n :, \
\"InlineFormula\"]}, Range[0, 5], ControlType -> SetterBar}, {{m, 6, \
Style[\[VeryThinSpace]m :, \"InlineFormula\"]}, Range[0, 10], \
ControlType -> SetterBar}, Paneled -> False, SaveDefinitions -> True]]

Out[140]= DynamicModule[«3»]
```

	* Probability density

```wl
$$\\left| \\psi _{0,m}\\left(z,\\bar{z}\\right)\\right| \
{}^2=\\frac{1}{\\pi  m!}\\left(\\bar{z}z\\right)^me^{-\\bar{z}z},$$
```

which distributes around the radius $$| z| =\\sqrt{m}$$.

Estimate the radius $$| z|$$ that maximizes the probability.

The probability

```wl
$$p(| z| )=\\frac{1}{\\pi  m!}| z| ^{2m}e^{-| z| ^2}$$
```

is maximized when

```wl
$$\\frac{dp(| z| )}{d| z| }=\\frac{2}{\\pi  m!}| z| ^{2m-1}e^{-| z| \
^2}\\left(m-| z| ^2\\right)=0,$$

In[142]:= D[z ^ (2m)Exp[ - z ^ 2], z]//Simplify

Out[142]= 2 E^ - z^2 z^ - 1 + 2 m (m - z^2)
```

which is achieved at $$| z| =\\sqrt{m}$$.

	* **Semi-classical argument**: The factor $$z^m=\\sqrt{B/2}r^me^{i m \
\\theta }$$ implies that the particle accumulates $$2\\pi  m$$ *Berry \
phase* when travelling around a circle of *radius* $$r$$.

		* To ensure that the wave function is single-valued, $$m$$ must be \
an integer, i.e.

```wl
$$2\\pi  m\\in 2\\pi  \\mathbb{Z}\\Rightarrow m\\in \\mathbb{Z}.$$
```

		* This corresponds to a *canonical momentum* of

```wl
$$p=\\frac{2\\pi  m}{2\\pi  r}=\\frac{m}{r}.$$
```

		* States in the LLL should *minimize* the energy \
$$E=\\left.(\\pmb{p}-\\pmb{A})^2\\right/2$$, which can be achieved if

```wl
$$p=A=\\frac{\\pi  r^2 B}{2\\pi  r}=\\frac{r B}{2}.$$
```

		* Eq. (XXX) and Eq. (XXX) together sets the optimal radius

```wl
$$\\frac{m}{r}=p=\\frac{r B}{2}\\Rightarrow \
r=\\sqrt{\\frac{2m}{B}},$$
```

or, in terms of $$z$$ variable, $$| z|  =\\sqrt{B/2}r=\\sqrt{m}$$ \
(with $$m\\in \\mathbb{Z}$$).

	* Any linear combination of $$| 0,m\\rangle$$ is still a state in \
the LLL, which takes the general form of

```wl
$$\\sum _m c_m\\psi _{0,m}\\left(z,\\bar{z}\\right)=\\frac{1}{\\sqrt{\
\\pi  m!}}\\left(\\sum _m \
c_mz^m\\right)e^{-\\bar{z}z/2}=f(z)e^{-\\bar{z}z/2}.$$
```

Conclusion: LLL wavefunctions are **holomorphic functions** of  z , \
multiplied by a **Gaussian envelope**.

* More generally, for higher Landau levels, the wave functions

```wl
$$\\psi _{n,m}\\left(z,\\bar{z}\\right)=\\frac{1}{\\sqrt{\\pi  n!m!}}\
\\left(\\left(\\bar{z}-\\partial \
_z\\right){}^nz^m\\right)e^{-\\bar{z}z/2},$$
```

can be written in terms of *associated Laguerre polynomials*.

### Quantum Hall Effect

#### Filling Landau Levels

For a **single electron** confined to a *two-dimensional plane* under \
a *uniform perpendicular* magnetic field, the energy eigenvalues are \
quantized into **Landau levels** :

```wl
$$E_n=\\hbar  \\omega _c\\left(n+\\frac{1}{2}\\right)\\text{      \
}(n=0,1,2,\\ldots ).$$
```

* **Level spacing** (energy gap): $$\\hbar  \\omega _c$$, where \
$$\\omega _c=e B/m$$ is the *cyclotron frequency*.

* **Level degeneracy**: Given the total magnetic flux $$\\phi _B$$ \
through the plane, degeneracy is

```wl
$$N_{\\phi }\\text{:=}\\frac{\\phi _B}{\\phi _0}=\\frac{B A}{\\phi \
_0},$$
```

where

	* $$A$$ - total area of the system,

	* $$\\phi _0=h/e$$ - the *magnetic flux quantum*.

**Many-body system**: In real materials, there is not just one single \
electron, but **many electrons** interacting with each other \
\[LongDash] the problem become *many-body* in nature.

* The key feature of electrons is their **fermionic statistics**. 
\[Implies] **Pauli exclusion principle**: no two electrons can occupy \
the same quantum state.

* **Filling up energy levels**: Due to Pauli exclusion, electrons \
will fill up *available quantum states* starting from the lowest \
energy states.

* **Filling fraction **$$\\nu$$ is the (fractional) number of Landau \
levels that will be filled up,

```wl
$$\\nu =\\frac{N}{N_{\\phi }}=\\frac{n h}{e B}.$$
```

	* $$N$$ - *total number* of electron in the system,

	* $$n=N/A$$ - **electron density**, i.e. the number of electrons per \
area.

Conversely, Eq. (XXX) allows us to express n in terms of \\[Nu],

```wl
$$n=\\frac{\\nu  e}{h}B.$$
```

The phenomenology of integer quantum Hall effect is that the Hall \
conductivity Subscript[\\[Sigma], H] takes quantized values (recall \
Eq. (XXX))

```wl
$$\\sigma _H=\\frac{n e}{B}=\\frac{\\nu  e^2}{h},$$
```

at $$\\nu =1,2,3,\\ldots$$, i.e. when the **filling fraction** $$\\nu \
\\in \\mathbb{N}$$ is an integer, corresponding to the situation where

* the lowest $$\\nu$$ **Landau levels** are completely *filled*,

* and all higher levels are completely *empty*.

This leads to an **incompressible quantum state**: electrons cannot \
change states without a large energy cost (the Landau level spacing \
$$\\hbar  \\omega _c$$).

Message: The *quantized* Hall conductance originates from fully \
filling *discrete* Landau levels. \[LongDash] Why does each filled \
Landau level contribute to exactly one unit of $$\\sigma _H$$ ?

#### Charge Pumping

Consider a *annular geometry* that allows us to probe the Hall effect \
via **radial charge pumping**.

```wl
In[200]:=
Manipulate[Block[{a = 0.3, M = 9}, Graphics[{{Lighter[Green, 0.9], \
Annulus[{0, 0}, {a, Sqrt[M + 1 / 2]}]}, {Green, Opacity[\[Phi]], \
Circle[{0, 0}, 0.5a], Disk[{0, 0}, 0.2a], Text[\[Phi], {0,  - a}, {0, \
0.8}]}, {AbsoluteThickness[1], LightGray, Dashed, Table[Circle[{0, \
0}, Sqrt[m]], {m, 1, M}]}, {Table[Circle[{0, 0}, Max[Sqrt[m - \
\[Phi]], a]], {m, 1, M}]}, {Opacity[1 - Sqrt[1 - \[Phi]] / a], Text[\
\[VeryThinSpace]e, {a, 0}, { - 1, 0}], Text[\[VeryThinSpace] - e, { - \
Sqrt[M + 1 / 2], 0}, {0.5, 0}]}}, ImageSize -> 160]], {{\[Phi], 1, \
Style[\[Phi]/\[Phi]
   0, \"InlineFormula\"]}, 0, 1, ImageSize -> Small}, Paneled -> False]

Out[200]= DynamicModule[«8»]
```

* In addition to a uniform perpendicular magnetic field $$B$$, we \
thread an extra *magnetic flux* $$\\phi (t)$$ through the central \
hole, which *slowly* increases from $$0$$ to $$\\phi _0$$ over a \
*long* time $$T$$,

```wl
$$\\phi (t)=\\phi _0\\frac{t}{T},$$
```

	* $$\\phi _0=h/e$$ - flux quantum,

	* $$T\\gg 1\\left/\\omega _c\\right.$$ - *adiabatic* evolution time. \
($$t:0\\rightarrow T$$).

* Due to the **Aharonov-Bohm effect**, each quantum state $$| \
n,m\\rangle$$ will be affected \[LongDash] its wave function radius \
$$r_m$$ will be deformed adiabatically,

```wl
$$r_m=\\sqrt{\\frac{\\phi _0}{\\pi  B}}\\sqrt{m-t/T}.$$
```

Derive Eq. (XXX).

The total flux within the radius $$r_m$$ is

```wl
$$\\phi _{\\text{total}}=\\pi  r_m^2B+\\phi (t),$$
```

which determines the Berry phase as the particle that travels \
adiabatically around the orbit,

```wl
$$\\frac{e \\phi _{\\text{total}}}{\\hbar }=\\frac{e}{\\hbar }\\left(\
\\pi  r_m^2B+\\phi (t)\\right)=2\\pi  m,$$
```

which is quantized to $$2\\pi  m$$. This implies

```wl
$$r_m^2=\\frac{1}{\\pi  B}\\left(\\frac{2\\pi  \\hbar  m}{e}-\\phi \
(t)\\right)$$
$$=\\frac{1}{\\pi  B}\\left(\\frac{h}{e}m-\\phi \
_0\\frac{t}{T}\\right),\\\\
=\\frac{\\phi _0}{\\pi  B}(m-t/T).$$
```

Under the flux insertion,

```wl
$$\\begin{array}{cccc}
 t: & 0 & \\text{-$>$} & T \\\\
 \\phi (t): & 0 & \\rightarrow  & \\phi _0 \\\\
 r_m\\propto  & \\sqrt{m} & \\rightarrow  & \\sqrt{m-1} \\\\
\\end{array}
,$$
```

the radius of every orbit shrinks from $$\\sqrt{m}$$ to \
$$\\sqrt{m-1}$$ \[Implies] pumping *one charge* $$e$$ from the \
*outer* edge to the *inner* edge.

* During this process,

	* the radial current density:

```wl
$$j_r=\\frac{1}{2\\pi  r}\\frac{e}{T},$$
```

	* the circular electric field induced by the changing flux:

```wl
$$E_{\\theta }=\\frac{1}{2\\pi  r}\\frac{d\\phi \
(t)}{dt}=\\frac{1}{2\\pi  r}\\frac{\\phi _0}{T},$$
```

**Hall conductivity** for each fully filled Landau level:

```wl
$$\\sigma _H=\\frac{j_r}{E_{\\theta }}=\\frac{e}{\\phi \
_0}=\\frac{e^2}{h}.$$
```

Conclusion: *quantized* transport of charge in response to \
*quantized* flux insertion \[Implies] *quantized* Hall conductance.

#### Linear Response Theory

The **Hall conductivity** $$\\sigma _H$$ characterizes how the \
**current density** $$\\pmb{j}$$ (observable) *responds* to the \
**electric field** $$\\pmb{E}$$ (perturbation).

* Current density operator for *each electron* (assuming $$m=e=h=1$$) \
reads

```wl
$$\\hat{\\pmb{j}}=\\frac{B}{N_{\\phi }}\\hat{\\pmb{\\pi }}.$$
```

Justify Eq. (XXX) based on Eq. (XXX).

According to Eq. (XXX), the current density of the system is given by

```wl
$$\\pmb{j}=n e \\pmb{v}$$
$$=\\frac{N e}{A m} \\pmb{\\pi }$$
$$=N\\frac{B}{N_{\\phi }}\\frac{e^2}{m h} \\pmb{\\pi },$$
```

where

* $$\\pmb{\\pi }=m \\pmb{v}$$ is the kinetic momentum,

* $$n=N/A$$ is the electron density (number of electrons per area),

* A is the total area of the system, related to the Landau level \
degeneracy Subscript[N, \\[Phi]] by Eq. (XXX)

```wl
$$N_{\\phi }=\\frac{B A}{\\phi _0}\\Rightarrow A=\\frac{N_{\\phi \
}\\phi _0}{B}=\\frac{N_{\\phi }h}{e B}.$$
```

So every electron in the system contributes to the current density by

```wl
$$\\frac{\\pmb{j}}{N}=\\frac{B}{N_{\\phi }}\\frac{e^2}{m h} \
\\pmb{\\pi }.$$
```

Take the $$m=e=h=1$$ unit, the *single-particle* current operator \
$$\\hat{\\pmb{j}}$$ should be given by

```wl
$$\\hat{\\pmb{j}}=\\frac{B}{N_{\\phi }} \\hat{\\pmb{\\pi }}.$$
```

	* The *expectation value* of **current density** in the *system* is \
given by

```wl
$$\\langle \\pmb{j}\\rangle =\\sum _{n,m \\in  \\text{occ}} \\langle \
n,m| \\hat{\\pmb{j}}| n,m\\rangle$$
$$=\\frac{B}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \\langle n,m| \
\\hat{\\pmb{\\pi }}| n,m\\rangle ,$$
```

where $$\\sum _{n,m \\in  \\text{occ}}$$ is to sum over all lowest \
$$| n,m\\rangle$$ states that are *occupied* by the electron.

	* Based on Eq. (XXX), the kinetic momentum operator 
\\!\\(\\*OverscriptBox[
StyleBox[\"\\[Pi]\",
FontWeight->\"Bold\"], \\(^\\)]\\) can be expressed as

```wl
$$\\hat{\\pi }_x=\\sqrt{\\frac{B}{2}}\\left(\\hat{a}^{\\dagger \
}+\\hat{a}\\right), \\hat{\\pi }_y=\\sqrt{\\frac{B}{2}}i \
\\left(\\hat{a}^{\\dagger }-\\hat{a}\\right).$$
```

As expected, the current density $$\\langle \\pmb{j}\\rangle =0$$ \
vanishes on the many-body ground state, in the absence of perturbation.

* Applying a (weak) **electric field** $$\\pmb{E}$$ to the system \
amounts to perturbing the **vector potential** $$\\pmb{A}$$ by a \
*time-dependent* perturbation $$\\delta \\pmb{A}(t)$$,

```wl
$$\\pmb{A}\\rightarrow \\pmb{A}+\\delta \\pmb{A}(t),$$
```

with E (t) = -\\!\\(
\\*SubscriptBox[\\(\\[PartialD]\\), \
\\(t\\)]\\[Delta]\\)\\[InvisibleComma]A (t), according to Eq. (XXX).

	* Assume that $$\\pmb{E}(t)=\\pmb{E} e^{-i \\left(\\omega +i\\, \
0_+\\right)t}$$ takes an oscillatory form with frequency $$\\omega$$, \
and is adiabatically turned on from the infinite past, then

```wl
$$\\delta \\pmb{A}(t)=\\int _{-\\infty \
}^tdt'\\pmb{E}(t')=-\\frac{\\pmb{E}}{i \\omega }e^{-i \\left(\\omega \
+i\\, 0_+\\right) t}.$$

In[111]:=
Block[{\[Omega] = 2\[Pi], \[CurlyEpsilon] = 0.05}, 
	Plot[Re[Exp[ - I (\[Omega] + I \[CurlyEpsilon]) t]], {t,  - 50, 2}, \
PlotStyle -> Black, PlotRange -> { - 1.2, 1.2}, FrameLabel -> {t/T,  \
-I (\[Omega] + I\[VeryThinSpace]\[CurlyEpsilon]) t
E}, PlotLabel -> StringTemplate[\[CurlyEpsilon]T = `2`][\[Omega], \
\[CurlyEpsilon]], AspectRatio -> 0.4, ImageSize -> 240]]

Out[111]=
\\!\\(\\*GraphicsBox[{{{}, {}, TagBox[{GrayLevel[0], \
AbsolutePointSize[4], AbsoluteThickness[1.5], 
     Opacity[1.], LineBox[{{-49.999, 0.082}, {-49.984, 
      0.081}, {-49.968, 0.080}, {-49.952, 
      0.078}, {-49.936, 0.075}, {-49.920, 
      0.072 ... \"\", TraditionalForm], 
 PlotRange -> {{-49.999, 1.999}, {-1.2, 1.2}}, PlotRangeClipping -> \
True, 
 PlotRangePadding -> {{Scaled[0.02], Scaled[0.02]}, {0, 0}}, Ticks -> \
{Automatic, Automatic}, 
 TicksStyle -> Directive[GrayLevel[0], FontSize -> 12]]\\)
```

	* This means the **Hamiltonian operator** will be perturbed by

```wl
$$\\hat{H}\\rightarrow \\hat{H}+\\delta \\hat{H}(t),$$
```

with the perturbation given by

```wl
$$\\delta \\hat{H}(t)=\\frac{\\partial \\hat{H}}{\\partial \
\\pmb{A}}\\cdot \\delta \\pmb{A}(t)$$
```

to the leading order of $$\\delta \\pmb{A}(t)$$.

		* Given that $$\\hat{\\pmb{\\pi }}=\\hat{\\pmb{p}}-\\pmb{A}$$ and

```wl
$$\\hat{H}=\\frac{1}{2}\\hat{\\pmb{\\pi \
}}^2=\\frac{1}{2}\\left(\\hat{\\pmb{p}}-\\pmb{A}\\right)^2,$$
```

we have

```wl
$$\\frac{\\partial \\hat{H}}{\\partial \
\\pmb{A}}=-\\left(\\hat{\\pmb{p}}-\\pmb{A}\\right)=-\\hat{\\pmb{\\pi \
}}.$$
```

Substitute Eq. (XXX) into Eq. (XXX), the time-dependent perturbation \
Hamiltonian reads

```wl
$$\\delta \\hat{H}(t)=-\\hat{\\pmb{\\pi }}\\cdot \\delta \\pmb{A}(t)=\
\\frac{1}{i \\omega }\\pmb{E}\\cdot \
\\pmb{\\overset{{}^{\\wedge}}{\\pmb{\\pi }}} e^{-i \\left(\\omega
+i\\, 0_+\\right) t}.$$
```

The time-dependent perturbation problem can solved by the Green\
\[CloseCurlyQuote]s function approach.

* **Dressed Green\[CloseCurlyQuote]s function** (unitary \
time-evolution operator) can be computed from the Dyson series to the \
leading order

```wl
$$\\hat{G}(t,-\\infty )=\\hat{G}_0(t,-\\infty )+(-i)\\int _{-\\infty \
}^tdt'\\hat{G}_0\\left(t,t'\\right)\\delta \
\\hat{H}\\left(t'\\right)\\hat{G}_0\\left(t',-\\infty
\\right)+\\ldots ,$$
```

where the **bare Green\[CloseCurlyQuote]s function** is defined by

```wl
$$\\hat{G}_0\\left(t,t'\\right)=\\sum _{n,m} | n,m\\rangle e^{-i \
E_n\\left(t-t'\\right)}\\langle n,m| ,$$
```

with Subscript[E, n] = B (n + 1/2) being the Landau level energy (see \
Eq. (XXX)).

* Every state will evolve in time by

```wl
$$| n,m\\rangle \\rightarrow \\hat{G}(t,-\\infty )| n,m\\rangle .$$
```

As a result, by Eq. (XXX), the current density expectation value \
\\[LeftAngleBracket]j\\[RightAngleBracket] evolves as

```wl
$$\\langle \\pmb{j}(t)\\rangle =\\frac{B}{N_{\\phi }}\\sum _{n,m \\in \
 \\text{occ}} \\langle n,m| \\hat{G}(-\\infty ,t)\\hat{\\pmb{\\pi \
}}\\hat{G}(t,-\\infty )|
n,m\\rangle$$
$$=\\frac{B}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \\langle n,m| \
\\left(\\hat{\\pmb{\\pi }}(t)+\\frac{1}{\\omega }\\int _{-\\infty \
}^tdt'e^{-i \\left(\\omega
+i\\, 0_+\\right) t'}\\left[\\pmb{E}\\cdot \
\\pmb{\\overset{{}^{\\wedge}}{\\pmb{\\pi }}}(t'),\\hat{\\pmb{\\pi \
}}(t)\\right]+\\ldots \\right)| n,m\\rangle .$$
```

Derive Eq. (XXX).

Substitute Eq. (XXX) into Eq. (XXX) and keep terms to the order of \
\\[Delta]\\[InvisibleComma]H,

```wl
$$\\langle \\pmb{j}(t)\\rangle =\\frac{B}{N_{\\phi }}\\sum _{n,m \\in \
 \\text{occ}} \\langle n,m| \\hat{G}(-\\infty ,t)\\hat{\\pmb{\\pi \
}}\\hat{G}(t,-\\infty )|
n,m\\rangle$$
$$=\\frac{B}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \\langle n,m| \
\\left(\\hat{G}_0(-\\infty ,t)\\hat{\\pmb{\\pi \
}}\\hat{G_0}(t,-\\infty )+(-i)\\int _{-\\infty
}^tdt'\\hat{G}_0(-\\infty ,t)\\hat{\\pmb{\\pi }}\\hat{G}_0\\left(t,t'\
\\right)\\delta \\hat{H}\\left(t'\\right)\\hat{G}_0\\left(t',-\\infty \
\\right)-\\right.\\\\
\\left.(-i)\\int _{-\\infty }^tdt'\\hat{G}_0\\left(-\\infty \
,t'\\right)\\delta \
\\hat{H}\\left(t'\\right)\\hat{G}_0\\left(t',t\\right)\\hat{\\pmb{\\\
pi }}\\hat{G_0}(t,-\\infty
)+\\ldots \\right)| n,m\\rangle .$$
```

To simplify, we may switch to the interaction picture by defining

```wl
$$\\hat{\\pmb{\\pi }}(t)\\text{:=}\\hat{G}_0(-\\infty ,t)\\hat{\\pmb{\
\\pi }}\\hat{G_0}(t,-\\infty ),$$

$$\\delta \\hat{H}_{\\mathcal{I}}(t)\\text{:=}\\hat{G}_0(-\\infty ,t)\
\\delta \\hat{H}(t)\\hat{G_0}(t,-\\infty )$$
$$=\\hat{G}_0(-\\infty ,t)\\frac{1}{i \\omega }\\pmb{E}\\cdot \
\\pmb{\\overset{{}^{\\wedge}}{\\pmb{\\pi }}} e^{-i \\left(\\omega \
+i\\, 0_+\\right) t}\\hat{G_0}(t,-\\infty
)$$
$$=\\frac{1}{i \\omega }\\pmb{E}\\cdot \\pmb{\\overset{{}^{\\wedge}}{\
\\pmb{\\pi }}}(t) e^{-i \\left(\\omega +i\\, 0_+\\right) t}.$$
```

Then we have

```wl
$$\\langle \\pmb{j}(t)\\rangle =\\frac{B}{N_{\\phi }}\\sum _{n,m \\in \
 \\text{occ}} \\langle n,m| \\left(\\hat{\\pmb{\\pi }}(t)+(-i)\\int \
_{-\\infty }^tdt'\\hat{\\pmb{\\pi
}}(t)\\delta \\hat{H}_{\\mathcal{I}}\\left(t'\\right)-(-i)\\int \
_{-\\infty }^tdt'\\delta \
\\hat{H}_{\\mathcal{I}}\\left(t'\\right)\\hat{\\pmb{\\pi \
}}(t)+\\ldots \\right)|
n,m\\rangle$$
$$=\\frac{B}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \\langle n,m| \
\\left(\\hat{\\pmb{\\pi }}(t)+i\\int _{-\\infty }^tdt'\\left[\\delta \
\\hat{H}_{\\mathcal{I}}\\left(t'\\right),\\hat{\\pmb{\\pi
}}(t)\\right]+\\ldots \\right)| n,m\\rangle$$
$$=\\frac{B}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \\langle n,m| \
\\left(\\hat{\\pmb{\\pi }}(t)+\\frac{1}{\\omega }\\int _{-\\infty \
}^tdt'e^{-i \\left(\\omega
+i\\, 0_+\\right) t'}\\left[\\pmb{E}\\cdot \
\\pmb{\\overset{{}^{\\wedge}}{\\pmb{\\pi }}}(t'),\\hat{\\pmb{\\pi \
}}(t)\\right]+\\ldots \\right)| n,m\\rangle .$$
```

where we have introduced

```wl
$$\\hat{\\pmb{\\pi }}(t)\\text{:=}\\hat{G}_0(-\\infty ,t)\\hat{\\pmb{\
\\pi }}\\hat{G_0}(t,-\\infty ).$$
```

	* The first term in Eq. (XXX) is the current density in the absence \
of an electric field, which vanishes.

```wl
$$\\sum _{n,m \\in  \\text{occ}} \\langle n,m| \\hat{\\pmb{\\pi \
}}(t)| n,m\\rangle =0.$$
```

Show Eq. (XXX).

Each term in the summation reads

```wl
$$\\langle n,m| \\hat{\\pmb{\\pi }}(t)| n,m\\rangle$$
$$=\\langle n,m| \\hat{G}_0(-\\infty ,t)\\hat{\\pmb{\\pi \
}}\\hat{G_0}(t,-\\infty )| n,m\\rangle$$
$$=\\langle n,m| e^{i E_n(t+\\infty )}\\hat{\\pmb{\\pi }}e^{-i E_n(t+\
\\infty )}| n,m\\rangle$$
$$=\\langle n,m| \\hat{\\pmb{\\pi }}| n,m\\rangle .$$
```

Given that

```wl
$$\\langle n,m| \\hat{\\pi }_x| n,m\\rangle \
=\\sqrt{\\frac{B}{2}}\\langle n,m| \\left(\\hat{a}^{\\dagger \
}+\\hat{a}\\right)| n,m\\rangle$$
$$=\\sqrt{\\frac{B}{2}}\\left(\\sqrt{n+1}\\langle n,m|n+1,m\\rangle +\
\\sqrt{n}\\langle n,m|n-1,m\\rangle \\right)$$
$$=0,\\\\
\\langle n,m| \\hat{\\pi }_y| n,m\\rangle =\\sqrt{\\frac{B}{2}}i \
\\langle n,m| \\left(\\hat{a}^{\\dagger }-\\hat{a}\\right)| \
n,m\\rangle$$
$$=\\sqrt{\\frac{B}{2}}i \\left(\\sqrt{n+1}\\langle n,m|n+1,m\\rangle \
-\\sqrt{n}\\langle n,m|n-1,m\\rangle \\right)$$
$$=0,$$
```

so $$\\langle n,m| \\hat{\\pmb{\\pi }}(t)| n,m\\rangle =0$$ for all \
$$n,m\\in \\mathbb{N}$$. Therefore, the summation $$\\sum _{n,m \\in  \
\\text{occ}} \\langle n,m| \\hat{\\pmb{\\pi }}(t)| n,m\\rangle$$ also \
vanishes.

	* The second term in Eq. (XXX) describes the linear response of the \
current density under the electric field, which takes the form of

```wl
$$\\langle \\pmb{j}(t)\\rangle =\\pmb{E}\\cdot \\sigma (\\omega \
)e^{-i \\left(\\omega +i\\, 0_+\\right) t},$$
```

with the **conductivity matrix** $$\\sigma _{j\\, i}(\\omega )$$ \
given by

```wl
$$\\sigma _{j\\, i}(\\omega )=\\frac{B}{\\omega  N_{\\phi }}\\int _{-\
\\infty }^0dt e^{-i \\left(\\omega +i\\, 0_+\\right) t}\\sum _{n,m \
\\in  \\text{occ}} \\langle
n,m| \\left[\\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_j(t),\\hat{\\pi \
}_i(0)\\right]| n,m\\rangle .$$
```

Derive Eq. (XXX) and Eq. (XXX).

Take the second term in Eq. (XXX),

```wl
$$\\langle \\pmb{j}(t)\\rangle =\\frac{B}{\\omega  N_{\\phi }}\\int \
_{-\\infty }^tdt'e^{-i \\left(\\omega +i\\, 0_+\\right) t'}\\sum \
_{n,m \\in  \\text{occ}} \\langle
n,m| \\left[\\pmb{E}\\cdot \\pmb{\\overset{{}^{\\wedge}}{\\pmb{\\pi \
}}}(t'),\\hat{\\pmb{\\pi }}(t)\\right]| n,m\\rangle$$
$$=\\frac{B e^{-i \\left(\\omega +i\\, 0_+\\right) t}}{\\omega  \
N_{\\phi }}\\int _{-\\infty }^tdt'e^{-i \\left(\\omega +i\\, \
0_+\\right) \\left(t'-t\\right)}\\sum
_{n,m \\in  \\text{occ}} \\langle n,m| \\left[\\pmb{E}\\cdot \
\\pmb{\\overset{{}^{\\wedge}}{\\pmb{\\pi }}}(t'),\\hat{\\pmb{\\pi \
}}(t)\\right]| n,m\\rangle .$$
```

Because the system is invariant under *time translation*, the \
correlation function above can only depend on $$t^{\\prime\\prime \
}=t'-t$$,

```wl
$$\\langle \\pmb{j}(t)\\rangle$$
$$=\\frac{B e^{-i \\left(\\omega +i\\, 0_+\\right) t}}{\\omega  \
N_{\\phi }}\\int _{-\\infty }^0dt^{\\prime\\prime }e^{-i \
\\left(\\omega +i\\, 0_+\\right) t^{\\prime\\prime
}}\\sum _{n,m \\in  \\text{occ}} \\langle n,m| \\left[\\pmb{E}\\cdot \
\\pmb{\\overset{{}^{\\wedge}}{\\pmb{\\pi }}}(t^{\\prime\\prime \
}),\\hat{\\pmb{\\pi }}(0)\\right]|
n,m\\rangle .$$
```

Introduce the conductivity tensor

```wl
$$\\sigma _{j\\, i}(\\omega )=\\frac{B}{\\omega  N_{\\phi }}\\int _{-\
\\infty }^0dt e^{-i \\left(\\omega +i\\, 0_+\\right) t}\\sum _{n,m \
\\in  \\text{occ}} \\langle
n,m| \\left[\\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_j(t),\\hat{\\pi \
}_i(0)\\right]| n,m\\rangle ,$$
```

the current density can be written as

```wl
$$\\left\\langle j_i(t)\\right\\rangle =E_j\\sigma _{j\\, i}(\\omega \
)e^{-i \\left(\\omega +i\\, 0_+\\right) t}.$$
```

Eq. (XXX) implies that when the applied electric field E (t) = E \
E^(-I (\\[Omega] + I SubPlus[0]) t) oscillates at frequency \
\\[Omega], the induced current \\[LeftAngleBracket]j(t)\\[RightAngleBracket] \
also oscillates at the same frequency. \\[LongDash] A feature of \
linear response.

* The **Hall conductivity** corresponds to the off-diagonal component \
$$\\sigma _{x\\, y}(\\omega )$$ of the conductivity matrix. In the DC \
limit $$\\omega \\text{-$>$}0$$, it is given by the **Kobo formula** :

```wl
$$\\sigma _H\\text{:=}\\lim_{\\omega \\text{-$>$}0} \\sigma _{x\\, \
y}(\\omega )=\\frac{B}{i N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \
\\sum _{n'\\neq n} \\frac{\\langle
n,m| \\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_x\\left| \
n',m\\right\\rangle \\left\\langle n',m\\right| \\hat{\\pi }_y| \
n,m\\rangle -h.c.}{\\left(E_{n'}-E_n\\right){}^2}.$$
```

Derive Eq. (XXX).

According to Eq. (XXX),

```wl
$$\\langle n,m| \\left[\\pmb{\\overset{{}^{\\wedge}}{\\pi \
}}{}_j(t),\\hat{\\pi }_i(0)\\right]| n,m\\rangle$$
$$=\\sum _{n',m'} \\left(\\langle n,m| \\pmb{\\overset{{}^{\\wedge}}{\
\\pi }}{}_j(t)\\left| n',m'\\right\\rangle \\left\\langle \
n',m'\\right| \\hat{\\pi }_i(0)|
n,m\\rangle -\\langle n,m| \\pmb{\\overset{{}^{\\wedge}}{\\pi \
}}{}_i(0)\\left| n',m'\\right\\rangle \\left\\langle n',m'\\right| \
\\hat{\\pi }_j(t)| n,m\\rangle
\\right)$$
$$=\\sum _{n',m'} \\left(\\langle n,m| e^{i E_nt}\\pmb{\\overset{{}^{\
\\wedge}}{\\pi }}{}_je^{-i E_{n'}t}\\left| n',m'\\right\\rangle \
\\left\\langle n',m'\\right|
\\hat{\\pi }_i| n,m\\rangle -\\langle n,m| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_i\\left| n',m'\\right\\rangle \
\\left\\langle n',m'\\right| e^{i \
E_{n'}t}\\pmb{\\overset{{}^{\\wedge}}{\\pi
}}{}_je^{-i E_nt}| n,m\\rangle \\right)$$
$$=\\sum _{n',m'} \\left(\\langle n,m| \\pmb{\\overset{{}^{\\wedge}}{\
\\pi }}{}_j\\left| n',m'\\right\\rangle \\left\\langle n',m'\\right| \
\\hat{\\pi }_i| n,m\\rangle
e^{i \\left(E_n-E_{n'}\\right)t}-\\langle n,m| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_i\\left| n',m'\\right\\rangle \
\\left\\langle n',m'\\right| \\pmb{\\overset{{}^{\\wedge}}{\\pi
}}{}_j| n,m\\rangle e^{-i \\left(E_n-E_{n'}\\right)t}\\right),$$
```

so the conductivity matrix reads

```wl
$$\\sigma _{j\\, i}(\\omega )=\\frac{B}{\\omega  N_{\\phi }}\\int _{-\
\\infty }^0dt \\sum _{n,m \\in  \\text{occ}} \\sum _{n',m'} \
\\left(\\langle n,m| \\pmb{\\overset{{}^{\\wedge}}{\\pi
}}{}_j\\left| n',m'\\right\\rangle \\left\\langle n',m'\\right| \
\\hat{\\pi }_i| n,m\\rangle e^{-i \\left(\\omega +i\\, 0_+-E_n+E_{n'}\
\\right) t}-\\right.\\\\
\\left.\\langle n,m| \\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_i\\left| \
n',m'\\right\\rangle \\left\\langle n',m'\\right| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_j|
n,m\\rangle e^{-i \\left(\\omega +i\\, 0_++E_n-E_{n'}\\right) \
t}\\right)$$
$$=\\frac{i B}{\\omega  N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \
\\sum _{n',m'} \\left(\\frac{\\langle n,m| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_j\\left| n',m'\\right\\rangle
\\left\\langle n',m'\\right| \\hat{\\pi }_i| n,m\\rangle }{\\omega \
-E_n+E_{n'}}-\\frac{\\langle n,m| \\pmb{\\overset{{}^{\\wedge}}{\\pi \
}}{}_i\\left| n',m'\\right\\rangle
\\left\\langle n',m'\\right| \\pmb{\\overset{{}^{\\wedge}}{\\pi \
}}{}_j| n,m\\rangle }{\\omega +E_n-E_{n'}}\\right).$$
```

Given Eq. (XXX), we know that Subscript[
\\!\\(\\*OverscriptBox[\\(\\[Pi]\\), \\(^\\)]\\), i] operator only \
change the quantum number n by one,

```wl
$$\\hat{\\pi }_i| n,m\\rangle \\rightarrow | n\\pm 1,m\\rangle ,$$
```

so the scalar products like $$\\langle n,m| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_i\\left| \
n',m'\\right\\rangle$$ will be non-vanishing only if $$m=m'$$. Thus \
we can perform the summation of $$m'$$ first to identify it with $$m$$,

```wl
$$\\sigma _{j\\, i}(\\omega )=\\frac{i B}{\\omega  N_{\\phi }}\\sum \
_{n,m \\in  \\text{occ}} \\sum _{n'} \\left(\\frac{\\langle n,m| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi
}}{}_j\\left| n',m\\right\\rangle \\left\\langle n',m\\right| \
\\hat{\\pi }_i| n,m\\rangle }{\\omega -E_n+E_{n'}}-\\frac{\\langle \
n,m| \\pmb{\\overset{{}^{\\wedge}}{\\pi
}}{}_i\\left| n',m\\right\\rangle \\left\\langle n',m\\right| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_j| n,m\\rangle }{\\omega \
+E_n-E_{n'}}\\right).$$
```

In the $$\\omega \\text{-$>$}0$$ limit,

```wl
$$\\frac{1}{\\omega -E_n+E_{n'}}=\\frac{1}{E_{n'}-E_n}-\\frac{\\omega \
}{\\left(E_{n'}-E_n\\right){}^2}+\\ldots ,\\\\
\\frac{1}{\\omega +E_n-E_{n'}}=-\\frac{1}{E_{n'}-E_n}-\\frac{\\omega \
}{\\left(E_{n'}-E_n\\right){}^2}+\\ldots ,$$
```

so $$\\sigma _{j\\, i}(\\omega )$$ breaks into

```wl
$$\\sigma _{j\\, i}(\\omega )=\\frac{i B}{\\omega  N_{\\phi }}\\sum \
_{n,m \\in  \\text{occ}} \\sum _{n'} \
\\frac{1}{E_{n'}-E_n}\\left(\\langle n,m| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi
}}{}_j\\left| n',m\\right\\rangle \\left\\langle n',m\\right| \
\\hat{\\pi }_i| n,m\\rangle +h.c.\\right)$$
$$-\\frac{i B}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \\sum _{n'} \
\\frac{1}{\\left(E_{n'}-E_n\\right){}^2}\\left(\\langle n,m| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi
}}{}_j\\left| n',m\\right\\rangle \\left\\langle n',m\\right| \
\\hat{\\pi }_i| n,m\\rangle -h.c.\\right)$$
```

* The first term looks divergent. Indeed, such divergences do arise \
for longitudinal conductivities. However, it does not contribute to \
the Hall conductivity.

* The Hall conductivity only receives contribution from the second \
term,

```wl
$$\\sigma _{x\\, y}(\\omega )=\\frac{B}{i N_{\\phi }}\\sum _{n,m \\in \
 \\text{occ}} \\sum _{n'} \\frac{\\langle n,m| \
\\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_x\\left|
n',m\\right\\rangle \\left\\langle n',m\\right| \\hat{\\pi }_y| \
n,m\\rangle -h.c.}{\\left(E_{n'}-E_n\\right){}^2}.$$
```

* Using Eq. (XXX) to represent the kinetic momentum operator 
\\!\\(\\*OverscriptBox[
StyleBox[\"\\[Pi]\",
FontWeight->\"Bold\"], \\(^\\)]\\) as annihilation and creation \
operators, and given that

```wl
$$\\hat{a}| n,m\\rangle =\\sqrt{n}| n-1,m\\rangle ,\\\\
\\hat{a}^{\\dagger }| n,m\\rangle =\\sqrt{n+1}| n+1,m\\rangle ,$$
```

the Hall conductivity Subscript[\\[Sigma], H] in Eq. (XXX) reduces to

```wl
$$\\sigma _H=\\frac{1}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \
1=\\sum _{n\\in \\text{occ}} 1.$$
```

Derive Eq. (XXX).

Substitute Eq. (XXX) into Eq. (XXX),

```wl
$$\\langle n,m| \\pmb{\\overset{{}^{\\wedge}}{\\pi }}{}_x\\left| n',m\
\\right\\rangle \\left\\langle n',m\\right| \\hat{\\pi }_y| \
n,m\\rangle$$
$$=\\frac{i B}{2}\\langle n,m| \\left(\\hat{a}^{\\dagger \
}+\\hat{a}\\right)\\left| n',m\\right\\rangle \\left\\langle \
n',m\\right| \\left(\\hat{a}^{\\dagger }-\\hat{a}\\right)|
n,m\\rangle$$
$$=\\frac{i B}{2}\\left(\\langle n,m| \\hat{a}\\left| \
n',m\\right\\rangle \\left\\langle n',m\\right| \\hat{a}^{\\dagger }| \
n,m\\rangle -\\langle n,m| \\hat{a}^{\\dagger
}\\left| n',m\\right\\rangle \\left\\langle n',m\\right| \\hat{a}| \
n,m\\rangle \\right)$$
$$=\\frac{i B}{2}\\left((n+1)\\left| \\left\\langle n',m\\right|n+1,m\
\\rangle \\right| ^2-n\\left| \\left\\langle \
n',m\\right|n-1,m\\rangle \\right| ^2\\right)$$
$$=\\frac{i B}{2}\\left((n+1)\\delta _{n',n+1}-n \\delta \
_{n',n-1}\\right).$$
```

Therefore

```wl
$$\\sigma _H=\\frac{B}{i N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \
\\sum _{n'\\neq n} \
\\frac{1}{\\left(E_{n'}-E_n\\right){}^2}\\left(\\frac{i \
B}{2}\\left((n+1)\\delta
_{n',n+1}-n \\delta _{n',n-1}\\right)-h.c.\\right)$$
$$=\\frac{B}{i N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \\sum \
_{n'\\neq n} \\frac{i \
B}{\\left(E_{n'}-E_n\\right){}^2}\\left((n+1)\\delta _{n',n+1}-n \
\\delta
_{n',n-1}\\right)$$
$$=\\frac{B^2}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \\sum \
_{n'\\neq n} \\left(\\frac{(n+1)\\delta \
_{n',n+1}}{\\left(E_{n'}-E_n\\right){}^2}-\\frac{n \\delta
_{n',n-1}}{\\left(E_{n'}-E_n\\right){}^2}\\right)$$
$$=\\frac{B^2}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \
\\left(\\frac{n+1}{\\left(E_{n+1}-E_n\\right){}^2}-\\frac{n}{\\left(E_\
{n-1}-E_n\\right){}^2}\\right).$$
```

Given that $$E_n=B (n+1/2)$$,

```wl
$$\\sigma _H=\\frac{B^2}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} \
\\left(\\frac{n+1}{B^2}-\\frac{n}{B^2}\\right)$$
$$=\\frac{1}{N_{\\phi }}\\sum _{n,m \\in  \\text{occ}} 1.$$
```

	* Each occupied state contributes $$1\\left/N_{\\phi }\\right.$$ to \
$$\\sigma _H$$ (in unit of the conductance quantum \
$$\\left.e^2\\right/h$$).

	* Each Landau level is $$N_{\\phi }$$-fold degenerated. \[Implies] \
Fully filling each Landau level produces exactly one unit of \
$$\\sigma _H$$.

## Spin and Monopole

### Classical Spin

#### Angular Momentum Decomposition

The classical motion of a **spinning top** is governed by

```wl
$$\\pmb{\\tau }=\\frac{d\\pmb{L}}{dt},$$
```

where

* $$\\pmb{\\tau }$$ - **torque** exerted on the top,

* $$\\pmb{L}$$ - total **angular momentum** of the top, decomposed \
into components *parallel* $$I_a\\pmb{\\omega }$$ and *perpendicular* \
$$I_t\\pmb{\\Omega }$$ to the spinning axis

```wl
$$\\pmb{L}=I_a\\pmb{\\omega }+I_t\\pmb{\\Omega },$$

In[353]:=
Block[{r = 1, d = 0.05, h = 1, a = 0.05, \[Theta] = \[Pi] / 8, \[Phi] \
=  - \[Pi] / 3, \[Alpha] = \[Pi] / 24, th = 0.016, c = 0.2, viewpt, \
dashedtube, rot}, 
	viewpt = {1.3,  - 2.4, 1.5};
	dashedtube[v_] := Tube[Table[{x v, (x + 0.05)v}, {x,  - 1, 0.9, \
0.1}], th];
	rot[g_] := Rotate[Rotate[g, \[Theta], {1, 0, 0}, {0, 0, 0}], \[Phi], \
{0, 0, 1}, {0, 0, 0}];
	Graphics3D[{Translate[rot[{White, AbsoluteThickness[5], Line[# h{0, \
0, 1}& /@ { - 1.3,  - 1.4}], 
	Line[# r{0, 1, 0}& /@ { - 1.15,  - 1.2}]}],  - 0.02viewpt], \
rot[{{EdgeForm[], Specularity[White, 5], Gray, Tube[{0, 0, #}& /@ { - \
h, h}, a], Opacity[0.8], Yellow, Cylinder[{0, 0, #}& /@ { - d, d}, \
r]}, {Black, dashedtube[1.7h{0, 0, 1}], dashedtube[1.5r{1, 0, 0}], \
dashedtube[1.5r{0, 1, 0}]}, {Black, Tube[Table[{0, 0,  - 1.5h} + \
c{Cos[\[Beta]], Sin[\[Beta]], 0}, {\[Beta], 0, 2\[Pi], \[Pi] / 32}], \
th], Text[I
 a, {0, 0,  - 1.5h}, {2, 0.8}], Tube[Table[{ - 1.2r, 0, 0} + c{0, \
Cos[\[Beta]], Sin[\[Beta]]}, {\[Beta], 0, 2\[Pi], \[Pi] / 32}], th], \
Text[I
 t, { - 1.2r, 0, 0}, { - 1.2,  - 1.2}], Tube[Table[{0,  - 1.2r, 0} + \
c{Cos[\[Beta]], 0, Sin[\[Beta]]}, {\[Beta], 0, 2\[Pi], \[Pi] / 32}], \
th], Text[I
 t, {0,  - 1.2r, 0}, {1, 1.5}]}}], Translate[rot[{Arrowheads[0.05], \
Block[{vL = 2{0, Sin[\[Alpha]], Cos[\[Alpha]]}, vS = 2{0, 0, Cos[\
\[Alpha]]}}, {Blue, Arrow[# vL& /@ {0, 1}], Text[\"\
\\!\\(\[VeryThinSpace]**L**\\)\", vL, { - 2, 1.5}], LightBlue, \
Arrow[vS#& /@ {0, 1}], Text[\"\\!\\(\[VeryThinSpace]**S**\\)\", vS, \
{1, 1}]}], {Red, Arrow[{0, 0, 1.5h}#& /@ {0, 1}], Text[\"\
\\!\\(**\[Omega]**\\)\", {0, 0, 1.5h}, {1, 0.5}], Arrow[{0, 0.4r, \
0}#& /@ {0, 1}], Text[\"\\!\\(**\[CapitalOmega]**\\)\", 0.4r{0, 1, \
0}, {0, 1}]}}], 0.04viewpt]}, Boxed -> False, Lighting -> \
\"Neutral\", ViewPoint -> viewpt, ImageSize -> 140]]

Out[353]=
\\!\\(\\*Graphics3DBox[{GeometricTransformation3DBox[\
GeometricTransformation3DBox[
    GeometricTransformation3DBox[{GrayLevel[1], AbsoluteThickness[5], \

      Line3DBox[{{0., 0., -1.3}, {0., 0., -1.4}}], Line3DBox[{{0., \
-1.15, 0.}, {0., -1.2, 0.}}]}, 
 ... rt[3]/2, 0}, {-1/2*Sqrt[3], 1/2, 0}, {0, 0, 1}}, {0, 0, 0}}, 
     {{{0.5, 0.866, 0}, {-0.866, 0.5, 0}, {0, 0, 1}}, {0, 0, 0}}]], 
   {0.052, -0.096, 0.06}]}, Boxed -> False, ImageSize -> 140, \
Lighting -> \"Neutral\", 
 ViewPoint -> {1.3, -2.4, 1.5}]\\)
```

	* $$I_a$$ - *axial* **moment of inertia** (about the spinning axis),

	* $$I_t$$ - *transverse*** moment of inertia** (about either of the \
two equivalent transverse axes)

	* **\[Omega]** - *axial* **angular velocity** (along the spinning \
axis)

	* $$\\pmb{\\Omega }$$ - *transverse* **angular velocity**, \
describing the instantaneous rotation rate of the spinning axis itself.

#### Dynamics of Spinning Axis

Substitute Eq. (XXX) into Eq. (XXX),

```wl
$$\\pmb{\\tau }=I_a\\frac{d\\pmb{\\omega \
}}{dt}+I_t\\frac{d\\pmb{\\Omega }}{dt}.$$
```

* **Transverse Torque Assumption**: Assume $$\\pmb{\\tau }$$ has no \
component along the spinning axis, so the *magnitude* of \
$$\\pmb{\\omega }$$ remains constant. Only its *direction* changes \
due to the rotation of the spinning axis:

```wl
$$\\frac{d\\pmb{\\omega }}{dt}=\\pmb{\\Omega }\\times \\pmb{\\omega \
},$$
```

Eq. (XXX) becomes

```wl
$$\\pmb{\\tau }=I_a\\pmb{\\Omega }\\times \\pmb{\\omega }+I_t\\frac{d\
\\pmb{\\Omega }}{dt}.$$
```

We are mainly interested in the *motion* of the **spinning axis**, \
represented by the *unit vector*

```wl
$$\\pmb{n}=\\frac{\\pmb{\\omega }}{\\omega }.$$
```

Similar to Eq. (XXX), n also gets rotated by \\[CapitalOmega] as

```wl
$$\\frac{d\\pmb{n}}{dt}=\\pmb{\\Omega }\\times \\pmb{n},$$
```

from which $$\\pmb{\\Omega }$$ can be \[OpenCurlyDoubleQuote]solved\
\[CloseCurlyDoubleQuote] and expressed as

```wl
$$\\pmb{\\Omega }=\\pmb{n}\\times \\frac{d\\pmb{n}}{dt}.$$
```

Derive Eq. (XXX) from Eq. (XXX).

Cross product with n from left on both sides of Eq. (XXX),

```wl
$$\\pmb{n}\\times \\frac{d\\pmb{n}}{dt}=\\pmb{n}\\times \
(\\pmb{\\Omega }\\times \\pmb{n})=\\pmb{\\Omega } (\\pmb{n}\\cdot \
\\pmb{n})-\\pmb{n} (\\pmb{n}\\cdot \\pmb{\\Omega
})=\\pmb{\\Omega },$$
```

because $$\\pmb{n}\\cdot \\pmb{n}=1$$ and $$\\pmb{n}\\cdot \
\\pmb{\\Omega }=0$$ (since $$\\pmb{\\Omega }$$ is defined as the \
component of angular momentum *perpendicular* to the spinning axis $$\
\\pmb{n}$$).

Substitute Eq. (XXX) into Eq. (XXX), and cross product with n from \
right on both sides, we obtain

```wl
$$I_t \\left(\\frac{d^2\\pmb{n}}{dt^2}\\right){}_{\\unicode{27c2}}=\\\
pmb{\\tau }\\times \\pmb{n}-\\frac{d\\pmb{n}}{dt}\\times \\pmb{S},$$
```

where

* $$\\pmb{S}\\text{:=}I_a\\pmb{\\omega }=S \\pmb{n}$$ - **spin \
angular momentum** (*parallel* to the spinning axis),

* $$\\left(\\pmb{\\overset{\\ddot{ \
}}{\\pmb{n}}}\\right)_{\\unicode{27c2}}=\\pmb{\\overset{\\ddot{ \
}}{\\pmb{n}}}-\\left(\\pmb{\\overset{\\ddot{ }}{\\pmb{n}}}\\cdot
\\pmb{n}\\right) \\pmb{n}$$ - component of acceleration \
$$\\pmb{\\overset{\\ddot{ }}{\\pmb{n}}}$$ in the tangent plane.

Derive Eq. (XXX).

Substitute Eq. (XXX) into Eq. (XXX),

```wl
$$\\pmb{\\tau }=I_a\\left(\\pmb{n}\\times \
\\frac{d\\pmb{n}}{dt}\\right)\\times \\pmb{\\omega }+I_t\\frac{d}{dt}\
\\left(\\pmb{n}\\times \\frac{d\\pmb{n}}{dt}\\right)$$
$$=I_a(\\pmb{n}\\cdot \\pmb{\\omega \
})\\frac{d\\pmb{n}}{dt}-I_a\\pmb{n}\\left(\\frac{d\\pmb{n}}{dt}\\cdot \
\\pmb{\\omega }\\right)+I_t\\frac{d\\pmb{n}}{dt}\\times
\\frac{d\\pmb{n}}{dt}+I_t\\pmb{n}\\times \\frac{d^2\\pmb{n}}{dt^2},$$
```

here

* $$(d\\pmb{n}/dt)\\cdot \\pmb{\\omega }=0$$, because the \
normalization condition $$\\pmb{n}\\cdot \\pmb{n}=1$$ of the unit \
vector $$\\pmb{n}$$ implies

```wl
$$2\\frac{d\\pmb{n}}{dt}\\cdot \\pmb{n}=\\frac{d}{dt}(\\pmb{n}\\cdot \
\\pmb{n})=\\frac{d}{dt}(1)=0,$$
```

therefore,

```wl
$$\\frac{d\\pmb{n}}{dt}\\cdot \\pmb{\\omega }=\\omega \
\\frac{d\\pmb{n}}{dt}\\cdot \\pmb{n}=0.$$
```

* $$(d\\pmb{n}/dt)\\times (d\\pmb{n}/dt)=0$$, because any vector \
cross product with itself always vanishes.

So the equation of motion simplifies to

```wl
$$\\pmb{\\tau }=I_a \\omega \\frac{d\\pmb{n}}{dt}+I_t\\pmb{n}\\times \
\\frac{d^2\\pmb{n}}{dt^2}$$
$$=S\\frac{d\\pmb{n}}{dt}+I_t\\pmb{n}\\times \
\\frac{d^2\\pmb{n}}{dt^2},$$
```

where $$S=I_s \\omega$$ is the magnitude of spin angular momentum. \
Further cross product with $$\\pmb{n}$$ on both sides,

```wl
$$\\pmb{\\tau }\\times \\pmb{n}=S\\frac{d\\pmb{n}}{dt}\\times \
\\pmb{n}+I_t \\left(\\pmb{n}\\times \\frac{d^2\\pmb{n}}{dt^2}\\right)\
\\times \\pmb{n},\\\\
=\\frac{d\\pmb{n}}{dt}\\times \\pmb{S}+I_t \\left((\\pmb{n}\\cdot \
\\pmb{n})\\frac{d^2\\pmb{n}}{dt^2}-\\pmb{n} \
\\left(\\frac{d^2\\pmb{n}}{dt^2}\\cdot \\pmb{n}\\right)\\right),$$
```

The last term

```wl
$$\\left(\\pmb{n}\\times \\frac{d^2\\pmb{n}}{dt^2}\\right)\\times \
\\pmb{n}=(\\pmb{n}\\cdot \\pmb{n})\\frac{d^2\\pmb{n}}{dt^2}-\\pmb{n} \
\\left(\\frac{d^2\\pmb{n}}{dt^2}\\cdot
\\pmb{n}\\right)$$
$$=\\frac{d^2\\pmb{n}}{dt^2}-\\pmb{n} \
\\left(\\frac{d^2\\pmb{n}}{dt^2}\\cdot \\pmb{n}\\right)$$
$$=\\left(\\frac{d^2\\pmb{n}}{dt^2}\\right){}_{\\unicode{27c2}}$$
```

is simply the component of $$d^2\\pmb{n}/dt^2$$ *perpendicular* to $$\
\\pmb{n}$$ (i.e. component of $$d^2\\pmb{n}/dt^2$$ in the tangent \
plane of $$\\pmb{n}$$). Therefore,

```wl
$$I_t \\left(\\frac{d^2\\pmb{n}}{dt^2}\\right){}_{\\unicode{27c2}}=\\\
pmb{\\tau }\\times \\pmb{n}-\\frac{d\\pmb{n}}{dt}\\times \\pmb{S}.$$
```

### Magnetic Monopole

#### Electromagnetic Analogy

The motion of the spinning axis $$\\pmb{n}$$ (**spin dynamics**) can \
be interpreted as the motion of a *charged particle* on a *unit \
sphere* with an *magnetic monopole* inside (**charge dynamics**).

* Analogy: Compare the spin dynamics in Eq. (XXX) and the charge \
dynamics in Eq. (XXX)

```wl
$$\\begin{array}{rccccc}
 \\text{spin}: & I_t \\left(\\pmb{\\overset{\\ddot{ \
}}{\\pmb{n}}}\\right)_{\\unicode{27c2}} & = & \\pmb{\\tau }\\times \
\\pmb{n} & - & \\dot{\\pmb{n}}\\times \\pmb{S}
\\\\
 \\text{charge}: & m \\ddot{\\pmb{x}} & = & \\pmb{E} & + & \
\\dot{\\pmb{x}}\\times \\pmb{B} \\\\
\\end{array}$$

$$\\begin{array}{c|c}
 \\text{Spin} \\text{dynamics} & \\text{Charge} \\text{dynamics} \\\\
\\hline
 \\text{Spin} \\text{orientation}:\\pmb{n} & \\text{Charge} \
\\text{position}:\\pmb{x} \\\\
 \\text{Moment} \\text{of} \\text{inertia}:I_t & \\text{Mass} \
(\\text{interia}):m \\\\
 \\text{Torque}-\\text{induced} \\text{force}:\\pmb{\\tau }\\times \
\\pmb{n} & \\text{Electric} \\text{field}:\\pmb{E} \\\\
 \\text{Spin} \\text{angular} \\text{momentum}:-\\pmb{S} & \
\\text{Magnetic} \\text{field}:\\pmb{B} \\\\
\\end{array}$$
```

	* Similarity: Just as in electromagnetism, where the Lorentz force \
*deflects* a charge moving in a magnetic field, the spin-induced term \
$$-\\dot{\\pmb{n}}\\times \\pmb{S}$$ generates *precession* of the \
spinning axis.

```wl
In[616]:=
Block[{r = 0.8, d = 0.05, h = 1, a = 0.04, \[Theta] = \[Pi] / 6, \
\[Phi] =  - \[Pi] / 6, th = 0.02, c = 0.08, viewpt, dashedtube, rot}, \

	viewpt = {0,  - 2.4, 0.8};
	dashedtube[v_] := Tube[Table[{x v, (x + 0.05)v}, {x, 0, 0.9, 0.1}], \
th];
	rot[g_] := Rotate[Rotate[g, \[Theta], {1, 0, 0}, {0, 0, 0}], \[Phi], \
{0, 0, 1}, {0, 0, 0}];
	Graphics3D[{rot[Translate[{{EdgeForm[], Specularity[White, 5], Gray, \
Tube[{0, 0, #}& /@ { - h, h}, a], Opacity[0.8], Orange, Cylinder[{0, \
0, #}& /@ { - d, d}, r]}, {Red, Sphere[{0, 0, h}, c]}, \
(*{Black,Sphere[{0,0,-h},c]},*)Translate[{Arrowheads[0.04], {Blue, \
Arrow[Tube[{{0, 0, 0}, {0, 0, 1}}, th]], \
Text[\"\\!\\(\[VeryThinSpace]-**B** = **S**\\)\", {0, 0, 1}, {1.1, \
1}]}, {Red, Arrow[Tube[{{0, 0, 0}, {1, 0, 0}}, th]], \
Text[\"\\!\\(**x**\\&.=**n**\\&.\\)\", {1, 0, 0}, { - 0.7, 1}]}, \
{Purple, Arrow[Tube[{{0, 0, 0}, {0, 1, 0}}, th]], \
Text[\"\\!\\(**x**\\&.\[Times]**B**=-**n**\\&.\[Times]**S**\\)\", {0, \
1, 0}, { - 0.7,  - 0.5}]}, {Green, Arrow[Tube[{{0, 0, 0}, {0,  - 1, \
0}}, th]], Text[\"\\!\\(\[VeryThinSpace]**E** = **\[Tau]**\[Times]**n\
**\\)\", {0,  - 1, 0}, {1,  - 0.3}]}}, {0, 0, h}]}, {0, 0, h}]], \
{Opacity[0.1], Sphere[{0, 0, 0}, 2h]}, {{Glow[Gray], Black, \
dashedtube[{0, 0, 2h}], dashedtube[{0, 0,  - 2h}], dashedtube[2h{Sin[\
\[Phi]],  - Cos[\[Phi]], 0}], dashedtube[{2h, 0, 0}], dashedtube[{ - \
2h, 0, 0}], Tube[2h{Cos[#], Sin[#], 0}& /@ Range[0, 2\[Pi], \[Pi] / \
32], th], 
	Tube[2h{Cos[#]Sin[\[Theta]], Sin[#]Sin[\[Theta]], Cos[\[Theta]]}& /@ \
Range[0, 2\[Pi], \[Pi] / 32], th], Tube[2h{Sin[\[Phi]]Sin[#],  - Cos[\
\[Phi]]Sin[#], Cos[#]}& /@ Range[0, \[Pi], \[Pi] / 32], th], Block[{\
\[Beta] = \[Pi] / 2}, Tube[2h{Sin[\[Beta]]Sin[#],  - \
Cos[\[Beta]]Sin[#], Cos[#]}& /@ Range[0, 2\[Pi], \[Pi] / 32], \
th]]}}}, Boxed -> False, Lighting -> \"Neutral\", ViewPoint -> \
viewpt, ImageSize -> {Automatic, 160}]]

Out[616]=
\\!\\(\\*Graphics3DBox[{GeometricTransformation3DBox[\
GeometricTransformation3DBox[
    GeometricTransformation3DBox[{{GrayLevel[0.5], EdgeForm[None], \
Specularity[GrayLevel[1], 5], 
       TubeBox[{{0, 0, -1}, {0, 0, 1}}, 0.04], {RGBColor[1, 0.56, \
0.16], ... 62}, 
      {-0.942, 0, 1.763}, {-0.765, 0, 1.847}, 
      {-0.580, 0, 1.913}, {-0.390, 0, 1.961}, 
      {-0.196, 0, 1.990}, {0, 0, 2}}], 0.02]}}, Boxed -> False, 
 ImageSize -> {Automatic, 160}, Lighting -> \"Neutral\", ViewPoint -> \
{0, -2.4, 0.8}]\\)
```

	* Difference: The constraint to the sphere makes the coordinate \
system non-Euclidean (curved), in which \\[Del] operator is defined \
differently. [XXX]

```wl
In[681]:=
Block[{r = 0.8, d = 0.05, h = 1, a = 0.04, \[Theta] = \[Pi] / 5, \
\[Phi] =  - \[Pi] / 6, th = 0.02, c = 0.4, viewpt, dashedtube, rot}, 
	viewpt = {0,  - 2.4, 0.8};
	dashedtube[v_, sp_ : 0.1] := Tube[Table[{x v, (x + 0.05)v}, {x, 0, \
0.9, sp}], th];
	rot[g_] := Rotate[Rotate[g, \[Theta], {1, 0, 0}, {0, 0, 0}], \[Phi], \
{0, 0, 1}, {0, 0, 0}];
	Row[{Spacer[25], Graphics3D[{rot[Translate[{Arrowheads[0.04], \
{Black, Arrow[Tube[{{0, 0,  - h}, {0, 0, h}}, th]], Text[\"\
\\!\\(\[VeryThinSpace]**n**\\)\", {0, 0, h}, {0.7,  - 0.55}]}, \
Translate[{Black, Arrow[Tube[{{0, 0, 0}, {1, 0, 0}}, th]], \
Text[\"\\!\\(**e**\\_\[CurlyPhi]\\)\", {1, 0, 0}, { - 0., 0.8}], \
Arrow[Tube[{{0, 0, 0}, {0,  - 1, 0}}, th]], Text[\"\\!\\(**e\
**\\_\[Theta]\\)\", {0,  - 1, 0}, {1.2,  - 0.5}]}, {0, 0, h}]}, {0, \
0, h}]], {Opacity[0.1], Sphere[{0, 0, 0}, 2h]}, {{Glow[Gray], Black, \
dashedtube[{0, 0, 2h}], dashedtube[{0, 0,  - 2h}], \
Translate[dashedtube[2h Sin[\[Theta]]{Sin[\[Phi]],  - Cos[\[Phi]], \
0}, 0.2], 2h{0, 0, Cos[\[Theta]]}], dashedtube[2h{Sin[\[Phi]],  - \
Cos[\[Phi]], 0}], dashedtube[{2h, 0, 0}], dashedtube[{ - 2h, 0, 0}], \
Tube[2h{Cos[#], Sin[#], 0}& /@ Range[0, 2\[Pi], \[Pi] / 32], th], 
	Tube[2h{Cos[#]Sin[\[Theta]], Sin[#]Sin[\[Theta]], Cos[\[Theta]]}& /@ \
Range[0, 2\[Pi], \[Pi] / 32], th], Tube[2h{Sin[\[Phi]]Sin[#],  - Cos[\
\[Phi]]Sin[#], Cos[#]}& /@ Range[0, \[Pi], \[Pi] / 32], th], 
	Block[{\[Beta] = \[Pi] / 2}, Tube[2h{Sin[\[Beta]]Sin[#],  - Cos[\
\[Beta]]Sin[#], Cos[#]}& /@ Range[0, 2\[Pi], \[Pi] / 32], th]]}, \
{Glow[Black], Black, Tube[c{Sin[\[Phi]]Sin[#],  - Cos[\[Phi]]Sin[#], \
Cos[#]}& /@ Range[0, \[Theta], \[Pi] / 32], th], Text[\[Theta], \
1.6c{Sin[\[Phi]]Sin[\[Theta] / 2],  - Cos[\[Phi]]Sin[\[Theta] / 2], \
Cos[\[Theta] / 2]}], Tube[c{ - Cos[#],  - Sin[#], 0}& /@ Range[0, \
\[Pi] / 2 + \[Phi], \[Pi] / 32], th], Text[\[CurlyPhi],  - 1.6c{Cos[\
\[Pi] / 4 + \[Phi] / 2], Sin[\[Pi] / 4 + \[Phi] / 2], 0}]}}}, Boxed -> \
False, Lighting -> \"Neutral\", ViewPoint -> viewpt, ImageSize -> \
{Automatic, 136}]}]]

Out[681]=
\\!\\(\\*Graphics3DBox[{GeometricTransformation3DBox[\
GeometricTransformation3DBox[
    GeometricTransformation3DBox[{Arrowheads[0.04], {GrayLevel[0], 
       Arrow3DBox[TubeBox[{{0, 0, -1}, {0, 0, 1}}, 0.02]], 
       Text3DBox[FormBox[
         \"\\\"\\\\!\\ ...     {-0.253, -0.309, 0.}, {-0.222, -0.332, \

     0.}}, 0.02], \
Text3DBox[FormBox[\"\\\"\\\\!\\\\(\[CurlyPhi]\\\\)\\\"\", \
TraditionalForm], {-0.554, 
     -0.320, 0.}]}}}, Boxed -> False, Lighting -> \"Neutral\", 
 ViewPoint -> {0, -2.4, 0.8}, ImageSize -> {Automatic, 136}]\\)
```

		* **Spherical coordinate**: parametrize the spin axis

```wl
$$\\pmb{n}=(\\cos  \\varphi  \\sin  \\theta , \\sin  \\varphi  \\sin  \
\\theta , \\cos  \\theta ),$$
```

by the *polar angle* $$\\theta \\in [0,\\pi ]$$ and the *azimuthal \
angle* $$\\varphi \\in [0,2\\pi )$$.

		* **Unit vectors** :

```wl
$$\\pmb{e}^{\\theta }=(\\cos  \\varphi  \\cos  \\theta ,\\sin  \
\\varphi  \\cos  \\theta ,-\\sin  \\theta ),\\\\
\\pmb{e}^{\\varphi }=(-\\sin  \\varphi ,\\cos  \\varphi ,0).$$
```

		* **Surface gradient**: $$\\nabla _{\\unicode{27c2}}\\Phi$$ for a \
scalar field $$\\Phi$$,

```wl
$$\\nabla _{\\unicode{27c2}}\\Phi =\\pmb{e}^{\\theta }\\partial \
_{\\theta }\\Phi +\\pmb{e}^{\\varphi }\\frac{1}{\\sin  \\theta \
}\\partial _{\\varphi }\\Phi .$$
```

		* **Surface curl**: $$\\nabla _{\\unicode{27c2}}\\times \\pmb{A}$$ \
for a vector field $$\\pmb{A}=A_{\\theta }\\pmb{e}^{\\theta \
}+A_{\\varphi }\\pmb{e}^{\\varphi }$$,

```wl
$$\\nabla _{\\unicode{27c2}}\\times \\pmb{A}=\\frac{1}{\\sin  \\theta \
}\\left(\\partial _{\\theta }\\left(A_{\\varphi }\\sin  \\theta \
\\right)-\\partial _{\\varphi
}A_{\\theta }\\right)\\pmb{n}.$$
```

Wikipedia. [Del in cylindrical and spherical \
coordinates](https://en.wikipedia.org/wiki/Del_in_cylindrical_and_\
spherical_coordinates).

##### Differential Geometry for Vector Calculus

In **vector calculus**, we often compute *gradients*, *divergences*, \
*curls*, and integrals over curves, surfaces, or volumes. While \
powerful, these operations depend heavily on the *coordinate system* \
and *dimension*. **Differential geometry** provide a more *geometric* \
and *coordinate-free* language for calculus. They unify many familiar \
operations and extend naturally to curved spaces (manifolds).

* **Differential Forms**: differential form is the basic object in \
differential geometry, it is an object that you can *integrate* :

	* A **0-form** is just a *scalar* field $$f(x)$$, which can be \
integrated (evaluated) on a **point** $$x$$.

	* A **1-form** is a *vector* field (*line* element), like $$\\omega \
(x)=\\omega _i(x)dx^i$$, something you can integrate along a **curve**.

	* A **2-form** is an *tensor* field (oriented *surface* element), \
e.g. $$\\sigma _{i\\, j}(x)dx^i\\wedge dx^j$$, integrable over a \
**surface**.

In general:

	* A $$k$$**-form** is something you integrate over a \
$$k$$-dimensional submanifold.

	* The **wedge product** $$\\wedge$$ defines an oriented, \
antisymmetric product between forms:

```wl
$$dx^i\\wedge dx^j=-dx^j\\wedge dx^i.$$
```

* **Metric**: The metric defines how distance is measured on the \
manifold.

```wl
$$ds^2=g_{i\\, j}(x)dx^idx^j,$$
```

where

	* $$ds^2$$ is the squared infinitesimal distance element,

	* $$g_{i\\, j}(x)$$ are the components of the metric tensor, forming \
a symmetric positive-definite matrix.

	* $$dx^i$$ are the differential 1-form basis (cotangent basis)

* **Exterior Derivative**: the exterior derivative $$d$$ acts on \
differential forms to produce forms of higher degree. Given \
$$f=f_Idx^I$$,

```wl
$$df=\\partial _if_Idx^i\\wedge dx^I.$$
```

	* $$d^2=0$$: the exterior derivative of an exterior derivative is \
always zero.

	* **Stoke\[CloseCurlyQuote]s Theorem** :

```wl
$$\\int _{\\partial M}\\omega =\\int _Md\\omega .$$
```

* **Hodge Dual**: On an $$n$$-dimensional oriented manifold, the \
Hodge star operator $$\\star$$ maps $$k$$-forms to $$(n-k)$$-forms.

```wl
$$\\star \\left(dx^{i_1}\\wedge \\ldots \\wedge \
dx^{i_k}\\right)=\\frac{\\left| \\det \\left[g_{i\\, \
j}\\right]\\right| {}^{1/2}}{(n-k)!}g^{i_1j_1}\\ldots  \
g^{i_kj_k}\\epsilon
_{j_1\\ldots  j_n}dx^{j_{k+1}}\\wedge \\ldots \\wedge dx^{j_n},$$
```

where

	* $$\\epsilon _{j_1\\ldots  j_n}$$ is the **Levi-Civita symbol**,

	* $$g^{i\\, j}=\\left\\langle dx^i,dx^j\\right\\rangle$$ is the \
**inverse metric**, which tells how differential forms $$dx^i$$ and \
$$dx^j$$are \[OpenCurlyDoubleQuote]angled\[CloseCurlyDoubleQuote] \
with respect to each other.

Exterior derivative and Hodge dual enable us to represent **vector \
calculus operators** in terms of differential forms in a unified \
manner.

```wl
$$\\begin{array}{cc}
 \\text{Vector} \\text{Calculus} & \\text{Differetial} \\text{Forms} \
\\\\
\\hline
 \\text{grad} (\\nabla f) & df \\\\
 \\text{curl} (\\nabla \\times \\pmb{\\omega }) & \\star d\\omega  \\\\
 \\text{div} (\\nabla \\cdot \\pmb{\\omega }) & \\star d\\star \
\\omega  \\\\
 \\text{Laplacian} \\left(\\nabla ^2f\\right) & \\star d\\star df \
\\\\
\\end{array}$$
```

See Refs. [XXX] for more details of the above concepts.

Application in spherical coordinates on $$S^2$$.

* **Metric**: the distance element is given by

```wl
$$ds^2=d\\theta ^2+\\sin ^2\\theta  d\\varphi ^2,$$
```

which implies

```wl
$$g_{i\\, j}=\\left(
\\begin{array}{cc}
 1 & 0 \\\\
 0 & \\sin ^2\\theta  \\\\
\\end{array}
\\right),g^{i\\, j}=\\left(
\\begin{array}{cc}
 1 & 0 \\\\
 0 & \\sin ^{-2}\\theta  \\\\
\\end{array}
\\right),$$
```

and $$\\left| \\det \\left[g_{i\\, j}\\right]\\right| {}^{1/2}=\\sin  \
\\theta$$.

* **Unit (co)vectors**: orthonormal basis of 1-forms

```wl
$$\\pmb{e}^{\\theta }\\leftrightarrow \\sqrt{g_{\\theta \\, \\theta \
}}d\\theta =d\\theta , \\\\
\\pmb{e}^{\\varphi }\\leftrightarrow \\sqrt{g_{\\varphi \\, \\varphi \
}}d\\varphi =\\sin  \\theta  d\\varphi .$$
```

This enables us to represent any *vector* field as *1-form* field, \
such as

```wl
$$\\pmb{A}=A_{\\theta }\\pmb{e}^{\\theta }+A_{\\varphi \
}\\pmb{e}^{\\varphi }\\leftrightarrow A=A_{\\theta }d\\theta \
+A_{\\varphi }\\sin  \\theta  d\\varphi .$$
```

* **Gradient**: given a scalar field $$\\Phi$$,

```wl
$$\\text{grad} \\Phi =\\pmb{e}^{\\theta } \\partial _{\\theta }\\Phi \
+\\pmb{e}^{\\varphi }\\frac{1}{\\sin  \\theta }\\partial _{\\varphi }\
\\Phi .$$
```

Derive Eq. (XXX) using differential geometry approach.

```wl
$$\\text{grad} \\Phi \\leftrightarrow d\\Phi =d\\theta  \\partial \
_{\\theta }\\Phi +d\\varphi  \\partial _{\\varphi }\\Phi \
\\leftrightarrow \\pmb{e}^{\\theta }
\\partial _{\\theta }\\Phi +\\pmb{e}^{\\varphi }\\frac{1}{\\sin  \
\\theta }\\partial _{\\varphi }\\Phi .$$
```

* **Curl**: given a vector field $$\\pmb{A}=A_{\\theta \
}\\pmb{e}^{\\theta }+A_{\\varphi }\\pmb{e}^{\\varphi }$$,

```wl
$$\\text{curl} \\pmb{A}=\\frac{1}{\\sin  \\theta }\\left(\\partial _{\
\\theta }\\left(A_{\\varphi }\\sin  \\theta \\right)-\\partial \
_{\\varphi }A_{\\theta }\\right)\\pmb{n}.$$
```

Derive Eq. (XXX) using differential geometry approach.

```wl
$$\\text{curl} \\pmb{A}\\leftrightarrow \\star dA=\\star \
d\\left(A_{\\theta }d\\theta +A_{\\varphi }\\sin  \\theta  d\\varphi \
\\right)$$
$$=\\star \\left(\\partial _{\\varphi }A_{\\theta }d\\varphi \\wedge \
d\\theta +\\partial _{\\theta }\\left(A_{\\varphi }\\sin  \\theta \
\\right)d\\theta \\wedge d\\varphi
\\right)$$
$$=\\left(\\partial _{\\theta }\\left(A_{\\varphi }\\sin  \\theta \
\\right)-\\partial _{\\varphi }A_{\\theta }\\right)\\star (d\\theta \
\\wedge d\\varphi )$$
$$=\\frac{1}{\\sin  \\theta }\\left(\\partial _{\\theta \
}\\left(A_{\\varphi }\\sin  \\theta \\right)-\\partial _{\\varphi \
}A_{\\theta }\\right).$$
```

The result is a 0-form, indicating a scalar field on the sphere. But \
alternatively, we may as well view it as a vector field along the \
*normal* direction of the sphere,

```wl
$$\\text{curl} \\pmb{A}=\\frac{1}{\\sin  \\theta }\\left(\\partial _{\
\\theta }\\left(A_{\\varphi }\\sin  \\theta \\right)-\\partial \
_{\\varphi }A_{\\theta }\\right)\\pmb{n}.$$
```

* **Divergence**: given a vector field $$\\pmb{A}=A_{\\theta \
}\\pmb{e}^{\\theta }+A_{\\varphi }\\pmb{e}^{\\varphi }$$,

```wl
$$\\text{div} \\pmb{A}=\\frac{1}{\\sin  \\theta }\\left(\\partial \
_{\\theta }\\left(A_{\\theta } \\sin  \\theta \\right)+\\partial \
_{\\varphi }A_{\\varphi }\\right).$$
```

Derive Eq. (XXX) using differential geometry approach.

```wl
$$\\text{div} \\pmb{A}\\leftrightarrow \\star d\\star \\, A=\\star \
d\\star \\left(A_{\\theta }d\\theta +A_{\\varphi }\\sin  \\theta  \
d\\varphi \\right)$$
$$=\\star d\\left(A_{\\theta } (\\sin  \\theta d\\varphi \
)+A_{\\varphi }\\sin  \\theta  \\left(-\\frac{1}{\\sin  \\theta \
}d\\theta \\right)\\right)$$
$$=\\star d\\left(A_{\\theta } \\sin  \\theta d\\varphi -A_{\\varphi \
}d\\theta \\right)$$
$$=\\star \\left(\\partial _{\\theta }\\left(A_{\\theta } \\sin  \
\\theta \\right)d\\theta \\wedge d\\varphi -\\partial _{\\varphi }A_{\
\\varphi }d\\varphi \\wedge
d\\theta \\right)$$
$$=\\left(\\partial _{\\theta }\\left(A_{\\theta } \\sin  \\theta \
\\right)+\\partial _{\\varphi }A_{\\varphi }\\right)\\star (d\\theta \
\\wedge d\\varphi )$$
$$=\\frac{1}{\\sin  \\theta }\\left(\\partial _{\\theta \
}\\left(A_{\\theta } \\sin  \\theta \\right)+\\partial _{\\varphi \
}A_{\\varphi }\\right).$$
```

* **Laplacian**: given a scalar field $$\\psi$$,

```wl
$$\\nabla ^2\\psi =\\frac{1}{\\sin  \\theta }\\partial _{\\theta \
}\\left(\\sin  \\theta  \\partial _{\\theta }\\psi \
\\right)+\\frac{1}{\\sin ^2\\theta }\\partial _{\\varphi
}^2\\psi .$$
```

Derive Eq. (XXX) using differential geometry approach.

For zero-form (scalar) field, $$\\nabla ^2=\\star d\\star d$$, thus

```wl
$$\\nabla ^2\\psi \\leftrightarrow \\star d\\star d\\psi$$
$$=\\star d\\star \\left(d\\theta \\partial _{\\theta }\\psi \
+d\\varphi \\partial _{\\varphi }\\psi \\right)$$
$$=\\star d\\left(\\partial _{\\theta }\\psi  (\\sin  \\theta \
d\\varphi )+\\partial _{\\varphi }\\psi \\left(-\\frac{1}{\\sin  \
\\theta }d\\theta \\right)\\right)$$
$$=\\star d\\left(\\sin  \\theta  \\partial _{\\theta }\\psi  \
d\\varphi -\\frac{1}{\\sin  \\theta }\\partial _{\\varphi }\\psi \
d\\theta \\right)$$
$$=\\star \\left(\\partial _{\\theta }\\left(\\sin  \\theta  \
\\partial _{\\theta }\\psi \\right)d\\theta \\wedge d\\varphi \
-\\frac{1}{\\sin  \\theta }\\partial _{\\varphi
}^2\\psi d\\varphi \\wedge d\\theta \\right)$$
$$=\\left(\\partial _{\\theta }\\left(\\sin  \\theta  \\partial \
_{\\theta }\\psi \\right)+\\frac{1}{\\sin  \\theta }\\partial \
_{\\varphi }^2\\psi \\right)\\star (d\\theta
\\wedge d\\varphi )$$
$$=\\frac{1}{\\sin  \\theta }\\left(\\partial _{\\theta }\\left(\\sin \
 \\theta  \\partial _{\\theta }\\psi \\right)+\\frac{1}{\\sin  \
\\theta }\\partial _{\\varphi
}^2\\psi \\right).$$
```

Vincent Bouchard. [MATH 315: Calculus \
IV](https://sites.ualberta.ca/~vbouchar/MATH315/notes.html) \
(University of Alberta).

#### Effective Gauge Field

Introduce the effective gauge field $$(\\Phi ,\\pmb{A})$$ on the \
sphere, such that

* Effective **electric field** :

```wl
$$\\pmb{E}(\\pmb{n})=-\\nabla _{\\unicode{27c2}}\\Phi (\\pmb{n}).$$
```

In this way, $$\\pmb{E}$$ is guaranteed to lie in the tangent plane, \
the same as the torque-induced force $$\\pmb{\\tau }\\times \\pmb{n}$$.

```wl
In[834]:=
Block[{d\[Theta] = \[Pi] / 8, d\[Phi] = \[Pi] / 6, \[Theta]s, \
\[Phi]s, cfun}, 
	\[Theta]s = Range[d\[Theta], \[Pi] - d\[Theta], d\[Theta]];
	\[Phi]s = Range[d\[Phi], 2\[Pi], d\[Phi]];
	cfun = ColorData[\"RedBlueTones\"];
	Row[{Show[{SphericalPlot3D[1, {\[Theta], 0, \[Pi]}, {\[Phi], 0, 2\
\[Pi]}, Mesh -> {\[Theta]s, \[Phi]s}, Axes -> False, Boxed -> False, \
ColorFunction -> (cfun[#3]&), MeshStyle -> Directive[Black, \
AbsoluteThickness[0.8], Opacity[0.4]], Lighting -> \"Neutral\", \
ViewPoint -> {0,  - 2.4, 0.8}], Graphics3D[{{Glow[Black], Black, \
Arrowheads[0.04], Function[{\[Theta], \[Phi]}, \
Translate[Arrow[Tube[{{0, 0, 0}, 0.35Sin[\[Theta]]{Cos[\[Phi]]Cos[\
\[Theta]], Sin[\[Phi]]Cos[\[Theta]],  - Sin[\[Theta]]}}, 0.015]], \
{Cos[\[Phi]]Sin[\[Theta]], Sin[\[Phi]]Sin[\[Theta]], \
Cos[\[Theta]]}]]@@@Tuples[N@{\[Theta]s, \[Phi]s}]}, {Black, \
Text[Style[\"\\!\\(\[VeryThinSpace]**E**\\)\", \"Text\"], { - 1, 0, \
0}, {2,  - 0.5}]}}, Lighting -> \"Neutral\"]}, PlotRange -> All, \
ImageSize -> 125], Graphics[Raster[List /@ Range[0, 1, 0.02], \
ColorFunction -> cfun], PlotLabel -> Style[\[CapitalPhi], Black, \
\"Text\"], AspectRatio -> 8, ImageSize -> {Automatic, 80}]}]]

Out[834]=
\\!\\(\\*Graphics3DBox[«2»]\\)\\!\\(\\*GraphicsBox[RasterBox[{{0.}, \
{0.02}, {0.04}, {0.06}, {0.08}, {0.1}, {0.12}, {0.14}, {0.16}, {0.18}, 
  {0.2}, {0.22}, {0.24}, {0.26}, {0.28}, {0.3}, {0.32}, {0.34}, \
{0.36}, {0.38}, {0.4}, {0.42}, 
  {0.44}, {0.46}, {0. ... Function[\"RedBlueTones\", \"Gradients\", \
{0, 1}, 
    Blend[\"RedBlueTones\", #1] & ]], 
 PlotLabel -> FormBox[StyleBox[\"\\\"\\\\!\\\\(\[CapitalPhi]\\\\)\\\"\
\", GrayLevel[0], \"Text\", StripOnInput -> False], 
   TraditionalForm], AspectRatio -> 8, ImageSize -> {Automatic, 80}]\\)
```

Example: a spinning top in a uniform gravity field $$\\Phi (\\pmb{n})\
\\propto n_z=\\cos  \\theta$$,

```wl
$$\\pmb{E}=-\\nabla _{\\unicode{27c2}}\\Phi =\\pmb{e}_{\\theta }\\sin \
 \\theta .$$
```

* Effective **magnetic field** :

```wl
$$\\pmb{B}(\\pmb{n})=-S \\pmb{n}=\\nabla _{\\unicode{27c2}}\\times \
\\pmb{A}(\\pmb{n}).$$
```

where $$S=I_a\\omega$$ is the spin angular momentum (magnitude). The \
magnetic field points towards the origin, where there is effective an \
**magnetic monopole**.

```wl
In[835]:=
Block[{th = 0.014, dashedtube}, 
	dashedtube[v_, sp_ : 0.1] := Tube[Table[{x v, (x + 0.05)v}, {x, 0, \
0.9, sp}], th];Graphics3D[{{Opacity[0.5], White, Sphere[{0, 0, 0}, \
1]}, {Blue, Sphere[{0, 0, 0}, 0.1], Arrowheads[0.035], Table[Block[{\
\[Theta], \[Phi]}, \[Theta] = ArcCos[1 - 2x];\[Phi] = \
20\[Theta];Arrow[Tube[{Sin[\[Theta]]Cos[\[Phi]], Sin[\[Theta]]Sin[\
\[Phi]], Cos[\[Theta]]}#& /@ {1.02, 1.25}, 0.015]]], {x, 0, 1, \
0.01}], Text[\"\\!\\(-**B**\\)\", {0,  - 1, 1}]}, Block[{\[Theta] = \
\[Pi] / 4}, {{Black, dashedtube[{0, 0, 1}], dashedtube[{0, Sin[\
\[Theta]], Cos[\[Theta]]}], Translate[dashedtube[{0, Sin[\[Theta]], \
0}, 0.15], {0, 0, Cos[\[Theta]]}], Tube[0.2{0, Sin[#], Cos[#]}& /@ \
Range[0, \[Theta], \[Pi] / 32], th], Text[\[Theta], {0, 0.3, 0.1}], \
Text[sin\[Theta], {0, 0.3, 0.8}]}, {Red, Arrowheads[{0.04, # + 0.01}& \
/@ (Range[0, 5] / 6)], Arrow[Tube[Table[{Sin[\[Theta]]Cos[\[Phi]], \
Sin[\[Theta]]Sin[\[Phi]], Cos[\[Theta]]}, {\[Phi], 0, 2\[Pi], \[Pi] / \
32}], th]]}}]}, Boxed -> False, Lighting -> \"Neutral\", ViewPoint -> \
{5, 0, 2}, ImageSize -> 140]]

Out[835]=
\\!\\(\\*Graphics3DBox[{{GrayLevel[1], Opacity[0.5], SphereBox[{0, 0, \
0}, 1]}, 
  {RGBColor[0, 0.45, 0.9], SphereBox[{0, 0, 0}, 0.1], \
{Arrowheads[0.035], 
    {Arrow3DBox[TubeBox[{{0., 0., 1.02}, {0., 0., 1.25}}, 0.015]], 
     Arrow3DBox[TubeBox[{{-0.1 ... 07}, {0.653, -0.270, 
        0.707}, {0.676, -0.205, 0.707}, 
        {0.693, -0.137, 0.707}, {0.703, 
        -0.069, 0.707}, {0.707, 0, 0.707}}], 
      0.014]]}}}, Boxed -> False, ImageSize -> 140, Lighting -> \
\"Neutral\", ViewPoint -> {5, 0, 2}]\\)
```

One common choice of vector potential A (n) to produce such magnetic \
field is the Wu-Yang monopole potential [XXX]

```wl
$$\\pmb{A}(\\pmb{n})=S \\frac{\\cos  \\theta -1}{\\sin  \\theta \
}\\pmb{e}_{\\varphi }$$
```

Verify that A (n) given in Eq. (XXX) satisfies Eq. (XXX).

Given Eq. (XXX), compared with A = Subscript[A, \\[Theta]] \
Subscript[e, \\[Theta]] + 
  Subscript[A, \\[CurlyPhi]] Subscript[e, \\[CurlyPhi]],

```wl
$$A_{\\theta }=0,A_{\\varphi }=S \\frac{\\cos  \\theta -1}{\\sin  \
\\theta }.$$
```

According to Eq. (XXX),

```wl
$$\\nabla _{\\unicode{27c2}}\\times \\pmb{A}=\\frac{1}{\\sin  \\theta \
}\\left(\\partial _{\\theta }\\left(A_{\\varphi }\\sin  \\theta \
\\right)-\\partial _{\\varphi
}A_{\\theta }\\right)\\pmb{n}$$
$$=\\frac{1}{\\sin  \\theta }\\partial _{\\theta }\\left(S \
\\frac{\\cos  \\theta -1}{\\sin  \\theta }\\sin  \\theta \
\\right)\\pmb{n}$$
$$=\\frac{S}{\\sin  \\theta }\\partial _{\\theta }(\\cos  \\theta -1)\
\\pmb{n}$$
$$=\\frac{-\\sin  \\theta }{\\sin  \\theta }S \\pmb{n}$$
$$=-S \\pmb{n}.$$
```

	* As a simple justification, along a *latitude loop* at the polar \
angle $$\\theta$$, the loop integral of the vector potential is

```wl
$$\\oint \\pmb{A}\\cdot d\\pmb{l}=\\int S \\frac{\\cos  \\theta \
-1}{\\sin  \\theta }\\sin  \\theta d\\varphi =2\\pi  S (\\cos  \
\\theta -1),$$
```

which indeed equals to the *magnetic flux* through the *spherical \
cap* from the north pole down to angle $$\\theta$$

```wl
$$\\int \\pmb{B}\\cdot d\\pmb{\\sigma }=-S \\Omega (\\theta )=-2\\pi  \
S (1-\\cos  \\theta ),$$
```

where $$\\Omega (\\theta )=2\\pi  (1-\\cos  \\theta )$$ denotes the \
*solid angle* of the cap.

	* However, as $$\\theta \\text{-$>$}\\pi$$ near the south pole, \
$$A_{\\varphi }\\rightarrow \\infty$$ diverges. What is going wrong?

T. T. Wu, C. N. Yang. [Dirac monopole without strings: monopole \
harmonics](https://wucj.lab.westlake.edu.cn/teach/CNYang/Lec7_wu1976.\
pdf). Nuclear Physics B107 365-380 (1976).

#### Quantization of Spin (or Monopole)

The divergence of $$A_{\\varphi }$$ is due to the requirement that an \
*infinitesimal latitude loop* near the south pole ($$\\theta \
\\text{-$>$}\\pi$$) must accumulate a finite amount of **Berry phase** \
set by the *total magnetic flux* through the sphere

```wl
$$\\Theta =\\frac{1}{\\hbar }\\oint \\pmb{A}\\cdot d\\pmb{l}=\\frac{2\
\\pi }{\\hbar } \\sin  \\theta  A_{\\varphi }=\\frac{4\\pi  B}{\\hbar \
}=-\\frac{4\\pi  S}{\\hbar
}.$$
```

The divergence can not be avoid, unless \[Ellipsis] $$\\Theta$$ is \
actually *equivalent* to 0, i.e.

```wl
$$\\Theta =2\\pi  n,$$
```

with $$n\\in \\mathbb{Z}$$.

* Therefore, it is only possible to avoid singular assignment of \
$$\\pmb{A}(\\pmb{n})$$ if the **spin angular momentum** $$S$$ is \
*quantized* to

```wl
$$S=\\frac{\\hbar }{2}n,$$
```

with $$n=0,1,2,\\ldots$$.

* This is also a statement about the **magnetic monopole**, that the \
**total magnetic flux** emitted by a magnetic monopole must be \
quantized to

```wl
$$\\phi _B=4\\pi  B=-2 \\pi  \\hbar  n.$$
```

Mathematically, the singularity is avoided by using two overlapping \
coordinate patches (north and south hemispheres) with smooth gauge \
fields on each.

* On the **northern hemisphere** ($$\\theta \\in [0,\\pi /2]$$, \
excluding the south pole):

```wl
$$\\pmb{A}_N(\\pmb{n})=S \\frac{\\cos  \\theta -1}{\\sin  \\theta \
}\\pmb{e}_{\\varphi }.$$
```

* On the **southern hemisphere** ($$\\theta \\in [\\pi /2,\\pi ]$$, \
excluding the north pole):

```wl
$$\\pmb{A}_S(\\pmb{n})=S \\frac{\\cos  \\theta +1}{\\sin  \\theta \
}\\pmb{e}_{\\varphi }.$$
```

* On the **equator** ($$\\theta =\\pi /2$$) where both patches \
overlap, the two gauge potentials are related by a **gauge \
transformation** :

```wl
$$\\pmb{A}_N(\\varphi )-\\pmb{A}_S(\\varphi )=\\hbar  \
\\pmb{e}_{\\varphi }\\partial _{\\varphi }\\chi (\\varphi ),$$
```

with $$\\chi (\\varphi )=-2(S/\\hbar ) \\varphi$$.

Since $$\\varphi$$ and $$\\varphi +2\\pi$$ correspond to the *same* \
point on the equator, the gauge transformation $$\\psi (\\varphi \
)\\rightarrow e^{i \\chi (\\varphi )}\\psi (\\varphi )$$ is only \
consistent if

```wl
$$e^{i \\chi (\\varphi )}=e^{i \\chi (\\varphi +2\\pi )}$$


$$\\Rightarrow \\exp (-i 2(S/\\hbar ) \\varphi )=\\exp (-i 2(S/\\hbar \
) (\\varphi +2\\pi ))$$
```

which requires

```wl
$$\\frac{2S}{\\hbar }\\in \\mathbb{Z},$$
```

reproducing the spin quantization condition in Eq. (XXX).

### Quantum Spin

#### Hamiltonian

Consider the spherical symmetric case, where there is no external \
scalar potential \\[CapitalPhi](n) = 0. Similar to Eq. (XXX), the \
quantum dynamics of a spin is described by the Hamiltonian

```wl
$$\\hat{H}=-\\frac{\\hbar \
^2}{2I_t}\\pmb{D}_{\\unicode{27c2}}^2+\\frac{S^2}{2I_a}.$$
```

* $$I_t=m$$ - the *transverse ***moment of inertia** of the spin,

* $$\\pmb{D}_{\\unicode{27c2}}$$ - **surface ****covariant \
derivative**,  along tangent directions on the sphere,

```wl
$$\\pmb{D}_{\\unicode{27c2}}=\\nabla \
_{\\unicode{27c2}}-\\frac{i}{\\hbar }\\pmb{A},$$
```

	* $$\\nabla _{\\unicode{27c2}}=\\pmb{e}^{\\theta }\\partial \
_{\\theta }+\\pmb{e}^{\\varphi }\\frac{1}{\\sin  \\theta }\\partial \
_{\\varphi }$$ - **surface gradient**,

	* $$\\pmb{A}=A_{\\theta }\\pmb{e}^{\\theta }+A_{\\varphi }\\pmb{e}^{\
\\varphi }$$ - **gauge connection** (vector potential) on the sphere. \
Take the Wu-Yang monopole potential:

```wl
$$A_{\\theta }=0,A_{\\varphi }=S \\frac{\\cos  \\theta -1}{\\sin  \
\\theta },$$
```

with the quantization condition ($$n\\in \\mathbb{N}$$),

```wl
$$S=\\hbar  s=\\hbar \\frac{n}{2},$$
```

where $$s=n/2$$ is introduced as the** spin quantum number** \
(quantized to half integers), also characterizing the *monopole \
strength*.

In spherical coordinate, the Hamiltonian acts on the wave function $$\
\\psi (\\theta ,\\varphi )$$ as

```wl
$$\\pmb{D}_{\\unicode{27c2}}^2\\psi =\\frac{1}{\\sin  \\theta \
}\\left(\\partial _{\\theta }\\left(\\sin  \\theta  \\partial \
_{\\theta }\\right)+\\frac{1}{\\sin  \\theta
}\\left(\\partial _{\\varphi }+i s (1-\\cos  \\theta \
)\\right){}^2\\right)\\psi .$$
```

Derive Eq. (XXX) using differential geometry approach.

As a vector field, the vector potential takes the form of A = \
Subscript[A, \\[CurlyPhi]] e^\\[CurlyPhi] (given that Subscript[A, \
\\[Theta]] = 0 for Wu-Yang monopole potential). To use differential \
geometry, we first convert that vector potential to a 1-form by the \
correspondence e^\\[CurlyPhi] = sin \\[Theta] \
\\[DifferentialD]\\[CurlyPhi] in Eq. (XXX)

```wl
$$A=A_{\\varphi }\\sin  \\theta d\\varphi .$$
```

The surface covariant derivative amounts to

```wl
$$\\pmb{D}_{\\unicode{27c2}}\\rightarrow D=d-\\frac{i}{\\hbar \
}A=d-\\frac{i A_{\\varphi }}{\\hbar }\\sin  \\theta d\\varphi .$$
```

Similar to Eq. (XXX), the covariant Laplacian operator reads

```wl
$$\\pmb{D}_{\\unicode{27c2}}^2\\psi =\\star \\, D\\, \\star \\, D \
\\psi$$
$$=\\star \\, D\\, \\star \\, \\left(d\\psi -\\frac{i A_{\\varphi }}{\
\\hbar }\\sin  \\theta  \\psi d\\varphi \\right)$$
$$=\\star \\, D\\, \\star \\, \\left(\\partial _{\\theta }\\psi \
d\\theta +\\left(\\partial _{\\varphi }\\psi -\\frac{i A_{\\varphi \
}}{\\hbar }\\sin  \\theta  \\psi \\right)d\\varphi
\\right)$$
$$=\\star \\, D\\, \\left(\\sin  \\theta  \\partial _{\\theta }\\psi \
d\\varphi -\\frac{1}{\\sin  \\theta }\\left(\\partial _{\\varphi \
}-\\frac{i A_{\\varphi }}{\\hbar
}\\sin  \\theta \\right)\\psi d\\theta \\right)$$
$$=\\star \\, \\left(d-\\frac{i A_{\\varphi }}{\\hbar }\\sin  \\theta \
d\\varphi \\right)\\left(\\sin  \\theta  \\partial _{\\theta }\\psi d\
\\varphi -\\frac{1}{\\sin
 \\theta }\\left(\\partial _{\\varphi }-\\frac{i A_{\\varphi \
}}{\\hbar }\\sin  \\theta \\right)\\psi d\\theta \\right)$$
$$=\\star \\, \\left(\\partial _{\\theta }\\left(\\sin  \\theta  \
\\partial _{\\theta }\\psi \\right)d\\theta \\wedge d\\varphi \
-\\frac{1}{\\sin  \\theta }\\left(\\partial
_{\\varphi }-\\frac{i A_{\\varphi }}{\\hbar }\\sin  \\theta \
\\right)\\left(\\partial _{\\varphi }-\\frac{i A_{\\varphi }}{\\hbar \
}\\sin  \\theta \\right)\\psi d\\varphi
\\wedge d\\theta \\right)$$
$$=\\star \\, \\left(\\partial _{\\theta }\\left(\\sin  \\theta  \
\\partial _{\\theta }\\psi \\right)+\\frac{1}{\\sin  \\theta }\\left(\
\\partial _{\\varphi }-\\frac{i
A_{\\varphi }}{\\hbar }\\sin  \\theta \\right){}^2\\psi \
\\right)d\\theta \\wedge d\\varphi$$
$$=\\frac{1}{\\sin  \\theta }\\left(\\partial _{\\theta }\\left(\\sin \
 \\theta  \\partial _{\\theta }\\psi \\right)+\\frac{1}{\\sin  \
\\theta }\\left(\\partial _{\\varphi
}-\\frac{i A_{\\varphi }}{\\hbar }\\sin  \\theta \\right){}^2\\psi \
\\right)$$
$$=\\frac{1}{\\sin  \\theta }\\left(\\partial _{\\theta }\\left(\\sin \
 \\theta  \\partial _{\\theta }\\right)+\\frac{1}{\\sin  \\theta \
}\\left(\\partial _{\\varphi
}-\\frac{i A_{\\varphi }}{\\hbar }\\sin  \\theta \\right){}^2\\right)\
\\psi .$$
```

Given Subscript[A, \\[CurlyPhi]] = S (cos \\[Theta] - 1)/(sin \
\\[Theta]) in Eq. (XXX),

```wl
$$\\pmb{D}_{\\unicode{27c2}}^2\\psi =\\frac{1}{\\sin  \\theta \
}\\left(\\partial _{\\theta }\\left(\\sin  \\theta  \\partial \
_{\\theta }\\right)+\\frac{1}{\\sin  \\theta
}\\left(\\partial _{\\varphi }-\\frac{i A_{\\varphi }}{\\hbar }\\sin  \
\\theta \\right){}^2\\right)\\psi$$
$$=\\frac{1}{\\sin  \\theta }\\left(\\partial _{\\theta }\\left(\\sin \
 \\theta  \\partial _{\\theta }\\right)+\\frac{1}{\\sin  \\theta \
}\\left(\\partial _{\\varphi
}-\\frac{i S}{\\hbar }(\\cos  \\theta -1)\\right){}^2\\right)\\psi \
.$$
```

Parametrize the spin angular momentum as $$S=\\hbar  s$$, we have

```wl
$$\\pmb{D}_{\\unicode{27c2}}^2\\psi =\\frac{1}{\\sin  \\theta \
}\\left(\\partial _{\\theta }\\left(\\sin  \\theta  \\partial \
_{\\theta }\\right)+\\frac{1}{\\sin  \\theta
}\\left(\\partial _{\\varphi }+i s (1-\\cos  \\theta \
)\\right){}^2\\right)\\psi .$$
```

#### Schrödinger Equation

Solve the stationary **Schrödinger equation**:

```wl
$$\\hat{H}\\psi (\\theta ,\\varphi )=E \\psi (\\theta ,\\varphi ).$$
```

* Separation of variables: let

```wl
$$\\psi (\\theta ,\\varphi )=e^{i (m-s) \\varphi }\\psi (\\theta ),$$
```

Eq. (XXX) takes the form of the generalized associated Legendre \
differential equation

```wl
$$\\left(\\frac{1}{\\sin  \\theta }\\partial _{\\theta }\\left(\\sin  \
\\theta  \\partial _{\\theta }\\right)-\\frac{1}{\\sin ^2 \\theta \
}(m-s \\cos  \\theta )^2+\\lambda
\\right)\\psi (\\theta )=0$$
```

where the eigenvalue \[Lambda] is related to the energy $$E$$ by

```wl
$$E=\\frac{\\hbar ^2}{2I_t}\\lambda +\\frac{\\hbar ^2}{2I_a}s^2.$$
```

Justify Eq. (XXX) and Eq. (XXX).

Given 
\\!\\(\\*OverscriptBox[\\(H\\), \\(^\\)]\\) in Eq. (XXX),

```wl
$$\\hat{H}\\psi (\\theta ,\\varphi )=\\left(\\frac{1}{2I_t}\\left(-i \
\\hbar  \\pmb{D}_{\\unicode{27c2}}\\right){}^2+\\frac{S^2}{2I_a}\\\
right)\\psi (\\theta ,\\varphi
)$$
$$=-\\frac{\\hbar ^2}{2I_t}\\pmb{D}_{\\unicode{27c2}}^2\\psi (\\theta \
,\\varphi )+\\frac{\\hbar ^2s^2}{2I_a}\\psi (\\theta ,\\varphi ).$$
```

By Eq. (XXX) and using the ansatz in Eq. (XXX), \\!\\(\\*
SubsuperscriptBox[
StyleBox[\"D\",
FontWeight->\"Bold\"], \"\\[Perpendicular]\", 
  \"2\"] \\(\\[Psi](\\[Theta], \\[CurlyPhi])\\)\\) reads

```wl
$$\\pmb{D}_{\\unicode{27c2}}^2\\psi (\\theta ,\\varphi \
)=\\pmb{D}_{\\unicode{27c2}}^2e^{i (m-s) \\varphi }\\psi (\\theta )$$
$$=\\left(\\frac{1}{\\sin  \\theta }\\partial _{\\theta }\\left(\\sin \
 \\theta  \\partial _{\\theta }\\right)+\\frac{1}{\\sin ^2 \\theta \
}\\left(\\partial _{\\varphi
}+i s (1-\\cos  \\theta )\\right){}^2\\right)e^{i (m-s) \\varphi \
}\\psi (\\theta )$$
$$=e^{i (m-s) \\varphi }\\left(\\frac{1}{\\sin  \\theta }\\partial _{\
\\theta }\\left(\\sin  \\theta  \\partial _{\\theta \
}\\right)+\\frac{1}{\\sin ^2 \\theta }(i(m-s)+i
s (1-\\cos  \\theta ))^2\\right)\\psi (\\theta )$$
$$=e^{i (m-s) \\varphi }\\left(\\frac{1}{\\sin  \\theta }\\partial _{\
\\theta }\\left(\\sin  \\theta  \\partial _{\\theta \
}\\right)-\\frac{1}{\\sin ^2 \\theta }(m-s+s-s
\\cos  \\theta )^2\\right)\\psi (\\theta )$$
$$=e^{i (m-s) \\varphi }\\left(\\frac{1}{\\sin  \\theta }\\partial _{\
\\theta }\\left(\\sin  \\theta  \\partial _{\\theta \
}\\right)-\\frac{1}{\\sin ^2 \\theta }(m-s
\\cos  \\theta )^2\\right)\\psi (\\theta ).$$
```

Assuming \\[Psi](\\[Theta]) is an eigen solution of Eq. (XXX),

```wl
$$\\left(\\frac{1}{\\sin  \\theta }\\partial _{\\theta }\\left(\\sin  \
\\theta  \\partial _{\\theta }\\right)-\\frac{1}{\\sin ^2 \\theta \
}(m-s \\cos  \\theta )^2\\right)\\psi
(\\theta )=-\\lambda  \\psi (\\theta ),$$
```

thus,

```wl
$$\\pmb{D}_{\\unicode{27c2}}^2\\psi (\\theta ,\\varphi )=e^{i (m-s) \
\\varphi }(-\\lambda )\\psi (\\theta )$$
$$=-\\lambda e^{i (m-s) \\varphi }\\psi (\\theta )$$
$$=-\\lambda  \\psi (\\theta ,\\varphi ).$$
```

Therefore, the Hamiltonian acts as

```wl
$$\\hat{H}\\psi (\\theta ,\\varphi )=-\\frac{\\hbar \
^2}{2I_t}(-\\lambda )\\psi (\\theta ,\\varphi )+\\frac{\\hbar \
^2s^2}{2I_a}\\psi (\\theta ,\\varphi )$$
$$=\\left(\\frac{\\hbar ^2}{2I_t}\\lambda +\\frac{\\hbar ^2s^2}{2I_a}\
\\right)\\psi (\\theta ,\\varphi ),$$
```

such that the eigen energy should be identified as

```wl
$$E=\\frac{\\hbar ^2}{2I_t}\\lambda +\\frac{\\hbar ^2s^2}{2I_a}.$$
```

* The equation Eq. (XXX) can be solved by

```wl
$$\\psi (\\theta )=(1-\\cos  \\theta )^{\\frac{s-m}{2}}(1+\\cos  \
\\theta )^{\\frac{s+m}{2}}P_{l-s}^{(s-m,s+m)}(\\cos  \\theta ),$$
```

where

	* $$P_n^{(a,b)}(x)$$ denotes the [Jacobi \
polynomial](paclet:ref/JacobiP),

```wl
$$P_n^{(a,b)}(x)=2^{-n}\\sum _{k=0}^n \
\\frac{(n+a)!}{k!(n+a-k)!}\\frac{(n+b)!}{(n-k)!(b+k)!}(x-1)^{n-k}(x+1)\
^k.$$
```

which is well-defined for $$x\\in [-1,1]$$ if $$n,n+a,n+b\\in \
\\mathbb{N}$$, implying the following quantization conditions:

		* $$l=s,s+1,s+2,\\ldots$$,

		* $$m=-l,-l+1,\\ldots ,l-1,l$$.

	* The corresponding eigenvalue $$\\lambda$$ is

```wl
$$\\lambda =l\\, (l+1)-s^2.$$
```

Verify Eq. (XXX) and Eq. (XXX).

First replace the $$\\theta$$ variable by $$x=\\cos  \\theta$$, such \
that

```wl
$$\\partial _{\\theta }=\\frac{\\partial  \\cos  \\theta }{\\partial \
\\theta }\\frac{\\partial }{\\partial  \\cos  \\theta }=-\\sin  \
\\theta  \\partial _x.$$
```

and rewrite

```wl
$$\\psi (\\theta )=F(\\cos  \\theta )=F(x).$$
```

Then Eq. (XXX) becomes

```wl
$$\\left(\\frac{-\\sin  \\theta }{\\sin  \\theta }\\partial \
_x\\left(-\\sin ^2 \\theta  \\partial _x\\right)-\\frac{1}{\\sin ^2 \
\\theta }(m-s \\cos  \\theta )^2+\\lambda
\\right)F(x)$$
$$=\\left(\\partial _x\\left(\\left(1-x^2\\right)\\partial \
_x\\right)-\\frac{(m-s x)^2}{1-x^2}+\\lambda \\right)F(x)=0.$$
```

To proceed, we rewrite $$F(x)$$ as

```wl
$$F(x)=(1-x)^{\\frac{s-m}{2}}(1+x)^{\\frac{s+m}{2}}P(x),$$

In[110]:=
Block[{F}, 
	F[x_] := (1 - x) ^ ((s - m) / 2)(1 + x) ^ ((s + m) / 2)P[x];
	Collect[#, {P[x], P'[x], P''[x]}]& /@ Factor[D[(1 - x ^ 2)D[F[x], \
x], x] - (m - s x) ^ 2 / (1 - x ^ 2)F[x] + \[Lambda] F[x]]]

Out[110]= - (1 - x)^ - (m/2) + (s/2) (1 + x)^(m/2) + (s/2) ((s - \
\[Lambda]) P[x] + ( - 2 m + 2 x + 2 s x) P^\[Prime][x] + ( - 1 + x^2) \
P^\[Prime]\[Prime][x])
```

then Eq. (XXX) is reduced to

```wl
$$\\left(\\left(1-x^2\\right)\\partial _x^2+(2m-2(1+s)x)\\partial \
_x+(\\lambda -s)\\right)P(x)=0.$$
```

Note that the [Jacobi polynomial](paclet:ref/JacobiP) \
$$P_n^{(a,b)}(x)$$ satisfies the following differential equation

```wl
$$\\left(\\left(1-x^2\\right)\\partial _x^2+(b-a-(a+b+2)x)\\partial \
_x+n(n+a+b+1)\\right)P(x)=0,$$
```

with $$n=0,1,2,\\ldots$$.

Compare Eq. (XXX) and Eq. (XXX), we should identify

```wl
$$2m=b-a,\\\\
2(1+s)=a+b+2,\\\\
\\lambda -s=n(n+a+b+1)$$
```

whose solution is

```wl
In[111]:= Solve[{b - a == 2m, b + a + 2 == 2(1 + s), \[Lambda] - s == \
n(n + a + b + 1)}, {a, b, \[Lambda]}]

Out[111]= {{a ->  - m + s, b -> m + s, \[Lambda] -> n + n^2 + s + 2 n \
s}}

$$a=s-m,\\\\
b=s+m,\\\\
\\lambda =n^2+(2s+1)n+s.$$
```

If we introduce a new quantum number $$l=s+n$$ to replace $$n$$, the \
eigenvalue $$\\lambda$$ can be further simplified

```wl
In[112]:= Simplify[n + n^2 + s + 2 n s /. n -> l - s]

Out[112]= l + l^2 - s^2

$$\\lambda =l(l+1)-s^2.$$
```

#### Monopole Harmonics

Put together, define the **monopole harmonics** $$Y_{slm}(\\theta \
,\\varphi )$$ function

```wl
$$Y_{slm}(\\theta ,\\varphi )=\\mathcal{N} e^{i (m-s) \\varphi \
}(1-\\cos  \\theta )^{\\frac{s-m}{2}}(1+\\cos  \\theta \
)^{\\frac{s+m}{2}}P_{l-s}^{(s-m,s+m)}(\\cos
 \\theta ).$$
```

where $$P_n^{(a,b)}$$ is the Jacobi polynomial, and $$\\mathcal{N}$$ \
is the *normalization* constant to ensure $$\\int _0^{2\\pi \
}d\\varphi \\int _0^{\\pi }d\\theta \\left| Y_{slm}(\\theta ,\\varphi \
)\\right| {}^2\\sin  \\theta =1$$.

* The eigen wavefunction of $$\\hat{H}$$ is given by

```wl
$$\\psi _{slm}(\\theta ,\\varphi )=Y_{slm}(\\theta ,\\varphi ).$$
```

* The corresponding eigen energy is

```wl
$$E_{slm}=\\frac{\\hbar ^2}{2I_t}\\left(l\\, \
(l+1)-s^2\\right)+\\frac{\\hbar ^2}{2I_a}s^2.$$
```

In the *isotropic* limit ($$I_a=I_t=I$$), the eigen energy only \
depends on the quantum number $$l$$,

```wl
$$E_{slm}=\\frac{\\hbar ^2}{2I}l\\, (l+1).$$
```

* The **quantum numbers** $$s,l,m$$ take values in

	* $$s=0,1/2,1,3/2,\\ldots \\in \\mathbb{N}/2$$, with $$S=\\hbar  s$$ \
\[Implies] sets the monopole strength (i.e. total **magnetic flux** \
through the unit sphere).

	* $$l=s,s+1,s+2,\\ldots \\in s+\\mathbb{N}$$ \[Implies] labels the \
**Landau levels** on the sphere.

	* $$m=-l,-l+1,\\ldots ,l-1,l$$ \[Implies] labels the degenerated \
states within each Landau level \[Implies] Landau level-$$l$$ has the \
**degeneracy** $$(2l+1)$$.

#### Angular Momentum

The total **angular momentum operator** is defined as

```wl
$$\\hat{\\pmb{L}}=\\pmb{n}\\times \\left(-i \\hbar  \
\\pmb{D}_{\\unicode{27c2}}\\right)+\\pmb{S}.$$
```

where

* $$\\pmb{S}=S \\pmb{n}=\\hbar  s \\pmb{n}$$ is the **spin angular \
momentum** (*axial* component).

* $$\\pmb{n}\\times \\left(-i \\hbar  \
\\pmb{D}_{\\unicode{27c2}}\\right)$$ is the **orbital angular \
momentum** (*transverse* component) associated with the spinning axis \
precession, which is given by the *cross product* between:

	* $$\\pmb{n}$$ - axis **coordinate** (on the sphere),

	* $$-i \\hbar  \\pmb{D}_{\\unicode{27c2}}$$ - axis **kinetic \
momentum** (in the tangent plane).

Explicitly,

```wl
$$\\hat{\\pmb{L}}=\\hbar \\, \\left(\\pmb{e}^{\\varphi \
}\\left(-i\\partial _{\\theta }\\right)-\\pmb{e}^{\\theta }\\frac{1}{\
\\sin  \\theta }\\left(\\left(-i\\partial
_{\\varphi }\\right)+s\\, (1-\\cos  \\theta )\\right)+s \
\\pmb{n}\\right).$$
```

Derive Eq. (XXX).

```wl
$$\\hat{\\pmb{L}}=\\pmb{n}\\times \\left(-i \\hbar  \
\\pmb{D}_{\\unicode{27c2}}\\right)+\\pmb{S}$$
$$=-i \\hbar  \\pmb{n}\\times \\left(\\nabla \
_{\\unicode{27c2}}-\\frac{i}{\\hbar }\\pmb{A}\\right)+\\hbar  s \
\\pmb{n}$$
$$=-i \\hbar  \\pmb{n}\\times \\left(\\pmb{e}^{\\theta }\\partial \
_{\\theta }+\\pmb{e}^{\\varphi }\\frac{1}{\\sin  \\theta }\\partial \
_{\\varphi }-\\frac{i}{\\hbar
}S \\frac{\\cos  \\theta -1}{\\sin  \\theta }\\pmb{e}^{\\varphi \
}\\right)+\\hbar  s \\pmb{n}$$
$$=-i \\hbar  \\pmb{n}\\times \\left(\\pmb{e}^{\\theta }\\partial \
_{\\theta }+\\pmb{e}^{\\varphi }\\frac{1}{\\sin  \\theta \
}\\left(\\partial _{\\varphi }+i s (1-\\cos
 \\theta )\\right)\\right)+\\hbar  s \\pmb{n}$$
$$=-i \\hbar \\left(\\pmb{e}^{\\varphi }\\partial _{\\theta \
}-\\pmb{e}^{\\theta }\\frac{1}{\\sin  \\theta }\\left(\\partial \
_{\\varphi }+i s (1-\\cos  \\theta )\\right)\\right)+\\hbar
 s \\pmb{n}$$
$$=\\hbar \\, \\left(\\pmb{e}^{\\varphi }\\left(-i\\partial _{\\theta \
}\\right)-\\pmb{e}^{\\theta }\\frac{1}{\\sin  \\theta \
}\\left(\\left(-i\\partial _{\\varphi }\\right)+s\\,
(1-\\cos  \\theta )\\right)+s \\pmb{n}\\right)$$
```

According to Eq. (XXX) and Eq. (XXX),

```wl
$$\\pmb{n}=\\cos  \\varphi  \\sin  \\theta  \\pmb{e}^x+\\sin  \
\\varphi  \\sin  \\theta  \\pmb{e}^y+\\cos  \\theta  \\pmb{e}^z,\\\\
\\pmb{e}^{\\theta }=\\cos  \\varphi  \\cos  \\theta  \\pmb{e}^x+\\sin \
 \\varphi  \\cos  \\theta  \\pmb{e}^y-\\sin  \\theta  \\pmb{e}^z,\\\\
\\pmb{e}^{\\varphi }=-\\sin  \\varphi  \\pmb{e}^x+\\cos  \\varphi  \
\\pmb{e}^y.$$
```

\\!\\(\\*OverscriptBox[
StyleBox[\"L\",
FontWeight->\"Bold\"], \\(^\\)]\\) in Eq. (XXX) can be decomposed in \
Cartesian coordinate system as

```wl
$$\\hat{\\pmb{L}}=\\hat{L}_x\\pmb{e}^x+\\hat{L}_y\\pmb{e}^y+\\hat{L}_\
z\\pmb{e}^z,$$
```

with

```wl
$$\\hat{L}_x=\\hbar \\, \\left(\\sin  \\varphi  \\left(i\\partial \
_{\\theta }\\right)+\\cos  \\varphi  \\left(\\cot  \\theta  \
\\left(i\\partial _{\\varphi }\\right)+s\\frac{1-\\cos
 \\theta }{\\sin  \\theta }\\right)\\right),\\\\
\\hat{L}_y=\\hbar \\, \\left(-\\cos  \\varphi  \\left(i\\partial \
_{\\theta }\\right)+\\sin  \\varphi  \\left(\\cot  \\theta  \
\\left(i\\partial _{\\varphi }\\right)+s\\frac{1-\\cos
 \\theta }{\\sin  \\theta }\\right)\\right),\\\\
\\hat{L}_z=\\hbar \\, \\left(\\left(-i\\partial _{\\varphi \
}\\right)+s\\, \\right).$$
```

Derive Eq. (XXX).

```wl
$$\\hat{L}_x=\\pmb{e}^x\\cdot \\hat{\\pmb{L}}$$
$$=\\hbar \\, \\left(\\pmb{e}^x\\cdot \\pmb{e}^{\\varphi \
}\\left(-i\\partial _{\\theta }\\right)-\\pmb{e}^x\\cdot \
\\pmb{e}^{\\theta }\\frac{1}{\\sin  \\theta \
}\\left(\\left(-i\\partial
_{\\varphi }\\right)+s\\, (1-\\cos  \\theta )\\right)+s \
\\pmb{e}^x\\cdot \\pmb{n}\\right)$$
$$=\\hbar \\, \\left(-\\sin  \\varphi  \\left(-i\\partial _{\\theta }\
\\right)-\\cos  \\varphi  \\frac{\\cos  \\theta }{\\sin  \\theta \
}\\left(\\left(-i\\partial _{\\varphi
}\\right)+s\\, (1-\\cos  \\theta )\\right)+s \\cos  \\varphi  \\sin  \
\\theta \\right)$$
$$=\\hbar \\, \\left(\\sin  \\varphi  \\left(i\\partial _{\\theta \
}\\right)+\\cos  \\varphi  \\cot  \\theta  \\left(i\\partial \
_{\\varphi }\\right)+s \\cos  \\varphi
 \\frac{1-\\cos  \\theta }{\\sin  \\theta }\\right)$$
$$=\\hbar \\, \\left(\\sin  \\varphi  \\left(i\\partial _{\\theta \
}\\right)+\\cos  \\varphi  \\left(\\cot  \\theta  \\left(i\\partial \
_{\\varphi }\\right)+s\\frac{1-\\cos
 \\theta }{\\sin  \\theta }\\right)\\right).$$

$$\\hat{L}_y=\\pmb{e}^y\\cdot \\hat{\\pmb{L}}$$
$$=\\hbar \\, \\left(\\pmb{e}^y\\cdot \\pmb{e}^{\\varphi \
}\\left(-i\\partial _{\\theta }\\right)-\\pmb{e}^y\\cdot \
\\pmb{e}^{\\theta }\\frac{1}{\\sin  \\theta \
}\\left(\\left(-i\\partial
_{\\varphi }\\right)+s\\, (1-\\cos  \\theta )\\right)+s \
\\pmb{e}^y\\cdot \\pmb{n}\\right)$$
$$=\\hbar \\, \\left(\\cos  \\varphi  \\left(-i\\partial _{\\theta \
}\\right)-\\sin  \\varphi  \\frac{\\cos  \\theta }{\\sin  \\theta \
}\\left(\\left(-i\\partial _{\\varphi
}\\right)+s\\, (1-\\cos  \\theta )\\right)+s \\sin  \\varphi  \\sin  \
\\theta \\right)$$
$$=\\hbar \\, \\left(-\\cos  \\varphi  \\left(i\\partial _{\\theta \
}\\right)+\\sin  \\varphi  \\cot  \\theta  \\left(i\\partial \
_{\\varphi }\\right)+s \\sin  \\varphi
 \\frac{1-\\cos  \\theta }{\\sin  \\theta }\\right)$$
$$=\\hbar \\, \\left(-\\cos  \\varphi  \\left(i\\partial _{\\theta \
}\\right)+\\sin  \\varphi  \\left(\\cot  \\theta  \\left(i\\partial \
_{\\varphi }\\right)+s\\frac{1-\\cos
 \\theta }{\\sin  \\theta }\\right)\\right).$$

$$\\hat{L}_z=\\pmb{e}^z\\cdot \\hat{\\pmb{L}}$$
$$=\\hbar \\, \\left(\\pmb{e}^z\\cdot \\pmb{e}^{\\varphi \
}\\left(-i\\partial _{\\theta }\\right)-\\pmb{e}^z\\cdot \
\\pmb{e}^{\\theta }\\frac{1}{\\sin  \\theta \
}\\left(\\left(-i\\partial
_{\\varphi }\\right)+s\\, (1-\\cos  \\theta )\\right)+s \
\\pmb{e}^z\\cdot \\pmb{n}\\right)$$
$$=\\hbar \\, \\left(-(-\\sin  \\theta )\\frac{1}{\\sin  \\theta \
}\\left(\\left(-i\\partial _{\\varphi }\\right)+s\\, (1-\\cos  \
\\theta )\\right)+s \\cos  \\theta \\right)$$
$$=\\hbar \\, \\left(\\left(-i\\partial _{\\varphi }\\right)+s\\, \
\\right).$$
```

They satisfy the following commutation relations:

```wl
$$\\left[\\hat{L}_x,\\hat{L}_y\\right]=i \\hbar  \\hat{L}_z,\\\\
\\left[\\hat{L}_y,\\hat{L}_z\\right]=i \\hbar  \\hat{L}_x,\\\\
\\left[\\hat{L}_z,\\hat{L}_x\\right]=i \\hbar  \\hat{L}_y,$$
```

which could be summarized as $$\\hat{\\pmb{L}}\\times \
\\hat{\\pmb{L}}=i \\hbar  \\hat{\\pmb{L}}$$ in vector form. This is \
the defining property of any angular momentum operator.

Verify Eq. (XXX).

As a general rule, for any variable $$x$$, the commutator between its \
derivative $$\\partial _x$$ and its function $$f(x)$$ results in

```wl
$$\\left[\\partial _x,f(x)\\right]=\\partial _xf(x),$$
```

because when acting on any wave function $$\\psi (x)$$, we have

```wl
$$\\left[\\partial _x,f(x)\\right]\\psi (x)=\\partial _x(f(x)\\psi \
(x))-f(x)\\partial _x\\psi (x)$$
$$=\\partial _xf(x)\\psi (x)+f(x)\\partial _x\\psi (x)-f(x)\\partial \
_x\\psi (x)$$
$$=\\partial _xf(x)\\psi (x),$$
```

so the commutator relation holds at the operator level.

Using this rule, we can evaluate the following

We first calculate the commutator between $$\\hat{L}_x$$ and \
$$\\hat{L}_y$$,

```wl
$$\\left[\\hat{L}_x,\\hat{L}_y\\right]=\\hbar ^2\\left[\\sin  \
\\varphi  \\left(i\\partial _{\\theta }\\right)+\\cos  \\varphi  \
\\left(\\cot  \\theta  \\left(i\\partial
_{\\varphi }\\right)+s\\frac{1-\\cos  \\theta }{\\sin  \\theta \
}\\right),-\\cos  \\varphi  \\left(i\\partial _{\\theta \
}\\right)+\\sin  \\varphi  \\left(\\cot  \\theta
 \\left(i\\partial _{\\varphi }\\right)+s\\frac{1-\\cos  \\theta \
}{\\sin  \\theta }\\right)\\right]$$
$$=\\hbar ^2\\left(\\left.\\left[\\sin  \\varphi  \\left(i\\partial \
_{\\theta }\\right),-\\cos  \\varphi  \\left(i\\partial _{\\theta \
}\\right)\\right]+\\left[\\sin
 \\varphi  \\left(i\\partial _{\\theta }\\right),\\sin  \\varphi  \
\\left(\\cot  \\theta  \\left(i\\partial _{\\varphi \
}\\right)+s\\frac{1-\\cos  \\theta }{\\sin  \\theta
}\\right)\\right]+\\right[\\right.\\\\
\\left.\\left.\\cos  \\varphi  \\left(\\cot  \\theta  \
\\left(i\\partial _{\\varphi }\\right)+s\\frac{1-\\cos  \\theta \
}{\\sin  \\theta }\\right),-\\cos  \\varphi  \\left(i\\partial
_{\\theta }\\right)\\right]+\\left[\\cos  \\varphi  \\left(\\cot  \
\\theta  \\left(i\\partial _{\\varphi }\\right)+s\\frac{1-\\cos  \
\\theta }{\\sin  \\theta }\\right),\\sin
 \\varphi  \\left(\\cot  \\theta  \\left(i\\partial _{\\varphi \
}\\right)+s\\frac{1-\\cos  \\theta }{\\sin  \\theta }\\right)\\right]\
\\right)$$
$$=\\hbar ^2\\left(0+\\sin ^2 \\varphi  \\left[i\\partial _{\\theta \
},\\cot  \\theta  \\left(i\\partial _{\\varphi \
}\\right)+s\\frac{1-\\cos  \\theta }{\\sin  \\theta
}\\right]+\\sin  \\varphi  \\cot  \\theta  \\left[\\sin  \\varphi \
,i\\partial _{\\varphi }\\right]\\left(i\\partial _{\\theta \
}\\right)+\\right.\\\\
\\cos  \\varphi  \\cot  \\theta  \\left[i\\partial _{\\varphi \
},-\\cos  \\varphi  \\right]\\left(i\\partial _{\\theta \
}\\right)-\\cos ^2 \\varphi  \\left[\\cot  \\theta
 \\left(i\\partial _{\\varphi }\\right)+s\\frac{1-\\cos  \\theta \
}{\\sin  \\theta },i\\partial _{\\theta }\\right]+\\\\
\\left.\\cos  \\varphi  \\cot  \\theta \\left[ i\\partial _{\\varphi \
},\\sin  \\varphi  \\right]\\left(\\cot  \\theta  \\left(i\\partial \
_{\\varphi }\\right)+s\\frac{1-\\cos
 \\theta }{\\sin  \\theta }\\right)+\\sin  \\varphi  \\cot  \\theta  \
\\left[\\cos  \\varphi ,i\\partial _{\\varphi }\\right]\\left(\\cot  \
\\theta  \\left(i\\partial
_{\\varphi }\\right)+s\\frac{1-\\cos  \\theta }{\\sin  \\theta \
}\\right)\\right)$$
$$=\\hbar ^2\\left(i \\sin ^2 \\varphi  \\left(\\frac{1}{\\sin \
^2\\theta }\\left(-i\\partial _{\\varphi }\\right)+\\frac{s}{1+\\cos  \
\\theta }\\right)-i \\sin  \\varphi
 \\cos  \\varphi  \\cot  \\theta  \\left(i\\partial _{\\theta \
}\\right)+i \\sin  \\varphi  \\cos  \\varphi  \\cot  \\theta  \
\\left(i\\partial _{\\theta }\\right)+\\right.\\\\
\\left.i \\cos ^2 \\varphi  \\left(\\frac{1}{\\sin ^2\\theta \
}\\left(-i\\partial _{\\varphi }\\right)+\\frac{s}{1+\\cos  \\theta }\
\\right)+i \\cos ^2 \\varphi  \\cot
 \\theta  \\left(\\cot  \\theta  \\left(i\\partial _{\\varphi \
}\\right)+s\\frac{1-\\cos  \\theta }{\\sin  \\theta }\\right)+i \\sin \
^2 \\varphi  \\cot  \\theta  \\left(\\cot
 \\theta  \\left(i\\partial _{\\varphi }\\right)+s\\frac{1-\\cos  \
\\theta }{\\sin  \\theta }\\right)\\right)$$
$$=i \\hbar ^2\\left(\\left(\\frac{1}{\\sin ^2\\theta } \
\\left(-i\\partial _{\\varphi }\\right)+\\frac{s}{1+\\cos  \\theta \
}\\right)+\\cot  \\theta  \\left(\\cot 
\\theta  \\left(i\\partial _{\\varphi }\\right)+s\\frac{1-\\cos  \
\\theta }{\\sin  \\theta }\\right)\\right)$$
$$=i \\hbar ^2\\left(\\left(\\frac{1}{\\sin ^2\\theta }-\\cot ^2 \
\\theta \\right)\\left(-i\\partial _{\\varphi }\\right)+s \
\\left(\\frac{1}{1+\\cos  \\theta }+\\frac{(1-\\cos
 \\theta )\\cos  \\theta }{\\sin ^2 \\theta }\\right)\\right)$$
$$=i \\hbar ^2\\left(\\left(-i\\partial _{\\varphi \
}\\right)+s\\right)$$
$$=i \\hbar  \\hat{L}_z.$$
```

We then calculate the commutator of $$\\hat{L}_z$$ with \
$$\\hat{L}_x$$ or $$\\hat{L}_y$$,

```wl
$$\\left[\\hat{L}_z,\\hat{L}_x\\right]=\\hbar \
^2\\left[\\left(-i\\partial _{\\varphi }\\right)+s\\, ,\\sin  \
\\varphi  \\left(i\\partial _{\\theta }\\right)+\\cos 
\\varphi  \\left(\\cot  \\theta  \\left(i\\partial _{\\varphi \
}\\right)+s\\frac{1-\\cos  \\theta }{\\sin  \\theta }\\right)\\right]$$
$$=\\hbar ^2\\left(-i \\left[\\partial _{\\varphi }\\, ,\\sin  \
\\varphi \\right]\\left(i\\partial _{\\theta }\\right)-i \
\\left[\\partial _{\\varphi },\\cos  \\varphi
\\right]\\left(\\cot  \\theta  \\left(i\\partial _{\\varphi \
}\\right)+s\\frac{1-\\cos  \\theta }{\\sin  \\theta }\\right)\\right)$$
$$=i \\hbar ^2\\left(-\\cos  \\varphi  \\left(i\\partial _{\\theta \
}\\right)+\\sin  \\varphi \\left(\\cot  \\theta  \\left(i\\partial _{\
\\varphi }\\right)+s\\frac{1-\\cos
 \\theta }{\\sin  \\theta }\\right)\\right)$$
$$=i \\hbar  \\hat{L}_y.$$
```

Since under the transformation $$\\varphi \\rightarrow \\varphi -\\pi \
/2$$,

```wl
$$\\sin  \\varphi \\rightarrow \\sin (\\varphi -\\pi /2)=-\\cos  \
\\varphi ,\\\\
\\cos  \\varphi \\rightarrow \\cos (\\varphi -\\pi /2)=\\sin  \
\\varphi ,\\\\
\\hat{L}_x\\rightarrow \\hat{L}_y,$$
```

we can infer

```wl
$$\\left[\\hat{L}_z,\\hat{L}_y\\right]=i \\hbar ^2\\left(-\\sin  \
\\varphi  \\left(i\\partial _{\\theta }\\right)-\\cos  \\varphi  \
\\left(\\cot  \\theta  \\left(i\\partial
_{\\varphi }\\right)+s\\frac{1-\\cos  \\theta }{\\sin  \\theta \
}\\right)\\right)$$
$$=-i \\hbar  \\hat{L}_x,$$
```

therefore $$\\left[\\hat{L}_y,\\hat{L}_z\\right]=i \\hbar  \
\\hat{L}_x$$.

#### Squared Angular Momentum

The **squared angular momentum operator** is generally defined as

```wl
$$\\hat{\\pmb{L}}^2\\text{:=}\\hat{\\pmb{L}}\\cdot \
\\hat{\\pmb{L}}=\\hat{L}_x^2+\\hat{L}_y^2+\\hat{L}_z^2.$$
```

* For our case of 
\\!\\(\\*OverscriptBox[
StyleBox[\"L\",
FontWeight->\"Bold\"], \\(^\\)]\\) in Eq. (XXX), 
\\!\\(\\*OverscriptBox[
StyleBox[\"L\",
FontWeight->\"Bold\"], \\(^\\)]\\)^2 can be explicitly written out

```wl
$$\\hat{\\pmb{L}}^2=-\\hbar ^2\\pmb{D}_{\\unicode{27c2}}^2+S^2$$
$$=\\frac{-\\hbar ^2}{\\sin  \\theta }\\left(\\partial _{\\theta \
}\\left(\\sin  \\theta  \\partial _{\\theta }\\right)+\\frac{1}{\\sin \
 \\theta }\\left(\\partial _{\\varphi
}+i s (1-\\cos  \\theta )\\right){}^2\\right)+\\hbar ^2s^2.$$
```

* A key property of $$\\hat{\\pmb{L}}^2$$ is that it commutes with \
any component of the angular momentum operator,

```wl
$$\\left[\\hat{\\pmb{L}}^2,\\hat{L}_a\\right]=0\\text{   \
}(\\text{for} a=x,y,z),$$
```

or simply written as \
$$\\left[\\hat{\\pmb{L}}^2,\\hat{\\pmb{L}}\\right]=0$$ in vector \
form. It is commonly referred to as the **Casimir operator** of the \
$$\\mathfrak{s}\\mathfrak{o}(3)$$ algebra \[LongDash] an element in \
the Lie algebra that *commutes* with all its *generators*.

Proof Eq. (XXX) based on Eq. (XXX).

```wl
$$\\left[\\hat{\\pmb{L}}^2,\\hat{L}_a\\right]=\\left[\\hat{L}_b\\hat{\
L}_b,\\hat{L}_a\\right]$$
$$=\\hat{L}_b\\left[\\hat{L}_b,\\hat{L}_a\\right]+\\left[\\hat{L}_b,\\\
hat{L}_a\\right]\\hat{L}_b$$
$$=i \\hbar  \\epsilon ^{bac}\\hat{L}_b\\hat{L}_c+i \\hbar  \\epsilon \
^{bac}\\hat{L}_c\\hat{L}_b$$
$$=i \\hbar  \\left(\\epsilon ^{bac}+\\epsilon \
^{cab}\\right)\\hat{L}_b\\hat{L}_c$$
$$=i \\hbar  \\left(-\\epsilon ^{abc}+\\epsilon \
^{abc}\\right)\\hat{L}_b\\hat{L}_c$$
$$=0.$$
```

Given $$\\left[\\hat{\\pmb{L}}^2,\\hat{L}_z\\right]=0$$ (i.e. \
$$\\hat{\\pmb{L}}^2$$ and $$\\hat{L}_z$$ are commuting operators), \
they can be *simultaneously diagonalized* by a set of **common \
eigenstates**, which turns out to be the *monopole harmonics* \
$$Y_{slm}(\\theta ,\\varphi )$$,

```wl
$$\\hat{\\pmb{L}}^2Y_{slm}(\\theta ,\\varphi )=\\hbar ^2 l \
(l+1)Y_{slm}(\\theta ,\\varphi ),\\\\
\\hat{L}_zY_{slm}(\\theta ,\\varphi )=\\hbar  m Y_{slm}(\\theta \
,\\varphi ).$$
```

Verify Eq. (XXX).

First verify the eigenvalue of 
\\!\\(\\*OverscriptBox[
StyleBox[\"L\",
FontWeight->\"Bold\"], \\(^\\)]\\)^2. According to Eq. (XXX) and \
Eq. (XXX),

```wl
$$\\pmb{D}_{\\unicode{27c2}}^2Y_{slm}(\\theta ,\\varphi )=-\\lambda \
Y_{slm}(\\theta ,\\varphi )=-\\left(l\\, \
(l+1)-s^2\\right)Y_{slm}(\\theta ,\\varphi ),$$
```

using Eq. (XXX), we have

```wl
$$\\hat{\\pmb{L}}^2Y_{slm}(\\theta ,\\varphi )=\\left(-\\hbar \
^2\\pmb{D}_{\\unicode{27c2}}^2+S^2\\right)Y_{slm}(\\theta ,\\varphi )$$
$$=\\left(\\hbar ^2\\left(l\\, (l+1)-s^2\\right)+\\hbar \
^2s^2\\right)Y_{slm}(\\theta ,\\varphi )$$
$$=\\hbar ^2l\\, (l+1)Y_{slm}(\\theta ,\\varphi ).$$
```

Then verify the eigenvalue of $$\\hat{L}_z$$. Given that \
$$Y_{slm}(\\theta ,\\varphi )$$ takes the form of

```wl
$$Y_{slm}(\\theta ,\\varphi )=e^{i (m-s) \\varphi }\\Theta \
_{slm}(\\theta ),$$
```

using Eq. (XXX), we have

```wl
$$\\hat{L}_zY_{slm}(\\theta ,\\varphi )=\\hbar \\, \
\\left(\\left(-i\\partial _{\\varphi }\\right)+s\\, \\right)e^{i \
(m-s) \\varphi }\\Theta _{slm}(\\theta )$$
$$=\\hbar \\, ((m-s)+s\\, )e^{i (m-s) \\varphi }\\Theta \
_{slm}(\\theta )$$
$$=\\hbar \\, m Y_{slm}(\\theta ,\\varphi ).$$
```

* The quantum numbers are reinterpreted as

	* $$l=s,s+1,s+2,\\ldots \\in s+\\mathbb{N}$$ - **angular quantum \
number** (labeling quantized total angular momentum),

	* $$m=-l,-l+1,\\ldots ,l-1,l$$ - **magnetic quantum number** \
(labeling quantized $$z$$-component of angular momentum).

#### Spin-$$1/2$$

The smallest *non-trivial* monopole strength is

```wl
$$s=1/2,$$
```

corresponding to a quantum spinning top with *axial* **angular \
momentum**

```wl
$$S=\\hbar  s=\\frac{\\hbar }{2}.$$
```

The total angular momentum can not be smaller than $$S$$.

The *lowest* Landau level is achieved at $$l=s=1/2$$, where the total \
angular momentum saturates its minimal value $$S=\\hbar /2$$, \
realizing a spin-$$1/2$$ system. In this case:

* There are only two options for the quantum number $$m$$

```wl
$$m=\\pm \\frac{1}{2},$$
```

corresponding to the *up* and *down* spin states.

* The corresponding *monopole harmonics* wave functions are

```wl
$$Y_{1/2,1/2,m}(\\theta ,\\varphi )=\\frac{1}{\\sqrt{4\\pi }}e^{i \
(m-1/2) \\varphi }(1-\\cos  \\theta )^{\\frac{1/2-m}{2}}(1+\\cos  \
\\theta )^{\\frac{1/2+m}{2}},$$
```

or respectively as

```wl
$$Y_{1/2,1/2,+1/2}(\\theta ,\\varphi )=\\frac{1}{\\sqrt{4\\pi \
}}\\sqrt{1+\\cos  \\theta },\\\\
Y_{1/2,1/2,-1/2}(\\theta ,\\varphi )=\\frac{1}{\\sqrt{4\\pi }}e^{-i \
\\varphi }\\sqrt{1-\\cos  \\theta }.$$

In[202]:=
Block[{monoY}, 
	monoY[s_, l_, m_] := SphericalPlot3D[1, {\[Theta], 0, \[Pi]}, {\
\[CurlyPhi], 0, 2\[Pi]}, ColorFunction -> Function[{x, y, z, \
\[Theta], \[CurlyPhi], r}, ComplexColor[Exp[I(m - s)\[CurlyPhi]]((1 - \
Cos[\[Theta]]) / 2) ^ ((s - m) / 2)((1 + Cos[\[Theta]]) / 2) ^ ((s + \
m) / 2)JacobiP[l - s, s - m, s + m, Cos[\[Theta]]]]], Axes -> False, \
SphericalRegion -> True, Boxed -> False, ColorFunctionScaling -> \
False, Lighting -> \"Neutral\", ViewPoint -> { - 5, 2, 0}, ImageSize -> \
140];
	Grid[{Style[#, \"InlineFormula\"]& /@ {Y
 1/2, 1/2, +1/2, Y
 1/2, 1/2, -1/2}, {monoY[1 / 2, 1 / 2, 1 / 2], monoY[1 / 2, 1 / 2,  - \
1 / 2]}}]]

Out[202]=
|                             |                             |
| --------------------------- | --------------------------- |
| Y  1/2, 1/2, +1/2           | Y  1/2, 1/2, -1/2           |
| \\!\\(\\*Graphics3DBox[«19»]\\) | \\!\\(\\*Graphics3DBox[«19»]\\) |
```

	* **Angular momentum** eigenvalues :

```wl
$$\\hat{\\pmb{L}}^2Y_{1/2,1/2,\\pm 1/2}=\\frac{3}{4}\\hbar \
^2Y_{1/2,1/2,\\pm 1/2},\\\\
\\hat{L}_zY_{1/2,1/2,\\pm 1/2}=\\pm \\frac{1}{2}\\hbar  \
Y_{1/2,1/2,\\pm 1/2}.$$
```

	* **Energy** eigenvalue (2-fold degenerated)

```wl
$$\\hat{H}Y_{1/2,1/2,\\pm 1/2}=\\left(\\frac{\\hbar ^2}{4I_t}+\\frac{\
\\hbar ^2}{8I_a}\\right)Y_{1/2,1/2,\\pm 1/2}.$$
```

Puzzle: It seems that $$Y_{1/2,1/2,-1/2}(\\theta ,\\varphi )$$ is not \
single-valued at the *south pole* ($$\\theta =\\pi$$), is there \
anything wrong?

* **Topological obstruction**: Monopole harmonics can not be \
*globally* single-valued in a naive coordinate sense because of the \
*nontrivial* **gauge curvature** induced by the monopole.

* However, the apparent multivaluedness is a **gauge artifact**, and \
can be removed by the *gauge transformation*.

Solution: define the monopole harmonics on different hemispheres with \
different gauge choices, and switch gauge choices at the equator by \
gauge transformation.

* For the **northern hemisphere** ($$\\theta \\in [0,\\pi /2]$$, \
excluding the south pole):

```wl
$$\\pmb{A}_N(\\theta ,\\varphi )=\\frac{\\hbar }{2}\\frac{\\cos  \
\\theta -1}{\\sin  \\theta }\\pmb{e}_{\\varphi },\\\\
Y_{1/2,1/2,+1/2}^N(\\theta ,\\varphi )=\\frac{1}{\\sqrt{4\\pi \
}}\\sqrt{1+\\cos  \\theta },\\\\
Y_{1/2,1/2,-1/2}^N(\\theta ,\\varphi )=\\frac{1}{\\sqrt{4\\pi }}e^{-i \
\\varphi }\\sqrt{1-\\cos  \\theta }.$$
```

* For the **southern hemisphere** ($$\\theta \\in [\\pi /2,\\pi ]$$, \
excluding the north pole):

```wl
$$\\pmb{A}_S(\\theta ,\\varphi )=\\frac{\\hbar }{2}\\frac{\\cos  \
\\theta +1}{\\sin  \\theta }\\pmb{e}_{\\varphi },\\\\
Y_{1/2,1/2,+1/2}^S(\\theta ,\\varphi )=\\frac{1}{\\sqrt{4\\pi }}e^{i \
\\varphi }\\sqrt{1+\\cos  \\theta },\\\\
Y_{1/2,1/2,-1/2}^S(\\theta ,\\varphi )=\\frac{1}{\\sqrt{4\\pi \
}}\\sqrt{1-\\cos  \\theta }.$$
```

* On the **equator** ($$\\theta =\\pi /2$$), the two gauge choices \
are related by a **gauge transformation** :

```wl
$$\\pmb{A}_N(\\pi /2,\\varphi )=\\pmb{A}_S(\\pi /2,\\varphi )+\\hbar  \
\\pmb{e}_{\\varphi }\\partial _{\\varphi }\\chi (\\varphi ),\\\\
Y_{1/2,1/2,m}^N(\\pi /2,\\varphi )=e^{i \\chi (\\varphi \
)}Y_{1/2,1/2,m}^S(\\pi /2,\\varphi ),$$
```

with $$\\chi (\\varphi )=-\\varphi$$.

Verify Eq. (XXX).

* Check

```wl
$$\\pmb{A}_N(\\pi /2,\\varphi )=\\frac{\\hbar }{2}\\frac{\\cos (\\pi \
/2)-1}{\\sin (\\pi /2)}\\pmb{e}_{\\varphi }$$
$$=-\\frac{\\hbar }{2}\\pmb{e}_{\\varphi },$$

$$\\pmb{A}_S(\\pi /2,\\varphi )+\\hbar  \\pmb{e}_{\\varphi }\\partial \
_{\\varphi }\\chi (\\varphi )=\\frac{\\hbar }{2}\\frac{\\cos (\\pi \
/2)+1}{\\sin (\\pi /2)}\\pmb{e}_{\\varphi
}+\\hbar  \\pmb{e}_{\\varphi }\\partial _{\\varphi }(-\\varphi )$$
$$=\\frac{\\hbar }{2}\\pmb{e}_{\\varphi }-\\hbar  \\pmb{e}_{\\varphi \
}$$
$$=-\\frac{\\hbar }{2}\\pmb{e}_{\\varphi },$$
```

thus $$\\pmb{A}_N(\\pi /2,\\varphi )=\\pmb{A}_S(\\pi /2,\\varphi \
)+\\hbar  \\pmb{e}_{\\varphi }\\partial _{\\varphi }\\chi (\\varphi \
)$$.

* It can be shown that

```wl
$$e^{i \\chi (\\varphi )}Y_{1/2,1/2,m}^S(\\pi /2,\\varphi )$$
$$=e^{-i \\varphi }\\frac{1}{\\sqrt{4\\pi }}e^{i (m+1/2) \\varphi \
}(1-\\cos (\\pi /2))^{\\frac{1/2-m}{2}}(1+\\cos (\\pi \
/2))^{\\frac{1/2+m}{2}}$$
$$=\\frac{1}{\\sqrt{4\\pi }}e^{i (m-1/2) \\varphi }$$
$$=\\frac{1}{\\sqrt{4\\pi }}e^{i (m-1/2) \\varphi }(1-\\cos (\\pi \
/2))^{\\frac{1/2-m}{2}}(1+\\cos (\\pi /2))^{\\frac{1/2+m}{2}}$$
$$=Y_{1/2,1/2,m}^N(\\pi /2,\\varphi ).$$
```

Therefore, monopole harmonics can (only) be defined by piecing \
different gauge patches together with gauge transformations,

```wl
$$Y_{1/2,1/2,m}(\\theta ,\\varphi )=
\\begin{array}{ll}
 \\{ & 
\\begin{array}{ll}
 Y_{1/2,1/2,m}^N(\\theta ,\\varphi ) & \\theta \\in [0,\\pi /2], \\\\
 Y_{1/2,1/2,m}^S(\\theta ,\\varphi ) & \\theta \\in [\\pi /2,\\pi ], \
\\\\
\\end{array}
 \\\\
\\end{array}$$
```

such that there is no singularity on any patch, and physical \
quantities are all well-behaved.

