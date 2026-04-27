---
source_path: /mnt/c/Users/Administrator/Zotero/storage/FEBCHPCW/Aivazidis 等 - 2023 - Model-based inference of RNA velocity modules improves cell fate prediction.pdf
ingested: 2026-04-23
sha256: a0d5b4f8ad774baf
---

bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
Model-based inference of RNA velocity modules improves cell fate
prediction
Alexander Aivazidis1, Fani Memi1, Vitalii Kleshchevnikov1, Brian Clarke2, Oliver Stegle2,3,1,*,
Omer Ali Bayraktar1,*
1 Wellcome Sanger Institute, Cambridge, CB10 1SA, UK
2 Division of Computational Genomics and Systems Genetics, German Cancer Research
Center (DKFZ), Heidelberg 69120, Germany
3 European Molecular Biology Laboratory, Genome Biology Unit, Heidelberg 69117,
Germany
*Correspondence:
Email: oliver.stegle@embl.de and ob5@sanger.ac.uk
Abstract
RNA velocity is a powerful paradigm that exploits the temporal information contained in spliced
and unspliced RNA counts to infer transcriptional dynamics. Existing velocity models either
rely on coarse biophysical simplifications or require extensive numerical approximations to
solve the underlying differential equations. This results in loss of accuracy in challenging
settings, such as complex or weak transcription rate changes across cellular trajectories. Here,
we present cell2fate, a formulation of RNA velocity based on a linearization of the velocity
ODE, which allows solving a biophysically accurate model in a fully Bayesian fashion. As a
result, cell2fate decomposes the RNA velocity solutions into modules, which provides a new
biophysical connection between RNA velocity and statistical dimensionality reduction. We
comprehensively benchmark cell2fate in real-world settings, demonstrating enhanced
interpretability and increased power to reconstruct complex dynamics and weak dynamical
signals in rare and mature cell types. Finally, we apply cell2fate to a newly generated dataset
from the developing human brain, where we spatially map RNA velocity modules onto the
tissue architecture, thereby connecting the spatial organisation of tissues with temporal
dynamics of transcription.
Introduction
The concept of "RNA velocity", which involves inferring transcriptional dynamics from
spliced and unspliced counts in single-cell RNA sequencing (scRNA-seq), has displayed
significant potential1–3. The first implementations of RNA velocity models1–3 have undergone
an evolution of conceptual and technical refinements, including improved parameter
inference4–6, as well as the use of numerical approaches5,7,8,9 to allow for solving the underlying
differential equations. However, these existing refinements are bound to trade-offs between
either introducing coarse biophysical approximations1–4,6,10,11 or relying on extensive numerical
approximations5,7–9. Hence, the fundamental challenge remains to define a mathematically
1
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
sound framework that allows for capturing unconstrained transcriptional dynamics while
retaining computational and numerical tractability.
To address the aforementioned limitations, we present cell2fate - a fully Bayesian
model of RNA velocity based on a realistic biophysical model of complex transcription
dynamics. Cell2fate employs a linearization to decompose complex differential equations into
tractable components that can be solved analytically. By doing so, the model is at the same
time expressive, interpretable and computationally efficient. The approach to decompose the
velocity problem into components also provides a new connection between RNA velocity and
dimensionality reduction using a biophysical solution.
We assess and benchmark cell2fate in the context of real-world settings,
demonstrating its ability to capture complex dynamics and weak dynamical signals in rare and
mature cell types. Finally, we show how cell2fate can be combined with spatial
transcriptomics, thereby connecting transcriptional dynamics to their spatial tissue
environment.
Results
The cell2fate model
Cell2fate builds on a long-stranding history of computational methods for RNA velocity,
which employ a dynamical model to explain variation in spliced and unspliced read counts for
individual genes and cells (Fig. 1a). At the core of cell2fate is a reformulation of the RNA
velocity problem that gives rise to an analytically tractable solution for cell-specific transcription
rates. This is achieved by linearizing the corresponding ODE for each gene into a set of M
components with simpler dynamics. The dynamics of each module is defined by a switch on/off
time, T /T on a cell specific time-scale T , as well as corresponding rates λ /λ and
m,on m,off c m,on m,off
a gene loading parameter, A (Fig. 1b, top right). The linearized solution allows for estimating
mg
modules at the level of transcription rates, RNA velocities and observed counts (Fig. 1c, d).
The linearization also provides a biophysical connection between RNA velocity and
statistical dimensionality reduction. This connection becomes apparent when casting the
linearization as a mixed membership model, whereby spliced and unspliced counts of each
gene are governed by a linear combination of M modules (Methods, Fig. 1b). The mixing
coefficients can then be interpreted analogous to gene loadings of factor analysis or principal
component analysis.
The cell2fate model directly operates on the raw cell-level counts as input, and it
includes a series of refinements to account for technical sources of variation, including
overdispersion, variation in detection sensitivity of spliced and unspliced RNA molecules,
ambient RNA and known batches (Methods). Parameter inference is conducted in a fully
Bayesian manner, which allows for encoding assumptions on sparsity using hierarchical
priors, regularising the effective number of active modules, as well as sharing of evidence
strength across genes, cells and modules (Methods). The model is implemented in Pyro and
builds on scvi-tools to facilitate its use in existing workflows. The software comes with
guidelines and heuristics to determine hyperparameters such as the number of modules
(Methods).
2
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
Figure 1: cell2fate model overview. Cell2fate allows to infer complex and subtle
transcriptional dynamics by modelling gene-specific transcription rates using a smaller number
of independent modules with simple dynamics.
3
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
A, Left: cell2fate input data, comprising raw UMI counts of unspliced and spliced RNA for
individual cells and genes; Middle: cell2fate infers time and RNA velocity by modelling gene-
specific transcription rates using a small number of modules that explain co-regulated
programs; Right: downstream use cases of cell2fate.
B, Representation of cell2fate as mixed membership generative model. Transcription rates of
individual genes (left) are modelled as a weighted combination of prototypical transcription
rates of a small number of M modules (right). Each module is defined by a switch on (T )
m,on
and off (T ) time and corresponding rates (λ , λ ) that determine the speed of activation
m,off m,on m,off
and deactivation.
C, Example application of cell2fate to a mouse dentate gyrus dataset covering differentiation
of intermediate progenitor cells into neurons and radial glia cells into astrocytes. Left: Overall
RNA velocity graph from all modules projected onto a UMAP plot; Arrows denote the total rate
of change of RNA across cells. Right: RNA velocity graph of individual modules. Grey box:
Time assignment of individual lineages, with the neuron lineages occupying low time points
and the astrocyte lineage high time points.
D, Expected mRNA counts (left) from the cell2fate model, derived as the sum of the analytical
solutions of differential equations for each module (right).
Improved cell fate predictions and estimation of complex of transcription rates
Next, to compare cell2fate to existing RNA velocity methods, we assessed the
consistency of estimated cell fate trajectories with prior knowledge. Briefly, we considered the
cross-boundary direction correctness (CBDir) metric for benchmarking, thereby scoring the
consistency of transition probabilities at the boundary between cell clusters with prior
knowledge3.
We considered 10 RNA velocity methods spanning different model classes, and
approaches for parameter inference (Methods). We applied each method to five scRNA-seq
datasets, including widely-used benchmark datasets such as the developing mouse dentate
gyrus12 and pancreas13. In order to assess the ability to resolve complex transcriptional
dynamics, we additionally examined mouse erythroid maturation14 and human bone marrow15,
two datasets that feature multiple transcriptional boosts across cellular trajectories11. Finally,
we considered a mouse bone marrow dataset with markedly low UMI counts1, thereby
assessing the ability of models to cope with low coverage data.
On average, across all five datasets, cell2fate achieved the best overall performance
(Fig. 2a, results on individual datasets shown in Supp. Fig. 1-13). More importantly, cell2fate
inferred the correct directionality of cell fate transitions in all datasets, whereas all other
methods except for pyroVelocity_model2 inferred a reverse order dynamics in at least one
benchmark setting (corresponding to negative CBDir values). Inspecting the benchmarking
results, we could attribute the performance of cell2fate to overcoming two major challenges
as elaborated below.
First, cell2fate provides sufficient statistical power to identify correct velocity flows from
subtle transcriptional dynamics. For example, in the mouse dentate gyrus dataset, other
methods consistently failed to resolve the late maturation trajectory of granule neurons and
incorrectly suggested that mature cells transitioned into their immature counterparts (Fig. 2b,
blue inset boxes, Supp. Fig. 12). Furthermore, alternative methods struggled with rare cell
populations such as oligodendrocyte precursors (OPCs) maturing into oligodendrocytes (Fig.
2b, red inset boxes).
4
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
Second, cell2fate correctly reconstructs complex transcriptional dynamics. In the
mouse erythroid maturation and human bone marrow datasets, the model resolved the correct
cell trajectories, whereas other models tended to perform poorly (Fig. 2c, Supp. Fig. 13).
Previous analysis14, based on the visual inspection of spliced and unspliced counts across
manually annotated cell clusters, has provided evidence that mouse erythroid lineage
formation features many “multi-rate kinetic” genes such as Hba-x and Nudt4 that display
coordinated changes in transcription rates across the cell maturation trajectory14. Consistently,
cell2fate recapitulated these step-wise transcriptional rate boosts in these multi-rate kinetic
genes14 (Fig. 2d, turquoise line). In contrast, other methods, such as pyroVelocity_model2 can
only predict a single non-zero transcription rate, due to their simpler underlying dynamical
model (Fig. 2d, green line). Taken together, these results demonstrate the ability of cell2fate
to capture complex cell trajectories and subtle transcriptional dynamics.
We also note that cell2fate provides two additional model outputs that help to provide
deeper insights compared to existing RNA velocity methods. First, cell2fate infers a cell-
specific time-scale3,5,6 (c.f. Fig. 1a,b), which aids the identification of cell lineage progression
and distinct cell lineages. For example, in the mouse dentate gyrus dataset, granule neurons
and astrocytes are assigned markedly disconnected timepoints, with oligodendrocytes
occupying a mid-timepoint range (Fig. 2e, left), consistent with the distinct lineage origins of
these three cell types12. In contrast, in the mouse erythroid maturation dataset, a single lineage
with a single connected time range is identified (Fig. 2e, right).
Second, cell2fate yields Bayesian posterior uncertainty estimates for all parameters,
including the time estimate of each cell4–6. This provides a principled measure of confidence
in the RNA velocity values across and within datasets. In both datasets mentioned above, the
coefficient of variation (CV) of the posterior distribution of individual cell times was consistently
close to zero, indicating low uncertainty (Fig. 2e, bottom). In contrast, cell2fate applied to a
steady state dataset of peripheral blood mononuclear cells (PBMCs)16, where no
transcriptional dynamics is expected11, yields confidence estimates with a CV close to 1,
indicating high uncertainty (Fig. 2f). Hence, the CV of posterior cell times can serve as quality
control to assess whether cell2fate identifies meaningful dynamics in a given dataset.
Taken together, our benchmark demonstrates cell2fate’s enhanced statistical power
to estimate cell trajectories and resolve complex transcriptional dynamics, and the ability to
quantify uncertainty in velocity estimates.
5
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
Figure 2: Enhanced performance of cell2fate in RNA Velocity benchmark of 10 methods
across 5 datasets.
A, Performance of 10 methods to reconstruct known trajectories on 5 datasets. Shown is the
cross boundary direction correctness3 with large positive values corresponding to correct
6
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
lineage reconstructions; negative values corresponding to opposite directionality. Cell2fate
yields the best overall performance across all datasets.
B-D, Examples of the solutions obtained from selected models and datasets, considering
datasets that harbour specific challenges, including (B) weak signals in mature or rare cell
types and (C,D) complex transcription rate dynamics.
D, Transcription rate as inferred by pyroVelocity_model2 and cell2fate for two selected genes
that have been postulated to have stepwise changes in transcription rates across
differentiation14.
E, Cell-specific time estimates from cell2fate separates different lineages into disconnected
time ranges: left, Astrocytes having much higher time than the neuron lineage in the dentate
gyrus example; right:, Erythroid Maturation dataset, revealing one connected time range
indicating a single lineage.
F, Coefficient of variation (CV) of the cell2fate cell-specific posterior time can be used as a
measure of uncertainty to assess the suitability of a dataset for cell2fate analysis. In a steady
state dataset of PBMCs this CV is close to 1 throughout.
RNA velocity modules reveal fine stages of late cell maturation
cell2fate modules are sequentially activated gene expression programs over time.
Given their biophysical foundations in transcriptional kinetics, we expected that RNA velocity
modules can provide a more granular characterisation of dynamic processes during cellular
differentiation compared to conventional dimensionality reduction techniques that lack a
mechanistic basis, such as matrix factorization or clustering. In addition, cell2fate comes with
a suite of downstream analysis and visualisation tools, enabling users to explore dynamic
processes and derive biological insights.
To demonstrate the cell2fate toolkit, we considered the mouse brain single cell dataset
included as part of the benchmarking study (c.f. Fig. 2b), profiling the dentate gyrus region in
the hippocampus across two developmental stages12. In addition to early differentiation of
neurons and astrocytes from neural progenitors, this dataset covers late maturation trajectory
of granule neurons (i.e. the late differentiation after the immature neuron stage), a critical
process that is however not well understood, and more generally it is unknown whether this
late maturation process unfolds across successive transcriptional stages. Previous RNA
velocity methods applied to this dataset2,3 were able to distinguish neuronal versus astrocyte
lineage trajectories, however the correct trajectory for the most mature granule neurons could
not be resolved (Fig. 2b).
Cell2fate applied to this dataset revealed 16 distinct RNA velocity modules (Supp. Fig.
2), capturing all the expected cell trajectories, with the dominant lineage corresponding to
granule neuron differentiation and maturation stemming from neural intermediate progenitor
cells (nIPCs), neuroblasts and immature neurons, while radial glial-like progenitor cells are
largely committed to astrocytes (Fig. 3a). We also observed that mossy cells, another neuronal
population in the dentate gyrus, were assigned to the middle stages of the granule neuron
trajectory. While mossy cells are thought to have different lineage origins, their transcriptional
development is highly similar to that of granule neurons17.
To explore the dynamics of neuronal differentiation in greater depth, we used the fitted
cell2fate model to estimate the total spliced transcript abundance for each of the 9 granule
neuron lineage modules in individual cells across the inferred time (Fig. 3b, top panel). This
analysis identified the successive induction of modules across the early differentiation of radial
7
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
glia into nIPCs, neuroblasts and immature neurons (modules #1 to 3). Strikingly, cell2fate also
recovered dynamics in mature granule neurons, explained by six modules (modules #4 to 9)
that are sequentially activated and temporally overlap across mature granule neurons, thereby
finely dissecting the late maturation of these cells into distinct transcriptional windows (Fig.
3b). The model also correctly identified a temporal gap between immature and mature granule
neurons (Fig. 3b), which is consistent with prior expectations12. The cell2fate visualisation tool
complements t-SNE or UMAP by providing dynamic insights anchored on estimated
differentiation time, and it can also visualise additional metadata such as cell type annotations
or developmental age (Fig. 3b, bottom 2 sidebars).
The total spliced count estimates can also be used to visualise the dynamics of RNA
velocity modules across cells, e.g. on a conventional UMAP plot (Fig. 3c). The activation of
different modules per cell can be inspected similar to the factor activity in conventional matrix
factorization. We also compared these module activation estimates to conventional factor
analysis and clustering methods. Briefly, Multi-Omics Factor Analysis (MOFA)18 yielded
factors that captured complementary sources of variation, with activity profiles that were
temporally more diffuse across the differentiation trajectory. Specifically, these factors did not
stratify late granule neuron maturation (Fig. 3c, Supp. Fig. 15). We also observed overall low
correlation between cell2fate module and MOFA factor gene loadings, particularly for the late
neuronal maturation modules 4 to 9 (Supp. Fig. 16). Similarly, Leiden clustering of the scRNA-
seq dataset at different resolutions identified clusters that were not aligned with the neuronal
maturation (Fig. 3c, Supp. Fig. 17). Collectively, these observations indicate that cell2fate
captures complementary aspects of variation compared to existing decomposition methods
and is well suited to conduct granular dissection of granule neuron maturation.
Beyond the activity of modules, the dynamics can be further classified into states within
each cell, based on whether they are increasing or decreasing in expression (Fig. 3d,
Methods). Both quantities are shown in Figure 3e-f for granule neuron differentiation. The
additional dynamic information in this visualisation shows for example that module 9 has not
reached a steady state, implying that granule neuron maturation continues beyond the time
range captured in this dataset.
Finally, we examined to what extent RNA velocity modules can provide deeper insights
into the late stages of granule neuron differentiation. We ranked genes by how much of their
transcription rate is explained by each module and utilised top genes as “module markers”
(Fig. 3g and Supp. Fig. 14). We identified Rmb24, Fam19a1, Sptb (Module 4) and Palm2,
Pdzd2, Usp19 (Module 5) as markers switched on in immature granule neurons (Fig. 3g, Supp.
Fig. 14). In contrast, Fst, Rapgef5, Moxd1 (Module 6), Prr16, Kdm5d, Rpa3 (Module 7) and
Rgs2, Nudt13, 1700048O20Rik (Module 8) provide novel markers of late granule neuron
maturation stages (Fig. 3g, Supp. Fig. 14). Fam19a1 has been reported to suppress neural
stem cell maintenance and promote differentiation19,20, consistent with its expression pattern
in maturing granule neurons. Rgs2 is dynamically expressed during neuronal activity21 and
involved in synaptic plasticity22, consistent with its late induction in module 8. Apart from these
two genes, the marker genes reported here have not been functionally investigated in granule
neurons or brain development to our knowledge.
Additionally, we can extract top module marker genes that are transcription factors as
“module TFs” (Fig. 3h). Moving on to such module TFs, Zmat4 (Module 6) and Tfam (Module
8) are enriched in late granule neuron maturation stages (Fig. 3h). Zmat4 has been reported
as upregulated in the auditory cortex of young P7 mice compared to adults23, while Tfam
knockouts result in immature neuronal phenotypes24. Yet their roles in granule neuron
differentiation have not been studied to date. We also find that genes with putative promoter
8
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
sequences that are most likely to be bound by the top 20 module TFs, as predicted by the
ProBound algorithm25, are more frequently among the top 300 module genes, than those least
likely to be bound by those TFs (Supp. Fig. 18). These TFs provide putative candidate
regulators of late granule neuron differentiation.
Taken together, our results demonstrate the great interpretability and statistical power
of cell2fate’s module decomposition for single-cell RNA-seq datasets to finely dissect cellular
processes and suggest that late granule neuron maturation is composed of distinct stages.
9
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
Figure 3: Module decomposition of cell2fate resolves final stages of granule neuron
maturation.
A, cell2fate velocity graph embedding for dentate gyrus data, reproduced from figure 2b for
clarity.
10
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
B, Activation of selected example cell2fate module, weight of selected MOFA18 (Multi-Omics
Factor Analysis) factor and Leiden clustering (with resolution parameter set to 1) for
comparison. Overall factor weights and Leiden clusters are more diffusely distributed and less
associated with the differentiation trajectory.
C, Spliced counts abundance caused by selected modules over time.
D, Module state definitions. < 5% of steady state counts is OFF, >95% is ON. Intermediate
values correspond to Induction if T_c < T_mOFF and repression if T_c > T_mOFF.
E, Activation, defined as the spliced counts produced by a module in each cell.
F, State of late granule neuron maturation modules.
G, Module marker genes, defined as having a large part of their transcription rate explained
by this module.
H, Module TF genes, defined as module marker genes that are also known transcription
factors.
Spatial mapping of RNA velocity modules
Temporal biological processes are often spatially organised in tissues. For example,
cell differentiation and migration are often coupled, with cells associating with distinct spatial
signalling microenvironments throughout their differentiation trajectories. Here, we sought to
link the temporal information captured by cell2fate to spatial tissue organisation by mapping
RNA velocity modules in a newly generated spatial transcriptomics dataset of human brain
development (Fig. 4a).
We focused on the developing human cerebral cortex where excitatory neuron
maturation follows a highly stereotyped trajectory through space and time26. Neural
progenitors termed radial glia and intermediate progenitors reside in the cortical germinal
zones, where they sequentially give rise to distinct neuronal subtypes that subsequently
migrate out to the deep and upper layers of the cortical plate across their maturation (Fig. 4b).
Deep layer residing neurons (DLn) are born before upper layer neurons (ULn) in early
gestation, hence DLn are relatively more mature than ULn by mid-gestation (Fig. 4b). Thus,
the maturation state and spatial location of cortical excitatory neurons are tightly linked.
To examine cellular differentiation trajectories in the human cortex, we initially
performed snRNA-seq profiling (10X v3.0) of one donor at mid-gestation. We then followed
standard snRNA-seq processing workflows (Methods) to cluster cells and annotated cell types
using markers from literature27. We annotated distinct neural progenitors (radial glial and
intermediate progenitor cells) as well as excitatory neuron populations at different stages of
maturation (Fig. 4c). As expected, mature neurons expressed DLn markers, whereas newborn
and immature neurons showed enriched expression of ULn markers (Supp. Fig. 19). We also
annotated inhibitory neurons and glial cell types but excluded them from the subsequent
excitatory neuron trajectory analysis.
We then applied cell2fate to this human brain snRNA-seq dataset and observed the
expected excitatory neuronal differentiation trajectory from neural progenitors to newborn,
immature and mature neurons (Fig. 4c). The RNA velocity modules dissected the neuronal
trajectory into finer-grained maturation stages, identifying 7 sequentially activated and
temporally overlapping modules throughout immature and mature neurons (Fig. 4d, Supp. Fig.
20). While these modules contained some DLn and ULn cell type markers, they also included
many genes that are widely expressed across all excitatory neurons in the adult human
11
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
cortex28, such as PSMC3, KRR1 and BMPER (Supp. Fig. 24). This suggests that the modules
partially identify a neuronal maturation trajectory common to both DLn and ULn.
In contrast to cell2fate, other RNA velocity methods such as scVelo were not able to
accurately identify velocity flow in mature neurons (Supp. Fig. 22). Additionally, the integrated
measurement model of cell2fate allowed us to factor in different detection probabilities for
spliced and unspliced counts and correct batch effects in our human brain snRNA-seq dataset
(Supp. Fig. 21), which is crucial for estimating true transcriptional dynamics from observed
counts (Methods).
To spatially map our RNA velocity modules in the developing human cortex, we
performed Visium spatial RNA-seq profiling (10X CytAssist) of one cortical tissue section from
an age matched donor (Fig. 4b). As the Visium assay offers a coarse spatial resolution and
profiles multiple cells at each tissue location (i.e. Visium spot), we used the cell2location
algorithm29 to deconvolve the abundance of RNA velocity modules across spatial data. We
used the steady-state expression counts of each module as reference gene expression
signatures, then applied the standard cell2location workflow to infer the abundance of each
module signature across Visium spots (Fig. 4a, Methods).
The RNA velocity modules showed expected patterns of spatial mapping across the
human cortex (Fig. 4e,f). Progenitor modules spatially mapped to germinal zones (Fig. 4e)
while neuronal modules primarily mapped to the cortical plate (Fig, 4e). The fine spatial
locations of neuronal modules were consistent with their maturation state (Fig. 4e,f). The
immature ULn module (#0) mapped to the upper cortical layers as well as the
subplate/intermediate zone that immature neurons pass through during their migration to the
cortical plate30. The early-mature ULn modules (#1, 2) were exclusively mapped to the upper
cortical layers. In contrast, the mature and late mature DLn modules (#4,5) specifically
mapped to deep cortical layers.
Taken together, our approach provides a new workflow to spatially resolve complex
cell trajectories through tissues.
12
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
Figure 4: cell2fate interfaces with cell2location to spatially map the cortical
neurogenesis process in human brain development
13
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
A, Workflow for spatial mapping of cell2fate modules. Cell2fate is used to infer modules in
scRNAseq data. Steady-state expression of modules is supplied as reference profiles for
cell2location to infer abundance of modules across spatial locations.
B, (left) Illustration of experimental setup: Single-nucleus (10X v3.0) and spatial
transcriptomics (10X CytAssist), were performed on cortical tissue sections from two age-
matched (13 post-conception week) donors
(middle) Illustration of known temporal lineage progression in human cortex: radial glia cells
(green) and intermediate progenitors (violet) first give rise to deep layer neurons (blue) early
in mid-gestation. They then switch to produce upper layer neurons (yellow) later in mid-
gestation, at which point deep layer neurons have matured further.
(right) Illustration of known spatial lineage progression in human cortex: progenitors (green,
violet) are located deeper inside the cortex, where they produce newborn neurons (yellow),
which differentiate and migrate towards the outside, where they form the cortical plate (yellow,
blue).
C, cell2fate velocity graph UMAP embedding for human brain data shows the expected
trajectory from radial glia to mature excitatory neurons
D, Spliced counts produced by each cell2fate module over inferred time illustrate the dynamics
of 7 partially overlapping transcriptional programs. Cell type annotations from the UMAP in
figure C are visualised by the colour bar at the bottom.
E, A summary spatial plot of three module locations, named by the cell type in which they
reach their steady state expression.
F, Module state, markers and locations for individual selected modules dissect the spatio-
temporal neuron maturation process in detail. Late maturation modules map to deep layers
(e.g. modules 4, 5) and early maturation modules to upper layers of the cortex (e.g. module
2).
Discussion
Here we presented cell2fate, a Bayesian model of RNA velocity that is capable of
inferring transcriptional dynamics in settings of complex changes or weak signals in rare and
mature cell types. A core innovation of cell2fate is a formulation of the velocity problem that
builds on linearization, which allows for solving a biophysically accurate model using
analytically tractable linearized components. Another benefit of this formulation is that these
linear components can be inspected as interpretable RNA velocity modules. This provides for
a direct biophysical connection between cell2fate and statistical dimensionality reduction
methods. We illustrated this feature by characterising late maturation trajectories in granule
neurons that have been elusive with other methods. Furthermore, RNA velocity modules can
be used to locate differentiation trajectories in spatial transcriptomics data. We exemplified
this in the developing human brain where the RNA velocity modules of neuronal differentiation
showed a high degree of spatial organisation.
The concepts proposed in cell2fate are general and give rise to several extensions that
could be considered in the future. It is possible to formulate RNA velocity models with cell-
specific splicing and degradation rates, stochastic rates at lineage branching points and causal
connections between transcription rates at different time points, equivalent to dynamic gene
regulatory networks (Methods). In the long term, dynamical models should also include the
effects of cell-cell interactions, based on signalling molecules measured with spatial
transcriptomics. An immediate step towards this goal would be combining RNA velocity
14
bioRxiv preprint doi: https://doi.org/10.1101/2023.08.03.551650; this version posted August 5, 2023. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is
made available under aCC-BY-NC-ND 4.0 International license.
module mapping with spatial cell-cell interaction tools, such as NCEM31, which could identify
putative interactions that drive specific steps of a differentiation process.
Methods
Methods and a description of the cell2fate model can be found in the supplemental methods
document.
Code availability
All results from the cell2fate method can be reproduced with the notebooks included in the
cell2fate repository on github:
https://github.com/BayraktarLab/cell2fate/tree/main/notebooks
Benchmarking results for all methods can be reproduced with the notebooks in this separate
repository:
https://github.com/AlexanderAivazidis/fate_benchmarking
Data availability
Raw UMI counts and metadata in anndata format for all single cell and Visium data is available
for download on this portal: https://cell2fate.cog.sanger.ac.uk/browser.html
We will deposit FASTQ files for the human brain single-nucleus and Visium data on ENA by
the date of publication.
Acknowledgements
We gratefully acknowledge Leopold Parts, Yuanhua Huang, Mingze Gao and Chen Qiao for
valuable discussions on the cell2fate model, and Elena Prigmore and Jing Eugene Kwa for
assistance with human brain single nucleus transcriptomics. This work was funded by the
European Commission (ERC project DECODE, 810296) to O.S. and Wellcome Sanger
Institute core funding (220540/Z/20/A) to O.A.B..
Author contributions
A.A. conceived of the cell2fate model, implemented and tested it and produced all figures and
results in the manuscript. F.M. generated the human brain single-nucleus and Visium data.
V.K. contributed to model conception and implementation on pyro. B.C contributed to the
model conception. O.S and O.A.B. co-supervised A.A.. A.A., O.S. and O.A.B. co-wrote the
manuscript with feedback from all authors.
15
