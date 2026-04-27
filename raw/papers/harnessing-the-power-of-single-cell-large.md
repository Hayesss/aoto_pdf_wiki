---
source_path: /mnt/c/Users/Administrator/Zotero/storage/8PWAYAP2/He 等 - 2025 - Harnessing the power of single-cell large language models with parameter-efficient fine-tuning using.pdf
ingested: 2026-04-23
sha256: b2ee82ee2b06bdc7
---

nature machine intelligence
Article https://doi.org/10.1038/s42256-025-01170-z
Harnessing the power of single-cell large
language models with parameter-efficient
fine-tuning using scPEFT
Received: 25 February 2025 Fei He 1, Ruixin Fei1, Jordan E. Krull 2,3, Yang Yu 1, Xinyu Zhang1,
Xianyu Wang1, Hao Cheng2,3, Mingyue Gao1, Li Su 1,4, Yibo Chen 1,4,
Accepted: 4 December 2025
Jinpu Li 1,4, Baichuan Jin1, Yuzhou Chang2,3, Anjun Ma 2,3, Qin Ma 2,3 &
Published online: 31 December 2025 Dong Xu 1,4
Check for updates
Single-cell large language models (scLLMs) capture essential biological
insights from vast single-cell atlases but struggle in out-of-context
applications, where zero-shot predictions can be unreliable. To address
this, here we introduce a single-cell parameter-efficient fine-tuning (scPEFT)
framework that integrates learnable, low-dimensional adapters into
scLLMs. By freezing the backbone model and updating only the adapter
parameters, scPEFT efficiently adapts to specific tasks using limited
custom data. This approach mitigates catastrophic forgetting, reduces
parameter tuning by over 96% and decreases GPU memory usage by more
than half, thus substantially enhancing the accessibility of scLLMs for
resource-constrained researchers. When validated across diverse datasets,
scPEFT outperformed zero-shot models and traditional fine-tuning in
disease-specific, cross-species and undercharacterized cell population tasks.
Its attention-mechanism analysis identified COVID-related genes associated
with specific cell states and uncovered unique blood cell subpopulations,
demonstrating the capacity of scPEFT for condition-specific interpretations.
These findings position scPEFT as an efficient solution for enhancing the
utility of scLLMs in general single-cell analyses.
Single-cell sequencing has revolutionized biology and medicine by Geneformer5, scGPT6, scFoundation7, SCimilarity8, GeneCompass9
providing high-resolution insights into the complex roles and interac- and scTab10. These scLLMs treat single-cell expression profiles as a
tions of cell types within their native environments1. This technology form of biological language in which gene identity and expression are
can uncover critical heterogeneities in tissues, such as those observed in analogous to words, and a cell is represented as a sentence. Using lan-
cancer and immune responses, thus advancing personalized medicine2. guage modelling objectives, such as predicting randomly masked gene
However, technical challenges, such as batch effects and biases, com- expression values from the remaining context, scLLMs learn gene-level
plicate the interpretation of single-cell data3. Inspired by the success dependencies and derive representations of cells and genes. Trained
of foundation models in natural language processing, researchers have on large single-cell atlases, scLLMs embed rich biological knowledge
developed single-cell large language models (scLLMs), such as scBERT4, and provide a strong foundation for downstream analyses.
1Department of Electrical Engineering and Computer Science, Bond Life Sciences Center, University of Missouri, Columbia, MO, USA. 2Department of
Biomedical Informatics, The Ohio State University, Columbus, OH, USA. 3Pelotonia Institute for Immuno-Oncology, The James Comprehensive
Cancer Center, The Ohio State University, Columbus, OH, USA. 4Institute for Data Science and Informatics, University of Missouri, Columbia, MO, USA.
e-mail: qin.ma@osumc.edu; xudong@missouri.edu
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 118
Article https://doi.org/10.1038/s42256-025-01170-z
The embeddings from scLLMs demonstrate promise in a variety of illustrates the behaviour of selected cell representations under native
tasks within familiar cellular contexts11. However, scLLMs often struggle scGPT, fine-tuned scGPT and scPEFT, indicating that native scGPT strug-
in out-of-context scenarios (for example, unseen diseases, new treat- gled with out-of-context scenarios, whereas its fine-tuned model was
ments, uncharacterized cell populations or cross-species applications), prone to catastrophic forgetting. The benchmarking results showed the
as performance can be unreliable, leading to misinterpretations in poor performance of native scLLMs in identifying out-of-distribution
zero-shot settings12,13. Current efforts to address this typically focus cells, as their pretraining data were derived from normal conditions
on scaling up both the model parameters and the pretraining data14, (Fig. 2b). Fine-tuning improved their performance but was compu-
which come with high computational costs and require extensive tationally intensive, whereas scPEFT further boosted accuracy under
data collection, limiting accessibility for many researchers with con- identical conditions and fivefold cross-validation (39.7–81.7% accu-
strained resources. A more practical solution is to fine-tune the entire racy improvements with P < 0.001 compared with native models, and
scLLM on out-of-context data. However, fine-tuning overwrites the 4.3–15% accuracy improvements with P < 0.05 compared with fine-tuned
original model parameters, potentially erasing valuable pre-learned models). Notable performance gaps were observed across the tested
knowledge, reducing adaptability and increasing the risk of overfitting scLLMs (Fig. 2b), with the four adapter types in scPEFT demonstrating
task-specific data, a phenomenon known as catastrophic forgetting13. various levels of efficacy (Supplementary Figs. 1a and 2a), driven by their
Additionally, full model updates still require substantial computational gene tokenizer designs and pretrained knowledge. Despite the various
resources, which remain a considerable barrier. native performances, scPEFT consistently elevated scLLMs to similar
To address these challenges, we propose scPEFT, a framework that levels, except for scBERT, which was pretrained on a smaller corpus. This
integrates parameter-efficient fine-tuning techniques into scLLMs to highlights the ability of scPEFT to unlock the full potential of scLLMs. By
calibrate them for specialized use cases. Unlike traditional fine-tuning, contrast, it seems that two widely used domain-agnostic tools, SingleR16
which modifies the entire model, scPEFT uses low-dimensional, and Seurat17, found it difficult to assign cell types accurately, highlighting
learnable and pluggable adapters to customize scLLMs in a sepa- the challenges posed by interpatient variability in this dataset.
rate, reduced-dimensional subspace. The critical role of these proxy Leveraging several pretrained checkpoints from scGPT, we
adapters is to estimate a ‘model delta’ (representing changes in cer- replaced its default model with organ-specific variants, including
tain model parameters) for context alignment, which is guided by lung-scGPT and pan-cancer-scGPT, as near-context scLLMs for the
task-specific objective functions and limited custom data. During NSCLC dataset. Interestingly, without adaptation, both lung-scGPT
the adaptation process, the original scLLM parameters are frozen and pan-cancer-scGPT underperformed relative to the default scGPT
to preserve pre-learned biological knowledge, and only the smaller (Extended Data Fig. 1). After applying domain adaptations, scPEFT
adapter parameters are updated. This design reduces the complexity of achieved similar performance across these scGPT variants (39.7–
domain adaptation, enabling higher performance with fewer resources 227.9% accuracy improvements with P < 0.001 over native models
than traditional fine-tuning strategies for scLLMs in out-of-context and 8.5–10.1% accuracy improvements with P < 0.01 compared with
scenarios. Furthermore, the learned model delta integrates biologi- fine-tuned models).
cal context into the attention scores of scLLMs, enabling conditional Confusion matrices (Extended Data Fig. 2) revealed that fine-tuned
interpretations that align with pre-learned general gene activities and scLLMs experienced catastrophic forgetting, as they failed to recognize
condition-specific requirements. certain cell types identifiable by their native models. For example,
We validated the robustness of scPEFT across diverse although the native scGPT model misclassified only 6% of CD4-specific
out-of-context scenarios, including disease-specific datasets, proliferating cells as other proliferating cells, its fine-tuned counterpart
cross-species transfer and undercharacterized cell populations (Sup- showed a 13% misclassification rate. By contrast, scPEFT overcame
plementary Notes 1–3 and Supplementary Tables 1 and 2). By mitigat- this performance drop and excelled at identifying rare classes, such as
ing the risk of overfitting to noisy or biased task-specific data, scPEFT XCL11 cells, which were overlooked by fine-tuned scGPT but success-
demonstrates marked performance gains over traditional fine-tuning fully identified by scPEFT. These advantages stem from the ability of
approaches and zero-shot models. Moreover, scPEFT greatly reduces scPEFT to preserve the original knowledge of scLLMs, thereby avoiding
the need for parameter tuning and graphics processing unit (GPU) overwriting during fine-tuning and reducing the risk of overfitting
memory. Through attention-mechanism analysis, scPEFT successfully to limited or biased data during domain adaptation. The UMAP visu-
identified COVID-specific cell-state-associated genes and distinguished alizations of cell embeddings (Supplementary Fig. 3) further exhibit
phenotypic subpopulations in CD34+-enriched and bone marrow these benefits.
mononuclear cell (BMMC) samples. In addition, scPEFT achieves The same comparisons were conducted on the Multiple Sclerosis
competitive performance in fine-tuning scLLMs for domain-specific (MS) and COVID-19 datasets, each with various disease conditions.
tasks, such as transcription factor (TF) identification, batch correction Consistent improvements by scPEFT across the four scLLMs were
and gene perturbation prediction. In summary, scPEFT offers a more evident in the performance plots (Fig. 2c,d), and its robustness across
efficient and effective framework for harnessing the full potential of diverse cell types and diseases was demonstrated in the confusion
scLLMs, thereby facilitating broader applications within the single-cell matrices (Extended Data Figs. 3 and 4) and the UMAP visualizations
biology community. (Supplementary Figs. 4 and 5).
Results Maximizing efficiency in domain adaptation of scLLMs
Achieving superior performance with scPEFT in cell-type We evaluated the computational cost across various adapta-
identification under disease conditions tion strategies with their default hyperparameter settings
The design and technical details of scPEFT are presented in Methods (Supplementary Table 3). Comparisons of trainable parameters and
and Fig. 1. To evaluate its adaptability to disease conditions unseen in GPU memory usage (Fig. 3a–d) show that scPEFT used only 0.05% to
the pretrained stage of scLLMs, we first focused on cell-type identifica- 3.97% of the trainable parameters and less than 50% of the GPU memory
tion using the Non-Small Cell Lung Cancer (NSCLC) dataset comprising compared with fine-tuning scLLMs. We further assessed the sensitiv-
diverse T cell subtypes from the tumour microenvironment. scPEFT ity of scPEFT to hyperparameter settings. Validation accuracies, cal-
was benchmarked with scBERT, Geneformer, scGPT and scFoundation culated using cells held out from a single donor in the reference set,
as backbones (see Supplementary Note 4 for benchmarking settings), were analysed in relation to the number of learnable parameters under
and we compared their native and fine-tuned performances. A uniform different transformer block configurations on the MS dataset (Fig. 3e).
manifold approximation and projection (UMAP) visualization15 (Fig. 2a) Across different hyperparameter settings, most scPEFT strategies
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 119
Article https://doi.org/10.1038/s42256-025-01170-z
a
Gene
… 1
Gene
m
Gene tokenizer Gene embedding Encoder Projector
Expression layer
Embeddi Q, K, V Attention-based Cell-level tasks
ngs transformers MLP and
Gene-level tasks
Name layer CLS Gene 1 … Gene m W Q ,W K ,W V
b Backpropagation
MLP and
layer norm Up
B
Down Up Adapter
W
W
A = N(0, σ2) Attention Down
Token adapter Prefix adapter LoRA Encoder adapter
Domain-agnostic
cell-type identification
Cross-species transfer Condition-specific Context-aware cell group
gene significance characterization
G1 G2 G3 Pretrain Pretrain Domain
Normal Perturbation prediction
Adaptation Adaptation Adaptation
G2 G3 G1
Tuned
Batch correction
Disease
Enable Enhance
consistently outperformed fine-tuning. However, increasing the keeping the query set unchanged. The results (Fig. 3g) show that as the
number of transformer blocks with adapters did not yield consistent amount of reference data was decreased, the validation performance
performance improvements. Additionally, we examined configura- of full fine-tuning dropped largely, whereas scPEFT remained more
tions with different intermediate gene and cell embedding dimen- robust, indicating that fewer trainable parameters require less data
sions within adapters, observing minimal accuracy variation across to optimize. We also assessed intermediate checkpoints before early
settings (Fig. 3f and Supplementary Note 5). Hence, we adopted the stopping (Fig. 3h) and observed that scPEFT strategies consistently
default scPEFT settings (Supplementary Table 3) for all experiments achieved higher validation performance, even in the first epoch. By
in this study to ensure that we obtained generalized results rather than contrast, the fine-tuning strategy required more epochs to adjust,
data-dependent optimizations. showing a gradual improvement over time. On the other hand, scPEFT
We evaluated the impact of annotated data availability across dif- adds a negligible inference overhead of approximately 0.1–0.3 ms per
ferent fine-tuning strategies, recognizing that previous annotations sample (Supplementary Note 6) due to adapter computations being
are scarce or costly to obtain. To simulate limited reference data, we integrated alongside the original scLLM layers, with minimal impact
randomly reduced the number of donors from the reference set while on the end-user experience.
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 120
sretpada
TFEPcs
Frozen
Trainable
W ,
Q
W,
K
W
Context-aware V
representations
c
scPEFT downstream applications
Batch 1 Batch 2 CT1 CT2
Fig. 1 | Overview of scPEFT. a, scLLM architecture. A typical scLLM features tasks in reduced-dimensional space. (2) Prefix adapter, which appends tunable
a gene tokenizer that encodes gene identities and expression profiles into tokens to gene tokens to incorporate task-specific information. (3) LoRA, which
gene embeddings. This is followed by the encoder, which comprises several adds low-rank matrices A and B to the transformers to approximate model
transformer blocks that aggregate gene expression in cells into gene and adjustments for the target domain. (4) Encoder adapter, another autoencoder
cell representations. The final module, a projector, transforms these gene attached to a transformer block, customizes gene contextual embeddings to new
and cell embeddings into task-specific outputs. The adapters from scPEFT biological contexts. These adapters can be used in combination. c, Downstream
can be adapted to various out-of-context applications without updating applications. scPEFT tailors scLLMs for a range of downstream applications in
their original parameters by using task-specific objective functions and specific biological contexts, including domain-agnostic cell-type identification,
backpropagation. b, Adapters in scPEFT. Four types of adapters enhance the condition-specific gene significance, context-aware cell group characterization,
domain adaptability of scLLM: (1) Token adapter, a compact autoencoder cross-species transfer, perturbation prediction and so on.
integrated into the gene tokenizer, refines gene token embeddings for specific
Article https://doi.org/10.1038/s42256-025-01170-z
a
UMAP1
Raw expression
Revealing disease-conditional cell-state-associated genes via phenotype of a cell, even if they are lowly expressed or prone to drop-
scPEFT attention analysis out. However, such a gene significance interpretation may also stick
The attention scores from the scLLMs quantify gene significance in a with their modelling context (Supplementary Note 7). We observed
specific cell group (Fig. 4a). scLLMs evaluate individual genes within the the differential attention scores of known signature genes provided
context of the expression of other genes, prioritizing genes linked to the by the original study18 between each T cell subtype and other subtypes
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 121
2PAMU
UMAP1
2PAMU
UMAP1
2PAMU
UMAP1
2PAMU
CD4-T 1-like scPEFT
H
CD4-Proliferative Native
CD4-RPL
Proliferative
Cell embedding
Fine-tuned
c
ycaruccA
0.95
0.80
0.65
0.50
ycaruccA
b
NSCLC
0.90
0.75
0.60
0.45
d
1.00
0.90
0.80
0.70
ycaruccA
scBERT Geneformer scFoundation scGPT P = 4.2 × 10−4
P = 0.044 P = 0.087 P = 9.6 × 10−4 P = 3 × 10−3 P = 1 × 10−5
P = 1.1 × 10−5 P = 1.7 × 10−6 P = 1.4 × 10−7 P = 5.2 × 10−8
4.3% 10.1% 9.2%
15.0%
39.7%
72.6% 81.7%
62.9%
MS
scBERT Geneformer scFoundation scGPT P = 7.6 × 10−4
P = 2.8 × 10−5
P = 0.24 P = 0.055 P = 3.3 × 10−3 P = 1.6 × 10−3
P = 2.7 × 10−3 P = 4.9 × 10−5 P = 3.1 × 10−5 P = 1.4 × 10−5
3.0%
6.2% 9.2%
5.8%
29.1%
50.5%
48.5%
53%
COVID-19
P = 2.5 × 10−4
scBERT Geneformer scFoundation scGPT
P = 8.1 × 10−4
P = 0.54 P = 0.018 P = 4.7 × 10−3 P = 3.1 × 10−3
P = 6.8 × 10−4 P = 7.7 × 10−7 P = 1.6 × 10−7 P = 4 × 10−6
2.8% 2.9% 2.8% 2.6%
12.1%
22.2% 27.0%
28.1%
Fold 0 1 2 3 4
Native Fine-tuned scPEFT Native Fine-tuned scPEFT Native Fine-tuned scPEFT Native Fine-tuned scPEFT SingleR Seurat
Fig. 2 | Cell-type identification of scPEFT under disease conditions. scPEFT preserves the capability of native scGPT while benefiting from domain
a, Illustration of how native scGPT, fine-tuned scGPT and scPEFT models drive adaptation.b–d, Violin plots benchmarking native, fine-tuned and scPEFT
cell embeddings in their feature space. The data points represent a 10% random models using scBERT, Geneformer, scFoundation and scGPT as backbones, along
sample of cells from four annotated cell types in the query partition of the with SingleR and Seurat, under fivefold cross-validation on the NSCLC (b), MS (c)
NSCLC dataset. Native scGPT seems to cluster cells according to their identities and COVID-19 (d) datasets. Statistical significance between scPEFT and the other
but misinterprets some CD4+ T helper 1 (T 1)-like cells into CD4-proliferative models was assessed using a paired two-sided Students t-test across the fivefold
H
cells, probably due to expression shifts in the tumour microenvironment validation results (n = 5 independent validation tests). In each box, the central
compared with its training data of normal cells. Fine-tuned scGPT achieves mark indicates the median, and the bottom and top edges of the box indicate the
better separation of CD4-T 1-like and CD4-RPL cells but performs worse in 25th and 75th percentiles. The whiskers extend to the most extreme data points
H
distinguishing CD4-proliferative cells from proliferation cells than native without outliers, and the outliers are plotted individually as circles.
scGPT, indicating catastrophic forgetting of pretrained knowledge. In contrast,
Article https://doi.org/10.1038/s42256-025-01170-z
0.95
0.90
0.85
0.80
0.75
0.70
0.65
0.60
100 80 60 40 20 0
Downsampled dataset/total dataset (%)
Linear probe Full fine-tune Prefix adapter LoRA Token adapter Encoder adapter
from native scGPT, fine-tuned scGPT and scPEFT to investigate their attention scores, whereas native and fine-tuned scGPT tended to miss
ability to spot known cell-type-associated signature genes from the or misinterpret some of these signature genes.
NSCLC dataset (Fig. 4b). The attention heat maps indicate that scPEFT We further compared the attention views of native scGPT,
attended these signatures with statistically significant differential fine-tuned scGPT and scPEFT in a differential gene expression analysis
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 122
ycaruccA
g
0.90
0.80
0.70
0.60
0.50
0.40
0.30
0.20
0 5 10 15 20 25 30
Epochs
ycaruccA
100.00%
1.00 88.12%
0.80
0.60 51.49%50.43%46.40%
0.40
0.20
0
h
evitaleR
egasu
yromem
UPG
100.00%
100
10–1
3.64%
1.04%
0.22%
10–3 0.08%
evitaleR
etar
retemarap
elbanrael
a scGPT
d scBERT
100.00%
100
10–1
10–3 0.74% 0.48% 0.24% 0.06%
100.00%
1.00 1.00 93.57%
0.80 0.80
0.60 0.60 47.97% 45.82% 39.03%
0.40 0.40
0.20 0.20
0 0
lluF enut-enif nekoT retpada xiferP retpada ARoL redocnE retpada lluF enut-enif nekoT retpada xiferP retpada ARoL redocnE retpada
0.82
0.80
0.78
0.76
0.74
0.72
0.70
0.68
Linear probe Token adapter Prefix adapter
Full fine-tune Encoder adapter LoRA
Layers
2 4 6 8 10 12
c Geneformer
100.00%
100
10–1
3.97%
0.33% 0.25% 10–3 0.05%
100.00%
93.20%
60.19%
50.84% 44.45%
ycaruccA
e
5 × 105 1 × 106 2 × 106 5 × 106 1 × 107 2 × 107 5 × 107
Learnable parameters
0.82
0.80
0.78
0.76
0.74
0.72
0.70
0.68
5 × 105 1 × 106 2 × 106 5 × 106 1 × 107 2 × 107 5 × 107
Linear probe Token adapter Prefix adapter
Full finetune Encoder adapter LoRA
Hidden dimension
864128256 512
ycaruccA
f
Learnable parameters
evitaleR
evitaleR
etar
retemarap
elbanrael
egasu
yromem
UPG
b scFoundation
100.00%
100
10–1 1.78%
0.59%
0.30%
0.15%
10–3
100.00%
88.24%
1.00
0.80
0.60 44.71% 44.28% 41.85%
0.40
0.20
0
lluF
lluF
lluF
enut-enif
enut-enif
enut-enif
nekoT
nekoT
nekoT
retpada
retpada
retpada
xiferP
xiferP
xiferP
retpada
retpada
retpada
ARoL
ARoL
ARoL
redocnE
redocnE
redocnE
retpada
retpada
retpada
lluF
lluF
lluF
enut-enif
enut-enif
enut-enif
nekoT
nekoT
redocnE
retpada
retpada
retpada
xiferP
xiferP
ARoL
retpada
retpada
nekoT
ARoL
ARoL
repada
redocnE
redocnE
xiferP
retpada
retpada
retpada
Article https://doi.org/10.1038/s42256-025-01170-z
Fig. 3 | Efficiency analysis of scPEFT and related scLLMs. a–d, Percentage accuracies. f, Validation accuracies versus learnable parameters for adapters
of learnable parameters and GPU memory usage for fine-tuned scGPT (a), with different hidden representation dimensions. Larger stars indicate
scFoundation (b), Geneformer (c) and scBERT (d), relative to scPEFT adapters. higher intermediate embedding dimensions that require more tunable
Evaluations were conducted using a batch size of 100 cells (the maximum setting parameters. Default scPEFT settings are marked, with red highlights indicating
for fine-tuning) on an Nvidia RTX A6000 GPU. GPU memory requirements the hyperparameter configurations that offer the best balance between
depend not only on the learnable parameters but also on the gradient performance and efficiency, selected as the defaults in this study. g, Validation
propagation path within the model. e, Validation accuracies plotted against accuracies of fine-tuned scGPT versus scPEFT adapters using a progressively
the number of learnable parameters for different numbers of transformer scaled-down reference dataset. Data points along each curve represent models
layers with adapters. Larger dots represent configurations with more layers, trained on smaller subsets of the referenced set. h, Validation accuracies of
hence more parameters. The default scPEFT settings are highlighted. Notably, training checkpoints for fine-tuned scGPT versus scPEFT adapters. The final
the highest parameter counts may not yield peak performance, indicating point on each curve marks the convergence epoch, defined by no improvement
that overparameterization may misalign with the intrinsic dimensionality of in validation loss over five consecutive epochs or reaching the maximum training
the model, thereby reducing generalization, as reflected in lower validation limit of 50 epochs.
of different cell states (memory CD8+ versus naive CD8+ and effec- with the transition to effector memory from naive T cells22. These find-
tor memory CD8+ versus memory CD8+) from the COVID-19 data- ings reveal that scPEFT provides a valuable alternative approach for
set. The histograms of differential attention scores (Fig. 4c–e and identifying disease-conditional cell-state-associated genes.
Extended Data Fig. 5) indicate that most genes exhibit minimal differ-
ential attention scores in the top transformer layer, while progressively Identifying cells from other animals with scPEFT and scLLMs
displaying more diverse patterns of differential attention in the middle pretrained on human data
and last transformer layers. This progression highlights the capability Most published scLLMs are pretrained on human scRNA-seq data.
of stacked transformers to capture gene contextual features effectively. However, building separate scLLMs from scratch for each species is
Additionally, the greater dispersion of histograms for fine-tuned scGPT impractical. Given that many cellular mechanisms and functions are
and scPEFT than for native scGPT indicates that these adapted models conserved across humans and other animals23, we explored adapting
may provide unique insights into gene–cell associations under disease scPEFT using orthologous genes for cross-species studies (Fig. 5a).
conditions relative to normal conditions. Conversely, the volcano plots Using scGPT as the backbone for scPEFT, we benchmarked
of differential gene expression (Extended Data Fig. 6), which are col- native scGPT, fine-tuned scGPT and scPEFT on a Smart-seq mouse
oured by the correlated differential attention scores of these models, dataset containing finely annotated neuron cell types from the pri-
show that scPEFT and native scGPT are typically highly correlated with mary visual cortex of healthy adult mice24. The results (Fig. 5b and
significantly differentially expressed genes identified through the dif- Supplementary Fig. 6a) show that native scGPT, using an orthologous
ferential gene expression analysis. By contrast, fine-tuned scGPT seems gene subset, achieved an accuracy of approximately 75% in identifying
to overemphasize a broader range of genes across both positive and mouse cell identities despite not being pretrained on mouse scRNA-seq
negative logarithmic fold change regions. These observations indicate data. This indicates the feasibility of adapting human-pretrained
that scPEFT may achieve a better balance between conditional sensitiv- scLLMs to identify cell types in other species. Following domain adapta-
ity and cell-state specificity. tion, scPEFT sharply improved the performancce of the native model
We further examined the genes annotated with the highest atten- (14% improvement, P < 0.001) and outperformed both the suboptimal
tion differences. In the comparison of effector memory CD8+ versus fine-tuned model (3.1% improvement, P < 0.05) and domain-agnostic
memory CD8+ T cells (Fig. 4c–e), all three models successfully identified tools like SingleR and Seurat.
three key effector molecules (KLRB1, GZMA and PRF1). However, scPEFT To examine their applicability, we tested these adapted models in
uniquely enriched CEBPD and SCART1 with high attention scores, which zero-shot settings on two independent datasets with similar cell tax-
have been implicated in effector function and tissue-specific homing onomies from the same tissue, sequenced separately using Smart-seq
in T cells19–21. These findings indicate that scPEFT may uncover previ- and Drop-seq. These tests served as intra-assay and inter-assay evalua-
ously uncharacterized regulators involved in the transitions of effector tions. The fine-tuned model performed consistently in the intra-assay
memory T cells. In the comparison of memory CD8+ versus naive CD8+ zero-shot test (Fig. 5c) but showed a noticeable performance drop in
T cells from COVID-19 infection (Extended Data Figs. 5 and 6), CCL5 and the inter-assay test (Fig. 5d), indicating that fine-tuning may overfit to
GZMK reversed their positions from native scGPT to scPEFT, indicating custom data, thus reducing generalizability to unseen datasets with
that scPEFT had recognized the decreased reliance on CCL5 for memory platform-related variations. By contrast, scPEFT maintained robust
homeostasis and the increased likelihood of an exhausted memory performance across both zero-shot tests.
phenotype with increased attention on GZMK. Additionally, CST7 had We further assessed the adapted models on a macaque dataset
high attention in only scPEFT, which has previously been associated containing important germ and somatic cells (Fig. 5e). These cell
Fig. 4 | Condition-specific cell-state-associated gene analysis via an attention for each signature gene. Statistical significance, indicated by stars on each heat
mechanism. a, Workflow for determining gene contributions to specific cell map, was determined from corrected P values using the two-sided Wilcoxon
states under given conditions. Attention scores, which describe the attention of rank-sum test with Benjamini–Yekutieli false discovery rate control. Differential
the cell representation cls (classification) token on gene tokens, are extracted and attention scores and corrected P values were calculated by comparing cells from
normalized from scLLMs with tuned adapters to assess gene–cell associations. the target T cell subtype with control cells from other T cell subtypes. n = 874,
Differential attention scores between control and target cell states are calculated 391, 242, 724, 2,174, 203, 868, 1,941 and 205 cells were used for the test cases,
to reveal gene roles in cell-state differentiation under the specified condition. b, respectively. c–e, Histograms of differential attention scores from native scGPT
Validation of differential attention values from native and fine-tuned scGPT and (c), fine-tuned scGPT (d) and scPEFT (e) models, in the analysis of COVID-related
from scPEFT, in relation to cell-type-associated signature genes on the NSCLC cell-state-specific genes in effector memory CD8+ T cells versus memory CD8+
dataset. The signature genes sourced from the original study18 are shown on T cells. Histograms were generated for the top, middle and bottom transformer
the x axis with matching colour bars beneath them indicating their associated layers in these models. Red crosses mark the bins where key effector molecules
T cell subtypes on the y axis. The dot plots display the expression profiles of each (KLRB1, GZMA and PRF1) and two effector-function-associated genes (CEBPD and
signature gene across all T cell subtypes. The heat maps illustrate the differential SCART1) arre located. Max, maximum; Min, minimum; T , central memory T cell;
CM
attention scores derived from native scGPT, fine-tuned scGPT and scPEFT models T , effector memory T cell.
EM
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 123
Article https://doi.org/10.1038/s42256-025-01170-z
a Gene expression of Differential
scLLM with tuned Normalized Attentions from cls
cell groups attention
adapters attention map to gene tokens
(target versus control) (target – control)
scPEFT cls
G1
cls
Target G1
G2
G2
G3
G3
Tokenizer Encoder
cls
cls G1
G1
G2 G2
Control G3 G3
cls G1 G2 G3
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 124
tegraT
lortnoC
G2 G3
cls G1 G2 G3
G1
Adapter
b * Corrected P < 0.05 ** Corrected P < 0.01 *** Corrected P < 0.001
Native
Differential
Fine-tuned attention
scPEFT
Min Max
CD4-Naive
CD4-T
CM Percentage
CD4-T expressed (%)
EM
CD4-CD69
CD4-ISG15
CD4-RPL
CD4-T1-like Average
H
CD4-T expression
reg
CD4-Prolif. Min Max
c
300 300
200
150 150 100
SCART1 PRF1 KLRB1 SCART1 GZMA CEBPD PRF1
CEBPD GZMA CEBPD KLRB1 PRF1 SCART1 GZMA KLRB1
0 0 0
–0.04 0 0.04 –0.15 0 0.15 –0.15 0 0.15
d
500 120 60
300
60 30
GZMA
SCART1 CE P B R P F D 1 GZMA KLRB1 SCART1 PRF1 KLRB C 1 EBPD GZMA SCART1 CEBPD PRF1 KLRB1
0 0 0
–0.04 0 0.04 –0.15 0 0.15 –0.15 0 0.15
e
300 120 50
30
150 60
SCART1 PRF1
CEBPD PRF1 GZMA KLRB1 SCART1 CEBP G D ZMA KLRB1 SCART1 GZMA KLRB1 CEBP P D RF1
0 0 0
–0.04 0 0.04 –0.15 0 0.15 –0.15 0 0.15
Differential attention scores
tnuoc
eneG
tnuoc
eneG
tnuoc
eneG
0
Native
scGPT Transformer 1 Transformer 6 Transformer 12
Fine-tuned
Transformer 1 Transformer 6 Transformer 12
scGPT
scPEFT Transformer 1 Transformer 6 Transformer 12
7RCC 1AXNA ANML MDAYM CCGR AMZG 5LCC KMZG SOF BSOF 1PSUD 51GSI 6IFI E6YL 72IFI 92SPR 14LPR 72SPR 7FCT 31LCXC 1DCDP XOT GNFI 3PXOF NYAL 8RCC 76IKM 1NMTS B1ABUT BBUT SMYT
20406080100
Article https://doi.org/10.1038/s42256-025-01170-z
a
Human gene space scPEFT
Orthologues
Projector Inference
Tokenizer Encoder
Annotated cells
Adapter
e
types are rare in the pretraining corpus of most existing scLLMs, which Native scGPT struggled owing to the evolutionary distance between
poses challenges for native scGPT in accurately identifying them. humans and C. elegans (Fig. 5f and Supplementary Fig. 6c). However,
After domain adaptation, scPEFT achieved 39.3% improvements in scPEFT adapted to achieve accuracies around 80%, representing a 145%
accuracy, indicating its ability to capture shared features between improvement over the native model and a 15.3% improvement over the
humans and macaques through orthologous genes. By contrast, the fine-tuning strategy. These results demonstrate that scPEFT regular-
fine-tuning strategy demonstrated weaker transferability, as confirmed izes the adaptation process by preserving pretrained knowledge and
by confusion matrices (Supplementary Fig. 6b). We also conducted leveraging human-tissue-specific features to form more generalized
a remote-species test on the Caenorhabditis elegans ageing atlas. cell representations for distant species such as C. elegans.
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 125
ycaruccA
P = 0.028 P = 3.9 × 10−3
P = 0.049 P = 2.9 × 10−3
P = 0.031
P = 5.7 × 10−3
P = 0.002
1.00 P = 6.3 × 10−5
0.90
0.80 5.28%
0.70 39.3%
0.60
Native Fine-tuned scPEFT SingleR Seurat
ycaruccA
b
1.00
0.95
0.90
0.85
f
0.80
15.3%
0.65
0.50 144.5%
0.35
0.20
ycaruccA
Intra-assay
zero-shot test
P = 0.014 P = 0.26
P = 0.042
P = 0.25
P = 0.06 P = 0.022
P = 4.9 × 10−6 P = 3.2 × 10−6
1.00
3.1%
0.90
14.0%
0.80
0.70
ycaruccA
c
Inter-assay
zero-shot test
P = 0.046
P = 0.029
P = 0.016
P = 2.4 × 10−7
0.95
3.6%
0.85
0.75
30.6%
0.65
0.55
ycaruccA
NA
k
n
NA
NA
Smart-seq2 Smart-seq2 Smart-seq2 d Smart-seq2 Drop-seq
Adaptation data
from Smart-seq2
6.7%
58.3%
Native Fine-tuned scPEFT SingleR Seurat Native Fine-tuned scPEFT SingleR Seurat Native Fine-tuned scPEFT SingleR Seurat
Native Fine-tuned scPEFT SingleR Seurat
Fig. 5 | Cross-species transfer results of scPEFT. a, Schematic workflow for c,d, Violin plots for zero-shot benchmarking of native scGPT, fine-tuned scGPT
adapting the human-pretrained scGPT model to data from other species, and scPEFT under fivefold cross-validation with an intra-assay interdependent
including mouse, macaque and C. elegans. During adaptation, non-orthologous test (c) and an inter-assay interdependent test (d), revealing the greater
genes are masked, and adapters from scPEFT are trained using a small subset stability of scPEFT than the fine-tuning strategy in handling assay variance. e,f,
of annotated cells from the target species, enabling cross-species cell-type Benchmarking violin plots for native scGPT, fine-tuned scGPT and scPEFT under
contextualization. b, Benchmarking performance of native scGPT, fine-tuned fivefold cross-validation with a macaque dataset (e) and a C. elegans dataset (f).
scGPT and scPEFT across fivefold cross-validation with a mice dataset, alongside On each box, the central mark indicates the median, and the bottom and top
comparisons with the stablished cell-type identification tools SingleR and Seurat. edges of the box indicate the 25th and 75th percentiles. The whiskers extend
Violin plots display performance metrics, with paired two-sided Student’s t-tests to the most extreme data points without outliers, and the outliers are plotted
evaluating the statistical significance of differences between scPEFT and other individually as circles. NA, not applicable.
methods across cross-validation results (n = 5 independent validation tests).
Article https://doi.org/10.1038/s42256-025-01170-z
Native scGPT
UMAP1
b
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 126
2PAMU
Fine-tuned scGPT
UMAP1
2PAMU
UMAP1
e Cluster 3 versus cluster 7
REACTOME_CYTOKINE_DIGNALING_IN_IMMUNE_SYSTEM
REACTOME_ADAPTIVE_IMMUNE_SYSTEM HALLMARK_ALLOGRAF N T F _R K E A J P E P C A T B IO _0 N 1 – (P lo v g a1l0ue)
NFKB_Q6 3.0 RCGCANGCGY_NRF1_Q6 2.0 HALLMARK_G2M_CHECKPOINT 1.5
HALLMARK_E2F_TARGETS
YATGNWAAT_OCT_C
CAGCTG_AP4_Q5
–1 0 1
c
Cluster 10 versus cluster 11
HALLMARK_MYC_TARGETS_V1 AML_Q6 –log REACTOME_NEUTROPHIL_DEGRANULATION (P va1l0ue) GTGACGGY_E4F1_Q6 4.0 GCCATNTTG_YY1_Q6 REACTOME_METABOLISM_OF_LIPIDS 2.5 HALLMARK_INTERFERON_GAMMA_RESPONSE 1.0 REACTOME_ADAPTIVE_IMMUNE_SYSTEM REACTOME_INTERFERON_SIGNALING REACTOME_MHC_CLASS_II_ANTIGEN_PRESENTATION –1 0 1 Cluster 2 versus cluster 19
HALLMARK_E2F_TARGETS GGGYGTGNY_UNKNOWN –log REACTOME_CELL_CYCLE (P va1l0ue) REACTOME_CELL_CYCLE_MITOTIC 2.5 HALLMARK_G2M_CHECKPOINT 1.5 HALLMARK_INTERFERON_GAMMA_RESPONSE RYTTCCTG_ETS2_B 1.0 Native scGPT Fine-tuned scGPT scPEFT
AACTT_UNKNOWN
REACTOME_ADAPTIVE_IMMUNE_SYSTEM
d HALLMARK_TNFA_SIGNALING_VIA_NFKB
–1 0 1
Normalized
enrichment score
Percentage expressed (%) Average expression
Min Max
2PAMU
a scPEFT
C T C C C r D D l D e a g 4 4 8 s s T T T ic n C n a a M a i i v v l e e monocyte 0 1 C C C C T M r D D D D e e g 4 8 8 4 m T T T T T n e e C x x r a M e iv g e 0 3 2 1 T C C C M B r D D D e e c g m 4 4 4 el T T T l T C n e r x a M e iv g e 0 3 1 C U CP M A N B C C N P C H C r r c n D K o L D D M S Ce c e o t P k n C 4 m 8 1 e R - - P i n 6 / v B T - l / 7 / p c T T l a o + / M M T + le ( e r t w N a r x D x e B e P e D s g n K - d N P P s c p - 2 i e p m r c / o l o a D l o - s l B N n s m o i 3 b o c ) l y n e t o e T c c y e te ll 1 1 1 0 96 4 8 3 5 2 2 7 1 DCCE CNU C C G C A B C Li T c e nK LL D L M D M M n c P t bPP P k – 1 4 e P P i P / n 6 / / v r g l D / E p i T l a o + s M r NT n r t a / w N a e e P j D n i 1 u v K n - de u P p n - l p m r k o o o c o - s B y n s t o i e b c s l y e t e T cell 1 1 1 1 1 1 1 1 0 9 6 6 4 4 8 3 5 5 2 7 7 1 DCC E G C C M CNU A P C L C i T r c e nK LL M M D L D M n P e P t bPP P k – 1 8 P - P P i P / n 6 / / v B r g D / E P i T a o + s M r N T r n t a / w N a e e P j P n i 1 v u - K n d e P u p n - l r p m k o o o c o - s B y n s t o i e b c s l y e t e T cell 1 1 1 1 1 1 1 0 9 6 4 4 8 3 5 5 2 2 7 7 1
E D G C M G C H C C Li T e M M S L L r M n P P a b P P C – P P P P n / / r g s D / E i u s M r N T l / a o P j P 1 n u c P u n y l k t o e cytes 1 1 1 1 1 1 6 4 8 3 5 7 C MCNP H C G P H r r o M C S l S r P e o a a n C C PR - - s P n B T - s s / 7 / c u / M i M + c l ( l a o D B P a P s c N l P P cs y m 2 ie t c / e l o a D l n l N m o 3 c o ) y n te ocyte 2 2 2 2 2 2 11 2 09 6 4 8 3 5 2 1 C CN P H C G H C r o l C S M S D r o a a n C C 8 R - s P n T - s / s 7 / c u T / M i M + c l ( e l a o D x B P a D s c N l P P cs y m 2 ie t c / e l o a D l n l N m o 3 c o ) y n te ocyte 2 2 2 2 1 11 2 0 9 6 4 8 3 2 1
BTL 47DC 1A4SM A97DC 1APD-ALH 4XOS B97DC 5LLGI A1LCT 4FRI OPM 1BA09PSH 75SSRP NGRS 3NTRP 1APD-ALH APD-ALH 47DC A1RECF A01CELC 1SLAGL 1NCF 8A001S 76IKM 1GTTP SSTC 21A001S 1NCF 2S0G 2RLT
3 7 10 11 2 19
3
7
10
11
2
19
20 40 6080100
PLC PTE/PLC B-orp-erp/PLC PMC PDM/PMC PPM/PMC PPM/CSH sCSH PPM 1ND/PTE PMG B-erP )3ND/2ND(/T-orP etyconom
lacissalC
etyconom
detavitcA
lacissalc-noN etyconom llec B llec B +7RCC KN +61DC T 4DC MC xeT 4DC evianT 4DC xeT 8DC evianT 8DC etycolunarG setycolunarg-niL gerT meM gerT KN
1,600
1,400
1,200
1,000
800
600
400
200 0
IHC
Native scGPT
Fine-tuned scGPT
scPEFT
Fig. 6 | scPEFT identifies developmental cell populations in BMMC and identified more distinct clusters than native scGPT. Notably, scPEFT was able to
CD34+-enriched CITE-Seq data. a, UMAP visualizations of cell representations avoid some perplexing splitting or combining that confounds the interpretation
from native scGPT, fine-tuned scGPT and scPEFT, trained on scRNA-seq data of the fine-tuned model. For instance, the fine-tuned model nearly equally split
from BMMC and CD34+-enriched cells, excluding cell identity annotations. The the CD4 T cell population between a group of memory T cells and exhausted
CM reg
arrow points to a BMMC mature B cell subset, which clusters closer to pre-proB CD4+ T cells and combined two groups of T cells and naive CD4+ T cells,
reg
and PreB cells, as annotated by protein (Supplementary Fig. 7). b, Evaluation of indicating some confusion among memory programs. d, Expression profiles
cell representations from native scGPT, fine-tuned scGPT and scPEFT models of genes receiving high differential attention scores in subgroups 3 versus 7, 10
using the CHI. This metric assesses the ability of generative embeddings from versus 11, and 2 versus 19 from c, with colours representing mean expression
each model to effectively characterize protein-annotated cell groups. c, Sankey within each cluster and dot sizes indicating the fraction of cells expressing a
diagrams illustrating the assignment of cells from protein-annotated identities gene. e, Gene set enrichment analysis based on attention differential scores for
(left) to clustering results (right), obtained using the Leiden algorithm at a these subgroups, showing normalized enrichment scores with colours denoting
resolution of 1.5. Clustering was performed on embeddings generated by native the significance of enriched phenotypes. n = 1,093, 1,390 and 1,686 cells were
scGPT, fine-tuned scGPT and scPEFT models. Fine-tuned scGPT and scPEFT used for the test cases, respectively18.
Article https://doi.org/10.1038/s42256-025-01170-z
These experiments demonstrate that scPEFT holds promise for activated monocyte population. Clusters 10 and 11 represented a split of
bridging the species divide by capturing a shared embedding subspace common myeloid progenitors, with cluster 11 enriched for class II mol-
of orthologs, facilitating integrated analyses across diverse organisms. ecules and antigen-presentation signatures, consistent with a distinct
differentiation pathway. Cluster 10 combined common myeloid progeni-
Uncovering biologically relevant cell populations with scPEFT tors, granulocyte–monocyte progenitors and multi-potent progenitors,
in an unsupervised manner indicating a mix of premature and undifferentiated myeloid cells not
Aiming to enable scLLMs to identify new cell states and potentially distinguishable by protein panel alone. These findings demonstrate the
undiscovered regulators of cell phenotypes and activities from ability of scPEFT to resolve biologically relevant subpopulations. Consist-
under-studied single-cell data without pre-annotations, we validated ent with this, further testing on a lung cancer atlas (Supplementary Note
the unsupervised adaptation protocol in scPEFT (Methods) with scGPT 8) showed that scPEFT more effectively preserves the global structure of
as an example backbone for scPEFT, on a human bone marrow and cell types while offering enhanced sensitivity to context-specific cellular
CD34+-enriched CITE-Seq dataset. CITE-Seq protein serves as a natu- heterogeneity in atlas-scale disease settings.
ral ground truth for classifying bone marrow cells, which have been
extensively characterized using techniques like flow cytometry. Con- Enhancing scLLMs on domain-specific downstream tasks
sequently, we annotated these cell identities according to their surface We further evaluated scPEFT on downstream tasks supported by
protein expression profile (Supplementary Fig. 7) but excluded them the respective scLLMs (see the summary in Supplementary Note 1),
from the adaptation process. UMAP visualizations colour-coded by including transcription factor identification, batch effect correction
the protein identity of each cell (Fig. 6a) demonstrate that the sub- and gene perturbation prediction. For transcription factor iden-
populations for fine-tuned scGPT and scPEFT have more heterogeneity tification, the token adapter in scPEFT consistently outperformed
compared with those from native scGPT, particularly among granulo- fine-tuned Geneformer, achieving improvements in the area under the
cytes, B cells and B cell progenitors. scPEFT has notable granularity in receiver operating characteristic curve (AUC) of 9.5%, 28.7% and 9.52%
delineating cellular populations, uniquely identifying nuances such (Extended Data Fig. 7) on the three datasets (Supplementary Note 3).
as a subset of mature B cells from BMMC (defined by protein) exhibit- It also exhibited a lower AUC variance across folds, indicating more
ing phenotypes closer to progenitor B cells (see the arrow in Fig. 6a). robust and specialized adaptation in this challenging task.
This may indicate that some B cells with remnants of developmental In batch correction, several scPEFT adapter strategies better pre-
programs are not captured by surface proteins or fine-tuned scGPT. served cell-type distributions across batches, achieving improvements in
We also applied the Leiden clustering algorithm25 with a resolution the average biological conservation score (Avg ) of 2.0–6.4% (Extended
BIO
of 1.5 to cell embeddings from these models. This resolution controls Data Figs. 8–10). Although scPEFT performs suboptimally on batch-mixing
the granularity of the clustering and allows the algorithm to determine metrics compared with scVI27 and Scanorama28 on certain datasets, it
the number of clusters adaptively based on the data. Using the same more effectively conserves biological cell relationships, resulting in bet-
resolution across different tuning strategies ensures a fair comparison ter overall performance relative to fully fine-tuned scGPT. Although these
of the clustering structure and cell membership at the same level of specialized tools excelled in batch mixing, they demanded higher param-
granularity. The Calinski–Harabasz index (CHI) scores (Fig. 6b) indi- eter updates or longer runtimes on the central processing unit (CPU)
cate that most of the clusters from scPEFT are more compatible with (Supplementary Fig. 8), whereas scPEFT was a more efficient solution.
the dispersion of protein-annotated cell groups. Note that in most For perturbation prediction using scFoundation and scGPT,
groups, the CHI scores from the fine-tuned model are obviously lower scPEFT enabled scFoundation to overcome GPU memory limitations
than for their native counterparts, evidencing catastrophic forgetting encountered during fine-tuning. It improved the mean squared error
caused by the fine-tuning process. From the connections between the (MSE) and Pearson’s correlation coefficient (PCC) for the top 20 most
protein annotations and scRNA clusters (Fig. 6c), we observed that differentially expressed genes (MSE_DE and PCC_DE) by 0.06 and up
fine-tuned scGPT and scPEFT found a larger number of distinct clusters, to 0.15, respectively, compared with zero-shot scFoundation, and
compared with native scGPT, and identified similarly unique splits with by 0.02–0.05 and up to 0.04, respectively, compared with GEARS29
no heterogeneity among the surface proteins, like B cells and classical (Supplementary Table 5). These improvements highlight the impor-
monocytes. However, scPEFT was able to avoid some perplexing split- tance of efficient adaptation for this task. scPEFT also outperformed
ting or combining that confounds the interpretation of the fine-tuned a linear model baseline30 by 0.02 to 0.09 in MSE_DE and 0.02 to 0.15
model. For instance, the fine-tuned model nearly equally split the CD4 in PCC_DE. However, none of the deep learning models surpassed
T population between a group of memory regulatory T (T ) cells and the linear model when evaluated across all genes (Supplementary
CM reg
exhausted CD4+ T cells and combined two groups of T cells and naive Note 9). scPEFT with the scGPT backbone performed comparably
reg
CD4+ T cells, indicating some confusion among memory programs. with fine-tuned scGPT and GEARS, except on the Norman dataset with
We investigated the functional interpretations of new subgroups two-gene perturbations (Supplementary Table 6). When evaluating all
(clusters 3 and 7, 2 and 19, and 10 and 11) identified by scPEFT using a genes, no significant differences were observed among these models.
gene set enrichment analysis26. Genes with differential attention scores Given its lower memory and time requirements, scPEFT offers a practi-
between subgroups (top-ranked genes in Fig. 6d) were submitted to cal and accessible solution for predicting perturbation responses in
the gene set enrichment analysis, which revealed subgroup-specific the most differentially expressed genes.
biological functions (top five in Fig. 6e). Cluster 3 was enriched for NF-κB
target genes and human leukocyte antigen molecules, whereas cluster 7 Discussion
showed enrichment for pro-growth and developmental pathways (E2F Traditionally, full fine-tuning of scLLMs is used to enhance down-
and AP4 targets, SOX4 and IRF4), indicating the identification of a recently stream task performance by updating all model parameters. How-
developed B cell cluster and an activated or memory B cell. Activated ever, this approach risks distorting pretrained features12, especially
monocytes split between cluster 2 on its own or cluster 19, where they in out-of-context applications where the data distribution diverges
combined with classical monocytes. Cluster 19 shows high attention for substantially from the pretraining corpus. scPEFT addresses this by
classical monocyte markers (CD14, CD36 and ITGAX) and enrichment reparameterizing the model parameters with low-dimensional prox-
of inflammatory and antigen-presentation pathways (TNF and NF-κB ies and restricting task adaptation to a separate subspace. This greatly
signalling, CTSS and TLR2), indicative of an intermediate monocyte reduces the number of trainable parameters, enabling faster conver-
population. Cluster 2 monocytes had reduced CD14 attention, increased gence and less annotated data requirements, thereby cutting adap-
MKI67 attention and enriched pro-growth gene sets, indicating a true tation time and effort. By preserving the original parameter values,
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 127
Article https://doi.org/10.1038/s42256-025-01170-z
scPEFT minimizes overfitting and catastrophic forgetting, resulting To embed the gene names and gene expression profiles, two
in better performance and greater computational efficiency across embedding layers, denoted as embg and embe , are used, respectively,
diverse single-cell analyses. We recommend using scPEFT to generate to obtain the final gene representation h(i):
context-aware embeddings from scLLMs for a wide range of down-
stream tasks. It supports both supervised and unsupervised modes for h(i)=embg(t(
g
i))+embe(x(
e
i)). (3)
datasets with or without pre-annotations. Furthermore, its attention
analysis enables condition-specific interpretation, which facilitates Unlike scBERT and scGPT, scFoundation directly uses continuous
more precise and context-aware discoveries. gene expression values as x(i), thus avoiding the information loss associ-
e
scPEFT extends the capabilities of scLLMs beyond their original ated with discretization or binning schemes. By contrast, Geneformer
human-centric pretraining corpus. Its plug-in adapters enable the ranks genes according to their relative expression levels across its entire
recognition of gene programs in other species by leveraging ortholo- Genecorpus-30M transcriptomic corpus5 to embed gene expression
gous gene subsets. However, one-to-one orthologous mapping is not profiles instead. In this case, equation (2) becomes
always possible. Future work will explore advanced homology inference
methods31 to incorporate non-orthologous genes with functional or x(i)=argsort[ 10,000X (i,j) ], (4)
e
evolutionary similarity. Another promising direction involves develop- median(gj)
ing a gene vocabulary adapter to align non-orthologous gene embed-
dings into the orthologous feature space, which would enable scPEFT where median(⋅) retrieves the non-zero median expression level of a
to capture transcriptomic landscapes across species. gene across Genecorpus-30M as a normalization factor, and argsort[⋅]
We describe optimal use cases of scPEFT across diverse scLLM extracts the rank index. The normalized expression values are scaled
backbones and applications in Supplementary Note 10. Although by multiplying them by 10,000 to enhance precision and are subse-
default hyperparameter values were used throughout this study, fur- quently adjusted by dividing them by the corpus-wide median normali-
ther performance gains may be achieved by task-specific optimization. zation factor. This implementation assigns lower ranks to housekeeping
The four adapter types in scPEFT can also be flexibly combined to suit genes, which exhibit stable expression, whereas transcription factors,
particular scenarios (Supplementary Note 11). Designed as a modular characterized by greater variability, are ranked higher. This ranking
and extensible framework, scPEFT is compatible with future scLLMs strategy improves the robustness of xe against technical variants.
and evolving single-cell parameter-efficient fine-tuning techniques
(Supplementary Note 12), despite certain engineering challenges (Sup- Encoder. The current batch of scLLMs use the transformer architec-
plementary Note 13). We are committed to maintaining and expanding ture35 to model gene expression patterns in cells. This architecture
scPEFT to support emerging scLLMs, particularly task-specific models consists of stacking n transformer blocks (n = 6 in scBERT4, n = 6 or 12
such as STATE32 for perturbation prediction, as well as adding more in Geneformer5, and n = 12 in scGPT6 and scFoundation7), in which each
tasks to better serve the broader single-cell research community. block includes a self-attention layer Att(⋅), two layer normalizations
Additionally, scPEFT is extensible in interacting with foundational LayerNorm(⋅), and a multi-layer perceptron MLP(⋅). This set-up is
models from other modalities, such as proteomics33 and imaging34, thus designed to capture interrelated gene patterns, which enables the
enabling an efficient, comprehensive and multimodal understanding computation of all learned gene embeddings h(i) from cell i as follows,
l
of cellular behaviours and interactions.
h(i)=[h(i,1),h(i,2),…,h(i,j),…,h(i,M)], (5)
Methods
Architecture of scLLMs
h(i)=h(i), (6)
A typical scLLM has a tokenizer to vectorize gene identities and expres- 0
sion values and a multi-head transformer encoder to aggregate gene
expression in cells into gene and cell representations. These are fol- att(i) =LayerNorm(Att(h(i) )+h(i) ), (7)
l−1 l−1 l−1
lowed by a task-specific projector for inference (Fig. 1a).
Tokenizer. Current scLLMs conceptualize single-cell expression pro- h(i)=LayerNorm(MLP(att(i) )+att(i) ),∀l∈[1,n]. (8)
l l−1 l−1
files as a form of biological language. Like LLMs, current scLLMs require
the tokenization of genes, which converts them into vector representa- Each cell, represented as a sequence of M genes, is then summa-
tions for downstream learning. However, the key difference in scLLMs rized by concatenating or pooling the learned gene-level representa-
is that their tokenizer needs to encode both the gene name and its tions h(i) in scBERT, Geneformer and scFoundation, respectively. In
l
expression profile. Each scLLM maintains a gene vocabulary based on certain scLLMs (for example, scGPT), a special gene-level classification
its training corpus, assigning a unique integer identifier, id(gj), to each token 〈cls〉 is placed as h(i,M+1). This token allows the model to learn an
gene gj within a given input cell i. Consequently, the gene token vector adaptive pooling operation for cell representation through the
t(i) for cell i is represented as follows: self-attention mechanism35 in transformer blocks.
g
t(i)=[id(g(i)),id(g(i)),…,id(g(i))]. (1) Projector. Typically, a MLP serves as a projector, mapping the learned
g 1 2 M
gene embedding h(i,j) from the last lth transformer block into a desired
l
Here M is the total number of genes in the input cell. When input genes prediction. This gene-level prediction can be a predicted gene expres-
do not match the predefined vocabulary, scLLMs omit them from the sion value or a gene ID. For cell-level predictions, the cell embedding
input. Furthermore, unlike traditional LLMs, scLLMs also incorporate h(i,M+1) is routed through a dedicated projector designed specifically
the expression profile of each gene into the token. A prevalent approach for cell-based tasks. The structure and configuration of these cell
used by scBERT and scGPT involves discretizing the normalized expres- projectors are tailored according to the specific cell-level tasks.
sion value X(i,j) of cell i into m discrete bins [b1,b2,…,bm], yielding the
expression profile vector x(i): Pretrained settings in scLLMs. In general, scLLMs used the masked
e
language model objective during the pretraining stage to encour-
age the learning of gene contextual features. This objective involves
x(
e
i)={k, ifX(i,j)>0andX(i,j)∈[bk,bk+1],k∈[1,m];0,ifX(i,j)=0}. (2)
randomly masking selected non-zero gene tokens and predicting the
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 128
Article https://doi.org/10.1038/s42256-025-01170-z
original tokens based on the context provided by the non-masked gene another MLP restores this compressed representation into an adap-
tokens. The learning objective is defined as follows: tive d-dimensional gene embedding. As a result, equation (3) is modi-
fied as follows:
LGEP=
|Um
1
ask| j∈
∑
Umask
loss(projector(h
n
(i,j))−x(i
j
)). (9)
h˜(i)=embg(t( g i))+Adapter(embe(x( e i))), (12)
In equation (9), Umask represents the set of masked non-zero genes, where Adapter(⋅) denotes the autoencoder-inspired small neural net-
and x(
j
i) denotes the actual binned expression value for each gene gj in work module. The resulting gene embedding h˜(i) is then fed into the
input cell i for scBERT, the raw expression value for scFoundation and subsequent transformer-based encoder. During training, only the
scGPT, or the gene identity in Geneformer. The projector(⋅) function adapter parameters are updated, while native scLLM was unchanged.
here decodes the gene embedding h(i,j) to predicted gene profile of This adapter layer, designed to improve the compatibility of gene
n
gene gj . scBERT, Geneformer and scGPT uses MLP, whereas scFounda- tokens across diverse biological contexts, is referred to as the
tion adopts a transformer architecture for the projector module in its ‘token adapter’.
pretraining. The loss(⋅) function measures the difference between the
predicted and actual gene information. scBERT and Geneformer use Prefix adapter. Extending task tokens to intermediate representations
the cross-entropy loss5 and scGPT uses the MSE loss6. is a popular method for introducing task-specific information into the
In scGPT, an extra objective models the relations between the natural language processing domain. Following the method of Li and
special cell token 〈cls〉 and other gene tokens, defined as Liang39, we insert learnable task tokens into the intermediate embed-
ding, which enables the model to generate task-aware representations.
qj=MLP(embg(t(
g
i))), (10) Given the embedding h(
l
i) for all genes from cell i at the lth transformer
block defined in equation (5), the extended embedding h˜(i) is defined
l
as follows:
LGEPC=
|Um
1
ask|
j∈
∑
Umask
MSE(qj⋅Wh(
c
i)−x(i
j
)), (11)
p=[p1,p2,…,pk], (13)
where qj is the gene identity embedding generated by the tokenizer h˜(i)=concat(cls,p,h (i) )orh˜(i)=concat(p,h (i) ), (14)
for each gene gj in input cell i. These embedding queries contain a l l l l
predicted expression value for gene gj from cell representation h(
c
i),
w to h t i h ch e 〈 is c t ls h 〉 e t o o u ke tp n u . T t f h r e o m qu t e h r e y f u in se a s l t a r a p n a s r f a o m rm et e e r r i b z l e o d c k in c n o e r r r e p s r p o o d n u d ct in W g a˜tt ( l i) =LayerNorm(Att(h˜( l i))+h˜( l i)), (15)
with the cell representationh(i), and the MSE function MSE(⋅) measures
c
t a h s e s h er o r w o n rs i b n e e t q w u e a e t n io t n h e ( 1 p 1 r ) e . d D i u c r t i e n d g a p n r d e a tr c a t i u n a i l n g g e , n a e n e o x p p t r i e m s i s z io er n s v u a c lu h e a s s , h˜( l+ i) 1 =LayerNorm(MLP(a˜tt ( l i) )+a˜tt ( l i) ),∀l∈[1,n], (16)
Adam36 is used to backpropagate gradients from the loss function L
to update the model parameters. This training process typically uses where p represents the added task token embedding, which comprises
several single-cell atlases. For example, the training set for scFounda- learnable tensors of the same dimension as the intermediate gene
tion includes over 50 million single cells from diverse organs and embedding h(i) and cell embedding 〈cls〉 (if applicable for the target
l
tissues; scGPT was trained on 33 million cells across various tissues scLLM). During training, only the learnable tensors in p are updated,
collected from CELLxGENE37; scBERT is grounded in the diverse while the parameters of the native scLLM remain unchanged. This
PanglaoDB38 with over 1.1 million cells; and Geneformer relies on 29.9 extension, aimed at expanding the semantic capacity of intermediate
million transcriptomes from the Genecorpus-30M5. The pretrained gene and cell embeddings to incorporate task-specific information, is
scLLMs embed essential biological insights from this extensive corpus denoted the ‘prefix adapter’.
and can be used to generate cell or gene representations in a zero-shot
setting or serve as a base model for further tuning in diverse LoRA. Low-rank adaptation (LoRA)40 is widely used in foundation
downstream applications. models for natural language processing to reduce computational costs
during fine-tuning by introducing low-rank matrices, as illustrated in
scPEFT integrates learnable adapters into scLLMs Fig. 1. We used LoRA to efficiently update the parameters in the
In scPEFT, we add four low-dimensional, learnable and pluggable adapt- self-attention layers of transformer blocks for downstream tasks. With
ers to existing scLLMs (Fig. 1b). These adapters, which have markedly LoRA, the query Ql , key Kl and value Vl components in the self-attention
fewer parameters than the scLLMs themselves, are integrated into layer of the lth transformer block are computed as follows:
various components of the models. They are specifically tuned to
estimate parameter deltas for their connected scLLM modules, under Q˜ l=WQ⋅h(
l
i)+ΔWQ⋅h(
l
i)=WQ⋅h(
l
i)+BA⋅h(
l
i), B∈Rd×r,A∈Rr×d, (17)
the supervision of task-specific data and objectives to bridge context
gaps and enable diverse downstream tasks in out-of-context scenarios
(Fig. 1c). During the scPEFT tuning process, the original scLLM param-
K˜ l=WK⋅h(
l
i), (18)
eters remain frozen to preserve the pretrained knowledge of the model.
Token adapter. Technical variations in single-cell expression profiles V˜ l=WV⋅h( l i)+ΔWV⋅h( l i)=WV⋅h( l i)+BA⋅h( l i), (19)
across datasets may lead to out-of-context issues. To mitigate this,
we developed a tunable adapter, appended to the gene token embed-
ding layer, to calibrate the query gene embedding into the pretrained Att(Q˜ l,K˜ l,V˜ l)=softmax(
Q˜ lK˜T
l )V˜ l, (20)
gene embedding space within the tokenizer. This adapter functions √d
as an autoencoder-like module by combining an MLP and a rectified
l i i n n t e o a a r u m n o it r a e c c t o iv m at p io a n ct t s o - d co im m e p n r s e i s o s n d a - l d f im or e m n a si t o ( n s a « l d g ) e . n S e u e b m se b q e u d e d n in tl g y s , a˜tt ( l i) =LayerNorm(Att(Q˜ l,K˜ l,V˜ l)+h( l i)), (21)
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 129
Article https://doi.org/10.1038/s42256-025-01170-z
h( l+ i) 1 =MLP(LayerNorm(a˜tt ( l i) ))+a˜tt ( l i) ,∀l∈[1,n]. (22) L=cross-entropy(MLP(h( c i)),z(i)), (25)
Here WQ , WK and WV represent the pretraining weights for generating where h(
c
i) denotes the embedding for the ith cell, and z(i) represents its
query, key and value components, respectively, which remain frozen annotated cell type.
during the fine-tuning stage to retain the pretrained knowledge. h(i) We followed the default fine-tuning configurations provided by
l
denotes all gene embeddings from cell i at the lth transformer block each scLLM when fine-tuning them for the cell-type identification task.
defined in equation (5). Updates to the query and value components During the domain adaptation by scPEFT, we used the Adam optimizer36
are approximated through two trainable low-rank decomposition with an initial learning rate of 10−5. Throughout this process, the learn-
matrices, A and B, of dimension r×d and r×d, respectively, where r is ing rate was gradually decreased to minimize the risk of missing the
a predefined low rank (with r≪d and d being the dimension of the global optimum. We set a maximum of 100 training epochs and applied
gene or cell embedding). We applied LoRA only to the query and value an early stopping criterion if there was no improvement in the valida-
components for simplicity40. The initialization of A and B is specified tion loss for five consecutive epochs.
with a random Gaussian and zeros, separately. Hence, ∆W = BA is zero
at the beginning of training on a specific task. After training, the Attention-based cell-state-specific gene association measure
task-specific context is embedded implicitly into the low-rank matrices To quantify the association of each gene with specific cell states, we
A and B to guide context-aware gene and cell embeddings h(i). derive the attention map from the final lth transformer block as follows:
l+1
Encoder adapter. To further adapt scLLMs for out-of-context data, Ql=WQ⋅h(
l
i), Kl=WK⋅h(
l
i), Vl=WV⋅h(
l
i), (26)
we integrated an adapter within the transformer layers in the targeted
scLLM (Fig. 1b). Positioned after the self-attention layers, this adapter
T
aligns learned gene embeddings from context-specific data with pre- Att(Ql,Kl,Vl)=attmap⋅Vl=softmax( QlKl )⋅Vl. (27)
trained universal patterns, thus facilitating knowledge transfer from √d
the pretrained model and preventing catastrophic forgetting. In this
set-up, equations (7) and (8) are modified as follows: Here h(i) represents the latent representations for gene or cell i at the
l
attention layer of the lth transformer block. WQ , WK and WV are the
a˜tt ( l i) =Adapter l (LayerNorm(Att(h( l i))+h( l i))), (23) weights from scLLMs using either fine-tuning or scPEFT. Notably, the
raw attention scores are computed post-softmax function across
several attention heads (for example, 8 heads in scGPT, 10 heads in
h( l+ i) 1 =LayerNorm(MLPl(a˜tt ( l i) )+a˜tt ( l i) ), ∀l∈[1,n]. (24) scBERT, 12 heads in Geneformer and scFoundation, and so on). The
average over these heads is obtained as a comprehensive measure.
Here the extra Adapter(⋅) is also an autoencoder-like small neural net- In the average attention map, the row indexed by the cls token (cell
work module. During the training process, only the adapters are representation) represents the influence of all genes on the cell, as
updated. We term this component the ‘encoder adapter’ because it interpreted by the tuned model. This row enables us to observe the
customizes gene and cell relationships within the encoder module to significance of genes within distinct cell groups. Furthermore, to
the specific task, leading to context-aware embeddings that enhance identify genes most strongly associated with a target cell group, we
task performance. calculated the differential attention score between two closely related
cell groups (Fig. 4a).
Implementation of downstream tasks in scPEFT
In this study, we evaluated scPEFT with four backbone models: scBERT, Orthologous gene mapping for cross-species transfer
Geneformer, scGPT and scFoundation. To minimize potential bias, we To leverage the scLLMs pretrained on human data on datasets from
applied their official fine-tuning protocols (Supplementary Table 1) other species, we first extracted the overlapping genes between the
rather than designing custom benchmarking pipelines. The evaluation human gene vocabulary in each scLLM and the custom dataset from
metrics used in these tasks are summarized in Supplementary Table 2. the other species to define the input feature space. This mapping
was implemented using the R package geneSyonym to query the
Cell-type identification with scLLMs in zero-shot settings HomoloGene database released by the National Center for Biotech-
We followed the reference mapping workflow of scGPT to apply scLLMs nology Information41. Only the matching genes were considered in
for cell-type identification in zero-shot settings. In this approach, our cross-species analysis.
native scLLMs were directly used to embed reference cells and query
cells separately. To transfer annotations from the reference set to Cell group discoveries in an unsupervised manner
a query cell, the k-nearest reference cells for the query cell in the When previous annotations are unavailable, scLLMs can still be adapted
embedding space (k = 10 in our study, as suggested in the tutorial for to custom data by reconstructing gene expression levels through
scGPT) were identified. The inferred cell type of the query cell was then self-supervised learning by scLLMs. To this end, some gene expres-
determined through a majority vote based on the cell types of these sions are randomly masked. Their predictions are generated from their
k-nearest references. gene embeddings and cls embedding (if applicable) within the scLLMs.
The pretrained objective functions, such as equations (9) and (11), are
Supervised cell-type identification applied in this scenario. In this approach, gene and cell representations
To identify cell types, scLLMs typically assign an MLP as a projector simultaneously learn to embed how cell regulatory programs organize
and then fine-tune it on a pre-labelled reference set. This projector themselves and the relationship between this organization and the cell
interprets cell representations (the cls tokens or aggregations of all activities and phenotypes. The unsupervised tuning of scPEFT was
gene embeddings in an scLLM) from the encoder module into cat- conducted using the same configurations for the optimizer, learning
egorical cell-type predictions. A cross-entropy6 loss function between rate, learning scheduler and early stopping criteria as in the supervised
predictions and annotated cell types from referenced data was used settings. The tuned models produce embeddings for all input cells,
as the loss function to supervise training. Accordingly, equation (9) is which are then clustered using Leiden25 at a resolution of 1.5 to reveal
adjusted as follows: potential new cell groups.
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 130
Article https://doi.org/10.1038/s42256-025-01170-z
Transcription factor identification
Geneformer was designed to identify different types of transcription
L=LGEPC+LGEP+LECS+LDAR. (32)
factors, which are fundamental components of gene regulatory net-
works. Such a task is a binary classification problem on transcription Perturbation prediction
factor genes across the gene panel in a single-cell transcriptomic In this task, we used scGPT and scFoundation as the backbone in
dataset. To enable gene token prediction, an MLP-based token classi- scPEFT due to their openly available codebases. For perturbation
fier was appended to the Geneformer backbone as a task projector, prediction, scGPT considers all genes, regardless of zero or non-zero
which transformed gene embeddings into inferred logits for each expression values. To predict absolute perturbed expression levels, we
input gene. For transcription factors from different gene regulatory used log1p-normalized expression values as both the input and target,
networks, Geneformer requires adaptation tuning to capture the diverging from original design of scGPT, which uses binned values. A
nuanced differences between a specific type of transcription factor binary condition token indicating whether a gene is perturbed was
and other transcription factors. In this task, all genes from the gene implemented in the tokenizer, thus modifying equation (3) as follows:
panel in a single-cell transcriptomic dataset were used as input to
learn gene contextual patterns, but non-transcription factor genes h(i)=embg(t(
g
i))+embv(x(
v
i))+embc(t(
c
i)), (33)
were masked out during both model adaptation and inference. The
objective function for this task aims to minimize the cross-entropy where embc denotes the condition embedding layer, which encodes
as follows: the binary perturbation condition token t(i) for each gene in cell i. This
c
adjustment renders the gene embedding perturbation informed. The
LTF=cross-entropy(MLP(h(
T
i
F
)),y(i)), (28) objective function for perturbation prediction aims to minimize the
difference between the predicted and true post-perturbation gene
where h(i) represents the transcription factor gene embeddings from expression values, defined as:
TF
the final transformer block, and y(i) are the labels of these transcription
factor genes. We adopted the default adaptation configurations from L=MSE(MLP(h(i)),z(i′)), (34)
g
scPEFT, including a learning rate of 10−5, a maximum of 50 training
epochs and early stopping based on the AUC of the validation subset. where h(i) is the gene embeddings of control cell i from the final trans-
g
To ensure a fair comparison and avoid excessive runtimes, we former block, and z(i′) is the perturbated gene expression for a randomly
fine-tuned Geneformer using its default settings rather than with its paired perturbated cell i’ of the same cell type. This approach, aligned
recommended hyperparameter optimization protocol. with scGPT6 and GEARS29, facilitates learning the general perturbated
effects across cells. The configurations of the optimizer, learning rate,
Batch correction learning scheduler and early stopping criteria of scPEFT with the scGPT
We used several learning objectives for batch correction as defined by backbone in this task were the same as in the supervised settings.
scGPT6. The configurations of the optimizer, learning rate, learning Unlike scGPT, scFoundation builds on the GEARS framework to
scheduler and early stopping criteria in this task were the same as in perform perturbation prediction. In GEARS, each gene is first embed-
the supervised settings. Specifically, two pretraining objectives, equa- ded and then processed by a graph neural network. scFoundation
tions (9) and (11), were applied to guarantee the context-aware nature replaces the native GEARS gene encoder with embeddings enriched
of the generative gene and cell representations. Another embedding through large-scale pretraining. To support this integration, it con-
layer embb is incorporated to encode batch information into the learned structs the gene relationship graph using its full vocabulary of 19,264
gene and cell representations from the final transformer block as: genes, rather than limiting it to the expressed genes in perturbed and
control cells as in GEARS. The training and prediction procedures of
h˜(
n
i)=concat(h(
n
i),embb(t(
b
i))), (29) scPEFT with scFoundation, including the objective function, optimizer
settings, learning rate, learning scheduler, early stopping and evalua-
where h(i) denotes the output gene and cell representations from the tion metrics, follow those used in GEARS.
n
final transformer block, and t(i) represents the labelled batch identity
b
for cell i. Reporting summary
To further enhance batch correction, scGPT has another objective Further information on research design is available in the Nature
named elastic cell similarity (ECS), which maximizes the similarity of Portfolio Reporting Summary linked to this article.
cell representations sharing the same labelled batch identity. The ECS
objective is defined as follows: Data availability
All datasets used in this study are publicly available. The NSCLC, BMMC
LECS=−(cosine(h(
c
i),h(
c
j))−β)whent(
b
i)=t(
b
j), (30) and CD34+, Mouse, Mouse-10x/smart-seq, and macaque datasets
can be accessed under numbers GSE179994, GSE139369, GSE115746,
where h(i) and h(j) refer to two cell embeddings from the same batch GSE185862 and GSE142585 of the Gene Expression Omnibus (GEO),
c c
identity. The cosine similairty is used to measure their dissimilarity, respectively. The MS dataset is available at https://www.ebi.ac.uk/gxa/
with β as a predefined margin. sc/experiments/E-HCAD-35. The COVID-19 dataset can be accessed via
Another objective, domain adaptation via reverse backpropaga- Figshare at https://doi.org/10.6084/m9.figshare.16922467.v1 (ref. 42).
tion (DAR), addresses the batch artefacts arising from sequencing The C. elegans dataset is available from Calico Research at https://c.
technology. In this approach, an MLP classifier is assigned to predict elegans.aging.atlas.research.calicolabs.com/. The processed Lung
the batch identity t(i) based on each cell representation h(i). The DAR atlas can be downloaded as a h5ad file from https://cellxgene.czisci-
b c
objective function is as follows: ence.com/collections/edb893ee-4066-4128-9aec-5eb2b03f8287. The
Bivalent promoters, long-range transcription factor and NOTCH1
LDAR=cross-entropy(MLP(h(
c
i)),t(
b
i)). (31) network datasets were preprocessed and published by Geneformer in
its Hugging Face repository at https://huggingface.co/datasets/ctheo-
Here the cross-entropy quantifies the error between the predicted doris/Genecorpus-30M/tree/main/example_input_files/gene_clas-
identity and the actual batch identity. Eventually, the overall objective sification. The Adamson, Norman, Replogle_k562 and Replogle_rpe1
for batch correction combines equations (9), (11), (30) and (31): datasets can be extracted and preprocessed using GEAR’s PerData
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 131
Article https://doi.org/10.1038/s42256-025-01170-z
class load function by specifying the data_name argument as ‘norman’, 20. Park, D. et al. Differences in the molecular signatures of
‘adamson’, ‘replogle_k562_essential’ and ‘replogle_rpe1_essential’, mucosal-associated invariant T cells and conventional T cells. Sci.
respectively. The PBMC 10K dataset can be extracted via scvi’s CLI: scvi. Rep. 9, 7094 (2019).
data.pbmc_dataset(). The Prirhinal cortex and COVID-BATCH datasets 21. Teng, X. et al. SIGIRR deficiency contributes to CD4 T cell
are available via GitHub at https://github.com/bowang-lab/scGPT/ abnormalities by facilitating the IL1/C/EBPβ/TNF-α signaling axis
tree/main/data. All processed datasets can be accessed via GitHub at in rheumatoid arthritis. Mol. Med. 28, 135 (2022).
https://github.com/coffee19850519/scPEFT and via Figshare at https:// 22. Yang, R. et al. Distinct epigenetic features of tumor-reactive CD8+
doi.org/10.6084/m9.figshare.30763886 (ref. 43). T cells in colorectal cancer patients revealed by genome-wide
DNA methylation analysis. Genome Biol. 21, 2 (2020).
Code availability 23. Hodge, R. D. et al. Conserved cell types with divergent features in
The source code is freely available via GitHub at https://github.com/ human versus mouse cortex. Nature 573, 61–68 (2019).
coffee19850519/scPEFT and via Zenodo at https://doi.org/10.5281/ 24. Yao, Z. et al. A taxonomy of transcriptomic cell types across the
zenodo.17781912 (ref. 44) with the MIT licence. isocortex and hippocampal formation. Cell 184, 3222–3241 (2021).
25. Traag, V. A., Waltman, L. & Van Eck, N. J. From Louvain to Leiden:
References guaranteeing well-connected communities. Sci. Rep. 9, 5233 (2019).
1. Paik, D. T. et al. Single-cell RNA sequencing in cardiovascular 26. Subramanian, A. et al. Gene set enrichment analysis: a
development, disease and medicine. Nat. Rev. Cardiol. 17, knowledge-based approach for interpreting genome-wide
457–473 (2020). expression profiles. Proc. Natl Acad. Sci. USA 102, 15545–15550
2. Zhang, Y. & Zhang, Z. The history and advances in cancer (2005).
immunotherapy: understanding the characteristics of 27. Lopez, R. et al. Deep generative modeling for single-cell
tumor-infiltrating immune cells and their therapeutic transcriptomics. Nat. Methods 15, 1053–1058 (2018).
implications. Cell. Mol. Immunol. 17, 807–821 (2020). 28. Hie, B. L. et al. Scanorama: integrating large and diverse
3. Li, X. et al. Deep learning enables accurate clustering with batch single-cell transcriptomic datasets. Nat. Protoc. 19, 2283–2297
effect removal in single-cell RNA-seq analysis. Nat. Commun. 11, (2024).
2338 (2020). 29. Roohani, Y., Huang, K. & Leskovec, J. Predicting transcriptional
4. Yang, F. et al. scBERT as a large-scale pretrained deep language outcomes of novel multigene perturbations with GEARS. Nat.
model for cell type annotation of single-cell RNA-seq data. Nat. Biotechnol. 42, 927–935 (2024).
Mach. Intell. 4, 852–866 (2022). 30. Ahlmann-Eltze, C., Huber, W. & Anders, S. Deep-learning-based
5. Theodoris, C. V. et al. Transfer learning enables predictions in gene perturbation effect prediction does not yet outperform
network biology. Nature 618, 616–624 (2023). simple linear baselines. Nat. Methods 22, 1657–1661 (2025).
6. Cui, H. et al. scGPT: toward building a foundation model for 31. Hong, L. et al. Fast, sensitive detection of protein homologs using
single-cell multi-omics using generative AI. Nat. Methods 21, deep dense retrieval. Nat. Biotechnol. 43, 983–995 (2025).
1470–1480 (2024). 32. Adduri, A. K. et al. Predicting cellular responses to perturbation
7. Hao, M. et al. Large-scale foundation model on single-cell across diverse contexts with State. Preprint at bioRxiv https://doi.
transcriptomics. Nat. Methods 21, 1481–1491 (2024). org/10.1101/2025.06.26.661135 (2025).
8. Heimberg, G. et al. A cell atlas foundation model for scalable 33. Lin, Z. et al. Evolutionary-scale prediction of atomic-level protein
search of similar human cells. Nature 638, 1085–1094 (2025). structure with a language model. Science 379, 1123–1130 (2023).
9. Yang, X. et al. GeneCompass: deciphering universal gene 34. Kirillov, A. et al. Segment anything. In Proc. IEEE/CVF International
regulatory mechanisms with a knowledge-informed Conference on Computer Vision 4015–4026 (IEEE, 2023).
cross-species foundation model. Cell Res. 34, 830–845 (2024). 35. Vaswani, A. et al. Attention is all you need. In Proc. Advances in
10. Fischer, F. et al. scTab: scaling cross-tissue single-cell annotation Neural Information Processing Systems, Vol. 30 (eds Guyon, I.
models. Nat. Commun. 15, 6611 (2024). et al.) (Curran Associates, 2017).
11. Ma, Q. et al. Harnessing the deep learning power of foundation 36. Kingma, D. P. & Ba, J. Adam: a method for stochastic optimization.
models in single-cell omics. Nat. Rev. Mol. Cell Biol. 25, 593–594 Preprint at https://doi.org/10.48550/arXiv.1412.6980 (2017).
(2024). 37. CZI Cell Science Program et al. CZ CELLxGENE Discover: a single-cell
12. Kedzierska, K. Z. et al. Zero-shot evaluation reveals limitations of data platform for scalable exploration, analysis and modeling of
single-cell foundation models. Genome Biol. 26, 101 (2025). aggregated data. Nucleic Acids Res. 53, D886–D900 (2024).
13. Boiarsky, R. et al. Deeper evaluation of a single-cell foundation 38. Franzén, O., Gan, L.-M. & Björkegren, J. L. M. PanglaoDB: a web
model. Nat. Mach. Intell. 6, 1443–1446 (2024). server for exploration of mouse and human single-cell RNA
14. Chen, H. et al. Quantized multi-task learning for context-specific sequencing data. Database 2019, baz046 (2019).
representations of gene network dynamics. Preprint at bioRxiv 39. Li, X. L. & Liang, P. Prefix-tuning: optimizing continuous
https://doi.org/10.1101/2024.08.16.608180 (2024). prompts for generation. Preprint at https://doi.org/10.48550/
15. Becht, E. et al. Dimensionality reduction for visualizing single-cell arXiv.2101.00190 (2021).
data using UMAP. Nat. Biotechnol. 37, 38–44 (2019). 40. Hu, E. J. et al. LoRA: Low-rank adaptation of large language
16. Aran, D. et al. Reference-based analysis of lung single-cell models. In The 10th International Conference on Learning
sequencing reveals a transitional profibrotic macrophage. Nat. Representations (ICLR, 2022).
Immunol. 20, 163–172 (2019). 41. O’Leary, N. A. et al. Exploring and retrieving sequence and
17. Hao, Y. et al. Dictionary learning for integrative, multimodal and metadata for species across the tree of life with NCBI datasets.
scalable single-cell analysis. Nat. Biotechnol. 42, 293–304 (2024). Sci. Data 11, 732 (2024).
18. Liu, B. et al. Temporal single-cell tracing reveals clonal revival and 42. Li, W. COVID-19 dataset. Figshare (2020).
expansion of precursor exhausted T cells during anti-PD-1 therapy 43. He, F. Processed datasets used in scPEFT study. Figshare
in lung cancer. Nat. Cancer 3, 108–112 (2022). https://doi.org/10.6084/M9.FIGSHARE.30763886 (2025).
19. Chang, H. et al. C/EBPδ drives interactions between human 44. He, F. Codebase for scPEFT: harnessing the power of single-cell
MAIT cells and endothelial cells that are important for large language models with parameter-efficient fine-tuning
extravasation. eLife 7, e32532 (2018). (v1.0.0). Zenodo https://doi.org/10.5281/zenodo.17781912 (2025).
Nature Machine Intelligence | Volume 8 | January 2026 | 118–133 132
