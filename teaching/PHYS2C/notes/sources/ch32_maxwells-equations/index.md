# Chap 32: Maxwell's Equations; Magnetism of Matter

## Sections

| Sec | Topic |
|-----|------|
| 32-1 | [Gauss' Law for Magnetic Fields](32-1-gauss-law-for-magnetic-fields.ipynb) |
| 32-2 | [Induced Magnetic Fields](32-2-induced-magnetic-fields.ipynb) |
| 32-3 | [Displacement Current](32-3-displacement-current.ipynb) |
| 32-4 | [Magnets](32-4-magnets.ipynb) |
| 32-5 | [Magnetism and Electrons](32-5-magnetism-and-electrons.ipynb) |
| 32-6 | [Diamagnetism](32-6-diamagnetism.ipynb) |
| 32-7 | [Paramagnetism](32-7-paramagnetism.ipynb) |
| 32-8 | [Ferromagnetism](32-8-ferromagnetism.ipynb) |

## Review & Summary

:::{glossary}
Gauss' Law for Magnetic Fields
  The simplest magnetic structures are magnetic dipoles. Magnetic monopoles do not exist (as far as we know). **Gauss' law** for magnetic fields states that the net magnetic flux through any closed Gaussian surface is zero:

  $$
  \oint \vec{B} \cdot d\vec{A} = 0
  $$ (eq-32-gauss-b)

  It implies that magnetic monopoles do not exist.

Induced Magnetic Fields
  A changing electric flux $\Phi_E$ through a loop induces a magnetic field along the loop. This is Maxwell's addition to Ampère's law.

Displacement Current
  The **displacement current** due to a changing electric field is defined as $i_d = \varepsilon_0 \, d\Phi_E/dt$. The **Ampère–Maxwell law** combines conduction current and displacement current:

  $$
  \oint \vec{B} \cdot d\vec{s} = \mu_0 i_{d,\mathrm{enc}} + \mu_0 i_{\mathrm{enc}}
  $$ (eq-32-ampere-maxwell)

  where $i_{d,\mathrm{enc}}$ is the displacement current encircled by the integration loop. Displacement current is *not* a transfer of charge but allows continuity of "current" through a capacitor.

Maxwell's Equations
  Maxwell's equations summarize electromagnetism and form its foundation, including optics. They unify electric and magnetic phenomena and predict electromagnetic waves.

Spin Magnetic Dipole Moment
  An electron has an intrinsic **spin angular momentum** $\vec{S}$ and an associated **spin magnetic dipole moment** $\vec{\mu}_s = -(e/m_e)\vec{S}$. For a measurement along a $z$ axis, $S_z$ can have only the values $\pm \hbar/2$.

Orbital Magnetic Dipole Moment
  An electron in an atom has **orbital angular momentum** $\vec{L}_{\mathrm{orb}}$ and an associated **orbital magnetic dipole moment** $\vec{\mu}_{\mathrm{orb}} = -(e/2m_e)\vec{L}_{\mathrm{orb}}$. Orbital angular momentum is quantized: $L_z = m_\ell \hbar$ with $m_\ell = 0, \pm 1, \ldots, \pm \ell$. The energy of the dipole in an external field $\vec{B}_{\mathrm{ext}}$ is $U = -\vec{\mu}_{\mathrm{orb}} \cdot \vec{B}_{\mathrm{ext}}$.

Diamagnetism
  **Diamagnetic materials** exhibit magnetism only when placed in an external field; they form magnetic dipoles directed *opposite* the external field. In a nonuniform field, they are repelled from the region of greater magnetic field.

Paramagnetism
  **Paramagnetic materials** have atoms with permanent magnetic dipole moments that are randomly oriented unless in an external field $\vec{B}_{\mathrm{ext}}$, where the dipoles tend to align. The **magnetization** $\vec{M}$ (dipole moment per unit volume) is $M = C B_{\mathrm{ext}}/T$ at low $B_{\mathrm{ext}}/T$, where $T$ is temperature and $C$ is the **Curie constant.** In a nonuniform field, paramagnetic materials are attracted to the region of greater field.

Ferromagnetism
  In **ferromagnetic materials**, magnetic dipole moments can be aligned by an external field and remain partially aligned in **domains** after the field is removed. Alignment is eliminated above the **Curie temperature** $T_C$. **Hysteresis** in the $B$–$H$ curve allows permanent magnets.
:::
