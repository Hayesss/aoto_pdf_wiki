---
marker_extracted: true
title: "Protocol Check for updates CellChat for systematic analysis"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/protocol-check-for-updates-cellchat-for-systematic-analysis.md]
confidence: medium
year: 2022
---

# Protocol Check for updates CellChat for systematic analysis

> 原文: [[protocol-check-for-updates-cellchat-for-systematic-analysis]]

## 摘要

Recent advances in single-cell sequencing technologies offer an opportunity to explore cell-cell communication in tissues systematically and with reduced bias. A key challenge is integrating known molecular interactions and measurements into a framework to identify and analyze complex cell-cell communication networks. Previously, we developed a computational tool, named CellChat, that infers and analyzes cell-cell communication networks from single-cell transcriptomic data within an easily interpretable framework. CellChat quantifies the signaling communication probability between two cell groups using a simplified mass-action-based model, which incorporates the core interaction between ligands and receptors with multisubunit structure along with modulation by cofactors. Importantly, CellChat performs a systematic and comparative analysis of cell-cell communication using a variety of quantitative metrics and machine-learning approaches. CellChat v2 is an updated version that includes additional comparison functionalities, an expanded database of ligand-receptor pairs along with rich functional annotations, and an Interactive CellChat Explorer. Here we provide a stepby-step protocol for using CellChat v2 on single-cell transcriptomic data, including inference and analysis of cell-cell communication from one dataset and identification of altered intercellular communication, signals and cell populations from different datasets across biological conditions. The Rimplementation of CellChat v2 toolkit and its tutorials together with the graphic outputs are available at https://github.com/jinworks/CellChat. This protocol typically takes ~5 min depending on dataset size and requires a basic understanding of R and single-cell data analysis but no specialized bioinformatics training for its implementation.



## 背景与目的

Cell–cell communication orchestrates tissue organization. Recent advances in single-cell genomics offer unprecedented opportunities to systematically explore signaling mechanisms for cell fate decisions and their consequent tissue phenotypes. Using single-cell transcriptomic data and ligand–receptor (L–R) interaction information from prior knowledge, computational methods such as CellPhoneDB have been developed for inferring cell–cell communication between groups of cells[1–](#page-38-0)[4](#page-38-1) . However, a versatile and easy-to-use toolkit capable of systematic analysis and intuitive visualization of cell–cell communication as well as comparison analysis across biological conditions was still needed, so we developed CellChat to systematically and comprehensively infer and analyze cell–cell communication from single-cell transcriptomic data within an easily interpretable framewor[k5](#page-38-2) .



## 主要发现

L1–R1 L1–R2 L2–R1 L2–R3 L3–R4 L5–R6 C1 → C C 2 1 → C C 3 1 → C C 4 1 → C C 5 1 → C6 Sender Mediator Identification of signaling roles for cells Discovery of cell group and using network centraility analysis signaling’s coordinated behavior Receiver Influencer Comparative analysis across biological conditions (Procedure 2, Steps 1–13; Procedure 3, Steps 1–4) )sredneS( secruoS Targets (Receivers) C4 C5 C6 C3 C1 C2 Outgoing centrality score erocs ytilartnec gnimocnI C1 FGF C2 P1 P1 V C E C G L F CXCL C3 CSF C4 P2 P2 C T D N 4 F 0 C5 WNT GAS C6 P3 P3 TGFb Cell groups Patterns Signaling Specific signaling Shared Specific Shared Dim 1 2 miD gnilangiS CXCL WNT Information flow snoitcaretni fo rebmuN Up 0 Down gnilangiS Cell groups )redneS( secruoS C3 C2 C4 C1 C5 C6 Social network theory and metrics Targets (Receivers) secruoS 3D communication probability array Targets L–R pairs or pathways (~3,300 L–R pairs) Influencer Mediator Receiver Sender ; Word cloud ...... 12% Secreted Signaling 38%20% ECM−Receptor Cell−Cell Contact 30% Non-protein Signaling 45% Heterodimers 55% Others Rich annotations of L–R pairs ••Classification (e.g., secreted) ••Signaling pathways (e.g.

## 方法概述

save(db.new, file = "CellChatDB.human_user.rda") Nature Protocols | Volume 20 | January 2025 | 180–219 188 Protocol Experimental design RNA isolation and sequencing data Although CellChat can, in principle, be used for any single-cell transcriptomics datasets, the quality of datasets directly affects the quality of CellChat outputs. First, having sufficient sequencing depth is critical to capturing gene expression of ligands and receptors. Expression levels are usually low for ligands during development, so sensitivity and depth of sequencing become particularly important for such cases. Second, batch effect may introduce output variability for any inference method, including CellChat.

## 讨论与结论

pathway by summarizing all cell groups displayed in the heatmap. CellChat employs a pattern recognition method to identify global communication patterns. For outgoing (or incoming) patterns, the cell group pattern indicates how these cell groups coordinate to send (or receive) signals and the signaling pathway pattern indicates how these signaling pathways work together to send (or receive) signals. To intuitively show the associations of latent patterns with cell groups and signaling pathways or L–R pairs, we used a river (alluvial) plot. As the number of patterns increases, there might be redundant patterns, making it difficult to interpret the communication patterns.

## 关键词

CellChat, Check, Protocol, analysis, systematic, updates

## 相关实体

通路: WNT
方法: single-cell

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
