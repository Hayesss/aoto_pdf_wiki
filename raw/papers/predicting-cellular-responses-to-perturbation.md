---
source_path: /mnt/c/Users/Administrator/Zotero/storage/RFDVMMPZ/Adduri 等 - Predicting cellular responses to perturbation across diverse contexts with State.pdf
ingested: 2026-04-23
sha256: 2e4c97822ca36b3c
---

bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
Predicting cellular responses to perturbation
State
across diverse contexts with
Abhinav K. Adduri∗,1, Dhruv Gautam∗,1,2, Beatrice Bevilacqua∗,1, Alishba Imran∗,1,2,
Rohan Shah∗,1,5, Mohsen Naghipourfar∗,1,2, Noam Teyssier∗,1, Rajesh Ilango∗,1,
Sanjay Nagaraj1,3, Mingze Dong1,6, Chiara Ricci-Tam1, Christopher Carpenter1,4,
Vishvak Subramanyam1,4, Aidan Winters1,4, Sravya Tirukkovular1, Jeremy Sullivan1,
Brian S. Plosky1, Basak Eraslan1, Nicholas D. Youngblut1, Jure Leskovec3,
Luke A. Gilbert1,4, Silvana Konermann†,1,3, Patrick D. Hsu†1,2,
Alexander Dobin†,1, Dave P. Burke†,1, Hani Goodarzi†,1,4, Yusuf H. Roohani†,‡,1
1Arc Institute; 2University of California, Berkeley; 3Stanford University;
4University of California, San Francisco; 5University of Pennsylvania; 6Yale University
Abstract
Cellular responses to perturbations are a cornerstone for understanding biological mecha-
nisms and selecting potential drug targets. While computational models offer tremendous
potential for predicting perturbation effects compared to experimental approaches, they
currentlystruggletogeneralizeeffectsfromexperimentallyobservedcellularcontextstoun-
observedones. Here,weintroduceState,amachinelearningarchitecturethatpredictsper-
turbation effects while accounting for cellular heterogeneity within and across perturbation
experiments. State operates across physical scales: it consists of a state transition model
thatlearnsperturbationeffectsacrosssetsofcellsusingdatafromover100millionperturbed
cells across 70 cell contexts and a cell embedding model trained on observational single-cell
data from 167 million human cells. State improved discrimination of perturbation effects
on multiple large datasets by over 50% and identified true differentially expressed genes
across genetic, signaling, and chemical perturbations with over 2-fold accuracy compared to
existing models. Using its embedding model, State can also identify strong perturbations
in novel cellular contexts where no perturbations have been observed during training. We
further introduce Cell-Eval, a comprehensive evaluation framework using biologically rel-
evant metrics that highlights how State enables more precise discovery of cell type-specific
perturbation responses, such as those related to cell survival. Overall, the performance and
flexibility of State sets the stage for scaling the development of virtual cell models.
∗State core contributor.
†These authors supervised this work.
‡Corresponding author: Y.H.R. (yusuf.roohani@arcinstitute.org)
1
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
1. Introduction
Therapeutic discovery relies on accurately predicting the impact of cellular perturbations.
Ranging from genetic interventions such as CRISPR or RNAi, to chemical treatments with
smallmoleculesorbiologics, theseperturbationsservenotonlytoinducedesiredphenotypes,
butarealsocentraltoestablishingcausalrelationshipsbetweengenes, pathways, andcellular
outcomes, thus uncovering deeper insights into cellular function. By selectively disrupting
specific components of cellular systems, scientists can identify causal drivers of phenotypes,
an essential step in both target identification and drug development. Experimental per-
turbation technologies enable researchers to probe the effects of interventions along two
main axes: the type of perturbation applied and the cellular or biological context. Both
factors profoundly influence the system’s response. Advances in functional genomics now
enable large-scale testing in specific cellular contexts, often through approaches like single-
cell screens that pair pooled CRISPR perturbations with transcriptome-wide readouts (Dixit
et al., 2016; Datlinger et al., 2017; Przybyla and Gilbert, 2022; Replogle et al., 2022; Nor-
man et al., 2019). However, these assays remain cost-prohibitive and labor-intensive to
scale across many contexts. Improving our ability to generalize perturbation response pre-
dictions across diverse biological contexts would greatly accelerate causal target discovery,
deepen our understanding of cellular function and disease, and in turn facilitate the design of
context-specific interventions, creating a foundation for personalized treatment predictions.
A range of computational approaches have been developed to tackle this problem (Lot-
follahi et al., 2019, 2023; Bunne et al., 2023; Roohani et al., 2024a; Cui et al., 2024; Hao
et al., 2024). However, despite the rapid growth of perturbation datasets in size and scope,
proportional gains in predictive capabilities have not been achieved (Wu et al., 2024; Cheval-
ley et al., 2022; Li et al., 2024b,a; Wenteler et al., 2024). Current deep learning methods
do not consistently outperform linear models when generalizing perturbation effects across
cellular contexts (Wu et al., 2024; Li et al., 2024b). We argue that this is primarily caused
by two major sources of noise that mask true perturbation effects in single-cell perturbation
datasets: biological heterogeneity within the studied population that is not explained by ex-
perimental covariates, and technical or experimental variation across different perturbation
datasets (Fig. 1A and Eq. 1).
The challenge of modeling biological heterogeneity is driven by an inherent limitation of
single-cellRNAsequencing: thedestructionofcellsduringmeasurementpreventsobservation
of their pre-perturbation states and accurate inference of each cell’s specific perturbation
response. To address this, perturbation effects are inferred by comparing populations of
perturbed and unperturbed cells, while attempting to resolve heterogeneity at the level of
cell type, batch, or other population-level covariates. Some approaches assume that within-
population heterogeneity is negligible compared to perturbation effects and simply map
perturbedcellstorandomlyselectedunperturbedcellswithsharedcovariates(Roohanietal.,
2024a), a mapping approach that has also been tested with expressive transformer-based
models (Cui et al., 2024; Hao et al., 2024). Although effective in datasets where perturbation
effects are strong (Norman et al., 2019), these approaches often fail to generalize when
perturbation effects are more subtle and heterogeneity in the unperturbed population may
even exceed the perturbation signal. This is particularly evident in cases of variation in cell
2
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
cyclestate, lineagebias, orpre-existingepigeneticprogramsandevenmoresowhenthebasal
populationisitselfdrawnfromdiversecelltypessuchasinin vivo studies(Lara-Astiasoetal.,
2023; Saunders et al., 2024). Other models treat cell populations as distributions, employing
generative approaches like variational autoencoders to learn data-generating distributions
or explicitly disentangle labeled and unlabeled sources of variation (Lotfollahi et al., 2023;
Piran et al., 2024; Bereket and Karaletsos, 2024; Weinberger et al., 2023; Lopez et al., 2023;
Papalexi et al., 2021; Weinberger et al., 2024; Song et al., 2025). However, in practice,
these models often fail to meaningfully outperform methods that do not explicitly model
distributional structure when applied to the prediction of perturbation effects (Wu et al.,
2024; Chevalley et al., 2022). Optimal transport-based methods that map unperturbed to
perturbed populations have also been proposed, but their applicability has been limited by
strong assumptions and poor scalability (Bunne et al., 2023, 2024b).
The second major source of noise is technical, arising from limitations in the data itself
rather than the model. In genetic perturbation experiments, the intended effects, such as
gene knockout or knockdown, may not always occur in each targeted cell, leaving cells incor-
rectly labeled as perturbed. Additional variability from experimental conditions, including
transduction efficiency, RNA sequencing depth, reagent chemistry, and timing of collection,
further complicate data integration across different studies (Bock et al., 2022). Together,
these technical confounders dilute the true perturbation-derived signal in the data, thereby
constraining the development of models that can generalize robustly across distinct datasets.
While single-cell foundation models have emerged as a strategy for learning robust cell rep-
resentations across datasets (Theodoris et al., 2023; Rosen et al., 2023; Cui et al., 2024; Hao
et al., 2024; Ho et al., 2024; Pearce et al., 2025), they are currently unable to meaningfully
distinguish between subtler variations such as those driven by genetic perturbations as they
have generally been optimized to differentiate between broader categories such as cell type
(Luecken et al., 2022).
Modeling heterogeneity in single cell perturbation experiments
The observed log-normalized perturbed expression state of each cell (X ) can be mod-
p
eled based on its unperturbed state. However, since the unperturbed state of the cell
is unobservable, we approximate X as
p
X ˆ ∼ T ˆ (D ) + H(D ) + ε, ε ∼ P (1)
p p basal basal ε
where
• D : The distribution of the unperturbed, baseline cell population.
basal
• T ˆ (D ): True effect caused by perturbation p on the population.
p basal
• H(D ): Biological heterogeneity of the baseline population.
basal
• ε: Experiment-specific technical noise, assumed independent of the unperturbed
cell state and D .
basal
This X ˆ serves as a distributional analogue of X , that is X ≈ d X ˆ , enabling modeling
p p p p
based on observable population characteristics.
3
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
To overcome these challenges and advance towards effective virtual cell models, we intro-
duce State, a flexible and expressive architecture for modeling cellular heterogeneity and
perturbation effects within and across diverse datasets. State is a multi-scale model with
two complementary modules: a State Transition model (ST) and a State Embedding model
(SE). ST is a transformer that uses self-attention to model perturbation-induced transfor-
mations across sets of cells, where each cell is represented either by its raw gene expression
profile or a learned embedding. SE is pretrained to generate expressive cell embeddings by
learning gene expression variation between cells across diverse datasets (Zhang et al., 2025;
Programetal.,2025;Youngblutetal.,2025), yieldingrepresentationsthatarerobusttotech-
nical variation and optimized for detecting perturbation effects. By leveraging self-attention
over sets of cells, ST can flexibly capture biological heterogeneity without relying on explicit
distributional assumptions. Together, SE and ST enable State to generalize across datasets
and perturbations, improving transferability of perturbation-response modeling.
The multi-scale architecture of State enables it to leverage both 167 million cells of
observational data to train its embedding model and over 100 million cells of perturbation
data to train a transition model. We evaluate State on several large-scale datasets, in-
cluding drug-based perturbations (Tahoe-100M (Zhang et al., 2025; Srivatsan et al., 2020)),
cytokine signaling perturbations (Parse Biosciences, 2023), and genome-scale genetic per-
turbations (Replogle et al., 2022; Nadig et al., 2025; Jiang et al., 2025; McFaline-Figueroa
et al., 2024; Feng et al., 2024). To fully assess the ability of State and other models to
simulate cellular perturbations, we present Cell-Eval, a comprehensive evaluation frame-
work that goes beyond conventional metrics based on expression counts to include a suite of
biologically relevant and interpretable metrics focused on differential expression prediction
and estimation of perturbation strength.
Across all metrics and data scales spanning multiple orders of magnitude, State con-
sistently outperforms both naive and state-of-the-art models. To our knowledge, it is the
first model to reliably outperform simple linear baselines in generalizing perturbation ef-
fects across cellular contexts. Moreover, we show that modeling perturbations in lower data
regimes with the State embedding enables the detection of strong responses in novel cell
types, when no perturbation data for those cell types are used during training. For example,
we demonstrate that pretraining State on the Tahoe-100M dataset (Zhang et al., 2025)
in the Arc Virtual Cell Atlas (Youngblut et al., 2025) improves the generalization of per-
turbation effects to unseen cellular contexts. Thus, State presents a scalable approach for
learning perturbation effects that transfer across datasets and experimental settings.
Beyond empirical performance, we provide novel theoretical results that connect State
to Optimal Transport (OT) theory, a commonly used method for modeling cellular hetero-
geneityinresponsetoperturbations(Bunneetal.,2023;Chenetal.,2024;Demiretal.,2024;
Dong et al., 2023; Bunne et al., 2024b; Ryu et al., 2024). Specifically, we prove that, under
mild regularity conditions and in an asymptotic limit, the unique continuous OT map be-
tween unperturbed and perturbed cell populations lies within the solution family of State.
This result positions State as a generalization of OT-based approaches: while it can recover
theclassical OTsolution, it alsoallowsformoreflexible modelingofperturbation effectsthat
may not adhere to the assumptions and constraints imposed by standard OT formulations.
4
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
Figure 1: State: A transformer-based model for predicting perturbation effects across
sets of cells. (A) Modeling perturbation effects at single-cell resolution requires disentangling bi-
ological signals from confounding variation introduced by noise, batch effects, and heterogeneity
across similarly treated cells. (B) State is a multi-scale machine learning architecture that oper-
atesacrossgenes,individualcells,andcellpopulations. ThecoreStateTransitionmodel(ST)learns
perturbation effects by training on sets of perturbed and unperturbed cell populations grouped by
shared covariates (e.g., perturbation type, cell context, and batch). ST can operate directly on gene
expression profiles or on compact cell representations from the State Embedding model (SE), which
learns information-rich embeddings from large-scale observational data. This multi-scale architec-
ture allows ST to effectively simulate perturbation experiments in silico and support downstream
analyses such as expression quantification, differential gene expression analysis, and estimation of
perturbation effect sizes. (C) ST is a transformer model that takes sets of unperturbed cell popu-
lations and perturbation labels as input to predict corresponding perturbed cell populations. When
using gene expression profiles to represent cells, ST directly predicts transcriptomes at single-cell
resolution. When using State embedding inputs, ST predicts output embeddings that are then
decoded with an MLP to predict transcriptomes. (D) Increasing the size of cell sets improves vali-
dationlossuptoanoptimalpoint, withbestperformanceontheTahoe-100M dataset(Zhangetal.,
2025)achievedwhencovariate-matchedgroupsarechunkedintosetsof256cells. ThefullSTmodel
significantly outperforms a pseudobulk model (State with mean-pooling instead of self-attention)
and a single-cell variant (State with set size = 1). An ablation removing the self-attention mech-
anism substantially degrades performance, highlighting the importance of modeling interactions
between cells within a set.
5
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
2. Results
2.1. Building the State Transition model for predicting perturba-
tion effects on sets of cells
State is a multi-scale machine learning architecture that predicts downstream transcrip-
tomic responses to cellular perturbations, including gene expression changes, differentially
expressed genes, and overall perturbation effect sizes (Fig. 1B). It leverages (i) at the molec-
ular level, embeddings that represent individual genes across experiments and species; (ii) at
the cellular level, embeddings that capture the transcriptomic state of each individual cell,
represented either as the cell’s log-normalized transcriptome or as embeddings generated
by the State Embedding model (SE); and (iii) at the population level, the State Transi-
tion model (ST) learns perturbation effects across sets of cells. State can leverage both
observational and interventional data during training: SE is trained on 167 million human
cells drawn from multiple large observational single-cell repositories (Youngblut et al., 2025;
Zhang et al., 2025; Program et al., 2025), and ST is trained on over 100 million chemically
or genetically perturbed cells from large-scale single-cell screens (Zhang et al., 2025; Parse
Biosciences, 2023; Replogle et al., 2022).
The core motivation for ST is to model cellular heterogeneity beyond known covariates,
such as cell type and perturbation label, to improve perturbation response prediction. To
achieve this, cells are first stratified by known covariates (Fig. S1). For each covariate-
matched perturbed group, ST constructs non-disjoint cell sets of fixed size, which serve as
input during training and are paired with unperturbed control cell sets of equal size and
matched covariates. ST uses a transformer backbone to perform repeated bidirectional self-
attention and feed-forward operations across control cell sets (Section 4.3, Fig. S2A). This
enables ST to model heterogeneity within the input cell set while predicting downstream
transcriptomic responses to perturbation (Fig. 1C).
ST is trained using a maximum mean discrepancy (MMD) loss between predicted and
observed transcriptomes of perturbed cells. While ST learns perturbation effects across
distributions of cells, it still predicts perturbed cell profiles for individual cells, a feature
that is important for learning distributional structure of a perturbed population. Empirical
resultsshowthatincreasingcellsetsize,uptoathreshold,achievesmuchlowervalidationloss
compared to losses on individual cells, whether they are true samples or pseudobulked across
neighboring cells (Fig. 1D). Furthermore, removing the self-attention leads to degraded
performance(Fig. 1D),highlightingthevalueofflexibleset-basedself-attentionformodeling
cellular heterogeneity relevant to perturbation response prediction.
2.2. State outperforms baselines in predicting perturbation effects
across cell contexts
We tested the State architecture on a generalization task assessing its ability to predict
perturbation effects in new cellular contexts, such as unseen cell lines or donors. Specifically,
we implemented an underrepresented context generalization task (Section 4.2.1), in which
each model had access to 30% of perturbations in the test context during training (Fig. 2A).
6
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
Figure 2: State outperforms existing baselines in predicting perturbation effects
across cell contexts. (A) Underrepresented context generalization task. Models were trained
on perturbation data from one or more cell contexts and evaluated on their ability to predict the
effects of the same perturbations in a largely held-out and underrepresented target context. (Con-
tinued on next page)
7
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
Figure 2 (Continued): The “perturbation mean” baseline estimates effects by averaging ob-
served differences between perturbed and control states across training cell contexts. The “context
mean” baselineusestheaverageexpressionprofileofthetargetcellcontextacrossalltrainingpertur-
bations. (B) Models were trained and evaluated on chemical, signaling, and genetic perturbation
datasets (Zhang et al., 2025; Parse Biosciences, 2023; Replogle et al., 2022; Nadig et al., 2025).
Comparisons included the mean baselines from (A), a simple linear model (Ahlmann-Eltze et al.,
2024), autoencoder-based models (scVI (Lopez et al., 2018), CPA (Lotfollahi et al., 2023)), and a
foundationmodel(scGPT(Cuietal.,2024)). (C)PerformancewasassessedusingCell-Evalmet-
rics (Section 4.7) on standard Perturb-Seq outputs: expression counts and differentially expressed
(DE) genes, with the following highlighted: (D) Perturbation discrimination score, measured us-
ing inverse normalized rank. (E) Pearson correlation between predicted and observed change in
post-perturbation log-normalized expression counts. (F) Area under the Precision-Recall curve for
model predictions of DE genes. (G) Precision-Recall curves for model predictions of DE genes.
(H) Spearman correlation of log fold changes for significant DE genes between predictions and true
values. (I) Overlap in top DE genes, defined as the percentage of significant genes in observed data
that were also predicted as significant in predictions. (J) Spearman correlation between predicted
and true overall perturbation effect size. (K) Confusion matrix comparing predicted and observed
perturbationeffectsizes, measuredbythenumberofdifferentiallyexpressedgenesperperturbation.
We benchmarked performance against several baselines (Section 4.7.5), including a simple
linear model (Ahlmann-Eltze et al., 2024) and three published machine learning models for
this task: CPA (Lotfollahi et al., 2023), scVI (Lopez et al., 2018), and scGPT (Cui et al.,
2024). We also included two naive mean-based baselines that explain a significant portion of
observed variance in cell-type generalization tasks (Fig. 2A). The “context mean” baseline
predicts the average expression observed in the training data for a given cell context across
all perturbations (Kernfeld et al., 2023), while the “perturbation mean” baseline predicts
the average perturbation effect across training cell contexts applied to the basal expression
for a given cell context. In our results, we refer to baselines predicting mean expression or
mean perturbation effect as “mean baselines” and the other models as “baseline models”. All
models (including State) were trained to predict the log-expression of the top 2,000 highly
varying genes (HVGs), a commonly used feature space for baseline comparisons.
WeevaluatedStateonchemicalperturbationdatafromtheTahoe-100M dataset(Zhang
et al., 2025), cytokine signaling perturbations from Parse Biosciences (Parse Biosciences,
2023) (abbreviated Parse-PBMC), and genetic perturbation data from Replogle et al. (2022)
and Nadig et al. (2025) (abbreviated Replogle-Nadig)(Fig. 2B). Tahoe-100M includes per-
turbation responses from 50 diverse cancer cell lines treated under 1,138 conditions involving
380 distinct drug perturbations. Parse-PBMC contains 90 cytokine perturbation responses
across 12 donors and 18 cell types. Replogle-Nadig consists of 2,024 genetic perturbations
applied to four distinct cell lines after filtering perturbations with low on-target efficacy. For
all datasets, we trained State directly on cell representations derived from highly variable
genes (ST+HVG).
To test generalization, we implemented a careful data splitting strategy: for the Tahoe-
100M dataset, we plotted a PCA using pseudobulked expression values for the fifty available
cell lines to visually identify distinct phenotypic clusters. From these, five cell lines were
8
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
chosen to be in the test set for final model evaluation (Fig. S3). No data from these cell
lines was observed throughout the model development process. In a separate evaluation,
we iteratively held out all cells from 11 distinct organs for testing. For the Parse-PBMC
dataset, we held out 4 random donors from the 12 donor cell lines. For each of these held-out
contexts, 30% of its perturbations were randomly removed from the test data and included
in the respective training data. For the Replogle-Nadig dataset, we conducted an evaluation
by iteratively holding out one cell line as a test set. For each iteration, models were trained
on the remaining three cell lines plus an additional 30% of perturbations randomly sampled
from the test cell line.
Our evaluation framework captures key outputs of a single-cell perturbation experiment
which are well represented through three readout categories: (1) gene expression counts, (2)
differentialexpression(DE)statistics,includingidentificationofdifferentiallyexpressedgenes
(DEGs) and their log fold changes, and (3) the magnitude of the perturbation effect (e.g.,
the total number of DEGs) (Fig. 2B). To comprehensively assess model performance across
these dimensions, we developed a suite of evaluation metrics, Cell-Eval (Section 4.7,
Fig. 2C). These metrics are designed to be both expressive and biologically interpretable,
offering complementary insights. For example, while overlap in DEGs helps link predictions
tospecificpathwaysgivingthembiologicalsignificance,itmaybelesssensitivetofine-grained
changes compared to the perturbation discrimination score, which captures the similarity
between predicted and true perturbation effects. Moreover, by benchmarking against naive
baselines, these metrics provide a clearer assessment on generalization performance versus
memorization of training-set effects.
A central goal of perturbation experiments is to identify perturbations that optimally
drive desired transcriptomic states. For a model to do this, it must be able to effectively
distinguish between different perturbation effects. Using a variant of the perturbation dis-
crimination score adapted from Wu et al. (2024), which ranks predicted post-perturbation
expression profiles by their similarity to the true perturbation outcomes, State achieved
an absolute improvement of 54% and 29% on the Tahoe and PBMC datasets respectively
(Fig. 2D). On genetic perturbation datasets, State matched the performance of the per-
turbation mean baseline and significantly outperforms baseline models.
To directly assess the accuracy of predicted gene expression counts, we computed the
Pearsoncorrelationbetweenobservedandpredictedperturbation-inducedexpressionchanges.
On this metric, State outperformed baselines by 63% on the Tahoe dataset and 47% on
the PBMC dataset. For the genetic perturbation dataset, this task is more challenging due
to the subtler effects of perturbations. State again matched the best-performing baseline,
which in this case was the context mean and not the perturbation mean, highlighting that
State’s predictions were not trivially similar to any single naive baseline (Fig. 2E).
To evaluate State beyond global ranking and correlation metrics, we conducted a sys-
tematic differential-expression (DE) analysis. Using a Wilcoxon rank-sum test, we identified
differentially expressed genes post-perturbation, calculating both their log fold changes and
adjusted p-values (false discovery rate). We decomposed our DE analysis into assessments of
each component (p-value and log fold change) independently as well as in combination (DE
gene overlap). To evaluate p-values for model-predicted DE genes, we first computed true
9
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
significantly DE genes using the experimentally observed perturbation data while setting
an FDR threshold of 0.05. P-values derived from model predictions were then compared to
true significance levels using a precision-recall curve. Measuring the area under the preci-
sion recall curve, we found that State consistently outperforms all baselines across datasets
(Fig. 2F). Notably, State’s AUPRC is 184% higher than the next best approach for the
genetic perturbation dataset (Fig. 2G, Fig. S4).
For evaluating log fold change, we limited our analysis to true significant DE genes to
limit confounding from predicted significance levels. The Spearman correlation was com-
puted between the predicted and true log fold changes for each of these genes. Some ma-
chine learning baselines such as scVI showed strong performance on this metric, yet State’s
performance was still over 10% higher than baselines for both Tahoe and PBMC datasets
(Fig. 2H). To simulate a practical DE analysis workflow, we selected DE genes using an
FDR threshold of 0.05 applied to model-predicted p-values, then ranked this set by log fold
change and compared it to the equivalent set derived from true p-values and fold changes.
Using different setting of overlap size (k = 50,100,200), we observe strong performance by
State across all three datasets and all three settings of k (Fig. S5A). For completeness,
we also evaluated the model on a variable sized overlap by setting k to be the same size as
the number of true differentially expressed genes. State is twice as good as the next base
baseline (scGPT) on the Tahoe dataset and 43% better than the corresponding best baseline
(Linear) on the PBMC dataset (Fig. 2I). To assess a more practically relevant scenario of
minimizing false positives, we also measured the proportion of predicted top k DE genes that
were significant at all in the observed experimental data (precision at k). Across datasets
and settings of k, State showed much stronger performance than baselines (Fig. S5B).
Moving beyond identification of individual genes, we assessed the accuracy of models in
predicting perturbation effects across the transcriptome. State accurately ranked pertur-
bations by their relative effect sizes, achieving Spearman correlations 53% higher on Parse-
PBMC and 22% higher than baselines on Replogle-Nadig, and 70% higher on Tahoe-100M
approaching an absolute correlation of 0.8 (Fig. 2J). Looking at the trend across individual
perturbations, we observe that State can predict perturbation effects across both datasets
with large effect sizes (i.e. drug perturbations in Tahoe) as well as those with subtler mag-
nitude of effects, such as the genetic perturbation dataset Replogle-Nadig (Fig. 2K).
Finally, to assess generalization across biological contexts with limited target data, we
evaluated tissue-level performance. In this setting, State was trained on HVGs for all but
onetissueandtestedontheheld-outtissue. AcrossmetricssuchasPearsoncorrelation, DEG
overlap, and log fold change accuracy, State consistently outperformed the perturbation
mean baseline (Fig. S6).
While State consistently outperformed all baseline models across datasets with few ex-
ceptions, the performance gains over mean baselines were notably larger on Tahoe-100M,
which includes 100 million cells spanning thousands of perturbations across dozens of base-
line cellular contexts, and Parse-PBMC, which includes 10 million cells across 12 donors
and 18 cell types, as compared to the genome-scale genetic perturbation datasets conducted
in just a few cell lines. This highlights State’s ability to leverage data scale and context
diversity more effectively than existing models, which do not display proportionate gains
10
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
in performance despite more data. Moreover, even in the case of the genetic perturbation
dataset, where some baselines showed occasional benefit over State on certain metrics (Lin-
ear model outperformed on DE overlap by 20% and the context mean baseline outperformed
on fold change prediction by 10%), these models were always inconsistent and were unable
to consistently outperform across multiple metrics. In contrast, State demonstrated the
most consistent performance overall.
2.3. State embeddings enhance zero-shot perturbation prediction
across contexts and perturbation modalities
One of the goals in creating virtual models of cell state and behavior is to develop general-
purpose predictive models that can be applied to new contexts, even when no perturbation
data are available for those contexts (Bunne et al., 2024a). These models should also be
able to learn cell regulatory information from one dataset and transfer it effectively to other
datasets regardless of perturbation modality, such as chemical or genetic interventions. How-
ever, gene expressioncountsare subjectto context-specificvariability(e.g., sequencingdepth
and experimental platform), and do not always generalize well across studies.
To address this, we developed a unified cell representation that can be shared across
datasets and experiments, enhancing perturbation prediction capabilities in previously un-
perturbed cellular contexts. The State Embedding model (SE) complements ST by learning
cell embeddings that are optimized to capture cell-type specific gene expression patterns
(Fig. 3A). When used with ST, the embedding enables a smoother landscape over cell
states, learned using a vast repository of observational single-cell data (Program et al., 2025;
Zhang et al., 2025; Youngblut et al., 2025). SE enables us to indirectly leverage observa-
tional single-cell data to improve perturbation response predictions, especially in cases where
interventional data for a particular context is scarce or noisy.
Architecturally, the SE encoder is a dense, bidirectional transformer trained to predict
log-normalized gene expression (Section 4.4). The SE decoder is a smaller, specialized
MLP that predicts gene expression from a combination of the learned cell embedding and the
target gene embedding (Fig. S2B). This architectural asymmetry encourages the learning
of generalizable representations of cell state in a single vector embedding. SE is trained
with a loss computed along two axes: it predicts expression across genes within each cell,
and for each gene across cells in each minibatch. This dual-axis formulation encourages the
model to capture relative variation in gene expression both within individual cells and across
the population (Lal et al., 2024; Ding et al., 2025; Fischer et al., 2024). The loss enhances
the model’s sensitivity to perturbation effects by preserving the inter-cellular variability
necessary for accurate differential expression modeling.
By learning a general-purpose embedding that captures subtle cell-to-cell variation, SE
addresses a core challenge in perturbation modeling: defining a transferable feature space
acrosssingle-celldatasets(Fig. 3B).WhenSEandSTareusedtogether,STlearnstopredict
perturbed cell embeddings, while simultaneously learning to decode those predicted embed-
dings to log expression space (Fig. S2B). To assess the quality of the embeddings produced
by SE, we evaluated their ability to distinguish between perturbations. We measured intrin-
11
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
Figure 3: State embeddings enhance zero-shot perturbation effect prediction across
datasets, experiments, and modalities. (A) The State Embedding model (SE) learns rich,
generalizable representations of transcriptomic information across diverse datasets. Given a control
(unperturbed) cell population, SE computes cell embeddings. ST then predicts how those embed-
dings shift in response to a specified perturbation, effectively modeling the distributional effect of
the perturbation in latent space. Finally, a learnt decoder maps the predicted embeddings back into
gene expression space. (Continued on next page)
12
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
Figure 3 (Continued): (B) Understanding the impact of a shared latent space across datasets
for modeling perturbation effects across diverse cell contexts and perturbations. (C) Embedding
quality is evaluated using both intrinsic and extrinsic metrics: intrinsic performance reflects classifi-
cationaccuracyofperturbedcellsintheembeddinggeneratedusingobserveddata; extrinsicperfor-
mance measures the classification accuracy over perturbed embeddings predicted by ST trained on
the cell embeddings. (D) Over two held-out perturbation datasets, using the intrinsic and extrinsic
metrics, we evaluate State embeddings against cell embeddings generated by scFoundation (Hao
et al., 2024), scGPT (Cui et al., 2024), Universal Cell Embedding (UCE) (Rosen et al., 2023), and
Transcriptformer (TF) (Pearce et al., 2025). State embeddings consistently outperform comparable
modelembeddings, evenpassingtheperformanceachievedusingtheoriginalexpressioncounts. (E)
State embeddings enhance prediction of perturbation effects zero-shot, e.g. in novel cell contexts
not seen perturbed at the time of training. (F) ST with State embeddings is pretrained using
Tahoe-100M and adapted using a query dataset consisting of one or more contexts, of which one
is called query context. ST is evaluated without any training using perturbations in the query cell
context (Section 4.2.2). (G) Zero-shot performance in ranking perturbations by overall effect size
in new cell contexts over 5 query datasets. (H) Zooming into Parse-PBMC, State embeddings also
improve performance over other metrics from Cell-Eval. More datasets are shown in Figure S7.
sic quality by testing how well the embeddings of observed cells cluster by perturbation label,
and extrinsic quality by examining how well the predicted embeddings from ST preserve this
separation (Fig. 3C). We compared SE against using gene expression counts directly, as
well as cell embeddings generated by scFoundation (Hao et al., 2024), scGPT (Cui et al.,
2024), Universal Cell Embedding (UCE) (Rosen et al., 2023), and Transcriptformer (TF)
(Pearce et al., 2025) across three held-out perturbation datasets not seen during SE training
(Srivatsan et al., 2020; Jiang et al., 2025; Replogle et al., 2022). To measure separability,
we train a simple linear probe on the embeddings to predict the perturbation label called
for that cell. State embeddings more effectively separated between perturbation phenotypes
compared to all other foundation models and the original expression counts, surpassing even
the performance achieved using the original data representation (Fig. 3D). This suggests
that SE is, in some cases, capable of denoising Perturb-seq data. In the extrinsic evaluation,
State embeddings also led to over a 6% absolute improvement in downstream perturbation
classification accuracy compared to all baselines.
Projecting gene expression into a shared latent space also enables zero-shot identification
of strong perturbation effects in new cell contexts (i.e., without explicit training in the new
cell context) (Fig. 3E). We assessed the robustness of embeddings from SE by pretraining
State (ST+SE) on Tahoe-100M and adapting the model with full fine tuning on smaller,
noisierdatasetswithnewcellcontexts(Fig. 3F).Inpredictingperturbationeffectsforprevi-
ously unperturbed contexts, State trained with the State embedding (ST+SE) consistently
ranked perturbation by their effect sizes more accurately than both the perturbation mean
baseline and State models trained directly on gene expression (ST+HVG). This evaluation
was performed using five datasets - which included two genetic perturbation datasets (Jiang
et al., 2025; McFaline-Figueroa et al., 2024) and a drug perturbation dataset (Srivatsan
et al., 2020) in addition to datasets used for the previous analyses, producing a total of
2102 perturbations (Fig. 3G) across 5 datasets and 40 cell contexts. For larger datasets
13
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
like Parse-PBMC and Replogle-Nadig, using the State embedding achieved more than 17%
improvement with an absolute Spearman correlation greater than 0.5. In smaller genetic
perturbation datasets (e.g., McFaline et al. and Jiang et al.), where baseline performance
was near zero, embeddings yielded several-fold improvements.
Dataset-specific processing and quality differences also affected other metrics. Notably,
in datasets with strong perturbation effects, zero-shot improvements of using SE were con-
sistent. For example, on the Parse-PBMC dataset, we saw an average of 15% improvement
across all five metrics described in Section 2.2 (Fig. 3H). When excluding cases where
baseline HVG performance was below 10% (indicating noisy data), the adaptation improve-
ments remained largely consistent across all 5 datasets tested (Fig. S7). These results show
SE’scapacityfortransferringlearningacrossdatasetswheretechnicalvariationcanconfound
the biological signal driven by perturbation. ST+SE model performance also consistently
benefited from pre-training even for datasets without drug-based perturbations (e.g. genetic
or signaling perturbations), highlighting the successful transfer of cell regulatory information
across perturbation modalities (Fig. S8).
2.4. State can detect cell type-specific response to perturbations
To illustrate a practical application of State, we evaluated its ability to detect cell type-
specific differential expression (Fig. 4A). This analysis focused on five held-out cell lines
from the Tahoe-100M dataset (Fig. 4A). We identified perturbations with strong cell type
specificity by comparing the overlap of DE genes and the Spearman correlation of log fold
changes between State’s predictions and two baselines: the context mean and the perturba-
tion mean. Improved performance relative to the perturbation mean baseline suggests that
State learns perturbation effects that are specific to a given cell type. Similarly, gains over
the context mean baseline indicate that the model can distinguish between different pertur-
bations within the same cell line and is not trivially predicting the average expression for
each cell line. Across perturbations, State consistently displayed superior ability to recover
the true ranking of log fold changes for differentially expressed genes, outperforming both
the context mean and perturbation mean baselines (Fig. 4B, C).
To explore the biological relevance of a State-generated prediction, we ranked pertur-
bations by how far they improved performance over the mean baselines, suggesting enhanced
sensitivity to context-specific effects. Out of the top two perturbations from over 700 possi-
ble choices, one was an FDA-approved drug for BRAF-mutant melanoma and certain other
tumors, Trametinib(Lugowskaetal.,2015). Wechosethisperturbation(specifically, 0.5µM
Trametinib) since one of the five test cell lines, C32, is a melanoma line known to have the
overactive BRAF mutation V600E (Banach et al., 2021). The model was not trained on C32
cells treated with any dosage of Trametinib. Both the predicted significance values for DE
genes in C32 following perturbation with Trametinib (Fig. 4D) and the log fold changes for
the true DE genes (Fig. 4E) showed much stronger alignment with ground truth for State
relative to mean baselines. Notably, context and perturbation mean baselines exhibited little
to no correlation with ground truth DE gene significance due to assigning extremely high lev-
els of significance to the vast majority of genes. This inability to distinguish signal from noise
underscores the limitations of simple averaging approaches, and highlights State’s advan-
14
bioRxiv preprint doi: https://doi.org/10.1101/2025.06.26.661135; this version posted June 27, 2025. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made
available under aCC-BY 4.0 International license.
Figure 4: State detects cell type-specific gene expression modulations in response
to perturbation. (A) Application of State for identifying perturbations with cell type-specific
effects. (B) DE Gene Overlap between predicted and observed perturbation effects. (C) Spearman
correlation between predicted versus observed log fold changes for differentially expressed (DE). For
(B) and (C) Left: comparison between State and the context mean baseline. Right: comparison
withtheperturbation meanbaseline. Aspecific held-out perturbation(Trametinib, 0.05 µM)shows
substantially higher correlation for State relative to both baselines, indicating detection of pertur-
bation effects that are both cell type specific but also not trivially predicted by the cell type mean.
(D) Predicted versus observed significance values for DE genes following Trametinib (0.05 µM)
perturbation, across the top 2,000 highly variable genes. State (blue) shows closer alignment with
ground truth than baselines (yellow). (Continued on next page)
15
