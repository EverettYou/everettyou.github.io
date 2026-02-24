# Chap 19: The Kinetic Theory of Gases

## Sections

| Sec | Topic |
|-----|------|
| 19-1 | [Avogadro's Number](19-1-avogadros-number.ipynb) |
| 19-2 | [Ideal Gases](19-2-ideal-gases.ipynb) |
| 19-3 | [Pressure, Temperature, and RMS Speed](19-3-pressure-temperature-and-rms-speed.ipynb) |
| 19-4 | [Translational Kinetic Energy](19-4-translational-kinetic-energy.ipynb) |
| 19-5 | [Mean Free Path](19-5-mean-free-path.ipynb) |
| 19-6 | [The Distribution of Molecular Speeds](19-6-the-distribution-of-molecular-speeds.ipynb) |
| 19-7 | [The Molar Specific Heats of an Ideal Gas](19-7-the-molar-specific-heats-of-an-ideal-gas.ipynb) |
| 19-8 | [Degrees of Freedom and Molar Specific Heats](19-8-degrees-of-freedom-and-molar-specific-heats.ipynb) |
| 19-9 | [The Adiabatic Expansion of an Ideal Gas](19-9-the-adiabatic-expansion-of-an-ideal-gas.ipynb) |

## Review & Summary

:::{glossary}
Kinetic Theory of Gases
  The *kinetic theory of gases* relates the *macroscopic* properties of gases (pressure, temperature) to the *microscopic* properties of gas molecules (speed, kinetic energy).

Avogadro's Number
  One mole of a substance contains $N_A$ (*Avogadro's number*) elementary units (usually atoms or molecules), where $N_A = 6.02 \times 10^{23}$ mol$^{-1}$. One molar mass $M$ of any substance is the mass of one mole. It is related to the mass $m$ of individual molecules by $M = N_A m$. The number of moles $n$ in a sample of mass $M_{\mathrm{sam}}$ consisting of $N$ molecules is

  $$
  n = \frac{N}{N_A} = \frac{M_{\mathrm{sam}}}{M}
  $$ (eq-19-moles)

Ideal Gas
  An *ideal gas* is one for which pressure $p$, volume $V$, and temperature $T$ are related by

  $$
  pV = nRT
  $$ (eq-19-ideal)

  where $n$ is the number of moles and $R = 8.31$ J/(mol·K) is the **gas constant.** Equivalently, $pV = NkT$, where $k = R/N_A = 1.38 \times 10^{-23}$ J/K is the **Boltzmann constant** and $N$ is the number of molecules.

Pressure, Temperature, and RMS Speed
  The pressure exerted by $n$ moles of an ideal gas, in terms of molecular speeds, is $p = (nM/V) v_{\mathrm{rms}}^2/3$, where $v_{\mathrm{rms}} = \sqrt{\overline{v^2}}$ is the **root-mean-square speed** and $M$ is the molar mass. This gives

  $$
  v_{\mathrm{rms}} = \sqrt{\frac{3RT}{M}}
  $$ (eq-19-vrms)

  The average translational kinetic energy $\overline{K}$ per molecule is

  $$
  \overline{K} = \frac{3}{2} kT
  $$ (eq-19-Kavg)

Mean Free Path
  The **mean free path** $\lambda$ of a gas molecule is its average path length between collisions:

  $$
  \lambda = \frac{1}{\sqrt{2}\,\pi d^2 (N/V)}
  $$ (eq-19-mfp)

  where $N/V$ is the number of molecules per unit volume and $d$ is the molecular diameter.

Maxwell Speed Distribution
  The *Maxwell speed distribution* $P(v)$ is such that $P(v)\,dv$ gives the fraction of molecules with speeds in the interval $dv$ at speed $v$. Three measures are $v_{\mathrm{avg}}$, $v_P$ (most probable), and $v_{\mathrm{rms}}$.

Molar Specific Heats
  For an ideal gas, the molar specific heat at constant volume is $C_V = \frac{f}{2}R$ and at constant pressure $C_P = C_V + R = \frac{f+2}{2}R$, where $f$ is the number of degrees of freedom. For monatomic: $f=3$; diatomic: $f=5$. 
  
  The internal energy for $n$ moles of an ideal gas at temperature $T$ is 
  
  $$
  E_{\mathrm{int}} = n C_V T
  $$ (eq-19-energy)

Adiabatic Expansion
  For a reversible **adiabatic** process ($Q=0$), $pV^\gamma = \mathrm{constant}$ and $TV^{\gamma-1} = \mathrm{constant}$, where $\gamma = C_P/C_V$ is the adiabatic exponent. The work done by the gas is $W = -\Delta E_{\mathrm{int}}$.
:::
