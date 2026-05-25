---
layout: page
title: 3-4-5-0 Luttinger Liquid Wave Simulator
subtitle: Browser-side demo for compact-boson scattering near an SMG interface
hide: true
---

<link rel="stylesheet" href="./app.css">

This project page hosts a small numerical playground for the bosonized
3-4-5-0 model. The simulator runs entirely in the visitor's browser; GitHub
Pages only serves static files.

<div class="simulator-embed">
<div class="page-shell">

      <main class="monitor-layout">
        <section class="monitor-stage" aria-label="Four channel wave monitor">
          <div class="stage-head">
            <div>
              <p class="eyebrow">Four compact bosons</p>
              <h2>Field profile on [-π, π)</h2>
            </div>
            <div class="time-pill">
              <span class="math-lite">t</span>
              <strong id="time-label">0.00</strong>
            </div>
          </div>

          <div class="plot-shell">
            <svg class="multi-panel-plot" id="multi-panel-plot" viewBox="0 0 900 620" preserveAspectRatio="none" role="img" aria-label="Four compact boson field profiles"></svg>
            <div class="plot-labels" aria-hidden="true">
              <span class="plot-text panel-symbol" style="left: 4%; top: 12.9%;">φ₁</span>
              <span class="plot-text panel-symbol" style="left: 4%; top: 32.6%;">φ₂</span>
              <span class="plot-text panel-symbol" style="left: 4%; top: 52.3%;">φ₃</span>
              <span class="plot-text panel-symbol" style="left: 4%; top: 71.9%;">φ₄</span>

              <span class="plot-text y-tick" style="top: 4.8%;">π</span>
              <span class="plot-text y-tick" style="top: 12.9%;">0</span>
              <span class="plot-text y-tick" style="top: 21.0%;">−π</span>
              <span class="plot-text y-tick" style="top: 24.5%;">π</span>
              <span class="plot-text y-tick" style="top: 32.6%;">0</span>
              <span class="plot-text y-tick" style="top: 40.6%;">−π</span>
              <span class="plot-text y-tick" style="top: 44.2%;">π</span>
              <span class="plot-text y-tick" style="top: 52.3%;">0</span>
              <span class="plot-text y-tick" style="top: 60.3%;">−π</span>
              <span class="plot-text y-tick" style="top: 63.9%;">π</span>
              <span class="plot-text y-tick" style="top: 71.9%;">0</span>
              <span class="plot-text y-tick" style="top: 80.0%;">−π</span>

              <span class="plot-text x-tick" id="x-min-label" style="left: 10.7%; top: 85.5%;"></span>
              <span class="plot-text x-tick" id="x-mid-label" style="left: 53.8%; top: 85.5%;"></span>
              <span class="plot-text x-tick" id="x-max-label" style="left: 96.9%; top: 85.5%;"></span>
              <span class="plot-text x-label math-lite" style="left: 53.8%; top: 89.4%;">x</span>
            </div>
          </div>

          <div class="transport-bar">
            <button class="transport-button icon-button" id="play-toggle" type="button" aria-label="Play simulation">
              <i class="fa-solid fa-play" aria-hidden="true"></i>
            </button>
            <input id="time-slider" type="range" min="0" max="0" step="1" value="0" />
            <select class="speed-select" id="speed-select" aria-label="Playback speed">
              <option value="0.5">x0.5</option>
              <option value="1" selected>x1</option>
              <option value="1.5">x1.5</option>
              <option value="2">x2</option>
            </select>
            <button class="ghost-button icon-button" id="restart-button" type="button" aria-label="Restart simulation">
              <i class="fa-solid fa-rotate-left" aria-hidden="true"></i>
            </button>
          </div>
        </section>

        <aside class="control-dock" aria-label="Simulation controls">
          <form id="control-form">
            <p id="status-text" class="status dock-status">Ready.</p>

            <details class="fold-panel" open>
              <summary>Initial condition</summary>
              <div class="panel-body">
                <label>
                  <span>Launch channel</span>
                  <select name="packet_channel">
                    <option value="0" selected>phi_1</option>
                    <option value="1">phi_2</option>
                    <option value="2">phi_3</option>
                    <option value="3">phi_4</option>
                  </select>
                </label>
                <label>
                  <span>Amplitude</span>
                  <input name="packet_amplitude" type="number" step="0.1" value="1.0" />
                </label>
                <label>
                  <span>Center</span>
                  <input name="packet_center" type="number" step="0.5" value="10.0" />
                </label>
                <label>
                  <span>Width</span>
                  <input name="packet_width" type="number" step="0.1" value="3.0" />
                </label>
              </div>
            </details>

            <details class="fold-panel" open>
              <summary>SMG interface</summary>
              <div class="panel-body">
                <label>
                  <span>SMG strength g0</span>
                  <input name="g0" type="number" step="0.1" value="1.0" />
                </label>
                <label>
                  <span>Crossover width w</span>
                  <input name="interface_width" type="number" step="0.1" value="0.4" />
                </label>
                <label>
                  <span>Interface center c</span>
                  <input name="interface_center" type="number" step="0.5" value="-10.0" />
                </label>
                <fieldset class="segmented-control">
                  <legend>Interaction side</legend>
                  <label>
                    <input name="interaction_side" type="radio" value="left" checked />
                    <span>Left</span>
                  </label>
                  <label>
                    <input name="interaction_side" type="radio" value="right" />
                    <span>Right</span>
                  </label>
                </fieldset>
              </div>
            </details>

            <details class="fold-panel">
              <summary>Discretization</summary>
              <div class="panel-body">
                <label>
                  <span>x min</span>
                  <input name="x_min" type="number" step="1" value="-24.0" />
                </label>
                <label>
                  <span>x max</span>
                  <input name="x_max" type="number" step="1" value="24.0" />
                </label>
                <label>
                  <span>Grid points</span>
                  <input name="num_points" type="number" step="1" value="256" />
                </label>
                <label>
                  <span>dt</span>
                  <input name="dt" type="number" step="0.005" value="0.05" />
                </label>
                <label>
                  <span>Steps</span>
                  <input name="num_steps" type="number" step="10" value="1200" />
                </label>
                <label>
                  <span>Sample every</span>
                  <input name="sample_every" type="number" step="1" value="20" />
                </label>
                <label>
                  <span>Boundary</span>
                  <select name="boundary">
                    <option value="neumann" selected>Neumann</option>
                    <option value="periodic">Periodic</option>
                  </select>
                </label>
              </div>
            </details>

            <details class="fold-panel">
              <summary>Velocity matrix</summary>
              <div class="panel-body compact-grid">
                <label>
                  <span>v1</span>
                  <input name="v1" type="number" step="0.1" value="1.0" />
                </label>
                <label>
                  <span>v2</span>
                  <input name="v2" type="number" step="0.1" value="1.0" />
                </label>
                <label>
                  <span>v3</span>
                  <input name="v3" type="number" step="0.1" value="1.0" />
                </label>
                <label>
                  <span>v4</span>
                  <input name="v4" type="number" step="0.1" value="1.0" />
                </label>
              </div>
            </details>
          </form>
        </aside>
      </main>
    </div>
</div>

<script src="./app.js" defer></script>

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

Thus $$\phi_1,\phi_2$$ are left-moving fields and
$$\phi_3,\phi_4$$ are right-moving fields in the free region.

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

The default simulation uses the $$\mathbb{Z}_2$$-symmetric case

$$
g_1(x)=g_2(x)=g(x),
$$

where $$g(x)$$ is a sigmoid profile. Choosing the interaction on the right
uses

$$
g(x)=\frac{g_0}{1+\exp[-(x-c)/w]},
$$

while choosing the interaction on the left reflects the profile about the
interface center $$c$$.

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

The compact fields are displayed modulo $$2\pi$$ in the interval
$$[-\pi,\pi)$$. The shaded monitor background encodes the local strength
of $$g(x)$$, from white in the gapless region to a darker tone in the SMG
region.

## Notes

This demo is meant as an exploratory visualization, not yet a controlled
scattering calculation. In particular, the nonlinear SMG region can be stiff,
and the numerical result should be checked against the free-wave solution by
setting $$g_0=0$$.
