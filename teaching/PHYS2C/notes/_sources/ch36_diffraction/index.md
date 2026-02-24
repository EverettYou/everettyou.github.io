# Chap 36: Diffraction

## Sections

| Sec | Topic |
|-----|------|
| 36-1 | [Single-Slit Diffraction](36-1-single-slit-diffraction.ipynb) |
| 36-2 | [Intensity in Single-Slit Diffraction](36-2-intensity-in-single-slit-diffraction.ipynb) |
| 36-3 | [Diffraction by a Circular Aperture](36-3-diffraction-by-a-circular-aperture.ipynb) |
| 36-4 | [Diffraction by a Double Slit](36-4-diffraction-by-a-double-slit.ipynb) |
| 36-5 | [Diffraction Gratings](36-5-diffraction-gratings.ipynb) |
| 36-6 | [Gratings: Dispersion and Resolving Power](36-6-gratings-dispersion-and-resolving-power.ipynb) |
| 36-7 | [X-Ray Diffraction](36-7-x-ray-diffraction.ipynb) |

## Review & Summary

:::{glossary}
Diffraction
  When waves encounter an edge, an obstacle, or an aperture the size of which is comparable to the wavelength, those waves spread out as they travel and undergo interference. This is **diffraction.**

Single-Slit Diffraction
  Waves passing through a long narrow slit of width $a$ produce a **single-slit diffraction pattern** on a viewing screen, with a central maximum and other maxima separated by minima at angles $\theta$ satisfying

  $$
  a\sin\theta = m\lambda, \quad m = \pm 1, \pm 2, \ldots
  $$ (eq-36-single-min)

  The intensity at angle $\theta$ is $I = I_m (\sin\alpha/\alpha)^2$, where $\alpha = (\pi a/\lambda)\sin\theta$ and $I_m$ is the intensity at the center.

Circular-Aperture Diffraction
  Diffraction by a circular aperture or lens of diameter $d$ produces a central maximum and concentric maxima and minima. The first minimum is at an angle $\theta$ given by

  $$
  \sin\theta = 1.22\,\frac{\lambda}{d}
  $$ (eq-36-circular)

Rayleigh's Criterion
  **Rayleigh's criterion** suggests that two point sources are on the verge of resolvability if the central diffraction maximum of one is at the first minimum of the other. The minimum angular separation is $\theta_R = 1.22\lambda/d$.

Double-Slit Diffraction
  Two slits, each of width $a$ with centers a distance $d$ apart, display a pattern that combines single-slit diffraction and double-slit interference. The intensity is $I = I_m (\sin\alpha/\alpha)^2 \cos^2\beta$, where $\alpha = (\pi a/\lambda)\sin\theta$ and $\beta = (\pi d/\lambda)\sin\theta$.

Diffraction Gratings
  A **diffraction grating** is a series of "slits" used to separate an incident wave into its component wavelengths. Maxima (spectral lines) occur at angles $\theta$ such that

  $$
  d\sin\theta = m\lambda, \quad m = 0, 1, 2, \ldots
  $$ (eq-36-grating)

  where $d$ is the slit separation. The grating provides **dispersion** (separation of wavelengths) and **resolving power** $R = \lambda/\Delta\lambda = Nm$ for $N$ slits.

X-Ray Diffraction
  X-rays scatter from the regularly spaced planes of a crystal. **Bragg's law** for constructive interference is

  $$
  2d\sin\theta = m\lambda
  $$ (eq-36-bragg)

  where $d$ is the spacing between crystal planes and $\theta$ is the angle between the incident ray and the plane.
:::
