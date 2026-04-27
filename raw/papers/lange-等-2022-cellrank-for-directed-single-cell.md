---
source_url: zotero://select/items/34NN9JEU
ingested: 2026-04-22
sha256: 138438e044efb833
---

# Lange 等 - 2022 - CellRank for directed single-cell fate mapping

> Zotero Item Key: 34NN9JEU
> Original File: Lange 等 - 2022 - CellRank for directed single-cell fate mapping.pdf

## Extracted Text

Articles
https://doi.org/10.1038/s41592-021-01346-6
CellRank for directed single-cell fate mapping
Marius Lange 1,2, Volker Bergen 1,2, Michal Klein1, Manu Setty3,10, Bernhard Reuter 4,5,
Mostafa Bakhti 6,7, Heiko Lickert 6,7, Meshal Ansari 1,8, Janine Schniering8, Herbert B. Schiller 8,
Dana Pe’er 3 ✉ and Fabian J. Theis 1,2,9 ✉
Computational trajectory inference enables the reconstruction of cell state dynamics from single-cell RNA sequencing experi-
ments. However, trajectory inference requires that the direction of a biological process is known, largely limiting its application
to differentiating systems in normal development. Here, we present CellRank (https://cellrank.org) for single-cell fate mapping
in diverse scenarios, including regeneration, reprogramming and disease, for which direction is unknown. Our approach com-
bines the robustness of trajectory inference with directional information from RNA velocity, taking into account the gradual and
stochastic nature of cellular fate decisions, as well as uncertainty in velocity vectors. On pancreas development data, CellRank
automatically detects initial, intermediate and terminal populations, predicts fate potentials and visualizes continuous gene
expression trends along individual lineages. Applied to lineage-traced cellular reprogramming data, predicted fate probabilities
correctly recover reprogramming outcomes. CellRank also predicts a new dedifferentiation trajectory during postinjury lung
regeneration, including previously unknown intermediate cell states, which we confirm experimentally.
C
ells undergo state transitions during many biological pro- information from RNA velocity to learn directed, probabilistic
cesses, including development, reprogramming, regeneration state-change trajectories under either normal or perturbed condi-
and cancer, and they typically do so in a highly asynchronous tions. Unlike other approaches, CellRank automatically infers initial,
fashion1. Single-cell RNA sequencing (scRNA-seq) successfully cap- intermediate and terminal populations of an scRNA-seq dataset and
tures the heterogeneity that results from these processes, but it loses computes fate probabilities that account for the stochastic nature of
lineage relationships, since each cell can be measured only once. To cellular fate decisions as well as uncertainty in velocity estimates.
mitigate this problem, scRNA-seq can be combined with lineage We use fate probabilities to uncover putative lineage drivers and to
tracing methods2,3 that use heritable barcodes to follow clonal evo- visualize lineage-specific gene expression trends. We demonstrate
lution over long time scales, or metabolic labeling methods4–6 that CellRank’s capabilities on pancreatic endocrine lineage develop-
use the ratio of nascent to mature RNA molecules to link observed ment, correctly recovering initial and terminal states in addition to
gene expression profiles over short time windows. Yet both strat- lineage bias and key driver genes for somatostatin-producing delta
egies are mostly limited to in vitro applications, prompting the cell differentiation. We show that CellRank generalizes beyond
development of computational approaches to reconstruct pseudo- normal development by applying it to a reprogramming dataset,
time trajectories1,7–12, which leverage the observation that develop- where predicted fate bias correctly recovers lineage-tracing-derived
mentally related cells tend to share similar gene expression profiles. ground truth. Further, by applying CellRank to lung regeneration,
Pseudotime approaches have been used extensively to order cells we predict a new dedifferentiation trajectory and experimentally
along differentiation trajectories and to study cell-fate decisions. validate newly discovered intermediate cell states. CellRank out-
Computational trajectory inference typically demands prior performs methods that do not include velocity information, and is
biological knowledge to determine the directionality of cell state available as a scalable, user-friendly open-source software package
changes, often by specifying an initial cell13, thereby limiting its with documentation and tutorials at https://cellrank.org.
applicability to normal developmental scenarios with known
cell-fate hierarchies. RNA velocity14 has been shown recently to Results
alleviate this problem by reconstructing trajectory direction based CellRank combines cell–cell similarity with RNA velocity to
on the spliced-to-unspliced mRNA ratio. The approach has been model cellular state transitions. The CellRank algorithm aims
generalized to include transient cell populations and protein kinet- to model the cell state dynamics of a system (Methods). CellRank
ics15,16; however, velocity estimates are noisy and the interpretation detects the initial, terminal and intermediate cell states of the system
of high-dimensional velocity vectors has been limited mostly to and computes a global map of fate potentials, assigning each cell the
low-dimensional projections, which do not easily reveal long-range probability of reaching each terminal state. Based on the inferred
probabilistic fates or allow quantitative interpretation. potentials, CellRank charts gene expression dynamics as cells take
Here, we present CellRank, a method that combines the robust- on different fates and identifies putative regulators of cell-fate
ness of similarity-based trajectory inference with directional decisions. The algorithm uses an scRNA-seq count matrix and
1Institute of Computational Biology, Helmholtz Center Munich, Munich, Germany. 2Department of Mathematics, Technical University of Munich, Munich,
Germany. 3Program for Computational and Systems Biology, Sloan Kettering Institute, Memorial Sloan Kettering Cancer Center, New York, NY, USA.
4Department of Computer Science, University of Tübingen, Tübingen, Germany. 5Zuse Institute Berlin (ZIB), Berlin, Germany. 6Institute of Diabetes
and Regeneration Research, Helmholtz Center Munich, Munich, Germany. 7German Center for Diabetes Research (DZD), Neuherberg, Germany.
8Comprehensive Pneumology Center (CPC) / Institute of Lung Biology and Disease (ILBD), Helmholtz Zentrum München, Member of the German Center
for Lung Research (DZL), Munich, Germany. 9TUM School of Life Sciences Weihenstephan, Technical University of Munich, Munich, Germany. 10Present
address: Basic Sciences Division and Translational Data Science IRC, Fred Hutchinson Cancer Research Center, Seattle WA, USA. ✉e-mail: peerd@mskcc.org;
fabian.theis@helmholtz-muenchen.de
NATuRe MeTHoDS | VOL 19 | FeBRUARY 2022 | 159–170 | www.nature.com/naturemethods 159
Articles NAtuRE MEtHODS
corresponding RNA velocity matrix as input (Extended Data Figure and cell–cell similarities by aggregating many of these into our final
1a,c). Note that, while we use RNA velocity here to approximate the fate prediction. Moreover, by restricting transitions to be within the
direction of cellular dynamics, CellRank generalizes to accommo- phenotypic manifold, CellRank captures cell state dynamics more
date any vector field that provides a directional measure, such as faithfully.
metabolic labeling4–6 or real time information17,18. Both the original velocyto and generalized scVelo models com-
The main assumption underlying all pseudotime algorithms that pute velocity vectors on the basis of spliced-to-unspliced count
faithfully capture trajectories1,7–10 is that cell states change in small ratios14,15. These counts are influenced by many sources of biologi-
steps with many transitional populations. CellRank uses the same cal and technical noise, such as ambient RNA, sparsity, doublets,
assumption to model state transitions using a Markov chain, where bursting kinetics and low capture efficiency. Unspliced RNA in
each state in the chain is given by one observed cellular profile, and particular is rarer in the cell and suffers from low detection rates.
edge weights denote the probability of transition

... [truncated]
