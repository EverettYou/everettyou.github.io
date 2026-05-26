---
layout: page
title: 3-4-5-0 Model Simulator
subtitle: Compact-Boson Scattering near an SMG Interface
hide: true
---

<link rel="stylesheet" href="./app.css">

## Overview

The **3-4-5-0 model** is a 1+1D theory of four chiral fermions carrying U(1)
charges $$(3,4,5,0)$$. It is an example of a fermionic system that
admits **symmetric mass generation (SMG)**: a fully symmetric, non-perturbative
interaction can gap every flavor *without* breaking the U(1) symmetry, even
though no fermion bilinear mass exists. After bosonization the four fermions
become four compact scalar fields propagating as a four-component Luttinger
liquid, and the SMG interaction becomes two cosine perturbations built from
Haldane null vectors. The physical question this page is built around is:
*how does a chiral mode scatter off a region where the SMG interaction is
turned on?* It is the continuum, real-time counterpart of the Wang–Wen
mirror-decoupling and Tong *et al.* monopole-scattering setups.

## Theory

### Bosonized Luttinger liquid

The four fermion flavors $$\psi_I$$, $$I=1,2,3,4$$, are bosonized by four
compact scalar fields

$$
\phi_I \sim \phi_I+2\pi,
\qquad
\psi_I\sim e^{i\phi_I}.
$$

In the standard 3-4-5-0 ordering, the first two flavors are left-movers and
the last two are right-movers. The free Luttinger Lagrangian is

$$
\mathcal{L}_0=
\frac{1}{4\pi}
\left(
K_{IJ}\,\partial_t\phi_I\,\partial_x\phi_J
-V_{IJ}\,\partial_x\phi_I\,\partial_x\phi_J
\right),
$$

with the chirality matrix and Luttinger metric

$$
K=\operatorname{diag}(1,1,-1,-1),
\qquad
V=\operatorname{diag}(v_1,v_2,v_3,v_4).
$$

The eigenvalues of $$K$$ make $$\phi_1,\phi_2$$ left-movers and
$$\phi_3,\phi_4$$ right-movers in the gapless region, with per-flavor
velocities $$v_I$$.

### SMG interface

The SMG interaction is built from two integer **Haldane null vectors**

$$
\ell_1=(1,-2,1,2)^\intercal,
\qquad
\ell_2=(-3,1,1,-3)^\intercal,
$$

which satisfy $$\ell_a^\intercal K^{-1}\ell_b=0$$ and which preserve the full
$$U(1)\times U(1)\times \mathbb{Z}_{10}\times\mathbb{Z}_{10}$$ symmetry of
the 3-4-5-0 model. The interacting Lagrangian is

$$
\mathcal{L}_{\mathrm{int}}
=
g_1(x)\cos(\ell_1^\intercal\phi)
+
g_2(x)\cos(\ell_2^\intercal\phi).
$$

To model a region in which the SMG interaction is turned on smoothly, we work
at the $$\mathbb{Z}_2$$-symmetric point $$g_1(x)=g_2(x)=g(x)$$ with a sigmoid
profile

$$
g(x)=\frac{g_0}{1+\exp[-(x-c)/w]},
$$

so that $$g(x)\to 0$$ on one side of $$x=c$$ and $$g(x)\to g_0$$ on the other,
with $$w$$ setting the crossover width.

### Wave equation

Varying $$\mathcal{L}_0+\mathcal{L}_{\mathrm{int}}$$ with respect to
$$\phi_I$$ gives the nonlinear wave equation

$$
K_{IJ}\,\partial_t\partial_x\phi_J
-V_{IJ}\,\partial_x^2\phi_J
+2\pi g(x)\,\ell_{1I}\sin(\ell_1^\intercal\phi)
+2\pi g(x)\,\ell_{2I}\sin(\ell_2^\intercal\phi)
=0.
$$

In the gapless region ($$g\to 0$$) this reduces to the free first-order
chiral wave equation $$K\,\partial_t\phi - V\,\partial_x\phi = 0$$. In the
deep SMG region ($$g\to g_0$$) the cosines pin the two null-vector
combinations $$\ell_1^\intercal\phi$$ and $$\ell_2^\intercal\phi$$, opening a
fully symmetric gap. The interface mediates the scattering between these two
phases.

## Numerics

