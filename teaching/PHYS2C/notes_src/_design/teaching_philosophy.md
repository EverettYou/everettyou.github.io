# AI-Era Undergraduate Physics Curriculum Design: A Research Report on Teaching Reform Based on First Principles and SciML

## Introduction

In an era of rapid artificial intelligence (AI) development, undergraduate physics education faces an unprecedented survival crisis and transformation opportunity. When large language models (LLMs) such as GPT-4o and Claude 3.5 can solve traditional textbook problems with far greater speed and precision than humans, the conventional teaching model centered on formula derivation and closed-form problem solving has lost its original educational value. For non-physics majors, the purpose of learning physics is no longer to master tedious computational techniques, but to build a rigorous scientific worldview, acquire cross-disciplinary methodology, and develop hands-on ability to solve complex problems in an AI-collaborative environment. This shift demands that curriculum design move from "how to compute" to "how to model," from "rote memorization of formulas" to "understanding physical intuition," and deeply integrate Scientific Machine Learning (SciML) tools to combine the first principles of physics with the computational power of AI.

---

## Part I: Reframing the Worldview

### 1.1 From Isolated Concepts to Unified First Principles

In the AI era, the core value of human learning in physics lies in building a complete and coherent worldview. Although AI models excel at pattern recognition and statistical inference, they often lack deep understanding of causality, physical constraints, and underlying laws. Therefore, physics courses should abandon the traditional approach of treating fluids, waves, thermodynamics, and optics as isolated modules, and instead emphasize their deep logical connections and unified theory.

### 1.2 Energy Principle and Substance Ontology

A major misconception in physics teaching is over-reliance on the "work-energy theorem" or "kinetic energy theorem," which are essentially path integrals of Newton's second law and concern momentum change more than the nature of energy. For non-majors, adopting the **Energy Principle** as the main axis of the course has greater educational value. The Energy Principle emphasizes that energy is a conserved and continuous quantity, understandable through a "Substance Ontology"—energy behaves like an indestructible substance stored and transferred across different mechanisms. Richard Feynman illustrated this with the "blocks story": energy is like blocks in a child's hands; whether hidden under the bed or buried in the ground, the total amount remains constant; only the form (mechanism) of storage changes. In this framework, kinetic, potential, and internal energy are no longer abstract formulas but concrete manifestations of energy stored in motion, gravitational fields, or microscopic molecular arrangements. This ontological perspective helps students form intuitive physical images and connects seamlessly with energy metabolism in chemistry and biology and thermodynamic processes.

A further theoretical reframing suggests viewing **kinematics** as a manifestation of energy conversion rather than an independent description of spacetime. Motion, velocity, and acceleration should not be seen as intrinsic reality but as perceptual byproducts of underlying energy dynamics. In this "process ontology," energy is primary; all mechanical, electronic, quantum, and even biological systems can be reduced to energy-based conversion processes. For life science students, this perspective extends to the **Free Energy Principle**, which treats homeostasis as the core of the physics of life and holds that system dynamics essentially minimize "surprisal" or variational free energy.

---

## Part II: Variational Modeling—The Common Language of Physics and AI

**Variational principles** are the most unifying mathematical framework in physics, revealing that nature behaves according to some optimal path. From Fermat's principle (light follows the path of least time) to the principle of least action, to Dirichlet's principle (static systems tend toward minimum potential energy), these principles form a coherent logical chain. In the AI era, variational modeling is especially significant because it directly corresponds to the underlying logic of machine learning—finding optimal model parameters by minimizing an objective (loss) function. By formulating physical problems as functional optimization problems, students can understand that nature is not merely a machine driven by differential equations but an intelligent system constantly seeking optimal solutions. This perspective greatly enhances physical intuition, enabling students to first think about a system's "goals" and "constraints" when facing complex new systems, rather than blindly searching for ready-made formulas.

The following table shows the unification of different physical domains under the variational framework:

| Physical Domain | Core Unified Principle | Optimization Objective (Functional) | AI/Computational Equivalent |
|-----------------|------------------------|-------------------------------------|-----------------------------|
| Classical Mechanics | Principle of Least Action | Stationary points of $\int L(t, y, \dot{y}) dt$ | Trajectory optimization / PINNs |
| Wave Optics | Fermat's Principle | Minimum of $\int n(s) ds$ (time) | Optical inverse design |
| Complex Fluids | Energy Dissipation Law (EnVarA) | Balance of kinetic and free energy change with dissipation rate | Physics-informed neural networks |
| Thermodynamics | Entropy increase / Free energy minimization | Minimize variational free energy (Surprisal) | Variational inference |
| Electromagnetism | Maxwell Action | Stationary points of spatial/temporal integral of field energy density | Automatic differentiation / Inverse design |

---

## Part III: Evolution of Scientific Methodology—Modeling, Abstraction, and AI Collaboration

Traditional physics teaching often focuses on solving well-defined problems. In the AI era, physics education should shift toward cultivating students' ability to "define problems" and "construct models." This involves four core elements of the scientific method: observation, hypothesis, experimental verification, and theory construction.

