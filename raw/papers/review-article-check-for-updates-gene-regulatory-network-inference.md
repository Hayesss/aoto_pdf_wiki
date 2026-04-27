---
source_path: /mnt/c/Users/Administrator/Zotero/storage/DL4Q54CL/Badia-i-Mompel 等 - 2023 - Gene regulatory network inference in the era of si.pdf
ingested: 2026-04-23
sha256: 55d91f3e6a27ebaa
---

nature reviews genetics https://doi.org/10.1038/s41576-023-00618-5
Review article Check for updates
Gene regulatory network inference
in the era of single-cell multi-omics
Pau Badia-i-Mompel 1, Lorna Wessels 1,2, Sophia Müller-Dott 1, Rémi Trimbour 1,3, Ricardo O. Ramirez Flores 1,
Ricard Argelaguet 4 & Julio Saez-Rodriguez 1
Abstract Sections
The interplay between chromatin, transcription factors and genes Introduction
generates complex regulatory circuits that can be represented as
Inference of GRNs
gene regulatory networks (GRNs). The study of GRNs is useful to
Downstream GRN analyses
understand how cellular identity is established, maintained and
Experimental assessment of
disrupted in disease. GRNs can be inferred from experimental
GRNs
data — historically, bulk omics data — and/or from the literature.
Challenges and future
The advent of single-cell multi-omics technologies has led to the directions
development of novel computational methods that leverage genomic,
Conclusions
transcriptomic and chromatin accessibility information to infer GRNs
at an unprecedented resolution. Here, we review the key principles of
inferring GRNs that encompass transcription factor–gene interactions
from transcriptomics and chromatin accessibility data. We focus
on the comparison and classification of methods that use single-
cell multimodal data. We highlight challenges in GRN inference,
in particular with respect to benchmarking, and potential further
developments using additional data modalities.
1Heidelberg University, Faculty of Medicine, Heidelberg University Hospital, Institute for Computational
Biomedicine, Bioquant, Heidelberg, Germany. 2Department of Vascular Biology and Tumor Angiogenesis,
European Center for Angioscience, Medical Faculty, MannHeim Heidelberg University, Mannheim, Germany.
3Institut Pasteur, Université Paris Cité, CNRS UMR 3738, Machine Learning for Integrative Genomics Group, Paris,
France. 4Altos Labs, Granta Park, Cambridge, UK. e-mail: pub.saez@uni-heidelberg.de
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 739
Review article
Introduction In this Review, we outline general principles of GRN inference and
Cells regulate gene transcription to coordinate cellular activities in their potential limitations. Furthermore, we describe how multimodal
response to intracellular and extracellular signals. Transcription is read-outs can be leveraged to infer more accurate GRNs, and we classify
largely regulated by transcription factors (TFs), proteins that bind and briefly describe several novel tools that have been developed for
to specific sequences of DNA (DNA binding sites) and can have posi- this task. In addition, we highlight possible downstream GRN analyses
tive or negative effects on the transcriptional rate of target genes1. and how to assess experimentally the obtained results. Finally, we
Genomic DNA is tightly packed with structural proteins into com- discuss current challenges and future directions in the field.
plexes known as nucleosomes, which are the basic unit of chromatin,
making most genes inaccessible to the transcription machinery. To Inference of GRNs
enable transcription, the region near a gene transcription start site, GRN inference refers to the process of summarizing gene regulation — a
known as the promoter, needs to be exposed by displacing tightly highly complex and dynamic process — into an interpretable network
packed nucleosomes. Changes in DNA accessibility can be triggered structure from data using computational methods. It is based on the
by the binding of so-called pioneer TFs2. Other TFs can bind to distal assumption that the effects of a true underlying GRN can be observed
cis-regulatory elements (CREs) of the DNA and, together with cofac- and measured in molecular data29 (Fig. 1b). Interactions in GRNs can
tors and other proteins, cooperatively enable the recruitment and be directed or undirected (denoting a causality relationship between
stabilization of the RNA polymerase protein complex that synthesizes genes or lack of it, respectively), signed (denoting the mode of regula-
mRNA from the gene body DNA (Fig. 1a). tion, positive or negative) and/or weighted (denoting the strength of
Gene regulatory networks (GRNs) are interpretable computational the interaction).
models of the regulation of gene expression in the form of networks,
mathematically also defined as graphs. Multiple components of gene From transcriptomics data
regulation, such as TFs, splicing factors, long non-coding RNAs, micro- Methods in this category fit models that try to explain the observed
RNAs and metabolites, can be incorporated in GRNs. Here, we focus variability of gene expression based on the expression of other genes.
on their simplest representation, which captures only the interplay Weighted gene co-expression network analysis (WGCNA)19 is one of
between TFs and target genes, whereby the nodes of the GRN consist the simplest and most popular approaches. It carries out pairwise
of genes, some of them being TFs, and the edges of the GRN represent correlations across the whole transcriptome to identify modules of
regulatory interactions between the genes (Fig. 1b). Other possible co-expressed genes. The resulting network is commonly known as a
GRN representations are discussed elsewhere3–6. Uncovering the topol- gene co-expression network and its interactions are undirected owing to
ogy and the dynamics of GRNs is fundamental to understanding how the symmetrical nature of correlations. Although this strategy is useful
cellular identity is established and maintained7, which has important to identify gene modules in an unsupervised manner, the lack of causal
implications for engineering cell fate8 and for disease prevention9. regulatory links hinders its interpretability and typically yields a large
Understanding GRNs is a long-standing quest in biology, as illus- number of false positive associations. To address these limitations,
trated by the seminal work from the 1960s characterizing the bacte- methods such as GENIE3 (ref. 20) and its faster implementation GRN-
rial lactose (lac) operon10. Reconstructing large-scale GRNs became a Boost2 (ref. 30) first distinguish TFs from target genes based on previ-
major focus of systems biology, leveraging various high-throughput ously reported regulatory activity31 and then train models that predict
experimental methods and computational algorithms11–13. Histori- the expression of target genes based solely on the expression of TFs,
cally, GRNs have been commonly assembled from experimentally which markedly reduces the number of interactions to be considered.
validated regulation events compiled in databases14–17 or inferred By doing so, undirected interactions are turned into directed connec-
de novo from gene co-expression in bulk transcriptomics data18–20. tions and thus introduce putative causal relationships. Nevertheless,
If sufficient transcriptomics data are available, GRNs can be inferred inference from transcriptomics data alone introduces false positives
that are better contextualized for the biological question at hand as many other mechanisms that are involved in gene regulation, such as
than GRNs extracted from databases, which tend to be generalistic. chromatin accessibility, are ignored. Moreover, because many pro-
However, transcriptomics data do not directly capture many under- cesses are required for a mRNA transcript encoding a TF to become
lying regulatory mechanisms, such as the TF protein abundance and a functional protein, transcript levels alone might not be informative
DNA binding events, cooperation of TFs and cofactors, alternative enough1,32. These limitations may hinder the inference process, as it
transcript splicing, post-translational protein modification events and has been shown that, overall, these methods tend to have moderate
the accessibility and structure of the genome. The inclusion and meas- success in accurately inferring GRNs33–35.
urement of these other aspects of gene regulation has the potential to
generate GRNs that better represent gene regulation in vivo (Fig. 1b). From TF binding data or chromatin accessibility
For example, the inclusion of chromatin accessibility21 data allows to Assays such as chromatin immunoprecipitation followed by sequencing
fine-tune TF–gene links by considering whether genes are open and (ChIP-seq)36 and cleavage under targets and tagmentation (CUT&Tag)37
by including CREs in the inference of GRNs. enable TF binding to be measured across the genome. This informa-
Furthermore, bulk profiling provides mixed measures across tion can be used to build GRNs directly by assigning TF binding sites
cell types in a tissue sample, and thus cannot disentangle regulatory to putative target genes38. However, despite some high-throughput
programmes specific to particular cell types or cell states22,23. This alternatives39–41, profiling of TF binding is still costly and limited to
limitation has been overcome by the use of single-cell technologies24,25, TFs for which antibodies are available. In addition, the use of TF bind-
allowing the inference of GRNs across different cell types, differentia- ing data alone typically requires the assignment of bound TFs to their
tion trajectories and conditions (Fig. 1c). For this reason, and with the target genes by closest genomic proximity, ignoring possible distal
introduction of multimodal profiling technologies26–28, there has been interaction events that are known to be relevant in gene regulation1.
a recent explosion of novel GRN inference methods. By contrast, a pioneering study explored the integration of ChIP-seq
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 740
Review article
a
TF Cofactor RNA polymerase
b
data and transcriptomics data to enable a more refined assignment of
GRN
TFs to genes that did not depend on the closest gene42.
An alternative approach is to use chromatin accessibility data to
infer gene regulatory elements that are potentially targeted by TFs.
The most commonly used technology owing to its simple and relatively
cheap protocol is the assay for transposase accessible chromatin with
TF Activation sequencing (ATAC-seq)21, but other technologies exist such as DNase-
Gene Inhibition seq43 and NOME-seq44 (reviewed elsewhere45). Methods that leverage
Chromatin accessibility chromatin accessibility data split GRN inference into two steps: first,
the assignment of TFs to gene regulatory elements (open chromatin
regions, commonly referred to as peaks); and second, the assignment of
these regulatory elements to genes (Fig. 2). For the first step, methods
leverage TF binding motif databases and motif matcher algorithms to
make binding predictions for TFs on accessible CREs (Box 1). For the
second step, methods link accessible CREs to genes that are within a
certain genomic distance. The distance cutoff is based on the observa-
tion that distal CREs such as enhancers or silencers generally interact
with the promoter regions of genes at a typical distance1. Some exam-
c Single-cell omics data ples of such inference methods include ATAC2GRN (ref. 46), LISA47
and SPIDER48. These methods assume that if the promoter region of
a gene is accessible, the gene is being transcribed, but that might not
always be the case.
From single-cell transcriptomics data
GRN inference methods using bulk omics data have enabled the charac-
UMAP 1 terization of genome-wide regulatory events but, in the case of mixed
samples such as tissues, they cannot capture the cell type or state
specificity of GRNs22,23. In addition, GRN inference methods require
Cell type and state specificity Dynamic cell Differences between large sample sizes to generate sufficient data, which can become
trajectories conditions
prohibitively costly in bulk profiling.
With the emergence of single-cell technologies, particularly
single-cell RNA sequencing (scRNA-seq), GRN reconstruction meth-
ods have been used to infer cell type-specific TF–gene interactions,
together with the dynamic changes that occur in these GRNs across
development and conditions49 (Fig. 1c). One of the first GRN inference
Pseudotime methods tailored to scRNA-seq data was SCENIC50, an extension to
the GRNBoost2 (ref. 30) method, which generates cell type-specific
GRNs by exploiting TF–gene co-expression patterns and, in addition,
prunes the edges of the GRN based on TF binding motif enrichment
on gene promoter regions. The improved resolution of single-cell
measurements also enables the identification of dynamic cell states
and their transitions that may not be easily differentiated into distinct
groups, such as during development, cell differentiation or disease
progression51,52. Pseudotime ordering characterizes these continuous
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 741
2 PAMU
Transcription start site
DNA CRE Promoter Gene body
region
mRNA
Observable data
Features
Gene coexpression
Assignment of TFs
TF binding motif analysis
Healthy individuals
GRN of cell type A
Patients with disease
GRN of cell type B GRN of cell type C
snoitavresbO
Fig. 1 | Principles of gene regulatory networks. a, Gene regulation and
its key elements. Transcription factors (TFs) bind to promoter regions and
cis-regulatory elements (CREs), displacing nucleosomes and making the
transcription start site accessible. Cooperation between TFs, cofactors and other
proteins allows for the recruitment and stabilization of the RNA polymerase
protein complex, which synthesizes mRNA from the gene body DNA. b, Gene
regulatory networks (GRNs) can be inferred from measured omics data and,
through the modelling of additional information such as TF binding predictions
or chromatin accessibility, can be refined to better resemble the true underlying
GRN. The nodes of the GRN are TFs and their regulated genes, and the edges
between nodes indicate the mode of regulation (activation or inhibition).
c, GRNs generated from single-cell omics data allow to understand cell type and
state specificity, explain the progression of dynamic trajectories and identify
differences between conditions.
Review article
changes and can be used to inform GRN inference. The resulting GRNs Supplementary Box 1). The multimodal data used for GRN inference can
provide valuable insights into the complex processes involved in key be paired if both measurements come from the same cell or unpaired if
fate decisions. LEAP53 and SINCERITIES54 are examples of GRN inference they come from different cells. Some methods do not require match-
methods that leverage pseudotime ordering to infer the directionality ing chromatin accessibility and gene expression profiles for each cell,
between genes in the GRNs. The use of contrast-level statistics obtained as they either summarize read-outs across groups of cells or build
after differential testing55,56 is an effective means of identifying differ- GRNs independently for each modality followed by a merging step.
ences between conditions, such as between healthy individuals and a By contrast, other methods model both modalities in the same cell
cohort of patients with disease. This strategy differs from computing simultaneously. In these ‘simultaneous’ methods, unpaired data can
differences between GRNs, as explained in the later section describing still be modelled if both modalities are matched using integration
‘Downstream GRN analyses’. approaches61. To facilitate usage, some of these methods (for example,
Recent advances in single-cell chromatin accessibility profiling DeepMAPS62, FigR63, GLUE64, scAI65 and SOMatic66) implement their
(such as single-cell ATAC-seq (scATAC-seq))57, which can be carried own integration approach.
out together with single-cell transcriptomics26–28, have allowed for Multimodal GRN inference methods use an extended framework
the refinement of GRN reconstruction at an unparalleled definition. to that used by single-modality methods to reconstruct GRNs. Spe-
Some early works inferred GRNs from unpaired multi-omics data to cifically, they predict gene expression from TF gene expression, they
study human myeloid cell differentiation58, mouse embryonic devel- assign TFs to accessible CREs using binding motif information and they
opment59 and HIV infection of dendritic cells60. However, they did not associate CREs with target genes constrained by genomic distance
provide their method implemented as a tool for others to use. These (Fig. 2). For the prediction of TF binding events, different methods
were followed by an explosion of novel methods for GRN inference use different, highly heterogeneous TF binding motif databases and
that leverage both scRNA-seq and scATAC-seq (Table 1 and Fig. 2; see prediction algorithms (Table 1 and Box 1). As TF binding motif databases
Preprocessing and integration
of both data modalities
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 742
slleC
slleC
Preprocessing and normalization Prediction of gene expression
of gene expression data from TF gene expression
TF 1 TF N
Gene ~ + … +
Cells ~
Assignment of TFs to CREs
using binding motif information
Generation of TF–CRE–gene
triplets
Preprocessing and peak calling Association of CREs to genes
of chromatin accesability data based on genomic distance
Peak regions
Accessibility
atad
scimotpircsnarT
atad
scimo-itluM
atad
ytilibissecca
nitamorhC
Infered GRN
Genes Peak regions
Expression Accessibility
slleC
Genes
Expression
TF
Gene CRE
Maximum distance
Gene CRE
Fig. 2 | Flow chart of methods for gene regulatory network inference. information about the openness of cis-regulatory elements (CREs) across
Methods for gene regulatory network (GRN) inference involve different steps samples or cells. CREs are associated with genes based on genomic distance
depending on the data modalities generated for the samples or cells being limits, and TFs are predicted to bind to CREs using TF binding motif databases
studied. Transcriptomics data are first preprocessed and normalized to build and motif matcher algorithms. Together, this information is used to obtain
a gene expression matrix, containing the transcript levels of each gene across TF–CRE–gene triplets. Finally, these interactions are simplified into TF–gene
samples or cells. A list of known transcription factor (TF) genes is obtained from pairs and aggregated into a GRN. When samples are profiled by both tran-
other sources to distinguish genes with regulatory capabilities. Interactions scriptomics and chromatin accessibility (multi-omics data), preprocessing
between TFs and target genes are then inferred by building models that try to of each modality is carried out and, if needed, the unpaired modalities are
predict the observed gene expression from TF transcript abundance, generating integrated. Having both modalities available, methods can simultaneously
TF–gene associations. Finally, the obtained interactions are aggregated and leverage the three aforementioned modelling steps to build TF–CRE–gene
represented as a GRN. Chromatin accessibility data are first preprocessed triplets, which then are simplified and aggregated into a GRN.
and peaks are called to build a peak accessibility matrix, containing binary
Review article
have different coverage of TFs, and prediction algorithms model bind-
ing differently, results between GRN inference methods might differ Box 1
even if they use similar modelling strategies. The majority of methods
allow for using different TF binding motif databases than their default,
Binding motif databases and
but most methods fix the motif matcher algorithm used — except for
SCENIC+67, which implements three algorithms, cisTarget67, DEM67 and motif matcher algorithms
HOMER68. In addition, GRN inference methods use different genomic
distance cutoffs to assign open chromatin regions to target genes.
Some consider close distances up to 10 kb, others medium distances Generating genome-wide binding data for multiple transcription
up to 100 kb, others large distal effects up to 1,000 kb and others do factors (TFs) requires laborious experiments, so methods for gene
not specify the distance cutoff either in the original publication or in regulatory network (GRN) inference instead predict TF binding
the source code (Table 1). Given that functionally validated interactions events on open genomic regions based on prior information. This
are greatly enriched at the closest distances, and that they substantially information comes from a large collection of TF–DNA binding
fall off by 100 kb1,69, differences in distance cutoffs will likely affect the assays, such as chromatin immunoprecipitation followed by
resulting inferred GRN. sequencing (ChIP-seq) experiments36, that can be used to extract the
After carrying out the above steps (Fig. 2), multimodal GRN infer- most likely genomic sequence to which a given TF specifically binds,
ence methods generate a candidate scaffold network made up of tri- commonly known as a TF binding motif208. Several databases have
plets of a TF associated with a CRE that is linked to a target gene. To collected such assays and generated TF binding motif collections
generate a final GRN structure, different mathematical strategies are for model organisms. Because coverage between databases may
used. Some of these strategies assume a linear relationship between vary, they can be merged to increase the number of TFs considered
TFs, CREs and genes, and others assume a non-linear relationship in the GRN inference process. Moreover, several computational
(Table 1). Linear modelling assumes that one variable, for example algorithms have been developed that leverage TF binding motifs
gene transcripts, changes in direct proportion to another variable, to predict binding events, known as motif matcher algorithms. All
for example TF transcripts or CRE openness. By contrast, non-linear of these algorithms are based on computing the probability of a TF
modelling can accommodate more complex interactions between binding event from the motif sequence and filtering the significant
variables such as synergistic effects70. Although it is widely acknowl- ones. Because the different methods model TF binding differently,
edged that gene expression is a non-linear process70, linear modelling results may vary between them and should be considered during
of GRNs is often preferred owing to its simplicity in formulation and GRN inference. The table lists the TF binding motif databases and
interpretation. Independently of the modelling strategy used, the motif matcher algorithms used across the reviewed methods.
significance of the obtained regulatory interactions can be assessed
using either frequentist or Bayesian probability statistical frameworks Name URL Refs.
(Table 1). A frequentist approach defines the probability of an event Binding motif databases
as the proportion of times that the event occurs in a large number of
CIS-BP http://cisbp.ccbr.utoronto.ca/ 209
identical experiments, whereas Bayesian probability defines it as a
measure of confidence in the occurrence of the said event based on cisTarget https://resources.aertslab.org/cistarget/ 67
databases databases/
both observed data and previous information. Bayesian methods can
take into account available prior knowledge but they usually require ENCODE https://www.encodeproject.org/software/ 210
encode-motifs/
larger computational resources than frequentist approaches, which
can be a limitation when inferring genome-wide GRNs with large-scale HOCOMOCO https://hocomoco11.autosome.org/ 211
single-cell data. In addition, the success of Bayesian inference depends JASPAR https://jaspar.genereg.net/ 212
on the quality of the prior knowledge used. Therefore, when no prior TRANSFAC https://genexplain.com/transfac/ 213
information is available or it is suspected to be inaccurate, frequentist
UniPROBE http://thebrain.bwh.harvard.edu/uniprobe/ 214
inference might be more accurate.
Multimodal GRN inference methods can be grouped based on Motif matcher algorithms
the combination of their modelling strategy and the types of input FIMO https://snystrom.github.io/memes-manual/ 215
they accept (Table 1). The majority of methods are designed to GimmeMotifs https://gimmemotifs.readthedocs.io/ 216
model GRNs across distinct groups, usually cell types, by frequentist
HOMER http://homer.ucsd.edu/homer/motif/ 68
regression. FigR63 and GRaNIE71, among others, use frequentist lin-
ear regression; DIRECT-NET72 and SCENIC+67 use frequentist non-linear MOODs (as https://github.com/jhkorhonen/MOODS 217,
implemented in https://github.com/GreenleafLab/ 218
regression (random forest); and PECA73 and Symphony74,75 use Bayes-
motifmatchr) motifmatchr
ian modelling. By contrast, CellOracle76, Inferelator 3.0 (ref. 77) and
motifanalysis (as https://reg-gen.readthedocs.io/ 219
Pando78 offer multiple modelling strategies to the user. In case no
implemented in
distinct groups can be defined from the data owing to its continu- reg-hint)
ous nature, for example in cell development, scMEGA79 and IReNA80
PIQ toolkit https://bitbucket.org/thashim/piq-single/ 220
leverage trajectories to infer GRNs linearly and non-linearly, respec- src/master/
tively. Also, Dictys81, scMTNI82 and TimeReg83 use a combination of
PWMScan https://ccg.epfl.ch/pwmtools/pwmscan.php 221
both cell type grouping and trajectory data to inform the GRN model-
ling, whereas CellOracle76 and SCENIC+67 use the latter to carry out pycisTarget https://pycistarget.readthedocs.io/ 67
downstream analyses. ANANSE84, sc-compReg85 and SCENIC+67 build
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 743
Review article
Table 1 | Existing tools for inference of gene regulatory networks from multi-omics data
Toola Possible Type of Type of Type of Statistical Default motif Default upstream/ Language Refs.
inputs multimodal data modelling interactions framework database/motif downstream
matcher distance cutoffs
ANANSE Groups, Unpaired Linear Weighted Frequentist CIS-BP/ 100 kb/100 kb Python 84
contrasts GimmeMotifs
CellOracle Groups, Unpaired Linear Signed, Frequentist CIS-BP/ 500 kb/500 kb Python 76
trajectories weighted or Bayesian GimmeMotifs
DC3 Groups Unpaired Linear Binary Frequentist Undefined/ Based on Hi-C Python 88
HOMER
DeepMAPS Groups Paired or Linear Weighted Frequentist JASPAR/ 150 kb/150 kb or Python 62
integrated PWMScan exon
Dictys Groups, Unpaired/paired Linear Signed, Frequentist HOCOMOCO/ 500 kb/500 kb Python 81
trajectories or integrated weighted HOMER
DIRECT-NET Groups Paired or Non-linear Binary Frequentist JASPAR/MOODs 250 kb/250 kb R 72
integrated
FigR Groups Paired or Linear Signed, Frequentist CIS-BP/MOODs 50 kb/50 kb R 63
integrated weighted
GLUE Groups Paired or Non-linear Weighted Frequentist JASPAR/cisTarget 150 kb/150 kb Python 64
integrated
GRaNIE Groups Paired or Linear Weighted Frequentist JASPAR, 250 kb/250 kb R 71
integrated HOCOMOCO/
PWMscan
Inferelator Groups Unpaired Linear Signed, Frequentist CIS-BP, ENCODE, 10 kb/10 kb Python 203
2.5 weighted or Bayesian TRANSFAC/FIMO
Inferelator Groups Unpaired Linear or Weighted Frequentist JASPAR/FIMO 50 kb/2.5 kb Python 77
3.0 non-linear or Bayesian
IReNA Trajectories Unpaired Linear Signed, Frequentist TRANSFAC/FIMO 250 kb/250 kb R 80
weighted
MAGICAL Groups, Unpaired Non-linear Weighted Bayesian CIS-BP, ENCODE/ Based on Hi-C R/MATLAB 166
contrasts MOODs
MICA Groups Unpaired Non-linear Signed, Frequentist HOCOMOCO, Nearest R 204
weighted JASPAR/ transcription start
motifanalysis site
Pando Groups Paired or Linear or Signed, Frequentist JASPAR, CIS-BP/ 100 kb/gene body R 78
integrated non-linear weighted or Bayesian MOODs
PECA Groups Paired or Linear Weighted Bayesian JASPAR, 1,000 kb/1,000 kb MATLAB 73
integrated TRANSFAC,
UniPROBE/
HOMER
Regulatory Groups Paired or Linear Signed Frequentist HOCOMOCO/ 5 kb/5 kb MATLAB 205
Motifs integrated motifanalysis
RENIN Groups Paired or Linear Signed, Frequentist CIS-BP/MOODs 500 kb/500 kb R 206
integrated weighted
scAI Groups Paired or Linear Weighted Frequentist CIS-BP/MOODs 250 kb/250 kb R 65
integrated
sc-compReg Groups, Unpaired Linear Binary Frequentist Undefined/ Undefined R 85
contrasts undefined
SCENIC+ Groups, Paired or Linear Signed, Frequentist cisTarget/ 150 kb/150 kb Python 67
contrasts, integrated weighted cisTarget
trajectories
scMEGA Trajectories Paired or Linear Weighted Frequentist JASPAR/MOODs 250 kb/250 kb R 79
integrated
scMTNI Groups, Unpaired Linear or Weighted Bayesian CIS-BP/PIQ 5 kb/5 kb C++ 82
trajectories non-linear
SOMatic Groups Unpaired Linear Binary Frequentist HOCOMOCO 50 kb/50 kb C++ 66
FIMO
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 744
Review article
Table 1 (continued) | Existing tools for inference of gene regulatory networks from multi-omics data
Toola Possible Type of Type of Type of Statistical Default motif Default upstream/ Language Refs.
inputs multimodal data modelling interactions framework database/motif downstream
matcher distance cutoffs
Symphony Groups Unpaired Linear Signed, Bayesian Undefined/FIMO Nearest Python 74,75
weighted transcription start
site
TimeReg Groups, Paired or Linear Binary Frequentist Undefined/ Undefined MATLAB 83
trajectories integrated HOMER
TRIPOD Groups Paired or Non-linear Signed, Frequentist HOCOMOCO, 100 kb/100 kb R 207
integrated weighted or Bayesian JASPAR/MOODs
aFurther detail regarding these tools and their methodologies is provided in Supplementary Box 1.
group-specific (for example, cell type-specific) GRNs but can also Topic modelling strategies such as latent Dirichlet allocation92, an
leverage gene contrast statistics during the inference process. unsupervised Bayesian model that was originally developed for natural
language processing, allow for generating dense, low-dimensional
Downstream GRN analyses representations that filter noise in the structure of the GRN, and
Once GRNs have been inferred from any resolution and combination thus capture more robustly the differences in regulatory relation-
of omics data, they can be queried using various downstream analyses ships. This strategy has been useful for predicting the survival of
to provide novel biological insights (Fig. 3 and Box 2). patients with cancer93 and for identifying rewiring events in human
haematopoiesis82.
Topological analysis
Although GRNs are simple and interpretable models of gene regula- Inference of TF activities
tion, they can still contain large numbers of genes and an even larger GRNs can be coupled with enrichment methods to infer TF activi-
number of interactions between them. Network centrality measures can ties from transcriptomics data15,50,94,95. This approach allows for the
help identify which TFs or genes are more important for the connec- observed gene expression to be integrated with the GRN topology to
tivity or the information flow of the network (Fig. 3a). Some examples extract which TFs might have relevant roles in certain contexts (Fig. 3c).
of network centrality measures include degree centrality, closeness Common enrichment methods include GSEA96, AUCell50 and VIPER94,
centrality, betweenness centrality and eigenvector centrality. These among others95. In bulk studies, inference of TF activities through
measures have been useful to identify TFs that drive cell fate changes enrichment methods has enabled, for example, the identification of
in diverse biological contexts, such as direct lineage reprograming76, druggable oncoproteins94, stratification of cell lines in response to drug
human myocardial infarction86 and mouse development87. treatment97 and identification of a master regulator as a metastasis pro-
Another approach to characterize the topology of GRNs is using moter in breast carcinoma98. In single-cell studies, enrichment methods
methods based on spectral graph theory, which explore the proper- have identified a novel mechanism of immunotherapy resistance in
ties of a network when represented as a matrix. For example, non- human T cells99, regulators and inducers of oligodendroglioma50, and
negative matrix factorization applied to the adjacency matrices of potential druggable targets for pathological fibroblasts in patients with
GRNs has identified groups of TFs that cooperatively drive lineage tran- COVID-19 (ref. 100). These methods have also been recently applied to
sitions in mouse embryonic stem cells83,88. Similarly, clustering of GRN spatially resolved transcriptomics data, for example to suggest regula-
topology identified known regulators in human haematopoietic cell tors involved in the functional transition of cardiomyocytes across the
differentiation70 and in the response of macrophages to interferon-γ71. border zone that surrounds ischaemic lesions in human myocardial
The gene regulatory modules that are obtained can then be enriched infarction86.
for gene sets to characterize their potential biological functions89.
Perturbation and prediction of cell fate
Comparative analysis GRNs can be used to simulate gene expression values over time by
Comparative analysis of GRNs can uncover the rewiring events that propagating TF expression to target genes in an iterative manner. With
drive differences between cell types, cell states, disease states, treat- this framework, in silico perturbations can be carried out by changing
ment approaches and organisms (Fig. 3b). The easiest method for the expression of a candidate TF and then observing how it affects the
comparative analysis involves the pairwise subtraction of TF–gene resulting transcriptome after a given number of iterations (Fig. 3d).
interactions between GRNs. This methodology has identified key Afterwards, the simulated values can be compared with the gene expres-
regulators in subpopulations of B cells in patients with lymphocytic sion of local neighbouring cells to estimate cell identity transition
leukaemia85, groups of TFs for transdifferentiation of fibroblasts to probabilities analogous to RNA velocity analysis101. First introduced
different human cell types84, candidate Alzheimer disease-specific by CellOracle76, this strategy suggested the role of Zfp57 in generating
trans-regulators90 and cell state-specific regulators in human T cells74,75. and maintaining mouse induced endoderm progenitors, which was
It has also been used to assess evolutionary conservation of TF–gene later experimentally validated with in vitro perturbation experiments.
interactions and adaptation of transcriptional regulation across spe- SCENIC+67 used a similar strategy to identify RUNX3 as a potential
cies91. However, owing to the sparse and noisy nature of GRNs, direct driver of melanocytes to mesenchymal melanoma cells, showcasing
comparison of TF–gene interactions is often not sufficiently robust. the ability of GRNs to capture and model complex regulatory events.
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 745
Review article
Experimental assessment of GRNs TF abundance and post-translational modification
The connections predicted by GRN inference methods should be seen The number of transcripts encoding a given TF is a limited proxy of
as hypothetical regulatory interactions that must be assessed by com- its protein abundance, let alone its activity102. To this end, proteom-
plementary information and/or experiments. In this section, we discuss ics technologies can be used to measure the abundance of TFs. Tar-
common practices for this purpose (Fig. 4). geted proteomics at single-cell resolution is still challenging but some
a Topological analysis b Comparative analysis
Hubs Modules
– =
Cell cycle
ATF3 E2F4
Cell type vs
STAT1
Metabolism Immune
response Condition vs
Organism vs
c Inference of TF activity
Single-cell
transcriptomics
UMAP 1
Integration
Spatial with GRN and
transcriptomics Expression enrichment TF activity
methods
Bulk
transcriptomics
d In silico perturbation
Original cell fates Perturbation N times propagation Predicted cell fates
Pseudotime Expression Pseudotime
Perturbation analysis
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 746
2
PAMU
UMAP 1
2
PAMU
Fig. 3 | Applications of gene regulatory networks. a, Topological analysis. or organisms. c, Inference of TF activity. GRNs can be coupled to enrichment
Network centrality measures can be used to identify hubs of transcription factors methods to infer which TFs might be functionally active from transcriptomics
(TFs) or genes within a gene regulatory network (GRN) that are highly connected. data. GRNs inferred from multi-omics data can then be used to infer TF activities
Clustering of nodes based on their connectivity gives rise to sub-network in other contexts, such as independent single-cell, spatial or bulk transcriptomics
modules that can be associated with biological functions. b, Comparative data. d, In silico perturbation experiments. GRNs can be used to simulate
analysis. Comparison of the connectivities in different GRNs by the pairwise perturbation experiments by propagating changes in gene expression through
subtraction of TF–gene interactions between GRNs can provide insight into the the network over short iterations. The obtained simulated gene expression
rewiring of gene regulation between different cell types, individuals, conditions profiles can then be used to infer cell fate decisions.
Review article
Box 2
Successful applications of gene regulatory networks derived from
single-cell multi-omics data
Gene regulatory networks (GRNs) have been used in various contexts • A multimodal atlas of mouse early organogenesis was built
to answer a range of research questions; here, we summarize some by profiling gene expression and chromatin accessibility from
recent examples. individual cells87. The authors developed in silico chromatin
• A multimodal time course of human brain organoids was immunoprecipitation followed by sequencing (ChIP-seq), a
generated using single-cell RNA sequencing (scRNA-seq) and method to predict TF binding sites, and used it to characterize the
single-cell assay for transposase accessible chromatin with GRNs underlying the transition of neuromesodermal progenitors
sequencing (scATAC-seq)78. Using the GRN inference tool Pando, to somitic mesoderm. Using the CellOracle76 framework for in
the authors predicted transcription factor (TF) binding sites and silico predictions, followed by experimental validation, they
inferred a global GRN underlying organoid development. By characterized a role of Brachyury in priming cis-regulatory
making in silico predictions from the GRN followed by a CRISPR- elements (CREs) for differentiation.
based screen, they identified GLI3 as an essential TF for cortical • scRNA-seq and scATAC-seq were carried out on cortical
fate establishment. tissue from patients with Alzheimer disease90. By modelling
• A multimodal atlas of the fly brain was generated using relationships between TFs, CREs and target genes, the authors
scRNA-seq and scATAC-seq, and characterized developmental, identified ZEB1 and MAFB as candidates involved in gene
reprogramming and maturation trajectories222. Using a deep regulation and, potentially, disease progression in neurons
learning model trained on the omics data, the authors inferred and microglia.
cell type-specific TF binding predictions and used this to decode • Inferelator 3.0 (ref. 77) was used to infer GRNs for several CD4+
the regulatory grammar of enhancer architectures that underlie memory T cell populations from mice and the results were
neuronal diversity. benchmarked by curating TF knockout and ChIP-seq data for
• CellOracle was introduced as a mathematical model to carry 42 of the identified TFs223. The authors integrated the obtained
out in silico TF perturbations from GRNs trained using single-cell GRNs with cell–cell communication networks, and functionally
multi-omics data76. In the context of zebrafish development, the validated a regulatory circuit involving IL-6, MAF and CD153 in
authors made systematic predictions of TF knockouts, which T follicular helper cells that is important for antibody-mediated
allowed the identification of new roles for key regulators of early vaccine responses in aged mice.
zebrafish development, including noto and lhx1a.
technologies such as mass spectrometry-based approaches or assays EpiMap111 and UniBind112 implement different strategies to curate the
that use antibody–oligonucleotide conjugates are already available103 data, thus providing more reliable information regarding TF binding
(reviewed elsewhere104). Alternatively, databases such as The Human sites. Another alternative is single-molecule footprinting, a technique
Protein Atlas105,106 can be queried to confirm whether a candidate TF that jointly measures TF binding and nucleosome occupancy at single
has been previously reported to be present at the protein level in a DNA molecule resolution113,114. It allows for checking the state frequency
given tissue or cell type. In addition, post-translational modifications of each genomic region: bound by a TF, unbound but with open chro-
such as phosphorylation, ubiquitylation and methylation can affect TF matin, or unbound and occupied by nucleosomes. The advantage of
localization, stability, activity and interaction with other proteins107. The single-molecule footprinting over ChIP-seq is that it provides a dynamic
most highly studied post-translational modification of TFs is phospho- and quantifiable state of TF binding instead of a binary description.
rylation, which can be informative as to whether a TF is in an inactive GRN inference methods predict that several TFs bind to the same open
or active form108. genomic region, which is in keeping with the knowledge that TFs bind
cooperatively to DNA to induce transcription1,115,116. Another approach
TF binding and cooperativity to assess the obtained GRN is to check whether the network has recov-
GRN inference methods rely on TF binding predictions based on binding ered the cooperative binding of TFs. Technologies such as CAP-SELEX117
motif analysis to assign TFs to open chromatin regions in the genome. enable cooperative interactions between selected TF pairs to be jointly
It is known that this type of prediction produces many false positives as profiled in the presence of DNA. Single-molecule footprinting can
a large number of TF binding motifs have low specificity109. To this end, also be used for this purpose by checking the overlap of footprints.
ChIP-seq36, which as mentioned above measures the binding of TFs to Other approaches include using protein–protein interaction assays118
DNA, can be used to test how many TF binding events were correctly or checking databases of previously annotated interactions119.
predicted by the GRN inference method76. Databases such as ChIP-
Atlas110, EpiMap111 and UniBind112 compile large collections of ChIP-seq Regulatory activity of CREs
experimental data and organize them by organism, tissue and cell CREs can be in three different chromatin states: transcriptionally active,
type, making them valuable resources for analysing GRN predictions. poised or repressive. Many of the reported open chromatin regions
Because not all ChIP-seq peaks represent direct binding events of a TF, might not have a role in gene regulation, thereby increasing the number
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 747
Review article
is based on sustained genomic interactions130,131, if a genomic region is
Cofactors
consistently in close contact with the promoter region of a gene, it may
• Protein–protein interactions regulate the gene. To this end, super-resolution microscopy has also
been used to validate candidate CRE–gene interactions132, although
TFs • (Phospho-)proteomics with less throughput than Hi-C. Perturbation assays such as CRISPR-
based screens coupled with whole-transcriptome analysis allow for
• Binding assays
deleting or activating specific CREs and observing how this changes
(ChIP-seq, CUT&Tag, CAP-SELEX)
gene expression69,133. In addition, databases of expression quantitative
trait loci in human populations can be used to validate distal candidate
CREs • Perturbation assays • Massively parallel reporter assays
• Evolutionary conservation CREs134–136.
• Genome-wide association studies
TF perturbation
• Chromosome conformation
A more direct approach to test whether a TF regulates a particular gene
capture techniques
• Expression quantitative trait loci is to perturb TF expression and see how this affects gene expression.
Genes
• Perturbation assays
Technologies for pooled CRISPR (in)activation screens coupled with
Fig. 4 | Experimental assessment of gene regulatory networks. Although whole-transcriptome read out are already available137–141. The changes in
there is no clear ‘ground truth’ for gene regulation, several experiments and gene expression upon TF perturbation can be used as the ground truth
analyses can be carried out to validate specific aspects of gene regulatory to check how many of the affected genes are identified as target genes
networks (GRNs). Interactions between transcription factors (TFs) can be in the GRN35,95,142. Also, one can see whether the estimated TF activities
queried in protein–protein databases for TFs that share large numbers of
(see previous section on ‘Inference of TF activities’) correspond to
target genes and are assumed to interact. The presence of TF protein can
the perturbation that has been carried out (low or high TF activity for
be confirmed by proteomic assays, and the activation state of TFs can be
knockout or overexpression of the TF, respectively).
assessed in targeted phosphorylation experiments. Links between TFs and
cis-regulatory elements (CREs) can be confirmed by binding assays, such as
Challenges and future directions
chromatin immunoprecipitation followed by sequencing (ChIP-seq), cleavage
The accumulation of omics data sets, particularly single-cell multi-
under targets and tagmentation (CUT&Tag) and CAP-SELEX. Candidate CREs
can be tested for regulatory capability with reporter assays or perturbation omics data, in recent years has enabled a new wave of improved GRN
experiments. Alternatively, functional CREs can be assumed to be evolutionarily inference strategies. An improved understanding of GRNs should pave
conserved or to be enriched in disease-associated loci as identified by genome- the way to use these models not only as means to understand the prin-
wide association studies. Links between CREs and genes can be evaluated ciples of gene regulation but also as tools to drive cell fate decisions for
experimentally by genome conformation assays such as Hi-C or super-resolution cellular engineering, enabling the generation of new cell types with new
microscopy, or by CRISPR-based perturbation experiments. Alternatively, functions and the reprogramming of diseased cells to a healthy pheno-
databases of expression quantitative trait loci may be used. type. The prospects are hugely promising, but many challenges remain
regarding the modelling of GRNs and their use as predictive tools.
Integrating transcription and accessibility
of false positives in GRN predictions. Therefore, experiments must The use of multi-omics, in principle, allows for a better representation
assess whether candidate enhancers affect gene expression. The mas- of gene regulation but also comes with its own challenges. As highly
sively parallel reporter assay120 is a technique that allows to test whether interrelated processes, chromatin accessibility and transcription are
candidate genomic regions can induce gene expression in episomal temporally coordinated. Yet they have profoundly different kinetics
vectors. Another strategy is to carry out pooled CRISPR-based per- and may be temporally shifted. These relationships are often not fully
turbations of candidate CREs followed by RNA sequencing to identify understood and it is typically assumed that paired chromatin acces-
which regions of the genome affect gene expression69,121. In addition, the sibility and transcriptomics data in the same cell at a single time point
ENCODE Consortium has catalogued, using various biochemical assays, are representative of the interplay between both processes143,144. This
more than one million candidate CREs with enhancer-like signatures limitation is compounded in the case of unpaired data if inadequate
that span ~16% of the human genome36,122,123. As functional enhancers integration results in mismatched scATAC-seq and scRNA-seq data that
are evolutionarily conserved124,125, another approach is to check for will mislead the downstream modelling of GRNs145. Novel integration
genomic sequence similarity across different species. When studying strategies, such as that introduced by FigR63, hold the promise to obtain
diseases, CREs in open chromatin regions can be scanned for single- better matching between cells. Among other factors, the temporal
nucleotide polymorphisms (SNPs) that have been previously linked shift between chromatin accessibility and gene expression, as well as
to diseases in genome-wide association studies. If candidate CREs are cooperative effects, gives rise to non-linear relationships. Some of the
enriched for disease-associated SNPs, this suggests that those CREs GRN inference methods that we have discussed use non-linear formula-
are likely to be functional90,126. tions to account for this, but they lose interpretability compared with
linear models, and they often do not explicitly capture the sign of the
Linkage to target genes interaction. For this reason, and for computational scalability, many
Even if an open chromatin region is validated to have regulatory methods still prefer to model gene regulation linearly. To improve the
properties, it is necessary to test which specific genes it affects. Chro- interpretability, SCENIC+67 and IReNA80 first infer regulatory interac-
mosome conformation capture techniques such as Hi-C127–129 allow tions non-linearly using random forests, and then determine the sign
to measure the probability of contact between genomic regions and to of the interaction based on correlation analysis between TF and gene
identify topologically associating domains. Because gene regulation transcripts.
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 748
Review article
Glossary
Assay for transpose- interactions with accessible Gene regulatory networks Peaks
accessible chromatin with DNA regions using transposase (GRNs). Network representations Regions of accessible chromatin
sequencing Tn5-mediated tagmentation followed of molecular interactions between that form the read-out of epigenetic
(ATAC-seq). A technique to identify by DNA sequencing. transcriptional regulators and target sequencing techniques.
accessible DNA regions using genes.
hyperactive Tn5 transposase. Closeness centrality Promoter
A network centrality measure Genome-wide association A regulatory region in the genome
Betweenness centrality describing the average distance (length studies located before the transcriptional start
A network centrality measure represen- of the shortest path) of a node to all Analysis approach to identify site of a gene.
ting the number of appearances of a other nodes. frequently appearing single-nucleotide
node in the shortest path of any other polymorphisms in the genome across a Silencers
two nodes in the network. Degree centrality large cohort of individuals. Distal regulatory DNA regions where
A network centrality measure transcription regulatory proteins can
Chromatin describing the number of edges Hi-C bind and repress transcription.
A higher-order filamentous structure of (degree) of a node. A technique to study chromatin
DNA–protein complex that can exist in a conformation in three dimensions to Single-nucleotide
condensed or uncondensed state. DNA binding sites identify genomic sequences that might polymorphisms
DNA sequences where transcription be distal to each other in linear distance (SNPs). DNA sequence variations
Chromatin immunoprecipita- factors can bind to drive gene but closer in the 3D space. caused by substitution of a single
tion followed by sequencing regulation, usually represented as nucleotide in a specific position.
(ChIP-seq). A technique to analyse nucleotide patterns known as motifs. Metacells
protein interactions with accessible Groups of cells with a similar molecular Topologically associating
DNA regions using chromatin Eigenvector centrality profile that can be aggregated into a domains
immunoprecipitation followed A network centrality measure single omics profile to reduce sparsity Self-interacting genomic regions
by DNA sequencing. describing the importance of a node of the data. with high interaction frequency of
in the network based on the centrality sequences within the domain and
cis-Regulatory elements of its neighbours. Motif matcher algorithms relative isolation from neighbouring
(CREs). Non-coding DNA regions that String matching algorithms to detect regions, forming a 3D chromosome
regulate the transcription of nearby Enhancers transcription factor binding sites in DNA structure.
genes upon binding of transcription Distal regulatory DNA regions where sequences.
factors (TFs). These include promoters, transcription regulatory proteins can Transcription factors
enhancers and silencers. bind and activate transcription. Network centrality (TFs). Proteins that modify the rate of
A group of graph theory metrics that transcription by binding to specific DNA
Expression quantitative trait defines the relative importance of a sequences.
Cleavage under targets and loci node in a network.
tagmentation Genomic locations whose sequence
(CUT&Tag). An antibody-based variation is associated with changes in
technique to analyse protein gene expression.
Scale and sparsity of single-cell data for data obtained by scATAC-seq, and proper filters need to be used to
GRN inference methods require a large number of observations that ensure a minimum quality148,149. For paired multi-omics technologies, a
capture the variability of the biological process being studied. These systematic benchmark comparing their varying coverage and sensitiv-
observations can be individual cells, samples or conditions. Single- ity to their single-omic counterparts is missing150. Although sparsity
cell technologies generate thousands of profiles for a given sample, is a known property of single-cell technologies151,152, none of the GRN
making it easier to infer GRNs in a larger variety of biological contexts inference methods discussed here explicitly accounts for sparsity in its
than for bulk profiling technologies. Nonetheless, cells from the same modelling. Some methods apply data transformations to counteract
sample are not necessarily independent and cannot be considered true this limitation. Imputation methods can be used to reduce the number
biological replicates146. For this reason, the inclusion of different sam- of ‘dropouts’ (caused by under-sampling of mRNAs or accessible DNA
ples might be needed to obtain meaningful GRNs. In addition, current reads)153–155, although it has been shown that they might have detri-
single-cell GRN inference methods build an aggregate network across mental effects on GRN reconstruction156. Strategies that aggregate
a population of cells and do not take into account that cells may come similar cells into pseudo-bulk profiles or metacells146,157,158 have been
from different samples. A candidate approach to address this issue is reported to be beneficial87. Owing to their sparsity, most computational
LIONESS147, which models the contribution of each sample when infer- pipelines treat scATAC-seq data as binary data, assigning regions of the
ring GRNs and can generate sample-specific regulatory interactions. genome that are either accessible or closed for each cell. However,
In addition, single-cell data are by nature sparse and noisy, particularly the true state of DNA accessibility is known to be more refined and can
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 749
Review article
involve regions of intermediate accessibility that fluctuate in a dynamic binding motifs. With the accumulation of high-quality cell atlases from
manner159. Thus, treating chromatin accessibility data as binary might consortium initiatives49,177,178, we envision that these strategies could
be detrimental for downstream analyses160,161, and methods that eventually replace classic TF binding motif predictions. Furthermore,
handle accessibility in a quantitative manner might improve GRN current TF binding predictions are binary but a quantitative definition
reconstruction154,155,162,163. could be more informative. BANC-seq179, a technology that measures
quantitative TF binding affinities, has the potential to generate more
The regulatory role of 3D genome structure accurate GRNs.
Current methods of GRN inference use arbitrary cutoffs based on
genomic distance to assign CREs to genes. The aim of this filtering is Emerging multi-omics for GRN inference
to reduce the search space for each gene, requiring less computational The paired profiling of transcriptomics and chromatin accessibility
resources, and to reduce the number of false positive interactions based data has enabled the potentially more accurate inference of GRNs but
on the fact that most genomic interactions are proximal69. However, is still a costly assay, limiting its widespread use. Newer alternatives
there are some examples of interactions between CREs and genes sepa- such as ISSAAC-seq180 enable multi-omics profiling at a much lower
rated by large distances, such as enhancers of the MYC gene located cost than the commercial 10× Multiome kit. Despite this, it might
almost 2 Mb downstream of it164. Depending on the distance cutoff that be the case that joint scRNA-seq and scATAC-seq data alone do not
is used, GRN inference methods might miss crucial CRE–gene interac- provide enough information to characterize gene regulation fully.
tions. In addition, some interactions occur across chromosomes, as In that case, advances in single-cell multi-omics profiling technolo-
reported during olfactory receptor selection165, which current GRN gies that include more data modalities will be crucial181. Among such
methods are not able to consider. One solution to this problem is to promising technologies is NEAT-seq182, which simultaneously profiles
use technologies based on 3D proximity, such as Hi-C127,129, to assess intra-nuclear proteins, chromatin accessibility and gene expression,
whether a CRE might be regulating a gene. This strategy has been suc- allowing to discard possible false positives in GRN modelling by includ-
cessfully applied by DC3 (ref. 88) and MAGICAL166. Despite some high- ing TF protein abundance. Another example is scChaRM-seq183, which
throughput alternatives167,168, chromosome conformation capture simultaneously profiles DNA methylation, chromatin accessibility
techniques pose new challenges owing to their sparse nature169 and the and gene expression. Their joint profiling allows for TF assignment to
facts that they still require integration with other modalities and their CREs to be fine-tuned according to their methylation status. Moreover,
protocol can be hard to reproduce170,171. Until they become more widely ATAC-STARR-seq184 can carry out massively parallel reporter assay and
available, computational approaches have been used to predict the 3D chromatin accessibility profiling simultaneously to test the transcribing
structure of the genome based on accessibility data such as scATAC-seq capacity of open CREs. Advances in untargeted single-cell proteom-
data172,173. Their use in GRN modelling has the potential to overcome ics and phosphoproteomics may enable the profiling of functionally
the limitations of using distance-based cutoffs. active TFs185. One example is Phospho-seq186, a novel technology that
profiles chromatin accessibility and phosphorylated proteins at the
Refinement of TF binding predictions single-cell level. Genetic information is known to be heterogeneous
The current strategy used by GRN inference methods of assigning TFs among populations of individuals but most methods assume that they
to CREs relies on TF binding motif databases (Box 1). Each database share the same genome187. scGET-seq188, a technology that jointly pro-
has a different coverage of motif collections, which might bias the files the genome and chromatin accessibility, has the potential to aid
resulting predictions. Motif databases are based on data from previ- the inference of causal GRNs by testing how SNPs may affect chromatin
ous binding experiments such as ChIP-seq. However, it is estimated accessibility owing to changes in TF binding affinities.
that there are no available binding data for 10% of the approximately
1,600 sequence-specific TFs encoded in the human genome31,109. TFs Benchmarking of GRNs
without known binding motifs are excluded from GRN modelling, a The benchmarking of GRNs is crucial to understand the accuracy
factor that is exacerbated for non-model organisms as they tend to of novel GRN inference methods, in particular those that leverage
have fewer known TF binding motifs than other more well-studied multi-omics data, which have not yet been evaluated systematically.
organisms. One possible solution to incorporate missing TFs might be Unfortunately, the validation of predicted GRNs is a complicated task
to leverage known protein–protein interactions during GRN inference. as there is no clear ‘ground truth’ for gene regulation. One approach
Moreover, current TF binding motifs are based on data from multiple to benchmarking is to build in silico GRNs that allow us to assess GRN
tissues and cell types. It is known that TF binding is a highly context- reconstruction against a known ground truth34, yet one that might
specific process1, and although the available motifs are still relevant not well reflect true biological GRNs. As mentioned in the previous
for many tissues, cell type-specific motif models might help to increase section, there are different methodologies that can be used to assess
the accuracy of TF binding predictions. Recent computational strate- indirectly the quality of the predicted gene regulation events but
gies based on deep learning allow for cell type-specific TF binding these have certain limitations. Even if TF binding to a gene is observed,
predictions174,175. These models are trained to predict cell type-specific it does not necessarily mean that the TF regulates that gene as TFs
DNA accessibility solely based on DNA sequence. Once trained, they bind stochastically into open regions of DNA and require coopera-
identify which nucleotides are predicted to affect accessibility the tion with other molecules for effective regulation of transcription159.
most through in silico mutagenesis or by using strategies of interpret- Chromosome conformation capture technologies provide contact
able machine learning such as SHAP176. To derive cell type-specific TF information and define topologically associating domains. However,
binding predictions, these methods combine the predicted nucleotide their resolution might not be sufficient to detect certain genomic
quantifications with binding motifs. Although these strategies have the interactions189. High-resolution Hi-C maps exist, such as Micro-C190, but
potential to better contextualize GRN inference, they require pretrained their cost becomes prohibitive when comparing many experimental
models using large amounts of data and are still limited to known TF conditions. To address this, machine learning approaches are being
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 750
Review article
used to impute higher-coverage Hi-C maps from lower-coverage data References
to increase their resolution191. Another possibility is to use super- 1. Kim, S. & Wysocka, J. Deciphering the multi-scale, quantitative cis-regulatory code.
Mol. Cell 83, 373–392 (2023).
resolution microscopy-based alternatives, but their throughput is
This extensive review covers the molecular basis of the cis-regulatory code.
rather limited189. TFs cooperatively drive gene expression but they 2. Zaret, K. S. & Carroll, J. S. Pioneer transcription factors: establishing competence for
do so mainly as a result of DNA-mediated interactions rather than gene expression. Genes Dev. 25, 2227–2241 (2011).
3. Lai, X., Wolkenhauer, O. & Vera, J. Understanding microRNA-mediated gene
protein–protein contacts117. Therefore, the evaluation of TF–TF inter-
regulatory networks through mathematical modelling. Nucleic Acids Res. 44,
actions might be limited to particular cases only. The evaluation of 6019–6035 (2016).
GRNs through the use of perturbation experiments is a more promis- 4. Du, J.-X. et al. Splicing factors: insights into their regulatory network in alternative
splicing in cancer. Cancer Lett. 501, 83–104 (2021).
ing approach owing to its inherent causality. However, perturbation
5. Statello, L., Guo, C.-J., Chen, L.-L. & Huarte, M. Gene regulation by long non-coding
screens are costly, sometimes do not work as expected and may be RNAs and its biological functions. Nat. Rev. Mol. Cell Biol. 22, 96–118 (2021).
hindered by compensatory mechanisms and unaccounted for down- 6. Carthew, R. W. Gene regulation and cellular metabolism: an essential partnership.
Trends Genet. 37, 389–400 (2021).
stream effects. In addition to all of these limitations, as gene regulation 7. Davidson, E. H. & Erwin, D. H. Gene regulatory networks and the evolution of animal body
is a time-dependent process, it might be the case that experiments plans. Science 311, 796–800 (2006).
contradict themselves because they captured a different time frame 8. Su, E. Y., Spangler, A., Bian, Q., Kasamoto, J. Y. & Cahan, P. Reconstruction of dynamic
regulatory networks reveals signaling-induced topology changes associated with germ
or because of experimental noise. Because the generation of a true layer specification. Stem Cell Rep. 17, 427–442 (2022).
‘gold standard’ of gene regulation seems out of reach for the moment, 9. Claringbould, A. & Zaugg, J. B. Enhancers in disease: molecular basis and emerging
treatment strategies. Trends Mol. Med. 27, 1060–1073 (2021).
we are more inclined to use these different assessment strategies as a
10. Jacob, F. & Monod, J. Genetic regulatory mechanisms in the synthesis of proteins.
collection of ‘silver standards’. We envision that a computational tool J. Mol. Biol. 3, 318–356 (1961).
that collects and distributes such information will be useful for the This seminal study delineates a gene regulatory system.
11. Ideker, T., Galitski, T. & Hood, L. A new approach to decoding life: systems biology.
community to carry out quality control on the inferred GRNs and to
Annu. Rev. Genomics Hum. Genet. 2, 343–372 (2001).
benchmark novel GRN inference methods. Platforms such as the Open 12. Davidson, E. H. et al. A genomic regulatory network for development. Science 295,
Problems for Single-Cell Analysis project192 offer a suitable infrastruc- 1669–1678 (2002).
13. Snyder, M. & Gallagher, J. E. G. Systems biology from a yeast omics perspective.
ture to run and evaluate the large variety of GRN inference methods.
FEBS Lett. 583, 3895–3899 (2009).
These would also enable the evaluation of GRN inference methods in 14. Han, H. et al. TRRUST v2: an expanded reference database of human and mouse
an unbiased manner through open competition, as was illustrated transcriptional regulatory interactions. Nucleic Acids Res. 46, D380–D386 (2018).
15. Garcia-Alonso, L., Holland, C. H., Ibrahim, M. M., Turei, D. & Saez-Rodriguez, J. Benchmark
for GRN inference from bulk transcriptomics data by the DREAM
and integration of resources for the estimation of human transcription factor activities.
challenges33. Genome Res. 29, 1363–1375 (2019).
16. Liu, Z.-P., Wu, C., Miao, H. & Wu, H. RegNetwork: an integrated database of transcriptional
and post-transcriptional regulatory networks in human and mouse. Database 2015,
GRNs in the bigger picture
bav095 (2015).
It is important to keep in mind that GRNs are not isolated. The classic 17. Keenan, A. B. et al. ChEA3: transcription factor enrichment analysis by orthogonal omics
example of the lac operon, whereby a metabolite (lactose) triggers integration. Nucleic Acids Res. 47, W212–W224 (2019).
18. Margolin, A. A. et al. ARACNE: an algorithm for the reconstruction of gene regulatory
gene regulation, highlights that GRNs are part of an entangled cellular
networks in a mammalian cellular context. BMC Bioinforma. 7, S7 (2006).
machinery, including signalling and metabolic processes. The addi- 19. Langfelder, P. & Horvath, S. WGCNA: an R package for weighted correlation network
tion of single-cell phosphoproteomics and metabolomics193 opens the analysis. BMC Bioinforma. 9, 559 (2008).
20. Huynh-Thu, V. A., Irrthum, A., Wehenkel, L. & Geurts, P. Inferring regulatory networks
possibility of linking gene regulation to cell signalling processes using
from expression data using tree-based methods. PLoS ONE 5, e12776 (2010).
context-specific network models194. 21. Buenrostro, J. D., Giresi, P. G., Zaba, L. C., Chang, H. Y. & Greenleaf, W. J. Transposition
Furthermore, cells rarely work as autonomous systems, and gene of native chromatin for fast and sensitive epigenomic profiling of open chromatin,
DNA-binding proteins and nucleosome position. Nat. Methods 10, 1213–1218 (2013).
regulation is highly coordinated within tissues. Thus, another promis-
22. Fiers, M. W. E. J. et al. Mapping gene regulatory networks from single-cell omics data.
ing direction will be the integration of multimodal data with spatial Brief. Funct. Genomics 17, 246–254 (2018).
information. In particular, we envision the integration of GRNs with 23. Cha, J. & Lee, I. Single-cell network biology for resolving cellular heterogeneity in human
diseases. Exp. Mol. Med. 52, 1798–1808 (2020).
intracellular and intercellular communication processes195–197 into 24. Klein, A. M. et al. Droplet barcoding for single-cell transcriptomics applied to embryonic
spatially aware models198,199. These strategies can help in understanding stem cells. Cell 161, 1187–1201 (2015).
multicellular regulatory processes in time and space200. 25. Macosko, E. Z. et al. Highly parallel genome-wide expression profiling of individual cells
using nanoliter droplets. Cell 161, 1202–1214 (2015).
26. Chen, S., Lake, B. B. & Zhang, K. High-throughput sequencing of the transcriptome
Conclusions and chromatin accessibility in the same cell. Nat. Biotechnol. 37, 1452–1457 (2019).
Advances in high-throughput, single-cell multimodal technologies 27. Liu, L. et al. Deconvolution of single-cell multi-omics layers reveals regulatory
heterogeneity. Nat. Commun. 10, 470 (2019).
together with computational methods are paving the way to increas- 28. Ma, S. et al. Chromatin potential identified by shared single-cell profiling of RNA and
ingly accurate GRN inference models. The large scale of the data sets chromatin. Cell 183, 1103–1116.e20 (2020).
29. Mercatelli, D., Scalambra, L., Triboli, L., Ray, F. & Giorgi, F. M. Gene regulatory network
makes it increasingly possible to train deep learning methods to predict
inference resources: a practical overview. Biochim. Biophys. Acta Gene Regul. Mech.
gene expression from sequencing data175,201,202. GRNs complement 1863, 194430 (2020).
these approaches by giving a more interpretable model. Together, 30. Moerman, T. et al. GRNBoost2 and Arboreto: efficient and scalable inference of gene
regulatory networks. Bioinformatics 35, 2159–2161 (2019).
these different approaches might help us to better understand dif-
31. Lambert, S. A. et al. The human transcription factors. Cell 175, 598–599 (2018).
ferences in gene regulation across cell types, organs, populations 32. Holland, C. H. et al. Robustness and applicability of transcription factor and pathway
and species, and serve as tools to control cell fate decisions. In the analysis tools on single-cell RNA-seq data. Genome Biol. 21, 36 (2020).
33. Marbach, D. et al. Wisdom of crowds for robust gene network inference. Nat. Methods 9,
biomedical field, such knowledge could enable the identification
796–804 (2012).
of novel drug targets that control pathophysiological processes This work is a crowdsourced benchmark for GRN inference from bulk transcriptomics
in different diseases. data.
34. Pratapa, A., Jalihal, A. P., Law, J. N., Bharadwaj, A. & Murali, T. M. Benchmarking
algorithms for gene regulatory network inference from single-cell transcriptomic data.
Published online: 26 June 2023 Nat. Methods 17, 147–154 (2020).
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 751
Review article
35. McCalla, S. G. et al. Identifying strengths and weaknesses of methods for computational 67. González-Blas, C. B. et al. SCENIC+: single-cell multiomic inference of enhancers and
network inference from single-cell RNA-seq data. G3 3, jkad004 (2023). gene regulatory networks. Preprint at bioRxiv https://doi.org/10.1101/2022.08.19.504505
36. Johnson, D. S., Mortazavi, A., Myers, R. M. & Wold, B. Genome-wide mapping of in vivo (2022).
protein–DNA interactions. Science 316, 1497–1502 (2007). This study presents a large, curated collection of TF binding motifs and introduces a
37. Kaya-Okur, H. S. et al. CUT&Tag for efficient epigenomic profiling of small samples and novel GRN inference method.
single cells. Nat. Commun. 10, 1930 (2019). 68. Heinz, S. et al. Simple combinations of lineage-determining transcription factors prime
38. Lee, T. I. et al. Transcriptional regulatory networks in Saccharomyces cerevisiae. Science cis-regulatory elements required for macrophage and B cell identities. Mol. Cell 38,
298, 799–804 (2002). 576–589 (2010).
39. Grosselin, K. et al. High-throughput single-cell ChIP-seq identifies heterogeneity 69. Gasperini, M. et al. A genome-wide framework for mapping gene regulation via cellular
of chromatin states in breast cancer. Nat. Genet. 51, 1060–1066 (2019). genetic screens. Cell 176, 1516 (2019).
40. Bartosovic, M., Kabbe, M. & Castelo-Branco, G. Single-cell CUT&Tag profiles histone 70. Zuin, J. et al. Nonlinear control of transcription through enhancer–promoter interactions.
modifications and transcription factors in complex tissues. Nat. Biotechnol. 39, 825–835 Nature 604, 571–577 (2022).
(2021). 71. Kamal, A. et al. GRaNIE and GRaNPA: inference and evaluation of enhancer-mediated
41. Bartosovic, M. & Castelo-Branco, G. Multimodal chromatin profiling using nanobody- gene regulatory networks. Mol. Syst. Biol. https://doi.org/10.15252/msb.202311627
based single-cell CUT&Tag. Nat. Biotechnol. https://doi.org/10.1038/s41587-022-01535-4 (2023).
(2022). 72. Zhang, L., Zhang, J. & Nie, Q. DIRECT-NET: an efficient method to discover cis-regulatory
42. Qin, J., Hu, Y., Xu, F., Yalamanchili, H. K. & Wang, J. Inferring gene regulatory networks elements and construct regulatory networks from single-cell multiomics data. Sci. Adv.
by integrating ChIP-seq/chip and transcriptome data via LASSO-type regularization 8, eabl7393 (2022).
methods. Methods 67, 294–303 (2014). 73. Duren, Z., Chen, X., Jiang, R., Wang, Y. & Wong, W. H. Modeling gene regulation from
43. Boyle, A. P. et al. High-resolution mapping and characterization of open chromatin paired expression and chromatin accessibility data. Proc. Natl Acad. Sci. USA 114,
across the genome. Cell 132, 311–322 (2008). E4914–E4923 (2017).
44. Kelly, T. K. et al. Genome-wide mapping of nucleosome positioning and DNA methylation 74. Burdziak, C., Azizi, E., Prabhakaran, S. & Pe’er, D. A nonparametric multi-view model for
within individual DNA molecules. Genome Res. 22, 2497–2506 (2012). estimating cell type-specific gene regulatory networks. Preprint at arXiv https://doi.org/
45. Minnoye, L. et al. Chromatin accessibility profiling methods. Nat. Rev. Methods Prim. 1, 10.48550/arXiv.1902.08138 (2019).
1–24 (2021). 75. Bachireddy, P. et al. Mapping the evolution of T cell states during response and
46. Pranzatelli, T. J. F., Michael, D. G. & Chiorini, J. A. ATAC2GRN: optimized ATAC-seq and resistance to adoptive cellular therapy. Cell Rep. 37, 109992 (2021).
DNase1-seq pipelines for rapid and accurate genome regulatory network inference. 76. Kamimoto, K. et al. Dissecting cell identity via network inference and in silico gene
BMC Genom. 19, 563 (2018). perturbation. Nature 614, 742–751 (2023).
47. Qin, Q. et al. Lisa: inferring transcriptional regulators through integrative modeling This work presents a novel GRN inference method from scRNA-seq and scATAC-seq
of public chromatin accessibility and ChIP-seq data. Genome Biol. 21, 32 (2020). data that also introduces an in silico TF perturbation strategy.
48. Sonawane, A. R., DeMeo, D. L., Quackenbush, J. & Glass, K. Constructing gene regulatory 77. Skok Gibbs, C. et al. High-performance single-cell gene regulatory network inference at
networks using epigenetic data. NPJ Syst. Biol. Appl. 7, 45 (2021). scale: the Inferelator 3.0. Bioinformatics 38, 2519–2528 (2022).
49. Tabula Sapiens Consortium et al. The Tabula Sapiens: a multiple-organ, single-cell 78. Fleck, J. S. et al. Inferring and perturbing cell fate regulomes in human brain organoids.
transcriptomic atlas of humans. Science 376, eabl4896 (2022). Nature https://doi.org/10.1038/s41586-022-05279-8 (2022).
50. Aibar, S. et al. SCENIC: single-cell regulatory network inference and clustering. 79. Li, Z., Nagai, J. S., Kuppe, C., Kramann, R. & Costa, I. G. scMEGA: single-cell multi-omic
Nat. Methods 14, 1083–1086 (2017). enhancer-based gene regulatory network inference. Bioinform. Adv. 3, vbad003 (2023).
This work presents the first bespoke method to infer GRNs at the single-cell level, 80. Jiang, J. et al. IReNA: integrated regulatory network analysis of single-cell transcriptomes
introducing the use of TF binding motif information for the estimation of GRNs. and chromatin accessibility profiles. iScience 25, 105359 (2022).
51. Herring, C. A., Chen, B., McKinley, E. T. & Lau, K. S. Single-cell computational strategies 81. Wang, L. et al. Dictys: dynamic gene regulatory network dissects developmental
for lineage reconstruction in tissue systems. Cell Mol. Gastroenterol. Hepatol. 5, 539–548 continuum with single-cell multi-omics. Preprint at bioRxiv https://doi.org/10.1101/
(2018). 2022.09.14.508036 (2022).
52. Wagner, A., Regev, A. & Yosef, N. Revealing the vectors of cellular identity with single-cell 82. Zhang, S. et al. Inference of cell type-specific gene regulatory networks on cell lineages
genomics. Nat. Biotechnol. 34, 1145–1160 (2016). from single cell omic datasets. Nat. Commun. 14, 3064 (2023).
53. Specht, A. T. & Li, J. LEAP: constructing gene co-expression networks for single-cell 83. Duren, Z., Chen, X., Xin, J., Wang, Y. & Wong, W. H. Time course regulatory analysis
RNA-sequencing data using pseudotime ordering. Bioinformatics 33, 764–766 (2017). based on paired expression and chromatin accessibility data. Genome Res. 30, 622–634
54. Papili Gao, N., Ud-Dean, S. M. M., Gandrillon, O. & Gunawan, R. SINCERITIES: inferring (2020).
gene regulatory networks from time-stamped single cell transcriptional expression 84. Xu, Q. et al. ANANSE: an enhancer network-based computational approach for
profiles. Bioinformatics 34, 258–266 (2018). predicting key transcription factors in cell fate determination. Nucleic Acids Res. 49,
55. Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold change and dispersion 7966–7985 (2021).
for RNA-seq data with DESeq2. Genome Biol. 15, 550 (2014). 85. Duren, Z. et al. sc-compReg enables the comparison of gene regulatory networks
56. Ritchie, M. E. et al. limma powers differential expression analyses for RNA-sequencing between conditions using single-cell data. Nat. Commun. 12, 4763 (2021).
and microarray studies. Nucleic Acids Res. 43, e47 (2015). 86. Kuppe, C. et al. Spatial multi-omic map of human myocardial infarction. Nature 608,
57. Buenrostro, J. D. et al. Single-cell chromatin accessibility reveals principles of regulatory 766–777 (2022).
variation. Nature 523, 486–490 (2015). 87. Argelaguet, R. et al. Decoding gene regulation in the mouse embryo using single-cell
This paper introduces single-cell assay for transpose-accessible chromatin (scATAC) multi-omics. Preprint at bioRxiv https://doi.org/10.1101/2022.06.15.496239 (2022).
technology. 88. Zeng, W. et al. DC3 is a method for deconvolution and coupled clustering from bulk
58. Ramirez, R. N. et al. Dynamic gene regulatory networks of human myeloid differentiation. and single-cell genomics data. Nat. Commun. 10, 4613 (2019).
Cell Syst. 4, 416–429.e3 (2017). 89. Liberzon, A. et al. The molecular signatures database (MSigDB) hallmark gene set
59. Starks, R. R., Biswas, A., Jain, A. & Tuteja, G. Combined analysis of dissimilar promoter collection. Cell Syst. 1, 417–425 (2015).
accessibility and gene expression profiles identifies tissue-specific genes and actively 90. Anderson, A. G. et al. Single nucleus multiomics identifies ZEB1 and MAFB as candidate
repressed networks. Epigenetics Chromatin 12, 16 (2019). regulators of Alzheimer’s disease-specific cis-regulatory elements. Cell Genomics 3,
60. Johnson, J. S. et al. A comprehensive map of the monocyte-derived dendritic cell 100263 (2023).
transcriptional network engaged upon innate sensing of HIV. Cell Rep. 30, 914–931.e9 91. Thompson, D., Regev, A. & Roy, S. Comparative analysis of gene regulatory networks:
(2020). from network reconstruction to evolution. Annu. Rev. Cell Dev. Biol. 31, 399–428 (2015).
61. Argelaguet, R., Cuomo, A. S. E., Stegle, O. & Marioni, J. C. Computational principles and 92. Pritchard, J. K., Stephens, M. & Donnelly, P. Inference of population structure using
challenges in single-cell data integration. Nat. Biotechnol. 39, 1202–1215 (2021). multilocus genotype data. Genetics 155, 945–959 (2000).
62. Ma, A. et al. Single-cell biological network inference using a heterogeneous graph 93. Lou, S. et al. TopicNet: a framework for measuring transcriptional regulatory network
transformer. Nat. Commun. 14, 964 (2023). change. Bioinformatics 36, i474–i481 (2020).
63. Kartha, V. K. et al. Functional inference of gene regulation using single-cell multi-omics. 94. Alvarez, M. J. et al. Functional characterization of somatic mutations in cancer using
Cell Genom. 2, 100166 (2022). network-based inference of protein activity. Nat. Genet. 48, 838–847 (2016).
This paper introduces FigR, which has a novel integration strategy for scRNA-seq and 95. Badia-i-Mompel, P. et al. decoupleR: ensemble of computational methods to infer
scATAC-seq data that can enhance GRN inference. biological activities from omics data. Bioinforma. Adv. 2, vbac016 (2022).
64. Cao, Z.-J. & Gao, G. Multi-omics single-cell data integration and regulatory inference with 96. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-based approach
graph-linked embedding. Nat. Biotechnol. 40, 1458–1466 (2022). for interpreting genome-wide expression profiles. Proc. Natl Acad. Sci. USA 102,
65. Jin, S., Zhang, L. & Nie, Q. scAI: an unsupervised approach for the integrative analysis 15545–15550 (2005).
of parallel single-cell transcriptomic and epigenomic profiles. Genome Biol. 21, 25 97. Garcia-Alonso, L. et al. Transcription factor activities enhance markers of drug sensitivity
(2020). in cancer. Cancer Res. 78, 769–780 (2018).
66. Jansen, C. et al. Building gene regulatory networks from scATAC-seq and scRNA-seq 98. Walsh, L. A. et al. An integrated systems biology approach identifies TRIM25 as a key
using linked self organizing maps. PLoS Comput. Biol. 15, e1006555 (2019). determinant of breast cancer metastasis. Cell Rep. 20, 1623–1640 (2017).
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 752
Review article
99. Guan, X. et al. Androgen receptor activity in T cells limits checkpoint blockade efficacy. 138. Datlinger, P. et al. Pooled CRISPR screening with single-cell transcriptome readout.
Nature 606, 791–796 (2022). Nat. Methods 14, 297–301 (2017).
100. Melms, J. C. et al. A molecular single-cell lung atlas of lethal COVID-19. Nature 595, 139. Schraivogel, D. et al. Targeted Perturb-seq enables genome-scale genetic screens in
114–119 (2021). single cells. Nat. Methods 17, 629–635 (2020).
101. La Manno, G. et al. RNA velocity of single cells. Nature 560, 494–498 (2018). 140. Ng, A. H. M. et al. A comprehensive library of human transcription factors for cell fate
102. de Sousa Abreu, R., Penalva, L. O., Marcotte, E. M. & Vogel, C. Global signatures of engineering. Nat. Biotechnol. 39, 510–519 (2021).
protein and mRNA expression levels. Mol. Biosyst. 5, 1512–1526 (2009). 141. Joung, J. et al. A transcription factor atlas of directed differentiation. Cell 186,
103. Chung, H. et al. Joint single-cell measurements of nuclear proteins and RNA in vivo. 209–229.e26 (2023).
Nat. Methods 18, 1204–1212 (2021). 142. Littman, R., Wang, N., Peng, C. & Yang, X. SCING: single cell integrative gene regulatory
104. Bennett, H. M., Stephenson, W., Rose, C. M. & Darmanis, S. Single-cell proteomics network inference elucidates robust, interpretable gene regulatory networks. Preprint at
enabled by next-generation sequencing or mass spectrometry. Nat. Methods 20, bioRxiv https://doi.org/10.1101/2022.09.07.506959 (2022).
363–374 (2023). 143. Yurkovsky, E. & Nachman, I. Event timing at the single-cell level. Brief. Funct. Genomics
105. Uhlén, M. et al. A human protein atlas for normal and cancer tissues based on antibody 12, 90–98 (2013).
proteomics. Mol. Cell. Proteom. 4, 1920–1932 (2005). 144. Co, A. D., Lagomarsino, M. C., Caselle, M. & Osella, M. Stochastic timing in gene
106. Uhlén, M. et al. Proteomics. Tissue-based map of the human proteome. Science 347, expression for simple regulatory strategies. Nucleic Acids Res. 45, 1069–1078 (2017).
1260419 (2015). 145. Lee, M. Y. Y., Kaestner, K. H. & Li, M. Benchmarking algorithms for joint integration of
107. Weidemüller, P., Kholmatov, M., Petsalaki, E. & Zaugg, J. B. Transcription factors: bridge unpaired and paired single-cell RNA-seq and ATAC-seq data. Preprint at bioRxiv
between cell signaling and gene regulation. Proteomics 21, e2000034 (2021). https://doi.org/10.1101/2023.02.01.526609 (2023).
108. Sousa, A. et al. Pan-cancer landscape of protein activities identifies drivers of signalling 146. Squair, J. W. et al. Confronting false discoveries in single-cell differential expression.
dysregulation and patient survival. Mol. Syst. Biol. 19, e10631 (2023). Nat. Commun. 12, 5692 (2021).
109. Inukai, S., Kock, K. H. & Bulyk, M. L. Transcription factor–DNA binding: beyond binding 147. Kuijjer, M. L., Tung, M. G., Yuan, G., Quackenbush, J. & Glass, K. Estimating sample-
site motifs. Curr. Opin. Genet. Dev. 43, 110–119 (2017). specific regulatory networks. iScience 14, 226–240 (2019).
110. Oki, S. et al. ChIP-Atlas: a data-mining suite powered by full integration of public 148. Luecken, M. D. & Theis, F. J. Current best practices in single-cell RNA-seq analysis:
ChIP-seq data. EMBO Rep. 19, e46255 (2018). a tutorial. Mol. Syst. Biol. 15, e8746 (2019).
111. Boix, C. A., James, B. T., Park, Y. P., Meuleman, W. & Kellis, M. Regulatory genomic circuitry 149. Yan, F., Powell, D. R., Curtis, D. J. & Wong, N. C. From reads to insight: a hitchhiker’s guide
of human disease loci by integrative epigenomics. Nature 590, 300–307 (2021). to ATAC-seq data analysis. Genome Biol. 21, 22 (2020).
112. Puig, R. R., Boddie, P., Khan, A., Castro-Mondragon, J. A. & Mathelier, A. UniBind: maps 150. Vandereyken, K., Sifrim, A., Thienpont, B. & Voet, T. Methods and applications for single-
of high-confidence direct TF–DNA interactions across nine species. BMC Genom. 22, cell and spatial multi-omics. Nat. Rev. Genet. https://doi.org/10.1038/s41576-023-00580-2
482 (2021). (2023).
113. Krebs, A. R. et al. Genome-wide single-molecule footprinting reveals high RNA 151. Blencowe, M. et al. Network modeling of single-cell omics data: challenges,
polymerase II turnover at paused promoters. Mol. Cell 67, 411–422.e4 (2017). opportunities, and progresses. Emerg. Top. Life Sci. 3, 379–398 (2019).
114. Sönmezer, C. et al. Molecular co-occupancy identifies transcription factor binding 152. Lähnemann, D. et al. Eleven grand challenges in single-cell data science. Genome Biol.
cooperativity in vivo. Mol. Cell 81, 255–267.e6 (2021). 21, 31 (2020).
115. Gasperini, M., Tome, J. M. & Shendure, J. Towards a comprehensive catalogue of 153. van Dijk, D. et al. Recovering gene interactions from single-cell data using data diffusion.
validated and target-linked human enhancers. Nat. Rev. Genet. 21, 292–310 (2020). Cell 174, 716–729.e27 (2018).
116. Ibarra, I. L. et al. Mechanistic insights into transcription factor cooperativity and its 154. Bravo González-Blas, C. et al. cisTopic: cis-regulatory topic modeling on single-cell
impact on protein–phenotype interactions. Nat. Commun. 11, 124 (2020). ATAC-seq data. Nat. Methods 16, 397–400 (2019).
117. Jolma, A. et al. DNA-dependent formation of transcription factor pairs alters their binding 155. Li, Z. et al. Chromatin-accessibility estimation from single-cell ATAC-seq data with
specificity. Nature 527, 384–388 (2015). scOpen. Nat. Commun. 12, 6386 (2021).
118. Lu, H. et al. Recent advances in the development of protein–protein interactions 156. Ly, L.-H. & Vingron, M. Effect of imputation on gene network reconstruction from
modulators: mechanisms and clinical trials. Signal. Transduct. Target. Ther. 5, 1–23 (2020). single-cell RNA-seq data. Patterns 3, 100414 (2022).
119. Orchard, S. et al. The MIntAct project—IntAct as a common curation platform for 11 157. Baran, Y. et al. MetaCell: analysis of single-cell RNA-seq data using K–nn graph partitions.
molecular interaction databases. Nucleic Acids Res. 42, D358–D363 (2014). Genome Biol. 20, 206 (2019).
120. Patwardhan, R. P. et al. High-resolution analysis of DNA regulatory elements by synthetic 158. Persad, S. et al. SEACells infers transcriptional and epigenomic cellular states from single-cell
saturation mutagenesis. Nat. Biotechnol. 27, 1173–1175 (2009). genomics data. Nat. Biotechnol. https://doi.org/10.1038/s41587-023-01716-9 (2023).
121. Ren, X. et al. Parallel characterization of cis-regulatory elements for multiple genes using 159. Klemm, S. L., Shipony, Z. & Greenleaf, W. J. Chromatin accessibility and the regulatory
CRISPRpath. Sci. Adv. 7, eabi4360 (2021). epigenome. Nat. Rev. Genet. 20, 207–220 (2019).
122. ENCODE Project Consortium. The ENCODE (ENCyclopedia Of DNA Elements) Project. 160. Miao, Z. & Kim, J. Is single nucleus ATAC-seq accessibility a qualitative or quantitative
Science 306, 636–640 (2004). measurement? Preprint at bioRxiv https://doi.org/10.1101/2022.04.20.488960 (2022).
123. Thurman, R. E. et al. The accessible chromatin landscape of the human genome. Nature 161. Martens, L. D., Fischer, D. S., Theis, F. J. & Gagneur, J. Modeling fragment counts
489, 75–82 (2012). improves single-cell ATAC-seq analysis. Preprint at bioRxiv https://doi.org/10.1101/
124. Hardison, R. C., Oeltjen, J. & Miller, W. Long human–mouse sequence alignments reveal 2022.05.04.490536 (2022).
novel regulatory elements: a reason to sequence the mouse genome. Genome Res. 7, 162. Stuart, T., Srivastava, A., Madad, S., Lareau, C. A. & Satija, R. Single-cell chromatin state
959–966 (1997). analysis with Signac. Nat. Methods 18, 1333–1341 (2021).
125. Pennacchio, L. A. et al. In vivo enhancer analysis of human conserved non-coding 163. Granja, J. M. et al. ArchR is a scalable software package for integrative single-cell
sequences. Nature 444, 499–502 (2006). chromatin accessibility analysis. Nat. Genet. 53, 403–411 (2021).
126. Wang, S. K. et al. Single-cell multiome of the human retina and deep learning nominate 164. Bahr, C. et al. Author Correction: a Myc enhancer cluster regulates normal and leukaemic
causal variants in complex eye diseases. Cell Genom. 2, 100164 (2022). haematopoietic stem cell hierarchies. Nature 558, E4 (2018).
127. Lieberman-Aiden, E. et al. Comprehensive mapping of long-range interactions reveals 165. Monahan, K., Horta, A. & Lomvardas, S. LHX2- and LDB1-mediated trans interactions
folding principles of the human genome. Science 326, 289–293 (2009). regulate olfactory receptor choice. Nature 565, 448–453 (2019).
128. Mumbach, M. R. et al. HiChIP: efficient and sensitive analysis of protein-directed genome 166. Chen, X. et al. Mapping disease regulatory circuits at cell-type resolution from single-cell
architecture. Nat. Methods 13, 919–922 (2016). multiomics data. Preprint at medRxiv https://doi.org/10.1101/2022.12.06.22282077 (2022).
129. Ramani, V. et al. Massively multiplex single-cell Hi-C. Nat. Methods 14, 263–266 (2017). 167. Stevens, T. J. et al. 3D structures of individual mammalian genomes studied by single-cell
130. Dixon, J. R. et al. Chromatin architecture reorganization during stem cell differentiation. Hi-C. Nature 544, 59–64 (2017).
Nature 518, 331–336 (2015). 168. Flyamer, I. M. et al. Single-nucleus Hi-C reveals unique chromatin reorganization at
131. Chen, H. et al. Dynamic interplay between enhancer–promoter topology and gene oocyte-to-zygote transition. Nature 544, 110–114 (2017).
activity. Nat. Genet. 50, 1296–1303 (2018). 169. Zhang, R., Zhou, T. & Ma, J. Multiscale and integrative single-cell Hi-C analysis with
132. Fukaya, T., Lim, B. & Levine, M. Enhancer control of transcriptional bursting. Cell 166, Higashi. Nat. Biotechnol. 40, 254–261 (2022).
358–368 (2016). 170. Yu, M. & Ren, B. The three-dimensional organization of mammalian genomes. Annu. Rev.
133. Xie, S., Duan, J., Li, B., Zhou, P. & Hon, G. C. Multiplexed engineering and analysis of Cell Dev. Biol. 33, 265–289 (2017).
combinatorial enhancer activity in single cells. Mol. Cell 66, 285–299.e5 (2017). 171. Marti-Renom, M. A. et al. Challenges and guidelines toward 4D nucleome data and
134. GTEx Consortium et al. Genetic effects on gene expression across human tissues. Nature model standards. Nat. Genet. 50, 1352–1358 (2018).
550, 204–213 (2017). 172. Rossini, R., Kumar, V., Mathelier, A., Rognes, T. & Paulsen, J. MoDLE: high-performance
135. van der Wijst, M. G. P. et al. Single-cell RNA sequencing identifies celltype-specific stochastic modeling of DNA loop extrusion interactions. Genome Biol. 23, 247 (2022).
cis-eQTLs and co-expression QTLs. Nat. Genet. 50, 493–497 (2018). 173. Tan, J. et al. Cell-type-specific prediction of 3D chromatin organization enables
136. Kerimov, N. et al. A compendium of uniformly processed human gene expression and high-throughput in silico genetic screening. Nat. Biotechnol. https://doi.org/10.1038/
splicing quantitative trait loci. Nat. Genet. 53, 1290–1299 (2021). s41587-022-01612-8 (2023).
137. Dixit, A. et al. Perturb-Seq: dissecting molecular circuits with scalable single-cell RNA This work demonstrates that the prediction of Hi-C data from chromatin accessibility
profiling of pooled genetic screens. Cell 167, 1853–1866.e17 (2016). is a promising strategy to replace the use of genomic distance thresholds.
Nature Reviews Genetics | Volume 24 | November 2023 | 739–754 753
