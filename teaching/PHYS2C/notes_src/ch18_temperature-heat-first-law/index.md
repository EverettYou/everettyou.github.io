# Chap 18: Temperature, Heat, and the First Law of Thermodynamics

## Sections

| Sec | Topic |
|-----|------|
| 18-1 | [Temperature](18-1-temperature.ipynb) |
| 18-2 | [The Celsius and Fahrenheit Scales](18-2-the-celsius-and-fahrenheit-scales.ipynb) |
| 18-3 | [Thermal Expansion](18-3-thermal-expansion.ipynb) |
| 18-4 | [Absorption of Heat](18-4-absorption-of-heat.ipynb) |
| 18-5 | [The First Law of Thermodynamics](18-5-the-first-law-of-thermodynamics.ipynb) |
| 18-6 | [Heat Transfer Mechanisms](18-6-heat-transfer-mechanisms.ipynb) |

## Review & Summary

:::{glossary}
Temperature; Thermometers
  Temperature is an SI base quantity related to our sense of hot and cold. It is measured with a thermometer, which contains a working substance with a measurable property (such as length or pressure) that changes in a regular way as the substance becomes hotter or colder.

Zeroth Law of Thermodynamics
  When a thermometer and some other object are placed in contact, they eventually reach thermal equilibrium. The **zeroth law of thermodynamics:** If bodies $A$ and $B$ are each in thermal equilibrium with a third body $C$ (the thermometer), then $A$ and $B$ are in thermal equilibrium with each other.

The Kelvin Temperature Scale
  In the SI system, temperature is measured on the **Kelvin scale**, based on the *triple point* of water (273.16 K). With a constant-volume gas thermometer, the temperature $T$ (in kelvins) is defined by

  $$
  T = (273.16\,\mathrm{K}) \frac{p}{p_3}
  $$ (eq-18-kelvin)

  where $p_3$ and $p$ are the pressures of the gas at the triple point and at the measured temperature. The Celsius scale is $T_C = T - 273.15$; the Fahrenheit scale is $T_F = \frac{9}{5}T_C + 32°$.

Thermal Expansion
  For a temperature change $\Delta T$, a change $\Delta L$ in any linear dimension $L$ is given by

  $$
  \Delta L = L \alpha \Delta T
  $$ (eq-18-linear)

  in which $\alpha$ is the **coefficient of linear expansion.** The change $\Delta V$ in the volume $V$ of a solid or liquid is $\Delta V = V \beta \Delta T$, where $\beta \approx 3\alpha$ is the **coefficient of volume expansion.**

Heat Capacity and Specific Heat
  If heat $Q$ is absorbed by an object of mass $m$, the temperature change $\Delta T = T_f - T_i$ is related to $Q$ by

  $$
  Q = C \Delta T = cm \Delta T
  $$ (eq-18-heat-capacity)

  where $C$ is the **heat capacity** and $c$ is the **specific heat** of the material. The **molar specific heat** is the heat capacity per mole.

Heat of Transformation
  Heat absorbed by a material may change its physical state. The **heat of transformation** $L$ is the energy per unit mass required to change the state (but not the temperature). Thus $Q = Lm$. The **heat of vaporization** $L_V$ and **heat of fusion** $L_F$ apply to vaporization/condensation and melting/freezing, respectively.

Work Associated with Volume Change
  The work $W$ done *by* a gas as it expands or contracts from volume $V_i$ to $V_f$ is

  $$
  W = \int_{V_i}^{V_f} p\,dV
  $$ (eq-18-work)

  The integration is necessary because the pressure $p$ may vary during the volume change.

First Law of Thermodynamics
  The principle of conservation of energy for a thermodynamic process is expressed in the **first law of thermodynamics:**

  $$
  \Delta E_{\mathrm{int}} = Q - W
  $$ (eq-18-first-law)

  Here $E_{\mathrm{int}}$ is the internal energy (a state function); $Q$ is the energy transferred as heat ($Q > 0$ if absorbed); $W$ is the work done *by* the system ($W > 0$ if the system expands). $Q$ and $W$ are path dependent; $\Delta E_{\mathrm{int}}$ is path independent.

Heat Transfer Mechanisms
  **Conduction:** $P = kA \Delta T / L$, where $k$ is thermal conductivity, $A$ is area, $L$ is thickness. **Convection:** heat transfer by mass motion of fluid. **Radiation:** $P = \sigma \varepsilon A T^4$ (Stefan–Boltzmann law), where $\sigma$ is the Stefan–Boltzmann constant and $\varepsilon$ is emissivity.
:::
