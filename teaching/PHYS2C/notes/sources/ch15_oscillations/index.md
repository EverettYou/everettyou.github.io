# Chap 15: Oscillations

## Sections

| Sec | Topic |
|-----|------|
| 15-1 | [Simple Harmonic Motion](15-1-simple-harmonic-motion.ipynb) |
| 15-2 | [Energy in Simple Harmonic Motion](15-2-energy-in-simple-harmonic-motion.ipynb) |
| 15-3 | [An Angular Simple Harmonic Oscillator](15-3-an-angular-simple-harmonic-oscillator.ipynb) |
| 15-4 | [Pendulums, Circular Motion](15-4-pendulums-circular-motion.ipynb) |
| 15-5 | [Damped Simple Harmonic Motion](15-5-damped-simple-harmonic-motion.ipynb) |
| 15-6 | [Forced Oscillations and Resonance](15-6-forced-oscillations-and-resonance.ipynb) |

## Review & Summary

:::{glossary}
Frequency
  The *frequency* $f$ of periodic, or oscillatory, motion is the number of oscillations per second. In the SI system, it is measured in hertz (Hz). The frequency is the reciprocal of the period $T$:

  $$
  f = \frac{1}{T}
  $$ (eq-15-freq)

Period
  The *period* $T$ is the time required for one complete oscillation, or **cycle.** It is related to the frequency by

  $$
  T = \frac{1}{f}
  $$ (eq-15-period)

Simple Harmonic Motion
  In *simple harmonic motion* (SHM), the displacement $x(t)$ of a particle from its equilibrium position is described by the equation

  $$
  x(t) = x_m \cos(\omega t + \phi)
  $$ (eq-15-shm)

  in which $x_m$ is the **amplitude** of the displacement (maximum distance from equilibrium), $\omega t + \phi$ is the **phase** of the motion, and $\phi$ is the **phase constant** (determines position at $t=0$). The **angular frequency** $\omega$ (in rad/s) is related to the period and frequency by

  $$
  \omega = \frac{2\pi}{T} = 2\pi f
  $$ (eq-15-omega)

  Differentiating Eq. [](#eq-15-shm) with respect to time gives the velocity and acceleration:

  $$
  v(t) = -\omega x_m \sin(\omega t + \phi), \quad a(t) = -\omega^2 x_m \cos(\omega t + \phi)
  $$ (eq-15-va)

  The **velocity amplitude** is $v_m = \omega x_m$ and the **acceleration amplitude** is $a_m = \omega^2 x_m$.

The Linear Oscillator
  A particle with mass $m$ that moves under the influence of a Hooke's law restoring force $F = -kx$ (where $k$ is the spring constant) exhibits simple harmonic motion. The angular frequency is set by the system:

  $$
  \omega = \sqrt{\frac{k}{m}}
  $$ (eq-15-omega-osc)

  Such a system is called a **linear simple harmonic oscillator.**

Energy
  A particle in simple harmonic motion has, at any time, kinetic energy $K = \frac{1}{2}mv^2$ and potential energy $U = \frac{1}{2}kx^2$. If no friction is present, the mechanical energy $E = K + U$ remains constant even though $K$ and $U$ change individually.

Pendulums
  Examples of devices that undergo simple harmonic motion (for small oscillations) are the **torsion pendulum**, the **simple pendulum**, and the **physical pendulum.** Their periods are, respectively,

  $$
  T = 2\pi\sqrt{\frac{I}{\kappa}}, \quad T = 2\pi\sqrt{\frac{L}{g}}, \quad T = 2\pi\sqrt{\frac{I}{mgh}}
  $$ (eq-15-pendulums)

  where for the torsion pendulum: $I$ is the rotational inertia and $\kappa$ is the torsion constant; for the simple pendulum: $L$ is the length and $g$ is the gravitational acceleration; for the physical pendulum: $I$ is the rotational inertia about the pivot, $m$ is the mass, and $h$ is the distance from pivot to center of mass.

Simple Harmonic Motion and Uniform Circular Motion
  Simple harmonic motion is the projection of uniform circular motion onto the diameter of the circle in which the circular motion occurs. All parameters of circular motion (position, velocity, and acceleration) project to the corresponding values for simple harmonic motion.

Damped Harmonic Motion
  The mechanical energy $E$ in a real oscillating system decreases during the oscillations because external forces, such as a drag force, inhibit the oscillations and transfer mechanical energy to thermal energy. The oscillator and its motion are then said to be **damped.** If the **damping force** is $F_d = -bv$, where $\vec{v}$ is the velocity of the oscillator and $b$ is the **damping constant**, then the displacement is

  $$
  x(t) = x_m e^{-bt/2m} \cos(\omega' t + \phi)
  $$ (eq-15-damped)

  where $\omega'$, the angular frequency of the damped oscillator, is

  $$
  \omega' = \sqrt{\omega^2 - (b/2m)^2}
  $$ (eq-15-omega-prime)

  with $\omega$ the angular frequency of the undamped oscillator.

Forced Oscillations and Resonance
  When an external driving force acts on an oscillator, the motion is **forced.** When the driving frequency matches the natural frequency $\omega$ of the oscillator, a condition called **resonance** occurs. The amplitude $x_m$ of the system is (approximately) greatest under the same condition.
:::
