# Chap 16: Waves—I

## Sections

| Sec | Topic |
|-----|------|
| 16-1 | [Transverse Waves](16-1-transverse-waves.ipynb) |
| 16-2 | [Wave Speed on a Stretched String](16-2-wave-speed-on-a-stretched-string.ipynb) |
| 16-3 | [Energy and Power of a Wave Traveling Along a String](16-3-energy-and-power-of-a-wave-traveling-along-a-string.ipynb) |
| 16-4 | [The Wave Equation](16-4-the-wave-equation.ipynb) |
| 16-5 | [Interference of Waves](16-5-interference-of-waves.ipynb) |
| 16-6 | [Phasors](16-6-phasors.ipynb) |
| 16-7 | [Standing Waves and Resonance](16-7-standing-waves-and-resonance.ipynb) |

## Review & Summary

:::{glossary}
Transverse and Longitudinal Waves
  Mechanical waves can exist only in material media and are governed by Newton's laws. **Transverse** mechanical waves, like those on a stretched string, are waves in which the particles of the medium oscillate perpendicular to the wave's direction of travel. Waves in which the particles oscillate parallel to the wave's direction of travel are **longitudinal** waves.

Sinusoidal Waves
  A sinusoidal wave moving in the positive direction of an $x$ axis has the mathematical form

  $$
  y(x,t) = y_m \sin(kx - \omega t)
  $$ (eq-16-sinusoidal)

  where $y_m$ is the **amplitude** of the wave, $k$ is the **angular wave number**, $\omega$ is the **angular frequency**, and $kx - \omega t$ is the **phase.** The **wavelength** $\lambda$ is related to $k$ by

  $$
  k = \frac{2\pi}{\lambda}
  $$ (eq-16-k)

  The **period** $T$ and **frequency** $f$ of the wave are related to $\omega$ by $\omega = 2\pi/T = 2\pi f$. The **wave speed** $v$ is

  $$
  v = \frac{\omega}{k} = \lambda f
  $$ (eq-16-speed)

Equation of a Traveling Wave
  Any function of the form $y(x,t) = h(kx \pm \omega t)$ can represent a **traveling wave** with wave speed given by Eq. [](#eq-16-speed). The plus sign denotes a wave traveling in the negative direction of the $x$ axis, and the minus sign a wave traveling in the positive direction.

Wave Speed on Stretched String
  The speed of a wave on a stretched string is set by properties of the string. The speed on a string with tension $\tau$ and linear density $\mu$ (mass per unit length) is

  $$
  v = \sqrt{\frac{\tau}{\mu}}
  $$ (eq-16-string)

Power
  The **average power** of, or average rate at which energy is transmitted by, a sinusoidal wave on a stretched string is given by

  $$
  P_{\mathrm{avg}} = \frac{1}{2} \mu v \omega^2 y_m^2
  $$ (eq-16-power)

Superposition of Waves
  When two or more waves traverse the same medium, the displacement of any particle of the medium is the sum of the displacements that the individual waves would give it.

Interference of Waves
  Two sinusoidal waves on the same string exhibit **interference**, adding or canceling according to the principle of superposition. If the two are traveling in the same direction and have the same amplitude $y_m$ and frequency (hence the same wavelength) but differ in phase by a **phase constant** $\phi$, the result is a single wave with this same frequency. If $\phi = 0$, the waves are exactly in phase and their interference is fully constructive; if $\phi = \pi$ rad, they are exactly out of phase and their interference is fully destructive.

Phasors
  A wave $y(x,t)$ can be represented with a **phasor.** This is a vector that has a magnitude equal to the amplitude $y_m$ of the wave and that rotates about an origin with an angular speed equal to the angular frequency $\omega$ of the wave. The projection of the rotating phasor on a vertical axis gives the displacement $y$ of a point along the wave's travel.

Standing Waves
  The interference of two identical sinusoidal waves moving in opposite directions produces **standing waves.** For a string with fixed ends, standing waves are characterized by fixed locations of zero displacement called **nodes** and fixed locations of maximum displacement called **antinodes.** If an end is fixed, it must be the position of a node. For a stretched string of length $L$ with fixed ends, the **resonant frequencies** are

  $$
  f = \frac{nv}{2L}, \quad n = 1, 2, 3, \ldots
  $$ (eq-16-resonance)

  where $v$ is the wave speed. The mode corresponding to $n=1$ is the *fundamental mode* or *first harmonic*; $n=2$ is the *second harmonic*; and so on.
:::
