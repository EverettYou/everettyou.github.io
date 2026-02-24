# Chap 33: Electromagnetic Waves

## Sections

| Sec | Topic |
|-----|------|
| 33-1 | [Electromagnetic Waves](33-1-electromagnetic-waves.ipynb) |
| 33-2 | [Energy Transport and the Poynting Vector](33-2-energy-transport-and-the-poynting-vector.ipynb) |
| 33-3 | [Radiation Pressure](33-3-radiation-pressure.ipynb) |
| 33-4 | [Polarization](33-4-polarization.ipynb) |
| 33-5 | [Reflection and Refraction](33-5-reflection-and-refraction.ipynb) |
| 33-6 | [Total Internal Reflection](33-6-total-internal-reflection.ipynb) |
| 33-7 | [Polarization by Reflection](33-7-polarization-by-reflection.ipynb) |

## Review & Summary

:::{glossary}
Electromagnetic Waves
  An electromagnetic wave consists of oscillating electric and magnetic fields. The various possible frequencies form a *spectrum*, a small part of which is visible light. A wave traveling along the $x$ axis has $E = E_m \sin(kx - \omega t)$ and $B = B_m \sin(kx - \omega t)$, where $E_m$ and $B_m$ are the amplitudes. The oscillating fields induce each other. The speed in vacuum is $c = 1/\sqrt{\mu_0\varepsilon_0}$, and the simultaneous magnitudes satisfy $E = cB$.

Energy Flow
  The rate per unit area at which energy is transported is given by the **Poynting vector** $\vec{S} = \vec{E} \times \vec{B}/\mu_0$. The direction of $\vec{S}$ is perpendicular to both $\vec{E}$ and $\vec{B}$. The **intensity** $I$ is the time-averaged magnitude:

  $$
  I = S_{\mathrm{avg}} = \frac{E_{\mathrm{rms}}^2}{c\mu_0}
  $$ (eq-33-intensity)

  where $E_{\mathrm{rms}} = E_m/\sqrt{2}$. A *point source* emits waves *isotropically*. The intensity at distance $r$ from a source of power $P_s$ is

  $$
  I = \frac{P_s}{4\pi r^2}
  $$ (eq-33-point-source)

Radiation Pressure
  When a surface intercepts electromagnetic radiation, a force is exerted. If the radiation is totally absorbed, $F = IA/c$, where $I$ is the intensity and $A$ is the area perpendicular to the path. If totally reflected back along its original path, $F = 2IA/c$. The **radiation pressure** is $p_r = F/A$: thus $p_r = I/c$ (absorbed) or $2I/c$ (reflected).

Polarization
  Electromagnetic waves are **polarized** if their electric field vectors all lie in a single plane (the *plane of oscillation*). Light from common sources is **unpolarized** (randomly polarized). A polarizing sheet transmits only components parallel to its **polarizing direction.** For initially unpolarized light, $I = \frac{1}{2}I_0$. For initially polarized light at angle $\theta$ to the polarizing direction, **Malus's law:** $I = I_0 \cos^2\theta$.

Reflection and Refraction
  When a light ray encounters a boundary between two transparent media, a reflected ray and a refracted ray appear. The angle of reflection equals the angle of incidence. **Snell's law:** $n_1 \sin\theta_1 = n_2 \sin\theta_2$, where $n_1$ and $n_2$ are the indices of refraction.

Total Internal Reflection
  When $n_1 > n_2$ and the angle of incidence exceeds the **critical angle** $\theta_c = \arcsin(n_2/n_1)$, all light is reflected back into medium 1.

Polarization by Reflection
  At **Brewster's angle** $\theta_B = \arctan(n_2/n_1)$, the reflected light is fully polarized perpendicular to the plane of incidence.
:::
