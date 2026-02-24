# Chap 34: Images

## Sections

| Sec | Topic |
|-----|------|
| 34-1 | [Images and Plane Mirrors](34-1-images-and-plane-mirrors.ipynb) |
| 34-2 | [Spherical Mirrors](34-2-spherical-mirrors.ipynb) |
| 34-3 | [Spherical Refracting Surfaces](34-3-spherical-refracting-surfaces.ipynb) |
| 34-4 | [Thin Lenses](34-4-thin-lenses.ipynb) |
| 34-5 | [Optical Instruments](34-5-optical-instruments.ipynb) |
| 34-6 | [Three Proofs](34-6-three-proofs.ipynb) |

## Review & Summary

:::{glossary}
Real and Virtual Images
  An **image** is a reproduction of an object via light. If the image can form on a surface, it is a **real image** and can exist even if no observer is present. If the image requires the visual system of an observer, it is a **virtual image.**

Image Formation
  *Spherical mirrors*, *spherical refracting surfaces*, and *thin lenses* form images by redirecting rays from the object. The image occurs where redirected rays cross (real) or where backward extensions cross (virtual). For rays close to the *central axis*, with *object distance* $p$ (positive) and *image distance* $i$ (positive for real, negative for virtual):

  **1. Spherical mirror:**

  $$
  \frac{1}{p} + \frac{1}{i} = \frac{2}{r} = \frac{1}{f}
  $$ (eq-34-mirror)

  where $f$ is the focal length and $r$ is the radius of curvature. A *plane mirror* has $r \to \infty$, so $p = -i$. Real images form on the object side; virtual on the opposite side.

  **2. Spherical refracting surface:**

  $$
  \frac{n_1}{p} + \frac{n_2}{i} = \frac{n_2 - n_1}{r}
  $$ (eq-34-refract)

  where $n_1$ and $n_2$ are the indices of refraction. Convex surface facing object: $r > 0$; concave: $r < 0$.

  **3. Thin lens:**

  $$
  \frac{1}{p} + \frac{1}{i} = \frac{1}{f} = (n-1)\left(\frac{1}{r_1} - \frac{1}{r_2}\right)
  $$ (eq-34-lens)

  where $n$ is the lens index and $r_1$, $r_2$ are the radii of the two surfaces. Real images form on the side opposite the object; virtual on the same side.

Lateral Magnification
  The **lateral magnification** $m$ produced by a spherical mirror or thin lens is

  $$
  m = -\frac{i}{p} = \frac{h'}{h}
  $$ (eq-34-magnification)

  where $h$ and $h'$ are the heights of the object and image (perpendicular to the central axis). The image is upright if $m > 0$, inverted if $m < 0$.

Optical Instruments
  **Simple magnifier:** angular magnification $m_\theta = 25\,\mathrm{cm}/f$, where $f$ is the focal length and 25 cm is the near-point distance. **Compound microscope:** overall magnification $M = m \cdot m_\theta$ with objective and eyepiece. **Refracting telescope:** angular magnification $m_\theta = -f_{\mathrm{ob}}/f_{\mathrm{ey}}$.
:::
