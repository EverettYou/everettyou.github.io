# Chap 14: Fluids

## Sections

| Sec | Topic |
|-----|------|
| 14-1 | [Fluids, Density, and Pressure](14-1-fluids-density-and-pressure.ipynb) |
| 14-2 | [Fluids at Rest](14-2-fluids-at-rest.ipynb) |
| 14-3 | [Measuring Pressure](14-3-measuring-pressure.ipynb) |
| 14-4 | [Pascal's Principle](14-4-pascals-principle.ipynb) |
| 14-5 | [Archimedes' Principle](14-5-archimedes-principle.ipynb) |
| 14-6 | [The Equation of Continuity](14-6-the-equation-of-continuity.ipynb) |
| 14-7 | [Bernoulli's Equation](14-7-bernoullis-equation.ipynb) |

## Review & Summary

:::{glossary}
Density
  The **density** $\rho$ of any material is defined as the material's mass per unit volume:

  $$
  \rho = \frac{\Delta m}{\Delta V}
  $$ (eq-14-1)

  Usually, where a material sample is much larger than atomic dimensions, we can write Eq. [](#eq-14-1) as

  $$
  \rho = \frac{m}{V}
  $$ (eq-14-2)

Fluid Pressure
  A **fluid** is a substance that can flow; it conforms to the boundaries of its container because it cannot withstand shearing stress. It can, however, exert a force perpendicular to its surface. That force is described in terms of **pressure** $p$:

  $$
  p = \frac{\Delta F}{\Delta A}
  $$ (eq-14-3)

  in which $\Delta F$ is the force acting on a surface element of area $\Delta A$. If the force is uniform over a flat area, Eq. [](#eq-14-3) can be written as

  $$
  p = \frac{F}{A}
  $$ (eq-14-4)

  The force resulting from fluid pressure at a particular point in a fluid has the same magnitude in all directions. Since Pa = N/m² = J/m³, pressure has units of **energy per volume**—work per unit volume, or the potential energy a fluid has to expand. **Gauge pressure** is the difference between the actual pressure (or *absolute pressure*) at a point and the atmospheric pressure.

Pressure Variation with Height and Depth
  Pressure in a fluid at rest varies with vertical position $y$. For $y$ measured positive upward, the pressure difference between two levels is

  $$
  p_2 - p_1 = \rho g (y_1 - y_2)
  $$ (eq-14-7)

  where $\rho$ is the fluid density and $g$ is the gravitational acceleration. The term $\rho g h$ equals the gravitational potential energy per unit volume at depth $h$. The pressure in a fluid is the same for all points at the same level (same gravitational PE density). If $h$ is the *depth* of a fluid sample below some reference level at which the pressure is $p_0$, then the pressure in the sample is

  $$
  p = p_0 + \rho g h
  $$ (eq-14-8)

Pascal's Principle
  A change in the pressure applied to an enclosed fluid is transmitted undiminished to every portion of the fluid and to the walls of the containing vessel. Since pressure is energy per unit volume, transmitting pressure means transmitting energy density everywhere.

Archimedes' Principle
  When a body is fully or partially submerged in a fluid, a buoyant force $\vec{F}_b$ from the surrounding fluid acts on the body. This force arises from pressure (energy density) differences in the fluid. The force is directed upward and has a magnitude given by

  $$
  F_b = m_f g
  $$ (eq-archimedes)

  where $m_f$ is the mass of the fluid that has been displaced by the body (that is, the fluid that has been pushed out of the way by the body).

  When a body floats in a fluid, the magnitude $F_b$ of the (upward) buoyant force on the body is equal to the magnitude $F_g$ of the (downward) gravitational force on the body. The **apparent weight** of a body on which a buoyant force acts is related to its actual weight by

  $$
  F_{g,\mathrm{app}} = F_g - F_b
  $$ (eq-apparent-weight)

Flow of Ideal Fluids
  An **ideal fluid** is incompressible and lacks viscosity, and its flow is steady and irrotational. A *streamline* is the path followed by an individual fluid particle. A *tube of flow* is a bundle of streamlines. The flow within any tube of flow obeys the **equation of continuity** (which fixes how speed $v$ varies with area); Bernoulli's equation adds energy conservation to determine how pressure varies:

  $$
  R_V = A v = \mathrm{constant}
  $$ (eq-14-continuity)

  in which $R_V$ is the **volume flow rate**, $A$ is the cross-sectional area of the tube of flow at any point, and $v$ is the speed of the fluid at that point. The **mass flow rate** $R_m$ is

  $$
  R_m = \rho R_V = \rho A v = \mathrm{constant}
  $$ (eq-mass-flow)

Bernoulli's Equation
  Conservation of **total energy density** along a streamline: pressure energy $p$ (work per volume), kinetic $\frac{1}{2}\rho v^2$, and gravitational $\rho g y$ trade off—e.g., higher speed implies lower pressure:

  $$
  p + \frac{1}{2} \rho v^2 + \rho g y = \mathrm{constant}
  $$ (eq-14-bernoulli)
:::
