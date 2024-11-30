I am broadly interested in the numerical analysis and scientific computing, especially in molecular modeling in materials science, including:

## Machine-learned Interatomic Potentials (MLIPs)

My research focuses on the numerical analysis and development of Machine-learned Interatomic Potentials (MLIPs), integrating interdisciplinary concepts from physics, materials science, applied mathematics, and data science. I aim to establish a systematic framework for modeling interatomic interactions, with a particular emphasis on understanding and minimizing approximation errors and propagating them through MLIP models to improve predictive accuracy and reliability.

**Highlights:**
- *Mathematical Foundations of MLIPs*: 
  - Analysis of generalization error and uncertainty quantification to assess model robustness;
  - Active learning strategies to optimize data efficiency and improve model performance;
  - Solving inverse problems for data-driven discovery of interatomic interactions.
- *Modeling and simulations of MLIPs*: 
  - Study of crystalline defects, including dislocations, grain boundaries, and random alloys;
  - Exploration of 2D materials and their unique interatomic behaviors;
  - Modeling vibrational entropy for thermodynamic property predictions;
  - Development of coarse-grained molecular dynamics approaches for large-scale systems;
  - Accelerated molecular dynamics simulations for efficient exploration of atomic-scale phenomena.



**Corresponding Papers:**  
>
> [1] Huajie Chen, Christoph Ortner and **Yangshuai Wang**, *QM/MM Methods for Crystalline Defects. Part 3: Machine-learned MM Models*, **Multiscale Model. Simul.**, 20:1490-1518, 2022.   
[2] Christoph Ortner and **Yangshuai Wang**, *A Framework for a Generalisation Analysis of Machine-learned Interatomic Potentials*, **Multiscale Model. Simul.**, 21:1053-1080, 2023.  
[3] **Yangshuai Wang**, Shashwat Patel and Christoph Ortner, *A Theoretical Case Study of the Generalisation of Machine-learned Potentials*, **Comput. Methods Appl. Mech. Engrg.**, 422:116831, 2024.  
[4] Tina Torabi, Christoph Ortner and **Yangshuai Wang**, *Surrogate models for vibrational entropy based on a spatial decomposition*, accepted by **Multiscale Model. Simul.**, 2024.   
[5] Ilyes Batatia, Philipp Benner, Yuan Chiang, Alin M. Elena, Dávid P. Kovács, and Janosh Riebesell et al. (62 authors not shown), *A Foundation Model for Atomistic Materials Chemistry*, 2024, arXiv preprint.   
[6] **Yangshuai Wang** and Cheuk Hin Ho, *Performance Assessment of Fine-tuned Pre-trained Mod-
els in Atomistic Materials Science*, **In preparation**.  
[7] **Yangshuai Wang**, Gabor Csanyi, and Christoph Ortner, *Exporing Many-Body Effects in Coarse-Grained Molecular Dynamics with the Atomic Cluster Expansion*, **In preparation**.  
[8] **Yangshuai Wang**, Drake Clark, Sambit Das, Ziyan Zhu, Daniel Massatt, Vikram Gavini, Mitchell Luskin, and Christoph Ortner, *An Atomic Cluster Expansion Potential for Twisted Multilayer Graphene*, **In preparation**.   
[9] Cheuk Hin Ho, **Yangshuai Wang**, and Christoph Ortner, *Robust Uncertainty Quantification in Machine-Learned Interatomic Potentials Using Classification-Based Conformal Prediction*, **In preparation**.




## Mathematical Modeling and Algorithms for Material Simulations

My research is dedicated to developing advanced mathematical models and computational algorithms for simulating material behaviors, particularly in the context of defects, multi-lattice structures, and phase transitions. The goal is to bridge theoretical insights with efficient numerical techniques, enabling accurate and scalable solutions for complex material systems.

**Highlights:**

- *Boundary Conditions for Defect Simulations*:
  - Development of mathematically rigorous and physically consistent boundary conditions to model defects in crystalline materials.

- **Regularity Estimates for Defect Equilibrium**:
  - Analytical study of the regularity properties of defect solutions, ensuring stability and well-posedness in equilibrium configurations.

- *Efficient Algorithms for Geometry Optimization and Transition State Calculations*:
  - Development of fast and reliable algorithms for geometry optimization, minimum energy path identification, and transition state finding in material systems.

- **Phase-Field Crystal (PFC) Models, Cauchy-Born Rule, and Numerical Algorithms**:
  - Design and implementation of PFC models to study mesoscale material behaviors, coupled with efficient numerical algorithms for dynamic simulations.
  - Extensions and applications of the Cauchy-Born framework for linking atomistic and continuum scales in material simulations.


