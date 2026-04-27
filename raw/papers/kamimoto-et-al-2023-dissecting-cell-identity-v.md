---
source_url: zotero://select/items/286YXBE4
ingested: 2026-04-22
sha256: ddd576104c1b0d9c
---

# Kamimoto et al. - 2023 - Dissecting cell identity via network inference and

> Zotero Item Key: 286YXBE4
> Original File: Kamimoto et al. - 2023 - Dissecting cell identity via network inference and.pdf

## Extracted Text

Article
Dissecting cell identity via network
inference and in silico gene perturbation
https://doi.org/10.1038/s41586-022-05688-9 Kenji Kamimoto1,2,3, Blerta Stringa1,3, Christy M. Hoffmann1,2,3, Kunal Jindal1,2,3,
Lilianna Solnica-Krezel1,3 & Samantha A. Morris1,2,3 ✉
Received: 4 January 2022
Accepted: 28 December 2022
Cell identity is governed by the complex regulation of gene expression, represented
Published online: 8 February 2023
as gene-regulatory networks1. Here we use gene-regulatory networks inferred from
Open access
single-cell multi-omics data to perform in silico transcription factor perturbations,
Check for updates simulating the consequent changes in cell identity using only unperturbed wild-type
data. We apply this machine-learning-based approach, CellOracle, to well-established
paradigms—mouse and human haematopoiesis, and zebrafish embryogenesis—
and we correctly model reported changes in phenotype that occur as a result of
transcription factor perturbation. Through systematic in silico transcription factor
perturbation in the developing zebrafish, we simulate and experimentally validate a
previously unreported phenotype that results from the loss of noto, an established
notochord regulator. Furthermore, we identify an axial mesoderm regulator, lhx1a.
Together, these results show that CellOracle can be used to analyse the regulation of
cell identity by transcription factors, and can provide mechanistic insights into
development and differentiation.
The expansion of single-cell technologies into perturbational omics is cell fate regulation governed by TFs. Furthermore, we apply CellOracle
enabling the development of methods to characterize cell identity. For to systematically perturb TFs across zebrafish development, recover-
example, single-cell RNA sequencing (scRNA-seq) coupled with pooled ing known and putative regulators of cell identity. Focusing on axial
CRISPR screens offers much promise for analysing the genetic regula- mesoderm, we predict and validate a prechordal plate phenotype after
tion of cell identity2–4, but cannot be readily used in many biological con- loss of function (LOF) of the prototypical notochord regulator, noto.
texts. Computational methods to simulate single-cell phenotypes after Moreover, we also simulate and validate a role for the TF lhx1a in the
perturbation are emerging, although many approaches still require development of axial mesoderm. Together, these results show that
experimental perturbation data for model training, and thus their scale CellOracle can be used to infer and interpret cell-type-specific GRN
and application are limited5. Moreover, previous deep-learning-based configurations at high resolution, enabling mechanistic insights into
models represent a ‘black box’, which restricts the interpretation of the regulation of cell identity. CellOracle code and documentation are
gene-regulatory mechanisms that underlie the simulated biological available at https://github.com/morris-lab/CellOracle and data can be
events. In this respect, gene-regulatory network (GRN) modelling explored at https://celloracle.org.
approaches are promising as they reconstruct systematic gene–gene
associations from unperturbed single-cell omics data6–11. However,
In silico gene perturbation using CellOracle
previous methods for analysing GRNs largely focus on the static net-
work structure, and determining how a static GRN governs cell identity To gain mechanistic insight into the regulation of cell identity, we
during dynamic biological processes therefore remains a challenge. developed an in silico strategy to simulate changes in cell identity upon
Scalable and interpretable approaches are required to understand how TF perturbation. CellOracle uses custom GRN modelling (Extended
gene-regulatory mechanisms relate to observed complex single-cell Data Fig. 1a) to simulate global downstream shifts in gene expression
phenotypes. following knockout (KO) or overexpression of TFs. These simulated
Here we present a strategy that overcomes these limitations by values are converted into a vector map of transitions in cell identity,
combining computational perturbation with GRN modelling. Cel- which enables simulated changes in cell identity to be intuitively visu-
lOracle integrates multimodal data to build custom GRN models that alized within a low-dimension space (Fig. 1a and Methods). In silico
are specifically designed to simulate shifts in cell identity following perturbation involves four steps. (1) Cell-type- or cell-state-specific
transcription factor (TF) perturbation, providing a systematic and GRN configurations are constructed using cluster-wise regularized
intuitive interpretation of context-dependent TF function in regulat- linear regression models with multi-omics data. (2) Using these GRN
ing cell identity. We apply CellOracle to well-characterized biological models, shifts in target gene expression in response to TF perturba-
systems: haematopoiesis in mice and humans; and the differentiation tion are calculated. This step applies the GRN model as a function to
of axial mesoderm into notochord and prechordal plate in zebrafish. propagate the shift in gene expression rather than the absolute gene
In haematopoiesis, we show that CellOracle recapitulates well-known expression value, representing the signal flow from TF to target gene.
1Department of Developmental Biology, Washington University School of Medicine in St Louis, St Louis, MO, USA. 2Department of Genetics, Washington University School of Medicine in St Louis,
St Louis, MO, USA. 3Center of Regenerative Medicine, Washington University School of Medicine in St Louis, St Louis, MO, USA. ✉e-mail: s.morris@wustl.edu
742 | Nature | Vol 614 | 23 February 2023
b
c d e
GMPs Monocytes GM lineage differentiation
GMPs
inhibited
MEPs
MEPs
MEP
differentiation
Granulocytes promoted
PS
Erythrocytes 1 × 10–3
–5 0 5
f g MPP i
GMP differentiation promoted Gata1
0.8 Spi1
Gene annotation MEP GMP 0.6 ME lineage
differentiation
GM lineage h differentiation
ME lineage LLaattee GGMMPP Late GMP 0.4 Both GM and ME
differentiation,
differentiation maintenance
inhibited Other or unknown 0.2
PS 0 1 × 10–3 GGrr D aann if uu fe lloo re cc n yyyy t tt i ee ation in G hi r b a i n te u d lo f c ro y m te 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
–5 0 5 late GMP to early granulocyte Negative PS sum in GM lineage
This signal is propagated iteratively to calculate the broad, down- to a two-dimensional (2D) vector, allowing for more robust predic-
stream effects of TF perturbation, allowing the global transcriptional tions against noise (Extended Data Fig. 1e). We purposefully limit the
‘shift’ to be estimated (Extended Data Fig. 1b–d). (3) The cell-identity simulation output data to a 2D vector representing the predicted shift
transition probability is estimated by comparing this shift in gene in cell identity because our goal is to model changes in identity rather
expression to the gene expression of local neighbours. (4) The transi- than predicting absolute changes in gene expression levels. Further
tion probability is converted into a weighted local average vector to details of the CellOracle algorithm are provided in the Methods, includ-
represent the simulated directionality of cell-state transition for each ing validation of the range of simulated values; null or randomized
cell following perturbation of candidate TFs. In the final calculation model analysis; and hyperparameter evaluation (Supplementary
step, the multi-dimensional gene expression shift vector is reduced Figs. 2–10).
Nature | Vol 614 | 23 February 2023 | 743
egaenil
EM
ni mus
SP
evitageN
Monocytes
Mk
GMPs
MEPs
Granulocytes
Erythrocytes
FA1
2AF
scRNA-seq data
Late GMPs
Cluster 1 configuration
Gene C perturbation
Gene B perturbation
Cluster 1 Cluster 2 configuration
Cluster 2
Cluster 3
scATAC-seq data
Cluster 3
Co-accessible peaks
Zbtb7a E2f4
Klf1
Gata1 Smarcc1
Bdp1 Nfe2l2 Smarca5 Ybx1 Smarcc2Cbx5
Nfia Lmo2 Nfatc3 Elf1*


... [truncated]
