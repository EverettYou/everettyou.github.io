# Chap 17: Waves—II

## Sections

| Sec | Topic |
|-----|------|
| 17-1 | [Speed of Sound](17-1-speed-of-sound.ipynb) |
| 17-2 | [Traveling Sound Waves](17-2-traveling-sound-waves.ipynb) |
| 17-3 | [Interference](17-3-interference.ipynb) |
| 17-4 | [Intensity and Sound Level](17-4-intensity-and-sound-level.ipynb) |
| 17-5 | [Sources of Musical Sound](17-5-sources-of-musical-sound.ipynb) |
| 17-6 | [Beats](17-6-beats.ipynb) |
| 17-7 | [The Doppler Effect](17-7-the-doppler-effect.ipynb) |
| 17-8 | [Supersonic Speeds, Shock Waves](17-8-supersonic-speeds-shock-waves.ipynb) |

## Review & Summary

:::{glossary}
Sound Waves
  Sound waves are longitudinal mechanical waves that can travel through solids, liquids, or gases. The speed $v$ of a sound wave in a medium having **bulk modulus** $B$ and density $\rho$ is

  $$
  v = \sqrt{\frac{B}{\rho}}
  $$ (eq-17-speed)

  In air at 20°C, the speed of sound is 343 m/s. A sound wave causes a longitudinal displacement $s$ of a mass element in the medium as given by

  $$
  s = s_m \cos(kx - \omega t)
  $$ (eq-17-displacement)

  where $s_m$ is the **displacement amplitude** (maximum displacement from equilibrium), $k = 2\pi/\lambda$, and $\omega = 2\pi f$, with $\lambda$ and $f$ the wavelength and frequency of the sound wave. The wave also causes a pressure change $\Delta p$ from the equilibrium pressure:

  $$
  \Delta p = \Delta p_m \sin(kx - \omega t)
  $$ (eq-17-pressure)

  where the **pressure amplitude** is $\Delta p_m = \rho v \omega s_m$.

Interference
  The interference of two sound waves with identical wavelengths passing through a common point depends on their phase difference $\phi$ there. If the sound waves were emitted in phase and are traveling in approximately the same direction, $\phi$ is given by $\phi = (2\pi/\lambda)\Delta L$, where $\Delta L$ is their **path length difference** (the difference in the distances traveled by the waves to reach the common point). Fully constructive interference occurs when $\phi$ is an integer multiple of $2\pi$, i.e., $\Delta L = n\lambda$. Fully destructive interference occurs when $\phi$ is an odd multiple of $\pi$, i.e., $\Delta L = (n + \frac{1}{2})\lambda$.

Sound Intensity
  The **intensity** $I$ of a sound wave at a surface is the average rate per unit area at which energy is transferred by the wave through or onto the surface:

  $$
  I = \frac{P}{A}
  $$ (eq-17-intensity)

  where $P$ is the time rate of energy transfer (power) of the sound wave and $A$ is the area of the surface intercepting the sound. The intensity $I$ is related to the displacement amplitude $s_m$ by $I = \frac{1}{2}\rho v \omega^2 s_m^2$. The intensity at a distance $r$ from a point source that emits sound waves of power $P_s$ is

  $$
  I = \frac{P_s}{4\pi r^2}
  $$ (eq-17-point-source)

  The **sound level** in decibels is $\beta = 10 \log_{10}(I/I_0)$, where $I_0 = 10^{-12}$ W/m² is a reference intensity. For every factor-of-10 increase in intensity, 10 dB is added to the sound level.

Standing Wave Patterns in Pipes
  Standing sound wave patterns can be set up in pipes. A pipe open at both ends will resonate at frequencies

  $$
  f = \frac{nv}{2L}, \quad n = 1, 2, 3, \ldots
  $$ (eq-17-pipe-open)

  where $v$ is the speed of sound in the air in the pipe. For a pipe closed at one end and open at the other, the resonant frequencies are $f = nv/4L$ for $n = 1, 3, 5, \ldots$

Beats
  **Beats** arise when two waves having slightly different frequencies $f_1$ and $f_2$ are detected together. The beat frequency is

  $$
  f_{\mathrm{beat}} = |f_1 - f_2|
  $$ (eq-17-beats)

The Doppler Effect
  The **Doppler effect** is a change in the observed frequency of a wave when the source or the detector moves relative to the transmitting medium (such as air). For sound, the observed frequency $f'$ is given in terms of the source frequency $f$ by

  $$
  f' = f \frac{v \pm v_D}{v \mp v_S}
  $$ (eq-17-doppler)

  where $v_D$ is the speed of the detector relative to the medium, $v_S$ is that of the source, and $v$ is the speed of sound in the medium. The signs are chosen such that $f'$ tends to be *greater* for motion toward and *less* for motion away.

Shock Wave
  If the speed of a source relative to the medium exceeds the speed of sound in the medium, the Doppler equation no longer applies. In such a case, **shock waves** result. The half-angle $\theta$ of the Mach cone is given by

  $$
  \sin\theta = \frac{v}{v_S}
  $$ (eq-17-mach)

  where $v_S$ is the speed of the source.
:::
