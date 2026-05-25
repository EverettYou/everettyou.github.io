---
layout: page
title: 3-4-5-0 Luttinger Liquid Wave Simulator
subtitle: Browser-side demo for compact-boson scattering near an SMG interface
sitemap: false
robots: noindex,nofollow
---

<style>
.demo-frame-wrap {
  margin: 1.5rem 0 2rem;
  border: 1px solid rgba(40, 44, 48, 0.16);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 12px 32px rgba(40, 44, 48, 0.08);
}
.demo-frame {
  display: block;
  width: 100%;
  height: min(1020px, 92vh);
  border: 0;
  background: #f6f3ec;
}
.demo-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin: 0.75rem 0 1.5rem;
}
.demo-actions a {
  display: inline-block;
  padding: 0.55rem 0.8rem;
  border: 1px solid rgba(40, 44, 48, 0.18);
  border-radius: 999px;
  text-decoration: none;
}
</style>

This unlisted project page hosts a small numerical playground for the bosonized
3-4-5-0 model.  The simulator runs entirely in the visitor's browser; GitHub
Pages only serves static files.

<div class="demo-actions">
  <a href="./simulator.html">Open the simulator full screen</a>
</div>

<div class="demo-frame-wrap">
  <iframe class="demo-frame" src="./simulator.html" title="3-4-5-0 Luttinger Liquid Wave Simulator"></iframe>
</div>

## Setup

The four fermion flavors are bosonized by compact fields

$$
\phi_I \sim \phi_I+2\pi,\qquad \psi_I\sim e^{i\phi_I},
\qquad I=1,2,3,4 .
$$

The quadratic Luttinger liquid used in the demo is

$$
\mathcal{L}_0=
\frac{1}{4\pi}
\left(
K_{IJ}\partial_t\phi_I\partial_x\phi_J
-V_{IJ}\partial_x\phi_I\partial_x\phi_J
\right),
$$

with

$$
K=\operatorname{diag}(1,1,-1,-1),\qquad V_{IJ}=\delta_{IJ}.
$$

Thus \(\phi_1,\phi_2\) are left-moving fields and
\(\phi_3,\phi_4\) are right-moving fields in the free region.

## SMG Interface

The symmetric mass generation interaction is represented by two null-vector
cosines

$$
\ell_1=(1,-2,1,2)^\intercal,\qquad
\ell_2=(-3,1,1,-3)^\intercal,
$$

and

$$
\mathcal{L}_{\mathrm{int}}
=
g_1(x)\cos(\ell_1^\intercal\phi)
+
g_2(x)\cos(\ell_2^\intercal\phi).
$$

The default simulation uses the \(\mathbb{Z}_2\)-symmetric case

$$
g_1(x)=g_2(x)=g(x),
$$

where \(g(x)\) is a sigmoid profile.  Choosing the interaction on the right
uses

$$
g(x)=\frac{g_0}{1+\exp[-(x-c)/w]},
$$

while choosing the interaction on the left reflects the profile about the
interface center \(c\).

## Equation Solved

The browser code evolves the once-integrated form of the nonlinear equation of
motion associated with

$$
K_{IJ}\partial_t\partial_x\phi_J
-V_{IJ}\partial_x^2\phi_J
+2\pi g(x)\ell_{1I}\sin(\ell_1^\intercal\phi)
+2\pi g(x)\ell_{2I}\sin(\ell_2^\intercal\phi)
=0.
$$

The compact fields are displayed modulo \(2\pi\) in the interval
\([-\pi,\pi)\).  The shaded monitor background encodes the local strength
of \(g(x)\), from white in the gapless region to a darker tone in the SMG
region.

## Notes

This demo is meant as an exploratory visualization, not yet a controlled
scattering calculation.  In particular, the nonlinear SMG region can be stiff,
and the numerical result should be checked against the free-wave solution by
setting \(g_0=0\).
