---
source_path: /mnt/c/Users/Administrator/Zotero/storage/GHPX9Q7S/s41586-023-06139-9.pdf
ingested: 2026-04-23
sha256: 93fac521515faa31
---

Article
Transfer learning enables predictions in
network biology
https://doi.org/10.1038/s41586-023-06139-9 Christina V. Theodoris1,2,3,4 ✉, Ling Xiao2,5, Anant Chopra6, Mark D. Chaffin2, Zeina R. Al Sayed2,
Matthew C. Hill2,5, Helene Mantineo2,5, Elizabeth M. Brydon6, Zexian Zeng1,7, X. Shirley Liu1,7,8
Received: 29 March 2022
& Patrick T. Ellinor2,5 ✉
Accepted: 27 April 2023
Published online: 31 May 2023
Mapping gene networks requires large amounts of transcriptomic data to learn the
Check for updates connections between genes, which impedes discoveries in settings with limited data,
including rare diseases and diseases affecting clinically inaccessible tissues. Recently,
transfer learning has revolutionized fields such as natural language understanding1,2
and computer vision3 by leveraging deep learning models pretrained on large-scale
general datasets that can then be fine-tuned towards a vast array of downstream tasks
with limited task-specific data. Here, we developed a context-aware, attention-based
deep learning model, Geneformer, pretrained on a large-scale corpus of about
30 million single-cell transcriptomes to enable context-specific predictions in
settings with limited data in network biology. During pretraining, Geneformer gained
a fundamental understanding of network dynamics, encoding network hierarchy
in the attention weights of the model in a completely self-supervised manner.
Fine-tuning towards a diverse panel of downstream tasks relevant to chromatin and
network dynamics using limited task-specific data demonstrated that Geneformer
consistently boosted predictive accuracy. Applied to disease modelling with limited
patient data, Geneformer identified candidate therapeutic targets for cardiomyopathy.
Overall, Geneformer represents a pretrained deep learning model from which
fine-tuning towards a broad range of downstream applications can be pursued to
accelerate discovery of key network regulators and candidate therapeutic targets.
Mapping the gene regulatory networks that drive disease progres- to yield meaningful predictions when used in isolation. Unlike model-
sion enables screening for molecules that correct the network by nor- ling approaches that necessitate retraining a new model from scratch
malizing core regulatory elements, rather than targeting peripheral for each task6,7, this approach democratizes the fundamental know-
downstream effectors that may not be disease modifying4,5. However, ledge learned during the large-scale pretraining phase to a multitude
mapping the gene network architecture requires large amounts of of downstream applications distinct from the pretraining learning
transcriptomic data to learn the connections between genes, which objective, transferring knowledge to new tasks (Fig. 1a and Extended
impedes network-correcting drug discovery in settings with limited Data Fig. 1a,b). The advent of the self-attention mechanism1,2 has fur-
data, including rare diseases and diseases affecting clinically inacces- ther transformed the deep learning field by generating context-aware
sible tissues. Although data remain limited in these settings, recent models that are able to pay attention to large input spaces and learn
advances in sequencing technologies have driven a rapid expansion in which elements are most important to focus on in each context, boost-
the amount of transcriptomic data available from human tissues more ing predictions in a wide realm of applications2,8. Gene regulatory net-
broadly. Furthermore, single-cell technologies have facilitated the work architectures are highly context-dependent, and attention-based
observation of transcriptomic states without averaging the expression models, known as transformers, may be exceptionally suited to
of genes across multiple cells, potentially providing more precise data context-specific modelling of network dynamics.
for inference of network interactions, especially in diseases driven by Here, we developed a context-aware, attention-based deep learning
dysregulation of multiple cell types. model, Geneformer, pretrained on large-scale transcriptomic data to
Recently, the concept of transfer learning has revolutionized fields enable predictions in settings with limited data. We assembled a large-
such as natural language understanding1,2 and computer vision3 by scale pretraining corpus, Genecorpus-30M, comprising 29.9 million
leveraging deep learning models pretrained on large-scale general human single-cell transcriptomes from a broad range of tissues from
datasets that can then be fine-tuned towards a vast array of down- publicly available data. We then pretrained Geneformer on this corpus
stream tasks with limited task-specific data that would be insufficient using a self-supervised masked learning objective to gain a fundamental
1Department of Data Science, Dana-Farber Cancer Institute, Boston, MA, USA. 2Cardiovascular Disease Initiative and Precision Cardiology Laboratory, Broad Institute of MIT and Harvard,
Cambridge, MA, USA. 3Division of Genetics and Genomics, Boston Children’s Hospital, Boston, MA, USA. 4Harvard Medical School Genetics Training Program, Boston, USA. 5Cardiovascular
Research Center, Massachusetts General Hospital, Boston, MA, USA. 6Precision Cardiology Laboratory, Bayer US LLC, Cambridge, MA, USA. 7Department of Biostatistics, Harvard T.H. Chan
School of Public Health, Boston, MA, USA. 8Center for Functional Cancer Epigenetics, Dana-Farber Cancer Institute, Boston, MA, USA. ✉e-mail: christina.theodoris@gladstone.ucsf.edu;
ellinor@mgh.harvard.edu
616 | Nature | Vol 618 | 15 June 2023
Self-supervised large-scale pretraining Fine-tuning with limited task-specific data
Limited task-specific
data for task 1
Fine-tuning
Fine-tuning
Model for layer for
Genecorpus-30M fine-tuning task 1 Task 1
task 1 predictions
Self-supervised Copy
pretraining Pretrained weights
...
Geneformer
Fine-tuning
Model for layer for
fine-tuning task N Task N
task N predictions
Fine-tuning
Limited task-specific
data for task N
Tissue representation of Genecorpus-30M
Brain
Placenta Prostate Breast
Adrenal Small intestine Lymphatic Decidua
Unlabelled Adipose Tonsil Bone marrow
Pancreas Endothelial Bladder Oesophagus
Airway Bone Stomach Skin
Immune
Cord blood Pluripotent Embryo Eye
Spleen Intestine, NOS Nasal Testis
Thymus Yolk sac Ear
Large intestine
Lymph node Muscle Liver
Kidney
Lung Heart
Gene T
Gene H
Gene Y
Gene A
Gene Z
Gene L
understanding of network dynamics. The pretrained Geneformer accu- of downstream applications can be pursued to accelerate discovery
rately predicted dosage-sensitive disease genes and their downstream of key network regulators and candidate therapeutic targets.
targets through a context-aware in silico deletion approach. Further-
more, fine-tuning Geneformer towards a diverse panel of downstream
Geneformer architecture and pretraining
tasks relevant to chromatin and network dynamics using just a limited
set of task-specific training examples demonstrated that Geneformer Geneformer is a context-aware, attention-based deep learning model
consistently boosted predictive accuracy. Applied to disease model- pretrained on large-scale transcriptomic data to enable predictions in
ling of cardiomyopathy, Geneformer predicted candidate therapeutic network biology with limited data through transfer learning (Fig. 1a).
targets whose experimental inhibition significantly improved cardio- Geneformer harnesses the recent advent of self-attention1,2 to maintain
myocyte contraction in an induced pluripotent stem cell (iPSC)-based attention over the large input space of genes expressed in the transcrip-
model of the disease. Overall, Geneformer represents a pretrained tome of each single cell and learn which genes are most important to
deep learning model from which fine-tuning towards a broad range focus on to optimize predictive accuracy within the given learning
Nature | Vol 618 | 15 June 2023 | 617
seneg
deknaR
a
S
Democratize
fundamental
understanding of
network dynamics
to vast array of
downstream
applications
b
c Rank value encoding
Transformer encoder unit
Contextual gene
and cell embeddings
Single-cell ... Contextual
transcriptome attention weights
Contextual
predictions
×6
noitnetta
fleS
noitazilamron
reyaL
drawrof-deeF krowten
laruen
noitazilamron
reyaL
Fig. 1 | Geneformer architecture and transfer learning strategy. a, Schematic Genecorpus-30M. NOS, not otherwise specified. c, Pretrained Geneformer
of transfer learning strategy with initial self-supervised large-scale pretraining, architecture. Each single-cell transcriptome is encoded into a rank value
copying pretrained weights to models for each fine-tuning task, adding encoding that then proceeds through six layers of transformer encoder units
fine-tuning layer and fine-tuning with limited task-specific data towards with parameters as follows: input size of 2,048 (fully represents 93% of rank
each downstream task. Through the single initial self-supervised large- value encodings in Geneformer-30M), 256 embedding dimensions, four
scale pretraining on a generalizable learning objective, the model gains attention heads per layer and feed-forward size of 512. Geneformer uses full
fundamental knowledge of the learning domain that is then democratized to a dense self-attention across the input size of 2,048. Extractable outputs include
multitude of downstream applications distinct from the pretraining learning contextual gene and cell embeddings, contextual attention weights and
objective, transferring knowledge to new tasks. b, Tissue representation of contextual predictions.
Article
objective. Importantly, network dynamics may vary across cell types, MYOD (Extended Data Fig. 2d,e). Furthermore, genes known to be
developmental timepoints or disease states. Accordingly, context highly context-dependent, such as NOTCH receptors, showed more
awareness is a unique strength of Geneformer’s model architecture variability in their embeddings across variable cell types14 compared
that allows predictions specific to each cell context. to the known housekeeping gene GAPDH (Extended Data Fig. 3).
First, we assembled a large-scale pretraining corpus, Genecorpus-30M, Next, we integrated the embeddings of genes expressed in each cell
comprising 29.9 million human single-cell transcriptomes from a broad to generate cell-level embeddings, which encode characteristics of
range of tissues from publicly available data (Fig. 1b and Supplementary the state of that single cell. Using a publicly available aortic aneurysm
Table 1). We excluded cells with high mutational burdens (for example, dataset14 as a test case, we found that although the original data were
malignant cells and immortalized cell lines) that could lead to sub- impacted by interpatient variability, Geneformer cell embeddings
stantial network rewiring without companion genome sequencing clustered primarily by cell type and phenotype as opposed to individual
to facilitate interpretation, and we established metrics for scalable patient (Extended Data Fig. 4a). Given that the pretrained Geneformer’s
filtering to exclude possible doublets and/or damaged cells. cell embeddings were robust to these technical artefacts, we next tested
The transcriptome of each single cell is then presented to the model as whether fine-tuning would impact generalizability. Using a publicly
a rank value encoding where genes are ranked by their expression in that available dataset11 of iPSC differentiation to cardiomyocytes assayed
cell normalized by their expression across the entire Genecorpus-30M in parallel on the Drop-seq (single cell) or DroNc-seq (single nucleus)
(Fig. 1c). Although the rank-based representation has limitations platform, we tested whether fine-tuning the model to distinguish cell
including not fully taking advantage of the precise gene expression types using data from one platform would reduce generalizability
measurements provided in transcript counts, the rank value encod- to cells assayed on the other platform. Interestingly, the fine-tuned
ing provides a non-parametric representation of the transcriptome of Geneformer’s cell embeddings primarily clustered by cell types and
each single cell and takes advantage of the many observations of the showed improved integration of platforms compared to the original
expression of each gene across Genecorpus-30M to prioritize genes data even after batch effect removal using the ComBat17 or Harmony18
that distinguish cell state. Specifically, this method will deprioritize methods (Extended Data Fig. 4b–f).
ubiquitously highly expressed housekeeping genes by normalizing Although Geneformer is most focused on understanding network
them to a lower rank. Conversely, genes such as transcription factors dynamics rather than cell-level annotations, we further investigated
that may be expressed at low levels when they are expressed but have Geneformer’s performance in cell-type annotation given it is a com-
a high power to distinguish cell state will move to a higher rank within mon application for previously published models. We compared
the encoding (Extended Data Fig. 1c). Furthermore, this rank-based Geneformer to alternative XGBoost7 and deep neural network-based6
approach may be more robust against technical artefacts that may models. These methods train a new model from scratch for each sepa-
systematically bias the absolute transcript counts value whereas the rate tissue using the same supervised learning objective as is used for
overall relative ranking of genes within each cell remains more stable. the final cell-type predictions in that specific tissue. Therefore, these
The rank value encoding of the transcriptome of each single cell then approaches do not take advantage of the large amounts of data avail-
proceeds through six transformer encoder units1,2, each composed of able more broadly that are not specifically labelled for that task. By
a self-attention layer and feed forward neural network layer (Fig. 1c). contrast, Geneformer learns from large-scale unlabelled data during
Pretraining was accomplished using a masked learning objective, which the self-supervised pretraining using a generalizable learning objec-
has been shown in other informational fields1,2 to improve generaliz- tive to gain fundamental knowledge that can then be transferred to a
ability of the foundational knowledge learned during pretraining for multitude of new and diverse fine-tuning tasks. Compared to these
a wide range of downstream fine-tuning objectives. During pretrain- alternative methods, Geneformer boosted cell-type predictions in a
ing, 15% of the genes within each transcriptome were masked, and the variety of tissues, with the gap in performance by accuracy and macro F1
model was trained to predict which gene should be within each masked score increasing as the number of cell-type classes increased, indicating
position in that specific cell state using the context of the remaining that Geneformer was robust in even increasingly complex multiclass
unmasked genes (Extended Data Fig. 1d–f). A principal strength of this prediction applications (Extended Data Figs. 5 and 6).
approach is that it is entirely self-supervised and can be accomplished
on completely unlabelled data, which allows the inclusion of large
Gene dosage sensitivity predictions
amounts of training data without being restricted to samples with
accompanying labels. We implemented recent advances in distributed We next tested whether Geneformer could boost predictions with
graphical processing unit (GPU) training9,10 to allow efficient pretrain- limited data in a diverse set of downstream fine-tuning applications
ing on the large-scale dataset. (Supplementary Table 2). A major challenge of interpreting copy num-
ber variants (CNVs) in genetic diagnosis is determining which genes are
sensitive to changes in their dosage. Although conservation and allele
Context awareness and batch integration
frequency are commonly used to predict dosage sensitivity, these fea-
For each single-cell transcriptome presented to Geneformer, the tures do not vary across cell states and do not capture transcriptional
model embeds each gene into a 256-dimensional space that encodes dynamics that may inform contextual dosage sensitivity indicating
the characteristics of the gene specific to the context of that cell. We which specific tissues would be affected by changes in the dosage of
first tested whether the pretrained Geneformer’s embedding of genes the gene. Using gene sets previously reported19–21 to be dosage-sensitive
was impacted by common batch-dependent technical artefacts. We versus dosage-insensitive, we fine-tuned Geneformer using only 10,000
found that the gene embeddings were robust to sequencing platform11, random single-cell transcriptomes to distinguish dosage-sensitive
preservation method12,13 and individual patient variability14 (Extended versus dosage-insensitive transcription factors. The fine-tuned Gen-
Data Fig. 2a). However, gene embeddings were dependent on the con- eformer significantly boosted the ability to predict dosage sensitivity
text of other genes expressed in the cell, highlighting Geneformer’s compared to alternative methods (area under the receiver operating
context awareness. When we in silico reprogrammed fibroblasts15 characteristic curve (AUC) 0.91) (Fig. 2a and Extended Data Fig. 7a).
by artificially adding OCT4, SOX2, KLF4 and MYC to the front of their Notably, pretraining with larger and more diverse corpuses consistently
rank value encodings, the remaining genes in the transcriptome sig- improved the predictive power in the downstream task despite using
nificantly shifted their embedding towards the iPSC state (Extended the same amount of limited task-specific data for fine-tuning (Fig. 2b).
Data Fig. 2b,c). Embeddings of genes in iPSC-derived myogenic cells16 We then asked whether, without any further training, the fine-tuned
showed similar context awareness with in silico differentiation by model could predict the dosage sensitivity of a recently reported set
618 | Nature | Vol 618 | 15 June 2023
AUC ± standard error by
fivefold cross-validation
False positive rate
of disease genes (Fig. 2c). Collins et al. analysed CNVs from 753,994 We then designed an in silico deletion approach to identify genes
individuals to define genes whose deletion was associated with pri- whose deletion is predicted to have a deleterious effect in that par-
marily neurodevelopmental disease with either high or moderate ticular cell context. We model gene deletion by removing the gene
confidence22. The fine-tuned Geneformer model correctly predicted from the rank value encoding of the cell and quantifying the impact
the high-confidence genes to be dosage sensitive in the specific con- on the embeddings of the remaining genes in the encoding. To test
text of fetal cerebral cells with 96% concordance with the original this approach, we performed in silico deletion in fetal cardiomyo-
study. The moderate-confidence genes reported by the authors were cytes23 using the pretrained Geneformer without any fine-tuning. In
a much more permissive set (0.15–0.85 score versus high-confidence silico deletion of known cardiomyopathy and structural heart disease
score cutoff greater than 0.85). The fine-tuned Geneformer predicted genes had a significantly larger effect than the control set of known
moderate-confidence genes to be dosage sensitive in fetal cerebral hyperlipidaemia genes, which are expressed in cardiomyocytes and
cells with 84% concordance with the original study. Interestingly, related to heart disease but whose phenotype affects cell types other
although the high-confidence genes, which may have a stronger effect, than cardiomyocytes (Fig. 2d). In silico deletion of genes linked by a
were predicted by Geneformer to be dosage sensitive at similar rates previous genome-wide association study24 (GWAS) to cardiac magnetic
in fetal cerebral (96%) and other cells (95%), the predicted dosage resonance imaging (MRI) traits relevant to cardiac disease also had
sensitivity of the moderate-confidence genes seemed to be more a larger effect compared to the control set (Extended Data Fig. 7b).
context specific. The moderate-confidence genes were predicted to Overall, genes whose deletion was predicted to have the most delete-
be dosage sensitive at a higher rate in fetal cerebral cells compared rious effect on cardiomyocytes were significantly enriched for human
to neurons across any adult or developmental timepoint, consistent phenotypes including cardiomyopathy and abnormal myocardial mor-
with the association of these genes with predominantly neurodevel- phology (Supplementary Tables 3 and 4). Among the top 25 deleted
opmental phenotypes in which adult neurons may be less relevant. genes with the most significant effect were transcription factors known
They were predicted to be dosage sensitive at an even lower rate in to regulate myocardial development (for example, FOXM1; refs. 25,26)
random cells from any tissue, highlighting the context awareness and entirely new dosage-sensitive gene candidates such as TEAD4
of Geneformer. (Supplementary Table 3). Experimental validation demonstrated
Nature | Vol 618 | 15 June 2023 | 619
etar
evitisop
eurT
Geneformer dosage sensitivity predictions in
random versus neuronal cell types for newly
reported neurodevelopmental disease genes
100
Random
80 Neurons
60 Fetal cerebrum
40
20
0
High Moderate
Confidence
(PIP ≥ 0.85) (PIP ≥ 0.15)
Gene sets from ref. 22
1.0 Diverse 0.5 *
Non-diverse
0.9
0
0.8
–0.5
0.7
–1.0
0.6
0.5 –1.5
104
remrofeneG egatnecrep ecnadrocnoc
Geneformer: 0.91 ± 0.02
SVM-r: 0.75 ± 0.08
RF-r: 0.72 ± 0.06
LR-r: 0.65 ± 0.05
SVM-c: 0.67 ± 0.09
RF-c: 0.67 ± 0.07
LR-c: 0.61 ± 0.05
6L: 0.41 ± 0.05
4L: 0.41 ± 0.04
3L: 0.51 ± 0.07
1L: 0.56 ± 0.07
Impact of size and diversity of pretraining corpus
No. of cells in pretraining corpus
CUA
ksat
maertsnwoD
sserts
elitcartnoC
)lortnoc
susrev
egnahc-dlof
gol( 2
a c
Dosage sensitive versus insensitive TFs
1.0
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1.0
Engineered cardiac
b d e microtissues
Cardiomyocyte embeddings
In silico deleted genes
Hyperlipidaemia
Structural heart disease *
Cardiomyopathy *
Validation *
105 106 107 0.980 0.985 0.990 0.995 1.000 Control TEAD4
Cosine similarity Target
(← more deleterious effect)
Fig. 2 | Geneformer boosted predictions of gene dosage sensitivity with either high- or moderate-confidence gene sets with the indicated posterior
limited data. a, A receiver operating characteristic curve (ROC curve) of inclusion probability (PIP) scores. d, In silico deletion of genes associated with
Geneformer fine-tuned to distinguish dosage-sensitive versus dosage- disease driven by cardiomyocyte pathology (cardiomyopathy and structural
insensitive transcription factors using limited data (10,000 cells) compared heart disease) had a more deleterious effect on cardiomyocyte embeddings
to alternative methods: support vector machine (SVM), random forest (RF) compared to control cardiac disease genes expressed in cardiomyocytes but
or logistic regression (LR) trained on gene ranks (-r) or counts (-c) or non- whose pathology occurs in non-cardiomyocyte cell types (hyperlipidaemia).
pretrained attention-based models with the same architecture as Geneformer Validation with experimental data from patients with cardiomyopathy (Fig. 6)
(6 layers (L)) or shallower (4, 3 or 1L) with retained depth-to-width aspect ratios. demonstrated that in silico deletion of genes distinguishing the cardiomyopathy
b, Larger and more diverse pretraining corpuses improved predictive potential state was also predicted to be more deleterious than in silico deletion of control
in downstream task of distinguishing dosage-sensitive versus dosage-insensitive genes. (*P < 0.05 Wilcoxon, false discovery rate (FDR)-corrected). e, Contractile
transcription factors using the same limited task-specific data (10,000 cells). stress (force per unit area) of cardiac microtissues derived from wild-type (WT)
Diverse corpuses were randomly sampled from Genecorpus-30M, whereas iPSCs, exposed to either control treatment or guides promoting CRISPR-
non-diverse corpuses were randomly sampled from an oesophageal dataset45. mediated knockout of Geneformer-predicted dosage-sensitive gene TEAD4.
c, Fine-tuned Geneformer’s contextual dosage sensitivity predictions in (Control n = 12, TEAD4 n = 11; P < 0.05 Wilcoxon; points are replicates.) In d and e,
(1) random cell types, (2) neurons (including adult) and (3) fetal cerebrum for centre line, median; box limits, upper and lower quartiles; whiskers, 1.5×
neurodevelopmental disease genes newly reported by ref. 22. Authors reported interquartile range.
Article
that CRISPR-mediated knockout of candidate TEAD4 in iPSC-derived long- versus short-range transcription factors using only single-cell
cardiac microtissues caused a significant reduction in their ability to transcriptomes from about 34,000 cells undergoing iPSC to cardiomyo-
generate contractile stress (force per unit area) (Fig. 2e and Extended cyte differentiation11 with no associated ChIP–seq or genomic distance
Data Fig. 7c). TEAD4 is a transcription factor involved in the Hippo data. Again, Geneformer significantly boosted the ability to predict
signalling pathway27, and future work is warranted to further examine the regulatory range of transcription factors compared to alternative
its role in cardiac development. methods, whose predictions were near random (Fig. 3d and Extended
Data Fig. 8d). Thus, fine-tuning the pretrained Geneformer model was
able to improve predictions even for this higher-order transcription
Chromatin dynamics predictions
factor property of regulatory range, a particularly challenging char-
Bivalent chromatin structure is known to mark key developmental acteristic to infer from transcriptional data alone.
genes in embryonic stem cells (ESCs), maintaining their promoters
poised for activation28. Bivalent domains consist of large regions of
Network dynamics predictions
H3K27me3 harbouring smaller regions of H3K4me3. We fine-tuned
Geneformer to distinguish bivalently marked genes from those whose Determining the hierarchy in gene networks enables the design of
promoters were unmethylated or marked solely by H3K4me3 using therapies targeting normalization of core regulatory elements that
transcriptomes from about 15,000 ESCs29. The labelled gene set used drive the disease process, rather than correction of peripheral down-
for this fine-tuning included only genes found in 56 conserved regions stream effectors that may not be disease modifying. We previously
of the genome, as previously reported28. Geneformer significantly mapped the NOTCH1 (N1)-dependent gene network governing cardiac
boosted the ability to predict bivalently marked genes compared to valve disease and identified central regulatory nodes whose correction
alternative methods (AUC 0.93 and 0.88; bivalent versus unmethylated had broad restorative impact on the network at large4,5. Mapping the
or H3K4me3-only, respectively) (Fig. 3a,b and Extended Data Fig. 7d,e). network hierarchy required large amounts of transcriptional perturba-
Furthermore, predictions were generalizable to the remainder of the tion data from patient-specific cells with isogenic controls to learn the
genome that was excluded from fine-tuning (Fig. 3c and Extended Data connections between genes.
Fig. 8a–c). Thus, by fine-tuning Geneformer using solely transcriptional We tested whether Geneformer could be fine-tuned to distinguish
data with only 56 labelled loci in about 15,000 ESCs, the model could central versus peripheral factors within the N1-dependent gene net-
predict the results of more recent studies30 that included genome-wide work using only single-cell transcriptional data from about 30,000
profiling of bivalent domains. normal endothelial cells (ECs) from the Heart Atlas32 without any per-
Determining the genomic distances over which transcription turbation data. Again, Geneformer significantly boosted the ability
factor binding influences downstream expression is valuable for to predict central versus peripheral factors compared to alternative
interpreting regulatory variants and inferring target genes from methods (AUC 0.81) (Fig. 4a and Extended Data Fig. 8e). Furthermore,
transcription factor genome occupancy data. Others previously sys- fine-tuning the pretrained Geneformer on the Heart Atlas ECs32 was able
tematically integrated thousands of transcription factor-binding and to distinguish N1 downstream targets from non-targets without any
histone-modification profiles assayed by chromatin immunoprecipita- perturbation data, further demonstrating the ability of the model to
tion sequencing (ChIP–seq) with thousands of gene expression profiles encode key features of gene network dynamics and again significantly
to identify two classes of transcription factor with distinct ranges of boosting predictions compared to alternative methods (Fig. 4b and
regulatory influence31. We fine-tuned Geneformer to distinguish these Extended Data Fig. 9a).
620 | Nature | Vol 618 | 15 June 2023
etar
evitisop
eurT
Bivalent versus Lys4-only methylated
(train on 56 loci, predict genome-wide)
AUC ± standard error by
fivefold cross-validation
Geneformer: 0.93 ± 0.07
SVM-r: 0.53 ± 0.08
RF-r: 0.54 ± 0.10
LR-r: 0.69 ± 0.10
SVM-c: 0.51 ± 0.06
RF-c: 0.51 ± 0.07 AUC
LR-c: 0.72 ± 0.05 Geneformer: 0.78
AUC ± standard error by
fivefold cross-validation
Geneformer: 0.88 ± 0.09
SVM-r: 0.74 ± 0.09
RF-r: 0.70 ± 0.10
LR-r: 0.63 ± 0.09
SVM-c: 0.74 ± 0.09
RF-c: 0.70 ± 0.10
LR-c: 0.65 ± 0.07
etar
evitisop
eurT
AUC ± standard error by
fivefold cross-validation
Geneformer: 0.74 ± 0.08
SVM-r: 0.49 ± 0.09
RF-r: 0.48 ± 0.07
LR-r: 0.59 ± 0.12
SVM-c: 0.49 ± 0.09
RF-c: 0.51 ± 0.08
LR-c: 0.58 ± 0.13
etar
evitisop
eurT
False positive rate
etar
evitisop
eurT
a c
Bivalent versus non-methylated
1.0 1.0
0.8 0.8
0.6 0.6
0.4 0.4
0.2 0.2
0 0
0 0.2 0.4 0.6 0.8 1.0 0 0.2 0.4 0.6 0.8 1.0
False positive rate
b d
Bivalent versus Lys4-only methylated Long versus short-range TFs
1.0 1.0
0.8 0.8
0.6 0.6
0.4 0.4
0.2 0.2
0 0
0 0.2 0.4 0.6 0.8 1.0 0 0.2 0.4 0.6 0.8 1.0
False positive rate False positive rate
Fig. 3 | Geneformer boosted predictions of chromatin dynamics with predictions of bivalent versus Lys4-only-methylated genes after fine-tuning
limited data. a,b, ROC curve of Geneformer fine-tuned to distinguish bivalent on only 56 loci as in b. d, ROC curve of Geneformer fine-tuned to distinguish
versus non-methylated (a) or bivalent versus Lys4-only-methylated (b) genes long-range versus short-range transcription factors (TFs) using limited data
in 56 conserved loci from ref. 28 using limited data (about 15,000 ESCs), (about 38,000 cells from iPSC to cardiomyocyte differentiation), compared to
compared to alternative methods. c, ROC curve of Geneformer’s genome-wide alternative methods. (Alternative methods described in Fig. 2).
1.0 1.0
0.8 0.8
0.6 0.6
0.4 0.4
0.2 0.2
0 0
1.0
0.8
0.6
0.4
0.2
0
To investigate the threshold for minimal data needed for fine-tuning, of Geneformer’s six layers has four attention heads that are meant to
we fine-tuned the pretrained Geneformer with progressively smaller learn in an unsupervised manner to pay attention to distinct classes of
numbers of normal ECs from the Heart Atlas32 to distinguish central genes to jointly improve predictions without previous knowledge of
versus peripheral factors within the N1-dependent gene network. We the biological function of any gene.
found that nearly equivalent predictive potential was retained even When examining the attention weights in aortic ECs14, we found
when reducing the fine-tuning data to only 5,000 ECs (Fig. 4c). Then, that 20% of attention heads significantly attended transcription
to determine whether Geneformer could generate meaningful pre- factors more than other genes, indicating that specific attention heads
dictions using an even more miniscule number of fine-tuning train- learned, in an entirely self-supervised manner, the relative importance of
ing examples when the task-specific data were more relevant to the transcription factors in distinguishing cell states (Fig. 4e). Furthermore,
learning objective, we fine-tuned the pretrained Geneformer using specific attention heads significantly attended central regulatory nodes
only 884 ECs from healthy versus dilated aortas14. Interestingly, Gen- to a greater degree than peripheral genes within N1-dependent network
eformer was able to distinguish central versus peripheral factors in the in ECs (Extended Data Fig. 9c). Concordantly, these centrality-driven
N1-dependent network with fine-tuning on this very minimal data to a attention heads consistently attended to a significantly greater degree
better degree than the predictions of alternative methods trained on the highest ranked genes in each cell’s unique rank value encoding in
the larger dataset of about 30,000 ECs32, demonstrating the strength aortic ECs, smooth muscle cells, T cells, and macrophage, monocyte and
of pretraining in enabling predictions from increasingly limited data dendritic cells (which each have different sets of highest ranked genes
(Fig. 4d and Extended Data Fig. 9b). More than twice as many general on the basis of cell-type context) (Extended Data Fig. 9d).
cardiac ECs were needed to gain similar predictive potential as was pos- Interestingly, attention heads in the earliest layers were consistently
sible from fine-tuning with the more relevant data from healthy versus the most diverse in terms of gene ranks they attended, suggesting that
dilated aortas, suggesting that the minimum amount of fine-tuning data the model initially orients to the observed cell state through a joint
needed is dependent on both the specific application and relevance survey of distinct portions of the input space. The middle layers were
of the data to that task. most broad in terms of gene ranks they attended, and the final layers
were dominated by centrality-driven attention heads that focused on
the highest ranked genes that uniquely define each cell state (Extended
Pretraining encoded network hierarchy
Data Fig. 9c,d).
To investigate how the model was learning network dynamics dur-
ing the pretraining stage, we examined the pretrained Geneformer
In silico gene network analysis
attention weights. The trained attention weights of the model for each
gene reflect (1) which genes that gene pays attention to and (2) which Given that the gene embeddings reflect the joint output of the attention
genes pay attention to that gene. These attention weights are itera- weights of the network, we tested whether the pretrained Geneformer
tively optimized during training to generate gene embeddings that already encoded network connections between transcription factors
best inform the correct answer for the given learning objective. Each and their targets before fine-tuning. We determined the genes whose
Nature | Vol 618 | 15 June 2023 | 621
etar
evitisop
eurT
N1 network central versus peripheral
AUC ± standard error by
fivefold cross-validation
Geneformer: 0.81 ± 0.06
SVM-r: 0.65 ± 0.08
RF-r: 0.68 ± 0.08
LR-r: 0.59 ± 0.12
SVM-c: 0.68 ± 0.08
RF-c: 0.69 ± 0.08
LR-c: 0.60 ± 0.06
N1 network central versus peripheral
(trained on only 884 ECs)
etar
evitisop
eurT
N1 activated versus non-target
AUC ± standard error by
fivefold cross-validation
Geneformer: 0.81 ± 0.07
SVM-r: 0.60 ± 0.06
RF-r: 0.58 ± 0.06
LR-r: 0.60 ± 0.02
SVM-c: 0.53 ± 0.05
RF-c: 0.61 ± 0.04
LR-c: 0.62 ± 0.03
etar
evitisop
eurT
1.0
0.8
0.6
0.4
0.2
Geneformer: 0.74 ± 0.05
0
Attention heads
sreyaL
0
1
2
3
4
5
0
noitnetta
rehgiH
Transcription factors
* *
* * *
AUC ± standard error
etar
evitisop
eurT
a b
0 0.2 0.4 0.6 0.8 1.0 0 0.2 0.4 0.6 0.8 1.0
False positive rate False positive rate
c N1 network central versus peripheral ROC d e
with varying amounts of fine-tuning data
AUC ± standard error by
fivefold cross-validation
30,000 ECs: 0.81 ± 0.06
10,000 ECs: 0.81 ± 0.06
5,000 ECs: 0.80 ± 0.06
2,500 ECs: 0.77 ± 0.09
2,000 ECs: 0.73 ± 0.09
1,500 ECs: 0.64 ± 0.12
1,000 ECs: 0.59 ± 0.16
1 2 3
0 0.2 0.4 0.6 0.8 1.0 0 0.2 0.4 0.6 0.8 1.0
False positive rate False positive rate
Fig. 4 | Geneformer encoded gene network hierarchy. a, ROC curve of peripheral genes within the N1-dependent gene network using increasingly
Geneformer fine-tuned to distinguish central versus peripheral genes within limited but more relevant data (884 ECs from healthy or dilated aortas).
the N1-dependent gene network using limited data (about 30,000 ECs), AUC was higher than alternative methods trained on a larger dataset of
compared to alternative methods. b, ROC curve of Geneformer fine-tuned to about 30,000 ECs (Fig. 4a). e, Pretrained Geneformer attention weights of
distinguish N1-activated versus non-target genes using limited data (about transcription factors indicated that the model learned in a completely self-
30,000 ECs), compared to alternative methods. c, ROC curve of Geneformer supervised way the relative importance of transcription factors, which were
fine-tuned to distinguish central versus peripheral genes within the more highly attended than other genes in 20% of attention heads (P < 0.05,
N1-dependent gene network using increasingly limited data (1,000–30,000 Wilcoxon rank sum, FDR-corrected) and were more attended in earlier layers
ECs). d, ROC curve of Geneformer fine-tuned to distinguish central versus (P < 0.05, Wilcoxon rank sum). (Alternative methods described in Fig. 2).
Article
Effect of in silico deletion of GATA4 on gene embeddings Effect of in silico deletion of GATA4 and TBX5 on gene embeddings
1.00
Housekeeping
0.98
NOTCH1 targets
0.96
*
NKX2-5 targets
0.94 In silico deleted genes
Indirect GATA4
TBX5
Direct * 0.92 GATA4 and TBX5
* *
GATA4/TBX5
Cosine similarity cobound targets
(←more deleterious effect)
embeddings in fetal cardiomyocytes23 were most impacted by in silico dilated cardiomyopathy, which were enriched for pathways involved
deletion of GATA4, a known congenital heart disease gene. In silico in muscle contraction38 and mitochondrial39 function.
deletion of GATA4 had a significantly higher effect on genes known to Then, we performed in silico treatment analysis in cardiomyocytes
be most significantly dysregulated by GATA4 variants in a previously from hypertrophic or dilated cardiomyopathy patients to determine
reported iPSC disease model of GATA4-related heart defects33 (Extended whether inhibition or activation of specific pathways would shift the
Data Fig. 9e). Notably, direct GATA4 targets (as defined by ChIP–seq33) cell embeddings back towards the non-failing heart state (Fig. 6e,
were significantly more impacted by in silico deletion of GATA4 in fetal Extended Data Fig. 10d and Supplementary Tables 12–15). Top enriched
cardiomyocytes compared to indirect targets (Fig. 5a). Analogously, pathways for hypertrophic cardiomyopathy pointed to candidate
in silico deletion of TBX5, another known congenital heart disease cardiomyocyte-specific therapeutic targets including ADCY5, dis-
gene, in fetal cardiomyocytes23 more significantly impacted its direct ruption of which is associated with longevity and protection against
targets (as defined by ChIP–seq34) compared to indirect targets and cardiomyopathy in mouse models40, as well as druggable targets41
housekeeping genes (Extended Data Fig. 9f). These data suggest that in including SRPK3, a downstream effector of MEF2 (ref. 42), which is
silico perturbation can be applied to model gene network connections. known to play a critical role in myocardial cell hypertrophy43.
Interestingly, the GATA4 variant studied in the iPSC disease model We then performed experimental validation to determine whether
disrupts the interaction of GATA4 with its binding partner, transcription inhibition of Geneformer-predicted therapeutic candidates for dilated
factor TBX5 (ref. 33). We tested whether our in silico deletion approach cardiomyopathy could improve cardiomyocyte function in an experi-
could model the effect of deleting these two genes in combination mental model of the disease. Titin (TTN) truncating mutations are the
(Fig. 5b). Indeed, in silico deletion of GATA4 or TBX5 alone had a sig- leading cause of dilated cardiomyopathy in humans and are found in
nificantly more deleterious effect on their known cobound targets33 about 20% of affected patients36. iPSC-derived cardiac microtissues har-
compared to housekeeping genes. Furthermore, in silico deletion of bouring a truncating variant (TTN+/−) in the A-band are known to exhibit
both GATA4 and TBX5 in combination had an even greater impact on reduced contractile stress compared to isogenic TTN+/+ controls36.
their known cobound targets than the sum of their individual in silico Strikingly, CRISPR-mediated knockout of both Geneformer-predicted
deletion, suggesting that Geneformer recognized their cooperative targets GSN and PLN in the TTN+/− cells significantly improved the con-
action at these cobound targets. tractile stress of the TTN+/− cardiac microtissues, validating these genes
as promising candidate therapeutic targets for this disease (Fig. 6f,g
and Extended Data Fig. 10e). These findings provide experimental
In silico treatment analysis
validation in support of the utility of Geneformer as a tool for discovery
We next tested whether our in silico perturbation strategy could be of candidate therapeutic targets in human disease.
applied to model human disease and reveal candidate therapeutic
targets (Fig. 6a). First, we fine-tuned Geneformer to distinguish car-
diomyocytes35 from non-failing hearts (n = 9) or hearts affected by Discussion
hypertrophic (n = 11) or dilated (n = 9) cardiomyopathy with an overall In sum, we developed a context-aware deep learning model, Gen-
out-of-sample accuracy of 90% (Fig. 6b and Extended Data Fig. 10a). eformer, pretrained on large-scale transcriptomic data to enable
We then determined the genes whose in silico deletion or activation predictions in settings with limited data. Through the observation
in cardiomyocytes from non-failing hearts significantly shifted the of a vast number of cell states during the pretraining process, Gen-
fine-tuned Geneformer cell embeddings towards the hypertrophic eformer gained a fundamental understanding of network dynamics,
or dilated cardiomyopathy states (Fig. 6c,d, Extended Data Fig. 10b,c encoding network hierarchy in the attention weights of the model
and Supplementary Tables 5–11). Overall, the model identified 447 in a completely self-supervised manner. Geneformer’s ability to pre-
genes whose loss was predicted to shift cardiomyocytes towards the dict dosage-sensitive disease genes through the context-aware in
hypertrophic cardiomyopathy state, which were enriched for pathways silico deletion approach represents a valuable asset for interpreta-
including Titin binding36 and sarcomere organization37 known to impact tion of genetic variants, including prioritization of GWAS hits driving
hypertrophic cardiomyopathy pathogenesis. The model identified complex traits, and the specific tissues they are expected to affect.
478 genes whose loss was predicted to shift cardiomyocytes towards Experimental validation of a dosage-sensitive gene candidate in fetal
622 | Nature | Vol 618 | 15 June 2023
4ATAG stegrat
ytiralimis
enisoC
)tceffe
suoireteled
erom
←(
a b
0.93 0.94 0.95 0.96 0.97 0.98 0.99 1.00 Housekeeping
Fig. 5 | In silico deletion revealed network connections. a, In silico deletion deletion of GATA4 or TBX5 alone was significantly more deleterious to
of GATA4 was significantly more deleterious to previously reported GATA4 previously reported GATA4/TBX5 cobound targets33 than to housekeeping
direct targets33 than to housekeeping genes, previously reported NOTCH1 genes; in silico deletion of the combination of GATA4 and TBX5 was even more
targets4, previously reported NKX2-5 targets46 or GATA4 indirect targets33 deleterious to cobound targets, significantly more than to housekeeping
(*P < 0.05 Wilcoxon, FDR-corrected; centre line, median; box limits, upper and genes and significantly more than the sum of the effect of GATA4 or TBX5 alone
lower quartiles; whiskers, 1.5× interquartile range; points, outliers). b, In silico on cobound targets (*P < 0.05 Wilcoxon, FDR-corrected).
Confidence
cardiomyocytes, TEAD4, supports the utility of Geneformer for driving Geneformer predicted candidate therapeutic targets whose experi-
biological insights in human development. Applied to disease model- mental targeting in an iPSC disease model led to significant functional
ling of cardiomyopathy using a limited number of patient samples, improvement. In silico treatment analysis using limited data may thus
Nature | Vol 618 | 15 June 2023 | 623
600,93
=
sllec
fo
.oN 985,39
=
sllec
fo
.oN
Predicted
Phenotype
Non-failing
Hypertrophic Non-failing
Dilated Hypertrophic
Dilated
Embedding
dimension
activation
0
Titin binding Mitochondrial function
Sarcomere organization Muscle contraction
Response to hypoxia Thyroid signalling No. of embedding dimensions = 256
SMAD binding Beta-catenin binding
Hypertrophic
cardiomyopathy
Distribution of candidate therapeutic targets
Shift towards non-failing
morf
yawa
tfihS
yhtapoymoidrac
detalid
ytisneD
)401
= seneg
fo .oN(
Disease modelling
x
x
Non-failing
Fine-tuned Geneformer out of sample predictions
Phenotype
Actual
Overlap of genes defining each cardiomyopathy state
Dilated
cardiomyopathy
lanoisnemid-652 ecaps
gniddebme
In silico treatment of HCM In silico treatment of DCM
Hypertrophic HHyyppeerrttrroopphhiicc Hypertrophic
x
x x
x
Non-failing Non-failing
Dilated Dilated
sserts
elitcartnoC
)lortnoc
susrev
egnahc-dlof
gol( 2
Control PLN GSN ESRRG HMGB1
Target
ecrof
elitcartnoC
)–/+NTT
susrav
egnahc-dlof
gol( 2
a
Dilated
b c
5 0 –5
0.5 1.0
d
250 197 281
g Engineered cardiac microtissues
*
1.5
e f Engineered cardiac microtissues
1.5 1.0 *
–0.01 0.5 * 0.5
–0.02 0 0
–0.03
–0.5
–0.04 –0.5
–0.05 –1.0
0.01 0.02 WT TTN+/–
Genotype
Fig. 6 | In silico treatment revealed candidate therapeutic targets. whose in silico deletion in cardiomyocytes from non-failing hearts
a, Fine-tuning Geneformer to distinguish cardiomyocytes from non-failing significantly shifted the fine-tuned Geneformer cell embeddings towards the
hearts or hearts affected by hypertrophic or dilated cardiomyopathy hypertrophic or dilated cardiomyopathy states and gene ontology terms
(HCM and DCM) defines the embedding position of each cell state. Then, enriched for each state. e, Distribution of mean embedding shift in response
disease modelling (left) can be performed by in silico deleting or activating to in silico deletion of candidate therapeutic targets in cardiomyocytes from
random genes within non-failing cardiomyocytes to define the random hypertrophic cardiomyopathy (n = 104 genes). f, Contractile force of cardiac
distribution (grey cloud) and thereby identify genes whose in silico deletion or microtissues derived from WT iPSCs or iPSCs with a TTN truncating mutation
activation shifts the embedding significantly towards either the hypertrophic modelling dilated cardiomyopathy (WT n = 11, TTN+/− n = 12, *P < 0.05
or dilated cardiomyopathy state. The reverse approach is taken for in silico Wilcoxon). g, Contractile stress (force per unit area) of cardiac microtissues
treatment analysis (centre and right). b, Out-of-sample predictions of derived from TTN+/− iPSCs exposed to either control treatment or guides
Geneformer fine-tuned to distinguish cardiomyocytes from non-failing hearts promoting CRISPR-mediated knockout of Geneformer-predicted therapeutic
or hearts affected by hypertrophic or dilated cardiomyopathy. Accuracy targets. (TTN+/− + control treatment n = 22, TTN+/− + CRISPR guides targeting
90%; precision 82%; recall 87%. (Training data: non-failing n = 9, hypertrophic knockout of PLN n = 22, GSN n = 7, ESRRG n = 9 or HMGB1 n = 11; P < 0.05
n = 11, dilated n = 9, total 93,589 cells; out-of-sample data: non-failing n = 4, Wilcoxon, FDR-corrected). In f and g, centre line, median; box limits, upper
hypertrophic n = 4, dilated n = 2, total 39,006 cells). c, Hierarchical clustering and lower quartiles; whiskers, 1.5× interquartile range; points, experimental
of fine-tuned Geneformer cardiomyocyte cell embeddings. d, Overlap of genes replicates.
Article
enable therapeutic discovery in innumerable diseases that have been 15. Xing, Q. R. et al. Diversification of reprogramming trajectories revealed by parallel
previously impeded by limited data because they are rare or affect single-cell transcriptome and chromatin accessibility sequencing. Sci. Adv. 6, 463–474
(2020).
clinically inaccessible tissue. 16. Guo, D. et al. iMyoblasts for ex vivo and in vivo investigations of human myogenesis and
Furthermore, we found that pretraining with larger and more diverse disease modeling. eLife 11, e70341 (2022).
17. Zhang, Y., Parmigiani, G. & Johnson, W. E. ComBat-seq: batch effect adjustment for
corpuses consistently improved Geneformer’s predictive power, in
RNA-seq count data. NAR Genom. Bioinform. 2, lqaa078 (2020).
agreement with observations that large-scale pretraining allows train- 18. Korsunsky, I. et al. Fast, sensitive and accurate integration of single-cell data with Harmony.
ing of deeper models that ultimately have greater predictive potential in Nat. Methods 16, 1289–1296 (2019).
19. Lek, M. et al. Analysis of protein-coding genetic variation in 60,706 humans. Nature 536,
fields including natural language understanding, computer vision and
285–291 (2016).
mathematical problem-solving44. Furthermore, exposure to hundreds 20. Shihab, H. A., Rogers, M. F., Campbell, C. & Gaunt, T. R. HIPred: an integrative approach to
of experimental datasets during pretraining also seemed to promote predicting haploinsufficient genes. Bioinformatics 33, 1751–1757 (2017).
21. Ni, Z., Zhou, X. Y., Aslam, S. & Niu, D. K. Characterization of human dosage-sensitive
robustness to batch-dependent technical artefacts and individual vari-
transcription factor genes. Front. Genet. 10, 1208 (2019).
ability that commonly impact single-cell analyses in biology. These find- 22. Collins, R. L. et al. A cross-disorder dosage sensitivity map of the human genome. Cell
ings suggest that as the amount of publicly available transcriptomic 185, 3041–3055 (2022).
23. Cao, J. et al. A human cell atlas of fetal gene expression. Science 370, 808 (2020).
data continues to expand, future models pretrained on even larger-scale
24. Pirruccello, J. P. et al. Analysis of cardiac magnetic resonance imaging in 36,000
corpuses may open opportunities to achieve meaningful predictions individuals yields genetic insights into dilated cardiomyopathy. Nat. Commun. 11, 2254
in even more elusive tasks with increasingly limited task-specific data. (2020).
25. Bolte, C. et al. Expression of Foxm1 transcription factor in cardiomyocytes is required for
Overall, Geneformer represents a pretrained deep learning model
myocardial development. PLoS ONE 6, e22217 (2011).
whose fundamental understanding of network dynamics can now be 26. Bolte, C. et al. Postnatal ablation of Foxm1 from cardiomyocytes causes late onset cardiac
democratized to a broad range of downstream applications to accel- hypertrophy and fibrosis without exacerbating pressure overload-induced cardiac
remodeling. PLoS ONE 7, e48713 (2012).
erate discovery of key network regulators and candidate therapeutic
27. Currey, L., Thor, S. & Piper, M. TEAD family transcription factors in development and
targets in settings with limited data. disease. Development 148, dev196675 (2021).
28. Bernstein, B. E. et al. A bivalent chromatin structure marks key developmental genes in
embryonic stem cells. Cell 125, 315–356 (2006).
29. Franzén, O., Gan, L.-M. & Björkegren, J. L. M. PanglaoDB: a web server for exploration of
Online content
mouse and human single-cell RNA sequencing data. Database 2019, baz406 (2019).
Any methods, additional references, Nature Portfolio reporting summa- 30. Pan, G. et al. Whole-genome analysis of histone H3 lysine 4 and lysine 27 methylation in
human embryonic stem cells. Cell Stem Cell 1, 299–312 (2007).
ries, source data, extended data, supplementary information, acknowl-
31. Chen, C. H. et al. Determinants of transcription factor regulatory range. Nat. Commun. 11,
edgements, peer review information; details of author contributions 2472 (2020).
and competing interests; and statements of data and code availability 32. Litviňuková, M. et al. Cells of the adult human heart. Nature 588, 455–472 (2020).
33. Ang, Y. S. et al. Disease model of GATA4 mutation reveals transcription factor
are available at https://doi.org/10.1038/s41586-023-06139-9.
cooperativity in human cardiogenesis. Cell 167, 1734–1749 (2016).
34. Kathiriya, I. S. et al. Modeling human TBX5 haploinsufficiency predicts regulatory
networks for congenital heart disease. Dev. Cell 56, 292–309 (2021).
1. Vaswani, A. et al. Attention is all you need. Preprint at https://doi.org/10.48550/ 35. Chaffin, M. et al. Single-nucleus profiling of human dilated and hypertrophic
arXiv.1706.03762 (2017). cardiomyopathy. Nature 608, 174–180 (2022).
2. Devlin, J., Chang, M. W., Lee, K. & Toutanova, K. BERT: pre-training of deep bidirectional 36. Hinson, J. T. et al. Titin mutations in iPS cells define sarcomere insufficiency as a cause of
transformers for language understanding. In Proc. 2019 Conference North American dilated cardiomyopathy. Science 349, 982–986 (2015).
Chapter of the Association for Computational Linguistics: Human Language Technologies 37. Seidman, C. E. & Seidman, J. G. Identifying sarcomere gene mutations in hypertrophic
Vol. 1 (eds Burstein, J. et al.) 4174–4186 (Association for Computational Linguistics, 2019). cardiomyopathy: a personal history. Circ. Res. 108, 743–750 (2011).
3. He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. In Proc. 38. Kamisago, M. et al. Mutations in sarcomere protein genes as a cause of dilated
IEEE Computer Society Conference on Computer Vision and Pattern Recognition 770–778 cardiomyopathy. New Engl. J. Med. 343, 1688–1696 (2000).
(IEEE, 2016). 39. Ramaccini, D. et al. Mitochondrial function and dysfunction in dilated cardiomyopathy.
4. Theodoris, C. V. et al. Human disease modeling reveals integrated transcriptional and Front. Cell Dev. Biol. https://doi.org/10.3389/fcell.2020.624216 (2021).
epigenetic mechanisms of NOTCH1 haploinsufficiency. Cell 160, 1072–1086 (2015). 40. Ho, D., Yan, L., Iwatsubo, K., Vatner, D. E. & Vatner, S. F. Modulation of β-adrenergic
5. Theodoris, C. V. et al. Network-based screen in iPSC-derived cells reveals therapeutic receptor signaling in heart failure and longevity: targeting adenylyl cyclase type 5. Heart
candidate for heart valve disease. Science 371, eabd0724 (2021). Fail. Rev. 15, 495–512 (2010).
6. Shao, X. et al. ScDeepSort: a pre-trained cell-type annotation method for single-cell 41. Wagner, A. H. et al. DGIdb 2.0: mining clinically relevant drug-gene interactions. Nucleic
transcriptomics using deep learning with a weighted graph neural network. Nucleic Acids Acids Res. 44, D1036–D1044 (2016).
Res. 49, e122 (2021). 42. Nakagawa, O. et al. Centronuclear myopathy in mice lacking a novel muscle-specific
7. Lieberman, Y., Rokach, L. & Shay, T. CaSTLe—classification of single cells by transfer protein kinase transcriptionally regulated by MEF2. Genes Dev. 19, 2066–2077 (2005).
learning: harnessing the power of publicly available single cell RNA sequencing 43. Akazawa, H. & Komuro, I. Roles of cardiac transcription factors in cardiac hypertrophy.
experiments to annotate new experiments. PLoS ONE 13, e0205499 (2018). Circ. Res. 92, 1079–1088 (2003).
8. Lin, T., Wang, Y., Liu, X. & Qiu, X. A survey of transformers. Preprint at https://doi.org/ 44. Henighan, T. et al. Scaling laws for autoregressive generative modeling. Preprint at
10.48550/arXiv.2106.04554 (2021). https://doi.org/10.48550/arXiv.2010.14701 (2020).
9. Ren, J. et al. ZeRO-offload: democratizing billion-scale model training. In Proc. 2021 45. Madissoon, E. et al. ScRNA-seq assessment of the human lung, spleen, and esophagus
USENIX Annual Technical Conference 551–564 (USENIX, 2021). tissue stability after cold preservation. Genome Biol. 21, 1 (2019).
10. Rajbhandari, S., Rasley, J., Ruwase, O. & He, Y. Zero: memory optimizations toward 46. Anderson, D. J. et al. NKX2-5 regulates human cardiomyogenesis via a HEY2 dependent
training trillion parameter models. In International Conference for High Performance transcriptional network. Nat. Commun. 9, 1373 (2018).
Computing, Networking, Storage and Analysis 1–16 (IEEE, 2020).
11. Selewa, A. et al. Systematic comparison of high-throughput single-cell and single- Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
nucleus transcriptomes during cardiomyocyte differentiation. Sci. Rep. 10, 1535 (2020). published maps and institutional affiliations.
12. 10x Genomics Datasets https://www.10xgenomics.com/resources/datasets/
frozen-pbm-cs-donor-a-1-standard-1-1-0. Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this
13. 10X Genomics Datasets https://www.10xgenomics.com/resources/datasets/fresh- article under a publishing agreement with the author(s) or other rightsholder(s); author
68-k-pbm-cs-donor-a-1-standard-1-1-0. self-archiving of the accepted manuscript version of this article is solely governed by the
14. Li, Y. et al. Single-cell transcriptome analysis reveals dynamic cell populations and terms of such publishing agreement and applicable law.
differential gene expression patterns in control and aneurysmal human aortic tissue.
Circulation 142, 1374–1388 (2020). © The Author(s), under exclusive licence to Springer Nature Limited 2023
624 | Nature | Vol 618 | 15 June 2023
Methods protein-coding and miRNA genes were used for downstream analysis.
Cells with less than seven detected Ensembl-annotated protein-coding
Assembly and rank value encoding of transcriptomes in or miRNA genes were excluded as the 15% masking used for the pretrain-
Genecorpus-30M ing learning objective would not reliably mask a gene in cells with fewer
Assembly and uniform processing of single-cell transcriptomes. We detected genes. Ultimately, 27.4 million (27,406,217) cells passed the
assembled a large-scale pretraining corpus, Genecorpus-30M, compris- defined quality filters.
ing 29.9 million (29,900,531) human single-cell transcriptomes from a
broad range of tissues from publicly available data (Fig. 1b and Supple- Rank value encoding of single-cell transcriptomes. We developed
mentary Table 1). We excluded cells with high mutational burdens (for a rank value encoding method that provides a non-parametric rep-
example, malignant cells and immortalized cell lines) that could lead to resentation of the transcriptome of each single cell, ranking genes
substantial network rewiring without companion genome sequencing by their expression within that cell normalized by their expression
to facilitate interpretation. We only included droplet-based sequencing across the entire Genecorpus-30M (Fig. 1c). This method takes advan-
platforms to assure expression value unit comparability. Overall, 561 tage of the many observations of the expression of each gene across
datasets were included and stored as uniform files in the .loom HDF5 Genecorpus-30M to prioritize genes that distinguish cell state. Speci-
format including metadata from the original studies as row (feature) fically, this method will deprioritize ubiquitously highly expressed
and column (cell) attributes described below. housekeeping genes by normalizing them to a lower rank. Conversely,
Publicly available datasets containing raw counts were collected genes such as transcription factors that may be expressed at low levels
from the National Center for Biotechnology Information (NCBI) Gene when they are expressed but have a high power to distinguish cell state
Expression Omnibus (GEO), NCBI Sequence Read Archive (SRA), will move to a higher rank within the encoding (Extended Data Fig. 1c).
Human Cell Atlas, European Molecular Biology Laboratory-European Furthermore, this rank-based approach may be more robust against
Bioinformatics Institute (EMBL-EBI) Single Cell Expression Atlas, technical artefacts that may systematically bias the absolute transcript
Broad Institute Single Cell Portal, Brotman Baty Institute (BBI)-Allen counts value whereas the overall relative ranking of genes within each
Single Cell Atlases, Tumor Immune Single-cell Hub (TISCH) (exclud- cell remains more stable.
ing malignant cells), Panglao Database, 10x Genomics, University of To accomplish this, we first calculated the non-zero median value of
California, Santa Cruz Cell Browser, European Genome-phenome expression of each detected gene across all cells passing quality filter-
Archive, Synapse, Riken, Zenodo, National Institutes of Health (NIH) ing from the entire Genecorpus-30M. We aggregated the transcript
Figshare Archive, NCBI dbGap, Refine.bio, China National GeneBank count distribution for each gene in a memory-efficient manner by
Sequence Archive, Mendeley Data and individual communication scanning through chunks of .loom data using loompy, normalizing
with authors of the original studies11,23,29,32,45,47–153. Further resources the gene transcript counts in each cell by the total transcript count of
for collecting information about suitable studies included Entrez that cell to account for varying sequencing depth and updating the
Direct tools and the dataset summary from Database 2020 (ref. 154). normalized count distribution of the gene within the t-digest157 data
Tools used in conversion of data to uniform .loom HDF5 files included structure developed for accurate online accumulation of rank-based
loompy, scanpy155, anndata, scipy, numpy, pandas, Cellranger and statistics. We then normalized the genes in each single-cell tran-
LoomExperiment. scriptome by the non-zero median value of expression of that gene
Row feature attributes included Ensembl annotations for the gene ID, across Genecorpus-30M and ordered the genes by the rank of their
ID version (if provided by original study), name and type (for example, normalized expression in that specific cell. Of note, we opted to use
protein coding, microRNA, mitochondrial and so on). Annotation data the non-zero median value of expression rather than include zeros
were retrieved from Ensembl and MyGene156. Column cell attributes in the distribution so as not to weight the value by tissue representa-
included a unique Genecorpus-30M cell ID comprising the dataset tion within Genecorpus-30M, assuming that a representative range of
name, sample name and cell barcode from that dataset. The dataset transcript values would be observed within the cells in which each gene
and sample names were also included as separate individual attributes was detected. This normalization factor for each gene is calculated
such that the cell barcode can be derived by subtracting these from once from the pretraining corpus and is used for all future datasets
the unique Genecorpus-30M cell ID if needed. Column cell attributes presented to the model. The provided tokenizer code includes this nor-
also included the principal organ included in the dataset, which we malization procedure and should be used for tokenizing new datasets
annotated as one of the following categories: adipose, adrenal, airway, presented to Geneformer to ensure consistency of the normalization
bladder, bone, bone_marrow, brain, breast, cord_blood, decidua, ear, factor used for each gene.
embryo, endothelial, eye, heart, immune, intestine_unspecified, kid- The rank value encodings for each single-cell transcriptome
ney, large_intestine, liver, lung, lymph_node, lymphatic, muscle, nasal, were then tokenized on the basis of a total vocabulary of 25,424
oesophagus, pancreas, placenta, pluripotent_stem_cell, prostate, skin, protein-coding or miRNA genes detected in a median of 173,152 cells
small_intestine, spleen, stomach, testis, thymus, tonsil, various, yolk_ within Genecorpus-30M. The vocabulary also included two more spe-
sac. Column cell attributes also included the specific organ(s) included cial tokens for padding and masking. The tokenized data were stored
in the dataset on the basis of metadata provided by the original study. within the Huggingface Datasets158 structure, which is based on the
If the original study included cell-type annotations, we included these Apache Arrow format that allows processing of large datasets with
as a cell-type column attribute for each cell as well. We also included zero-copy reads without memory constraints. Of note, this strategy is
the sequencing platform used. also space-efficient as the genes are stored as ranked tokens as oppo-
Column cell attributes also included several calculated measure- sed to the exact transcript values, and we only store genes detected
ments for each cell: the total number of read counts, the percentage within each cell rather than the full sparse dataset that includes all of
of mitochondrial reads, the number of genes Ensembl-annotated the undetected genes.
as protein-coding or miRNA genes and whether the cell passed the
quality-control metrics we established for scalable filtering of the cells Geneformer architecture and pretraining
to exclude possible doublets and/or damaged cells. Only cells that Geneformer architecture. Geneformer is composed of six trans-
passed these filtering metrics were used for downstream analyses in this former encoder units1,2, each composed of a self-attention layer and
work. Specifically, datasets were filtered to retain cells with total read feed forward neural network layer with the following parameters:
counts within 3 s.d. of the mean within that dataset and mitochondrial input size of 2,048 (fully represents 93% of rank value encodings in
reads within 3 s.d. of the mean within that dataset. Ensembl-annotated Genecorpus-30M), 256 embedding dimensions, four attention heads
Article
per layer and feed forward size of 512 (Fig. 1c). Geneformer uses full cell classes as indicated in Supplementary Table 2. To demonstrate the
dense self-attention across the input size of 2,048. Depth was chosen efficacy of the pretrained Geneformer in boosting predictive poten-
on the basis of the maximum depth for which there were sufficient tial of downstream fine-tuning applications, we intentionally used
data to pretrain as it has been established that this approach yields the the same fine-tuning hyperparameters for all applications. It should
greatest predictive potential in other informational fields including be noted that hyperparameter tuning for deep learning applications
natural language understanding, computer vision and mathematical generally significantly enhances learning and so it is likely that the
problem-solving44. Furthermore, we maximized the amount of context maximum predictive potential of Geneformer in these downstream
(input size) considered by the model with full attention based on the applications is significantly underestimated. Hyperparameters used for
number of genes standardly detected in each cell within the pretrain- fine-tuning were as follows: max learning rate, 5 × 10–5; learning sched-
ing corpus. Further parameters were as follows: nonlinear activation uler, linear with warmup; optimizer, Adam with weight decay fix160;
function, rectified linear unit (ReLU); dropout probability for all fully warmup steps, 500; weight decay, 0.001; batch size, 12. All fine-tuning
connected layers, 0.02; dropout ratio for attention probabilities, 0.02; in Supplementary Table 2 was performed with a single training epoch
standard deviation of the initializer for weight matrices, 0.02; epsilon to avoid overfitting.
for layer normalization layers, 1 × 10–12. Modelling was implemented in The number of layers frozen from fine-tuning are indicated in Sup-
pytorch and using the Huggingface Transformers library159 for model plementary Table 2. Generally, in our experience, applications that are
configuration, data loading and training. more relevant to the pretraining objective benefit from more layers
being frozen to prevent overfitting to the limited task-specific data,
Geneformer pretraining and performance optimization. Pretraining whereas applications that are more distant from the pretraining objec-
was accomplished using a masked learning objective, which has been tive benefit from fine-tuning of more layers to optimize performance
shown in other informational fields1,2 to improve generalizability of on the new task. Fine-tuning results for gene classification applications
the foundational knowledge learned during pretraining for a wide were reported as AUCs ± standard deviation and F1 score calculated
range of downstream fine-tuning objectives. During pretraining, 15% on the basis of a fivefold cross-validation strategy for which training
of the genes within each transcriptome were masked and the model was performed on 80% of the gene training labels and performance
was trained to predict which gene should be within each masked posi- was tested on the 20% held-out gene training labels, repeating for five
tion in that specific cell state using the context of the remaining un- folds. Of note, because the fine-tuning applications are trained on
masked genes. A principal strength of this approach is that it is entirely classification objectives that are completely separate from the masked
self-supervised and can be accomplished on completely unlabelled learning objective, whether or not task-specific data were included in
data, which allows the inclusion of large amounts of training data with- the pretraining corpus is not relevant to the classification predictions,
out being restricted to samples with accompanying labels. Pretraining as demonstrated in Extended Data Fig. 1f.
hyperparameters were optimized to the following final values: max We then fully fine-tuned the dosage sensitivity and bivalency clas-
learning rate, 1 × 10–3; learning scheduler, linear with warmup; opti- sification models using all gene training labels to test their ability to
mizer, Adam with weight decay fix160; warmup steps, 10,000; weight generalize to out-of-sample data. We tested whether, without any fur-
decay, 0.001; batch size, 12. Tensorboard was used for experimentation ther training, the model fine-tuned to distinguish dosage-sensitive
tracking, and the model was pretrained for three epochs. versus insensitive genes could predict dosage sensitivity of a recently
As the input size of 2,048 is considerably large for a full dense reported set of disease genes from ref. 22, which analysed CNVs from
self-attention model (for example, BERT1,2 input size is 512) and trans- 753,994 individuals to define genes whose deletion was associated
formers have a quadratic memory and time complexity O (L2) with with primarily neurodevelopmental disease with either high (greater
respect to input size, we implemented measures to optimize efficiency than 0.85 score) or moderate (0.15–0.85 score) confidence22. Predicted
of large-scale pretraining. The trainer from the Huggingface Trans- dosage sensitivity of these gene sets was tested in the context of 10,000
formers library159 was used for pretraining with the substitution of a randomly sampled cells from Genecorpus-30M, neurons across any
custom tokenizer to implement dynamic, length-grouped padding, adult or developmental timepoint defined as TUBB3-marked cells from
which minimized computation on padding and achieved a 29.4× Genecorpus-30M or fetal cerebral cells from the Fetal Cell Atlas23. We
speedup in pretraining. This process takes a randomly sampled also tested whether, without any further training, the model fine-tuned
megabatch and then orders minibatches by their length in descending to distinguish bivalent versus single Lys4-marked genes by training
order (to ensure that any memory constraints are encountered earlier). on the 56 highly conserved loci would generalize to the genome-wide
Minibatches are then dynamically padded, minimizing the compu- setting30.
tation wasted on padding due to being length grouped. We also
implemented recent advances in distributed GPU training9,10 to allow Geneformer gene embeddings, cell embeddings and attention
efficient pretraining on the large-scale dataset using Deepspeed, weights
which partitions parameters, gradients and optimizer states across Gene embeddings. For each single-cell transcriptome presented to
available GPUs, offloads processing/memory as possible to central Geneformer, the model embeds each gene into a 256-dimensional space
processing units (CPUs) to allow more to fit on GPU and reduces mem- that encodes the characteristics of the gene specific to the context of
ory fragmentation by ensuring that long- and short-term memory that cell. Contextual Geneformer gene embeddings are extracted as
allocations do not mix. Overall, pretraining was achieved in approxi- the hidden state weights for the 256 embedding dimensions for each
mately 3 days distributed across three nodes each with four Nvidia gene within the given single-cell transcriptome evaluated by forward
V100 32GB GPUs (total 12 GPUs). pass through the Geneformer model. Gene embeddings analysed in
this study were extracted from the second to last layer of the models
Geneformer fine-tuning as the final layer is known to encompass features more directly related
Fine-tuning of Geneformer was accomplished by initializing the model to the learning objective prediction whereas the second to last layer is
with the pretrained Geneformer weights and adding a final task-specific a more generalizable representation.
transformer layer. The fine-tuning objective was either gene classifica-
tion or cell classification as indicated in Supplementary Table 2. The Cell embeddings. Geneformer cell embeddings, which encode
trainer from the Huggingface Transformers library159 was used for characteristics of the state of that single cell, are generated by aver-
pretraining with the substitution of a custom tokenizer as described aging the embeddings of each gene detected in that cell, resulting
above and a custom data collator for dynamically labelling gene or in a 256-dimensional embedding. We used the second to last layer
embeddings as discussed above (except for the disease modelling 50. Fang, Z. et al. Single-cell heterogeneity analysis and CRISPR screen identify key
application as discussed in the Supplementary Methods). β-cell-specific disease genes. Cell Rep. 26, 3132–3144 (2019).
51. Agarwal, D. et al. A single-cell atlas of the human substantia nigra reveals cell-specific
pathways associated with neurological disorders. Nat. Commun. 11, 4183 (2020).
Attention weights. Each of Geneformer’s six layers has four atten- 52. Rasouli, J. et al. A distinct GM-CSF+ T helper cell subset requires T-bet to adopt a TH1
phenotype and promote neuroinflammation. Sci. Immunol. 5, eaba9953 (2020).
tion heads that are meant to learn in an unsupervised manner to pay
53. Park, J.-E. et al. A cell atlas of human thymic development defines T cell repertoire
attention to distinct classes of genes to jointly improve predictions formation. Science 367, eaay3224 (2020).
without previous knowledge of the biological function of any gene. 54. Mende, N. et al. Quantitative and molecular differences distinguish adult human
medullary and extramedullary haematopoietic stem and progenitor cell landscapes.
Contextual Geneformer attention weights are extracted for each at-
Preprint at BioRxiv https://doi.org/10.1101/2020.01.26.919753 (2020).
tention head within each self-attention layer for each gene within the 55. Setty, M. et al. Characterization of cell fate probabilities in single-cell data with Palantir.
given single-cell transcriptome evaluated by forward pass through the Nat. Biotechnol. 37, 451–460 (2019).
56. Popescu, D.-M. et al. Decoding human fetal liver haematopoiesis. Nature 574, 365–371
Geneformer model.
(2019).
57. Vento-Tormo, R. et al. Single-cell reconstruction of the early maternal-fetal interface in
In silico perturbation humans. Nature 563, 347–353 (2018).
58. Ramachandran, P. et al. Resolving the fibrotic niche of human liver cirrhosis at single-cell
We designed an in silico perturbation approach for which the rank of
level. Nature 575, 512–518 (2019).
given genes is perturbed to model their inhibition or activation. The 59. Kinchen, J. et al. Structural remodeling of the human colonic mesenchyme in
effects of the in silico perturbation are measured at the cell and gene inflammatory bowel disease. Cell 175, 372–386 (2018).
60. James, K. R. et al. Distinct microbial and immune niches of the human colon. Nat. Immunol.
embedding level, modelling how the perturbation affects the state
21, 343–353 (2020).
of the cell and the regulation of downstream genes within the gene 61. Zhou, L. et al. Single-cell RNA-seq analysis uncovers distinct functional human NKT cell
network, respectively. In silico deletion was modelled by removing the sub-populations in peripheral blood. Front. Cell Dev. Biol. 8, 384 (2020).
62. Liao, J. et al. Single-cell RNA sequencing of human kidney. Sci. Data 7, 4 (2020).
given gene from the rank value encoding of the given single-cell tran-
63. Jäkel, S. et al. Altered human oligodendrocyte heterogeneity in multiple sclerosis. Nature
scriptome and quantifying the cosine similarity between the original 566, 543–547 (2019).
and perturbed (1) cell embeddings to determine the predicted del- 64. Merrick, D. et al. Identification of a mesenchymal progenitor cell hierarchy in adipose
tissue. Science 364, eaav2501 (2019).
eterious impact of deleting that gene in that cell context or (2) gene
65. Habermann, A. C. et al. Single-cell RNA sequencing reveals profibrotic roles of distinct
embeddings of the remaining genes in the single-cell transcriptome epithelial and mesenchymal lineages in pulmonary fibrosis. Sci. Adv. 6, eaba1972
to determine which genes were predicted to be most sensitive to in (2020).
66. Rosa, F. F. et al. Direct reprogramming of fibroblasts into antigen-presenting dendritic
silico deletion of the given gene. In silico deletion can be performed
cells. Sci. Immunol. 3, eaau4292 (2018).
with a single gene or multiple genes being deleted. In silico activation 67. Stewart, B. J. et al. Spatiotemporal immune zonation of the human kidney. Science 365,
was modelled by moving a given gene(s) to the front of the rank value 1461–1466 (2019).
68. MacParland, S. A. et al. Single cell RNA sequencing of human liver reveals distinct
encoding (similarly to the in silico reprogramming strategy discussed
intrahepatic macrophage populations. Nat. Commun. 9, 4383 (2018).
in the Supplementary Methods in which genes were artificially added to 69. Welch, J. et al. Integrative inference of brain cell similarities and differences from
the front of the rank value encoding to model cellular reprogramming single-cell genomics. Preprint at BioRxiv https://doi.org/10.1101/459891 (2018).
70. Ledergor, G. et al. Single cell dissection of plasma cell heterogeneity in symptomatic and
by these factors). In theory, more subtle downregulation and activation
asymptomatic myeloma. Nat. Med. 24, 1867–1876 (2018).
could be modelled by shifting genes up or down within the rank value 71. Lukowski, S. W. et al. A single-cell transcriptome atlas of the adult human retina. EMBO J.
encoding to a subtler degree. 38, e100811 (2019).
72. Kang, H. M. et al. Multiplexed droplet single-cell RNA-sequencing using natural genetic
Please refer to the Supplementary Methods for complete methods
variation. Nat. Biotechnol. 36, 89–94 (2018).
including analysis of context dependence and robustness to batch- 73. Zirkel, A. et al. HMGB2 loss upon senescence entry disrupts genomic organization and
dependent technical artefacts, attention weight analysis, in silico induces CTCF clustering across cell types. Mol. Cell 70, 730–744 (2018).
74. Goudot, C. et al. Aryl hydrocarbon receptor controls monocyte differentiation into
perturbation analysis, alternative modelling approaches, cell-type dendritic cells versus macrophages. Immunity 47, 582–596 (2017).
annotation fine-tuning application, disease modelling approach, 75. McCauley, K. B. et al. Single-cell transcriptomic profiling of pluripotent stem cell-derived
scRNA-seq sample collection and preprocessing and experimen- SCGB3A2+ airway epithelium. Stem Cell Rep. 10, 1579–1595 (2018).
76. Das, R. et al. Early B cell changes predict autoimmunity following combination immune
tal testing of Geneformer-predicted targets in engineered cardiac checkpoint blockade. J. Clin. Invest. 128, 715–720 (2018).
microtissues. 77. Kini Bailur, J. et al. Changes in bone marrow innate lymphoid cell subsets in monoclonal
gammopathy: target for IMiD therapy. Blood Adv. 1, 2343–2347 (2017).
78. Patil, V. S. et al. Precursors of human CD4+ cytotoxic T lymphocytes identified by
Reporting summary
single-cell transcriptome analysis. Sci. Immunol. 3, eaan8664 (2018).
Further information on research design is available in the Nature Port- 79. Wang, C. et al. Expansion of hedgehog disrupts mesenchymal identity and induces
folio Reporting Summary linked to this article. emphysema phenotype. J. Clin. Invest. 128, 4343–4358 (2018).
80. Hermann, B. P. et al. The mammalian spermatogenesis single-cell transcriptome, from
spermatogonial stem cells to spermatids. Cell Rep. 25, 1650–1667 (2018).
81. Menon, R. et al. Single-cell analysis of progenitor cell dynamics and lineage specification
Data availability in the human fetal kidney. Development 145, dev164038 (2018).
82. Czerniecki, S. M. et al. High-throughput screening enhances kidney organoid
Genecorpus-30M is available on the Huggingface Dataset Hub at differentiation from human pluripotent stem cells and enables automated
https://huggingface.co/datasets/ctheodoris/Genecorpus-30M. multidimensional phenotyping. Cell Stem Cell 22, 929–940 (2018).
83. Papa, L. et al. Ex vivo human HSC expansion requires coordination of cellular
reprogramming with mitochondrial remodeling and p53 activation. Blood Adv. 2,
2766–2779 (2018).
Code availability 84. Schulthess, J. et al. The short chain fatty acid butyrate imprints an antimicrobial program
in macrophages. Immunity 50, 432–445 (2019).
The pretrained Geneformer model, transcriptome tokenizer and code
85. Guo, J. et al. The adult human testis transcriptional cell atlas. Cell Res. 28, 1141–1157
for pretraining and fine-tuning the model are available on the Hugging- (2018).
face Model Hub at https://huggingface.co/ctheodoris/Geneformer. 86. Karow, M. et al. Direct pericyte-to-neuron reprogramming via unfolding of a neural stem
cell-like program. Nat. Neurosci. 21, 932–940 (2018).
All other code used in this study is available upon request from the
87. Xin, Y. et al. Pseudotime ordering of single human β-cells reveals states of insulin
corresponding authors. production and unfolded protein response. Diabetes 67, 1783–1794 (2018).
88. Phipson, B. et al. Evaluation of variability in human kidney organoids. Nat. Methods 16,
79–87 (2019).
47. Smillie, C. S. et al. Intra- and inter-cellular rewiring of the human colon during ulcerative 89. Balan, S. et al. Large-scale human dendritic cell differentiation revealing notch-dependent
colitis. Cell 178, 714–730 (2019). lineage bifurcation and heterogeneity. Cell Rep. 24, 1902–1915 (2018).
48. Lee, J. S. et al. Immunophenotyping of Covid-19 and influenza highlights the role of type I 90. Milpied, P. et al. Human germinal center transcriptional programs are de-synchronized in
interferons in development of severe Covid-19. Sci. Immunol. 5, eabd1554 (2020). B cell lymphoma. Nat. Immunol. 19, 1013–1024 (2018).
49. Baron, M. et al. A single-cell transcriptomic map of the human and mouse pancreas 91. Parikh, K. et al. Colonic epithelial cell diversity in health and inflammatory bowel disease.
reveals inter- and intra-cell population structure. Cell Syst. 3, 346–360 (2016). Nature 567, 49–55 (2019).
Article
92. Habiel, D. M. et al. CCR10+ epithelial cells from idiopathic pulmonary fibrosis lungs drive 130. Schafflick, D. et al. Integrated single cell analysis of blood and cerebrospinal fluid
remodeling. JCI Insight 3, e122211 (2018). leukocytes in multiple sclerosis. Nat. Commun. 11, 247 (2020).
93. Paik, D. T. et al. Large-scale single-cell RNA-seq reveals molecular signatures of 131. Su, C. et al. Single-cell RNA sequencing in multiple pathologic types of renal cell
heterogeneous populations of human induced pluripotent stem cell-derived endothelial carcinoma revealed novel potential tumor-specific markers. Front. Oncol. 11, 719564
cells. Circ. Res. 123, 443–450 (2018). (2021).
94. Martin, J. C. et al. Single-cell analysis of Crohn’s disease lesions identifies a pathogenic 132. He, J. et al. Dissecting human embryonic skeletal stem cell ontogeny by single-cell
cellular module associated with resistance to anti-TNF therapy. Cell 178, 1493–1508 transcriptomic and functional analyses. Cell Res. 31, 742–757 ( 20 21 ).
(2019). 133. Liao, M. et al. Single-cell landscape of bronchoalveolar immune cells in patients with
95. Zheng, Y. et al. A human circulating immune cell landscape in aging and COVID-19. COVID-19. Nat. Med. 26, 842–844 (2020).
Protein Cell 11, 740–770 (2020). 134. Liu, X. et al. Reprogramming roadmap reveals route to human induced trophoblast stem
96. Hochane, M. et al. Single-cell transcriptomics reveals gene expression dynamics of cells. Nature 586, 101–107 (2020).
human fetal kidney development. PLoS Biol. 17, e3000152 (2019). 135. He, S. et al. Single-cell transcriptome profiling of an adult human cell atlas of 15 major
97. Sohni, A. et al. The neonatal and adult human testis defined at the single-cell level. Cell organs. Genome Biol. 21, 294 (2020).
Rep. 26, 1501–1517 (2019). 136. Wu, C.-L. et al. Single cell transcriptomic analysis of human pluripotent stem cell
98. Tran, T. et al. In vivo developmental trajectories of human podocyte inform in vitro chondrogenesis. Nat. Commun. 12, 362 (2021).
differentiation of pluripotent stem cell-derived podocytes. Dev. Cell 50, 102–116 137. Cowan, C. S. et al. Cell types of the human retina and its organoids at single-cell
(2019). resolution. Cell 182, 1623–1640 (2020).
99. Wang, Y. et al. Single-cell transcriptome analysis reveals differential nutrient absorption 138. Savas, P. et al. Single-cell profiling of breast cancer T cells reveals a tissue-resident
functions in human intestine. J. Exp. Med. 217, e20191130 (2020). memory subset associated with improved prognosis. Nat. Med. 24, 986–993
100. Vieira Braga, F. A. et al. A cellular census of human lungs identifies novel cell states in (2018).
health and in asthma. Nat. Med. 25, 1153–1163 (2019). 139. Wang, L. et al. Single-cell map of diverse immune phenotypes in the metastatic brain
101. Guo, J. et al. The dynamic transcriptional cell atlas of testis development during human tumor microenvironment of non small cell lung cancer. Preprint at BioRxiv https://doi.org/
puberty. Cell Stem Cell 26, 262–276 (2020). 10.1101/2019.12.30.890517 (2019).
102. Voigt, A. P. et al. Single-cell transcriptomics of the human retinal pigment epithelium and 140. Lu, Y.-C. et al. Single-cell transcriptome analysis reveals gene signatures associated with
choroid in health and macular degeneration. Proc. Natl Acad. Sci. USA 116, 24100–24107 T-cell persistence following adoptive cell therapy. Cancer Immunol. Res. 7, 1824–1836
(2019). (2019).
103. Menon, M. et al. Single-cell transcriptomic atlas of the human retina identifies 141. Wang, L. et al. The phenotypes of proliferating glioblastoma cells reside on a single axis
cell types associated with age-related macular degeneration. Nat. Commun. 10, 4902 of variation. Cancer Discov. 9, 1708–1719 (2019).
(2019). 142. Wang, R. et al. Adult human glioblastomas harbor radial glia-like cells. Stem Cell Rep. 14,
104. Wilk, A. J. et al. A single-cell atlas of the peripheral immune response in patients with 338–350 (2020).
severe COVID-19. Nat. Med. 26, 1070–1076 (2020). 143. Wang, L., Catalan, F., Shamardani, K., Babikir, H. & Diaz, A. Ensemble learning for
105. Li, B. et al. Cumulus provides cloud-based data analysis for large-scale single-cell and classifying single-cell data and projection across reference atlases. Bioinformatics 36,
single-nucleus RNA-seq. Nat. Methods 17, 793–798 (2020). 3585–3587 (2020).
106. Daniszewski, M. et al. Single cell RNA sequencing of stem cell-derived retinal ganglion 144. Ruffin, A. T. et al. B cell signatures and tertiary lymphoid structures contribute to outcome
cells. Sci. Data 5, 180013 (2018). in head and neck squamous cell carcinoma. Nat. Commun. 12, 3349 (2021).
107. Goveia, J. et al. An integrated gene expression landscape profiling approach to identify 145. Zhang, Q. et al. Landscape and dynamics of single immune cells in hepatocellular
lung tumor endothelial cell heterogeneity and angiogenic candidates. Cancer Cell 37, carcinoma. Cell 179, 829–845 (2019).
21–36 (2020). 146. Song, Q. et al. Dissecting intratumoral myeloid cell plasticity by single cell RNA-seq.
108. Norelli, M. et al. Monocyte-derived IL-1 and IL-6 are differentially required for Cancer Med. 8, 3072–3085 (2019).
cytokine-release syndrome and neurotoxicity due to CAR T cells. Nat. Med. 24, 739–748 147. Kim, N. et al. Single-cell RNA sequencing demonstrates the molecular and cellular
(2018). reprogramming of metastatic lung adenocarcinoma. Nat. Commun. 11, 2285
109. Daniszewski, M. et al. Single-cell profiling identifies key pathways expressed by iPSCs (2020).
cultured in different commercial media. iScience 7, 30–39 (2018). 148. Tang-Huau, T.-L. et al. Human in vivo-generated monocyte-derived dendritic cells and
110. Miller, A. J. et al. In vitro and in vivo development of the human airway at single-cell macrophages cross-present antigens through a vacuolar pathway. Nat. Commun. 9,
resolution. Dev. Cell 53, 117–128 (2020). 2570 (2018).
111. Silvin, A. et al. Elevated calprotectin and abnormal myeloid cell subsets discriminate 149. Peng, J. et al. Single-cell RNA-seq highlights intra-tumoral heterogeneity and
severe from mild COVID-19. Cell 182, 1401–1418 (2020). malignant progression in pancreatic ductal adenocarcinoma. Cell Res. 29, 725–738
112. Deprez, M. et al. A single-cell atlas of the human healthy airways. Am. J. Resp. Crit. Care (2019).
Med. 202, 1636–1645 (2020). 150. 10x Genomics Datasets: Single Cell Gene Expression. 10x Genomics https://
113. Sridhar, A. et al. Single-cell transcriptomic comparison of human fetal retina, www.10xgenomics.com/resources/datasets?menu%5Bproducts.name%5D=Single%20
hPSC-derived retinal organoids, and long-term retinal cultures. Cell Rep. 30, 1644–1659 Cell%20Gene%20Expression&query=&page=1&configure%5Bfacets%5D%5B0%5D=che
(2020). mistryVersionAndThroughput&configure%5Bfacets%5D%5B1%5D=pipeline.version&confi
114. Wu, H. et al. Comparative analysis and refinement of human PSC-derived kidney gure%5BhitsPerPage%5D=500.
organoid differentiation with single-cell transcriptomics. Cell Stem Cell 23, 869–881 151. de Andrade, L. F. et al. Discovery of specialized NK cell populations infiltrating human
(2018). melanoma metastases. JCI Insight 4, e133103 (2019).
115. Vijay, J. et al. Single-cell analysis of human adipose tissue identifies depot and disease 152. Zhang, P. et al. Dissecting the single-cell transcriptome network underlying gastric
specific cell types. Nat. Metab. 2, 97–109 (2020). premalignant lesions and early gastric cancer. Cell Rep. 27, 1934–1947 (2019).
116. Solé-Boldo, L. et al. Single-cell transcriptomes of the human skin reveal age-related loss 153. Durante, M. A. et al. Single-cell analysis reveals new evolutionary complexity in uveal
of fibroblast priming. Commun. Biol. 3, 188 (2020). melanoma. Nat. Commun. 11, 496 (2020).
117. Adams, T. S. et al. Single-cell RNA-seq reveals ectopic and aberrant lung-resident cell 154. Svensson, V., da Veiga Beltrame, E. & Pachter, L. A curated database reveals trends in
populations in idiopathic pulmonary fibrosis. Sci. Adv. 6, eaba1983 (2020). single-cell transcriptomics. Database 2020, baaa073 (2020).
118. Moreira, L. M. et al. Paracrine signalling by cardiac calcitonin controls atrial fibrogenesis 155. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell gene expression data
and arrhythmia. Nature 587, 460–465 (2020). analysis. Genome Biol. 19, 15 (2018).
119. Ren, X. et al. COVID-19 immune features revealed by a large-scale single-cell 156. Xin, J. et al. High-performance web services for querying gene and variant annotation.
transcriptome atlas. Cell 184, 1895–1913 (2021). Genome Biol. 17, 91 (2016).
120. Bunis, D. G. et al. Single-cell mapping of progressive fetal-to-adult transition in human 157. Dunning, T. The t-digest: efficient estimates of distributions. Softw. Impacts 7, 100049
naive T cells. Cell Rep. 34, 108573 (2021). (2021).
121. Plasschaert, L. W. et al. A single-cell atlas of the airway epithelium reveals the CFTR-rich 158. Lhoest, Q. et al. Datasets: a community library for natural language processing. Preprint
pulmonary ionocyte. Nature 560, 377–381 (2018). at https://doi.org/10.48550/arXiv.2109.02846 (2021).
122. Takeda, A. et al. Single-cell survey of human lymphatics unveils marked endothelial cell 159. Wolf, T. et al. HuggingFace’s transformers: state-of-the-art natural language processing.
heterogeneity and mechanisms of homing for neutrophils. Immunity 51, 561–572 (2019). Preprint at https://doi.org/10.48550/arXiv.1910.03771 (2019).
123. Frumm, S. M. et al. A hierarchy of proliferative and migratory keratinocytes maintains the 160. Loshchilov, I. & Hutter, F. Decoupled weight decay regularization. Preprint at https://
tympanic membrane. Cell Stem Cell 28, 315–330 (2021). doi.org/10.48550/arXiv.1711.05101 (2017).
124. Yu, Z. et al. Single-cell transcriptomic map of the human and mouse bladders. J. Am. Soc.
Nephrol. 30, 2159–2176 (2019).
125. Rubenstein, A. B. et al. Single-cell transcriptional profiles in human skeletal muscle. Sci.
Acknowledgements We thank J. Rae for helpful scientific discussions and Google Research
Rep. 10, 229 (2020).
for providing tensor processing unit (TPU) resources for experimentation. P.T.E. was supported
126. McCracken, I. R. et al. Transcriptional dynamics of pluripotent stem cell-derived
by grants from the National Institutes of Health (NIH) (1RO1HL092577, 1R01HL157635 and
endothelial cell differentiation revealed by single-cell RNA sequencing. Eur. Heart J. 41,
5R01HL139731), American Heart Association Strategically Focused Research Networks
1024–1036 (2020).
(18SFRN34110082) and European Union (MAESTRIA 965286). C.V.T. was supported by NIH
127. Hua, P. et al. Single-cell analysis of bone marrow-derived CD34+ cells from children with
T32GM007748 and the Helen Hay Whitney Foundation Postdoctoral Fellowship. L.X. was
sickle cell disease and thalassemia. Blood 134, 2111–2115 (2019).
supported by the American Heart Association (20CDA35260081).
128. Orozco, L. D. et al. Integration of eQTL and a single-cell atlas in the human eye identifies
causal genes for age-related macular degeneration. Cell Rep. 30, 1246–1259 (2020).
129. Hurley, K. et al. Reconstructed single-cell fate trajectories define lineage plasticity Author contributions C.V.T. conceived of the work, developed Geneformer, assembled
windows during differentiation of human PSC-derived distal lung progenitors. Cell Stem Genecorpus-30M and designed and performed computational analyses. L.X., A.C., Z.R.A.S.,
Cell 26, 593–608 (2020). M.C.H., H.M. and E.M.B. performed experimental validation in engineered cardiac microtissues.
M.D.C. performed preprocessing, cell annotation and differential expression analysis of E.M.B. was a full-time employee of Bayer when this work was performed. The remaining
the cardiomyopathy dataset. Z.Z. provided data from the TISCH database for inclusion in authors declare no competing interests.
Genecorpus-30M. X.S.L. and P.T.E. designed analyses and supervised the work. C.V.T., X.S.L.
and P.T.E. wrote the manuscript. All authors edited the manuscript. Additional information
Supplementary information The online version contains supplementary material available at
https://doi.org/10.1038/s41586-023-06139-9.
Competing interests X.S.L. conducted this work while on faculty at Dana-Farber Cancer Correspondence and requests for materials should be addressed to Christina V. Theodoris or
Institute and is now a board member and CEO of GV20 Therapeutics. P.T.E. has received Patrick T. Ellinor.
sponsored research support from Bayer AG, IBM Research, Bristol Myers Squibb and Pfizer. Peer review information Nature thanks Amir Bashan, Natasa Przulj and Nathan Palpant for their
P.T.E. has also served on advisory boards or consulted for Bayer AG, MyoKardia and Novartis. contribution to the peer review of this work. Peer reviewer reports are available.
A.C. is an employee of Bayer US LLC (a subsidiary of Bayer AG) and may own stock in Bayer AG. Reprints and permissions information is available at http://www.nature.com/reprints.
Article
Extended Data Fig. 1 | See next page for caption.