### 3.1 Methodology of Modeling and Abstraction

Model construction is the process of transforming complex real-world scenarios into formalized, solvable mathematical representations. Students must learn to simplify systems through **analogy** and **abstraction**. For example, in fluid mechanics, abstracting the chaotic motion of microscopic molecules into a continuum model; in circuit analysis, abstracting physical components into idealized resistors and inductors. In an AI-assisted modeling workflow, the human role is to identify key variables, define objective functions, and impose physical constraints. Teachers should guide students to practice describing novel problems to AI, e.g.: *"Given a manufacturing system with three production lines and two inspection points, what are the core entities and processes for a discrete-event simulation?"* This training elevates students from "problem-solving machines" to "architecture designers."

### 3.2 Prompt Engineering: AI as a Cognitive Partner

In the AI era, **prompt engineering** is not merely a technique but a tool for logical expression and scientific communication. Students must learn to make AI a helpful tutor rather than a cheating tool through precise instructions. Research shows that structured prompt frameworks significantly improve AI assistance in physics problems:

- **COSTAR framework**: By defining Context, Objective, Style, Tone, Audience, and Response format, students obtain highly tailored explanations of physical concepts.
- **RACE framework**: For designing physical experiments or course plans, clear delineation of Role, Action, Context, and Expectation effectively reduces AI hallucinations and improves output logic.
- **CREATE framework**: Emphasizing Character, Request, Examples, Additions, output Type, and Extras, suitable for generating complex physical visualization code or innovative thought experiments.

Through reverse exercises such as "Spot the Bot," students can learn to identify AI limitations. For example, when asked why a ball continues moving after leaving the hand, AI may confuse inertia with motive force. By pointing out AI errors and correcting them with physical laws, students internalize physics principles more deeply.

---

## Part IV: Redefining Hands-On Ability—Differentiable Programming and Physics-Informed Neural Networks (PINNs)

In non-major undergraduate physics courses, hands-on ability should shift from tedious manual calculations to computer programming and numerical simulation, especially learning to use SciML tools to study physical systems.

### 4.1 Automatic Differentiation: The "Calculus" of the New Era

**Automatic Differentiation (AD)** is the cornerstone of modern computational physics and AI. It allows precise computation of derivatives of arbitrarily complex algorithms at machine precision—without manual derivation of chain rules. Introducing AD tools (e.g., JAX or PyTorch) in the course lets students directly face the optimization objectives of physical systems. For example, in optical design, students can use AD to optimize photon crystal waveguide dispersion in real time; this "inverse design" methodology is far more representative of modern technology than traditional ray tracing.

| Property | Automatic Differentiation (AD) | Traditional Finite Difference (FD) |
|----------|----------------------------------|------------------------------------|
| Precision | Machine precision, no truncation error | Affected by step size; balance of truncation and rounding error |
| Efficiency | Gradient cost comparable to function evaluation | Cost explodes in high-dimensional parameter space |
| Flexibility | Supports control flow (if, while) in derivative computation | Difficult to handle code with complex branching |
| Stability | Accelerates gradient descent dynamics, more robust convergence | Prone to local numerical instability |

### 4.2 PINNs: Turning Physical Laws into Optimization Problems

**Physics-Informed Neural Networks (PINNs)** provide a universal approach to converting all physical problems into optimization problems. The core idea is to embed governing physical equations (e.g., heat equation, wave equation, Navier–Stokes equations) directly into the neural network loss function. A typical undergraduate PINN experiment should include three loss terms:

1. **PDE residual ($L_{PDE}$)**: Use AD to compute derivatives of network output with respect to inputs (e.g., time $t$, space $x$) and check whether the physical equation is satisfied. For free fall, smaller residual of $h''(t) + g = 0$ means the model better matches gravity.
2. **Initial/ boundary conditions ($L_{BC/IC}$)**: Force the network to satisfy physical boundaries at specific points, e.g., initial position $h(0)=H$.
3. **Data matching ($L_{data}$)**: If experimental data exist, the model must match those points.

This method teaches students that all physical systems can be addressed through a unified workflow: identify variables, define objectives, impose constraints—greatly enhancing transferability of physics knowledge.

---

## Part V: Classroom Structure—Socratic Flipped Classroom 2.0

In an AI environment, the classroom is no longer a venue for information delivery but a workshop for high-order thinking and collaborative innovation.

### 5.1 Pre-Class: AI-Scaffolded Exploration

Use AI-assisted systems (e.g., SMART) for pre-class work. Students submit summaries of videos or materials; AI provides immediate feedback on conceptual gaps. Teachers can configure AI tutors (e.g., NotebookLM) to guide students through dialogue to derive concepts. For example, AI might ask: *"Why does the ball continue moving after leaving the hand?"* and gradually introduce physical constraints as students answer, rather than giving the answer directly.

### 5.2 In-Class: Verification, Reflection, and Forensic Analysis

