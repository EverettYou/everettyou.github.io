# Chap 37: Relativity

## Sections

| Sec | Topic |
|-----|------|
| 37-1 | [Simultaneity and Time Dilation](37-1-simultaneity-and-time-dilation.ipynb) |
| 37-2 | [The Relativity of Length](37-2-the-relativity-of-length.ipynb) |
| 37-3 | [The Lorentz Transformation](37-3-the-lorentz-transformation.ipynb) |
| 37-4 | [The Relativity of Velocities](37-4-the-relativity-of-velocities.ipynb) |
| 37-5 | [Doppler Effect for Light](37-5-doppler-effect-for-light.ipynb) |
| 37-6 | [Momentum and Energy](37-6-momentum-and-energy.ipynb) |

## Review & Summary

:::{glossary}
Simultaneity and Time Dilation
  Events that are simultaneous in one inertial frame need not be simultaneous in another. **Time dilation:** If a clock at rest in a frame measures a time interval $\Delta t_0$ (the *proper time*), then an observer in a frame moving at speed $v$ relative to that clock measures a longer interval:

  $$
  \Delta t = \gamma \Delta t_0
  $$ (eq-37-time-dilation)

  where $\gamma = 1/\sqrt{1 - v^2/c^2}$ is the Lorentz factor.

The Relativity of Length
  **Length contraction:** If an object has length $L_0$ in its rest frame (the *proper length*), then an observer moving parallel to that length measures

  $$
  L = \frac{L_0}{\gamma}
  $$ (eq-37-length)

The Lorentz Transformation
  For motion along the $x$ axis with relative speed $v$, the coordinates $(x,t)$ and $(x',t')$ in two inertial frames are related by $x' = \gamma(x - vt)$, $t' = \gamma(t - vx/c^2)$, with inverse $x = \gamma(x' + vt')$, $t = \gamma(t' + vx'/c^2)$.

The Relativity of Velocities
  If a particle has velocity $u$ in one frame and the frame moves at $v$ relative to another, the velocity $u'$ in the second frame is $u' = (u - v)/(1 - uv/c^2)$ for motion along the same line. Velocities do not add simply; $c$ is the invariant speed limit.

Doppler Effect for Light
  The observed frequency $f'$ differs from the source frequency $f$ when source and detector move relative to each other. For a source approaching the detector: $f' = f\sqrt{(1 + \beta)/(1 - \beta)}$ with $\beta = v/c$. For receding, $\beta \to -\beta$. **Transverse Doppler** (source moving perpendicular to line of sight): $f' = f/\gamma$.

Momentum and Energy
  **Relativistic momentum:** $\vec{p} = \gamma m \vec{v}$. **Total energy:** $E = \gamma mc^2$. **Rest energy:** $E_0 = mc^2$. **Kinetic energy:** $K = E - E_0 = (\gamma - 1)mc^2$. The energy and momentum satisfy the invariant relation

  $$
  E^2 = (pc)^2 + (mc^2)^2
  $$ (eq-37-energy-momentum)
:::
