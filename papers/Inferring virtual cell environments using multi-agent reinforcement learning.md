---
title: "Inferring virtual cell environments using multi-agent reinforcement learning"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/inferring-virtual-cell-environments-using-multi-agent-reinforcement-learning.md]
confidence: medium
year: 2025
---

# Inferring virtual cell environments using multi-agent reinforcement learning

> 原文: [[inferring-virtual-cell-environments-using-multi-agent-reinforcement-learning]]

## 摘要

28 perturbation, can prioritize spatial and developmental genes for single-cell-level changes, enabling the 29 generation of new insights into cell dynamics over time and space. CellTRIP is open source as a general 30 tool and available at github.com/daifengwanglab/CellTRIP. 31 2 Introduction 32 Single cells continually interact and establish a cell environment to coordinate many key biological 33 processes, such as development and disease progression. For example, within tissue microenvironments, 34 cells develop along different lineages and migrate to specific regions during maturation of cell types, 35 such as T cell lineages1. Furthermore, gene expression, a key single-cell-level mechanism to determine 36 cellular function, can be controlled by intracellular gene regulation and through intercellular molecular 37 interactions with neighboring cells2,3. These interactions are dynamic, developing the cell environment 38 to drive specific biological processes. These environments are sensitive to small perturbations. Varying 39 conditionscanleadtoheterogeneousfunctionaloutcomes. Forexample,inter-individualvarianceintumor 40 immune microenvironments can dictate responsiveness to chemo-immunotherapy4. Characterizing these 41 environments is critical to understanding a wide range of developmental, pathological, and embryonic 42 processes, among others.

## 背景与目的

84 during Drosophila embryonic and larval development8. 85 3 Methods 86 CellTRIP infers a virtual cell environment from the single-cell data (e.g., gene expression) for spatiotem- 87 poral imputation and perturbation prediction. Given a single-cell dataset, each Cell i has |K| types of 88 measurements, such as gene expression and spatial location, where K is a set of indices representing 89 each type of measurement. Let m⃗ ( i k) ∈ Rn mk represent measured data for Cell i in modality k ∈ K with 90 n mk features. We also define the matrix M(k) ∈ Rnc×n mk, where each row is m⃗ ( i k) over all n c cells in the 91 2 bioRxiv preprint doi: this version posted November 24, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. : CellTRIP uses multi-agent reinforcement learning techniques to infer virtual cell environments from static biological data for spatiotemporal imputation and perturbation prediction. The model learns to optimally construct environment spaces to maximize data retention from source modalities. Retention quality and reliability are communicated to the model through environmental rewards, while the model can interact with the environment by imparting forces on each cell, independently.

## 主要发现

normal distribution, ∆⃗v i t ∼ N(E s (⃗s i t),diag(σ2)), where diag(σ2) ∈ Rn d ×n d is a diagonal covariance 177 matrix with all nonzero entries σ. Note that, internally, σ is stored in log-form to prevent negative 178 values for σ from backpropagation. The computed cell actions are then applied to the environment 179 space according to Equation 1 to iterate the cell positions and velocities. The model is trained using 180 proximal policy optimization (PPO), simulating multiple environments in parallel and iterating at fixed 181 step intervals until convergence. We additionally utilize novel input scaling techniques derived from 182 PopArt normalization21. For more details concerning model training or the distributed environment, see 183 Supplementary Section S1 and Supplementary Section S6. 184 3.4 Cell Spatiotemporal Imputation and Perturbation Prediction 185 With the trained CellTRIP model, specifically π and ρ(k), we can perform spatiotemporal imputation and θˆ 186 perturbationprediction. Spatiotemporalimputationcanbeviewedastwomajorcomponents, thosebeing 187 spatialandtemporalimputation. CellTRIPusespinningmodules, ρ(k), toestimatetargetmodalitiesfrom 188 the environment space, Xt (Section 3.4.1). These pinning modules also enable imputation of single-cell 189 spatial coordinates from gene expression data.

## 方法概述

363 distribution of cell spatial coordinates in embryonic and early larval stages (a). CellTRIP spatial 364 12 bioRxiv preprint doi: this version posted November 24, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder. All rights reserved. No reuse allowed without permission. imputation performance was comparable to other methods on most training stages, but had the lowest 365 prediction MSE (CellTRIP 90.41, MLP 333.86, KNN 360.33) and highest classification accuracy of 10 366 tissue types (CellTRIP 0.237, MLP 0.231, KNN 0.207, Baseline 0.100) on the heldout developmental 367 stageE16-18h_a andinamajorityofconstituenttissuetypes(Figure5bandSupplementaryFigureS11). 368 Wethenperformedtemporalimputationtoinferthespatialtrajectoryofcellsbetweenknowndevelop- 369 mental timepoints, and subsequently recover the cellular spatial distribution of our held out intermediate 370 developmental stage (Section 3.4.2, Figure S1). First, we use optimal transport to match pseudocells 371 between the stages immediately preceding and following E16-18h_a, namely, E14-16h_a and L1_a. We 372 then used CellTRIP to compute a spatial trajectory between the two timepoints, selecting an interme- 373 diate trajectory timestep to recover the cell spatial distribution of E16-18h_a (c).

## 讨论与结论

417 distributed computing for forwards and backwards passes and user-adjustable inference settings mitigate 418 this runtime limitation significantly. CellTRIP needs to employ additional strategies to ensure minimal 419 usage of both memory and VRAM throughout the running process. CellTRIP can also be extended to 420 predict cell death, proliferation, or the spread of disease in tissue samples through modifications to the 421 environment space and policy actions. 422 References 423 1. Yayon, N., Kedlian, V. R., Boehme, L., Suo, C., Wachter, B. T., Beuschel, R. T., Amsalem, O., 424 Polanski, K., Koplev, S., Tuck, E., Dann, E., Van Hulle, J., Perera, S., Putteman, T., Predeus, 425 A. V., Dabrowska, M., Richardson, L., Tudor, C., Kreins, A. Y., Engelbert, J., Stephenson, E., 426 Kleshchevnikov, V., De Rita, F., Crossland, D., Bosticardo, M., Pala, F., Prigmore, E., Chipampe, 427 N.-J., Prete, M., Fei, L., To, K., Barker, R. A., He, X., Van Nieuwerburgh, F., Bayraktar, O. A., 428 Patel, M., Davies, E. G., Haniffa, M. A., Uhlmann, V., Notarangelo, L. D., Germain, R. N., Radtke, 429 A. J., Marioni, J. C., Taghon, T., and Teichmann, S. A. (2024). A spatial human thymus cell atlas 430 mapped to a continuous tissue axis. Nature 635, 708–718. URL: 431 s41586-024-07944-6. doi:10.1038/s41586-024-07944-6. 432 2. Binan, L., Jiang, A., Danquah, S. A., Valakh, V., Simonton, B., Bezney, J., Manguso, R. T., 433 Yates, K. B., Nehme, R., Cleary, B., and Farhi, S. L.

## 关键词

Inferring, cell, environments, learning, multi-agent, reinforcement, using, virtual

## 相关实体

细胞类型: T cell, all
方法: single-cell
疾病: disease

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
