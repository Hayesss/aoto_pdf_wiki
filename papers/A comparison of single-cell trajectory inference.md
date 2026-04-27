---
title: "A comparison of single-cell trajectory inference"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/a-comparison-of-single-cell-trajectory-inference.md]
confidence: medium
year: 2019
marker_extracted: true
---

# A comparison of single-cell trajectory inference

> 原文: [[a-comparison-of-single-cell-trajectory-inference]]

## 摘要

Trajectory inference approaches analyze genome-wide omics data from thousands of single cells and computationally infer the order of these cells along developmental trajectories. Although more than 70 trajectory inference tools have already been developed, it is challenging to compare their performance because the input they require and output models they produce vary substantially. Here, we benchmark 45 of these methods on 110 real and 229 synthetic datasets for cellular ordering, topology, scalability and usability. Our results highlight the complementarity of existing tools, and that the choice of method should depend mostly on the dataset dimensions and trajectory topology. Based on these results, we develop a set of guidelines to help users select the best method for their dataset. Our freely available data and evaluation pipeline ([https://benchmark.dynverse.org\)](https://benchmark.dynverse.org) will aid in the development of improved tools designed to analyze increasingly large and complex single-cell datasets.


## 背景与目的

branches dist similarity in cellular positions between two trajectories, by calculating the correlation between pairwise geodesic distances. Finally, wcor quantifies features the agreement between trajectory differentially expressed features from the known trajectory and the predicted trajectory. harder to know a priori, and which can potentially introduce a large well across the board (Fig. 2b). We will discuss each evaluation cri- bias into the analysis (Fig. 2a). terion in more detail (Fig. 3 and Supplementary Fig. 2), after which The largest difference between TI methods is whether a method we conclude with guidelines for method users and future perspec- fixes the topology and, if it does not, what kind of topology it can tives for method developers. detect.

## 主要发现

**Trajectory inference methods.** To make the outputs from different methods directly comparable to each other, we developed a common probabilistic model for representing trajectories from all possible sources (Fig. [1b](#page-1-0)). In this model, the overall topology is represented by a network of 'milestones', and the cells are placed within the space formed by each set of connected milestones. Although almost every method returned a unique set of outputs, we were able to classify these outputs into seven distinct groups (Supplementary Fig. 1) and we wrote a common output converter for each of these groups (Fig. [2a](#page-2-0)). When strictly required, we also provided prior information to the method. These different priors can range from weak priors that are relatively easy to acquire, such as a start cell, to strong priors, such as a known grouping of cells, that are much

Data mining and Modelling for Biomedicine, VIB Center for Inflammation Research, Ghent, Belgium. 2 Department of Applied Mathematics, Computer Science and Statistics, Ghent University, Ghent, Belgium. 3 Center for Medical Genetics, Ghent University Hospital, Ghent, Belgium. 4Department of Biomolecular Medicine, Ghent University, Ghent, Belgium. 5 Centre International de Recherche en Infectiologie, Inserm, U1111, Université Claude Bernard Lyon 1, CNRS, UMR5308, École Normale Supérieure de Lyon, Université de Lyon, Lyon, France. 6These authors contributed equally: Wouter Saelens, Robrecht Cannoodt. \*e-mail: [yvan.saeys@ugent.be](mailto:yvan.saeys@ugent.be)

ARTICLES NATURE BIOTECHNOLOGY

 Overview of several key aspects of the evaluation. **a**, A schematic overview of our evaluation pipeline. **b**, To make the trajectories comparable to each other, a common trajectory model was used to represent reference trajectories from the real and synthetic datasets, as well as any predictions of TI methods.


## 方法概述

Trajectory inference methods. We gathered a list of 71 trajectory inference tools (Supplementary Table 1) by searching the literature for 'trajectory inference' and 'pseudotemporal ordering', and based on two existing lists found online: https://github.com/seandavi/awesome-single-cell and https://github.com/agitter/single-cell-pseudotime. We welcome any contributions by creating an issue at https://methods.dynverse.org.

Methods were excluded from the evaluation based on several criteria: (1) not freely available; (2) no code available; (3) superseded by another method; (4) requires data types other than expression; (5) no programming interface; (6) unresolved errors during wrapping; (7) too slow (requires more than 1 h on a 100×100 dataset); (8) does not return an ordering; and (9) requires additional user input during the algorithm (other than prior information). The discussions on why these methods were excluded can be found at https://github.com/dynverse/dynmethods/issues?q=label:unwrappable. In the end, we included 45 methods in the evaluation.

Method wrappers. To make it easy to run each method in a reproducible manner, each method was wrapped within Docker and singularity containers (available at <a href="https://methods.dynverse.org">https://methods.dynverse.org</a>). These containers are automatically built and tested using Travis continuous integration (<a href="https://travis-ci.org/dynverse">https://travis-ci.org/dynverse</a>) and can be ran using both Docker and Singularity. For each method, we wrote a wrapper script based on example scripts or tutorials provided by the authors (as mentioned in the respective wrapper scripts). This script reads in the input data, runs the method and outputs the files required to construct a trajectory. We also created a script to generate an example dataset, which is used for automated testing.


## 讨论与结论

In this study, we presented a large-scale evaluation of the performance of 45 TI methods. By using a common trajectory representation and four metrics to compare the methods' outputs, we were able to assess the accuracy of the methods on more than 200 datasets. We also assessed several other important quality measures, such as the quality of the method's implementation, the scalability to hundreds of thousands of cells and the stability of the output on small variations of the datasets.

Based on the results of our benchmark, we propose a set of practical guidelines for method users (Fig. and guidelines.dynverse. org). We postulate that, as a method's performance is heavily dependent on the trajectory type being studied, the choice of method should currently be primarily driven by the anticipated trajectory topology in the data. For most use cases, the user will know very little about the expected trajectory, except perhaps whether the data is expected to contain multiple disconnected trajectories, cycles or a complex tree structure. In each of these use cases, our evaluation

 Trajectories inferred by each method were projected to a common dimensionality reduction using multidimensional scaling. For each dataset, we also calculated a 'consensus' prediction, by calculating the cor<sub>dist</sub> between each pair of models and picking the model with the highest score on average. **a**, The top methods applied on a dataset containing a linear trajectory of differentiation dendritic cells, going from MDP, CDP to PreDC. **b**, The top methods applied on a dataset containing a bifurcating trajectory of reprogrammed fibroblasts. **c**, A synthetic dataset generated by dyntoy, containing four disconnected trajectories. **d**, A synthetic dataset generated by dyngen, containing a cyclic trajectory.

suggests a different set of optimal methods, as shown in Fig. 5.


## 关键词

comparison, inference, single-cell, trajectory

## 相关实体

细胞类型: all
方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
