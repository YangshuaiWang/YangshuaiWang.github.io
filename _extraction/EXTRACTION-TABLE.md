# 数据抽取中间表 (Source of Truth)
来源: https://sites.google.com/view/yangshuaiwang/about-me 及其 5 个子页面 (CV / Publications / Selected Preprints / Conferences / Teaching)。
本表由 `_extraction/source-data.json` 自动生成,是所有 Hugo 内容文件填充与核对的唯一依据(single source of truth)。
## ⚠️ 已知的源站异常 / 需要人工确认的点
- About Me page: the hyperlink on 'Prof. Weizhu Bao' points to https://personal.math.ubc.ca/~ortner/ (Christoph Ortner's homepage) instead of a Bao homepage — almost certainly a copy-paste bug on the original Google Site. We did NOT carry this incorrect link over; Weizhu Bao is left as plain text in the new site. Recommend fixing on the Google Site too.
- Publication [27] 'Before Lean Checks...' and Preprint [19] 'Stopping Reliability in Adaptive Krylov-Shadow...' both link to the same arXiv ID 2605.14338, despite being different papers. Reproduced verbatim as-is; flagged for user to check the source.
- Preprint [11] 'Flexible Boundary Sequential Coupling...', Preprint [8] 'NanoTitan...', and Preprint [6] 'A Study on the Fine-Tuning Performance of U-MLIPs...' all link to the same arXiv ID 2506.07401, despite being three different papers. Reproduced verbatim as-is; flagged for user to check the source.
- CV page states 'My Full CV can be found as follows, updated by Sept. 2023' but no PDF/download link or embedded file could be found in the page HTML (likely a Google Sites embedded-file widget that doesn't serialize to static HTML/links). No CV PDF was carried over — left as a TODO for the user to upload their own PDF to uploads/resume.pdf.
- No profile photo, Google Scholar/GitHub/LinkedIn/ORCID/X links, or 'News' section exist anywhere on the source site — confirmed absent, not omitted by mistake.
- Teaching page: the '2023 Autumn: Instructor, MATH 100, UBC' row has no course title given on the source site (only the code MATH 100).

## Profile
| 字段 | 内容 |
|---|---|
| 姓名 | Yangshuai Wang |
| 职位 | Peng Tsu Ann Assistant Professor (Visiting Fellow) |
| 机构 | Department of Mathematics, National University of Singapore (https://www.math.nus.edu.sg/) |
| 邮箱 | yswang@nus.edu.sg |
| 办公地址 | S17-05-16, 10 Lower Kent Ridge Road, National University of Singapore, Singapore 119076. |

## Education
| 学位 | 机构 | 起止 | 导师 |
|---|---|---|---|
| Ph.D | Shanghai Jiao Tong University | 2016-09 – 2021-12 | Prof. Lei Zhang |
| B.S | Sichuan University | 2012-09 – 2016-06 | Prof. Hao Wang |

## Experience
| 职位 | 机构 | 起止 | 导师/合作者 |
|---|---|---|---|
| Peng Tsu Ann Assistant Professor | National University of Singapore | 2024-07 – Present | Prof. Weizhu Bao |
| Postdoc | University of British Columbia | 2021-12 – 2024-07 | Prof. Christoph Ortner |

## Awards
| 名称 | 时间 |
|---|---|
| National Scholarship for Doctoral Students | 2020 |
| Qiushi Postgraduates Scholarship | 2019 |
| Tanglixin Scholarship | 2015-2021 |

## Publications (27 篇)
| # | 作者备注 | 标题 | 作者 | 期刊/会议 | 年份 | 链接 |
|---|---|---|---|---|---|---|
| 27 | Corresponding author | Before Lean Checks: Candidate Exposure in Proof-Action Ranking | Shivangi Kamat, me | arXiv preprint; accepted by ICML 2026 Workshop AI4Math | 2026 | http://arxiv.org/abs/2605.14338 |
| 26 |  | Amplitude Expansion Phase Field Crystal (APFC) Modeling based Efficient Dislocation Simulations using Fourier Pseudospectral Method | Xinyi Wei, me, Kai Jiang, Lei Zhang | J. Sci. Comput. | 2026 | https://link.springer.com/epdf/10.1007/s10915-026-03376-8?sharing_token=S_RCrz-k2nLi2XKH7PMYDPe4RwlQNchNByi7wbcMAY6ytA1Xukv2AQZGTbDQqxrxR31inTpCxkhcWJzSFSPYZz7qKHgpM1ts2ZsgooTy3UMOOiHhO5uOW2_iiOIYocrZfs-KR5_L-he72eMJOvMy0MuUY25X_CwEm4ZOQGizKDY%3D |
| 25 | Corresponding author | Higher-Order Boundary Conditions for Atomistic Dislocation Simulations | Xinyi Wei, Julian Braun, me, Lei Zhang | accepted by SIAM J Sci. Comp. | 2026 | (无) |
| 24 | Corresponding author | A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks | Yifan Yu, Cheuk Hin Ho, me | J. Comp. Phys. | 2026 | https://doi.org/10.1016/j.jcp.2026.114979 |
| 23 | Corresponding author | Flexible Uncertainty Calibration for Machine-Learned Interatomic Potentials | Cheuk Hin Ho, Christoph Ortner, me | npj Comput. Mater. | 2026 | https://doi.org/10.1038/s41524-026-02080-3 |
| 22 |  | Bayesian Physics-Informed Neural Networks to Solve the PDEs with Noise or Incomplete Constraints | Xi'an Li, Jinran Wu, Xiao Ning, me, Lei Zhang | Innov. Inform. (Editorial) | 2026 | https://www.the-innovation.org/article/doi/10.59717/j.xinn-inform.2026.100039 |
| 21 |  | Concurrent Atomistic-Continuum Coupling via Physics-Informed Neural Networks (PINNs-CAC) with Adaptive Energy Weighting and Direct Boundary Encoding | Peng Liu, Lidong Fang, me, Lei Zhang, Qingcheng Yang | Appl. Math. Model. | 2026 | https://www.sciencedirect.com/science/article/abs/pii/S0307904X26001927 |
| 20 | Corresponding author | Beyond Adam: Disentangling Optimizer Effects in the Fine-Tuning of Atomistic Foundation Models | Xiaoqing Liu, me, Teng Zhao | AI for Sci. | 2026 | https://iopscience.iop.org/article/10.1088/3050-287X/ae5078 |
| 19 | Corresponding author | Adaptive Multiscale Coupling Methods of Molecular Mechanics Based on a Unified Framework of a Posteriori Error Estimates | Hao Wang, me | Comput. Phys. Commun. | 2026 | https://www.sciencedirect.com/science/article/pii/S0010465526000676?dgcid=author |
| 18 | Co-corresponding author | Fine-Tuning Universal Machine-Learned Interatomic Potentials: A Tutorial on Methods and Applications | Xiaoqing Liu, me, Kehan Zeng, Zedong Luo, Teng Zhao, Zhenli Xu | J. Appl. Phys. | 2026 | https://arxiv.org/pdf/2506.21935 |
| 17 | Co-corresponding author | MicroEvoEval: A Systematic Evaluation Framework for Image-Based Microstructure Evolution Prediction | Qinyi Zhang, Duanyu Feng, Ronghui Han, me, Hao Wang | Proceedings of the AAAI Conference on Artificial Intelligence | 2026 | https://arxiv.org/abs/2511.08955 |
| 16 |  | An Atomic Cluster Expansion Potential for Twisted Multilayer Graphene | me, Drake Clark, Sambit Das, Ziyan Zhu, Daniel Massatt, Vikram Gavini, Mitchell Luskin, Christoph Ortner | Mach. Learn.: Sci. Technol. | 2025 | https://iopscience.iop.org/article/10.1088/2632-2153/ae1807 |
| 15 |  | A Foundation Model for Atomistic Materials Chemistry | Ilyes Batatia, Philipp Benner, Yuan Chiang, Alin M. Elena, Dávid P. Kovács, and Janosh Riebesell et al. (62 authors not shown) | J. Chem. Phys. | 2025 | https://pubs.aip.org/aip/jcp/article/163/18/184110/3372267/A-foundation-model-for-atomistic-materials |
| 14 | Corresponding author | Higher Order Far-Field Boundary Conditions for Crystalline Defects | Julian Braun, Christoph Ortner, me, Lei Zhang | SIAM J. Numer. Anal. | 2025 | https://epubs.siam.org/doi/abs/10.1137/24M165836X |
| 13 | Corresponding author | Surrogate models for vibrational entropy based on a spatial decomposition | Tina Torabi, Christoph Ortner, me | SIAM Multiscale Model. Simul. | 2025 | https://epubs.siam.org/doi/abs/10.1137/24M165168X?journalCode=mmsubt |
| 12 |  | A Posteriori Analysis and Adaptive Algorithms for Blended Type Atomistic-to-Continuum Coupling with Higher-Order Finite Elements | me | Comput. Phys. Commun. | 2025 | https://doi.org/10.1016/j.cpc.2025.109533 |
| 11 | Corresponding author | MeshAC: A 3D Mesh Generation and Adaptation Package for Multiscale Coupling Methods | Kejie Fu, Mingjie Liao, me, Jianjun Chen, Lei Zhang | Comput. Phys. Commun. (Computer Programs in Physics) | 2025 | https://www.sciencedirect.com/science/article/abs/pii/S0010465525000268?CMX_ID=&SIS_ID=&dgcid=STMJ_219742_AUTH_SERV_PA&utm_acid=270809738&utm_campaign=STMJ_219742_AUTH_SERV_PA&utm_in=DM540521&utm_medium=email&utm_source=AC_; https://github.com/kjfu/MeshAC |
| 10 |  | A Posteriori Error Estimate and Adaptivity for QM/MM Models of Crystalline Defects | me, James Kermode, Christoph Ortner, Lei Zhang | Comput. Methods Appl. Mech. Engrg. | 2024 | https://www.sciencedirect.com/science/article/pii/S0045782524003530 |
| 9 |  | A Theoretical Case Study of the Generalisation of Machine-learned Potentials | me, Shashwat Patel, Christoph Ortner | Comput. Methods Appl. Mech. Engrg. | 2024 | https://www.sciencedirect.com/science/article/pii/S0045782524000872 |
| 8 |  | Efficient a Posteriori Error Control of a Consistent Atomistic/Continuum Coupling Method for Two Dimensional Crystalline Defects | me, Hao Wang | J. Sci. Comput. | 2023 | https://link.springer.com/article/10.1007/s10915-023-02362-8 |
| 7 | Corresponding author | Elastic Far-field Decay from Dislocations in Multilattices | Derek Olson, Christoph Ortner, me, Lei Zhang | SIAM Multiscale Model. Simul. | 2023 | https://epubs.siam.org/doi/full/10.1137/22M1502021 |
| 6 | Corresponding author | A Framework for a Generalisation Analysis of Machine-learned Interatomic Potentials | Christoph Ortner, me | SIAM Multiscale Model. Simul. | 2023 | https://epubs.siam.org/doi/10.1137/22M152267X |
| 5 | Corresponding author | Adaptive Multigrid Strategy for Large-scale Molecular Mechanics Optimization | Kejie Fu, Mingjie Liao, me, Jianjun Chen, Lei Zhang | J. Comp. Phys. | 2023 | https://www.sciencedirect.com/science/article/pii/S0021999123002085?via%3Dihub |
| 4 | Corresponding author | QM/MM Methods for Crystalline Defects. Part 3: Machine-learned MM Models | Huajie Chen, Christoph Ortner, me | SIAM Multiscale Model. Simul. | 2022 | https://epubs.siam.org/doi/10.1137/21M1441122 |
| 3 |  | A Posteriori Error Estimates for Adaptive QM/MM Coupling Methods | me, Huajie Chen, Mingjie Liao, Christoph Ortner, Hao Wang, Lei Zhang | SIAM J Sci. Comp. | 2021 | https://epubs.siam.org/doi/10.1137/20M1353678 |
| 2 |  | A Priori Analysis of a Higher Order Nonlinear Elasticity Model for an Atomistic Chain with Periodic Boundary Condition | me, Hao Wang, Lei Zhang | IMA J. Numer. Anal. | 2020 | https://academic.oup.com/imajna/article-abstract/41/2/1465/5837821?redirectedFrom=fulltext&login=false |
| 1 | Alphabetic order | Adaptive QM/MM Coupling for Crystalline Defects | Huajie Chen, Mingjie Liao, Hao Wang, me, Lei Zhang | Comput. Methods Appl. Mech. Engrg. | 2019 | https://www.sciencedirect.com/science/article/pii/S0045782519302233?via%3Dihub |

## Selected Preprints (23 篇)
| # | 作者备注 | 标题 | 作者 | 状态 | 年份 | 链接 |
|---|---|---|---|---|---|---|
| 25 | Corresponding author | Residual-Christoffel Sampling for Random Feature Collocation of Linear PDEs | Jiale Linghu, me | under review | 2026 | http://arxiv.org/abs/2607.13382 |
| 24 | Corresponding author | Trainable Photonic Measurement for Physics-Informed PDE Learning | Jiale Linghu, Hao Dong, me | under review | 2026 | http://arxiv.org/abs/2606.18713 |
| 23 | Corresponding author | Random Feature Kalman Filtering for Linear PDE Data Assimilation | Xi'an Li, Jiale Linghu, me | under review | 2026 | https://arxiv.org/abs/2606.16086 |
| 22 | Corresponding author | Liquid Random Feature Methods for Time-Dependent Partial Differential Equations | Jiale Linghu, me | under review | 2026 | https://arxiv.org/abs/2606.15571 |
| 21 | Corresponding author | Local Surrogates for Harmonic Vibrational Entropy in Multilattices | Tina Torabi, Jiale Linghu, me | under review | 2026 | http://arxiv.org/abs/2605.26588 |
| 20 | Corresponding author | Geometry-Preserving Nudged Elastic Band and Dimer Methods under Anisotropic Force Uncertainty | Yifan Yu, me | under review | 2026 | https://arxiv.org/abs/2605.24401 |
| 19 | Corresponding author | Stopping Reliability in Adaptive Krylov-Shadow Quantum Fisher Information Estimation | Erjie Liu, me | under review | 2026 | http://arxiv.org/abs/2605.14338 |
| 18 |  | IADR: Interface-Augmented Neural Operator for Phase-Field Mean-Curvature Flow | Qinyi Zhang, Duanyu Feng, me, Hao Wang | under review | 2026 | (无) |
| 17 | Corresponding author | The Geometry of Adapter Placement in Equivariant Machine-Learned Interatomic Potentials | Xiaoqing Liu, me | under review | 2026 | (无) |
| 16 | Corresponding author | Long-Range Operator Learning: Comparative Diagnostics for Transformer Reasoning and Equivariant Interatomic Potentials | Xiaoqing Liu, me | under review | 2026 | (无) |
| 15 | Co-corresponding author | A Discrete-Time Random Feature Method for Nonlinear Evolution Equations with Implicit-Explicit Runge–Kutta Time Stepping | Haoran Zhou, Zhaohui Fu, me, Xinlong Feng | under review | 2026 | http://arxiv.org/abs/2604.25502 |
| 14 |  | Symmetry-Protected Basin Localization in Variational Quantum Eigensolvers | me | under review | 2026 | http://arxiv.org/abs/2605.09909 |
| 13 | Corresponding author | Analysis of Hessian Variance Scaling for Local and Global Cost Functions in Variational Quantum Algorithms | Yihan Huang, me | under review | 2026 | https://arxiv.org/abs/2602.00783 |
| 12 | Corresponding author | LDD-RFM: Learnable Domain Decomposition for Random Feature Models via Variable Projection | Zhaohui Fu, Duanyu Feng, me | under review | 2026 | (无) |
| 11 | Co-first author | Flexible Boundary Sequential Coupling for Atomistic Simulation of Crystal Defects | Yanbo Zhan, me, Xingyu Gao, Hao Wang |  | 2026 | https://arxiv.org/abs/2506.07401 |
| 10 |  | 2D-ProteinRAG: Mitigating Intent-Context Misalignment in Homology-Based Protein Question Answering | Li Ding, Duanyu Feng, Chen Huang, me, Wenqiang Lei | under review | 2026 | (无) |
| 9 | Corresponding author | Trainability-Oriented Hybrid Quantum Regression via Geometric Preconditioning and Curriculum Optimization | Qingyu Meng, me | under review | 2026 | https://arxiv.org/abs/2601.11942 |
| 8 |  | NanoTitan: An AI-Driven Memory-Efficient Platform for High-Performance Molecular Dynamics Simulation | me, Yongfa Guo, Zedong Luo, Xiaoqing Liu, Cheng Chen, Qi Zhou, Teng Zhao, Zhenli Xu |  | 2025 | https://arxiv.org/abs/2506.07401 |
| 7 | Co-first author | An AI-Ready Fine-Tuning Framework for Accurate Machine-Learning Interatomic Potentials in Solid–Solid Battery Interfaces | Xiaoqing Liu, Xinyu Yu, me, Zhe-Tao Sun, Zedong Luo, Kehan Zeng, Teng Zhao, Shou-Hang Bo, Zhenli Xu | under review | 2025 | https://arxiv.org/abs/2601.17847 |
| 6 | Corresponding author | A Study on the Fine-Tuning Performance of Universal Machine-Learned Interatomic Potentials (U-MLIPs) | Xiaoqing Liu, Kehan Zeng, me, Teng Zhao |  | 2025 | https://arxiv.org/abs/2506.07401 |
| 5 | Co-corresponding author | Formulation and Analysis of Blended Atomistic to Higher-Order Continuum Coupling Methods for Crystalline Defects | Junfeng Lu, Hao Wang, me |  | 2025 | https://arxiv.org/abs/2502.18854 |
| 4 | Co-corresponding author | A General Framework of Linear Elasticity Enhanced Multiscale Coupling Methods for Crystalline Defects | Yanbo Zhan, me, Hao Wang | under review | 2025 | https://arxiv.org/abs/2502.17164 |
| 3 |  | Many-Body Coarse-Grained Molecular Dynamics with the Atomic Cluster Expansion | me, Gabor Csanyi, Christoph Ortner |  | 2025 | https://arxiv.org/abs/2502.04661 |

**Book**: Mitchell Luskin, Christoph Ortner, me, *Mathematical Modeling of Materials at the Atomic Scale*, Texts in Applied Mathematics, Springer Nature, under the contract.

**Thesis**: me, *Some Progress on Multi-scale Methods in Materials Modeling*, Shanghai Jiao Tong University, 2021.

## Conferences — Organizing
| 标题 | 场合 | 角色 | 地点 | 日期 |
|---|---|---|---|---|
| Numerical Methods, Mathematical Modeling and Analysis in Materials Science | mini-symposium in WCCM 2024 | organizer | Vancouver Convention Centre, Vancouver | 2024-07-21 to 2024-07-26 |
| Analysis, Methods and Applications in Complex Materials | mini-symposium in ICIAM 2023 | co-organizer | Waseda University | 2023-08-25 |

## Conferences — Invited Talks (21 场)
| 标题 | 地点 | 日期 |
|---|---|---|
| Workshop on Mathematical Theory, Methods, and Applications in Materials Simulations (Tianyuan Mathematical Center in Science and Technology, TMCST) | Kunming | 2025-05-18 to 2025-05-24 |
| Computational Multiscale Methods | Oberwolfach | 2025-04-27 to 2025-05-02 |
| 22nd Annual Conference of China Society for Industrial and Applied Mathematics (CSIAM 2024) | Nanjing | 2024-10-25 to 2024-10-27 |
| International Workshop on Data-driven Computational and Theoretical Materials Design (DCTMD) | Shanghai | 2024-10-09 to 2024-10-13 |
| Advancing Molecular Simulations with Machine-Learned Interatomic Potentials | Sichuan Normal University | 2024-07-03 |
| Machine Learning in Multiscale and Reduced Order Methods for the Simulation of Physical Systems (International Conference on Scientific Computation and Differential Equations, SciCADE 2024) | National University of Singapore | 2024-07-15 to 2024-07-19 |
| Advancing Molecular Simulations with Machine-Learned Interatomic Potentials | Beijing Normal University | 2024-06-13 |
| Using Uncertainty Quantification to Improve Learning in Atomistic Modeling (SIAM Conference on Mathematical Aspects of Materials Science) | Pittsburgh, Pennsylvania | 2024-05-19 to 2024-05-23 |
| Machine Learning Force Fields, Data-Driven Materials Informatics (Institute for Mathematical and Statistical Innovation) | University of Chicago | 2024-04-04 to 2024-04-08 |
| Application of machine-learned interatomic potentials in atomic-scale simulations and beyond (Data Science Seminars) | University of Minnesota | 2024-04-02 |
| Enhacing Machine-Learned Interatomic Potentials in Materials Science: Progressing from Accuracy to Robustness (Hot Topics in AI for Sciences) | Shanghai Jiao Tong University | 2024-02-29 |
| Application of machine-learned interatomic potentials in atomic-scale simulations and beyond (Model Reduction and Simulation at Atomic Scale) | University of Warwick | 2024-01-26 |
| Mathematical Modeling, Analysis and Applications of Machine-Learned Interatomic Potentials | Shanghai Jiao Tong University (online) | 2023-06-12 |
| Atomic Cluster Expansion with and without Atoms | Beijing Normal University (online) | 2023-03-10 |
| A Framework for a Generalisation Analysis of Machine-Learned Interatomic Potentials (Atomic Cluster Expansion (ACE) Seminar) | University of Cambridge (online) | 2022-10-19 |
| A Framework for a Generalisation Analysis of Machine-Learned Interatomic Potentials (online) (Computational Methods in Applied Mathematics, CMAM 2022) | TU Wien | 2022-08-31 |
| Error Propagation of Machine-Learned Interatomic Potentials (MLIPs) (Machine-learned Interatomic Potentials Mini-workshop) | IPAM UCLA | 2022-05-12 |
| A Posteriori Error Estimates for Adaptive QM/MM Coupling Methods (Workshop on Computational Materials Science) | Sichuan University (online) | 2021-11-15 |
| The Applications of Data-Driven Interatomic Potentials to QM/MM Coupling Methods (International Workshop on Mathematical Theory, Methods and Application in Materials Simulation) | Shanghai Jiao Tong University | 2021-04-11 |
| Adaptive QM/MM Coupling Methods (Workshop on Materials Modeling, University of Warwick-Shanghai Jiao Tong University-University of British Columbia) | online | 2020-06 |
| Some Recent Progress on Multiscale Coupling Methods (Top-notch Doctoral Seminar in Computational and Applied Mathematics) | Peking University | 2019-09-04 |

## Teaching (10 门)
| 学期 | 角色 | 课程代码 | 课程名 | 机构 |
|---|---|---|---|---|
| 2025 Autumn | Lecturer | MA4270 | Data Modeling and Computation | NUS |
| 2025 Autumn | Lecturer | MA4230 | Matrix Computation | NUS |
| 2025 Spring | Lecturer | MA5240 | Finite Element Method | NUS |
| 2024 Autumn | Lecturer | MA4230 | Matrix Computation | NUS |
| 2023 Autumn | Instructor | MATH 100 | (未提供) | UBC |
| 2021 Autumn | Teaching Assistant |  | Advanced Computational Methods | SJTU |
| 2019 Spring | Teaching Assistant |  | Numerical Methods for Partial Differential Equations | SJTU |
| 2018 Spring | Teaching Assistant |  | Applied Mathematics Methods | SJTU |
| 2017 Spring | Teaching Assistant |  | Scientific Computing | SJTU |
| 2017 Autumn | Teaching Assistant |  | Mathematical Analysis | SJTU |