The simulator integrates the wave equation above in real time on a
one-dimensional interval. The interval is split into a gapless region and an
SMG region by the sigmoid profile $$g(x)$$, and a Gaussian wave packet is
launched in one of the four channels $$\phi_I$$. The four field profiles
$$\phi_I(x,t)$$ are displayed in stacked panels, reduced modulo $$2\pi$$ into
the window $$[-\pi,\pi)$$; the PDE itself is integrated on the universal
cover. The shaded background under each panel tracks $$g(x)$$, so the
location and width of the interface are visible at a glance.

<div class="simulator-frame-wrap">
  <iframe
    class="simulator-frame"
    id="model-simulator-frame"
    title="3-4-5-0 Model Simulator"
    src="./simulator.html"
    loading="lazy"
  ></iframe>
</div>

<script>
  (() => {
    const frame = document.getElementById("model-simulator-frame");
    if (!frame) return;

    const resizeFrame = () => {
      try {
        const doc = frame.contentDocument;
        if (!doc) return;
        const height = Math.max(
          doc.body?.scrollHeight || 0,
          doc.documentElement?.scrollHeight || 0,
          640,
        );
        frame.style.height = `${height}px`;
      } catch (_error) {
        // Keep the CSS fallback height when same-origin iframe sizing is unavailable.
      }
    };

    frame.addEventListener("load", () => {
      resizeFrame();
      const doc = frame.contentDocument;
      if (doc?.body && "ResizeObserver" in window) {
        new ResizeObserver(resizeFrame).observe(doc.body);
      }
    });
  })();
</script>

### How to use it

- *Launch channel*: which of $$\phi_1,\dots,\phi_4$$ carries the initial
  packet. $$\phi_{1,2}$$ are left-movers and $$\phi_{3,4}$$ are right-movers.
- *Amplitude / Center / Width*: shape of the Gaussian initial profile.
- *SMG Region*: which part of the line hosts the SMG interaction. *Left* and
  *Right* create a single interface. *Both* creates two interfaces at
  $$x=\pm c$$, sets the packet center to $$0$$, and uses
  $$g(x)=g_{\mathrm{left}}(x)+g_{\mathrm{right}}(x)$$.
- *SMG interface*: strength $$g_0$$, crossover width $$w$$, and center $$c$$
  of the sigmoid interface.
- *Discretization*: spatial grid extent and resolution, time step $$dt$$,
  total number of steps, sampling stride, and outer boundary condition. The
  default *Absorbing* boundary mimics outgoing radiation; *Dirichlet*,
  *Neumann*, and *Periodic* are useful as sanity checks.
- *Solver*: *Automatic* chooses the best browser-side solver for the current
  boundary condition, so most users should leave it there. The manual choices
  are simplified labels for the leading research branches:
  *Stable default*, *Stiff interface*, *Plateau pinning*, *Conservative
  transport*, and *Legacy baseline*.
- *Velocity matrix*: per-flavor velocities $$v_I$$ on the diagonal of $$V$$.

A useful starting experiment is to set $$g_0=0$$ to recover free chiral
propagation as a baseline, then gradually turn the SMG interaction on and
watch how each channel begins to mix near the interface.

### Caveats

This is an exploratory visualizer rather than a controlled scattering
calculation:

- The solver menu is synced to the current research frontrunners, but these
  are still lightweight browser implementations for interactivity, not exact
  reproductions of the Python benchmark harness.
- The nonlinear region can become numerically stiff for large $$g_0$$ or
  small $$w$$; if the trace develops obvious artifacts, reduce $$dt$$ or
  widen the interface.
- The compact identification $$\phi\sim\phi+2\pi$$ is applied only for
  display; the PDE itself is integrated on the universal cover, so apparent
  jumps at $$\pm\pi$$ are display wraps rather than dynamics.
- Extracting reflected, transmitted, and twisted-sector amplitudes from the
  outgoing wave — the comparison most relevant to the Wang–Wen and Tong
  *et al.* analyses — is not done in this demo.

## References

- J. Wang and X.-G. Wen, *A Solution to the 1+1D Gauged Chiral Fermion
  Problem*, [arXiv:1807.05998](https://arxiv.org/abs/1807.05998).
- T. Onogi, T. Wada, and S. Yamaoka, *Discrete Symmetry and 't Hooft Anomalies
  for 3450 Model*, [arXiv:2501.18156](https://arxiv.org/abs/2501.18156).
- M. van Beest, P. Boyle Smith, D. Delmastro, Z. Komargodski, and D. Tong,
  *Monopoles, Scattering, and Generalized Symmetries*,
  [arXiv:2306.07318](https://arxiv.org/abs/2306.07318).
