<!--
  Source: PathIntegral.nb
  Generated: Mathematica `Import[..., "Plaintext"]` plus heading structure from notebook cells (stylesheet stripped).
  Interactive/graphics cells appear as Wolfram Language source text.
-->

# 130B Quantum Physics

## Part 1. Path Integral Quantization

### From Classical to Quantum

#### Historical Review

##### History: What is the Nature of Light?

There has been two theories in the history concerning the nature of light.

The corpuscular (particle) theory: light is composed of steady stream of particles carrying the energy and travelling along rays in the speed of light.

The wave theory: light is wave-like, propagating in the space and time.

The long-running dispute about this problem has lasted for centuries.

###### The Wave-Particle Wars in History

A time-line of “the wave-particle wars” in the history of physics. (c.f. Wikipedia: Historical theories about light <https://en.wikipedia.org/wiki/Light#Historical_theories_about_light,_in_chronological_order>).

Ancient Greece

	Pythagorean discipline postulated that every visible object emits a steady stream of particles, while Aristotle concluded that light travels in a manner similar to waves in the ocean.

	
Early 17th century	

	R. Descartes proposed light is a kind of pressure propagating in the media.

	
1662

	P. de Fermat stated the Fermat principle, the fundamental principle of geometric optics, where light rays are assumed to be trajectories of small particles.

	
1665

	P. Hooke expressly pointed out the wave theory of light in his book, where light was considered as some kind of fast pulses.

	
1672

	I. Newton conducted the dispersion experiment of light. He decomposed white light into seven colors. Thus he explained that light is a mixture of little corpuscles of different colors. His paper was strongly opposed by Hook, and “the first wave-particle war” broke out.

	
1675

	The phenomenon of Newton’s ring was discovered by Newton.

	
1690

	C. Huygens considered light as longitudinal wave propagating in a media called ether. He introduced the concept of wave front, deduced the law of reflection and refraction, and explained the phenomenon of Newton’s ring by wave interference. The wave theory reached its crest.

	
1704

	I. Newton published his book Optiks, which explained dispersion, double refraction, and diffraction from particle viewpoint. On the other side, Newton integrated the corpuscular theory with his classical mechanics, which combined to show enormous strength over the century.

	
Early 18th century

	“The first wave-particle war” ends, and corpuscular (particle) theory occupied the mainstream of physics for the following hundred years.

	
1807

	T. Young conducted the double-split experiment, and proposed light to be a longitudinal wave, which simply explained the interference and diffraction of light. Young’s experiment triggered “the second wave-particle war”. The corpuscular theory could do nothing but to suffer one defeat after another.

	
1809

	E. Malus discover the polarization of light, which could not be explained by longitudinal wave theory. This gave the wave theory a heavy strike.

	
1819

	A. Fresnel submitted a paper, perfectly explained the diffraction of light from wave viewpoint based on rigorous mathematical deductions. When Poisson applied this theory to circular disk diffraction, he predicted that a light spot will appear at the center of the shadow of the disk. This unreasonable effect was considered by Poisson as an opposing evidence of the wave theory. However, F. Arago insisted on doing the experiment and proved the existence of the Poisson spot. The success of Fresnel’s theory won the decisive battle for the wave in “the second wave-particle war”.

	
1821

	Fresnel proposed that light is a transverse wave, and successfully explained the polarization of light. “The second wave-particle war” ended with the victory of wave theory.

	
1865

	J. Maxwell formulated the classical theory of electrodynamics, which predicted that light is kind of electromagnetic wave.

	
1887

	H. R. Hertz verified the existence of electromagnetic wave in experiments. The speed of the electromagnetic wave is exactly the speed of light. The wave theory of light was firmly established.

	
1900

	M. Planck obtained the formula of blackbody radiation, the quantum hypothesis of light was proposed.

	
1905

	A. Einstein explained the photoelectric effect. In Einstein’s theory light is consisted of some particles carrying the discrete amount of energy, and can only be absorbed or emitted one by one. The concept of light quantum (photon) resurrected the particle theory. “The third wave-particle war” broke out.

	
1923

	A. Compton studied the scattering of X-ray by a free electron. The Compton effect was discovered, that the frequency of X-ray changes in the scattering. The experiment exactly proved that X-ray is also composed by radiation quantum with certain momentum and energy.

	
1924

	S. N. Bose considered light as a set of indistinguishable particles and obtained Planck’s formula of blackbody radiation. Bose-Einstein statistics was established, which further supports the idea of particle theory.

	
…

	…

	

###### Concluding Remarks

In fact, “the third wave-particle war” had gone beyond the scope of the nature of light. The discussion had been extended to the nature of all matter in general.

Light: originally considered as wave, also behaves like particle.

Electrons, \[Alpha]

 particles ( ^4

He nucleus): originally considered as particles, also behave like wave.

The dispute ends up with the discovery of wave-particle duality, which finally leads to the formulation of quantum mechanics. Another century has passed, we hope that wave and particle will live in peace under the quantum framework, and there should be no more wars.

#### Quantization of Light

##### Geometric Optics

Geometric optics is the particle mechanics of light (light travels along a path)

Fermat’s Principle: Light always travels along the path of extremal optical path length.

\[Delta]\[InvisibleComma]L = 0, 

The optical path length is defined by

L(A->B) = ∫ABnds, 

where n

 is the refractive index of the medium and ds

 is an infinitesimal displacement along the ray.

The optical path length is simply related to the light travelling time T

 by L = c T

, where c

 is the speed of light in vacuum. So extremization of either of them will be equivalent.

Eikonal equation (Newton’s law of light)

nd/dt(n^2dx/dt) = c^2∇n.

Derive Eq. (1) from Fermat’s principle Eq. (1).

Fermat’s Principle states that light follows a path for which the optical path length is extremized:

L = ∫ABn(x)ds
 = ∫n(x)\[LeftBracketingBar]x.\[RightBracketingBar]dt.

where:

n(x)

 is the refractive index at position x

,

ds = \[LeftBracketingBar]x.\[RightBracketingBar]dt

 is the infinitesimal arc length along the path.

Instead of integrating over the path, we will treat the optical path length as an action S[x(t)] = ∫ℒ(x, x.)dt

 that integrates over time, where

ℒ(x, x.) = n(x)\[LeftBracketingBar]x.\[RightBracketingBar]

is the Lagrangian.

In this way, we can apply the standard result in classical mechanics: extremization of the action \[Delta]\[InvisibleComma]S = 0

 leads to the Euler-Lagrange equation

d/dt(∂L/∂x.) - ∂L/∂x = 0.

Compute the derivatives:

∂L/∂x. = n(x)x./\[LeftBracketingBar]x.\[RightBracketingBar], 
∂L/∂x = ∇n(x)\[LeftBracketingBar]x.\[RightBracketingBar], 

then

d/dt(nx./\[LeftBracketingBar]x.\[RightBracketingBar]) = ∇n\[LeftBracketingBar]x.\[RightBracketingBar].

Using the fact that n\[LeftBracketingBar]x.\[RightBracketingBar] = c

 (along the classical path that light travels), where \[LeftBracketingBar]x.\[RightBracketingBar]

 is the speed of light in the medium and c

 is the vacuum speed of light, by multiplying or dividing n

 appropriately, we obtain

nd/dt(n^2x./n\[LeftBracketingBar]x.\[RightBracketingBar]) = n\[LeftBracketingBar]x.\[RightBracketingBar]∇n
\[Implies]nd/dt(n^2x./c) = c∇n
\[Implies]nd/dt(n^2dx/dt) = c^2∇n.



Examples of light rays in the medium by solving Eq. (1):

Refraction (Snell’s law)

Module[{x0 =  - 1, y0 =  - 1, \[Theta] = 30Degree, n, tend = 5, sol, data, xmin, xmax, ymin, ymax, colbg = ColorData["Legacy"]["DodgerBlue"], colray = ColorData["Legacy"]["Firebrick"]}, n[x_, y_]:=1.366 + 0.366Tanh[25y];sol = NDSolve[{n[x[t], y[t]]D[n[x[t], y[t]]^2D[x[t], t], t]==D[n[x[t], y[t]], x[t]], n[x[t], y[t]]D[n[x[t], y[t]]^2D[y[t], t], t]==D[n[x[t], y[t]], y[t]], x[0]==x0, y[0]==y0, x'[0]==Cos[\[Theta]] / n[x0, y0], y'[0]==Sin[\[Theta]] / n[x0, y0]}, {x, y}, {t, 0, tend}];data = First@Cases[ParametricPlot[Evaluate[{x[t], y[t]}/.sol], {t, 0, tend}, PlotPoints->10, MaxRecursion->3], Line[pts_]:>pts, ∞];{{xmin, xmax}, {ymin, ymax}} = {Min[#], Max[#]}&/@Thread[data];Show[ContourPlot[n[x, y], {x, xmin, xmax}, {y, ymin, ymax}, Contours->16, ContourStyle->None, ColorFunction->(Blend[{White, colbg}, Rescale[#, {0.9, 2.0}]]&), ColorFunctionScaling->False], Graphics[{AbsoluteThickness[1.2], colray, Arrowheads[{{0.001, 0.2, Arrowhead[]}, {0.001, 0.8, Arrowhead[]}}], Arrow[data]}], AspectRatio->Automatic, PlotRangePadding->0.05, FrameTicks->None, ImageSize->120]]

None
None
NoneNone
NoneNone


Total reflection

Module[{x0 =  - 1, y0 = 1, \[Theta] =  - 45Degree, n, tend = 6.6, sol, data, xmin, xmax, ymin, ymax, colbg = ColorData["Legacy"]["DodgerBlue"], colray = ColorData["Legacy"]["Firebrick"]}, n[x_, y_]:=1.3 + 0.3Tanh[3y];sol = NDSolve[{n[x[t], y[t]]D[n[x[t], y[t]]^2D[x[t], t], t]==D[n[x[t], y[t]], x[t]], n[x[t], y[t]]D[n[x[t], y[t]]^2D[y[t], t], t]==D[n[x[t], y[t]], y[t]], x[0]==x0, y[0]==y0, x'[0]==Cos[\[Theta]] / n[x0, y0], y'[0]==Sin[\[Theta]] / n[x0, y0]}, {x, y}, {t, 0, tend}];data = First@Cases[ParametricPlot[Evaluate[{x[t], y[t]}/.sol], {t, 0, tend}, PlotPoints->10, MaxRecursion->3], Line[pts_]:>pts, ∞];{{xmin, xmax}, {ymin, ymax}} = {Min[#], Max[#]}&/@Thread[data];Show[ContourPlot[n[x, y], {x, xmin, xmax}, {y, ymin - 0.5, ymax}, Contours->16, ContourStyle->None, ColorFunction->(Blend[{White, colbg}, Rescale[#, {0.9, 2.0}]]&), ColorFunctionScaling->False], Graphics[{AbsoluteThickness[1.2], colray, Arrowheads[{{0.001, 0.2, Arrowhead[]}, {0.001, 0.8, Arrowhead[]}}], Arrow[data]}], AspectRatio->Automatic, PlotRangePadding->0.05, FrameTicks->None, ImageSize->140]]

None
None
NoneNone
NoneNone


Gradient-index (GRIN) optics

Module[{x0 =  - 5, \[Theta] = 0Degree, n, tend = 13, sols, datas, colbg = ColorData["Legacy"]["DodgerBlue"], colray = ColorData["Legacy"]["Firebrick"]}, n[x_, y_]:=1 + 0.8Exp[ - ((x / 2)^10 + y^2 / 14)];sols = NDSolve[{n[x[t], y[t]]D[n[x[t], y[t]]^2D[x[t], t], t]==D[n[x[t], y[t]], x[t]], n[x[t], y[t]]D[n[x[t], y[t]]^2D[y[t], t], t]==D[n[x[t], y[t]], y[t]], x[0]==x0, y[0]==#, x'[0]==Cos[\[Theta]] / n[x0, #], y'[0]==Sin[\[Theta]] / n[x0, #]}, {x, y}, {t, 0, tend}]&/@{ - 2,  - 1, 0, 1, 2};datas = Cases[ParametricPlot[Evaluate[{x[t], y[t]}/.sols], {t, 0, tend}, PlotPoints->10, MaxRecursion->3], Line[pts_]:>pts, ∞];
Show[ContourPlot[n[x, y], {x,  - 5, 5}, {y,  - 5, 5}, Contours->16, ContourStyle->None, PlotRange->All, ColorFunction->(Blend[{White, colbg}, Rescale[#, {0.9, 2.0}]]&), ColorFunctionScaling->False], Graphics[{AbsoluteThickness[1.2], colray, Arrowheads[{{0.001, 0.2, Arrowhead[]}, {0.001, 0.6, Arrowhead[]}}], Arrow/@datas}], AspectRatio->Automatic, PlotRangePadding->0.2, FrameTicks->None, ImageSize->120]]

None
None
NoneNone
NoneNone


##### Physical Optics

Physical optics is the wave mechanics of light (light propagates in the spacetime as a wave).

Huygens’ Principle: Every point on the wavefront acts as a secondary source emitting spherical wavelet. The new wavefront is formed by the coherent superposition of these wavelets.

Block[{y0 =  - 10, r0 = 10, dr = 0.1, d\[Theta] = 0.005\[Pi], d\[Theta]2 = 0.05\[Pi], \[Theta]max = 0.2\[Pi], \[Theta]b = 0.16\[Pi], wv, wc}, 
wv[r_, \[Theta]_, dk_]:=Block[{col}, col = Lighter[Yellow, 1 - dk];{EdgeForm[col], col, Polygon[ReIm[I Flatten[ - y0 + {r  Exp[I (\[Theta] + d\[Theta]{ - 1, 1} / 2)], (r + dr)Exp[I (\[Theta] + d\[Theta]{1,  - 1} / 2)]}]]]}];
wc[r_, \[Theta]_, dk_]:=Table[{Opacity[Mod[a, 1] dk], Yellow, Annulus[ReIm[I( - y0 + r Exp[I \[Theta]])], {a - dr, a}]}, {a, 2 - dr, 2dr,  - dr}];
Graphics[{Table[wv[r, \[Theta], Mod[r, 1]LogisticSigmoid[20(\[Theta]b^2 - \[Theta]^2)]LogisticSigmoid[0.5r Sin[\[Theta]]]], {\[Theta],  - \[Theta]max, \[Theta]max, d\[Theta]}, {r, r0 + 3, r0 + 5 - dr, dr}], 
Block[{r = r0 + 3}, Table[wc[r, \[Theta], LogisticSigmoid[ - 0.5r Sin[\[Theta]]]], {\[Theta], d\[Theta]2,  - \[Theta]max + d\[Theta]2,  - d\[Theta]2}]], 
Table[wv[r, \[Theta], Mod[r, 1]LogisticSigmoid[20(\[Theta]b^2 - \[Theta]^2)]], {\[Theta],  - \[Theta]max, \[Theta]max, d\[Theta]}, {r, r0, r0 + 3 - dr, dr}], 
Translate[{Point[{0, 0}], Text["\!\( A\)", {0, 0}, {0, 1.2}]}, ReIm[I( - y0 + (r0 + 3) Exp[ - I d\[Theta]2])]], Translate[{Point[{0, 0}], Text["\!\( B\)", {0, 0}, {0,  - 1}]}, ReIm[I( - y0 + (r0 + 4) Exp[I ( - d\[Theta]2 + 0.01\[Pi])])]]}, ImageSize->220]]

SplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegreeSplineKnotsSplineWeightsSplineDegree\!\( A\)\!\( B\)

Wave propagation: The wave amplitude \[Psi]B

 on the new wave front is determined by the amplitude \[Psi]A

 on the preceding wave front, modified by a phase factor E^I \[CapitalTheta](A->B)

 that encodes the accumulated phase \[CapitalTheta](A->B)

 during wave propagation.

Interference effect: contributions from different paths must be collected and summed up (integrated over)

\[Psi]B = ∫A->B\[Psi]AE^I \[CapitalTheta](A->B).

The accumulated phase \[CapitalTheta]

 is determined by the propagation time T

 × the frequency \[Omega]

 of light

\[CapitalTheta](A->B) = \[Omega] T(A->B) = \[Omega]/cL(A->B), 

proportional to the optical path length L

 (given that the light propagates with a fixed frequency).

The resulting profile of the wave amplitude throughout the spacetime (or the space) is described by the wavefunction

spacetime: \[Psi](x, t), 
space (at fixed-time):\[Psi](x).

The magnitude (or the absolute amplitude) \[LeftBracketingBar]\[Psi]\[RightBracketingBar]

 of the wave is related to the intensity of the light, or the probability density to observe a photon at a given position x

,

p(x) = \[LeftBracketingBar]\[Psi](x)\[RightBracketingBar]^2.

Normalization: the wavefunction is said to be normalized, if

∫\[LeftBracketingBar]\[Psi](x)\[RightBracketingBar]^2d^Dx = ∫p(x)d^Dx = 1, 

a requirement for the total probability to be 1.

##### From Fermat to Huygens

Optimizing the optical path length L

 can be viewed as optimizing an action S



S(A->B) = ℏ \[Omega]/cL(A->B), 

which is defined by properly rescaling L

 to match the dimension of energy × time.

Particle mechanics defines the action S

 in the variational principle \[Delta] S = 0

.

Wave mechanics defines the phase \[CapitalTheta]

 in the wavelet propagator E^I \[CapitalTheta]

. 

They are related by

S(A->B) = ℏ \[CapitalTheta](A->B).

The Planck constant ℏ

 provides a natural unit for the action.

Therefore the particle and wave mechanics are connected by

The action accumulated by particle = the phase accumulated by wave.

This is also the guiding principle of the path integral quantization - a universal approach to promote any classical theory to its quantum version.

### Path Integral Quantization

#### Quantization of Matter

##### Classical Mechanics

Action: a function(al) associated to each possible path of a particle,

S[x] = ∫L(x, x., t)dt.

The principle of stationary action: the path taken by the particle x_(t)

 is the one for which the action is stationary (to first order), subject to boundary conditions: x_(t0) = x0

 (initial) and x_(t1) = x1

 (final).

\[Delta] S[x]\[RightBracketingBar]x = x_ = \[Delta]∫L(x, x., t)dt\[RightBracketingBar]x = x_ = 0.

This leads to the Euler-Lagrange equation (the equation of motion),

d/d t(∂L/∂x.) - ∂L/∂x = 0, 

such that the classical path x_(t)

 is the solution of Eq. (8). For a non-relativistic particle, the Lagrangian takes the form of L = T - V

, where T

 is the kinetic energy and V

 is the potential energy. For a relativistic particle, the action is simply the proper time of the path in the spacetime.

For a non-relativistic free particle L = (m / 2) x.^2

.
(i) Show that the stationary (classical) action S[x_]

 corresponding to the classical motion of a free particle travelling from (x0, t0)

 to (x1, t1)

 is S[x_] = m/2(x1 - x0)^2/t1 - t0

.
For this case of the free particle,
(ii) Show that the spatial derivative of the action ∂x1S[x_]

 is the momentum of the particle.
(iii) Show that the (negative) temporal derivative of the action  - ∂t1S[x_]

 is the energy of the particle.

A computability problem: the principle of stationary action is formulated as a deterministic global optimization, which requires exact computations and indefinitely long run time (on any computer).

Nature may not have sufficient computational resources to carry out the classical mechanics precisely. \[Implies] Classical mechanics might actually be realized only approximately as a stochastic global optimization, which is computationally more feasible. 

Quantum mechanics takes a stochastic approach to optimize the action, which is more natural than the deterministic approach of classical mechanics, if we assume only limited computational resource is available to nature.

Solution (HW 1)

(i) From classical equation of motion Eq. (8),

d/d t(∂L/∂x.) - ∂L/∂x = m x.. = 0, 

we find the solution of classical path x_ = v t + x0

. Using the boundary condition that x_(t0) = x0

, x_(t1) = x1

, we determine v = (x1 - x0) / (t1 - t0)

. The stationary action is the action evaluated on the classical path

S[x_] = ∫t0t11/2m v^2dt = m/2(x1 - x0)^2/t1 - t0.

(ii) Given Eq. (10),

∂x1S[x_] = mx1 - x0/t1 - t0 = m v = p.

(iii) Given Eq. (11),

 - ∂t1S[x_] = m/2(x1 - x0/t1 - t0)^2 = 1/2m v^2 = E.

##### Optimization by Interference

Each path is associated with an action. Quantum mechanics effectively finds the stationary action by the interference among all possible paths.

Example: find the stationary point(s) of

f(x) =  - x^2 + 2x^4.

Plot[ - x^2 + 2x^4, {x,  - 1, 1}, PlotStyle->Black, FrameLabel->{"\!\( x\)", "\!\(f(x)\)"}]

None
None
\!\(f(x)\)None
\!\( x\)None


Every point x

 is a legitimate guess of the solution.

Each point x

 is associated with an action f(x)

 (the objective function).

Raise the action f(x)

 to the exponent (as a phase): E^I f(x) / ℏ

 \[Implies] call it a “probability amplitude” contributed by the point x

.

A “Planck constant” ℏ = h / (2\[Pi])

 is introduced as a hyperparameter of the algorithm, to control “how quantum” the algorithm will be.

Contributions from all points must be collected and summed (integrated) up,

Z = ∫ - ∞∞E^I f(x) / ℏdx.

The result Z

 summarizes the probability amplitudes. It is known as the partition function of the stationary problem. But it is just a complex number, how do we make use of it? \[Implies] Well, we need to analyze how Z

 is accumulated. Each infinitesimal step in the integral -> a infinitesimal displacement on the complex plane

dz = E^I f(x) / ℏdx.

dx

 controls the infinitesimal step size,

E^I f(x) / ℏ

 controls the direction to make the displacement,

displacement dz

 is accumulated to form the partition function,

Z≡∫dz.

Let us see how the partition function is constructed.

For small h

 (classical limit)

Block[{f, h = 0.001, dx, acc, Z1, Z2}, 
	f[x_]:= - x^2 + 2x^4;
	dx = 0.01Sqrt[h];
	acc = ReIm@Prepend[Accumulate[Table[Exp[2\[Pi] I f[x] / h]dx, {x, dx / 2, 1 / 2 + 2Sqrt[2h], dx}]], 0];
	{Z1, Z2} = {NIntegrate[Exp[2\[Pi] I f[x] / h], {x, 0, 1 / (2Sqrt[3])}], NIntegrate[Exp[2\[Pi] I f[x] / h], {x, 1 / (2Sqrt[3]), ∞}]};
	Graphics[{{AbsoluteThickness[1], Line/@{acc,  - acc}}, {Arrowheads[0.08], 
	{Red, Arrow/@ReIm/@{{ - Z1 - Z2,  - Z1}, { - Z1, Z1}, {Z1, Z1 + Z2}}, Text["\!\(Z\_\("<>#1<>"\)\)", ReIm@#2, #3]&@@@{{"-1/2",  - Z1 - Z2 / 2, {1,  - 1}}, {"0", 0, { - 0.5,  - 1}}, {"1/2", Z1 + Z2 / 2, { - 1, 1}}}}, 
	{Blue, Arrow/@ReIm/@{{ - Z1 - Z2, Z1 + Z2}}, 
	Text["\!\( Z\)", ReIm@(Z1 + Z2) / 2, {0,  - 0.6}]}}}, 
	PlotLabel->Style["\!\(h="<>ToString[h]<>"\)", 14, Black], ImageSize->160]
]

\!\(h=0.001\)
\!\(Z\_\(-1/2\)\)\!\(Z\_\(0\)\)\!\(Z\_\(1/2\)\)\!\( Z\)

Z = Z - 1 / 2 + Z0 + Z1 / 2, 

Z

 can break up into three smaller contributions, which correspond to the contributions around the three stationary points: x = 0, ±1 / 2

.

Around the stationary point, phase changes slowly ∂xf(x)∼0

 \[Implies] constructive interference \[Implies] large contribution to the partition function.

The solutions of stationary points (classical solutions) emerge from interference due to their dominant contribution to the probability amplitude.

*More precisely, the partition function is actually evaluated with respect to the momentum k

,

Z(k)≡∫dz E^I k x≃Z - 1 / 2e^ - I k / 2 + Z0 + Z1 / 2E^I k / 2.

Then its Fourier spectrum Z~(x) = ∫dk Z(k)E^ - I k x

 will reveal the saddle points.

Block[{\[Epsilon] = 0.0001, ℏ = 0.001, a = 1 / 32, L = 3, Z}, 
Z[k_]:=NIntegrate[Exp[(I - \[Epsilon])( - x^2 + 2x^4) / ℏ]Exp[I k x], {x,  - ∞, ∞}];
ListLinePlot[RotateLeft[#, Ceiling[Length[#] / 2]]&[Abs[Fourier[Z/@Range[ - \[Pi] / a, \[Pi] / a, 2\[Pi] / L]]]^2], DataRange->{ - L / 2, L / 2}, FrameLabel->{"\!\( x\)", "\!\(\[LeftBracketingBar]Z\&~(x)\[RightBracketingBar]\^2\)"}, PlotStyle->Black, PlotRange->All, AspectRatio->1 / 2, ImageSize->200]]

None
None
\!\(\[LeftBracketingBar]Z\&~(x)\[RightBracketingBar]\^2\)None
\!\( x\)None


For intermediate h



Block[{f, h = 0.1, dx, acc, Z1, Z2}, 
	f[x_]:= - x^2 + 2x^4;
	dx = 0.01Sqrt[h];
	acc = ReIm@Prepend[Accumulate[Table[Exp[2\[Pi] I f[x] / h]dx, {x, dx / 2, 1 / 2 + Sqrt[2h], dx}]], 0];
	{Z1, Z2} = {NIntegrate[Exp[2\[Pi] I f[x] / h], {x, 0, 1 / (2Sqrt[3])}], NIntegrate[Exp[2\[Pi] I f[x] / h], {x, 1 / (2Sqrt[3]), ∞}]};
	Graphics[{{AbsoluteThickness[1], Line/@{acc,  - acc}}, {Arrowheads[0.08], 
	{Red, Dashed, Arrow/@ReIm/@{{ - Z1 - Z2,  - Z1}, { - Z1, Z1}, {Z1, Z1 + Z2}}, Text["\!\(Z\_\("<>#1<>"\)\)", ReIm@#2, #3]&@@@{{"-1/2",  - Z1 - Z2 / 2, { - 1,  - 1}}, {"0", 0, { - 1,  - 1}}, {"1/2", Z1 + Z2 / 2, {1, 1}}}}, 
	{Blue, Arrow/@ReIm/@{{ - Z1 - Z2, Z1 + Z2}}, Text["\!\( Z\)", 0.9ReIm@(Z1 + Z2), {0,  - 1}]}}}, 
	PlotLabel->Style["\!\(h="<>ToString[h]<>"\)", 14, Black], ImageSize->140]
]

\!\(h=0.1\)
\!\(Z\_\(-1/2\)\)\!\(Z\_\(0\)\)\!\(Z\_\(1/2\)\)\!\( Z\)

The decomposition of Z

 into three subdominant amplitudes is not very well defined. \[Implies] Quantum fluctuations start to smear out nearby stationary points.

For large h

 (quantum limit)

Block[{f, h = 10, dx, acc, Z1, Z2}, 
	f[x_]:= - x^2 + 2x^4;
	dx = 0.01Sqrt[h];
	acc = ReIm@Prepend[Accumulate[Table[Exp[2\[Pi] I f[x] / h]dx, {x, dx / 2, 1 / 2 + Sqrt[h / 2], dx}]], 0];
	{Z1, Z2} = {NIntegrate[Exp[2\[Pi] I f[x] / h], {x, 0, 1 / (2Sqrt[3])}], NIntegrate[Exp[2\[Pi] I f[x] / h], {x, 1 / (2Sqrt[3]), ∞}]};
	Graphics[{{AbsoluteThickness[1], Line/@{acc,  - acc}}, {Arrowheads[0.08], 
	{Blue, Arrow/@ReIm/@{{ - Z1 - Z2, Z1 + Z2}}, Text["\!\( Z\)", 0.9ReIm@(Z1 + Z2), {0,  - 1}]}}}, 
	PlotLabel->Style["\!\(h="<>ToString[h]<>"\)", 14, Black], ImageSize->160]
]

\!\(h=10\)
\!\( Z\)

Stationary points are indistinguishable if quantum fluctuations are too large. \[Implies] As if there is only one (approximate) stationary point around x = 0

.

If there is no sufficient resolution power, fine structures in the action landscape will be ignored by quantum mechanics. In this way, the computational complexity is controlled.

Generalize the same problem from stationary points to stationary paths (in classical mechanics) \[Implies] path integral formulation of quantum mechanics.

The Planck constant characterizes nature’s resolution (computational precision) of the action.

h = 6.62607004×10^ - 34J s.

Two nearby paths with an action difference smaller than the Planck constant can not be resolved.

 h

 is very small (in our everyday unit) \[Implies] our nature has a pretty high resolution of action \[Implies] no need to worry about the resolution limit in the macroscopic world \[Implies] classical mechanics works well.

However, in the microscopic world, nature’s resolution limit can be approached \[Implies] “round-off error” may occur \[Implies] one consequence is the quantization of atomic orbitals (discrete energy levels etc.).

##### Path Integral and Wave Function

Feynman’s principle: The probability pA->B

 for a particle to propagate from A

 to B

 is given by the square modulus of a complex number KA->B

 called the transition amplitude

pA->B = \[LeftBracketingBar]KA->B\[RightBracketingBar]^2.

The transition amplitude is given by adding together the contributions of all paths x

 from A

 to B

.

Block[{randpath}, 
randpath[p1_, p2_]:=BSplineCurve@Table[(1 - t)p1 + t p2 + {0, t(1 - t)RandomReal[{ - 1, 1}]}, {t, 0, 1, 0.05}];
Graphics[{{Opacity[0.5], AbsoluteThickness[1], Table[{ColorData[0, i], randpath[{0, 0}, {1, 0}]}, {i, 10}]}, Point/@{{0, 0}, {1, 0}}, 
Text["\!\( A\)", {0, 0}, {1.2, 0}], Text["\!\( B\)", {1, 0}, { - 1.2, 0}]}]]

\!\( A\)\!\( B\)

KA->B∝∫A->BD[x]E^I S[x] / ℏ.

The contribution of each particular path is proportional to E^I S[x] / ℏ

, where S[x]

 is the action of the path x

.

In the limit of ℏ->0

, the classical path x_

 (that satisfies \[Delta] S[x_] = 0

) will dominate the transition amplitude,

KA->B∼E^I S[x_] / ℏ.

Quantum mechanics reduces to classical mechanics in the limit of ℏ->0

.

To make the problem tractable, an important observation is that the transition amplitude satisfies a composition property

KA->B = ∫CKA->CKC->B.

This allows us the chop up time into slices t0<t1<…<tN - 1<tN

,

K(x0, t0)->(xN, tN) = ∫dx1…dxN - 1K(x0, t0)->(x1, t1)… K(xN - 1, tN - 1)->(xN, tN).

The “front” of transition amplitude propagates in the form of wave \[Implies] define the wavefunction \[Psi](x, t)

, which describes the probability amplitude to observe the particle at (x, t)

,

\[Psi](xk + 1, tk + 1) = ∫dxkK(xk, tk)->(xk + 1, tk + 1)\[Psi](xk, tk).

If we start with a initial wavefunction \[Psi](x, t0)

 concentrated at x0

, following the time evolution Eq. (23), the final wavefunction \[Psi](x, tN)

 will give the transition amplitude K(x0, t0)->(xN, tN) = \[Psi](xN, tN)

. \[Implies] It is sufficient to study the evolution of a generic wavefunction over one time step, then the dynamical rule can be applied iteratively.

Putting together Eq. (23) and Eq. (23),

\[Psi](xk + 1, tk + 1)∝∫D[x]exp(I/ℏS[x])\[Psi](xk, tk), 

this path integral involves multiple integrals:

for each given initial point xk

, integrate over paths x(t)

 subject to the boundary conditions x(tk) = xk

 and x(tk + 1) = xk + 1

,

finally integrate over choices of initial point xk

.

The Schrödinger equation is the equation that governs the time evolution of the wavefunction, which plays a central role in quantum mechanics. It can be derived from the path integral formulation in Eq. (24).

#### Deriving the Schrödinger Equation

##### Action in a Time Slice

The action of a free particle of mass m

,

S[x] = ∫t0t1dt 1/2m x.^2, 

where the particle starts from x(t0) = x0

, ends up at x(t1) = x1

.

Suppose the time interval \[Delta] t = t1 - t0

 is small, approximate the path of the particle by a straight line in the space-time,

x(t) = x0 + v t, 

where the velocity v

 will be a constant

v = x1 - x0/t1 - t0 = x1 - x0/\[Delta] t.

Plug into Eq. (26), we get an estimate of the action accumulated as the particle moves from x0

 to x1

 in time \[Delta] t

,

S[x] = 1/2m(x1 - x0/\[Delta] t)^2\[Delta] t = m/2\[Delta] t(x1 - x0)^2.

##### Path Integral in a Time Slice

The wavefunction \[Psi](x, t + \[Delta] t)

 in the next time slice is related to the previous one \[Psi](x, t)

 by

\[Psi](x1, t + \[Delta] t)∝∫dx0exp(I/ℏS[x])\[Psi](x0, t)
 = ∫dx0exp(I m/2ℏ \[Delta] t(x1 - x0)^2)\[Psi](x0, t).

The proportional sign “∝

” implies that the normalization factor is not determined yet. (It will be determined later.)

To proceed we expand \[Psi](x0, t)

 around x0->x1

, by defining x0 = x1 + a

, and Taylor expand with respect to a

,

\[Psi](x0, t) = \[Psi](x1 + a, t)
 = \[Psi](x1, t) + a \[Psi]^′(x1, t) + a^2/2!\[Psi]^″(x1, t) + a^3/3!\[Psi]^(3)(x1, t) + …
 = ∑n = 0∞a^n/n!∂x1n\[Psi](x1, t).

Substitute into Eq. (29),

\[Psi](x1, t + \[Delta] t)∝∑n = 0∞∫da exp(I m/2ℏ \[Delta] ta^2)a^n/n!∂x1n\[Psi](x1, t).

We pack everything related to the integral of a

 into a coefficient

\[Lambda]n≡∫da exp(I m/2ℏ \[Delta] ta^2)a^n/n!, 

then the time evolution is simply given by (we are free to replace x1

 by x

)

\[Psi](x, t + \[Delta] t)∝∑n = 0∞\[Lambda]n∂xn\[Psi](x, t).

The idea is that the time-evolved wavefunction can be expressed as the original wavefunction “dressed” by its (different orders of) derivatives.

Plot[{Exp[ - x^2 / 2],  - x Exp[ - x^2 / 2], (x^2 - 1)Exp[ - x^2 / 2]}, {x,  - 5, 5}, PlotRange->All, Epilog->{{#1, Text["\!\("<>#2<>" \[Psi](x)\)", #3]}&@@@{{Blue, "", {1.8, 0.9}}, {Red, "∂\_x", {3.5,  - 0.5}}, {Green, "∂\_x\%2", {2.2,  - 0.9}}}}, FrameLabel->{"\!\(x \)", "\!\(∂\_x\%n \[Psi](x)\)"}, ImageSize->200]

None
None
\!\(∂\_x\%n \[Psi](x)\)None
\!\(x \)None


For example, \[Psi](x)

 is a wave packet.

\[Psi](x) + \[Lambda] \[Psi]^′(x)

: shift the wave packet around.

\[Psi](x) + \[Lambda] \[Psi]^″(x)

: expand or shrink the wave packet.

Locality of Physics: the time evolution should only involve local modifications of the wavefunction \[Psi](x)

 (mostly within the light-cone) in each step.

Computing the Coefficients \[Lambda]n



The \[Lambda]n

 coefficient can be computed by Mathematica

\[Lambda]n = 1 + ( - 1)^n/2√\[Pi]/2^n\[CapitalGamma](1 + n/2)( - I m/2ℏ \[Delta] t)^ - 1 + n/2.

Evaluate the integral in Eq. (31) for \[Lambda]n

.

Use Mathematica. Denote the coefficient c = m / (2ℏ \[Delta]\[InvisibleComma]t)

 for conciseness.

FunctionExpand[Integrate[Exp[I c a^2]a^n / n!, {a,  - ∞, ∞},  GenerateConditions->False]]

2^ - 1 - n (1 + ( - 1)^n) ( - I c)^ - 1/2 - n/2 √\[Pi]/Gamma[1 + n/2]



The first term (1 + ( - 1)^n) / 2

 just discriminates even and odd n

. 

1 + ( - 1)^n/2 = \[Piecewise]	1	if n∈even, 	
0	if n∈odd.		

So as long as n∈odd

, \[Lambda]n = 0

. We only need to consider the case of even n

.

For even n

, the first several \[Lambda]n

 are given by

\[Lambda]0 = √\[Pi]( - I m/2ℏ \[Delta] t)^ - 1 / 2, 
\[Lambda]2 = √\[Pi]/4( - I m/2ℏ \[Delta] t)^ - 3 / 2 = I /4(2ℏ \[Delta] t/m)\[Lambda]0, 
\[Lambda]4 = √\[Pi]/32( - I m/2ℏ \[Delta] t)^ - 5 / 2 =  - 1/32(2ℏ \[Delta] t/m)^2\[Lambda]0, 
…

Compute the first several \[Lambda]n

 for even integer n

 using Eq. (33).

Block[{\[Lambda]}, 
\[Lambda] = Association@Table[
	n->Sqrt[\[Pi]] / (2^n Gamma[1 + n / 2])( - I c)^( - (1 + n) / 2), {n, 0, 4, 2}];
{\[Lambda], \[Lambda] / \[Lambda][0]}]

{\[LeftAssociation]0->√\[Pi]/√ - I c, 2->√\[Pi]/4 ( - I c)^3 / 2, 4->√\[Pi]/32 ( - I c)^5 / 2\[RightAssociation], \[LeftAssociation]0->1, 2->I/4 c, 4-> - 1/32 c^2\[RightAssociation]}

##### Determining the Normalization

Plugging the results of \[Lambda]n

 in Eq. (33) into Eq. (33), we get

\[Psi](x, t + \[Delta] t)∝\[Lambda]0(1 + I/4(2ℏ \[Delta] t/m)∂x2 - 1/32(2ℏ \[Delta] t/m)^2∂x4 + …)\[Psi](x, t).

If we take \[Delta] t = 0

, all higher order terms vanishes,

\[Psi](x, t)∝\[Lambda]0\[Psi](x, t).

So obviously, the normalization factor should be such to cancelled out \[Lambda]0

.

So we should actually write (in equal sign) that

\[Psi](x, t + \[Delta] t) = (1 + I/4(2ℏ \[Delta] t/m)∂x2 - 1/32(2ℏ \[Delta] t/m)^2∂x4 + …)\[Psi](x, t).

Taking the Limit of \[Delta] t->0



Let us consider the time derivative of the wavefunction

∂t\[Psi](x, t) = lim\[Delta] t->0\[Psi](x, t + \[Delta] t) - \[Psi](x, t)/\[Delta] t
 = lim\[Delta] t->01/\[Delta] t(I/4(2ℏ \[Delta] t/m)∂x2 - 1/32(2ℏ \[Delta] t/m)^2∂x4 + …)\[Psi](x, t)

Only the first term survives under the limit \[Delta] t->0

,

∂t\[Psi](x, t) = I ℏ/2m∂x2\[Psi](x, t).

All the higher order terms will have higher powers in \[Delta] t

, so they should all vanish under the limit \[Delta] t->0

.

By convention, we write Eq. (38) in the following form

I ℏ∂t\[Psi](x, t) =  - ℏ^2/2m∂x2\[Psi](x, t).

This is the Schrödinger equation that governs the time evolution of the wavefunction of a free particle.

##### Adding Potential Energy

Now suppose the particle is not free but moving in a potential V(x)

, the action changes to

S = ∫t0t1dt (1/2m x.^2 - V(x)), 

The additional action that will be accumulated over time \[Delta] t

 will be

\[CapitalDelta] S =  - V(x)\[Delta] t.

Eventually this cause an additional phase shift in the wavefunction

\[Psi](x, t + \[Delta] t) = E^I \[CapitalDelta] S / ℏ\[Psi]0(x, t + \[Delta] t)
 = E^ - I V(x)\[Delta] t / ℏ\[Psi]0(x, t + \[Delta] t)
 = (1 - I/ℏV(x)\[Delta] t + …)\[Psi]0(x, t + \[Delta] t), 

where \[Psi]0

 is the expected wavefunction at t + \[Delta] t

 without the potential. Combining with the result in Eq. (40), to the first order of \[Delta] t

 we have

\[Psi](x, t + \[Delta] t) = (1 - I/ℏV(x)\[Delta] t + …)(1 + I/4(2ℏ \[Delta] t/m)∂x2 + …)\[Psi](x, t)
 = (1 + I/4(2ℏ \[Delta] t/m)∂x2 - I/ℏV(x)\[Delta] t + …)\[Psi](x, t).

Then after taking the \[Delta] t->0

 limit, we arrive at

∂t\[Psi](x, t) = I ℏ/2m∂x2\[Psi](x, t) - I/ℏV(x)\[Psi](x, t), 

or equivalently written as

I ℏ∂t\[Psi](x, t) =  - ℏ^2/2m∂x2\[Psi](x, t) + V(x)\[Psi](x, t).

This is the Schrödinger equation that governs the time evolution of the wavefunction \[Psi](x, t)

 of a particle moving in a potential V(x)

.

##### Time-Independent Case

If the potential function V(x)

 is independent of time t

, the problem can be simplified by a separation of variables for \[Psi](x, t)

 in the form of

\[Psi](x, t) = \[Psi](x)E^ - I E t / ℏ.

Substitute Eq. (42) into Eq. (42), we arrived as the stationary Schrödinger equation as an eigen equation,

( - ℏ^2/2m∂x2 + V(x))\[Psi](x) = E \[Psi](x).

Derive Eq. (42) from Eq. (42).

Left-hand-side:

I ℏ∂t\[Psi](x, t) = I ℏ∂t(\[Psi](x)E^ - I E t / ℏ)
 = I ℏ(∂tE^ - I E t / ℏ)\[Psi](x)
 = I ℏ( - I E/ℏE^ - I E t / ℏ)\[Psi](x)
 = E \[Psi](x) E^ - I E t / ℏ.

Right-hand-side:

 - ℏ^2/2m∂x2\[Psi](x, t) + V(x)\[Psi](x, t)
 =  - ℏ^2/2m∂x2\[Psi](x)E^ - I E t / ℏ + V(x)\[Psi](x)E^ - I E t / ℏ
 = ( - ℏ^2/2m∂x2 + V(x))\[Psi](x)E^ - I E t / ℏ.

Equal both sides and eliminate the common phase factor E^ - I E t / ℏ

,

( - ℏ^2/2m∂x2 + V(x))\[Psi](x) = E \[Psi](x).



The solution to the eigen problem provides

En

: eigen energies,

\[Psi]n(x)

: corresponding eigen wavefunctions,

both labeled by the eigenstate index n

.

#### Semiclassical Approach

##### WKB Approximation (General)

WKB (Wentzel-Kramers-Brillouin) approximation:  a method for solving the Schrödinger equation in the semiclassical limit where ℏ->0

. 

Goal: find approximate solution of Eq. (42), keeping only the leading quantum effects (i.e., the leading terms of ℏ

).

Postulate a solution for \[Psi](x, t)

 of the form

\[Psi](x, t) = A(x, t)E^I S(x, t) / ℏ.

Substitute into the Schrödinger equation, 

To the leading (0th) order of ℏ

, the action function S(x, t)

 is governed by

∂tS(x, t) + 1/2m(∂xS(x, t))^2 + V(x) = 0, 

also known as the Hamilton-Jacobi equation.

In general, given the Hamiltonian function H(x, p, t)

 of the system, the Hamilton-Jacobi equation reads

∂tS(x, t) + H(x, ∇S(x, t), t) = 0.

Eq. (43) is a special case of Eq. (43) for a particle moving in 1D with H(x, p, t) = 1/2mp^2 + V(x)

.

Physical meaning of action derivatives:

Energy: (negative) rate of action accumulation in time

E =  - ∂tS.

Momentum: action accumulation rate in space (along every direction), or the spatial gradient of action

p = ∇S.

To the next leading (1st) order of ℏ

, 

∂tA(x, t) + 1/2m(2∂xA(x, t)∂xS(x, t) + A(x, t) ∂x2S(x, t)) = 0, 

which determines A(x, t)

 from the solution of S(x, t)

.

Derive Eq. (44) and Eq. (44).

Substitute Eq. (44) into Eq. (44),

I ℏ∂t(A E^I S / ℏ) = ( - ℏ^2/2m∂x2 + V)A E^I S / ℏ.

Compute the derivatives,

I ℏ∂t(A E^I S / ℏ) = I ℏ (∂tA E^I S / ℏ + A ∂tE^I S / ℏ)
 = I ℏ (∂tA E^I S / ℏ + I/ℏA ∂tS E^I S / ℏ)
 = (I ℏ ∂tA  - A ∂tS)E^I S / ℏ, 

 - ℏ^2/2m∂x2(A E^I S / ℏ) =  - ℏ^2/2m∂x(∂xA E^I S / ℏ + A ∂xE^I S / ℏ)
 =  - ℏ^2/2m∂x(∂xA E^I S / ℏ + I/ℏA ∂xS E^I S / ℏ)
 =  - ℏ^2/2m∂x((∂xA + I/ℏA ∂xS)E^I S / ℏ)
 =  - ℏ^2/2m(∂x(∂xA + I/ℏA ∂xS)E^I S / ℏ + (∂xA + I/ℏA ∂xS)∂xE^I S / ℏ)
 =  - ℏ^2/2m((∂x2A + I/ℏ∂xA ∂xS + I/ℏA ∂x2S)E^I S / ℏ + I/ℏ(∂xA + I/ℏA ∂xS)∂xS E^I S / ℏ)
 =  - ℏ^2/2m(∂x2A + 2I/ℏ∂xA ∂xS + I/ℏA ∂x2S - 1/ℏ^2A (∂xS)^2)E^I S / ℏ
 = 1/2m( - ℏ^2∂x2A - 2I ℏ∂xA ∂xS - I ℏ A ∂x2S + A (∂xS)^2)E^I S / ℏ.

Collecting terms in order of ℏ

,

\[ScriptCapitalO](ℏ^0)

: to the leading order, we have

 - ∂tS A E^I S / ℏ = (1/2m(∂xS)^2 + V)A E^I S / ℏ.

Eliminating common factors, we obtain

∂tS + 1/2m(∂xS)^2 + V = 0.

\[ScriptCapitalO](ℏ^1)

: to the next leading order, we have

I ℏ ∂tA E^I S / ℏ = 1/2m( - 2I ℏ∂xA ∂xS - I ℏ A ∂x2S)E^I S / ℏ, 

Eliminating common factors, we obtain

∂tA  + 1/2m(2∂xA ∂xS + A ∂x2S) = 0.



The WKB approach amounts to solving Eq. (44) and Eq. (44), then substitute the solution S(x, t)

 and A(x, t)

 into Eq. (44) to construct the approximate solution for the wavefunction \[Psi](x, t)

.

Solutions of Hamilton-Jacobi Equation

###### Particle in the Free Space

For a particle moving in the free space, the potential will be flat

V(x) = 0.

Substitute into the Hamilton-Jacobi equation Eq. (45), depending on the initial condition

S(x, 0) = p x = m v0x, 

v0

 is the initial velocity of the particle at time t = 0

,

p = m v0

 is the momentum of the particle, which will remain conserved,

the solution of S(x, t)

 is

S(x, t) = p x - E t
 = m v0x - 1/2m v02t, 

E = 1/2mp^2 = 1/2m v02

 is the (kinetic) energy of the particle.

S(x, t)

 looks like:

Manipulate[DynamicModule[{m = 1, V, S, xmin, xmax, tmin, tmax}, 
V[x_]:=0;
{{xmin, xmax}, {tmin, tmax}} = {{ - 5, 5}, { - 5, 5}};
Quiet[S = NDSolveValue[{D[S[x, t], t] + (D[S[x, t], x])^2 / (2m) + V[x] == 0, S[x, 0] == m v0 x}, S, {x, xmin, xmax}, {t, tmin, tmax}]];
Block[{cfun = "Rainbow"}, 
ContourPlot[S[x, t], {x, xmin, xmax}, {t, tmin, tmax}, PlotRange->All, Contours->Range[ - 200, 200, 2], ContourStyle->Directive[AbsoluteThickness[1], Opacity[0.4], Black], ColorFunction->cfun, FrameLabel->{"\!\( x\)", "\!\( t\)"}, PlotLabel->"\!\(S(x,t)\)", ImageSize->180]]], {{v0, 1, "\!\(v\_0\)"},  - 3, 3, ImageSize->Small}, Paneled->False]

-Dynamic-

The contours of S(x, t)

 are wave fronts (equal-phase surface) in the spacetime.

The solution S(x, t)

 in Eq. (46) corresponds to a plane wave solution of the wavefunction

\[Psi](x, t) = E^I S(x, t) / ℏ
 = exp(I/ℏ(p x - E t)).

This turns out to be the exact solution of the Schrödinger equation for a free particle (the WKB approximation becomes exact in this case).

###### Particle under a Constant Force

In a linear potential,

V(x) =  - F x, 

the particle will experience a constant force F:= - ∂xV(x)

. Plugging V(x)

 in the Hamilton-Jacobi equation Eq. (47), 

∂tS + 1/2m(∂xS)^2 + V(x) = 0, 

the solution of S(x, t)

 look like:

Manipulate[DynamicModule[{V, S, xmin, xmax, tmin, tmax}, 
V[x_]:= - F x;
{{xmin, xmax}, {tmin, tmax}} = {{ - 5, 5}, { - 5, 5}};
Quiet[S = NDSolveValue[{D[S[x, t], t] + (D[S[x, t], x])^2 / (2m) + V[x] == 0, S[x, 0] == m v0 x}, S, {x, xmin, xmax}, {t, tmin, tmax}]];
Block[{cfun = "Rainbow"}, 
Show[ContourPlot[S[x, t], {x, xmin, xmax}, {t, tmin, tmax}, PlotRange->All, Contours->Range[ - 200, 200, 2], ContourStyle->Directive[AbsoluteThickness[1], Opacity[0.4], Black], ColorFunction->cfun, FrameLabel->{"\!\( x\)", "\!\( t\)"}, PlotLabel->"\!\(S(x,t)\)", ImageSize->180], ContourPlot[x == 1 / 2(F / m)t^2 + v0 t + m v0^2 / (2F), {x, xmin, xmax}, {t, tmin, tmax}, ContourStyle->Black]]]], 
{{m, 1}, 0.5, 10, ImageSize->Small}, {{F, 1},  - 2, 2, ImageSize->Small}, 
{{v0, 0, "\!\(v\_0\)"},  - 3, 3, ImageSize->Small}, Paneled->False]

-Dynamic-

In the m->∞

 limit, ∂tS =  - V(x)

, such that

S(x, t) =  - V(x) t = F x t, 

creating a growing spatial gradient of the action

p = ∂xS = F t, 

corresponding to a momentum that increases in time.

When m

 is finite, the kinetic energy (∂xS)^2 / (2m)

 grows with the momentum p = ∂xS

, which also contributes to the total energy and alters the rate of action accumulation in time. \[Implies] This leads to curvature in the constant-action contours, signaling acceleration in the particle’s motion.

The classical trajectory (in black) of the particle corresponds to the family of stationary points of S(x, t)

 in the spacetime, which turns out to form a parabola

x = 1/2a (t + v0/a)^2.

v0 = x.(t = 0)

 is the initial velocity of the particle at time t = 0

,

a

 is the acceleration of the particle. It increases with F

 and decreases with m

, and can be verified to follow

a = F/m, 

which recovers Newton’s 2nd law (F = m a

).

##### WKB Approximation (Time-Independent)

In the time-independent case, the energy E

 is a conserved quantity, the action can be separated as

S(x, t) = W(x) - E t, 

meaning that \[Psi](x, t) = \[Psi](x)E^ - I E t / ℏ

 with

\[Psi](x) = A(x)E^I W(x) / ℏ.

The spatial part W(x)

 of the action satisfies the stationary Hamilton-Jacobi equation, reduced from Eq. (53),

1/2m(∂xW(x))^2 + V(x) = E.

Derive Eq. (54) from Eq. (54).

Substitute Eq. (54) into Eq. (54),

 - E + 1/2m(∂xW(x))^2 + V(x) = 0, 

which becomes Eq. (54) by moving E

 to the right hand side.



Given a time-independent Hamiltonian H(x, p)

, a more general form of Eq. (54) is

H(x, ∇W(x)) = E.

Eq. (55) can be solved by introducing the momentum function p(x)

 - the rate that the action is accumulated in space,

p(x):=∂xW(x), 

such that Eq. (55) becomes an algebraic equation

p(x)^2/2m + V(x) = E, 

with the solution(s) given by

p(x) = ±√2m (E - V(x)).

Then the solution of W(x)

 can be reconstructed by integration

W(x) = ∫^xp(x^′)dx^′ = ∫^x√2m (E - V(x^′))dx^′.

Eq. (57) also reduces to its stationary form

∂xlog A(x) =  - 1/2∂xlog p(x), 

whose solution is

A(x) = C/√p(x).

Derive Eq. (59).

Note that A(x)

 no longer has t

 dependence in the stationary case, we have ∂tA = 0

, hence Eq. (59) reads

1/2m(2∂xA∂xW + A∂x2W) = 0, 

therefore

2∂xA∂xW =  - A∂x2W
\[Implies]∂xA/A =  - 1/2∂x2W/∂xW
\[Implies]∂xlog A =  - 1/2∂xlog(∂xW).

Given that p = ∂xW

,

∂xlog A =  - 1/2∂xlog p.



Putting Eq. (59) and Eq. (59) together into Eq. (59), the WKB wavefunction for a quantum state of energy E

 is

\[Psi](x)≈C/√p(x)exp(I/ℏ∫^xp(x^′)dx^′), 

where p(x) = ±√2m (E - V(x))

 as in Eq. (59), and C

 serves as the normalization constant for \[Psi](x)

 to ensure ∫\[LeftBracketingBar]\[Psi](x)\[RightBracketingBar]^2 = 1

.

Classically allowed regions (V(x)<E

):

p(x)∈\[DoubleStruckCapitalR]

, the WKB wavefunction \[Psi](x)

 exhibits wavy behavior.

Both ±

 solutions of p(x)

 are valid, corresponding to right-moving and left-moving waves.

Classically forbidden regions (V(x)>E

):

p(x)∈\[DoubleStruckCapitalI]

, the WKB wavefunction \[Psi](x)

 exhibits exponential decay (or grow) behavior

\[Psi](x)≈C/√\[LeftBracketingBar]p(x)\[RightBracketingBar]exp(∓1/ℏ∫^x\[LeftBracketingBar]p(x^′)\[RightBracketingBar]dx^′).

Only one of the ±

 solutions of p(x)

 will be valid, which corresponding to the decaying wave, as the particle’s probability density must diminish as it enters the classical forbidden regions. The invalid solution will correspond to an growing wave.

Transition region (V(x)->E

): p(x)->0

, the amplitude diverges as p(x)^ - 1 / 2

, and the WKB wavefunction is ill-defined. Joining the WKB wave function across the transition region is a rather complicated task, more can be found in Ref. [0]. 

Examples of WKB approximations:

Scattering states

Quantum climbing: the potential top is lower than the energy level E

.

Block[{m = 1, \[CapitalEpsilon] = 2, ℏ = 0.05, dx = 0.02, V, p, W, \[Psi], xmin, xmax}, 
	V[x_]:=1.9Exp[ - x^2];
	p[x_]:=Sqrt[2m(\[CapitalEpsilon] - V[x])];
	W[x_?NumericQ]:=Quiet[NIntegrate[p[x1], {x1,  - 3, x}]];
	\[Psi][x_?NumericQ]:=Exp[I W[x] / ℏ] / Sqrt[Abs[p[x]]];
	{xmin, xmax} = { - 3, 3};
	Plot[V[x], {x, xmin, xmax}, PlotStyle->Black, Axes->False, FrameLabel->{"\!\( x\)", "\!\(V(x)\)"}, Prolog->{AbsoluteThickness[1], LightGray, InfiniteLine[{#, \[CapitalEpsilon]}&/@{0, 1}]}, Epilog->{Translate[{Red, Cases[ListLinePlot[Block[{data}, data = Table[If[Abs[p[x]]dx>ℏ / 8, {x, Re@\[Psi][x]}, {x, Null}], {x, xmin, xmax, dx}];
	data[[All, 2]] = 0.5data[[All, 2]] / Abs[data[[1, 2]]];data]], _Line, ∞], Text["\!\(Re \[Psi](x)\)", {2, 1}, {0, 0}]}, {0, \[CapitalEpsilon]}]}, PlotRange->{0, 4}, PlotRangePadding->{Scaled[0.02], Scaled[0.05]}, ImageSize->180]
]

None
None
\!\(V(x)\)None
\!\( x\)None


Quantum tunneling: the potential top is higher than the energy level E

.

Block[{m = 1, \[CapitalEpsilon] = 2, ℏ = 0.05, dx = 0.02, V, p, W, \[Psi], xmin, xmax}, 
	V[x_]:=2.1Exp[ - x^2];
	p[x_]:=Sqrt[2m(\[CapitalEpsilon] - V[x])];
	W[x_?NumericQ]:=Quiet[NIntegrate[p[x1], {x1,  - 3, x}]];
	\[Psi][x_?NumericQ]:=Exp[I W[x] / ℏ] / Sqrt[Abs[p[x]]];
	{xmin, xmax} = { - 3, 3};
	Plot[V[x], {x, xmin, xmax}, PlotStyle->Black, Axes->False, FrameLabel->{"\!\( x\)", "\!\(V(x)\)"}, Prolog->{AbsoluteThickness[1], LightGray, InfiniteLine[{#, \[CapitalEpsilon]}&/@{0, 1}]}, Epilog->{Translate[{Red, Cases[ListLinePlot[Block[{data}, data = Table[If[Abs[p[x]]dx>ℏ / 10, {x, Re@\[Psi][x]}, {x, Null}], {x, xmin, xmax, dx}];
	data[[All, 2]] = 0.5data[[All, 2]] / Abs[data[[1, 2]]];data]], _Line, ∞], Text["\!\(Re \[Psi](x)\)", {2, 1}, {0, 0}]}, {0, \[CapitalEpsilon]}]}, PlotRange->{0, 4}, PlotRangePadding->{Scaled[0.02], Scaled[0.05]}, ImageSize->180]
]

None
None
\!\(V(x)\)None
\!\( x\)None


Bound state: the potential grows higher than the energy level E

 towards both sides.

Block[{m = 1, \[CapitalEpsilon] = 2, ℏ = 0.05, dx = 0.02, V, xmin, xmax, p, W, \[Psi]}, 
	V[x_]:=x^2 / 2 - x^3 / 6 + x^4 / 24;
	{xmin, xmax} = x/.NSolve[V[x] == \[CapitalEpsilon], x, Reals];
	p[x_]:=If[\[CapitalEpsilon]>V[x], Sqrt[2m(\[CapitalEpsilon] - V[x])], Sign[x]Sqrt[2m(\[CapitalEpsilon] - V[x])]];
	W[x_?NumericQ]:=Quiet[NIntegrate[p[x1], {x1, 0, x}]];
	\[Psi][x_?NumericQ]:=Exp[I W[x] / ℏ] / Sqrt[Abs[p[x]]];
	Plot[V[x], {x,  - 2, 3}, PlotStyle->Black, Axes->False, FrameLabel->{"\!\( x\)", "\!\(V(x)\)"}, Prolog->{{AbsoluteThickness[1], LightGray, InfiniteLine[{#, \[CapitalEpsilon]}&/@{0, 1}], Table[InfiniteLine[{x, #}&/@{0, 1}], {x, {xmin, xmax}}]}, {Text["\!\(x\_min\)", {xmin, 0}, {0,  - 0.5}], Text["\!\(x\_max\)", {xmax, 0}, {0,  - 0.5}]}}, Epilog->{Translate[{Red, Cases[ListLinePlot[Block[{data}, data = Table[If[Abs[p[x]]dx>ℏ / 6, {x, Re@\[Psi][x]}, {x, Null}], {x,  - 2, 3, dx}];
	data[[All, 2]] = data[[All, 2]] / Max[Abs[DeleteCases[data[[All, 2]], Null]]];data]], _Line, ∞], Text["\!\(Re \[Psi](x)\)", {0, 1}]}, {0, \[CapitalEpsilon]}]}, ImageSize->180]
]

None
None
\!\(V(x)\)None
\!\( x\)None


xmin

, xmax

: two classical turning points, at which E = V(x)

 and the particle will be bounced back in the classical limit.

Total phase acquired by the wavefunction between the classical turning points is given by

\[CapitalTheta](xmin->xmax) = 1/ℏW(xmin->xmax), 

where W

 is the corresponding action,

W(xmin->xmax) = ∫xminxmaxp(x)dx = ∫xminxmax√2m (E - V(x))dx.

Wikipedia, WKB approximation <https://en.wikipedia.org/wiki/WKB_approximation>.

##### Bohr-Sommerfeld Quantization

The WKB approximation can be used to estimate the bound state eigenenergies. 

Intuition: Consider a sine wave, with one node pinned to xmin

, how to pin another node to xmax

 by varying \[CapitalTheta](xmin->xmax)

?

Manipulate[Block[{k, col}, {k, col} = If[Abs[Mod[\[CapitalTheta] / \[Pi], 1,  - 1 / 2]]<0.1, {Round[\[CapitalTheta] / \[Pi]]\[Pi], Green}, {\[CapitalTheta], Red}];Plot[Sin[k x], {x,  - 0.5, 1.5}, PlotStyle->col, Prolog->{{LightGray, AbsoluteThickness[1], InfiniteLine[{#, 0}&/@{0, 1}], Table[InfiniteLine[{x, #}&/@{0, 1}], {x, {0, 1}}]}}, Epilog->{{Opacity[0.5], Rectangle[{ - 1,  - 2}, {0, 2}], Rectangle[{1,  - 2}, {2, 2}]}}, PlotLabel->StringTemplate["\!\(\[CapitalTheta](x\_min->x\_max)=`1`\[Pi]\)"][If[# == 1, "", #]&@(k / \[Pi])], Axes->False, FrameLabel->{None, "\!\(\[Psi](x)\)"}, FrameTicks->{{None, None}, {{{0, "\!\(x\_min\)"}, {1, "\!\(x\_max\)"}}, None}}, PlotRange->{ - 1.2, 1.2}, AspectRatio->1 / 3, ImageSize->220]], {{\[CapitalTheta], \[Pi]}, 0.5\[Pi], 5\[Pi]}, Paneled->False]

-Dynamic-

Bohr-Sommerfeld quantization condition: To confine the wave in the region [xmin, xmax]

, we must pin the wave nodes on both turning points, which requires the phase acquired between the turning points to be an integer of \[Pi]

, i.e.

\[CapitalTheta](xmin->xmax) = 1/ℏ∫xminxmax√2m (E - V(x))dx = n \[Pi], 

for n = 1, 2, 3, …

. 

Example: Harmonic Oscillator

Consider the potential

V(x) = 1/2m \[Omega]^2x^2.

\[Omega] - angular frequency of the oscillator.

Plot[1 / 2 x^2, {x,  - 3, 3}, GridLines->{{ - 2, 0, 2}, {2}}, Epilog->{Text["\!\(-x\_0\)", { - 2, 0}, {0,  - 0.6}], Text["\!\(x\_0\)", {2, 0}, {0,  - 0.6}], Text["\!\( E\)", { - 3, 2}, { - 1, 0}]}, Axes->False, PlotStyle->Black, FrameLabel->{"\!\( x\)", "\!\(V(x)\)"}, ImageSize->180]

None
None
\!\(V(x)\)None
\!\( x\)None


Let ±x0

 be the turning points, at which E = V(x)

, such that

E = 1/2m \[Omega]^2x02.

The Bohr-Sommerfeld quantization condition Eq. (64) requires

m \[Omega]/ℏ∫ - x0x0√x02 - x^2dx = \[Pi] m \[Omega] x02/2ℏ = n \[Pi], 

which sets x02 = 2n ℏ / (m \[Omega])

. By Eq. (65), the energy that correspond to such turning points is

En = n ℏ \[Omega], 

for n = 1, 2, 3, …

.

This predicts the energy quantization with the correct energy level spacing ℏ \[Omega]

. Compare with the exact eigenenergies

En = (n + 1/2)ℏ \[Omega], 

the only missing part is the vacuum energy 1/2ℏ \[Omega]

, which requires more rigorous quantum treatment.

Consider a potential where energy grows linearly with the distance of the particle from the origin: 
V(x) = F\[LeftBracketingBar]x\[RightBracketingBar]

, 
where F

 is a constant with the unit of force. Use the Bohr-Sommerfeld quantization condition to estimate the energy levels in this potential. To which power do they scale with the level index n

?

Solution (HW 2)

Let ±x0

 be the turning points where E = V(x)

, such that

E = F x0.

Then the Bohr-Sommerfeld quantization condition requires that

n \[Pi] = 1/ℏ∫ - x0x0dx√2m F (x0 - \[LeftBracketingBar]x\[RightBracketingBar])
 = 2√2m F/ℏ∫0x0dx√x0 - x
 = 4√2m F/3ℏx03 / 2.

By Eq. (69), expressing x0

 in terms of E / F

, Eq. (69) becomes

4√2m F/3ℏ(En/F)^3 / 2 = n \[Pi], 

or

En = (3\[Pi] ℏ F n/4√2m)^2 / 3.

The energy level for linear potential scale like n^2 / 3

.

