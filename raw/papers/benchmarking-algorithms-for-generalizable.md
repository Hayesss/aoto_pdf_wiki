---
source_path: /mnt/c/Users/Administrator/Zotero/storage/JG9B8XEL/Wei 等 - 2026 - Benchmarking algorithms for generalizable single-cell perturbation response prediction.pdf
ingested: 2026-04-23
sha256: 07939e50bf005fb8
---

nature methods
Analysis https://doi.org/10.1038/s41592-025-02980-0
Benchmarking algorithms for generalizable
single-cell perturbation response prediction
Received: 20 January 2025 Zhiting Wei 1,2,3,4,6, Yiheng Wang1,2,5,6, Yicheng Gao1,2,6, Shuguang Wang 1,2,6,
Ping Li1, Duanmiao Si1,2, Yuli Gao1,2, Siqi Wu1,2, Danlu Li1,2, Kejing Dong 1,2,
Accepted: 5 November 2025
Xingbo Yang1,2, Chen Tang1,2, Shaliu Fu 1,2, Xiaohan Chen1,2, Wannian Li1,2,
Published online: 11 December 2025 Yuzhou You1,2, Chen Zhang1,2, Aibin Liang 1 , Guohui Chuai 1,2,3 &
Qi Liu 1,2,3
Check for updates
Single-cell perturbation technologies enable systematic investigation
of gene functions and regulatory networks with single-cell resolution.
However, performing large-scale and combinatorial perturbation screens
poses notable challenges due to their exponentially increased complexity.
Computational methods, including foundation models, have been
developed to predict perturbation effects. Yet despite claims of promising
performance, concerns remain about their true efficacy, particularly when
evaluated across diverse and previously unseen cellular contexts and
perturbation scenarios. Here, we present a comprehensive benchmark of
27 methods for single-cell perturbation response prediction, evaluated
across 29 datasets using 6 complementary performance metrics. By
evaluating them under multiple scenarios, we systematically assess their
generalizability, including that of emerging foundation models. Our results
provide practical guidance for method selection and underscore the need
for cellular context embedding approaches to enhance the generalizability
of perturbation effect prediction in single-cell research.
Single-cell perturbation technology (for example, Perturb-seq and screens, particularly for combined perturbations, is infeasible because
sciPlex) provides an innovative platform for integrating single-cell of the exponential growth in complexity.
sequencing technologies with targeted perturbations, such as gene To address the challenges associated with large-scale perturbation
knockouts, knockdowns and chemical treatments, to reveal gene func- screens, various computational methods have been developed to pre-
tions, regulatory networks and mechanisms driving cell states at a dict perturbation effects. These computational methods can generally
single-cell resolution1–3. Despite its immense potential, the application be classified into two major categories on the basis of their application
of single-cell perturbation sequencing at large scales faces substantial scenarios. The first category, defined as the ‘cellular context generali-
practical and economic barriers. Conducting large-scale perturbation zation scenario’, involves training a model on data measured in a set
1Department of Hematology, Tongji Hospital, Frontier Science Center for Stem Cell Research, Bioinformatics Department, School of Life Sciences and
Technology, Tongji University, Shanghai, China. 2Shanghai Key Laboratory of Anesthesiology and Brain Functional Modulation, Clinical Research Center
for Anesthesiology and Perioperative Medicine, Translational Research Institute of Brain and Brain-Like Intelligence, Shanghai Fourth People’s Hospital,
Frontier Science Center for Stem Cell Research, Bioinformatics Department, School of Life Sciences and Technology, Tongji University, Shanghai,
China. 3State Key Laboratory of Autonomous Intelligent Unmanned Systems, Frontiers Science Center for Intelligent Autonomous Systems, Ministry of
Education, Shanghai Research Institute for Intelligent Autonomous Systems, Shanghai, China. 4Institute for Data-Driven Tumor Immunology, Chongqing
Medical University, Chongqing, China. 5Institute of Biophysics, Chinese Academy of Sciences; College of Life Sciences, University of Chinese Academy of
Sciences, Beijing, China. 6These authors contributed equally: Zhiting Wei, Yiheng Wang, Yicheng Gao, Shuguang Wang. e-mail: lab7182@tongji.edu.cn;
18alexanderm117@tongji.edu.cn; qiliu@tongji.edu.cn
Nature Methods | Volume 23 | February 2026 | 451–464 451
Analysis https://doi.org/10.1038/s41592-025-02980-0
of cellular contexts (such as cell lines) for a specific perturbation and of the performance of foundation models compared with baseline
then using the model to predict the effects of that perturbation in a dif- models is performed. By analyzing datasets of varying sizes, it is found
ferent, unobserved cellular context. A prominent tool in this category that baseline models tend to perform better on smaller training data-
is scGen, which is based on variational autoencoders and enables pre- sets. In contrast, foundation models tend to perform better in terms
dictions to be generated across diverse cellular contexts4. The second of both prediction accuracy and generalizability, when the fine-tuning
category, defined as the ‘perturbation generalization scenario’, involves datasets are sufficiently large. Based on our findings, we have devel-
training a model on the effects of a set of perturbations, which are oped a tool selection guidance tailored to dataset characteristics,
usually measured in a specific cellular context, and then using the enabling researchers to quickly select the most suitable methods;
model to predict the effects of unseen perturbations. Notable methods (3) For challenging cases where perturbation effect prediction needs
in this category include GEARS, which is based on knowledge graphs to be generalized to a new cellular context that is substantially differ-
of gene–gene relationships that can be generalized to unseen ent from the model’s training contexts, we explored a cellular context
perturbed genes5. embedding strategy as a potential approach to enhance generaliza-
In recent years, numerous methods have been presented in tion. This strategy was found to improve perturbation effect predic-
the field of single-cell perturbation effect prediction for both of tion in our evaluation.
the aforementioned scenarios. In addition, single-cell foundation Overall, our study underscores the importance of tailoring per-
models have established a paradigm for in silico perturbation predic- turbation prediction methods to specific data characteristics and
tion through pretraining and fine-tuning strategies6–9. Models such as highlights the need for further improvements in model design to
scGPT and scFoundation, which utilize large-scale pretrained archi- increase generalizability. We anticipate that the insights gained from
tectures, have demonstrated the potential to predict perturbation this benchmark will facilitate the development of methods with greater
effects across diverse cellular and perturbation contexts6,7. However, effectiveness and generalizability for diverse single-cell perturbation
recent studies have continued to raise concerns regarding the true prediction tasks.
effectiveness of these models10–12. Specifically, many of these methods
do not outperform baseline models or linear models on the basis of Results
straightforward assumptions when they are evaluated across multiple A comprehensive framework for benchmarking single-cell
datasets. This has led to a growing call for more comprehensive and perturbation effect prediction
rigorous assessments of these methods. To address this, researchers Methods. To thoroughly assess the performance of prediction meth-
should carefully examine several key aspects of single-cell perturba- ods in this field, we developed a comprehensive benchmark framework,
tion effective modeling methods, including the comprehensiveness including state-of-the-art methods, diverse datasets and rigorous
of the test scenarios they are designed for, the diversity of the datasets evaluation metrics (Fig. 1a). In this study, we evaluated the methods
used and the thoroughness of the evaluation metrics. Only by properly across two key scenarios: cellular context generalization and pertur-
and thoroughly addressing these factors can we obtain a reliable and bation generalization (Fig. 1a). While we aimed to include a diverse set
clear understanding of the strengths and limitations of these methods. of methods in our evaluation, several tools were excluded for specific
Furthermore, it is crucial for an evaluation framework to go beyond reasons (Supplementary Note 1). As a result, in the cellular context
performance tests and present applicable guidance and solutions generalization scenario, we examined 10 methods from published
for the development of more reliable and generalizable models in studies: biolord16, CellOT14, inVAE17, scDisInFact18, scGen4, scPRAM15,
this domain. scPreGAN19, SCREEN20, scVIDR21 and trVAE22. In the perturbation gener-
In this study, we provide a comprehensive evaluation of single-cell alization scenario, we examined another 14 methods: AttentionPert23,
perturbation prediction methods, where the main procedure is as fol- biolord16, CPA24, GEARS5, GenePert25, linearModel12, scFoundation6,
lows: (1) In the cellular context generalization scenario, we compare 14 scGPT7, chemCPA26, scouter27, scELMo28, GeneCompass29, PRnet30 and
methods across 12 datasets that cover a wide range of cellular contexts cycleCDR31. Given the growing concerns raised in recent literature
from different cell lines, participant samples, and even different spe- regarding the effectiveness of advanced machine learning models,
cies to investigate the generalizability of the methods across different particularly foundation models, we also included 4 baseline models
cellular contexts; (2) in the perturbation generalization scenario, we named baseReg, baseMLP, baseControl and trainMean (Methods).
compare 18 methods across 17 datasets to investigate generalizability These baseline models serve as benchmarks to determine whether
to unseen perturbations; (3) in both scenarios, we use 6 evaluation more complex methods learn additional meaningful information
metrics to comprehensively assess prediction accuracy, including from the data. In total, our evaluation includes 23 published methods
the mean squared error (MSE), Pearson correlation coefficient delta and 4 baseline models, covering a broad spectrum of methodological
(PCC-delta)5, E-distance13, Wasserstein distance14, Kullback–Leibler approaches in single-cell perturbation effect prediction.
divergence (KL-divergence) and common differentially expressed
genes (Common-DEGs)15; and (4) we utilize simulated data in both Datasets. The systematic benchmark relies on a collection of diverse
scenarios to assess the scalability of the evaluated methods and to datasets designed to reflect real-world biological challenges. For
investigate impacts of noise and sparsity on the performance of those the cellular context generalization scenario, we curated 12 datasets
methods. Analysis results obtained from the comprehensive bench- categorized on the basis of the cellular context1,32–37 (Fig. 1b). These
mark are presented, including the following: (1) Our study indicated datasets include 8 that are focused on cross-cell-line predictions
that there is no ‘one-size-fits-all’ method that works well across all (predicting perturbation effects in a new cell type), 3 that are focused
datasets. Some limitations of current methods, including foundation on cross-patient predictions (predicting perturbation effects in
models for both test scenarios, were identified. In the cellular context a new patient) and one that is focused on cross-species predictions
generalization scenario, owing to limitations in algorithm design, that (predicting perturbation effects in a new species). Each dataset
is, neglecting the specificity of perturbation responses across differ- challenges the ability of the models to generalize perturbation
ent cellular contexts (intercellular heterogeneity, or for simplicity effects across contexts. Additionally, the datasets can be further
inter-heterogeneity), all methods likely exhibit poor generalizability. grouped on the basis of the presence of perturbation metadata.
Specifically, when predicting the effects of perturbations in a new Of the 12 datasets, 7 contain only perturbation data (single-condition
cellular context that is quite different from the training datasets, all datasets), and the remaining 5 include additional perturbation
methods performed poorly, even worse than the baseline models; (2) metadata, that is, time-point/dosage information (multi-condition
In the perturbation generalization scenario, an objective evaluation datasets).
Nature Methods | Volume 23 | February 2026 | 451–464 452
Analysis https://doi.org/10.1038/s41592-025-02980-0
Cellular context generalization Perturbation generalization
Cell
Deep learning model Foundation model
GRN model
Nature Methods | Volume 23 | February 2026 | 451–464 453
eneG
Perturbation
Cell
eneG Perturbation ?
niarT tciderP etareneG Cell
eneG
Perturbation
Cell
eneG Perturbation
niarT tciderP etareneG
12 datasets 17 datasets
(genetic, chemical,
environmental factors) (Genetic, chemical)
7 single-condition 5 multi-conditions 13 genetic 4 chemical
3 Perturb 3 Perturb, time 2 Perturb, dosage 4 combo
AI
Linear model
Accuracy
Ground truth Prediction
ESM
nietsressaW
atled-CCP
sGED-nommoC
Robustness Scalability
Overall rank
Method 1
Method 2
Method 3
Level of noise
Limitation and insights
ycaruccA
Level of sparsity
ycaruccA
emiT
Number of
perturbations/cells
yromeM
a
Scenarios
Kang et al.
Haber et al.
Norman et al.
Datasets Replogle et al.
...
9 single 3 single 1 combo
14 methods 18 methods
scGen, CellOT, trVAE, scELMo, scFoundation, CPA, biolord,
Methods inVAE, scPreGAN, SCREEN, scDisInFact, scGPT, GeneCompass, baseMLP, chemCPA,
scPRAM,baseMLP, biolord, AttentionPert, baseControl, PRnet,
baseControl, trainMean, scVIDR scouter,GEARS, trainMean, cycleCDR
baseReg GenePert,linearModel baseReg
Population-average
metrics MSE,
PCC-delta,
E-distance
Evaluation
Population-distribution
metrics Wasserstein, Out of . . m . emory
KL-divergence, GB
Common-DEGs
Number of
perturbations/cells
b
ecnegrevid-LK
ecnatsid-E
?
Dataset ID/name Contexts Conditions Context counts Perturbation counts Dataset ID/name Contexts Conditions Context counts Perturbation counts
CrossSpecies Species Multi 4 2 KangCrossCell Cell lines Single 8 2
Afriat Cell lines Multi 2 3 Parekh Cell lines Single 3 11
McFarland Cell lines Multi 5 12 KangCrossPatient Patients Single 8 2
TCDD Cell lines Multi 6 2 Haber Cell lines Single 8 4
Sciplex3 Cell lines Multi 3 10 KaggleCrossPatient Patients Single 3 11
CrossPatient Patients Single 6 3
KaggleCrossCell Cell lines Single 5 11
c
Perturbation Is Perturbation
Dataset ID/name
type combination counts
Perturbation Is Perturbation
Dataset ID/name
Adamson No 77 type combination counts
Frangieh No 212 Norman Yes 227
TianActivation No 93 Wessels Yes 128
Genetic
TianInhibition No 181 Schmidt Yes 148
Replogle-exp7 Genetic No 105 Reploge-exp6 Yes 70
Replogle-exp8 No 62 Sciplex3-A549 No 188
Papalexi No 26 Sciplex3-MCF7 No 188
Chemical
Replogle-RPE1essential No 1,331 Sciplex3-K562 No 188
Replogle-K562-essential No 1,618 Sciplex3-comb Yes 32
Fig. 1 | Workflow and datasets for benchmarking the single-cell perturbation to evaluate the performance of these algorithms, and we also assessed their
effect prediction. a, We classified the single-cell perturbation effects robustness, scalability and consumed computational resources. b, Detailed
prediction tasks into ‘cellular context generalization scenario’ and ‘perturbation information of the 12 single-cell perturbation datasets used in cellular context
generalization scenario’. In the cellular context generalization scenario, we generalization scenario. c, Detailed information of the 17 single-cell perturbation
benchmarked 14 methods across 12 datasets. In the perturbation generalization datasets used in perturbation generalization scenario.
scenario, we benchmarked 18 methods across 17 datasets. We adopted 6 metrics
Analysis https://doi.org/10.1038/s41592-025-02980-0
For the perturbation generalization scenario, we curated 17 definition (Supplementary Note 2). Metrics calculated for this
datasets that broadly cover 2 perturbation types (Fig. 1c), includ- smaller, meaningful set of genes are generally preferred in the
ing (1) 13 genetic perturbation datasets, of which 9 focus on single field, as genes with modest expression change do not contrib-
pertur bations and 4 on combined perturbations, and (2) 4 chemical ute substantially to understanding perturbation effects48.
perturbation datasets, including 3 single-perturbation datasets and Therefore, for conciseness, we present the results based on the
one combined-perturbation dataset3,38–46. In total, the numbers of top 100 most differentially expressed genes in the main text,
perturbations in these datasets range from 25 to 1,618, ensuring their and the analysis results of all genes are provided at https://
broad applicability to evaluate the methods. bm2-lab.github.io/scPerturBench-reproducibility/. Moreover,
we demonstrate that the number of most differentially
Evaluation metrics and assessment of methods. To evaluate the expressed genes selected does not affect our main conclusions
current tools for single-cell perturbation prediction comprehensively, (Supplementary Note 2). We use a ranking-based method to fur-
we focused on three key metrics, that is, accuracy, robustness and ther compare the performance of the selected methods on the
scalability. basis of the six metrics (Methods)49.
(2) To evaluate robustness to technical variation, we generated sim-
(1) Accuracy evaluation presents a particular challenge because of ulated datasets based on real data by introducing controlled lev-
the lack of consensus on the most suitable evaluation metrics in els of noise and sparsity, allowing us to assess how such artifacts
the field. A variety of metrics have been proposed for evaluat- impact method performance50. In the main text, we focus on
ing single-cell perturbation effect prediction performance, but population-average metrics—specifically MSE and PCC-delta—to
their reliability and informativeness are still debated. To ensure a evaluate model robustness under these challenging conditions,
fair, interpretable and representative evaluation of perturbation as these metrics more accurately reflect model performance
prediction models, we conducted an extensive literature survey and are computationally efficient47. Importantly, this analysis is
covering 28 existing tools and benchmarking studies in the field, intended to assess robustness to technical artifacts rather than
with a particular focus on a study by Ji et al., to guide our selection biological variability in perturbation responses.
of evaluation metrics47. From these sources, we identified 19 evalu- (3) To evaluate scalability, an essential consideration for practical
ation metrics and selected three population-average metrics and application, we systematically varied the sizes of the datasets.
three population-distribution metrics (Supplementary Table 1, We measured computational performance in terms of runtime
Methods and Extended Data Fig. 1): (a) Population-average met- and CPU utilization to provide a detailed analysis of resource ef-
rics. MSE is among the most stable and widely used metrics in ficiency across tools. This multifaceted evaluation framework
single-cell RNA-sequencing (RNA-seq) evaluation47; E-distance, ensures a thorough and balanced assessment of single-cell per-
selected as another top-performing metric, provides a robust turbation prediction tools, addressing both methodological
and informative assessment by primarily capturing the difference rigor and practical applicability.
in average effects between predicted and actual gene expression
profiles13; PCC-delta, introduced by GEARS and scGPT, has an ad- Benchmarking analysis for the cellular context generalization
vantage over the traditional PCC in that it better captures the direc- scenario
tional consistency of predictions5,7; (b) Population-distribution In the cellular context generalization scenario, we evaluated the predic-
metrics. Wasserstein distance and KL-divergence were selected tion of known perturbations in previously unobserved cellular contexts.
as the most widely used metrics for evaluating distribution-level The cellular context generalization scenario was further divided into
prediction performance. They quantify the discrepancy between two distinct test settings by partitioning the training and test datasets
predicted and actual distributions of single-cell profiles, which is into independent and identically distributed or in-distribution (i.i.d.)
essential for capturing heterogeneity and higher-order statistical and out-of-distribution (o.o.d.) settings (Fig. 2a)14,18. In the o.o.d. set-
properties. The Common-DEGs metric measures the accuracy of ting, we used leave-one-out cross-validation, where one context was
the predicted most differentially expressed genes, which is criti- held out as the test set, while the remaining contexts served as the
cal for downstream functional analyses and biological interpre- training set (Supplementary Note 3). In the i.i.d. scenario, the model
tation15. In our analysis, we prior itized using MSE and PCC-delta was trained using the same training data as in the o.o.d. scenario but
as the representative metric for model performance47. PCC-delta with access to some of the cells from the held-out context. These extra
was particularly emphas ized due to its bounded range from −1 training cells and the test cells were assumed to be independent and
to 1, which allows for intuitive and interpretable assessment of identically distributed14. In practical applications, the o.o.d. scenario
model effectiveness. Moreo ver, both metrics are computationally is more commonly encountered, as we often aim to predict the effects
efficient, making them well-suited for large-scale benchmarking. of perturbations in a new, previously unseen context. Furthermore,
the i.i.d. setting can be considered a special case of the o.o.d. scenario,
We calculated the metrics in two ways: for all genes and for the where the test context has a highly similar counterpart in the training
top 100 most differentially expressed genes ranked by abso- data. Therefore, in the following benchmark analysis, we focus primar-
lute effect sizes. It should be noted that, for clarity, we use the ily on the o.o.d. setting scenario, and the results of the i.i.d. setting
term ‘DEGs’ in a broader sense than its conventional statistical scenario can be found in Supplementary Fig. 1.
Fig. 2 | Benchmarking results for the o.o.d. setting in the cellular context datasets. Data are presented as mean values with error bars indicating standard
generalization scenario. a, A schematic diagram illustrating the splitting of errors of the mean. N = 4, 4, 42, 6 and 27 predictions for CrossSpecies, Afriat,
training and testing data in the i.i.d. and o.o.d. settings. Different colors represent McFarland, TCDD and sciPlex3 datasets. f, Performance overview of scDisInFact
different cellular contexts. b, Performance overview of the 14 evaluated methods, and scDisInFact baseline (without considering covariates) across multi-condition
including accuracy, robustness and scalability. Data are presented as mean datasets. Data are presented as mean values with error bars indicating standard
values with error bars indicating standard errors of the mean. N = 12 datasets. errors of the mean. N = 4, 4, 42, 6 and 27 predictions for CrossSpecies, Afriat,
CV, coefficient of variation. c, Overview of PCC-delta for the 14 methods across McFarland, TCDD and sciPlex3 datasets. g, MSE and PCC-delta results for the
the 12 datasets. d, Silhouette scores calculated using three different clustering 14 methods on simulated datasets with varying levels of noise and sparsity.
labels from the Afriat and TCDD datasets. e, Performance overview of biolord h, Runtime and CPU memory usage of the 14 methods on simulated datasets
and the biolord baseline (without considering covariates) across multi-condition with varying sizes.
Nature Methods | Volume 23 | February 2026 | 451–464 454
Analysis https://doi.org/10.1038/s41592-025-02980-0
a b
Training data
Testing data
o.o.d. setting
i.i.d. setting
c d
h
Nature Methods | Volume 23 | February 2026 | 451–464 455
ecnamrofreP
Cellular context generalization o.o.d. setting
Method Properties Accuracy Robustness Scalability
Time Memory
LanguageGPU Metrics Sparsity Noise (min) (GB)
Ranking
scGen 3 2 1.8 2.5
inVAE 2 1 2 2.1 4.5 1
trVAE 1 2 1 1 6.5 3.8
VAE based scVIDR 3 1 2 5.5 14
scPRAM 1 1 3.8 6.1
biolord 3 2 0.9 3.4
scDisInFact 2.1 4.9 0 Low
Optimal transport CellOT 2 2 3 1,423 2.9
based SCREEN 3 31.2 3.9
GAN based scPreGAN 2 111.4 3.8 1 High
trainMean 2 1 0.2 2 1.3
baseControl 3 0.3 1 1.1
baseMLP 0.3 3.2
baseReg 1 0.2 3 1.4
0 1
Overall MSE PCC-delta E-distance Wasserste
K
i
L
n -diverge
C
n
o
c
m
e mon-DEGs C
C
V
V
M PC SE C-delta C
C
V
V
M PC S C E -delta
Methods
1,000 5,000 10,000 50,000
Cell counts
)nim(
emiT
1 perturbation
1 3 9
Perturbation counts
)nim(
emiT
10,000 cells
)BG(
yromeM
1,000 5,000 10,000 50,000
P
1
erturbati
3
on coun
9
ts
Cell counts
)BG(
yromeM
0.15
0.10
0.05
0
Cell type PerturbationTime point
scGen
inVAE
trVAE
scVIDR
scPRAM
biolord
scDisInFact
1 perturbation 10,000 cells CellOT
1,300 2,500 20 6 s S c C P R r E e E G N AN
1,200 2,000 15 trainMean
1,500 4 baseControl
1, 2 1 0 0 0 0 1,000 10 b b a a s s e e M Re L g P
100 500 5 2
0 0 0
erocs
etteuohliS
Afriat
0.3
0.2
0.1
0
Cell type Perturbation Dosage
erocs
etteuohliS
Datasets with additional covariates
scGen
inVAE
trVAE
scVIDR
scPRAM PCC-delta
biolord 0 Low
scDisInFact
CellOT
SCREEN 1 High
scPreGAN TCDD
trainMean
Conditions Perturbation
Perturbation + time point
Perturbation + dosage
0 1
ecnamrofreP
gniknaR
3
2
2
1 1
3 3 3
1 2
2 1
2 3 3 2 2 2 1
2 3 1 2
1 1 3 1 3 3 1
14
3 2 2 2
1 1 1
3 1 2 1 1
3
2
2 1 1 2 3
baseControl baseMLP
baseReg
e
MSE PCC-delta E-distance KL-divergence Wasserstein Common-DEGs
3 1.0 2 2 0 5 40 400 0.1 Meth B o io d lo s rd
2 1 0. 0 5 1 1 0 5 5 3 2 10 0 0 3 2 10 0 0 0 0 0 0.05 B b io as lo e r l d ine
0 0 0 0 0
f
4 3 2 1 − 0 0 0 . . . 5 2 2 0 0 5 5 3 2 10 0 0 4 3 2 10 0 0 0 4 3 2 10 0 0 0 0 0 0 0 0 0 . . 0 10 5 Met s s h c c b o D D a d i i s s s s e I I n n li F F n a a e c c t t
0 0 0 0 0
CrossSpecies Af M ria c t Farland TCDD sciPlex CrossSpecies A M fri c a F t arland TCDD sciPlex CrossSpecies A M fri c a F t arland TCDD sciPlex CrossSpecies A M fr c ia F t arland TCDD sciPlex CrossSpecies A M fr c ia F t arland TCDD sciPlex CrossSpecies M Af c r F ia a t rland TCD s D ciPlex
g
Level of noise
atled-CCP
0 0.1 0.30.50.7 0.9 0 0.1 0.30.50.7 0.9
Level of sparsity
atled-CCP
0 0.1 0.3 0.5 0.7 0.9
Level of noise
ESM
10 1.0 1.0
0.5
0.5 5
0
0
0
0 0.1 0.30.5 0.7 0.9
Level of sparsity
ESM
Baseline model
KangCrossCell Par
K
e
a
k
n
h gCrossPatient H
K
a
a
b
g
e
g
r leCrossPatient CrossPati
K
en
ag
t gleCrossCell CrossSpecies Afriat McFarland TCDD sciPlex
7.5
5.0
2.5
0
Analysis https://doi.org/10.1038/s41592-025-02980-0
In the o.o.d. scenario, trVAE, CellOT and inVAE achieved the data50. As the noise and sparsity in the data increased, the perfor-
best overall performance (Fig. 2b). When selecting a method, users mance of all methods decreased markedly (Fig. 2g). We also noted
can consider the specific needs of their analysis. For example, if the that the performance of the algorithms deteriorated more severely for
objective is to minimize population-average metrics such as MSE, high-sparsity data, indicating that their performance is more sensitive
inVAE and trVAE are the most suitable options. If the objective is to to data sparsity (Fig. 2b). In terms of scalability (Supplementary Note 8),
minimize population-distribution metrics such as KL-divergence and none of the algorithms encountered out-of-memory issues, and their
Common-DEGs, scVIDR and scPRAM are the most suitable options. runtimes were within acceptable limits, except for CellOT (Fig. 2h).
Furthermore, we found that, in contrast to population-average metrics, The increased computational complexity of CellOT arises from its
all methods performed relatively poorly on population-distribution explicit modeling of cell-to-cell heterogeneity, and it currently does
metrics, particularly on the Common-DEGs metric. For instance, in the not support GPU acceleration.
Haber dataset, although the top-performing method achieved an aver- In summary, the following insights are obtained regarding the
age PCC-delta of 0.86, uniform manifold approximation and projection benchmark analysis of the cellular context generalization scenario:
visualization revealed a substantial discrepancy between the predicted (1) trVAE, CellOT and inVAE demonstrated the best overall perfor-
and ground-truth distributions (Supplementary Fig. 12). Furthermore, mance on single-condition datasets. For accurate prediction of DEGs,
on average, only about 10% of the true most differentially expressed scPRAM is the optimal choice. Additionally, when the dataset includes
genes were recovered. We conduct a more in-depth discussion of the perturbation dosage information, such as in chemical perturbation
underlying reasons for this in the next section on the ‘perturbation datasets, scVIDR is the best method to use. (2) Models that consider
generalization scenario’. covariates affecting cellular responses provide more accurate pre-
In addition, among the 12 benchmark datasets used in this study, dictions of single-cell perturbation effects. However, most existing
5 included additional perturbation metadata, such as time-point/dos- tools do not incorporate covariates, and those that do are still far
age information, and these are classified as multi-condition datasets from being sufficiently accurate. Given the increasing availability
(Fig. 2c). Among the 14 methods tested, only biolord, scDisInFact and of multi-condition data in the single-cell perturbation field, there
scVIDR utilized these additional metadata16,18,21. Through uniform is a pressing need to develop high-performing models tailored for
manifold approximation and projection visualization, calculation of sil- multi-condition data, which can fully exploit covariate information to
houette score51 and multifactor analysis of variance (Fig. 2d, Extended achieve improved prediction accuracy. (3) All the algorithms’ perfor-
Data Figs. 2 and 3, Supplementary Fig. 7and8, Supplementary Notes 4 mance was affected by data noise and sparsity, with greater sensitivity
and5 and Supplementary Table 2), time-point/dosage covariates gen- to sparsity. (4) In terms of scalability, none of the algorithms encoun-
erally had a substantial effect on the cellular response. We evaluated tered out-of-memory issues, and their runtimes were within acceptable
the performance of biolord and scDisInFact on these datasets, as well limits, except for CellOT.
as the performance of scVIDR on the TCDD and sciPlex3 dataset, to
assess whether these tools were optimal for use with multi-condition Limitations of current methods in the cellular context
datasets. However, biolord and scDisInFact did not outperform the generalization scenario
tools that did not incorporate covariates on these datasets (Fig. 2c). We observed substantial performance variability among the 14 algo-
This may be because, although the time-point/dosage covariates rithms across the 12 datasets in the cellular context generalization
provided useful information, the baseline performance of biolord test. In some datasets, all methods achieved excellent performance,
and scDisInFact—without incorporating covariate information—was whereas in others, the performance of all methods was notably poor.
relatively suboptimal. As a result, despite performance improvements For example, in the Afriat dataset, even the trainMean baseline per-
upon the inclusion of covariates, these models did not achieve top formed exceptionally well, with a median PCC-delta of 0.92 and an
rankings. To validate this, we calculated the baseline performance average value of 0.85 (Fig. 2c). On the other hand, in datasets such
of biolord and scDisInFact on these datasets. In the comparison, the as KaggleCrossCell, all machine learning models performed poorly,
performance of biolord was generally better than that of its baseline with a median PCC-delta of 0.54 and an average value of 0.52 (Fig. 2c).
model (Fig. 2e). This analysis indicated that incorporating covariate To investigate the underlying reasons for these discrepancies, we
information improved the model’s performance. However, in some conducted the following analyses: (1) We compared the performance
cases, scDisInFact did not improve from its baseline value (Fig. 2f). of the methods in the i.i.d. and o.o.d. scenarios. As mentioned earlier,
This aligns with the primary design focus of scDisInFact, which is to in the i.i.d. scenario, the model was trained using the same training
address batch effects and integrate single-cell datasets rather than to data as in the o.o.d. scenario but with additional access to half of the
predict perturbation effects18. The scVIDR method achieved the best cells from the held-out context. In other words, in the i.i.d. scenario,
overall performance on the TCDD dataset and ranked second on the we can assume that for each test context, the training dataset always
sciPlex3 dataset. Therefore, for a dataset that includes perturbation includes a context that is highly similar to it. Therefore, the predic-
dosage information, scVIDR is an optimal choice. tion task in i.i.d. scenarios is simpler, while making predictions for
Next, we assessed the robustness of the perturbation effect predic- the same cellular context in o.o.d scenarios is more challenging and
tion algorithms to technical noise and data sparsity using simulated places greater demands on the model’s generalization capabilities.
Fig. 3 | Limitation of current methods in the cellular context generalization similarities between contexts in the KangCrossCell and Haber datasets.
scenario. a, Comparison of the performance between the o.o.d. and i.i.d. e,f, These sub-figures illustrate how the algorithm’s PCC-delta and MSE
settings across all datasets. Data are presented as mean values with error bars performance varies with changes in the training context. The x axis represents
indicating standard errors of the mean. N = 217 predictions. b, Comparison of the the dissimilarity between the test context and the newly added training context,
performance between the o.o.d. and i.i.d. settings in the CrossPatient dataset. with larger values indicating lower similarity. The y axis shows the change in
Box plots show the median (center line) and the 25th and 75th percentiles the PCC-delta metric for the test context after adding the new training context.
(bounds of the box), and whiskers extend to 1.5 times the interquartile range Positive values indicate improved performance, while negative values indicate
(IQR); N = 10 predictions. c, Spearman’s correlation between MSE or PCC-delta diminished performance. A linear regression line with 95% confidence interval
and inter-heterogeneity. We combined the results of the test contexts from the is shown. PCCs were calculated, and statistical significance was assessed using
12 datasets, with each point representing a test context in a specific dataset. two-sided t-tests. Adjustments were not made for multiple comparisons.
A linear regression line with 95% confidence interval is shown. Statistical g, Recommendation of suitable software for users based on their needs and
significance was assessed using two-sided t-tests. d, Heat maps showing the the characteristics of the data at hand.
Nature Methods | Volume 23 | February 2026 | 451–464 456
Analysis https://doi.org/10.1038/s41592-025-02980-0
a b
1.5
0.3 0.2 1.0 0.1 0
0.5
0 scGen inVAE trVAE scVIDR scPRA M biolo
s
r
c
d DisInFact CellOT SCREEN scPreGAN train Me
b
a
a
n seControl base MLP baseReg
o.o.d. setting
i.i.d. setting
f g
trVAE
Population-average
Yes
inVAE
Running time
Do you aim to minimize efficient?
population-average or
Others population-distribution metrics? CellOT No
What covariate factor
do you have? trVAE
Yes
Population-distribution
scPRAM
Dosage
Does your perturbation scVIDR
dataset contain a
covariate factor?
trVAE
Population-average
Yes
No inVAE
Running time Do you aim to minimize efficient?
population-average or
population-distribution metrics? CellOT No
trVAE
Population-distribution
scPRAM
Nature Methods | Volume 23 | February 2026 | 451–464 457
ESM
CellOT trVAE scPreGAN inVAE SCREEN scDisInFact scGen
0 0 0 0 . . . 0 . 4 3 2 1 0 0 0 . . . 6 4 2 0 0 0 . . . 3 2 1 0 0 0 0 0 0 . . . . . . 6 4 3 5 2 1 0 0 0 . . . 6 4 2 0 0 0 . . . 3 2 1
0.4 0.3 0.2 0.1 0 ESM
biolord scPRAM scVIDR trainMean baseControl baseMLP baseReg
0 0 0 0 . . . . 4 3 2 1 0 0 0 . . . 3 2 1 0 0 0 0 . . . . 4 3 2 1 0 0 0 0 . . . . 4 3 2 1 0 0 0 0 . . . . 4 3 2 1 0 0 0 0 . . . . 4 3 2 1
o.o.d. se i. t i. t d in . g setting o.o.d. se i. t i. t d in . g setting o.o.d. se i. t i. t d in . g setting o.o.d. se i.i t . t d in . g setting o.o.d. se i. t i. t d in . g setting o.o.d. se i.i t . t d in . g setting o.o.d. se i. t i. t d in . g setting
ESM
r = –0.78, P = 0.0027
1
0
2 4 6 8 10
ESM
0.4 r = –0.73, P = 1.5 × 10−5
0.3
0.2
0.1
0
10 20 30
ESM
1.0
0.5
0
0 10 20 30 Inter-heterogeneity
ESM
1.00
0.75
0.50
0.25
0 10 20 30 Inter-heterogeneity
atled-CCP
0.75
0.50
0.25
0
scGen inVAE trVAE scVIDR scPRA M biolo
s
rd cDisInFact CellOT SCREEN scPreGAN train Me
b
a
a
n seControl base MLP baseReg
atled-CCP
o.o.d. setting i.i.d. setting
c
0.2
0.1
0
−0.1
2 4 6 8 10
atled-CCP
r = –0.96, P = 1.3 × 10−6 0.4
0.3
0.2
0.1
0
10 20 30
atled-CCP
r = 0.71, P = 3.91 × 10−10 r = –0.47, P = 0.000196
e
DC
CD14_mono
CD16_mono
B
T r = –0.71, P = 3.9 × 10−5
NK
CD4_T
CD8_T
1
0
−1 Dissimilarity Disimilarity
Dissimilarity
Dissimilarity
noitalerroc
s’nosraeP
d
KangCrossCell
1
0
−1
Enterocyte_progenitor
Enterocyte
Stem
TA_Early
TA Goblet
Tuft
Endocrine
noitalerroc
s’nosraeP
Testing contexts
Training contexts
Haber
Testing contexts
Training contexts
Analysis https://doi.org/10.1038/s41592-025-02980-0
As shown in Fig. 3a,b, the performance of each method in the i.i.d. GenePert25, linearModel12, scouter27, scFoundation6, scGPT7, scELMo28
setting is better than that in the o.o.d. setting, which is expected. (2) and GeneCompass29—as well as 4 baseline models, on 13 datasets of
We calculated the similarity between the test context and each con- varying sizes, including between 25 and 1,618 perturbations. In addi-
text in the training dataset via the E-distance, and the minimum value tion, recent studies suggest that for predicting gene expression profiles
was used to assess the degree of similarity between the test context under combined perturbations, the simplest additive model—which
and the training context (inter-heterogeneity). As shown in Fig. 3c, predicts the effects of combined perturbations as the sum of the effects
when the inter-heterogeneity between the test context and training of two single perturbations—often outperforms complex deep learn-
context was low, the methods generally performed well. In contrast, ing models or foundation models such as scGPT12. However, these
when the inter-heterogeneity between the test context and training conclusions were derived from a single dataset. To address this limi-
context was high, the performance of the methods was poor. This tation in the previous evaluations, we included 4 datasets focused
result indicated that it is still challenging for the current methods to on combined perturbations (two-gene combinations) in our evaluation.
be generalized to a new cellular context that is dissimilar to the train- (2) Chemical perturbation effect prediction. Similarly, in chemical
ing cellular context (Extended Data Fig. 4). (3) We conducted holdout perturbation effect prediction scenarios, datasets are categorized
experiments on kangCrossCell and Haber datasets to simulate a test into single-perturbation datasets and combined-perturbation datasets.
to mimic different degrees of inter-heterogeneity (Supplementary Among the methods tested, biolord16, chemCPA26 and cycleCDR31 are
Note 9). We first selected several cell lines as the test contexts and then limited to single-perturbation datasets.
sequentially added contexts that were either similar or dissimilar to the
test contexts from the training dataset to observe the performance of Genetic perturbation setting. Across the 9 single-perturbation
each method (Fig. 3d). When contexts with greater similarity to the datasets, GenePert, scGPT and scouter demonstrated the best
test context were added to the training dataset, the prediction per- overall performance (Fig. 4a). Both GenePert and scouter leverage
formance generally improved considerably. However, when contexts ChatGPT-derived textual descriptions as embeddings. It is surprising
with low similarity to the test context were added, the performance that models relying on unaligned natural language embeddings out-
either showed little improvement or remained unchanged (Fig. 3e,f perform those leveraging transcriptome-informed embeddings. To
and Supplementary Fig. 9). investigate the underlying source of performance gain, we conducted
In summary, the analysis of the benchmark results in the cellular an ablation study designed to isolate the contribution of different
context generalization scenarios shows that the performance of the embedding types. Specifically, we replaced the original embeddings
evaluated methods is highly dependent on the inter-heterogeneity. in GenePert and scouter with five alternative embeddings: Gene-
When predicting perturbation effects in a new cellular context that Compass29, geneformer9, scBERT8, scELMo28 and scGPT7, while keeping
differs substantially from the training datasets, all methods likely all other model parameters and training procedures identical. Among
performed unsatisfactorily, highlighting their limited generalizability. these, scELMo and ChatGPT-based embeddings are derived from
We believe that accounting for intercellular heterogeneity is crucial for large language models (LLMs) trained on biomedical corpora, whereas
enhancing the generalizability of current models across diverse cellular GeneCompass, geneformer, scBERT and scGPT are derived from
contexts. Finally, user guidance is provided regarding the benchmark foundation models trained on large-scale single-cell transcriptomic
analysis of the cellular context generalization scenario (Fig. 3g). datasets. We evaluated model performance using MSE and PCC-delta,
as these metrics more accurately reflect model performance and
Benchmarking analysis of the perturbation generalization are more computationally efficient50. As shown, across nine single-
scenario gene perturbation datasets, GenePert and scouter consistently
In the perturbation generalization scenario, we assess the ability of achieved top performance when using embeddings from scELMo and
models to predict the effects of previously unobserved perturbations ChatGPT (Supplementary Fig. 45). In contrast, performance dropped
within a specific cellular context. Depending on the type of pertur- markedly when transcriptome-informed embeddings (for example,
bation, this scenario can be further divided into two categories: genetic from scGPT and geneformer) were used. Notably, GenePert uses
perturbation effect prediction and chemical perturbation effect a linear regression model, and scouter uses a simple multilayer per-
prediction. (1) Genetic perturbation effect prediction. In this scenario, ceptron—yet both outperform more complex models such as GEARS
we evaluated the performance of 11 existing algorithms, including and biolord under certain settings. This suggests that the performance
the foundation models—AttentionPert23, biolord16, CPA24, GEARS5, advantage likely stems from the rich biological priors embedded
Fig. 4 | Benchmarking results for genetic perturbation in the perturbation made for multiple comparisons. d, Performance overview of the 15 evaluated
generalization scenario. a, Performance overview of the 15 evaluated methods, methods across the four genetic combination perturbation datasets. Box plots
including accuracy, robustness and scalability. Data are presented as mean show the median (center line) and the 25th and 75th percentiles (bounds of the
values with error bars indicating standard errors of the mean. N = 9 datasets. box), and whiskers extend to 1.5 times the IQR; N = 4 datasets. e, Performance
b, Performance of the 14 methods on MSE and PCC-delta metrics in the Replogel- overview of the 15 evaluated methods on PCC-delta and MSE metrics for the
RPE1essential and Replogel-K562essential datasets. The scFoundation method additive gene interaction subtype. Data are presented as mean values with error
encountered an ‘out-of-memory’ error on these two datasets, so results were bars indicating standard errors of the mean. f, Performance overview of the
not available. Box plots show the median (center line) and the 25th and 75th 15 evaluated methods on PCC-delta and MSE metrics for potentiation, epistasis
percentiles (bounds of the box), and whiskers extend to 1.5 times the IQR; N = 798, and redundant gene interaction subtypes. Data are presented as mean values
969 predictions for Replogel-RPE1essential and Replogel-K562essential datasets. with error bars indicating standard errors of the mean. g, Average performance
c, The relationship between performance differences and the similarities of the 15 methods on PCC-delta and MSE metrics across the comb-seen0, combo-
between testing and training perturbations (inter-heterogeneity). The x axis seen1 and combo-seen2 perturbation categories. h, Performance of the scGPT
represents inter-heterogeneity, with larger values indicating that a testing and trainMean baseline models on MSE and PCC-delta metrics across the comb-
perturbation is less similar to the training perturbations (Methods). The y axis seen0, combo-seen1 and combo-seen2 perturbation categories in the Schmidt
represents the performance difference in MSE between the CPA model and dataset. i, Runtime and CPU memory usage of the 15 methods on simulated
trainMean, with lower values indicating that CPA achieves better performance. datasets with varying cell counts. j, MSE and PCC-delta results for the 15 methods
Each point corresponds to a testing perturbation. A linear regression line on simulated datasets with varying levels of noise and sparsity. Due to the long
with 95% confidence interval is shown. PCCs were calculated, and statistical runtime of scFoundation, we did not evaluate its robustness.
significance was assessed using two-sided t-tests. Adjustments were not
Nature Methods | Volume 23 | February 2026 | 451–464 458
Analysis https://doi.org/10.1038/s41592-025-02980-0
a
b c
0
−0.1
−0.2
−0.3
−0.4
0 0.2 0.4 0.6
Inter-heterogeneity
d
Perturbation generalization (genetic combo)
Method Accuracy
0 1
Overall MS
P
E CC-de
E
l
-
ta distance
m
mon-DEGs
Co
g h
Nature Methods | Volume 23 | February 2026 | 451–464 459
ESM
0
−0.1
−0.2
−0.3
r = –0.5, P = 2.199 × 10−18 r = –0.53, P = 3.579 × 10−25
−0.4
ESM
Replogle-RPE1essential Replogle-K562essential
0 0.2 0.4 0.6
0.20 0.15 0.10 0.05
0
ESM
atled-CCP 0.8 0.6 0.4
0.2
0 0 1 2
Combo seen
Combo seen
ecnamrofreP daB
dooG
0.03 0.02 0.01
0
0.4
0.2
0
0 1 2
ESM
atled-CCP
scGPT trainMean 0.019
0.53
0.012
0.25
0.006
0.14
Perturbation generalization Method Properties Accuracy Robustness Scalability
(genetic single)
Time Memory
Language GPU Metrics Sparsity Noise (min) (GB) Ranking
CPA 3 1 6.7 21.1
1
biolord 2 152.2 3 6.2
Deep learning model scouter 3 3 1 2 7.3 13.3
AttentionPert 1 3 140.6 18.9 15
baseMLP 1 1 2 0.5 2 5.9
scELMo 3 66.9 22.3
Foundation model GeneCo s m c p G a P s T s 2 2 3 1 2 3 9 74 8 . . 3 4 2 2 1 1 . . 1 1 Pe 0 rformance Low
scFoundation 386.8 24.1
Graph model GEARS 57.4 17.2
GenePert 1 1 2 1 3 3 2 3 0.7 8.4 1 High
linearModel 2 3 2 1 1.7 16.4
Linear model trainMean 3 3 0.7 10.5
baseControl 2 1 1.1 9.2
baseReg 2 1 0.4 1 4.2
0 1
Overall MS
P
E CC-del
E
ta -distan
W
ce asse
K
rs
L
t
-
e
d
in iver
C
g
o
e
m
nc
m
e on-DEGs CV
C
M
V
S
P
E CC-delta CV
C
M
V
S
P
E CC-delta
Dataset: Schmidt 50 Methods
40
30 20
10
0 5,000 20,000 50,000 150,000
Cell counts
)BG(
yromeM
...Out of memory ...Out of memory
400
200
0 5,000 20,000 50,000 150,000
Cell counts
)nim(
emiT
Replogle-RPE1essential Replogle-K562essential
CPA CPA CPA CPA
GeneCompass scGPT biolord scGPT
scELMo GenePert AttentionPert GenePert AttentionPert linearModel GenePert biolord
GenePert scouter scGPT scouter
biolord GeneCompass GEARS AttentionPert
linearModel scELMo GeneCompass linearModel
GEARS AttentionPert scELMo trainMean scGPT trainMean scouter GeneCompass
trainMean GEARS linearModel GEARS
scouter biolord baseReg scELMo
baseReg baseReg trainMean baseReg
baseMLP baseMLP baseControl baseMLP
baseControl baseControl baseMLP
MSE PCC-delta MSE PCC-delta
CPA 3 3
biolord
scouter1 1 1 1 3 AttentionPert
baseMLP 1 scELMo GeneCompass scGPT 2
scFoundation GEARS 3
GenePert linearModel1 1 1 1 1
trainMean
baseControl 2
baseReg3 3 3 2 2
Wasser
K
st
L
e
-d
in ivergence
i
50 Perturbations 50 Perturbations
CPA
biolord scouter AttentionPert
baseMLP scELMo
GeneCompass
scGPT
scFoundation
GEARS
GenePert
linearModel
trainMean
baseControl
baseReg
0 2.0 4.0 0 5.0 0.1 0 2.0 4.0 0 5.0 0.1
e f
Additive
atled-CCP
baseControl
Inter-heterogeneity
Potentiation Epistasis Redundant
1.00 trainMean 1.00 CPA 1.00 1.2
0.75 linearModel 0.75 0.75 CPA 0.8 CPA 0.50 0.50 0.50
0.4 0.25 0.25
0 0 0.25 0
0 0.1 0.2 0.3 0.1 0.2 0.3 0 0.2 0.4 0.6 0 0.2 0.4 0.6
MSE MSE MSE MSE
j
2.0
1.5
1.0
0.5
0
ESM
0.6
0.3
0
–0.3
0 0.1 0.3 0.5 0.7 0.9
Level of noise
atled-CCP
0 0.1 0.3 0.5 0.7 0.9
Level of sparsity
atled-CCP
2.0
1.5
1.0
0.5
0
ESM
0.6
0.3
0
0 0.1 0.3 0.5 0.7 0.9 0 0.1 0.3 0.5 0.7 0.9
Level of noise Level of sparsity
Analysis https://doi.org/10.1038/s41592-025-02980-0
in LLM-derived embeddings, rather than model complexity or archi- This may further demonstrate the superior generalizability of the
tecture. Furthermore, all downstream architectures, loss functions, foundation model in certain test scenarios.
training protocols and evaluation metrics were kept constant across We also assessed the scalability of algorithms and the robustness
experiments. Thus, we believe the observed improvements are not of the algorithms to technical noise and data sparsity using simulated
artifacts, but instead reflect genuine representational advantages data (Methods). The procedure and evaluation metrics were similar
provided by LLMs. These results indicate that LLM-derived gene to those in the cellular context generalization scenario. In terms of
embeddings may capture high-level functional and contextual knowl- scalability, none of the algorithms encountered out-of-memory
edge that is otherwise hard to extract from gene expression data alone. issues, and their runtimes were within acceptable limits, except for
In our study, the four baseline models and linearModel per- scFoundation (Fig. 4i). All the algorithms’ performance was affected
formed relatively poorly, which differs from the findings of previous by data noise and sparsity, with greater sensitivity to sparsity (Fig. 4a,j).
studies—potentially due to differences in data preprocessing and Owing to the long runtime of scFoundation, we did not evaluate
the size of the training set (Supplementary Note 18). In datasets its robustness.
with abundant fine-tuning data, deep learning and foundation
models such as CPA and scGPT performed well, particularly on Chemical perturbation setting. For the three single-perturbation
population-average metrics. For example, in the Replogle-RPE1es- datasets, chemCPA achieved the best performance on the
sential and Replogle-K562essential datasets41, CPA achieved the population-average metrics, outperforming the baseline model by
highest accuracy in terms of both MSE and PCC-delta24 (Fig. 4b). Further a substantial margin (Fig. 5a). Unlike other deep learning models,
analysis revealed that the performance advantage of CPA over train- chemCPA performed impressively even on smaller datasets, likely
Mean increased as the similarity between the test and training pertur- because of its effective use of prior knowledge during pretraining on
bations decreased (Fig. 4c). This suggests that deep learning models bulk RNA-seq datasets53, which enriched its understanding of gene
have superior generalizability when fine-tuned on sufficiently large expression patterns. In the combined-perturbation dataset, baseReg
datasets. To further validate our conclusion, we conducted an experi- outperformed CPA on all six metrics, highlighting the current gap in
ment where we varied the training (fine-tuning) set size (10%, 30%, 50% methods for chemical perturbation prediction, particularly in combi-
and 80%) on the Replogle-RPE1essential and Replogle-K562essential natorial contexts (Fig. 5b). Therefore, developing more effective tools
datasets, keeping all other parameters constant. The results showed for such scenarios remains an urgent priority.
a clear trend that the performance of scGPT improved with increasing Next, we assessed the robustness and scalability of the evalu-
amounts of fine-tuning data, whereas the trainMean baseline model ated algorithms (Methods). The procedure and evaluation metrics
remained stable or showed slight degradation (Extended Data Fig. 5). are similar to those in the cellular context generalization scenario.
For the combined-perturbation datasets, we focused on accuracy In terms of scalability (Fig. 5c), none of the algorithms encountered
across three perturbation categories: combo-seen2, combo-seen1 out-of-memory issues, and their runtimes were within acceptable
and combo-seen0 (Fig. 4d). These categories correspond to scenar- limits. Regarding the impact of sparsity, PRnet and chemCPA were the
ios in which both, one and neither individual perturbation is present most stable. Regarding the impact of noise, PRnet and cycleCDR were
in the training set, respectively, which increase the difficulty of the most stable (Fig. 5a,d).
achieving high accuracy5,52. linearModel and scouter achieved the In summary, the following insights were obtained from the
highest overall accuracy across all categories (Fig. 4d). Accurately benchmark analysis of the perturbation generalization scenario:
predicting combined-perturbation effects fundamentally relies on (1) To predict genetic single-perturbation effects, GenePert is an
correctly learning the interactions between genes. Therefore, we used optimal choice when the training dataset is small. However, when
the Norman dataset to assess the ability of current models to predict the fine-tuning dataset is sufficient, deep learning and foundation
gene interactions40. In this dataset, gene interactions are categorized models such as CPA and scGPT are preferable. (2) In predicting genetic
into seven types, including additive, suppressor, synergy and other combined-perturbation effects, linearModel and scouter perform the
types (Supplementary Note 10). The additive-based linearModel and best. (3) In chemical single-perturbation effect prediction, chemCPA
trainMean achieved the best performance on the additive interaction is the preferred choice. (4) At present, methods for predicting
type, which is in line with expectations (Fig. 4e). Additionally, CPA chemical combined-perturbation effects are limited, and the baseReg
performed best on the potentiation, epistasis and redundant gene baseline model achieves the highest accuracy.
interaction types, which may indicate that deep learning models have
certain advantages in predicting specific types of gene interactions Limitations of current methods in the perturbation
(Fig. 4f and Supplementary Fig. 25). generalization scenario
Among the combo-seen2, combo-seen1 and combo-seen0 In this test scenario, we identified several limitations of current tools:
perturbation types, predicting the perturbation effects for combo- (1) Suboptimal performance in predicting combined-perturbation
seen0 was the most challenging and placed greater demands on the effects. Although scouter performed best among all the evaluated
model’s generalization ability, as both perturbations are unseen. methods in the combined-perturbation prediction setting, its improve-
In all four combined-perturbation datasets, the performance of all ment over the baseline models was limited (Fig. 4d). Other deep
tools is the worst for combo-seen0 prediction (Fig. 4g). Notably, in learning models and foundation models even performed worse than
the Schmidt dataset38, scGPT substantially outperformed the baseline the baseline models did; (2) Limited generalizability of deep learning
model in terms of the MSE and PCC-delta metrics, especially for the and foundation models. To evaluate their generalizability, we system-
combo-seen0 perturbation type (Fig. 4h and Supplementary Fig. 26). atically examined the performance of several representative deep
Fig. 5 | Benchmarking results in the perturbation generalization scenario. between the magnitude of perturbation effects and the performance of the
a, Performance overview of the nine evaluated methods, including accuracy, methods. A linear regression line with 95% confidence interval is shown. PCCs
robustness and scalability. Data are presented as mean values with error bars were calculated, and statistical significance was assessed using two-sided
indicating standard errors of the mean. N = 3 datasets. b, Performance overview t-tests. Adjustments were not made for multiple comparisons. f, Number of
of the six evaluated methods on a chemical combination perturbation dataset. DEGs identified by the baseMLP model in genetic single-perturbation datasets.
c, Runtime and CPU memory usage of the nine methods on simulated datasets g, Recommendation of suitable software for users based on their needs and the
with different cell counts. d, MSE and PCC-delta results for the nine methods characteristics of the data at hand.
on simulated datasets with varying levels of noise and sparsity. e, Correlation
Nature Methods | Volume 23 | February 2026 | 451–464 460
Analysis https://doi.org/10.1038/s41592-025-02980-0
c
Nature Methods | Volume 23 | February 2026 | 451–464 461
)nim(
emiT
1,000
500
0
5,000 20,000 50,000 150,000
Cell counts
)BG(
yromeM
a
Perturbation generalization Chemical single
Method Properties Accuracy Robustness Scalability
Language GPU Metrics Sparsity Noise ( T m im in e ) Me (G m B o ) ry Ranking
CPA 2 2 2 69.6 3.1 1
biolord 2 2 2 2 2 2 32.7 3.9
Dee m p o le d a e r l ning chemCPA 1 1 1 1 1 1 3 23.2 3.6 9
PRnet 1 1 97.3 8.3
cycleCDR 3 3 3 3 1 566.3 11.5 Performance
baseMLP 1 3 1 0.1 1 0.6 0 Low
trainMean 3 3 3 1 0.3 2
Linear model baseControl 3 2 2 0.2 2 0.8 1 High
baseReg 2 3 2 0.2 3 0.9
Ov
0 erall1 MSE PCC-delta E-distance Wasserste
K
in
L-diverge
C
nc
o
e
m
mon-DEGs
CV
MS
C
E
V
PCC-delta
CV
MS
C
E
V
PCC-delta
b
Perturbation generalization Chemical combo
Ranking
Method Properties Accuracy
Language GPU Metrics 1 20
CPA 6
PRnet 3 3 3 3 10
baseMLP 3 3 3 2 Performance
trainMean 2 2 2 2 2 2 0 Low 0
baseControl 1
5,000 20,000 50,000150,000
baseReg 1 1 1 1 1 1
Ov 0 erall1 MSE PCC-delta E-distanc
W
e assers
K
t
L
e
-
i
d
n iverge
C
n
o
c
m
e mon-DEGs 1 High Cell counts
Methods
CPA
biolord
chemCPA
PRnet
cycleCDR
baseMLP
trainMean
baseControl
baseReg
e f
Genetic single dataset: Replogle-RPE1essential Chemical single dataset: Sciplex3-A549
1 r = 0.8, P = 4.25 × 10−148
0.75
0.5
0.25
0
0 2 4 6
Perturbation effect
g
ESM
2.0
1.5
1.0
0.5
0
0 1 2 3 4
Perturbation effect
ESM
r = 0.55, P = 9.95 × 10−25
6
4
2
0
Dataset 1 2 3 4 5 6 7 8 9
fo rebmuN
sGED
deifitnedi
d
0.6
0.4
0.2
0
−0.2
baseMLP
Genetic single-perturbation datasets
atled-CCP
0.6
0.3
0
−0.3
0 0.1 0.3 0.5 0.7 0.9
Level of noise
atled-CCP
1.5
1.0
0.5
0 0.1 0.3 0.5 0.7 0.9 0 0.1 0.3 0.5 0.7 0.9
Level of sparsity Level of noise
ESM
1.5
1.0
0.5
0 0.1 0.3 0.5 0.7 0.9
Level of sparsity
ESM
scGPT Foundation model
Yes GenePert Linear model
Do you have sufficient data?
Single No trainMean Linear model
Single or combo perturbation? CPA Deep learning model
Genetic Combo Yes scGPT Foundation model
Do you have sufficient data?
Perturbation type No scouter Deep learning model
chemCPA Deep learning model
Chemical Single
Single or combo perturbation?
Combo
baseReg Linear model
Analysis https://doi.org/10.1038/s41592-025-02980-0
learning models, including CPA, scGPT, scouter and GEARS, across models in the perturbation effect prediction field are optimized using
13 genetic perturbation benchmark datasets with varying size. As loss functions that focus more on population-average metrics. This may
shown in our results, increasing the number of cells or perturbations account for the strong performance of these methods on such metrics
in the training data did not lead to performance gains across all evalu- and their poorer results regarding population-distribution metrics.
ation metrics (Supplementary Note 11 and Supplementary Figs. 13 and However, understanding the heterogeneity within cellular subpopula-
14). Further analysis revealed that model performance declined on tions in response to perturbations is vital for revealing gene functions
perturbations with high inter-heterogeneity, suggesting that gener- and regulatory networks. To increase prediction accuracy, future mod-
alization is more strongly influenced by data quality—particularly the els for perturbation effect prediction may consider incorporating both
similarity between training and testing perturbations—than by dataset population-average and population-distribution metrics into their
size (Supplementary Fig. 29). Additionally, we used the E-distance to loss function design; (3) One limitation of current methods emerges
measure the degree of perturbation effects in each dataset. In gen- in the perturbation generalization setting, where advanced models
eral, accurately predicting the perturbation expression profile for tend to underperform relative to simpler approaches, particularly on
strong perturbations requires models with greater generalizability. As small-scale datasets. This finding suggests that complex models may
shown in Fig. 5e, strong perturbations were associated with increased struggle to generalize effectively in low-data regimes. Enhancing the
MSE, E-distance and Wasserstein values, suggesting greater difficulty robustness and generalizability of advanced models under data-limited
in accurately capturing their expression responses (Supplementary conditions represents an important direction for future research.
Note 11 and Supplementary Figs. 15–17). Collectively, these findings (4) All current methods likely exhibited poor generalizability, espe-
highlight the current limitations in the generalizability of deep learn- cially when predicting perturbation effects in novel cellular contexts.
ing models for perturbation effect prediction, especially in the pres- To alleviate this, we propose incorporating prior knowledge through
ence of strong perturbations and heterogeneous perturbations; (3) cell-line embeddings, which can improve model generalizability (Sup-
Poor performance on population-distribution metrics. We observed plementary Notes 12 and 13 and Supplementary Figs. 27, 28 and 38).
that all methods likely performed poorly on population-distribution As a proof-of-concept study, we present an initial attempt to inte-
metrics especially on the Common-DEGs metric in genetic perturba- grate such prior knowledge and formulate an applicable framework
tion scenarios. For instance, in genetic single-perturbation datasets, with validations. We encourage researchers to explore and develop
even the best-performing model, baseMLP, identified fewer than 10 of alternative approaches on the basis of their own deeper understanding
100 true most differentially expressed genes (Fig. 5f). This also aligns and hope that our approach will inspire future work and drive innova-
with findings from the cellular context generalization scenario. tion in this area.
Finally, user guidance is provided regarding the benchmark There are several limitations of our current research. (1) In
analysis of the perturbation generalization scenario (Fig. 5g). certain test scenarios, the available datasets are currently insuffi-
cient, which may lead to bias in the conclusions drawn; (2) Our pro-
Discussion posed cellular context embedding strategy is currently applicable
In this study, we provide a comprehensive benchmark of single-cell only to cell-line-derived contexts and cannot be directly applied to
perturbation prediction methods across two key scenarios: cellular patient-derived contexts (Supplementary Note 12); (3) While the pro-
context generalization and perturbation generalization. We assessed posed cellular context embedding strategy represents a conceptu-
27 methods with a total of 29 datasets using 6 evaluation metrics— ally promising direction, its current performance demonstrates only
MSE, PCC-delta, E-distance, Wasserstein distance, KL-divergence and limited improvements—mainly in the PCC-delta and Common-DEGs
Common-DEGs—with a focus on evaluating the methods’ generaliz- metrics—and does not consistently surpass baseline methods across
ability. Simulated data were also used to assess the impact of noise evaluation metrics on all the evaluated datasets. As a preliminary
and sparsity on performance. Our findings revealed that no single attempt, this method remains an early exploration, and we acknowl-
method performs well across all datasets, highlighting the need for edge that further methodological refinements will be necessary to
user-specific guidance in selecting methods on the basis of dataset improve its performance and enhance its practical applicability;
characteristics. These results are as follows: (1) In the cellular context (4) Our current work does not address the challenge of poor perfor-
generalization scenario, trVAE, CellOT and inVAE demonstrated the mance on population-distribution metrics, which reflect a model’s
best overall performance on single-condition datasets. For the accurate ability to capture intracellular heterogeneity. Addressing this limitation
prediction of the top most differentially expressed genes, scPRAM is the remains an important direction for future research; (5) One limitation
optimal choice. Additionally, when the dataset includes perturbation of our current robustness evaluation framework is that it primarily
dosage information, scVIDR is the best method. (2) In the perturbation focuses on the effects of technical artifacts, such as noise and sparsity.
generalization scenario, for predicting genetic single-perturbation While this allows us to systematically assess the sensitivity of predic-
effects, GenePert is the optimal choice when the training dataset is tive models to common experimental distortions, it does not capture
small. When the fine-tuning dataset is sufficiently large, CPA and scGPT biological variability in perturbation responses across different cellular
are preferable. For predicting genetic combined-perturbation effects, contexts or genetic backgrounds. Evaluating robustness to biological
the linearModel and scouter method perform the best. In chemical variation with simulator tools such as scDesign3 (ref. 54) remains an
single-perturbation effect prediction, chemCPA is the preferred choice, important and complementary direction for future work.
whereas the baseReg baseline model achieves the highest accuracy in Looking ahead, several important directions could further
chemical combined-perturbation effect prediction (Fig. 5g). advance the field of single-cell perturbation outcome prediction.
For designing future algorithms, the following limitations of exist- (1) There is an urgent need to establish more diverse and compre-
ing methods and insights should be considered: (1) In the cellular hensive single-cell perturbation atlases. Similarly to how large-scale
context generalization scenario, most existing tools do not incorporate single-cell atlases have accelerated algorithmic development in the
time-point/dosage covariates, and those that do are still far from suf- broader single-cell field, systematically building perturbation-focused
ficiently accurate. Given the increasing availability of multi-condition cell atlases could catalyze progress in perturbation effect prediction.
data in the single-cell perturbation field, there is a pressing need to Notably, Rood et al. have proposed the concept of a ‘perturbation
develop high-performing models tailored for such data. (2) In both cell atlas’, highlighting the value of such systematic efforts for the
test scenarios, despite accounting for intra-heterogeneity, the models community55. Large-scale resources such as Tahoe-100M and X-Atlas
exhibited weaker performance on population-distribution metrics have begun to fill this gap by providing comprehensive perturbation
compared to population-average metrics. Typically, deep learning datasets, which lay a strong foundation for future benchmarking
Nature Methods | Volume 23 | February 2026 | 451–464 462
Analysis https://doi.org/10.1038/s41592-025-02980-0
and systematic evaluation of foundation model performance56,57; 18. Zhang, Z., Zhao, X., Bindra, M., Qiu, P. & Zhang, X. scDisInFact:
(2) Future work may further explore the integration of prior biological disentangled learning for integration and prediction of
knowledge—such as gene regulatory networks or pathway informa- multi-batch multi-condition single-cell RNA-sequencing data.
tion—into model design to enhance generalization across a wide range Nat. Commun. 15, 912 (2024).
of cellular contexts. Incorporating biological priors could substantially 19. Wei, X., Dong, J. & Wang, F. scPreGAN, a deep generative
improve the robustness and interpretability of perturbation prediction model for predicting the response of single-cell expression to
models; (3) Despite promising advances, the field of chemical pertur- perturbation. Bioinformatics 38, 3377–3384 (2022).
bation prediction, especially in the context of chemical combination 20. Wang, H., Wang, Y., Jiang, Q., Zhang, Y. & Chen, S. SCREEN:
effects, remains underdeveloped. More dedicated research is needed to predicting single-cell gene expression perturbation responses via
develop specialized algorithms capable of accurately modeling chemi- optimal transport. Front. Comput. Sci. 18, 2095–2228 (2024).
cal combination perturbations, which would have important implica- 21. Kana, O. et al. Generative modeling of single-cell gene expression
tions for accelerating chemical discovery and therapeutic development. for dose-dependent chemical perturbations. Patterns 4, 100817
(2023).
Online content 22. Lotfollahi, M., Naghipourfar, M., Theis, F. J. & Wolf, F. A.
Any methods, additional references, Nature Portfolio reporting sum- Conditional out-of-distribution generation for unpaired data using
maries, source data, extended data, supplementary information, transfer VAE. Bioinformatics 36, i610–i617 (2020).
acknowledgements, peer review information; details of author contri- 23. Bai, D., Ellington, C. N., Mo, S., Song, L. & Xing, E. P. AttentionPert:
butions and competing interests; and statements of data and code avail- accurately modeling multiplexed genetic perturbations with
ability are available at https://doi.org/10.1038/s41592-025-02980-0. multi-scale effects. Bioinformatics 40, i453–i461 (2024).
24. Lotfollahi, M. et al. Predicting cellular responses to complex
References perturbations in high-throughput screens. Mol. Syst. Biol. 19,
1. Srivatsan, S. R. et al. Massively multiplex chemical transcriptomics e11517 (2023).
at single-cell resolution. Science 367, 45–51 (2020. 25. Chen, Y. & Zou, J. Simple and effective embedding model for
2. Dixit, A. et al. Perturb-seq: dissecting molecular circuits with single-cell biology built from ChatGPT. Nat. Biomed. Eng. 9,
scalable single-cell RNA profiling of pooled genetic screens. Cell 483–493 (2025).
167, 1853–1866 (2016). 26. Hetzel, L., Boehm, S., Kilbertus, N., Günnemann, S. & Theis, F.
3. Adamson, B. et al. A multiplexed single-cell CRISPR screening Predicting cellular responses to novel drug perturbations at a
platform enables systematic dissection of the unfolded protein single-cell resolution. Adv. Neural Inf. Process. Syst. 35,
response. Cell 167, 1867–1882 (2016). 26711–26722 (2022).
4. Lotfollahi, M., Wolf, F. A. & Theis, F. J. scGen predicts single-cell 27. Zhu, O. & Li, J. Scouter: predicting transcriptional responses to
perturbation responses. Nat. Methods 16, 715–721 (2019). genetic perturbations with LLM embeddings. Preprint at bioRxiv
5. Roohani, Y., Huang, K. & Leskovec, J. Predicting transcriptional https://doi.org/10.1101/2024.12.06.627290 (2024).
outcomes of novel multigene perturbations with GEARS. Nat. 28. Liu, T., Chen, T., Zheng, W., Luo, X. & Zhao, H. scELMo:
Biotechnol. 42, 927–935 (2024). embeddings from language models are good learners for
6. Hao, M. et al. Large-scale foundation model on single-cell single-cell data analysis. Preprint at bioRxiv https://doi.org/
transcriptomics. Nat. Methods 21, 1481–1491 (2024). 10.1101/2023.12.07.569910 (2023).
7. Cui, H. et al. scGPT: toward building a foundation model for 29. Yang, X. et al. GeneCompass: deciphering universal gene
single-cell multi-omics using generative AI. Nat. Methods 21, regulatory mechanisms with a knowledge-informed
1470–1480 (2024). cross-species foundation model. Cell Res. 34, 830–845 (2024).
8. Yang, F. et al. scBERT as a large-scale pretrained deep language 30. Qi, X. et al. Predicting transcriptional responses to novel chemical
model for cell type annotation of single-cell RNA-seq data. Nat. perturbations using deep generative model for drug discovery.
Mach. Intell. 4, 852–866 (2022). Nat. Commun. 15, 9256 (2024).
9. Theodoris, C. V. et al. Transfer learning enables predictions in 31. Huang, W. & Liu, H. Predicting single-cell cellular responses to
network biology. Nature 618, 616–624 (2023). perturbations using cycle consistency learning. Bioinformatics
10. Wu, Y. et al. PerturBench: benchmarking machine learning 40, i462–i470 (2024).
models for cellular perturbation analysis. Preprint at https://arxiv. 32. McFarland, J. M. et al. Multiplexed single-cell transcriptional
org/abs/2408.10609 (2024). response profiling to define cancer vulnerabilities and
11. Bendidi, I. et al. Benchmarking transcriptomics foundation therapeutic mechanism of action. Nat. Commun. 11, 4296 (2020).
models for perturbation analysis: one PCA still rules them all. 33. Kang, H. M. et al. Multiplexed droplet single-cell RNA-
Preprint at https://arxiv.org/abs/2410.13956 (2024). sequencing using natural genetic variation. Nat. Biotechnol. 36,
12. Ahlmann-Eltze, C., Huber, W. & Anders, S. Deep-learning-based 89–94 (2018).
gene perturbation effect prediction does not yet outperform 34. Hagai, T. et al. Gene expression variability across cells and species
simple linear baselines. Nat. Methods 22, 1657–1661 (2025). shapes innate immunity. Nature 563, 197–202 (2018).
13. Peidli, S. et al. scPerturb: harmonized single-cell perturbation 35. Zhao, W. et al. Deconvolution of cell type-specific drug responses
data. Nat. Methods 21, 531–540 (2024). in human tumor tissue with single-cell RNA-seq. Genome Med. 13,
14. Bunne, C. et al. Learning single-cell perturbation responses using 82 (2021).
neural optimal transport. Nat. Methods 20, 1759–1768 (2023). 36. Nault, R., Fader, K. A., Bhattacharya, S. & Zacharewski, T. R.
15. Jiang, Q., Chen, S., Chen, X. & Jiang, R. scPRAM accurately Single-nuclei RNA sequencing assessment of the hepatic effects
predicts single-cell gene expression perturbation response based of 2,3,7,8-tetrachlorodibenzo-p-dioxin. Cell Mol. Gastroenterol.
on attention mechanism. Bioinformatics 40, btae265 (2024). Hepatol. 11, 147–159 (2021).
16. Piran, Z., Cohen, N., Hoshen, Y. & Nitzan, M. Disentanglement of 37. Haber, A. L. et al. A single-cell survey of the small intestinal
single-cell data with biolord. Nat. Biotechnol. 42, 1678–1683 (2024). epithelium. Nature 551, 333–339 (2017).
17. Yeh, C. -H., Chen, Z. -G., Liou, C. -Y. & Chen, M. -J. Homogeneous 38. Schmidt, R. et al. CRISPR activation and interference screens
space construction and projection for single-cell expression decode stimulation responses in primary human T cells. Science
prediction based on deep learning. Bioengineering 10, 996 (2023). 375, eabj4008 (2022).
Nature Methods | Volume 23 | February 2026 | 451–464 463
Analysis https://doi.org/10.1038/s41592-025-02980-0
39. Wessels, H. H. et al. Efficient combinatorial targeting of RNA 51. Shahapure, K. R. & Nicholas, C. Cluster quality analysis using
transcripts in single cells with Cas13 RNA Perturb-seq. Nat. silhouette score. in 2020 IEEE 7th International Conference on
Methods 20, 86–94 (2023). Data Science and Advanced Analytics (DSAA) 747-748 (IEEE, 2020).
40. Norman, T. M. et al. Exploring genetic interaction manifolds 52. Gao, Y. et al. Toward subtask-decomposition-based learning and
constructed from rich single-cell phenotypes. Science 365, benchmarking for predicting genetic perturbation outcomes and
786–793 (2019). beyond. Nat. Comput Sci. 4, 773–785 (2024).
41. Replogle, J. M. et al. Mapping information-rich genotype- 53. Subramanian, A. et al. A next generation connectivity map: L1000
phenotype landscapes with genome-scale Perturb-seq. Cell 185, platform and the first 1,000,000 profiles. Cell 171, 1437–1452
2559–2575 (2022). (2017).
42. Papalexi, E. et al. Characterizing the molecular regulation of 54. Song, D. et al. scDesign3 generates realistic in silico data for
inhibitory immune checkpoints with multimodal single-cell multimodal single-cell and spatial omics. Nat. Biotechnol. 42,
screens. Nat. Genet. 53, 322–331 (2021). 247–252 (2024).
43. Replogle, J. M. et al. Combinatorial single-cell CRISPR screens 55. Rood, J. E., Hupalowska, A. & Regev, A. Toward a foundation
by direct guide RNA capture and targeted sequencing. Nat. model of causal cell and tissue biology with a perturbation cell
Biotechnol. 38, 954–961 (2020). and tissue atlas. Cell 187, 4520–4545 (2024).
44. Tian, R. et al. Genome-wide CRISPRi/a screens in human neurons 56. Zhang, J. et al. Tahoe-100M: a giga-scale single-cell perturbation
link lysosomal failure to ferroptosis. Nat. Neurosci. 24, 1020–1034 atlas for context-dependent gene function and cellular modeling.
(2021). Preprint at bioRxiv https://doi.org/10.1101/2025.02.20.639398
45. Frangieh, C. J. et al. Multimodal pooled Perturb-CITE-seq screens (2025).
in patient models define mechanisms of cancer immune evasion. 57. Huang, A. C. et al. X-Atlas/Orion: genome-wide Perturb-seq
Nat. Genet. 53, 332–341 (2021). datasets via a scalable fix-cryopreserve platform for training
46. Wei, Z. et al. PerturBase: a comprehensive database for single-cell dose-dependent biological foundation models. Preprint at bioRxiv
perturbation data analysis and visualization. Nucleic Acids Res. https://doi.org/10.1101/2025.06.11.659105 (2025).
53, D1099–D1111 (2025).
47. Ji, Y. et al. Optimal distance metrics for single-cell RNA-seq Publisher’s note Springer Nature remains neutral with regard to
populations. Preprint at bioRxiv https://doi.org/10.1101/ jurisdictional claims in published maps and institutional affiliations.
2023.12.26.572833 (2023).
48. Gaudelet, T. et al. Season combinatorial intervention predictions Springer Nature or its licensor (e.g. a society or other partner) holds
with Salt & Peper. Preprint at https://arxiv.org/html/2404.16907v1 exclusive rights to this article under a publishing agreement with
(2024). the author(s) or other rightsholder(s); author self-archiving of the
49. Luecken, M. D. et al. Benchmarking atlas-level data integration in accepted manuscript version of this article is solely governed by the
single-cell genomics. Nat. Methods 19, 41–50 (2022). terms of such publishing agreement and applicable law.
50. Yuan, Z. et al. Benchmarking spatial clustering methods with
spatially resolved transcriptomics data. Nat. Methods 21, 712–722 © The Author(s), under exclusive licence to Springer Nature America,
(2024). Inc. 2025
Nature Methods | Volume 23 | February 2026 | 451–464 464
Analysis https://doi.org/10.1038/s41592-025-02980-0
Methods For the perturbation generalization scenario, we curated 17
Settings of benchmark methods datasets that broadly cover two perturbation types. These include 13
In this study, we selected a range of advanced modeling approaches genetic perturbation datasets, of which 9 focus on single perturba-
to systematically compare their ability to predict single-cell perturba- tions and 4 focus on combined perturbations, and 4 chemical per-
tion effects. The models include diverse theoretical frameworks and turbation datasets, including 3 single-perturbation datasets and one
algorithmic structures, ranging from linear models to foundation combined-perturbation dataset. The numbers of perturbations in these
models, and other deep learning-based approaches. In this study, we datasets range from 25 to 1,618, ensuring broad applicability and robust
evaluated the methods in two key scenarios: cellular context gener- evaluation of the methods. The sciPlex3-comb dataset was downloaded
alization and perturbation generalization. In the cellular context gen- from the CPA tutorial website and can be accessed at https://drive.
eralization scenario, we selected 14 methods, including 10 published google.com/uc?export=download&id=1RRV0_qYKGTvD3oCklKfoZQ-
methods, namely, biolord16, CellOT14, inVAE17, scDisInFact18, scGen4, FYqKJy4l6t. The remaining 16 datasets—Adamson3, Frangieh45, Tian-
scPRAM15, scPreGAN19, SCREEN20, scVIDR21 and trVAE22 and 4 baseline Activation44, TianInhibition44, Replogle-exp6 (ref. 43), Replogle-exp7
models. In the perturbation generalization scenario, we examined 18 (ref. 43), Replogle-exp8 (ref. 43), Papalexi42, Replogle-RPE1essential41,
methods: AttentionPert23, biolord16, CPA24, GEARS5, GenePert25, lin- Replogle-K562essential41, Norman40, Wessels39, Schmidt38, sciPlex-A549
earModel12, scFoundation6, scGPT7, chemCPA26, scouter27, scELMo28, (ref. 1), sciPlex3-K562 (ref. 1) and sciPlex3-MCF7 (ref. 1)—were down-
GeneCompass29, PRnet30, cycleCDR31 and 4 baseline models. For each loaded from the PerturBase database (http://www.perturbase.cn/).
method, the parameters were set according to official guidelines The TianActivation and TianInhibition datasets correspond to the
and tailored to align with our benchmarking datasets. Please refer CRISPR activation and inhibition experiments from the study by Tian
to Supplementary Note 1 for detailed descriptions and settings of all et al. The Replogle-exp6, Replogle-exp7 and Replogle-exp8 datasets
benchmark methods. represent single-cell perturbation data from different experiments
conducted in the study by Replogle et al. The Replogle-RPE1essen-
Datasets used in our benchmark tial and Replogle-K562essential datasets consist of single-cell per-
For the cellular generalization scenario, we collected 12 datasets. These turbation data for the RPE1 and K562 cell lines from Replogle et al.’s
datasets include various cell types, species nd individuals, making study. The sciPlex-A549, sciPlex3-K562 and sciPlex3-MCF7 datasets
them suitable for studying predictions at multiple cellular levels. The include measurements from three human cancer cell lines (A549, K562
datasets were all downloaded from public repositories and the NCBI and MCF7) subjected to perturbations with 188 chemicals at four
Gene Expression Omnibus (GEO). Specifically, the kangCrossCell, different dosages. The detailed information of these datasets is
kangCrossPatient, and Haber datasets use preprocessed data from Lot- given in Supplementary Table 3.
follahi et al., which can be downloaded directly from Google Drive via
https://drive.google.com/drive/folders/1n1SLbXha4OH7j7zZ0zZAxrj_- Data preprocessing
2kczgl8/. kangCrossCell and kangCrossPatient consist of data from All single-cell perturbation datasets used in our study were subjected
human peripheral blood mononuclear cells from eight donors stimu- to the following quality-control procedures. (1) Cell filtering. Cells
lated with interferon-beta and the corresponding control groups33. were excluded if they expressed fewer than 200 genes, or exhibited a
The original data can be obtained from the GEO under the identifier high mitochondrial gene fraction exceeding 10%. Furthermore, in the
GSE96583. The Haber dataset includes data of intestinal epithelial context of benchmarking models for the perturbation generalization
cells infected with bacterial and helminth infections, and the original scenario, cells subjected to perturbations in Schmidt dataset by at
dataset is available from the GEO under the identifier GSE92332 (ref. most two genes were retained, given the predominance of two-gene
37). The Parekh, CrossPatient and sciPlex3 datasets were obtained combinatorial perturbation data in the currently available datasets,
from the PerturBase database46 (http://www.perturbase.cn/). The resulting in the exclusion of 5,942 cells. We excluded any perturba-
Parekh perturbation dataset contains overexpression data for eight tions, other than the control, which affected fewer than 30 cells from
transcription factors across three cell lines58. The CrossPatient dataset our analysis. Additionally, to address the issue of computational effi-
includes single-cell perturbation data for six patients in response to ciency, the perturbations with a large number of cells need further to
two chemicals, Panobinostat and Etoposide35. The sciPlex3 dataset be processed. Specifically, for perturbations affecting more than 2,000
comprises measurements from three human cancer cell lines (A549, cells, we used a random selection method to include only 2,000 cells
MCF7 and K562) subjected to perturbations with 188 chemicals at in our downstream analysis. This data preprocessing strategy allows
four different dosages1. As suggested in a previous study, only data us to balance computational resources and time without substantially
for the nine most effective chemicals were used for testing16. The compromising model accuracy (Supplementary Note 15). (2) Gene
KaggleCrossPatient and KaggleCrossCell datasets were derived from filtering. Genes that were expressed in fewer than three cells were
the Open Problems competition. The organizers provided peripheral removed. In the context of benchmarking models for perturbation
blood mononuclear cell data from three donors, including data from generalization scenario, genes that did not have embeddings from
five cell types exposed to 144 chemicals. These datasets can be down- scGPT and scFoundation were excluded for each dataset. To balance the
loaded from the Kaggle competition webpage via https://www.kaggle. need for managing computational complexity and preserving maximal
com/competitions/open-problems-single-cell-perturbations/data/. information, we constrained each dataset to the 5,000 genes exhibit-
The McFarland32 dataset contains measurements from six human ing the highest variability. This decision aligns with the preprocessing
cancer cell lines exposed to perturbations with 11 chemicals and protocol established by the majority methods. During the selection
was downloaded from the scPerturb database13 (version 1.3), which of highly variable genes, we first split the entire dataset into training
is available at Zenodo via https://doi.org/10.5281/zenodo.10044268 and testing sets. The highly variable genes are selected using only the
(ref. 59). The CrossSpecies34 dataset contains expression data from training set, and these selected genes are then used to evaluate model
four species (mouse, rat, rabbit and pig). The processed dataset is performance on the testing set. This procedure helps to minimize
available at https://github.com/theislab/scgen-reproducibility/ the risk of information leakage. Additionally, we ensured the inclu-
blob/master/code/DataDownloader.py/. The Afriat perturbation sion of any genes that were specifically targeted by perturbations but
dataset60 was downloaded from the biolord GitHub tutorial site via not already represented among these highly variable genes, thereby
https://biolord.readthedocs.io/en/latest/tutorials/biolord_pipe- maintaining the integrity of our dataset for analyses involving these
line.html. The detailed information of these datasets is given in perturbed genes. (3) Data normalization. We used the global scaling
Supplementary Table 3. normalization technique provided by Scanpy, which standardizes
Nature Methods
