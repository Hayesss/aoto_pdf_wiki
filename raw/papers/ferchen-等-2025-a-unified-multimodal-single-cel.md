---
source_url: zotero://select/items/32MHZCQC
ingested: 2026-04-22
sha256: 8104898adcf5da50
---

# Ferchen 等 - 2025 - A unified multimodal single-cell framework reveals a discrete state model of hematopoiesis in mice

> Zotero Item Key: 32MHZCQC
> Original File: Ferchen 等 - 2025 - A unified multimodal single-cell framework reveals a discrete state model of hematopoiesis in mice.pdf

## Extracted Text

nature immunology
Resource https://doi.org/10.1038/s41590-025-02307-3
A unified multimodal single-cell
framework reveals a discrete state model of
hematopoiesis in mice
Received: 7 March 2025 Kyle Ferchen 1, Xuan Zhang 1, Kairavee Thakkar 2,3, Guangyuan Li 2,
David Bernardicius1, Sidharth Sen2, Priyanka Rawat 2, Andre Olsson1,
Accepted: 11 September 2025
Sierra N. Bennett1, Crystal Potter4, Fred D. Finkelman4, Josh Croteau 5,
Published online: 22 October 2025 Samantha Morris 6,7,8, Harinder Singh 9,10 , Nathan Salomonis 2,11 &
H. Leighton Grimes 1,11,12
Check for updates
Large-scale, unbiased single-cell genomics studies of complex
developmental compartments, such as hematopoiesis, have inferred
novel cell states and trajectories; however, further characterization has
been hampered by difficulty isolating cells corresponding to discrete
genomic states. To address this, we present a framework that integrates
multimodal single-cell analyses (RNA, surface protein and chromatin) with
high-dimensional flow cytometry and enables semiautomated enrichment
and functional characterization of diverse cell states. Our approach
combines transcription factor expression with chromatin activity to
uncover hierarchical gene regulatory networks driving these states. We
delineated and isolated rare bone m ar row L in −S ca− C D1 17+ CD27+ multilineage
cell states (‘MultiLin’), validated predicted lineage trajectories and mapped
differentiation potentials. Additionally, we used transcription factor activity
on chromatin to trace and isolate multilineage progenitors undergoing
multipotent to oligopotent lineage restriction. In the proposed model
of steady-state hematopoiesis, discrete states governed developmental
trajectories. This framework provides a scalable solution for isolating and
characterizing novel cell states across different biological systems.
A fundamental challenge in developmental biology is understand- developmental relationships and cellular potentials. Newer meth-
ing the hierarchical states within stem cell and progenitor com- ods, such as CITE-seq, combine transcriptome profiles and surface
partments, along with the gene regulatory networks (GRNs) that protein data but do not permit the isolation of discrete populations
drive cell fate decisions. GRNs involve transcription factors that act because these methods are destructive. Integrating CITE-seq with
on regulatory elements like enhancers and silencers, influencing high-dimensional flow cytometry (for example, InfinityFlow1,2)
cell-type-specific gene expression patterns. Single-cell genomics provides a powerful approach to isolate and study cell populations
technologies like single-cell RNA sequencing (scRNA-seq) and assay manifesting discrete transcriptional and chromatin signatures, thus
for transposase-accessible chromatin using sequencing (ATAC–seq) offering insights into the developmental potential of progenitors and
provide high-resolution data on transcriptome and chromatin states. their underlying GRNs.
However, due to technical limitations, these techniques often rely Flow cytometry has long been used to identify and isolate pro-
on inferential rather than experimental evidence to understand genitor populations based on surface markers. This method has helped
A full list of affiliations appears at the end of the paper. e-mail: harinder@pitt.edu; nathan.salomonis@cchmc.org; lee.grimes@cchmc.org
Nature Immunology | Volume 26 | November 2025 | 2086–2099 2086
Resource https://doi.org/10.1038/s41590-025-02307-3
define key progenitor cell types like multipotent progenitors (MPPs), CITE-seq antibodies have been previously molecularly titrated
megakaryocyte–erythroid progenitors (MEPs), common myeloid with antibody-derived oligonucleotide tags (ADTs) on human bone
progenitors (CMPs), granulocyte–monocyte progenitors (GMPs) and marrow by diluting them and analyzing ADT sequence abundance
common lymphoid progenitors (CLPs), forming the basis of the clas- by scRNA-seq10. To evaluate their performance, we initially manu-
sical model of hematopoiesis. However, flow cytometry is limited ally titrated 65 TotalSeq-A antibodies on CD117+-enriched mouse
by the number of detectable markers, and recent findings show that bone marrow cells9,11 and then captured the progenitor gates men-
these progenitor populations are more heterogeneous than previously tioned earlier using TotalSeq-A Universal Cocktail (Universal Mix
thought3–5. New techniques, including scRNA-seq, have revealed a more v1.0, n = 195; Supplementary Tables 1 and 2). As previously shown in
complex view of hematopoiesis, suggesting that lineage commitment humans10, manual titration improved the detection of many ADTs
is a continuum rather than a series of stable, defined states6,7. More over a universal mix (Extended Data Fig. 2a,b). Individual fivefold
recently, the punctuated continuum model reintroduced the classical titrations of 195 antibodies (Extended Data Fig. 2d) were prioritized
concept of stability across developmental trajectories, with pools of for an optimized CITE-seq panel based on known discriminative
cells that are variably lineage specified8. markers of progenitor populations as well as dose-dependent signals
Novel bioinformatics approaches and clonogenic assays have of the antibodies used for detection (Fig. 1c). The revised titrated
helped identify intermediate progenitor states, such as multilineage CITE-seq panel of 103 ADTs demonstrated improved cell-state
(MultiLin) cells, which exhibit mixed-lineage gene expression and reclassification accuracy when used to profile 63,000 new cells in
reside within traditional CMP and GMP gates4,5,9. These findings chal- HSC-MPP, CD127+, MultiLin and CD117+ gates (Methods, Extended
lenge classical progenitor definitions, highlighting the importance Data Fig. 2a–c,e and Supplementary Tables 1 and 2). To annotate the
of transitional states in lineage specification. To better understand captured populations, we compiled a database of reference cell states
hematopoietic progenitors, we combined multiomic single-cell meth- for HSC-MPP, dendritic cell, basophil–mast cell commitment, early
ods with high-dimensional flow cytometric profiling1,2 (Extended Data lymphoid and myeloid intermediate cells (Methods) and integrated
Fig. 1a) and developed a unified computational framework (termed RNA and ADTs across the database of published cell populations with
‘ChromLinker’) that integrates data from different sources to derive those from unsupervised clustering of each modality (ICGS2 (ref. 12))
GRNs that reflect developmental trajectories (Extended Data Fig. 1b). using scTriangulate13 (Extended Data Fig. 2f). scTriangulate identi-
Analysis of transcription factor activities on accessible chromatin fied 87 stable discrete cell states, as evidenced by modality-specific
regions identified key surface proteins, such as CD55 and CD371, as contribution scores and cluster confidence (Extended Data Fig. 2g–j).
markers of critical lineage transitions in Lin−Sca−CD117+CD27+ Mul- This multimodal integration defined clusters from a combination
tiLin progenitors (Extended Data Fig. 1c). This framework provides of prior-defined cell states (n = 31) and unsupervised transcrip-
a comprehensive view of progenitor heterogeneity and reveals how tome (n = 40) or ADT (n = 16) clustering (Extended Data Fig. 2k).
transcriptional and chromatin profiles influence lineage commitment To supplement this atlas, we used a well-based scRNA-seq cap-
and orchestrate steady-state blood production, forming the basis of a ture method (HIVE; Methods) to analyze CD117+ progenitors and
model of steady-state hematopoiesis in which discrete states govern Lin−CD117+CD34+CD115−Ly6C− MultiLin populations along with
developmental trajectories (Extended Data Fig. 1d). Interactive analysis gates enriched for CD125+ eosinophil and FcER1a+ basophil–mast
tools and datasets for the MarrowAtlas are available at https://altana- cell progenitors (BMC

... [truncated]
