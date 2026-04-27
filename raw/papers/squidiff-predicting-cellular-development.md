---
source_path: /mnt/c/Users/Administrator/Zotero/storage/G4G7XHEF/He 等 - 2026 - Squidiff predicting cellular development and responses to perturbations using a diffusion model.pdf
ingested: 2026-04-23
sha256: 43c8b2c7ed392644
---

nature methods
Article https://doi.org/10.1038/s41592-025-02877-y
Squidiff: predicting cellular development
and responses to perturbations using a
diffusion model
Received: 16 November 2024 Siyu He1,2,3,13, Yuefei Zhu 1,13, Daniel Naveed Tavakol1,13, Haotian Ye4,
Yeh-Hsing Lao 1,5, Zixian Zhu1, Cong Xu1, Shradha Chauhan6, Guy Garty7,
Accepted: 18 September 2025
Raju Tomer 1,6, Gordana Vunjak-Novakovic 1,8, James Zou 3,4,9 ,
Published online: 3 November 2025 Elham Azizi 1,2,8,10,11 & Kam W. Leong 1,12
Check for updates
Single-cell sequencing has revolutionized our understanding of cellular
heterogeneity and responses to environmental stimuli. However, mapping
transcriptomic changes across diverse cell types in response to various
stimuli and elucidating underlying disease mechanisms remains challenging.
Here we present Squidiff, a diffusion model-based generative framework
that predicts transcriptomic changes across diverse cell types in response
to environmental changes. We demonstrate the robustness of Squidiff
across cell differentiation, gene perturbation and drug response prediction.
Through continuous denoising and semantic feature integration, Squidiff
learns transient cell states and predicts high-resolution transcriptomic
landscapes over time and conditions. Furthermore, we applied Squidiff to
model blood vessel organoid development and cellular responses to neutron
irradiation and growth factors. Our results demonstrate that Squidiff enables
in silico screening of molecular landscapes and cellular state transitions,
facilitating rapid hypothesis generation and providing valuable insights into
the regulatory principles of cell fate decisions.
Cells coordinate responses to environmental stimuli collectively, with Several machine learning-based models, including scGen6,
variations driven by tissue heterogeneity and external cues1,2. Living scVIDR7, CellOT8, GEARS9 and GenePert10, have been developed to
cells function as complex, dissipative systems far from chemical equi- predict single-cell perturbation using variational autoencoders (VAE)11,
librium and often exhibit highly nonlinear responses3. While single-cell optimal transport8, graph neural networks9, and large language mod-
sequencing enables unbiased characterization of cellular heterogene- els. Despite their advances, these models face limitations in predict-
ity, predicting transcriptomic changes in response to stimuli remains ing high-resolution dynamic transcriptional responses, especially in
challenging. Exploring disease mechanisms and optimizing drug com- transient states in organ development. Reconstructing smooth transi-
ponents require large-scale sequencing screens, which are laborious tions of learned features remains challenging. Most models focus on
and expensive4,5. specific tasks instead of a broad range of scenarios and require both
1Department of Biomedical Engineering, Columbia University, New York, NY, USA. 2Irving Institute for Cancer Dynamics, Columbia University, New York,
NY, USA. 3Department of Biomedical Data Science, Stanford University, Stanford, CA, USA. 4Department of Computer Sciences, Stanford University,
Stanford, CA, USA. 5Department of Pharmaceutical Sciences, University at Buffalo, Buffalo, NY, USA. 6Department of Biological Sciences, Columbia
University, New York, NY, USA. 7Center for Radiological Research, Columbia University, New York, NY, USA. 8Herbert Irving Comprehensive Cancer Center,
Columbia University, New York, NY, USA. 9Department of Electrical Engineering, Stanford University, Stanford, CA, USA. 10Department of Computer
Sciences, Columbia University, New York, NY, USA. 11Data Science Institute, Columbia University, New York, NY, USA. 12Department of Systems Biology,
Columbia University Irving Medical Center, New York, NY, USA. 13These authors contributed equally: Siyu He, Yuefei Zhu, Daniel Naveed Tavakol.
e-mail: jamesz@stanford.edu; ea2690@columbia.edu; kam.leong@columbia.edu
Nature Methods | Volume 23 | January 2026 | 65–77 65
Article https://doi.org/10.1038/s41592-025-02877-y
unperturbed and perturbed data as inputs but do not fully leverage of cell heterogeneity and differentiation trajectories in vessel organoids
underlying biological knowledge, failing to interpolate cell states. exposed to radiation and G-CSF proteins. Squidiff thus shows the
Diffusion models show potential in data generation through itera- power of capturing high-resolution cell dynamics under environmental
tive refinement and learning richer data distributions than VAEs12–14. changes by leveraging the strengths of diffusion models.
Integrating diffusion models with VAEs or performing diffusion in
latent space further enhances efficiency15–17. In fact, these models have Results
been applied in generating high-fidelity single-cell transcriptomic data, Squidiff predicts transcriptomic changes through denoising
such as scVAEDer, scDiffusion and scDiff17–19. Variants of diffusion mod- Squidiff is a diffusion model designed to predict single-cell transcrip-
els, such as conditional diffusional models, can manipulate smooth tomic changes in response to cell state changes such as cell differen-
feature transitions and capture complex latent cellular features19,20. tiation, development and exposure to various physical or chemical
Recent perspectives highlight their potential in creating virtual cells, stimuli across different cell types (Fig. 1a). Leveraging a neural network
establishing them as a promising artificial intelligence approach for in architecture and a continuous denoising process, Squidiff predicts
silico screening and perturbation prediction21. However, their applica- future and past cell states when stimuli are specified and can further
tions in predicting gene and drug perturbations or cell development predict the effects of multiple drug combinations as well as multiple
remain unexplored. gene perturbations.
Here, we introduce Squidiff (single-cell quantitative inference of Squidiff integrates a diffusion model for data generation and a
stimulus responses by a diffusion model), a computational framework semantic encoder for encoding latent representations11,25. This integra-
designed to predict transcriptomic responses of diverse cell types tion enables the generation of new transcriptomic data while modulat-
to a spectrum of environmental changes, including cell differentia- ing states via latent variables. Specifically, the semantic encoder maps
tion, gene perturbation and drug treatment. Squidiff is a conditional single-cell transcriptomic data into a unified latent representation
denoising diffusion implicit model (DDIM)22 generating new tran- space comprising semantic variables (z ), while the diffusion model
sem
scriptomes representing distinct cellular states. Squidiff allows for generates target cell transcriptomes from denoising a Gaussian noise
the incorporation of diverse perturbation conditions, including gene x conditioned on z via a standard denoising process (Fig. 1b and
T sem
edits and drug compounds with defined structures and dosages, when Supplementary Fig. 1a; see Methods for details). Overall, Squidiff is
this information is available. It excels in predicting the differentiation capable of generating transcriptomic data reflecting cell type varia-
of induced pluripotent stem cells (iPSCs) into the three germ layers, tions, cell state transitions and cell type-specific responses to multiple
guided by stimulus vectors. Notably, Squidiff captures transient cel- stimuli such as drug and gene perturbations.
lular states that other methods often miss. Moreover, it effectively pre- To explain the Squidiff framework, we first show an application
dicts nonadditive gene perturbation and cell type-specific responses, to synthetic single-cell RNA-sequencing (scRNA-seq) data gener-
as shown in glioblastoma and melanoma cells in response to new drug ated using Splatter26 (Supplementary Fig. 1b and Methods), which
combinations, providing an effective framework for dissecting the new simulated gene expression based on a gamma–Poisson distribution.
molecular programs that govern cell fate decisions. We simulated single-cell transcriptomics data for three distinct cell
We applied Squidiff to investigate neovascularization and vascu- types. During the diffusion process, iterative noise addition gradu-
lopathy induction in blood vessel organoids (BVOs) exposed to high ally transformed the three cell types into Gaussian noise after 1,000
linear energy transfer radiation, uncovering potential mechanisms steps (Supplementary Fig. 1c). The semantic latent variable (z ) cap-
sem
related to radiation-induced changes in vascular differentiation tra- tured biologically meaningful variations in gene expression associated
jectories. BVOs derived from human iPSCs have shown promise in with specific cell states or responses to stimuli, resulting in a clear
disease modeling and as drug-testing platforms, especially in the separation between different conditions in the latent space (Fig. 1c).
context of self-organizing models that can start from a single source Meanwhile, the Gaussian noise x accounts for stochasticity in the gen-
T
of stem cells23. This platform is useful for understanding injury and erated single-cell data. The reverse diffusion process then denoises and
identifying potential drug candidates in extreme conditions, such reconstructs the data given the condition, successfully recovering the
as high linear energy transfer radiation exposure or deep space mis- original transcriptomic profiles (Fig. 1d and Supplementary Fig. 1d,e),
sions, in which patient studies are not feasible. Despite the benefits of demonstrating the model’s ability to accurately capture and reproduce
three-dimensional (3D) systems for modeling cell types in vitro, the cellular states with complex gene expression distribution.
complexity of organoids and the labor-intensive nature of drug testing To generate new single-cell gene expression data over time and in
have limited the widespread application of these models. response to stimuli, Squidiff employs two methods of latent manipula-
To evaluate Squidiff’s capabilities in characterizing cellular tion: interpolation and addition (Fig. 1e). Addition involves combining
dynamics in BVOs, probing the potential mechanisms of neutron the original latent representation with a perturbed direction Δz . This
sem
radiation damage associated with secondary radiation sources in results in a shift in the gene expression distribution, reflecting effects
deep space and facilitating candidate drug discovery, we applied of the perturbation (Fig. 1f). Interpolation, on the other hand, primarily
Squidiff to predict molecular profiles of various cell compositions uses linear interpolation6, which computes intermediate points along
within BVOs throughout differentiation and development. These a straight line between two vectors, offering computational efficiency.
included endothelial cells, fibroblasts and mural cells, the principal For instance, during interpolation, the blue–green cluster transitions
components of blood vessels. We validated Squidiff’s predictions gradually from the red to the blue cluster as time t increases, with linear
with experimental single-cell sequencing data. Interestingly, Squidiff interpolation providing a direct path (Fig. 1g). We further validated
suggested a mural-to-endothelial developmental pathway consistent Squidiff’s performance across three biomedical scenarios, including
with recent time series studies of vessel organoids24. Additionally, cell differentiation or transdifferentiation, gene perturbations and
Squidiff predicted the effects of irradiation on various cell types by drug response predictions.
generating single-cell transcriptomic data upon irradiation, even with
limited available information on irradiated cell types, and identified key Squidiff predicts cell differentiation
affected signaling pathways at each stage of injury. Incorporating an Squidiff can predict transcriptomic profiles of specific cell states
FDA-approved radioprotective drug, granulocyte colony-stimulating when the transcriptome of a starting point and the latent embedding
factor (G-CSF), Squidiff further predicted that G-CSF might have a learned by Squidiff for the applied stimuli are known. This capability
protective effect by promoting vascular specification compared to is particularly useful for investigating the evolution of cells or miss-
irradiated groups. These findings provide a comprehensive assessment ing intermediate states in cellular differentiation and development.
Nature Methods | Volume 23 | January 2026 | 65–77 66
Article https://doi.org/10.1038/s41592-025-02877-y
a
Genes
Pluripotent cell
Intermediate state
State B
State C
State A
Differentiation
State transition State D1
State D2
Cell type A
Cell type B
Cell type C
Nature Methods | Volume 23 | January 2026 | 65–77 67
slleC Semantic
encoder
Genes
slleC
b
Conditional DDIM
Semantic encoder: genes
Diffusion processes:
Stimuli
Decoder: (z sem , x T ) Reconstructed genes
c d
Gene space diffusion Gene space reverse diffusion
2
C
P
PC1
e f
Original cell types A + B t = 0.25 t = 0.5
slleC
g
Cell type A
State A
State B
direction vector
Interpolation/extrapolation
hturt
dnuorG
noisserpxe
eneg
Perturbed cell type A
Reconstructed gene expression
ytisneD
Semantic variable z
sem
Gaussian noise z sem
x T ≈ N(0, I) x 0 x T
z sem x T p(x 0 ) p(x T ) p(x T ) p(x 0 )
4
∆z sem z 1
sem 2
0
2
z 0 2 4 6 8 10
sem
t = 0.75 t = 1
1.0
Generated
Cell type A
Original
0.5 Cell type B
Perturbed Interpolation
∆z sem
0
0 2 4 2 C
Gene expression P
PC1
Fig. 1 | Overview of Squidiff and its performance on synthetic data. in gene space. Probability distributions p(x) and p(x) illustrate the transition
0 T
a, Waddington’s landscape illustration depicting cell differentiation and from the original gene space to Gaussian noise and back to the gene space via
transdifferentiation paths from a pluripotent cell to various states (states denoising in the reverse process. e, Schematic of latent space manipulation for
A, B, C, D1 and D2). Solid black lines represent differentiation, while dashed generating new cell states. Arrows represent direction vectors (Δz ) used for
sem
lines indicate state transitions due to external stimuli. b, Diagram of Squidiff interpolation and extrapolation between states, with the spherical structure
model architecture, based on diffusion autoencoders20. The model comprises indicating the semantic latent space. f, Top: correlation between ground truth
a semantic encoder and a conditional DDIM. The semantic encoder maps and reconstructed gene expression levels for cell type A and its perturbed
scRNA-seq data into a semantic latent space (z ). The conditional DDIM state, showing high accuracy in predictions. Bottom: density plot comparing
sem
includes a diffusion process that incrementally adds noise to input data x, the distribution of gene expression values between generated, original and
0
transforming it into Gaussian noise x after T steps, and a denoising process perturbed data, indicating successful reconstruction by Squidiff. g, PCA
T
that decodes the latent variables (z , x) to generate gene expression profiles visualization of gene expression for cell types A and B, illustrating the temporal
sem T
(see Methods for details). c, Principal-component (PC) analysis (PCA) of latent progression of interpolated states from t = 0 (original) to t = 1 (fully interpolated).
representations: z (left) shows clustering of cell types A, B and C, while x Intermediate time points (t = 0.25, t = 0.5 and t = 0.75) show the gradual transition
sem T
(right) displays stochastic variations across the same cell types. d, Visualization between cell types A and B in the latent space.
of the forward diffusion process (left) and the reverse diffusion process (right)
Article https://doi.org/10.1038/s41592-025-02877-y
The approach leverages the generative capabilities of the diffusion based on real-time conditions and those predicted by these trajectory
model and its manipulation of semantic latent variables. models (Fig. 2h).
Applied to a public single-cell transcriptomics dataset of iPSC
differentiation as an example27, Squidiff effectively captures the state Squidiff predicts gene and drug perturbation
changes from iPSCs to mesendoderm and definitive endoderm cells Squidiff also predicts cellular responses to gene perturbations and
from day 0 to day 3 through diffusion (Supplementary Fig. 2a) and drug treatments. By leveraging vector operations, a trained Squidiff
denoising processes. The model was trained on data only from day model generalizes single-cell transcriptomic data across conditions,
0 and day 3 (Supplementary Fig. 2b). With the semantic encoder, the accurately modeling complex cellular responses.
semantic latent variables z0 and z3 represented distinct informa- For nonadditive gene perturbations, in which genes interact syn-
sem sem
tion for day 0 and day 3. The computing of Δz
sem
by subtracting z3
sem
ergistically to produce effects beyond simple additive approaches,
from day 3 and z0 from day 0 represents the direction vector for Squidiff assumes that perturbations involving two genes can be
sem
the averaged stimuli over the period (Fig. 2a, Supplementary represented as the sum of two learned semantic variables (Fig. 3a),
Fig. 2c and Methods). Starting with the initial states on day 0 allowing prediction of transcriptomic changes in wild-type cells.
and applying the learned stimulus direction, Squidiff accurately Specifically, we tested Squidiff on K562 cells perturbed for ZBTB25
predicts single-cell transcriptomics from day 1 to day 3 (Fig. 2b,c). and PTPN12 (ref. 34), a known nonadditive case discussed by the
Additionally, applying the stimulus vector to the predicted tran- authors of GEARS9 (Supplementary Fig. 3a). Unlike GEARS, which
scriptomics on day 1 also results in an accurate prediction of cell uses graph-based prior knowledge, Squidiff requires no explicit
states on day 2 (Fig. 2c). graph structure yet achieves highly accurate predictions (Fig. 3b,
To further assess the biological relevance of the model’s predic- Supplementary Fig. 3b–d and Methods). Compared to GEARS and
tions, we conducted differential gene expression analysis, identifying scGen, Squidiff consistently yields more robust and precise predictions
day-specific genes with distinct signatures corresponding to mesendo- (Fig. 3c and Supplementary Fig. 3e), showing its ability to capture gene
derm and predefinitive endoderm stages (Fig. 2d). For instance, NANOG perturbation effects and underlying molecular mechanisms.
expression emerged as a pluripotency marker on day 0 (ref. 28), with Aside from gene perturbations, we evaluated Squidiff for drug
its expression diminishing over subsequent days. By contrast, GATA6, screening. Unlike gene targets, drug effects are often complex, involv-
which encodes a key transcription factor involved in the transition ing influences on multiple genes concurrently and the regulation of
toward both mesodermal and endodermal fates29, showed a progres- associated pathways. Thus, a model predicting the overall cellular
sive increase. By applying pseudotime analysis (Methods) to the com- response to drugs is valuable for exploring drug mechanisms and
bined input data from day 0 and the model-predicted data from days identifying the most effective drugs with minimal side effects. We first
1 to 3, we observed matched fluctuations in cell proportions, with a tested Squidiff’s ability to predict the effects of two-drug combinations
continuous decline in NANOG expression and a corresponding increase on cell transitions. The assumption is that the latent space captures
in GATA6 expression (Fig. 2e,f) and signaling pathways such as WNT additive or synergistic interactions implicitly. Due to the limited avail-
and BMP signaling (Supplementary Fig. 2d). We further examined the ability of scRNA-seq data related to drug combinations, we evaluated
gene TBXT (T/brachyury), a mesodermal marker30, which was enriched Squidiff on an alternative dataset, 4i8, which profiles the molecular and
on days 1 and 2, indicating its role in early mesoderm differentiation morphological properties of melanoma cells treated with various drug
(Fig. 2e,f). These findings underscore the nonlinearity of gene expres- compounds using a novel microscopic technology. We withheld drug
sion dynamics during developmental processes and show that Squidiff combination data and trained Squidiff using only control cells and
learns gene relationships. Notably, the latent variable embeddings cells treated with single drugs, including trametinib, panobinostat,
from the ground truth data of day 2 and day 3 differ from the inter- dabrafenib, erlotinib and midostaurin. We then used Squidiff to gener-
polated variables, likely due to the different growth factors applied ate single-cell data for drug combination treatments and compared the
on each day in this experiment. This suggests that z represents an Pearson correlation between predicted and ground truth responses
sem
averaged trajectory. from the 4i dataset. While 4i does not contain single-cell transcrip-
Squidiff outperformed scGen6, a previous state-of-the-art model tomic data and provides only ~50 features per condition, it serves as
that combines VAEs and latent space vectors for high-dimensional a validation of Squidiff’s ability to generalize to drug perturbations
single-cell gene expression data (Fig. 2g). When trajectory inference (Supplementary Fig. 3f). However, the limited cellular features in this
methods such as PAGA31, Scorpius32 and Monocle33 were applied to dataset may impact Squidiff’s ability to fully capture complex drug
the Squidiff output transcriptomics, we observed successful recon- interactions compared to transcriptomic data.
struction of the dataset along a continuous pseudotime that closely We next applied Squidiff to a study investigating drug responses
matched the real discrete time points (d), surpassing random baselines. in glioblastoma, focusing on distinct effects of etoposide and panobi-
Moreover, there was a significant overlap between the genes identified nostat on tumor cells (Fig. 3d and Supplementary Fig. 4a). We trained
Fig. 2 | Squidiff predicts cell differentiation. a, Schematic of cell differentiation (hinges) and 1.5× interquartile range (whiskers). n = 600 cells for each day.
or transdifferentiation prediction using Squidiff. The model extracts semantic One-way ANOVA test was performed across time points (d). P = 6.6 × 10−56. f, Dot
latent variables (z1
sem
and z2
sem
) and computes the difference (Δz
sem
) to define the plot showing the fraction of cells expressing T, GATA6 and NANOG over different
direction vector over the differentiation period. b, UMAP visualization of training groups and time points (d), reflecting their roles in cell state transitions. g, Bar
datasets with iPSCs (day 0) and definitive endoderm (day 3) in blue and red, plot of R2 values and Pearson correlation comparing the prediction accuracy of
respectively. Combined training and testing datasets demonstrate Squidiff and scGen across all time points (d). Bar plots indicate the mean (bar
differentiation from iPSCs to mesendoderm and definitive endoderm. c, Pearson height) and 95% confidence interval (error bars) across six independent model
correlation plots comparing model-predicted and ground truth scRNA-seq data runs (n = 6), with individual replicate values overlaid. Two-sided independent
(scRNA) across different days. High correlation coefficients indicate accurate two-sample t-test was performed. P = 1.97 × 10−35, 1.48 × 10−9, 5.79 × 10−7 and
predictions by Squidiff. d, Heatmap of the top 15 differentially expressed (DE) 3.6 × 10−33 sequentially for Pearson correlation and 3.97 × 10−32, 1.55 × 10−1,
genes across time (days 0 to 3). Values are mean z-scored expression (per gene) 3.93 × 10−7 and 7.22 × 10−35 for R2 values. ****P < 0.0001. NS, not significant. h, Left:
averaged over cells from each day. Example genes include NANOG, GATA6, Spearman correlation between predicted cell orders from trajectory methods
HIST1H4B, GAREML and TMSB15BL. e, Pseudotime analysis showing cell density (PAGA, Monocle and Scorpius), random orders and actual time points (d) used in
distributions along pseudotime (top), with changes in expression patterns of Squidiff. Right: Jaccard index of top differentially expressed genes from day 0 to
NANOG and GATA6 (bottom). Comparison of inferred gene T expression across day 3 across pseudotime series identified by PAGA, Monocle, Scorpius, random
days 0 and 3. Box plots indicate the median (center lines), interquartile range orders and the actual time points used in Squidiff.
Nature Methods | Volume 23 | January 2026 | 65–77 68
Article https://doi.org/10.1038/s41592-025-02877-y
the Squidiff model using a dataset consisting of randomly selected panobinostat as having the most potent effect on tumor cells com-
myeloid cells treated with six different drugs as well as tumor cells and pared to other cell types among all screened drugs, consistent with
oligodendrocytes that were only exposed to etoposide (Fig. 3e and previous findings35 (Fig. 3g). Validating these predictions, we observed
Supplementary Fig. 4b). Despite this constraint, Squidiff accurately clear separation on uniform manifold approximation and projection
predicted the effects of all six drugs on tumor cells and oligoden- (UMAP) between untreated and drug-treated cells, with etoposide and
drocytes, demonstrating its ability to infer transcriptomic changes panobinostat producing distinct, drug-specific shifts in the embedding
induced by drug treatments (Fig. 3f). Notably, Squidiff also identified (Supplementary Fig. 4c).
Predict cell differentiation/transdifferentiation
Day 0
? ?
Growth factor
Day 0
Day 1
Day 2
Day 3
Nature Methods | Volume 23 | January 2026 | 65–77 69
seneg
ED
51
poT
0
yaD
1
yaD
2
yaD
3
yaD
3 yaD
2
yaD
1 yaD
0
yaD
1–
0
1
noisserpxe
naeM
a b
Day 1 Day 2 Day 3
?
c d
Predicted scRNA
e f g
NANOG GATA6
ANRcs
hturt
dnuorG
ANRcs
hturt
dnuorG
ANRcs
hturt
dnuorG
day 1 (predicted) day 2 (predicted)
Pearson R = 0.85 Pearson R = 0.90
Predicted scRNA
day 3 (predicted)
Pearson R = 0.99
Predicted scRNA
Fraction of cells in group (%)
Mean expression
0 2
****
R nosraeP
2R
Gene T expression
0
yaD
1
yaD
2
yaD
3
yaD
scGen
Squidiff
NS
Day 0 Day 1 Day 2 Day 3
R nosraeP
2R
iPSC
Definitive endoderm
Day 0
Day 3
UMAP1
h
2PAMU
Gene expression space of training datasets Gene expression space of training and testing datasets
Mesendoderm
Day 0 Day 0
Day 0 Predicted day 1 day 2
ANRcs
hturt
dnuorG
Predicted scRNA
Day 0
Day 1
Day 2 20 40 60 80 100
Day 3
ytisneD
noisserpxe
eneG
iPSC
Mesendoderm Definitive
endoderm
10 10
8 8
6 6
4 4
2 2
0 0
0 5 10 0 5 10
10 10
Pearson R = 0.89
8 8
6 6
4 4
2 2
0 0
0 5 10 0 5 10
Day 0
Day 1
Day 2 2 T Day 3 1.0
0 GATA6 0.8
0 0.2 0.4 0.6 0.8 1.0
Pseudotime
NANOG
1.0
10 10
5 5
0.5
0 0
0 0.5 1.0 0 0.5 1.0
Pseudotime Pseudotime
PAGA
0.8
Monocle
0.6 Scorpius
Random 0.4
0.2
0
10 20 30 40 50
Number of top DE genes (top n)
xedni
draccaJ
0.6
0.4
0.2
0
PAGA Monocle Scorpius Random
Method
noitalerroc
namraepS
GONAN AFGDP X1TM 1PPS 3SNCK 3FPIW 31LTTEM 12FSGI UMN 21PAKA IBFGT 41DEM 2QNCK SOF G1TM 7AMSP 22PSU 67RDW B4H1TSIH 1PHC 1P14LPR KRPTP 61BSA LMERAG 2PIAFNT 7PBFGI 3DUTO 1NOPS 1FNAB LC7K3PAM 7AMSP 22PSU 1FNAB 6ATAG 91MADA 1PHC 1SSRP 1PRN 1DNXLP 24fro22C 1P14LPR 2SSRP ANLF 4DARLDL BPPN 6ATAG 7LYM BPPN 1CTS 4LYM 91MADA APPN 2RCSLP PRG 2LPFR RNLPA 1PRN LB51BSMT 11NDLC
∆z sem
z1 z2
sem sem
**** **** ****
****
**** ****
****
Article https://doi.org/10.1038/s41592-025-02877-y
Predict two-gene perturbations
z2
sem
Predict drug responses
* *
NS
Nature Methods | Volume 23 | January 2026 | 65–77 70
52BTBZ
?
PTPN12
ANRcs
hturt
dnuorG
Predicted ZBTB25 + PTPN12
Pearson R = 0.97
R2 = 0.92
Predicted scRNA
Oligodendrocytes Vehicle Training data
Tumor cells Etoposide Held-out data
Myeloid cells Panobinostat
R04929097
Tazemetostat
Ispenisib
ANA-12
Oligodendrocytes Tumor cells
Reconstructed scRNA
ANRcs
hturt
dnuorG
Reconstructed scRNA
ANRcs
hturt
dnuorG
a b c
d e
f g
Pearson R = 0.915 Pearson R = 0.912
Vehicle
Etoposide
Panobinostat
R04929097
Tazemetostat Ispenisib
ANA-12
h i
Genes
slleC
Semantic
encoder
Conditional DDIM
slleC
Semantic variable z
sem
SMILES
RDKit
Drug compounds rFCFP
Genes Gaussian noise
slleC
Unperturbed cells Unseen compounds
Drug-perturbed cells
erocs
nosraeP 2R
Unseen compounds
Random split Random split
erocs
nosraeP 2R
R2 with true change in
expression (all genes)
erocS
Percentage of all genes
with opposite direction
erocS
4
3 1.0 20
z1
sem 2 0.8
10
1 0.6
0
0 GEARSscGenSquidiff GEARS scGenSquidiff
0 2 4
zTumor zMyeloid sem sem
R04929097 R04929097
Panobinostat
Vehicle
Vehicle
zOligodendrocyte
Vehicle sem
Etoposide 177 127 193
4 4 Panobinostat 102 143 220
3 3
R04929097 116 30 125
2 2
Tazemetostat 108 39 151 1 1
Ispenisib 99 37 142
0 0
0 2 4 0 2 4 ANA-12 186 86 178
Myeloid
cel
O
ls ligodendrocytes
Tu
mor
cells
1.00 1.00
0.95 0.95
0.90 0.90
Squidiff PRnet Squidiff PRnet
*** 1.00 1.00
x ≈ N(0, I)
T
0.95 0.95
0.90 0.90
Squidiff PRnet Squidiff PRnet
Fig. 3 | Squidiff predicts gene and drug perturbation. a, Schematic visualization of predicted drug responses, colored by three cell types, drug
representation of Squidiff’s approach for predicting the effects of two-gene treatment and training versus test datasets. f, Mean gene expression between
perturbations by leveraging semantic latent variables (z1
sem
and z2
sem
). This Squidiff-predicted and experimentally perturbed data, assessed using Pearson
method enables the exploration of combined effects of gene perturbations, such correlation scores. g, Heatmap displaying the response of different cell types
as the combination of ZBTB25 and PTPN12. b, Comparison of mean gene (myeloid cells, oligodendrocytes and tumor cells) to various drug treatments.
expression between Squidiff’s predictions and real perturbed data, evaluated Intensity values indicate the number of differentially expressed genes identified
using R2 values and Pearson correlation scores. c, Left: bar plots comparing the in each condition. h, Schematic diagram of Squidiff integrated with rFCFP.
true expression changes induced by ZBTB25 and PTPN12 perturbation in control i, Performance (Pearson correlation and R2 scores) of Squidiff and PRnet in
single-cell data across all genes by Squidiff, scGen and GEARS in terms of R2 out-of-distribution perturbation scenarios, including both unseen compound
values. Right: fraction of genes for which predicted expression changes are split and random split in the sci-Plex datasets. Bar plots indicate the mean (bar
opposite to the ground truth. Bar plots indicate the mean (bar height) and 95% height) and 95% confidence interval (error bars), with individual data points
confidence interval (error bars), with individual data points (n = 10) overlaid for (n = 3) overlaid for each bar. Results are shown across three independent data
each bar. d, Schematic representation of Squidiff’s approach to drug response splits per condition, with statistical significance assessed using a one-sided t-test.
prediction, in which semantic latent variables (z ) are manipulated based on cell P = 3.58 × 10−2, 1.67 × 10−2, 9.96 × 10−4 and 7.46 × 10−2, sequentially. *P < 0.05,
sem
types and drug treatments to model transcriptomic changes. e, UMAP ***P < 0.001. Cell images in a created with BioRender.com.
Article https://doi.org/10.1038/s41592-025-02877-y
When Squidiff encounters a completely unseen drug, prediction and ACTA2) and endothelial cells (PECAM1 and CLDN5) in the organoids
is limited. Unlike cell type transfer learning, by which Squidiff can on day 11 (Fig. 4b and Supplementary Fig. 5a).
generalize across different cell types, predicting the response to an To predict cell fates and states during blood vessel development,
entirely new drug is challenging, as the model has never been exposed we combined scRNA-seq data from iPSCs and BVOs on day 11 and
to its molecular characteristics during training. Therefore, we inte- trained the Squidiff model on these datasets (Supplementary Fig. 5b,c).
grated a drug compound adaptor inspired by PRnet36 (Fig. 3h). Specifi- We then performed interpolation for days 1, 3, 5, 7, 9, 13, 15 and 17
cally, we incorporated the drug-rescaled Functional Class Fingerprints using Squidiff. The predictions captured the differentiation and
(rFCFP) from PRnet, which updates the Squidiff semantic latent variable development trajectories of endothelial and mural cells from iPSCs,
from z sem to z′ sem =Enc(x0,rFCFP) (Methods). This adaptation allows as shown in the distribution of marker gene expression (Fig. 4c,d and
Squidiff to incorporate unseen drug information by leveraging its Supplementary Fig. 6a). The predicted data revealed intermediate
structural and functional properties, thereby enhancing its predictive states in which some endothelial cells exhibited properties akin to
capabilities beyond drugs included in the training set. We benchmarked those of mural cells, while mural and fibroblast cells appeared to
Squidiff against PRnet on the sci-Plex3 datasets37 using both an unseen derive from mural progenitor cells, consistent with published findings
drug split and a random data split. Our results show that Squidiff per- from experimentally sequenced real-time BVOs (Fig. 4c). To quantify
forms comparably to or better than PRnet (Fig. 3i). this, we tracked the expression of marker genes across time (d) for
endothelial cells, fibroblasts and mural cells, identifying fluctuations
Squidiff predicts BVO differentiation in mural-specific genes, such as LUM and DLK1 (Fig. 4e). Expression of
To evaluate Squidiff’s prediction of the cascade of transcriptional pro- these genes showed an increase before day 7 and a decrease after day 9,
grams during continuous cell state transitions and their alteration with while expression continued to increase in fibroblast and mural cells
stimuli, we employed organoid technology. Organoids, differentiated (Fig. 4e). A heatmap of differentially expressed genes across cell type
from human iPSCs, have emerged as unique 3D biomimetic systems for clusters on the UMAP further confirmed cell type distinctions and indi-
modeling human tissue development38, disease and drug responses, cated cell state transitions from iPSCs to mature cell lineages (Fig. 4f,g).
including those for brain, liver and lung organoids, among others39. We observed a substantial proportion of endothelial cells in the mural
However, as self-organized systems, organoids are inherently hetero- progenitor population, which resembled the results of real scRNA-seq
geneous, and the interactions among cells within them are complex39. data24 (Fig. 4h). The existence of differentiating endothelial cells from
Single-cell and spatial RNA sequencing have profiled these heteroge- day 5 to day 9, shown as mural progenitors, suggests the potential of
neities in differentiation trajectories, but fully characterizing develop- endothelial cells differentiated from mural-like cells, a feature that
mental processes at any given time point remains challenging. While scGen methods failed to capture (Fig. 4i and Supplementary Fig. 6b–g).
pseudotime analysis of scRNA-seq provides snapshots of organoid This underscores Squidiff’s enhanced capability in predicting cell
development at specific stages, real-time profiling across organoids is heterogeneity and transient cell states, offering insights for in
challenging due to labor-intensive workflows and technical expertise silico modeling.
requirements for manipulation of these engineered models39,40, in addi-
tion to the costly sequencing steps. Squidiff addresses these limitations Neutron irradiation disrupts structure and metabolism
by predicting cell transcriptomic changes during development and in After demonstrating Squidiff’s ability to predict gene and drug pertur-
response to stimuli. bations, we next evaluated its capacity to predict cellular response to
Using BVOs as a case study for applying Squidiff, organoids were physical perturbations, such as irradiation. Ionizing radiation, from
differentiated from human iPSCs and guided toward endothelial and radiotherapy, nuclear accidents or deep space travel, poses serious
vascular lineages, forming vascular network-like structures as early as health risks41, impacting not only cancerous but also noncancerous
day 6 (Supplementary Fig. 5a). BVOs show promise in modeling human cells, particularly endothelial, blood and immune, and local paren-
vascular development and disease and serve as a powerful platform for chymal cells within the radiated area42. High-energy particles such
drug discovery of human blood vessels24. as neutrons penetrate tissues and cause cellular and molecular dam-
The fate and state transition of cells in BVOs have been studied age43. Understanding radiation effects helps to develop effective
in real time24, providing an ideal dataset for comparison. In these countermeasures and treatments for radiation-induced damage44.
studies, progenitor states in early BVOs were observed to bifurcate Degenerative vascular changes are primary radiation health risks to
into endothelial and mural fates, highlighting the potential of BVO astronaut crews on exploration missions45. Microvascular endothelial
mural cells to differentiate into endothelial lineages (Fig. 4a). To test cells are susceptible to ionizing radiation, and radiation-induced altera-
whether Squidiff could replicate these findings, we generated BVOs tions in endothelial cell function are critical factors in organ damage
from healthy human iPSCs to create a training dataset. We fixed a through endothelial cell activation, enhanced leukocyte–endothe-
subset of organoids and with another dissociated the organoids into lial cell interactions, increased barrier permeability and initiation of
single cells, performing scRNA-seq on day 11. The BVOs were exposed apoptotic pathways42,46. BVOs provide an excellent model for studying
to differentiation processes from day −1 and progressed to mesoderm these effects.
aggregates from day 3 to day 5, with vascular formation starting on On day 5 of BVO development, we exposed the cultures to either
day 6. We identified fibroblasts (COL1A1 and LUM), mural cells (PDGFRB neutron or photon radiation and continued BVO culture until day 11
Fig. 4 | Squidiff predicts cell differentiation processes in BVOs. a, Diagram mesendoderm layer (GATA6). e, Stepwise expression of markers along with time
for hypothesized differentiation processes of iPSCs into cell components in (d) in fibroblasts, endothelial cells and mural cells. f, Joint UMAPs of training
BVOs. b, Embedding of scRNA-seq data of BVOs on day 11, colored by subtypes of scRNA-seq data on day −1 and the predicted scRNA-seq data from day −1 to day
endothelial cells, fibroblasts and mural cells. c, Joint UMAPs of training scRNA- 17, colored by cell types. FB, fibroblast. g, Heatmap of differential gene analysis
seq data on day −1, namely, the iPSCs and the predicted scRNA-seq data from day for clustering of joint training scRNA-seq data and predicted data. h, Stacked bar
−1 to day 17, with 2-d intervals with the semantic meaning, which was learned by plot of the number of cells colored by the major types and time points (d) across
only endothelial cells on day −1 and day 11. EC, endothelial cell. d, Joint UMAPs cell type clusters. i, Number of endothelial cell lineages in mural progenitor
of training scRNA-seq data on day −1 and the predicted scRNA-seq data from and mural cell clusters, comparing Squidiff and scGen. Bar plots indicate the
day −1 to day 17, colored by the markers including pluripotent genes (NANOG mean (bar height) and 95% confidence interval (error bars), with individual data
and MKI67), endothelial genes (CLDN5 and SOX17), fibroblast and mural-specific points (n = 2 and 3 for Squidiff and scGen) overlaid for each bar. A two-sided
genes (COL1A1, LUM and ACTA2) and markers denoting differentiation into the independent two-sample t-test was performed. P = 1.02 × 10−3. **P < 0.01.
Nature Methods | Volume 23 | January 2026 | 65–77 71
Article https://doi.org/10.1038/s41592-025-02877-y
Nature Methods | Volume 23 | January 2026 | 65–77 72
noisserpxe
eneG
a b
Real scRNA embedding for BVOs on day 11
Fibroblast
Endothelial cells
Non-mesoderm
ETV2
TFPI2
Pluripotent cells
(POU5F1+) Lateral plate
mesoderm Mural cell/fibroblast Endothelial
Day –1 Days 0–3 Days 3–5 Days 5–21
2PA
M Mural
U
UMAP1
c
Endothelial cells Fibroblasts Mural cells
Training data at day –1 Training data at day –1 Training data at day –1
Predicted data Predicted data Predicted data
Predicted EC development Predicted EC development Predicted EC development
Day –1 Day 17 Day –1 Day 17 Day –1 Day 17
Fibroblast-like Fibroblast-like Fibroblast-like
Training data at day –1
Predicted data from days –1 to 17
Mural-like Mural-like Mural-like
EC-like EC-like EC-like
Density
d NANOG CLDN5
e
Endothelial cells Fibroblasts Mural cells
NANOG
10 n 8 MKI67
8
o isse 6 C
SO
LD
X
N
17
5
6 ACTA2 GATA6
rp
xe n ae
M
4
2
D LU L M K1
4
0
2 –1 1 3 5 7 9 11 131517
Time (d) Time (d) Time (d)
f g h
Cluster ID i Cell numbers from EC lineages
Mesoderm cells EC progenitor 1 identified as mural progenitors
Pluripotent cells FB progenitors
Mural progenitors EC2
FB progenitors EC progenitor 2
Mural cells FB
Squidiff scGen
tnuoc
lleC
srebmun
lleC
400
200
0
000,4
000,2
0
Mean expression
in group
–2.5 0 2.5
MIV 4AGTI 1A1LOC 7PBFGI 2YRPS 4AGTI ARFGDP 7PBFGI 1A6LOC 2XTIP MUL 3OPSR 3PRGSAR 71XOS 1TCYM 5NDLC RDK 71XOS 5NDLC 1TCYM MACPE 1DT1L 6NDLC 1BLAC 6NDLC 1F5UOP 2CIZ 9KNIPS RDK 1L1PAFA 71XOS 5NDLC A2POT 1ESTG MPSA 76IKM 5CRIB 5PAGLD 1PASUN C2EBU
8 8
6 6
4 4
2 2
0 0
–1 1 3 5 7 9 11 131517 –1 1 3 5 7 9 11 131517
**
2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 0.1
Article https://doi.org/10.1038/s41592-025-02877-y
(Fig. 5a). On day 11, scRNA-seq was used to profile both healthy and G-CSF mitigates radiation damage in BVOs
irradiated BVOs. We identified endothelial cells, mural cells and fibro- Given the disruption of vascular structures, apoptosis of cells triggered
blasts. Reduced overlap between irradiated and control cells indicated by the p53 pathway and increased protein kinase B signaling, we tested
substantial molecular alterations (Fig. 5b). Squidiff encoded radia- whether the FDA-approved radioprotective drug G-CSF could rescue
tion exposure as a vector in the semantic space, enabling the genera- defects in vasculogenesis in vitro. G-CSF is a glycoprotein that plays a
tion of perturbed transcriptomes for different cell states in response crucial role in the production, differentiation and function of granu-
to radiation. locytes, a type of white blood cell essential for fighting infections48.
For validation, we masked mural cells and fibroblasts entirely dur- It has been used in clinical settings to stimulate the bone marrow to
ing Squidiff training, using only endothelial cells under irradiation and produce more white blood cells, particularly after chemotherapy or
control conditions (Fig. 5b). The model successfully generated tran- bone marrow transplants. Recent studies suggest that G-CSF may also
scriptomic data under irradiation (Fig. 5c and Supplementary Fig. 7a,b). have protective effects on vascular tissues, promoting endothelial cell
The model was then applied to interpolate irradiated transcriptomes survival and enhancing tissue repair processes49. However, the study
for endothelial cells, mural cells and fibroblasts from day −1 to day of the effect of G-CSF on fibroblasts and mural cells in the vasculature
17. UMAP indicated that early-stage cells were most affected (Fig. 5d remains limited. A known effect of G-CSF is its activation of the MEK1–
and Supplementary Fig. 7c,d), likely due to immature tissue structure MEK2, PI3K–AKT and NF-κB pathways50–52 (Fig. 6a), consistent with
and weak cell interactions. The ranking of the most differentiated findings on the regulation of NF-κB and kinase B signaling in radiation
genes upon irradiation across cells varied across developmental stages injury (Supplementary Fig. 8a,b). Squidiff offers a way to predict the
(Supplementary Fig. 7e,f). effect of G-CSF on other cell types when the responses of only one cell
Intriguingly, genes behaved differently over time and across cell type (for example, endothelial) are known. We sequenced single-cell
types. For instance, MYCT1 expression in endothelial cells decreased RNA expression in G-CSF-treated BVOs and considered it as ground
in the middle period and resumed at the latest stage of development, truth data.
while MYCT1 remained one of the most differentiated genes in mural Given the training data on endothelial cells only (Fig. 6b), Squidiff
cells and fibroblasts (Supplementary Fig. 7e). The most affected genes successfully generated predicted single-cell transcriptomic data for
upon irradiation across all these cells included upregulated genes fibroblasts and mural cells (Fig. 6c and Supplementary Fig. 10a). To
such as CDKN1A, MDM2, GDF15, ACTA2, ABCA1, MMP14 and ITGA6 validate predictions, we conducted differential gene expression
and downregulated genes such as NNAT, H1-3 (HIST1H1D), TOP2A, analysis comparing real irradiated data with predicted G-CSF-treated
HMGB2 and PRC1 (Fig. 5e). The top associated biological processes data. Notably, we identified distinct sets of differentially expressed
included cellular responses to ionizing radiation, cell motility, DNA genes for each cell type, with some genes shared across multiple types
damage through the p53 pathway, apoptosis, tumor necrosis factor (Supplementary Fig. 10b,c). The biological processes identified for
(TNF) signaling via nuclear factor (NF)-κB, the KRAS pathway, pro- enriched genes revealed unique roles for each cell type in response
tein kinase B (AKT)-mediated signaling and inflammation responses to G-CSF treatment. Fibroblasts were associated with blood vessel
(Supplementary Fig. 8a,b). morphogenesis and vasculogenesis, indicating their critical role in
Notably, CDKN1A encodes p21 (WAF1 or CIP1), known for its role in structural development (Fig. 6d and Supplementary Fig. 10d). Endothe-
cell cycle regulation. MDM2 encodes a protein functioning as a negative lial cells showed enrichment in pathways regulating apoptosis and
regulator of the p53 tumor suppressor, thus playing a critical role in the cell cycle, highlighting their involvement in maintaining cell sur-
controlling cell proliferation and apoptosis47. Live–dead assays showed vival and proliferation (Fig. 6d). Mural cells, by contrast, were linked
that the percentage of dead cells was much higher in irradiated BVOs to pathways related to genomic stability, cell cycle progression and
(Supplementary Fig. 9a–c), consistent with radiation-induced apopto- mitosis, indicating their role in maintaining genomic integrity. This
sis. BVOs decreased in size after neutron irradiation. We found that the aligned with reduced cell death percentages in G-CSF-treated samples
culture supernatant after irradiation was enriched in interleukin 1β (IL- versus irradiated samples (Supplementary Fig. 9b). Collectively, this
1β) and TNF, indicating enhanced induction of inflammation (Fig. 5f), study demonstrates Squidiff’s capability to predict cell type-specific
consistent with the increased expression of GDF15, a stress response responses to drug treatments and reveals the effects of G-CSF on irradi-
gene associated with the regulation of inflammation and cell survival ated blood vessel systems.
(Supplementary Fig. 9d). These metabolic changes overall resulted in
downstream failures in vascular formation and abnormal distribution Discussion
patterns in BVOs (Fig. 5g), causing earlier vascular sprouting in the In this study, we introduce Squidiff, a conditional diffusion model with
radiated BVOs versus controls. Overall, Squidiff effectively generated a semantic encoder designed to predict transcriptomic changes across
data with biological relevance and predicted the complex molecular diverse cell types in response to a spectrum of environmental changes.
responses to radiation exposure. Squidiff provides a robust framework for modeling cell dynamics,
Fig. 5 | Structural damage and metabolic phenotype alteration in BVOs 4 Gy of neutron irradiation (30,000 irradiated cells and 30,000 control cells
induced by neutron irradiation. a, Experimental workflow for differentiating across days −1 to 17). Two-sided Wilcoxon rank-sum tests were performed.
BVOs from human pluripotent stem cells. Key steps include embryoid body P values were adjusted with the Benjamini–Hochberg method. Genes exceeding
(EB) formation, mesoderm induction, vascular induction, embedding into log (fold change) > 2 or <–2.5 and adjusted P value < 1 × 10−5 are highlighted and
the gel and subsequent neutron irradiation or G-CSF treatment. Imaging and labeled. f, Enzyme-linked immunosorbent assay (ELISA) results showing the
scRNA-seq were performed on day 11. b, UMAP visualization of scRNA-seq data levels of IL-1β and TNF in the culture medium of BVOs on day 1 and day 6 under
from BVOs on day 11, showing different cell types: healthy fibroblasts, irradiated different irradiation conditions (0 Gy and 4 Gy). Bar plots indicate the mean
fibroblasts, healthy endothelial cells, irradiated endothelial cells, healthy mural (bar height) and s.e.m. (error bars), with individual data points overlaid for each
cells and irradiated mural cells. Training and nontraining datasets are indicated. bar (n = 2 biologically independent replicates per group). g, Left: 3D rendering of
c, Scatterplots showing the correlation between ground truth scRNA-seq data a CD31-stained BVO. Right: immunofluorescent images of BVOs showing structural
and Squidiff-predicted data for irradiated fibroblasts (top) and irradiated mural changes under control conditions and photon irradiation with 1 Gy and 4 Gy.
cells (bottom), with Pearson correlation coefficients and R2 values. d, UMAP CD31 (endothelial cell marker), cyan; α-smooth muscle actin (α-SMA) (smooth
visualization of scRNA-seq data from BVOs across different developmental muscle cell marker), red; 4,6-diamidino-2-phenylindole (DAPI) (nuclear stain),
days (day −1 to day 17), showing the distribution of healthy and irradiated cell blue. Scale bars, 100 μm. The workflow in a was created with BioRender.com.
types over time. e, Volcano plot of differential gene expression in BVOs after
Nature Methods | Volume 23 | January 2026 | 65–77 73
Article https://doi.org/10.1038/s41592-025-02877-y
including development and responses on single-cell transcriptomic We applied Squidiff to BVOs to investigate the effects of neutron
data, offering insights into differentiation trajectories, lineage specifi- irradiation and G-CSF treatment, a radioprotective intervention.
cation and therapeutic responses. By capturing complex, nonadditive As vascular integrity plays a central role in maintaining blood flow,
perturbation effects, Squidiff can reveal regulatory principles govern- nutrient distribution and metabolic homeostasis, radiation-induced
ing cell fate decisions and molecular dynamics. Its conditional design endothelial damage poses major risks in deep space missions53–55.
allows flexible control of experimental factors, while the integration A key advantage of Squidiff is its ability to reconstruct dynamic,
of rFCFP embeddings enables prediction for previously unseen drugs. cell type-specific responses from single-time-point datasets, thus
a
b c
Nature Methods | Volume 23 | January 2026 | 65–77 74
IPAD
AMS-α
13DC
Cells in BVO on day 11 Training data Healthy fibroblasts
Nontraining data
Irradiated fibroblasts
Healthy endothelial cells
Irradiated endothelial cells
Healthy mural cells
Irradiated mural cells
g
Control 1 Gy 4 Gy
ANRcs
hturt
dnuorG
ANRcs
detciderP
Radiation
Imaging
exposure
EB Mesoderm Vascular Embedding
formation induction induction into gel
Day 0 1 4 6 11
CEPT CHIR Forskolin VEGFA Focus, clear
scRNA-seq
BMP4 VEGFA FGF2
G-CSF
treatment
Irradiated fibroblasts
10.0
Pearson R = 0.98
7.5 R2 = 0.95
5.0
2.5
0
0 5 10
Irradiated mural cells
10.0
Pearson R = 0.96 R2 = 0.91 7.5
5.0
2.5
0
0 5 10
Ground truth scRNA
d e f
Cells in BVO from day –1 to day 17
Healthy fibroblasts Healthy endothelial cells
Irradiated fibroblasts Irradiated endothelial cells
Healthy mural cells
Irradiated mural cells
200
150
100
50
0
0 Gy4 Gy 0 Gy4 Gy
CD31
)1−lm
gp(
FNT
300
200
100
0
0 Gy4 Gy 0 Gy4 Gy
WTC day 1 WTC day 6
)1−lm
gp(
β1-LI
WTC day 1
WTC day 6
60
50
40
30
20
10
0
−3 −2 −1 0 1 2 3
Mean log (fold change)
)eulav
P
naem(
gol– 01
CDKN1A
NNAT MDM2
HIST1H1D GDF15
TOP2A
HMGB2 ACTA2
PRC1 MM A P B 1 C 4 A1
ITGA6
Article https://doi.org/10.1038/s41592-025-02877-y
a
b c
Cells in BVO on day 11
Healthy fibroblasts Training data
Irradiated fibroblasts Provided data
Irradiated and G-CSF-treated fibroblasts
Healthy endothelial cells
Irradiated endothelial cells
Irradiated and G-CSF-treated endothelial cells
Healthy mural cells
Irradiated mural cells
Irradiated and G-CSF-treated mural cells
Nature Methods | Volume 23 | January 2026 | 65–77 75
ANRcs
hturt
dnuorG
ANRcs
detciderP
PD98059
G-CSF MEK1/ ERK1/
MEK2 ERK2
Degradation
IκBα
Nuclear
NF-κB
PI3K AKT translocation
NF-κB
MMP2
Ly294002
VEGF
β integrin
1
Irradiated fibroblasts with G-CSF
10.0
Pearson R = 0.90
7.5 R2 = 0.78
5.0
2.5
0
0 5 10
Irradiated mural cells with G-CSF
10.0 Pearson R = 0.96
Data to predict R2 = 0.92
7.5
5.0
2.5
0
0 5 10
Ground truth scRNA
d
Enriched biological processes in fibroblasts Enriched biological processes in endothelical cells
Regulation of cell migration Regulation of apoptotic process
Apoptotic process Genes in Negative regulation of cellular response to growth factor stimulus Genes in
set (%) set (%)
Regulation of apoptotic process Positive regulation of extrinsic apoptotic signaling pathway via death domain receptors
0.10 0.20
Regulation of transforming growth factor β receptor signaling Regulation of transforming growth factor β receptor signaling
0.40
Blood vessel morphogenesis 0.20 Positive regulation of intrinsic apoptotic signaling
Regulation of c R e e ll g p u o la p t u io la n t i o o f n a p n r g o io li g fe e r n a e ti s o i n s log 5 10FD 1 R Neg P a o t s iv it e iv r e e g re u g la u t l i a o t n io o n f o m f e a m po b p ra to n t e ic p p o r t o e c n e ti s a s l log 4 10FD 1 R
Regulation of endothelial cell apoptotic process Negative regulation of cellular process
Embryonic heart tube development 4 Intrinsic apoptotic signaling 3
Vasculogenesis 3 Negative regulation of transmembrane receptor protein serine/threonine kinase signaling 2
Co
0
mbine
5
d
0
s
0
core
0 2,500 5,000
Combined score
Fig. 6 | Treatment potential of G-CSF in securing against radiation disruption irradiated fibroblasts, endothelial cells and mural cells. Data to predict include
in BVOs. a, Schematic illustration of the signaling pathways activated by G-CSF irradiated and G-CSF-treated fibroblasts, endothelial cells and mural cells.
treatment50. G-CSF binds to its receptor (G-CSF-R), triggering downstream c, Scatterplots comparing ground truth scRNA-seq data with Squidiff-predicted
signaling cascades involving MEK1, MEK2, ERK1, ERK2, PI3K and AKT. This leads data for irradiated fibroblasts (top) and irradiated mural cells (bottom) treated
to the degradation of IκBα and nuclear translocation of NF-κB, promoting the with G-CSF. Pearson correlation and R2 values indicate high prediction accuracy.
expression of target genes such as those encoding MMP2, VEGF and β integrin, d, Gene Ontology (Biological Process) enrichment for differentially expressed
1
which are involved in cell survival, proliferation and migration. b, UMAP genes in fibroblasts and endothelial cells. Bubble size indicates genes in set (%)
visualization of scRNA-seq data from BVOs on day 11, showing the distribution and color indicates FDR; x axis shows the combined score. FDR, false discovery
of healthy, irradiated and G-CSF-treated cell types. The training data include rate. The illustration in a was created with BioRender.com.
healthy fibroblasts, endothelial cells and mural cells. Provided data include
Article https://doi.org/10.1038/s41592-025-02877-y
circumventing both the high costs and the variability inherent in 9. Roohani, Y., Huang, K. & Leskovec, J. Predicting transcriptional
multi-time-point single-cell sequencing. Despite sequencing being outcomes of novel multigene perturbations with GEARS.
performed 1 week after irradiation, Squidiff reconstructed transcrip- Nat. Biotechnol. 42, 927–935 (2023).
tomic changes from the early injury phase, identifying temporal gene 10. Chen, Y. & Zou, J. Simple and effective embedding model for
responses as potential radioprotective targets. This ability to infer single-cell biology built from ChatGPT. Nat. Biomed. Eng. 9,
latent molecular trajectories positions Squidiff as a tool not only for 483–493 (2025).
therapeutic applications but also for uncovering fundamental mecha- 11. Kingma, D. P. & Welling, M. Auto-encoding variational Bayes. In
nisms of cellular adaptation, stress response and fate determination. 2nd International Conference on Learning Representations
Our analysis further highlights the role of G-CSF in regulating vascular (ICLR 2014) (eds Bengio, Y. & LeCun, Y.) (OpenReview, 2014).
responses, providing mechanistic insight into pathways of vascular 12. Yang, L. et al. Diffusion models: a comprehensive survey of
protection and strategies to enhance its therapeutic efficacy in vivo. methods and applications. ACM Comput. Surv. 56, 1–39 (2023).
These findings open avenues for future studies exploring cellular 13. Ho, J., Jain, A. & Abbeel, P. Denoising diffusion probabilistic
resilience pathways and other protective agents in space medicine, models. In Advances in Neural Information Processing Systems 33
precision medicine and beyond. (NeurIPS 2020) (eds Larochelle, H. et al.) 6840–6851
Despite these promising results, Squidiff has several limitations. (Curran Associates, 2020).
The training process involves introducing Gaussian noise into the data, 14. Guo, Z. et al. Diffusion models in bioinformatics and
resulting in prolonged training times. Furthermore, diffusion models computational biology. Nat. Rev. Bioeng. 2, 136–154 (2023).
generally require more computational resources than other generative 15. Rombach, R., Blattmann, A., Lorenz, D., Esser, P. & Ommer, B.
frameworks, such as VAEs or generative adversarial networks. These High-resolution image synthesis with latent diffusion models.
challenges underscore the need for optimizing training protocols and In Proc. IEEE/CVF Conference on Computer Vision and Pattern
more efficient implementations. Additionally, the current assump- Recognition 10684–10695 (IEEE, 2022).
tion of linearity in semantic variables may only provide approximate 16. Pandey, K., Mukherjee, A., Rai, P. & Kumar, A. VAEs meet diffusion
predictions in highly complex scenarios, requiring future refinement. models: efficient and high-fidelity generation. In NeurIPS
In the future, improving Squidiff’s scalability and computational 2021 Workshop on Deep Generative Models and Downstream
efficiency will be essential to broaden applications to large-scale data- Applications (OpenReview, 2021); https://openreview.net/
sets and to establish Squidiff as a more generalizable foundation model. pdf?id=-J8dM4ed_92
While Squidiff has demonstrated strong performance in identifying cell 17. Sadria, M. & Layton, A. scVAEDer: integrating deep diffusion
state transitions and perturbation responses, further validation using models and variational autoencoders for single-cell
in vivo models would strengthen its translational potential. Moreover, transcriptomics analysis. Genome Biol. 26, 64 (2025).
extending Squidiff to integrate multimodal omics data, including pro- 18. Luo, E., Hao, M., Wei, L. & Zhang, X. scDiffusion: conditional
teomics, epigenomics and spatial information, may further enhance generation of high-quality single-cell data using diffusion model.
its predictive capabilities and enable the discovery of new regulatory Bioinformatics 40, btae518 (2024).
mechanisms governing cell fate decisions. 19. Tang, W. et al. A general single-cell analysis framework via
conditional diffusion generative models. Preprint at bioRxiv
Online content https://doi.org/10.1101/2023.10.13.562243 (2023).
Any methods, additional references, Nature Portfolio reporting sum- 20. Preechakul, K., Chatthee, N., Wizadwongsa, S. &
maries, source data, extended data, supplementary information, Suwajanakorn, S. Diffusion autoencoders: toward a meaningful
acknowledgements, peer review information; details of author con- and decodable representation. In 2022 IEEE/CVF Conference on
tributions and competing interests; and statements of data and code Computer Vision and Pattern Recognition (CVPR) 10619–10629
availability are available at https://doi.org/10.1038/s41592-025-02877-y. (IEEE, 2022).
21. Bunne, C. et al. How to build the virtual cell with artificial
References intelligence: priorities and opportunities. Cell 187, 7045–7063
1. Schneider, G., Schmidt-Supprian, M., Rad, R. & Saur, D. (2024).
Tissue-specific tumorigenesis: context matters. Nat. Rev. Cancer 22. Song, J., Meng, C. & Ermon, S. Denoising diffusion implicit
17, 239–253 (2017). models. In 9th International Conference on Learning
2. Potente, M. & Mäkinen, T. Vascular heterogeneity and Representations (ICLR 2021) (OpenReview, 2021); https://
specialization in development and disease. Nat. Rev. Mol. Cell openreview.net/pdf?id=St1giarCHLP
Biol. 18, 477–494 (2017). 23. Yahaya, B. H. Organoid Technology for Disease Modelling and
3. Rafelski, S. M. & Theriot, J. A. Establishing a conceptual Personalized Treatment (Springer Nature, 2022).
framework for holistic cell states and state transitions. Cell 187, 24. Nikolova, M. T. et al. Fate and state transitions during human
2633–2651 (2024). blood vessel organoid development. Cell 188, 3329–3348.e31
4. Gullapalli, R. R., Desai, K. V., Santana-Santos, L., Kant, J. A. & (2025).
Becich, M. J. Next generation sequencing in clinical medicine: 25. Ho, J., Jain, A. & Abbeel, P. Denoising diffusion probabilistic
challenges and lessons for pathology and biomedical models. Adv. Neural Inf. Process. Syst. 33, 6840–6851
informatics. J. Pathol. Inform. 3, 40 (2012). (2020).
5. Atanasov, A. G., Zotchev, S. B., Dirsch, V. M. & Supuran, C. T. 26. Zappia, L., Phipson, B. & Oshlack, A. Splatter: simulation of
Natural products in drug discovery: advances and opportunities. single-cell RNA sequencing data. Genome Biol. 18, 174 (2017).
Nat. Rev. Drug Discov. 20, 200–216 (2021). 27. Cuomo, A. S. E., et al. Single-cell RNA-sequencing of
6. Lotfollahi, M., Wolf, F. A. & Theis, F. J. scGen predicts single-cell differentiating iPS cells reveals dynamic genetic effects on gene
perturbation responses. Nat. Methods 16, 715–721 (2019). expression. Nat. Commun. 11, 810 (2020).
7. Kana, O. et al. Generative modeling of single-cell gene expression 28. Chambers, I. et al. Nanog safeguards pluripotency and mediates
for dose-dependent chemical perturbations. Patterns 4, 100817 germline development. Nature 450, 1230–1234 (2007).
(2023). 29. Schrode, N., Saiz, N., Di Talia, S. & Hadjantonakis, A.-K. GATA6
8. Bunne, C. et al. Learning single-cell perturbation responses using levels modulate primitive endoderm cell fate choice and timing in
neural optimal transport. Nat. Methods 20, 1759–1768 (2023). the mouse blastocyst. Dev. Cell 29, 454–467 (2014).
Nature Methods | Volume 23 | January 2026 | 65–77 76
Article https://doi.org/10.1038/s41592-025-02877-y
30. Wilson, V. & Beddington, R. Expression of T protein in the 46. Wijerathne, H. et al. Mechanisms of radiation-induced
primitive streak is necessary and sufficient for posterior endothelium damage: emerging models and technologies.
mesoderm movement and somite differentiation. Dev. Biol. 192, Radiother. Oncol. 158, 21–32 (2021).
45–58 (1997). 47. Oliner, J. D., Saiki, A. Y. & Caenepeel, S. The role of MDM2
31. Wolf, F. A. et al. PAGA: graph abstraction reconciles clustering amplification and overexpression in tumorigenesis. Cold Spring
with trajectory inference through a topology preserving map of Harb. Perspect. Med. 6, a026336 (2016).
single cells. Genome Biol. 20, 59 (2019). 48. Ruef, C. & Coleman, D. L. Granulocyte–macrophage
32. Cannoodt, R. et al. SCORPIUS improves trajectory inference and colony-stimulating factor: pleiotropic cytokine with potential
identifies novel modules in dendritic cell development. Preprint clinical usefulness. Rev. Infect. Dis. 12, 41–62 (1990).
at bioRxiv https://doi.org/10.1101/079509 (2016). 49. Ping, S., Qiu, X., Gonzalez-Toledo, M. E., Liu, X. & Zhao, L.-R. Stem
33. Qiu, X. et al. Reversed graph embedding resolves complex cell factor in combination with granulocyte colony-stimulating
single-cell trajectories. Nat. Methods 14, 979–982 (2017). factor reduces cerebral capillary thrombosis in a mouse model of
34. Norman, T. M. et al. Exploring genetic interaction manifolds CADASIL. Cell Transplant. 27, 637–647 (2018).
constructed from rich single-cell phenotypes. Science 365, 50. Furmento, V. A., Marino, J., Blank, V. C. & Roguin, L. P. The granulocyte
786–793 (2019). colony-stimulating factor (G-CSF) upregulates metalloproteinase-2
35. Zhao, W., et al. Deconvolution of cell type-specific drug and VEGF through PIK/Akt and Erk1/2 activation in human
3
responses in human tumor tissue with single-cell RNA-seq. trophoblast Swan 71 cells. Placenta 35, 937–946 (2014).
Genome Med. 13, 82 (2021). 51. Boneberg, E. M. & Hartung, T. Molecular aspects of anti-
36. Qi, X., et al. Predicting transcriptional responses to novel inflammatory action of G-CSF. Inflamm. Res. 51, 119–128 (2002).
chemical perturbations using deep generative model for drug 52. Magné, N. et al. NF-κB modulation and ionizing radiation:
discovery. Nat. Commun. 15, 9256 (2024). mechanisms and future directions for cancer treatment.
37. Srivatsan, S. R., et al. Massively multiplex chemical transcriptomics Cancer Lett. 231, 158–168 (2006).
at single-cell resolution. Science 367, 45–51 (2020). 53. Hughson, R. L., Helm, A. & Durante, M. Heart in space: effect of
38. Hofer, M. & Lutolf, M. P. Engineering organoids. Nat. Rev. Mater. 6, the extraterrestrial environment on the cardiovascular system.
402–420 (2021). Nat. Rev. Cardiol. 15, 167–180 (2018).
39. Yang, S. et al. Organoids: the current status and biomedical 54. Delp, M. D., Charvat, J. M., Limoli, C. L., Globus, R. K. & Ghosh, P.
applications. MedComm 4, e274 (2023). Apollo lunar astronauts show higher cardiovascular disease
40. Huang, Y. et al. Deciphering the impact of aging on splenic mortality: possible deep space radiation effects on the vascular
endothelial cell heterogeneity and immunosenescence through endothelium. Sci. Rep. 6, 29901 (2016).
single-cell RNA sequencing analysis. Immun. Ageing 21, 48 55. Barcellos-Hoff, M. H., et al. Concepts and challenges in cancer
(2024). risk prediction for the space radiation environment. Life Sci.
41. Mettler, F. A. Jr & Voelz, G. L. Major radiation exposure — what Space Res. 6, 92–103 (2015).
to expect and how to respond. N. Engl. J. Med. 346, 1554–1561
(2002). Publisher’s note Springer Nature remains neutral with regard to
42. Kameni, L. E. et al. A review of radiation-induced vascular injury jurisdictional claims in published maps and institutional affiliations.
and clinical impact. Ann. Plast. Surg. 92, 181–185 (2024).
43. Durante, M. New challenges in high-energy particle radiobiology. Springer Nature or its licensor (e.g. a society or other partner) holds
Br. J. Radiol. 87, 20130626 (2014). exclusive rights to this article under a publishing agreement with
44. Tavakol, D. N. et al. Modeling and countering the effects of cosmic the author(s) or other rightsholder(s); author self-archiving of the
radiation using bioengineered human tissues. Biomaterials 301, accepted manuscript version of this article is solely governed by the
122267 (2023). terms of such publishing agreement and applicable law.
45. Chancellor, J. C., Scott, G. B. I. & Sutton, J. P. Space radiation: the
number one risk to astronaut health beyond low earth orbit. © The Author(s), under exclusive licence to Springer Nature America,
Life 4, 491–510 (2014). Inc. 2025
Nature Methods | Volume 23 | January 2026 | 65–77 77
Article https://doi.org/10.1038/s41592-025-02877-y
Methods Reverse process. The reverse process of DPMs aims to learn the noise
Ethics statement distribution p(x |x), which is an intractable and complex distribution.
t − 1 t
All procedures involving human iPSCs were conducted in accordance Fortunately, we know from the diffusion process that p(x |x, x ) is a
t − 1 t 0
with institutional and federal ethical regulations, with guidance from Gaussian distribution. In this regard, the diffusion model first estimates
the Columbia Stem Cell Initiative. The established WTC11 hiPSC line was the clean data ‘x ’ using the mean of distribution p(x |x), denoted
0 0 t
obtained from B. Conklin at the Gladstone Institutes under a material as µ(x, t):
θ t
transfer agreement (to G.V.-N.).
Diffusion probabilistic models (DPMs) are a class of latent variable μθ(xt,t)=
1
(xt−
βt
ϵθ(xt,t)).
generative models that iteratively transform data into noise and then
√αt √1−αt
reverse this process to reconstruct the original data. A DPM consists of Here ε(x, t) is the noise predicted by the denoiser, that is, a neural
θ t
the forward process, the reverse process and the sampling procedure. network parameterized by θ. Based on the estimation, the diffusion
The model learns to reverse the diffusion processes step by step, cap- model will sample x from p(x |x = x, x = µ(x, t)).
t − 1 t − 1 t 1 0 θ t
turing complex data distributions. A variant of DPM, the DDIM, further The most famous DDIM suggests the following deterministic
modifies the reverse process to be deterministic, improving sampling generative process:
efficiency by eliminating the need for iterative sampling steps. DPMs
and DDIMs have proven to be powerful methods for generating new p(xt−1|xt,x0)=N(√ᾱ t−1x0+√1−ᾱ t−1
xt−√ᾱ tx0
,0).
data in various domains, such as images25, videos56 and protein struc- √1−ᾱ t
tures57 in biomedicine. These models have also shown high potential This ensures a deterministic transformation from x back to x .
t t − 1
in single-cell reconstruction and inference14, although their actual To guide the denoising process via the semantic latent variable z , the
sem
implementation in genetics is still limited. This limitation may be due denoising neural network in Squidiff is conditioned on the variable,
to the unique challenges of applying DPMs to generate gene expression that is, ε(x, t, z ), and it predicts x by
θ t sem 0
data, particularly the need for semantic manipulation and meaningful
interpretation of the generated expression profiles. Recent advances in 1
fθ(xt,t,zsem)= (xt−√1−αt ̄ϵθ(xt,t,zsem)).
combining DPMs and VAEs have demonstrated effective representation √αt ̄
learning in the image domain65. Building on these advancements, we
adapted the diffusion autoencoder model65, also a conditional DDIM This ensures that the predicted x is conditioned on the environ-
0
model for single-cell gene expression prediction under various pertur- ments represented by z , which is derived from a semantic encoder
sem
bations. The goal is to learn a semantically rich latent space that allows (see below) capable of capturing complex environmental features while
smooth interpolation while maintaining the reconstruction capability performing dimension reduction (Supplementary Fig. 1a).
that the diffusion model excels at. In summary, the conditional DDIM decoder takes z = (z , x) as
sem T
input, with the entire reverse process described as:
Squidiff model
Similar to other diffusion autoencoder models, the goal of Squidiff is pθ(x0∶T|zsem)=p(xT) ΠT t=1pθ(xt−1|xt,zsem),
to model the target distribution of perturbed gene expression by learn-
ing a denoising process at varying noise levels. The diffusion process,
the reverse process and the semantic encoder are the three major
pθ(xt−1|xt,zsem)=N(fθ(x1,1,zsem),0)ift=1,
components of the Squidiff model (Fig. 1b). Specifically, biologically
meaningful information, such as cell type, environmental changes and pθ(xt−1|xt,zsem)=q(xt−1|xt=xt,x0=fθ(xt,t,zsem))otherwise.
disease states, are encoded via the semantic latent variable z , as these
sem
perturbations are assumed to be inherently reflected in the transcrip- Semantic encoder. The goal of the semantic encoder is to provide z
sem
tomic data under given conditions. On the other hand, stochasticity for the reverse process to generate transcriptomics conditioned on
is controlled via the random variable x. z . The semantic encoder is designed to capture high-level semantic
T sem
features from the input data, which are then used to condition the
Diffusion process. Given input data, the gene expression vector in an reverse diffusion process, ensuring that the generated transcriptomics
individual cell is denoted as x . We first define the Gaussian diffusion data adhere to the desired semantic characteristics.
0
process, which increasingly adds noise to x 0 at time t, t ∈ {0, 1, 2, 3,…, T}. Our semantic encoder is implemented as a multilayer perceptron
The forward diffusion process is defined as: (MLP)-based encoder designed for processing structured input data
with optional auxiliary features such as drug-related information (see
q(xt|xt−1)=N(√1−βtxt−1,βtI), sections below). The architecture consists of sequential linear transfor-
mations with batch normalization and ReLU activation, ensuring effi-
where β
t
are hyperparameters representing the noise levels, N (𝜇,Σ) cient feature extraction and transformation (Supplementary Fig. 1a).
denotes a (multivariate) normal distribution with mean 𝜇 and The semantic encoder is trained as part of the overall model. During
covariance Σ, and 𝐼 is the identity matrix. This leads to training, the semantic encoder takes the input data and produces z sem ,
q(xt|x0)=N(√αtx0,(1−αt)I) and αt= Π
s
t
=1
(1−βs). which is then used in the reverse diffusion process to conditionally gen-
In our implementation, these parameters are defined as follows: erate the transcriptomics data. The training process ensures that the
generated data are semantically coherent and adheres to the desired
• β values are generated linearly spaced between 0.001 and
s characteristics specified by z , which is equal to Enc(x ).
0.01, where 𝑠 is the index over diffusion steps (that is, 𝑠 = 1,…,𝑡). sem 0
• The cumulative product of β values is computed to
s Sinusoidal position embeddings. To incorporate temporal infor-
obtain α.
t mation into the model, we use sinusoidal position encoding ψ(t) for
• The square root of these cumulative products and their com-
time step t, which allows the model to represent time as a continuous
plements are used to scale x and the noise, respectively.
0 function rather than a discrete step. The core of this embedding lies
The forward diffusion step, which adds noise to the gene expres- in its frequency scaling. It applies an exponentially decaying function
sion vector, follows the equation xt = √αtx0+√(1−αt)ϵ, where ε is that controls how the frequencies are distributed, ensuring that both
Gaussian noise. short-term and long-term dependencies are encoded effectively.
Nature Methods
Article https://doi.org/10.1038/s41592-025-02877-y
Training. The training process optimizes the objective function: plots confirmed that 1,000 diffusion steps were optimal
L=∑ T
t=1
Ex0,ϵt (||ϵθ(xt,t,zsem)−ϵt||)
2
2, ϵt∈∼N(0,I), where the noise predic- (Supplementary Fig. 2a). After training, the semantic variable for
tive function ε(x, t, z ) is modeled using an MLP architecture condi- differentiation was computed by the mean difference between
θ t sem
tioned on both the time step t and semantic features z
sem
. The model the latent representations on day 3 and day 0: Δz=E(z3
sem
)−E(z0
sem
).
architecture consists of an initial linear transformation followed by a The model then generated interpolated scRNA-seq representations
sequence of MLP blocks incorporating time step embeddings and using zi =z0 + i ×Δz+η,i∈(0,1,2,3), where η is a Gaussian
latent semantic representations. Each MLP block performs a linear noise t s e em rm an se d m 𝑖 in3dexes the interpolation step (0→3). This
transformation followed by SiLU activations. The architecture incor- linear interpolation allowed the generation of synthetic
porates a conditional residual mechanism in which time step embed- scRNA-seq profiles that transitioned smoothly from day 0
dings and semantic features from an auxiliary encoder are added to to day 3.
the transformed representation, enhancing the model’s ability to 2. Prediction of two nonadditive gene perturbations: the pro-
capture temporal dependencies and contextual information cessed data were grouped into four categories: control,
(Supplementary Fig. 1a). The MLP is trained using the Adam optimizer PTPN12 + control, ZBTB25 + control and PTPN12 + ZBTB25. The
with a learning rate of 1 × e−4. dataset was split such that the first three groups were used for
training, while the last group served as the testing dataset. The
Encoding drug structure information. Squidiff is primarily trained diffusion process was set to 1,000 steps. After training, the
on transcriptomic data. However, in cases in which transcriptomic data semantic variables for the training groups were inferred, and
alone may not be sufficient, such as predicting responses to unseen the gene perturbation-specific variables were computed
drug perturbations, we introduce an adaptor module inspired by as follows:
PRnet36 (Fig. 3h). This module is not involved in the training process
but is used to encode SMILES-based drug structure and dosage infor- a. ΔzPTPN12=E(zP se T m PN12+control)−E(zc se o m ntrol)
mation into a latent representation. This drug-encoded representation b. ΔzZBTB25=E(zZ se B m TB25+control)−E(zc se o m ntrol).
is then concatenated with the original semantic latent variable z ,
sem
forming an extended representation z′ . In future work, Squidiff could To generate the predicted two-gene perturbed scRNA-seq data,
sem
incorporate additional environmental factors as needed to enhance we manipulated the latent representation by applying the learned
its predictive capability. perturbation variables: zPTPN12+ZBTB25= zcontrol+ΔzPTPN12+ΔzZBTB25 .
sem
These modified semantic representations were then used as conditions
Simulation of single-cell RNA-sequencing data to simulate the transcriptomic changes induced by the combined
We simulated the scRNA-seq data using Splatter and its simulation perturbation of PTPN12 and ZBTB25.
model Splat. Splatter is an R Bioconductor package that provides a
unified interface for multiple published simulation methods, includ- 3. Prediction of drug perturbation: we selected highly variable
ing its own Splat model, which generates synthetic scRNA-seq data genes along with some specific genes of interest, such as
that closely resemble real datasets26. Splat is a gamma–Poisson hier- oligodendrocyte markers. The training data included oligoden-
archical model in which the mean expression level for each gene is drocytes, tumor cells and myeloid cells, with conditions in
sampled from a gamma distribution and the observed count for each which these cells were either untreated (vehicle) or treated
cell is drawn from a Poisson distribution. Splat accounts for expres- with etoposide. Additionally, myeloid cells treated with
sion outliers and imposes constraints on variance to better mimic panobinostat, R04929097, tazemetostat, ispenisib and ANA-12
real scRNA-seq data characteristics. To obtain simulated scRNA-seq were included in the training dataset. This setup ensured that
data from three distinct groups, we used Splatter and Splat with their two of the cell types (oligodendrocytes and tumor cells) had
default parameter settings. never been exposed to drug treatments other than etoposide
during training. As a result, Squidiff was challenged to
Data preprocessing and quality control generalize its predictions to new drug–cell interactions.
To ensure robust downstream analysis, scRNA-seq data underwent Squidiff learned the latent representation of each drug by
quality control: computing the drug-specific perturbation effect in the
latent space:Δzdrug=E(zdrug,celltypeA)−E(zvehicle,celltypeA ).
• Cells with fewer than 1,000 expression counts or more than sem sem
This formulation allows Squidiff to capture the distinct transcrip-
20% mitochondrial gene expression were excluded.
tomic shifts induced by each drug, enabling it to predict the
• Genes expressed in fewer than three cells were filtered out.
response of unseen cell types to new drug treatments.
• Potential multiplets were removed by excluding cells with
4. Prediction of unseen drug perturbation: while Squidiff
over 10,000 detected genes.
demonstrates the capability to identify drug perturbations in
• Mitochondrial and ribosomal genes, often associated with
unseen cell types, its predictive accuracy depends on the drug
stress responses, were excluded.
being trained on at least one cell type. When a drug is complete-
After quality control, the gene count data were normalized and ly unseen during training, the model’s ability to predict its effect
log transformed to correct for sequencing depth variability. We then becomes limited due to the lack of prior exposure. To overcome
focused our analyses on highly variable genes and specific genes of this limitation, Squidiff incorporates an adaptor module that
interest, using Scanpy version 1.10.1 (ref. 58) for processing. transforms drug-related molecular information, including the
SMILES structure and dosage information, into an updated
Squidiff training tasks latent representation: z′
sem
=Enc(x0,rFCFP), where x
0
represents
1. Prediction of iPSC differentiation: to model iPSC differentia- the baseline single-cell expression profile and rFCFP denotes
tion, we selected the top 203 most variable genes, balancing the fingerprint representation of the drug compound. By
biological significance with computational efficiency. Data integrating these chemical and dosage features, Squidiff can
collected on days 0 and 3 were used as the training datasets, generalize its predictions to completely unseen drugs.
while data from days 1 and 2 served as the testing datasets, To evaluate this approach, we tested Squidiff using the sci-Plex3
respectively, resulting in 2,400 cells for training and 2,400 cells dataset, performing two types of data splits: (1) random split,
for testing. Gaussian noise was added to training data, and PCA where the dataset is randomly divided into training and testing
Nature Methods