**Corresponding Papers:**  
>
> [1] **Yangshuai Wang**, Hao Wang and Lei Zhang, *A Priori Analysis of a Higher Order Nonlinear Elasticity Model for an Atomistic Chain with Periodic Boundary Condition*, **IMA J. Numer. Anal.**, 41:1465-1495, 2020.    
[2] Kejie Fu, Mingjie Liao, **Yangshuai Wang**, Jianjun Chen and Lei Zhang, *Adaptive Multigrid Strategy for Large-scale Molecular Mechanics Optimization*, **J. Comp. Phys.**, 485,112113, 2023.  
[3] Derek Olson, Christoph Ortner, **Yangshuai Wang** and Lei Zhang, *Elastic Far-field Decay from Dislocations in Multilattices*, **Multiscale Model. Simul.**, 21(4), 2023.   
[4] Julian Braun, Christoph Ortner, **Yangshuai Wang** and Lei Zhang, *Higher Order Far-Field Boundary Conditions for Crystalline Defects*, 2022, **arXiv preprint**.       
[5] Xinyi Wei, **Yangshuai Wang**, Kai Jiang and Lei Zhang, *Amplitude Expansion Phase Field Crystal (APFC) Modeling based Efficient Dislocation Simulations using Fourier Pseudospectral Method*, 2024, **arXiv preprint**.   
[6] Mitchell Luskin, Christoph Ortner and **Yangshuai Wang**, *Mathematical Modeling of Materials at the Atomic Scale*, Book Series Texts in Applied Mathematics, **Springer Nature**, under the contract.  
[7] Xinyi Wei, **Yangshuai Wang**, and Lei Zhang, *Higher-Order Boundary Conditions for Dislocation
Simulations*, **In preparation**.  


## Analysis and Applications of Multi-scale Coupling Methods

My research centers on the development and analysis of multi-scale coupling techniques for integrating atomistic-to-continuum (A/C) and quantum mechanics/molecular mechanics (QM/MM) methods. These approaches enable accurate simulations of material systems by bridging scales from quantum-level interactions to macroscopic behavior.

**Highlights:**

- *A Priori Analysis*:
  - Theoretical investigation of the stability, convergence, and error bounds of multi-scale coupling methods.

- *A Posteriori Error Control*:
  - Development of error estimators to assess the reliability of simulation results and guide computational efficiency.

- *Adaptive Algorithm Design*:
  - Creation of adaptive algorithms that dynamically refine simulations based on error indicators, ensuring computational resources are used optimally.

**Corresponding Papers:**  
>
> [1] Huajie Chen, Mingjie Liao, Hao Wang, **Yangshuai Wang** and Lei Zhang, *Adaptive QM/MM Coupling for Crystalline Defects*, **Comput. Methods Appl. Mech. Engrg.**, 354:351-368, 2019.    
[2] **Yangshuai Wang**, Huajie Chen, Mingjie Liao, Christoph Ortner, Hao Wang and Lei Zhang, *A Posteriori Error Estimates for Adaptive QM/MM Coupling Methods*, **SIAM J Sci. Comp.**, 43:A2785-A2808, 2021. 
[3] **Yangshuai Wang** and Hao Wang, *Efficient a Posteriori Error Control of a Consistent Atomistic/Continuum Coupling Method for Two Dimensional Crystalline Defects*, **J. Sci. Comput.**, 97:51, 2023.   
[4] Hao Wang and **Yangshuai Wang**, *Adaptive Multiscale Coupling Methods of Molecular Mechanics Based on a Unified Framework of a Posteriori Error Estimates*, 2023, **arXiv preprint**.       
[5] **Yangshuai Wang**, *A Posteriori Analysis and Adaptive Algorithms for Blended Type Atomistic-to-Continuum Coupling with Higher-Order Finite Elements*, 2023, **arXiv preprint**.   
[6] Kejie Fu, Mingjie Liao, **Yangshuai Wang**, Jianjun Chen and Lei Zhang, *MeshAC: A 3D Mesh Generation and Adaptation Package for Multiscale Coupling Methods*, 2024, **arXiv preprint**.  
[7] Junfeng Lu, Hao Wang and **Yangshuai Wang**, *Formulation and Analysis of the Blended Atomistic to Higher Order Continuum Coupling Methods*, **In preparation**.   
[8] Yanbo Zhan, Hao Wang and **Yangshuai Wang**, *A Priori Analysis for an Atomistic to Nonlinear-Linear Elasticity
Coupling Model in One Dimension*, **In preparation**.  
[9] Yuchuan Zhang, Hao Wang, and **Yangshuai Wang**, *Analysis of the many-body higher-order elastic continuum
approximation with periodic boundary condition for an atomistic chain*, **In preparation**. 


## Scientific Machine Learning:

My research focuses on leveraging data-driven and machine learning techniques to address partial differential equations (PDEs) and other complex scientific and mathematical problems. By integrating computational methods with machine learning, I aim to develop efficient and robust tools for solving real-world challenges.

**Highlights:**

- *Approximation Theory and Error Analysis*:
  - Investigating the theoretical underpinnings of machine learning models for PDEs, including convergence rates and error bounds.

- *Random Feature Methods*:
  - Exploring random feature techniques to improve computational efficiency and scalability in high-dimensional problems.

- *Operator Learning*:
  - Developing machine learning models to approximate solution operators of PDEs, enabling rapid predictions and simulations.

**Corresponding Papers:**  
>
> [1] Zhaohui Fu and **Yangshuai Wang**, *A General Framework for Analyzing Random Feature Method and Discrete Time Algorithms for Solving Time-Dependent Partial Differential Equations*, **In preparation**.   