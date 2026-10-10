---
# Leave the homepage title empty to use the site title
title: ''
summary: 'Yangshuai Wang（王阳帅） — numerical analysis, scientific computing, AI for science, and multiscale materials modeling at the National University of Singapore.'
seo:
  title: 'Yangshuai Wang | 王阳帅'
date: 2022-10-24
lastmod: 2026-10-10
type: landing

# Single-page CV: every section below lives on this one page, in reading
# order, styled as a side-heading + indented-content row (side-section /
# side-collection blocks). The nav bar (config/_default/menus.yaml) links
# to each section's `id` as an in-page anchor. Publications/Preprints/Talks
# show only a partial list with a "see all" link to their full archive page.
sections:
  - block: resume-biography
    id: about
    content:
      username: me
      tags:
        - AI for Science (AI4Science) & Foundation Models
        - Machine-Learned Interatomic Potentials (MLIPs)
        - Multi-scale Modeling of Crystalline Defects
        - Microstructure Evolution & Computational Materials Design
    design:
      avatar:
        size: small

  - block: side-section
    id: interests
    content:
      title: Research Interests
      text: |-
        My research is situated at the intersection of Numerical Analysis, Scientific Computing, and Computational Materials Science. I focus on developing mathematically rigorous and computationally efficient methods for molecular modeling and multi-scale simulation. My specific research directions include:

        **1. AI for Science (AI4Science) & Foundation Models**

        - *LLMs for Scientific Discovery:* Investigating the integration of Large Language Models (LLMs) and specialized foundation models to accelerate scientific workflows, automate property prediction, and facilitate "inverse design" in materials science.
        - *Scientific & Quantum Machine Learning:* Developing data-driven solvers and Quantum Machine Learning (QML) techniques for solving high-dimensional PDEs. My work emphasizes the development of robust numerical algorithms with a focus on Uncertainty Quantification (UQ) and the theoretical analysis of convergence and generalization.

        **2. Machine-Learned Interatomic Potentials (MLIPs)**

        - *Numerical Analysis of MLIPs:* Advancing the mathematical foundation of interatomic potentials by investigating approximation errors, stability, and the reliability of force-field predictions.
        - *Multi-Fidelity & Coarse-Graining:* Developing systematic approaches for fine-tuning pre-trained models and constructing coarse-grained (CG) force fields for soft-matter systems.
        - *Applications in Materials:* Applying these potentials to study complex phenomena in energy storage and conversion materials, ensuring a seamless integration of physics-based priors with data-driven flexibility.

        **3. Multi-scale Modeling of Crystalline Defects**

        - *Coupling Methods:* Engineering and analyzing Atomistic-to-Continuum (A/C) and Quantum Mechanics/Molecular Mechanics (QM/MM) coupling schemes.
        - *Rigorous Error Estimation:* Implementing both a priori and a posteriori error analysis to guide the development of adaptive algorithms that balance accuracy and computational cost.
        - *Boundary Conditions:* Formulating sophisticated boundary conditions to accurately capture the long-range strain fields associated with crystalline defects.

        **4. Microstructure Evolution & Computational Materials Design**

        - *Data-Driven Microstructure Modeling:* Utilizing machine learning to decipher the kinetics of microstructure evolution in complex systems, including optical and magnetic materials.
        - *Multi-scale Property Prediction:* Intersection of multiscale behavior and surrogate modeling to predict macroscopic material performance from mesoscopic morphological data, facilitating the accelerated design of high-performance materials.

  - block: side-section
    id: education
    content:
      title: Education
      text: |-
        **Ph.D in Computational Mathematics**, 2016 – 2021
        Shanghai Jiao Tong University. Supervised by [Prof. Lei Zhang](https://ins.sjtu.edu.cn/people/lzhang/home.html).

        **B.S in Mathematics and Applied Mathematics**, 2012 – 2016
        Sichuan University. Supervised by [Prof. Hao Wang](https://math.scu.edu.cn/info/1013/6696.htm).

  - block: side-section
    id: experience
    content:
      title: Experience
      text: |-
        **Peng Tsu Ann Assistant Professor**, National University of Singapore — Jul 2024 – Present
        Mentored by [Prof. Weizhu Bao](https://blog.nus.edu.sg/matbwz/).

        **Postdoc**, University of British Columbia — Dec 2021 – Jul 2024
        Supervised by [Prof. Christoph Ortner](https://personal.math.ubc.ca/~ortner/).

  - block: side-collection
    id: publications
    content:
      title: Publications
      count: 8
      sort_by: source_order
      numbered: true
      filters:
        folders:
          - publications
        tag: publication
      archive:
        link: /publications/
    design:
      view: citation

  - block: side-collection
    id: preprints
    content:
      title: Preprints
      count: 6
      sort_by: source_order
      numbered: true
      filters:
        folders:
          - publications
        tag: preprint
      archive:
        link: /preprints/
    design:
      view: citation

  - block: side-collection
    id: talks
    content:
      title: Talks
      count: 6
      filters:
        folders:
          - conferences
        exclude_tag: organizer
    design:
      view: citation-talk

  - block: side-section
    id: teaching
    content:
      title: Teaching
      text: |-
        | Term | Role | Course | Institution |
        |---|---|---|---|
        | 2025 Autumn | Lecturer | MA4270 — Data Modeling and Computation | NUS |
        | 2025 Autumn | Lecturer | MA4230 — Matrix Computation | NUS |
        | 2025 Spring | Lecturer | MA5240 — Finite Element Method | NUS |
        | 2024 Autumn | Lecturer | MA4230 — Matrix Computation | NUS |
        | 2023 Autumn | Instructor | MATH 100 | UBC |

        [See all 10 →](/teaching/)

  - block: side-section
    id: awards
    content:
      title: Awards
      text: |-
        | Year | Award |
        |---|---|
        | 2026 | NeurIPS Top Reviewer |
        | 2020 | National Scholarship for Doctoral Students |
        | 2019 | Qiushi Postgraduates Scholarship |
        | 2015 – 2021 | Tanglixin Scholarship |

  - block: side-section
    id: contact
    content:
      title: Contact
      text: |-
        [yswang@nus.edu.sg](mailto:yswang@nus.edu.sg)

        S17-05-16, 10 Lower Kent Ridge Road, National University of Singapore, Singapore 119076

        [Google Sites homepage](https://sites.google.com/view/yangshuaiwang) · [Google Scholar](https://scholar.google.com/citations?user=MDfgwG0AAAAJ&hl=en)
---