- **Code forensics**: Teachers distribute AI-generated physics simulation code containing a subtle physical error (e.g., violating energy conservation). Students run the code, observe the physics, locate the error, and fix it. This "error-correction learning" effectively cultivates critical thinking.
- **Physics visualization competition**: Using Manim or similar tools, students prompt AI to generate dynamic visualizations of complex phenomena (e.g., turbulence, optical interference). Evaluation goes beyond aesthetics to whether the physics is correct (e.g., whether waves satisfy Huygens' principle).
- **Real-world challenges**: Form cross-disciplinary teams to solve practical problems with physical modeling, e.g.: *"How to optimize a drone delivery route to minimize battery consumption?"* Students identify variables (drone weight, drag, path curvature), objective (energy integral), and constraints (altitude limits, battery capacity), and solve using AD.

### 5.3 Assessment: Process Over Outcome

In the AI era, final answers have lost their assessment value. Assessment should shift toward **metacognition** (thinking about thinking): require submission of AI interaction logs and analysis of how questioning logic evolved. Adopt ungrading or alternative grading that emphasizes oral explanation of physical intuition and deep reflection on model limitations. Add in-class "variant quizzes" without AI assistance to ensure students retain core physical intuition when tools are removed.

---

## Part VI: Case Applications—Teaching Reframing for Fluids, Waves, Thermodynamics, and Optics

For specific subject modules, physics teaching should highlight their deep intersection with modern AI technology.

### 6.1 Fluid Mechanics: From First-Principles Derivation to Data-Driven Discovery

Fluid mechanics is the intersection of "big data" and complex dynamics. Teaching should shift from rote memorization of Bernoulli's equation to deriving the Navier–Stokes (N–S) equations using energy functionals. Students can participate in a "fluid digital twin" experiment:

- **Task**: Use AI to recover the full flow field from sparse wing-surface pressure sensor data.
- **Method**: Build a PINN embedding the N–S equations as constraints, leveraging AI's nonlinear fitting to compensate for sparse data.
- **Intuition**: Understand why AI performs well for simple laminar flow but needs more physics-informed bias (e.g., ModLaNet) for turbulence with multi-scale chaotic features.

### 6.2 Wave Optics: From Ray Tracing to Inverse Design

Wave optics teaching should emphasize the mathematical mapping of "wave physics as a recurrent neural network (RNN)." Wave propagation is essentially sequential processing; each layer of medium through which light passes can be seen as a layer of a neural network. In this module, students practice "optical mask inverse design":

- **Scenario**: Design a lens that focuses light into a specific shape (e.g., school logo).
- **Tools**: Tidy3D or similar electromagnetic simulation plugins with AD support.
- **Methodology**: Define MSE loss between target and actual focused image; backpropagate gradients to update refractive index distribution. This "optimization thinking" shows that wave laws are not just for computing refraction angles but for controlling information flow.

### 6.3 Thermodynamics: Statistical Physics and AI Insights into Phase Transitions

The modern value of thermodynamics lies in its description of collective behavior of complex systems composed of vast numbers of individuals. AI has shown capabilities beyond traditional methods in materials discovery and phase transition classification. Students can explore through:

- **Phase transition classifier**: Train a classifier on generated statistics to distinguish paramagnetic vs. ferromagnetic states.
- **Physics-informed analysis**: Compare the traditional Ising model with modern Poisson flow generative models (PFGM++) to understand how electrostatics can simulate thermal diffusion.
- **Risk awareness**: Learn why thermodynamic data are often non-Gaussian, and how fatal bias arises when AI models wrongly assume Gaussian noise in predicting extreme climate or new material stability.

---

## Part VII: Conclusions and Action Recommendations—Building a Mental "Insurance Policy" for the AI Era

Redesigning the undergraduate physics curriculum is a "mental insurance project" for an AI-dominated future. When machines remove the technical barriers of entry-level jobs, students must leap to higher cognitive levels to maintain competitive advantage in the AI wave. Serious physics study builds solid character and deep intuition, offering meaning in life that does not depend on economic necessity.

To achieve this, institutions and teachers should act promptly:

1. **Update teaching materials**: Introduce variational modeling and energy-first principles as the main thread; gradually phase out exercises over-focused on hand calculation.
2. **Set up computational environments**: Embrace cloud-based interactive computing (e.g., Google Colab); teach AD-capable frameworks such as JAX and PyTorch.
3. **Integrate prompt engineering**: Incorporate structured prompt frameworks (COSTAR, RACE, CREATE) into syllabi as essential skills for scientific communication and model specification.
4. **Implement Flipped 2.0**: Reserve limited class time for complex experimental argumentation and Socratic debate; use AI tutors for personalized pre-class knowledge building.
5. **Cross-disciplinary collaboration**: Deeply connect physics first principles with optimization problems in engineering, biology, and data science; cultivate students' ability to solve whole classes of problems with a unified approach.

Ultimately, the goal of physics education is not to teach students to compete with AI, but to stand on the high ground of natural laws and lead and harness AI. By building deep physical intuition, students gain a unique "human advantage"—the ability to see through the essence of truth in a chaotic ocean of data.
