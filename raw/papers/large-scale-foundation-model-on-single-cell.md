---
source_path: /mnt/c/Users/Administrator/Zotero/storage/ZMJZTYIX/Hao 等 - 2024 - Large-scale foundation model on single-cell transcriptomics.pdf
ingested: 2026-04-23
sha256: 38787d5e62cc25da
---

nature methods
Article https://doi.org/10.1038/s41592-024-02305-7
Large-scale foundation model on single-cell
transcriptomics
Received: 2 June 2023 Minsheng Hao 1,2, Jing Gong2, Xin Zeng2, Chiming Liu 2, Yucheng Guo 2,
Xingyi Cheng2, Taifeng Wang 2, Jianzhu Ma 3,4 , Xuegong Zhang 1,5
Accepted: 10 May 2024
& Le Song 2,6
Published online: 6 June 2024
Check for updates Large pretrained models have become foundation models leading to
breakthroughs in natural language processing and related fields. Developing
foundation models for deciphering the ‘languages’ of cells and facilitating
biomedical research is promising yet challenging. Here we developed a
large pretrained model scFoundation, also named ‘xTrimoscFoundationα’,
with 100 million parameters covering about 20,000 genes, pretrained on
over 50 million human single-cell transcriptomic profiles. scFoundation
is a large-scale model in terms of the size of trainable parameters,
dimensionality of genes and volume of training data. Its asymmetric
transformer-like architecture and pretraining task design empower
effectively capturing complex context relations among genes in a variety of
cell types and states. Experiments showed its merit as a foundation model
that achieved state-of-the-art performances in a diverse array of single-cell
analysis tasks such as gene expression enhancement, tissue drug response
prediction, single-cell drug response classification, single-cell perturbation
prediction, cell type annotation and gene module inference.
Large-scale pretrained models are revolutionizing research in natu- gene–gene co-expression and interaction within cells. With the efforts
ral language processing related fields and becoming a new paradigm of the Human Cell Atlas (HCA)3 and many other studies4–8, the data scale
toward general artificial intelligence. These models trained on huge is exponentially growing9. With about 20,000 protein-coding genes
corpora become foundation models due to their fundamental roles across millions of cells, the observed gene expression values scale
in leading breakthroughs in many downstream tasks and their ability to a magnitude of trillion ‘tokens’ (Supplementary Table 1), which is
in discerning patterns and entity relationships within language1. In life comparable to the volume of natural language texts used to train large
sciences, living organisms have their underlying ‘languages’. Cells, the language models (LLMs) such as generative pretrained transformers.
basic structural and functional units of the human body, constitute This provides the foundation for us to pretrain a large-scale model to
‘sentences’ composed of a myriad of ‘words’ such as DNA, RNA, proteins extract complex, multifaceted internal patterns of cells in a manner
and gene expression values. An intriguing question is: Can we develop similar to LLMs learning human knowledge from huge archives of
foundation models of cells based on massive cell ‘sentences’? natural language texts.
Single-cell RNA sequencing (scRNA-seq) data, also known as In the LLM pretraining10,11, the growth in both model and data
single-cell transcriptomics, offer high-throughput observations into scale is critical for constructing foundation models that can effectively
cellular systems2, providing massive archives of transcriptomic sen- mine intricate multilevel internal relationships. Recently, progress has
tences of all types of cells for developing foundation models. In tran- been made in pretraining models on single-cell data12–15, but creating
scriptomic data, gene expression profiles depict complex systems of large-scale foundation models still presents unique challenges. First, the
1MOE Key Laboratory of Bioinformatics and Bioinformatics Division, BNRIST, Department of Automation, Tsinghua University, Beijing, China. 2BioMap,
Beijing, China. 3Department of Electrical Engineering, Tsinghua University, Beijing, China. 4Institute for AI Industry Research, Tsinghua University, Beijing,
China. 5School of Life Sciences and School of Medicine, Center for Synthetic and Systems Biology, Tsinghua University, Beijing, China. 6Mohamed bin
Zayed University of Artificial Intelligence, Abu Dhabi, UAE. e-mail: majianzhu@tsinghua.edu.cn; zhangxg@tsinghua.edu.cn; songle@biomap.com
Nature Methods | Volume 21 | August 2024 | 1481–1491 1481
Article https://doi.org/10.1038/s41592-024-02305-7
gene expression pretraining data need to encompass a landscape of cells respectively. We randomly masked both zero- and nonzero-expressed
across different statuses and types. Currently, most scRNA-seq data are genes in the input sample and recorded their index. Then the model
loosely organized, and a comprehensive and complete database is still took the masked input sample and two indicators to predict the expres-
lacking. Second, when modeling each cell as a sentence and each gene sion value of the raw sample at the masked index (Fig. 1b). This enabled
expression value as a word, the nearly 20,000 protein-coding genes the pretrained model not only to capture the gene–gene relationship
make the ‘sentence’ exceptionally long, a scenario that traditional trans- within the cell but also to harmonize the cell with different read depths.
formers struggle to handle16,17. Existing work often had to restrict their When used for inference, we feed the cell’s raw gene expression to the
models to a small list of selected genes. Third, scRNA-seq data across pretraining model and set the T higher than its total counts S to gener-
different techniques and laboratories exhibit high variance in sequenc- ate gene expression values with enhanced read-depth. We conducted
ing read depth. Unlike random noises due to technical effects such as several ablation experiments with cell clustering performance as an
contamination that would be reduced by training on large-volume data, evaluation to show the advantage of our model architecture and pre-
read depth is not random and its variation hinders models from learning training task design (Methods and Supplementary Note 1).
uniform and meaningful cell and gene representations. We constructed a comprehensive single-cell dataset by collecting
In this Article, we addressed these challenges and designed a data from all publicly available single-cell resources, including Gene
large-scale foundational model scFoundation of 100 million param- Expression Omnibus (GEO)22, Single Cell Portal, HCA3, human Ensemble
eters working on ~20,000 genes. We collected the scRNA-seq data- Cell Atlas (hECA)4, Deeply Integrated human Single-Cell Omics data
set with over 50 million gene expression profiles for pretraining. We (DISCO)7, European Molecular Biology Laboratory-European Bioinfor-
developed an asymmetric architecture for scRNA-seq data to acceler- matics Institute database (EMBL-EBI)8 and so on. We aligned all data to
ate the training process and improve model scalability. We designed a gene list composed of 19,264 protein-coding and common mitochon-
a read-depth-aware (RDA) modeling pretraining task that enables drial genes, as identified by the HUGO Gene Nomenclature Committee23.
scFoundation to not only model the gene co-expression patterns within After data quality control (Methods), we got over 50 million human
a cell but also link the cells with different read depths. scRNA-seq data for pretraining. The abundant data sources made the
To verify the ability of scFoundation, we conducted experiments on pretraining dataset rich in biological patterns. Anatomically, it spans
multiple downstream tasks, including cell clustering, drug response pre- over 100 tissue types across various diseases, tumors and normal states
diction on bulk data, single-cell drug response classification, single-cell (Fig. 1a), encompassing almost all known human cell types and states.
perturbation prediction and cell type annotation. Recognizing the After pretraining, we applied the scFoundation model to mul-
computational burden for users to fine-tune the large-scale models, tiple downstream tasks (Fig. 1c). The outputs of the scFoundation
we achieved advanced performance by adapting non-fine-tuned or encoder were pooled into cell-level embeddings, which were used for
light-fine-tuned scFoundation’s context embeddings to the correspond- cell-level tasks including clustering (within and across datasets), bulk
ing downstream models. We also showcased using gene embeddings and single-cell level drug response prediction and cell type annotation.
from scFoundation to infer the gene modules and gene regulation The outputs of the scFoundation decoder were gene-level context
networks. All results demonstrated the power and value of scFounda- embeddings, which were used for gene-level tasks such as perturbation
tion for transcriptomics data analyses and as foundation functions in prediction and gene module inference.
facilitating biology and medical task learning. The work explored and
pushed the boundaries of foundation models in the single-cell field. Scalable read-depth enhancement model without fine-tuning
In our study, we found a power-law decline in validation loss correlat-
Results ing with increased model size and computation, which is called ‘scal-
The scFoundation pretraining framework ing law’10,24 in LLMs. We trained three models with parameter sizes of
We developed scFoundation to model 19,264 genes with ~100 million 3, 10 and 100 million, respectively, and recorded their losses on the
parameters pretrained on over 50 million scRNA-seq data. This is a validation dataset. As the model parameters and the total number of
large-scale model of large parameter size, gene coverage and data scale floating-point operations (FLOPs) increased, the loss on the valida-
in the single-cell field. The ability to efficiently train such a model was tion dataset exhibited a power-law decline. We then estimated the
empowered by three key parts in our pretraining frameworks: model performance of various scale xTrimoGene architecture models with
design, pretraining tasks and data collection (Fig. 1a). parameter sizes equivalent to previous transformer-based models13–15,
We developed xTrimoGene, a scalable transformer-based model and compared with scVI25 (Supplementary Note 2). The scFoundation
with strategies for both algorithmic efficiency and engineering acceler- model with 100 million parameters surpassed all other models (Fig. 2a).
ation18. It included an embedding module and an asymmetric encoder– We further evaluated our three models on a cell-type annotation task
decoder structure. The embedding module converted continuous gene and observed the trend that the performance was improved as the
expression scalars into learnable high-dimensional vectors ensuring model size increased (Supplementary Table 2).
full retention of raw expression values, which was a notable improve- The RDA modeling enables scFoundation to enhance the read
ment over the discretized values used in previous models13,19. The depth of the input cell by setting T as a higher number than S. We
asymmetric encoder–decoder architecture had a similar form to the assessed this ability on independent test data of 10,000 cells ran-
masked autoencoder20 model in computer vision but was designed to domly sampled from the validation dataset. We downsampled the
accommodate the high sparsity of scRNA-seq data, achieving efficient total counts to 1%, 5%, 10% and 20% of the original profiles, generating
learning of all gene relationships without any selection. Moreover, we four corresponding datasets with varying total count fold changes. For
incorporated a variety of large-scale model training optimization tech- each dataset, we utilized non-fine-tuned scFoundation to enhance the
niques in the model deployment to ensure efficient training (Methods). cells with low total counts by setting the desired total counts T as the
We designed a pretraining task called the RDA modeling, an exten- reciprocal of the sampling rate. We measured the mean absolute error
sion of masked language modeling21, by considering the high variance (MAE), mean relative error (MRE) and Pearson correlation coefficient
of read depth in large-scale data. In RDA modeling, the model predicted (PCC) between predicted and actual nonzero gene expressions. As
the masked gene expression of a cell on the basis of its context genes. shown in Fig. 2b and Supplementary Fig. 1, scFoundation demonstrated
The context was from a duplication or a low-read-depth variant of that a notable reduction of half the MAE and MRE from the downsampled
cell’s gene expression profile (Methods). We treated the total count as data even when the downsampling rate was below 10%. These observa-
one cell’s read depth and defined two total counts indicators: T (‘target’) tions showed the ability of scFoundation to enhance gene expressions
and S (‘source’), for the total counts of the raw and the input samples, in scenarios even with extremely low total counts.
Nature Methods | Volume 21 | August 2024 | 1481–1491 1482
Article https://doi.org/10.1038/s41592-024-02305-7
a
Data collection Pretraining stage
Input M ··· ··· ··· M + T S
(~20,000)
M Mask
50 million single cells
Model
T Target total counts (~100 million Transformer blocks
parameters) S Input total counts
Bone Blood Nontumor
Brain P Predict value
ti 1 s 0 s 0 ue + s T n u o m nt o u r m an o d r Mixed Output P ··· ··· ··· P
Loss
Skin Tumor
Ground truth ··· ··· ···
Lung Normal
b
Bayesian
down sampling Mask
c
We then compared scFoundation with imputation methods it exhibited lower performance compared with smaller models like
including MAGIC26, SAVER27, scImpute28 and scVI25 on a human pan- SAVER. This phenomenon wherein the read depth is unaltered has also
creatic islet dataset processed by SAVER. This dataset contained been reported in a recent work29. As the T/S fold increased, we observed
manually generated downsampled gene expression profiles and their a quick jump in scFoundation’s performance that surpassed all other
corresponding reference data. For scFoundation, we obtained five methods. Its performance reached a plateau on higher T/S folds, indi-
sets of cell embeddings from the non-fine-tuned encoder by setting cating the cell embeddings were not sensitive to the value of T higher
T as the different folds of S ranging from 1 to 5. For other methods, we than 3.5S. We visualized the scFoundation embedding results at fold
first used the downsampled data to train the methods, and then got change 5 and results from other methods (Fig. 2d). Notably, scFounda-
imputed cell embeddings and gene expression from scVI and other tion’s cell embeddings exhibited more distinctive cluster boundaries
methods, respectively. The ground truth cluster labels were obtained compared with the baselines and other methods. Furthermore, we
from the reference data (Methods). For evaluating clustering accu- clustered the results of all methods and applied the cluster labels back
racy, we employed metrics including normalized mutual information onto the reference Uniform Manifold Approximation and Projection
(NMI), adjusted Rand index (ARI) and silhouette coefficient (SIL) (Sup- (UMAP). Other methods showed mixed labels, especially for cluster 0
plementary Note 3). The clustering performance obtained from the in the ground truth. scFoundation was the only method that aligned
downsampled data was used as the baseline. all cell cluster assignments consistently with the reference results.
scFoundation outperformed both the baseline and scImpute We then applied scFoundation to the Zheng68K dataset30, com-
in all metrics when T was set equal to S (fold change of 1; Fig. 2c) but prising about 60,000 human peripheral blood mononuclear cells
Nature Methods | Volume 21 | August 2024 | 1481–1491 1483
redocnE
redoceD PLM
Reconstruction loss
T S
gnilooP
Model
0
0 ···
0 ···
Cell embedding
Clustering Drug response prediction Perturbation prediction
Resistant/sensitive
IC50
gniddebmE eludom
GEO, HCA, EMBL-EBI, hECA, DISCO, ...
Organ: heart, liver, kidney, lung, brain, ...
0 0 Zero ····· ·· · ·
0 Mask ··· ··· ····· ·· · · ··· ···
0 0
Nonzero ····· · ···· · ·
··· ···
T
S
···
Annotation Gene module inference
···
···
Fig. 1 | The schematic overview of the pretraining framework. a, Fifty embeddings corresponding to nonzero and nonmasked values (including T and S)
million single-cell gene expression profiles were collected, covering tumor and are fed into the model encoder. The output embeddings of the encoder are then
nontumor cells from various tissues. These data were used for the RDA modeling combined with mask and zero embeddings and fed into the decoder. Also, the
task to pretrain the model. In the RDA task, the input consists of the masked gene encoder output can be pooled to generate a cell embedding for downstream
expression vector and two total count indicators (T and S). The output is the usage. The decoder output embeddings are projected to the gene expression
predicted expression value for all genes, and the loss is computed at the masked value via a shared MLP layer. The regression loss between the predicted and raw
positions. b, Outline of the pretraining process. A raw gene expression vector sample’s gene expression values is computed. c, The pretraining embeddings
serves as a training sample. A hierarchical Bayesian downsampling strategy can be leveraged as substitutes for the gene expression profiles, facilitating
generates the input sample. The gene expression total counts (T and S) of the downstream tasks such as cell clustering, drug response prediction, single-cell
raw and input samples are computed. Values in the input sample are randomly level perturbation prediction, cell-type annotation, gene module inference
masked. The scalar expression values are converted into embeddings. Only and so on.
Article https://doi.org/10.1038/s41592-024-02305-7
c
scFoundation Downsample MAGIC SAVER scImpute scVI
d
Reference
e f
Raw scFoundation
0.8
0.6
0.4
0.2
0
NMI ARI SIL
B cell CD4 T helper cell CD14 monocyte CD56 NK cell CD34 cell Regulatory T cell
Cytotoxic T cell Memory T cell Naive cytotoxic T cell Naive T cell
sequenced on an early 10x Chromium platform. Each cell had about was used without fine-tuning to enhance cell embeddings by setting
500 expressed genes and fewer than 2,000 total reads, making cell the T value as 10,000. The resulting UMAP plots showed that scFoun-
type distinction challenging13,31 (Supplementary Fig. 2). scFoundation dation effectively separated memory T cells from other T cells and
Nature Methods | Volume 21 | August 2024 | 1481–1491 1484
eulaV
Downsample SAVER scImpute scVI scFoundation
UMAP1
scFoundation
scVI
Raw
2PAMU
0.8
0.7
0.6
0.5
1 2 3 4 5
Fold
Annotation mapping
Cluster 0 Cluster 1 Cluster 2
Cluster 3 Cluster 4 Cluster 5
Cluster 6
IMN
0.8
0.6
0.4
1 2 3 4 5
Fold
IRA
0.15
0.10
0.05
1 2 3 4 5
Fold
LIS
UMAP1
2PAMU
UMAP1
2PAMU
1.0
0.8
0.6
0.4
0.2
0
P = 0.01 P = 0.05 P = 0.1 P = 0.2 P = 0.01 P = 0.05 P = 0.1 P = 0.2
Downsampling rate Downsampling rate
ERM
oreznoN CCP
a b
scFoundation Downsampled data
0.50 0.7
0.6
0.45
0.5
0.40 0.4
0.3
0.35 0.2
0.1
0.30 0
17 18 19 20
log (FLOPs)
10
tes
dilav
no
ssol
ESM
3M 10M 100M
y = –0.014x + 0.611
scBERT
Geneformer
scGPT
scFoundation
Fig. 2 | Performance of read-depth enhanced clustering results. a, Training counts, and the y axis represents the score. d, UMAP plots of cell embeddings
loss under different parameter sizes and FLOPs. The dots noted as other models’ generated by different methods. The left plot shows the reference UMAP plot
names were the performance of various scale xTrimoGene architecture models obtained using raw gene expression, with colors indicating cell clusters. The
with parameter sizes equivalent to other models. The scVI model achieved an upper-right plots display clustering results obtained by different methods:
MSE of 0.98. Since it was not a transformer-based model and not applicable to downsample (no imputation), SAVER, scImpute, scVI and scFoundation. The
plot on the figure. b, Evaluation of read-depth enhancement performance on numbers of clusters are aligned. The lower-right plots depict the clustering
the unseen dataset. MREs of nonzero genes and PCCs of all genes were used to results of each method mapped onto the reference UMAP plot. e, UMAP plot
evaluate the recovered gene expression performance. Lower MREs and higher comparing raw gene expression and scFoundation-imputed cell embeddings
PCCs indicate better performance. c, Comparison of the scFoundation model on the Zheng68K dataset. f, Comparison of clustering performance among
with other imputation methods based on cell clustering metrics. The x axis scFoundation, scVI and raw data on the Zheng68K dataset.
represents the fold change between the desired total counts and the input total
Article https://doi.org/10.1038/s41592-024-02305-7
distinguished CD14 monocytes and CD34 cells better (Fig. 2e). We (GSEA)40 on the new predictions with relatively low IC , which indicated
50
compared our results with scVI trained on the same dataset. Both that the cell line is sensitive to the drug (Fig. 3e). For instance, the
methods outperformed the raw data in clustering. While their NMI and sphingolipid signaling pathway was enriched in doxorubicin-sensitive
ARI metrics were similar, scFoundation had a higher SIL score, showing cell lines. According to the Kyoto Encyclopedia of Genes and Genome
its generalization ability in non-fine-tuning mode (Fig. 2f). database41, this pathway was related to sphingomyelin and its metabo-
scFoundation also showcased its capability to facilitate read depth lism. Sphingomyelin was reported to interact synergistically with
enhanced clustering across different batches. Note that merely align- doxorubicin by altering cell membrane permeability resulting in a
ing the read depth would not eliminate the entire batch effect since lower IC of the drug in these cell lines42. The mTOR signaling pathway
50
batch effects can involve other variations such as donor gender, experi- was enriched in vorinostat-sensitive cell lines. Previous studies have
ment treatment, cell cycle and so on32. We mapped single-cell data from shown that vorinostat inhibits carcinoma growth by dampening the
different batches together by feeding the read-depth-enhanced cell mTOR signaling pathway43. Other clinical studies have also shown that
embeddings into a nontrainable downstream header BBKNN33. Results mTOR inhibitors were often used in conjunction with vorinostat44,45,
on simulated data and on data collected from organoid and in vivo experi- suggesting a relationship between vorinostat and the mTOR pathway.
ments showed that scFoundation can achieve better cell mapping while These examples supported the validity of our predictions.
slightly reducing the dispersion of different cell types (Supplementary Although scFoundation was pretrained on single-cell transcrip-
Table 3 and Supplementary Figs. 3 and 4; details in Supplementary Note 4). tomics data, the learned gene relationships were transferable to
These results demonstrated that scFoundation possessed the bulk-level expression data to produce condensed embeddings, facili-
capability to enhance the read-depth of cells. Notably, an important tating more accurate IC prediction. These findings illustrated the
50
distinction between scFoundation and other imputation methods potential of scFoundation in expanding the understanding of drug
was that scFoundation could achieve the best performance without responses in cancer biology and possibly guiding the design of more
the need for dataset-specific fine-tuning. effective anticancer treatments.
Improving cancer drug response prediction Transferring bulk drug response to single cells
Cancer drug responses (CDRs) study tumor cells’ responses upon drug Inference of drug sensitivities at the single-cell level can help identify
intervention. Computationally predicting CDR is critical to guiding specific cell subtypes that exhibit different drug resistance charac-
anticancer drug design and understanding cancer biology34. We com- teristics, offering valuable insights into underlying mechanisms and
bined scFoundation with the CDR prediction method DeepCDR35 to potential new therapies46. We applied scFoundation to the crucial task
predict the half-maximal inhibitory concentration IC values of drugs of single-cell-level drug response classification based on a downstream
50
across several cell line data. This experiment served as a validation of model called SCAD47. Due to the limited single-cell drug response data,
whether scFoundation could provide informative embeddings for SCAD used domain adaption to eliminate the single-cell and bulk dif-
bulk-level gene expression data, despite being trained on single cells. ferences, and transferred knowledge learned on bulk data to infer the
The original DeepCDR model used drug structural information drug sensitivity of single cells. The process took both bulk and single-
and multiomics data as input and outputted the predicted IC . Here, we cell data as input and output predicted the sensitivity for each cell. In
50
focused on gene expression data and replaced the transcriptome mul- our setting, we used non-fine-tuned scFoundation to obtain unified
tilayer perceptron (MLP) subnetwork in DeepCDR with scFoundation embeddings of bulk and single-cell data, and used these embeddings
(Fig. 3a). We used the Cancer Cell Line Encyclopedia36 and Genomics to train SCAD models (Fig. 4a).
of Cancer Drug Sensitivity37 datasets to obtain the input cell line gene We focused on the four drugs (sorafenib, NVP-TAE684, PLX4720
expression data, the input drugs and IC labels (Methods). and etoposide) that exhibited lower area under the receiver operating
50
We evaluated the performance of scFoundation-based results with characteristic curve (AUC) values in the original study. These drugs
gene expression-based results across multiple drugs and cancer cell had drug-sensitive labels of bulk data in the Genomics of Cancer Drug
lines (Fig. 3b). Most drugs and all cancer types achieved a higher PCC Sensitivity37 database, and the true cell-level drug-sensitive labels were
by using scFoundation embeddings. We visualized the best prediction obtained in different ways. For drug PLX4720 and etoposide-affected
case of drug and cancer types (Fig. 3c). Regardless of high or low lC , the single cells, cells from untreated cell lines were considered sensi-
50
scFoundation-based DeepCDR model could predict accurate values and tive, while cells that survived after drug exposure were considered
achieved a PCC above 0.93. In a drug-blind test that left out one drug at resis tant48. For drug sorafenib and NVP-TAE684-affected cells, the cells’
a time from the dataset, scFoundation-based models consistently out- sensitive labels were determined by the value of senescence-related
performed the original model (Fig. 3d). The top 1 PCC-gaining drug PHA- (EpiSen) program scores that were proven to have a relation with drug
793887, a potent ATP-competitive CDK inhibitor, improved the PCC from responses previously49 (Methods).
0.07 to 0.73. Even for the 200th-ranked drug zobotentan used for block- We compared the scFoundation-based model with the base-
ing endothelin A receptor activity, its PCC improved from 0.49 to 0.64. line SCAD model that took all genes’ expression values as input. The
We further grouped drugs into different therapy types to examine scFoundation-based model achieved higher AUC values for all drugs,
whether the IC prediction performance was related to their intrin- with notable improvements for NVP-TAE684 and sorafenib, exceeding
50
sic mechanisms. Based on scFoundation-predicted results, drugs a 0.2 increase in AUC. Baseline results for all four drugs were at best
belonging to chemotherapy such as antitumor antibiotics and topoi- 0.66, with one result even worse than random, highlighting the task’s
somerase inhibitors tend to have higher PCC than drugs belonging difficulty (Fig. 4b). We used the Spearman correlation to assess the
to targeted therapy such as ataxia telangiectasia mutated (ATM) and relationship between predicted drug sensitivity and EpiSen scores.
poly(ADP-ribose) polymerase (PARP) inhibitors (Fig. 3d). This may For NVP-TAE684 and sorafenib, there should be a positive and nega-
be due to the fact that specific gene mutations often have important tive correlation with EpiSen scores, respectively. The scFoundation
impacts on targeted therapy34 but such information is hardly revealed in model showed Spearman correlations of 0.56 and −0.55 for these drugs,
gene expression data, while chemotherapy drugs were widely reported while the baseline model achieved only 0.24 and −0.06 (Fig. 4c), indicat-
to be related to gene expression38,39 so their IC is easier to predict. As for ing that using scFoundation embeddings had the potential to capture
50
the gene expression-based results, they had an overall lower PCC, and the signal of drug sensitivity biomarkers. These results further moti-
we did not observe a performance difference between therapy types. vated us to investigate whether the embeddings were more informative
Then we used our model to predict unknown CDR in the data. To than gene expression without the necessity for extracting the signal.
validate these predictions, we performed a gene set enrichment analysis We conducted principal component analysis (PCA) on embeddings
Nature Methods | Volume 21 | August 2024 | 1481–1491 1485
Article https://doi.org/10.1038/s41592-024-02305-7
a
b c
All cancer types Low-grade gliomas
1.00
Pearson: 0.93 5.0 0.95 4 Spearman: 0.87
0.90 2 N = 73 4.5
4.0 0.85 0
3.5
0.80 −2
0.75 −4 3.0
0.70 2.5
−6
0.70 0.75 0.80 0.85 0.90 0.95 1.00 −5.0 −2.5 0 2.5 5.0 2.5 3.0 3.5 4.0 4.5 5.0
Baseline PCC Observed lnIC 50
d
Drug blind test e
of single-cell dataset SSC47 and visualized the first two principal com- interactions across different cell types and potential drug targets50.
ponents. Results showed less linear correlation compared with raw Using Perturb-seq51,52 data resources to train models for modeling cellu-
data PCA, suggesting richer information captured by the embeddings lar response to perturbations is a key task of computational biology53–55.
(Fig. 4d). Furthermore, we computed the clustering performance based We combined the scFoundation with an advanced model called GEARS53
on the embeddings and gene expression of both bulk and single-cell for predicting the single-cell-resolution perturbation. The original
data, using drug sensitivity as the label. The results of higher Calinski– GEARS model used a Gene Ontology knowledge graph to represent
Harabasz (CH) and SIL scores (Fig. 4e and Supplementary Fig. 5) demon- unseen gene perturbations by learning from a combination of previ-
strated that the scFoundation better-grouped cells or bulk cell lines with ously observed gene perturbation nodes, and a gene co-expression
the same drug response, compared with the gene expression baseline. graph combined with perturbation information to predict the
These findings highlighted that the unified embedding obtained post-perturbation gene expression. Each node in the co-expression
from scFoundation aligned bulk and single-cell data into a unified graph represented a gene with initially randomized embeddings, and
representation space. This condensed representation produced a clear edges connected to co-expressed genes. This graph was shared across
distinction between data with sensitive and resistant states, facilitating all cells. In our method, we obtained gene context embeddings for
the downstream model to better transfer pharmacogenomics informa- each cell from the scFoundation decoder and set these embeddings
tion from bulk cell lines to single-cell data. as the nodes in the graph (Methods), resulting in a cell-specific gene
co-expression graph for predicting perturbations (Fig. 5a).
Facilitating perturbation response prediction We trained and tested models on three perturbation datasets
Understanding cellular responses to perturbations is crucial for bio- following the original study (Supplementary Note 5). Since there was
medical applications and drug design, as it helps identify gene–gene no single-cell-level ground truth in the perturbed data, we computed
Nature Methods | Volume 21 | August 2024 | 1481–1491 1486
CInl
detciderP
05
WZ-1-84
Pearson: 0.94 Spearman: 0.95
N = 8
0.6 0.5 0.4 0.3
0.2 0.1 0
0 50 100 150 200
niag nosraeP CCP
1.00
0.75
0.50
0.25
0
−0.25
−0.50
−0.50 −0.25 0 0.25 0.50 0.75 1.00
CCP
noitadnuoFcs
All drugs
WZ-1-84
LGG
0.8
Top 1: PHA-793887 0.6 0.4 0.2 0 Top 100: PD173074
Top 200: zibotentan
tnemhcirnE erocs NES: 1.707 P value: 1.894 × 10−3 FDR: 1.408 × 10−1
4.0 2.0 0
–2.0
Antitu
T
m
o
o
p
r
o
a
is
n
o
t m
ib
e
io
r
t
a
ic
se
s inhib
A
it
T
o
M
rs inhib
PA
it
R
o
P
rs inhibitors –4.0 0 100 200 300 400 500 600
tsil deknaR cirtem
tnemhcirnE
tsil deknaR
erocs
cirtem
Graph neural
Drug network
IC
50
Bulk data scFoundation
Sphingolipid signaling mTOR signaling
1.0 0.5 NES: 1.776 P value: 5.941 × 10−3 FDR: 1.384 × 10−1 0
Sensitive 4.0 Sensitive 2.0 Zero score at 446 0 Zero score at 318
Resistant –2.0 Resistant 0 100 200 300 400 500 600
Rank Rank
···
Drug embedding
···
Bulk embedding
0.65 Etoposide 0.60 Gemcitabine CP466722 Methotrexate 0.55 Olaparib
0.50 SN-38 Veliparib 0.45 KU-55933 0.40 Talazoparib
Fig. 3 | Drug response prediction using scFoundation embeddings. represents a drug, with the y axis indicating the PCC between predicted and
a, Illustration of the scFoundation-based CDR prediction model. b, PCC between ground truth IC and the x axis representing four drug types. The first two
50
all drugs and cancer types in the test set. Each dot represents a drug or cancer belong to chemotherapy and the last two belong to targeted therapy. The dashed
type, with the x axis and y axis showing PCCs obtained by the baseline CDR model line showed the mean PCC within each therapy type. e, GSEA results on cell-line
and scFoundation-based model, respectively. c, Comparison of predicted and data with lower predicted IC values. The Sphingolipid signaling pathway was
50
observed IC values for the drug WZ-1-84 on the cancer-type low-grade gliomas. enriched in doxorubicin-sensitive cell lines, while the mTOR signaling pathway
50
Each dot represents a drug and cell-line combination. d, Leave-one-drug-out was enriched in vorinostat-sensitive cell lines. The P value is one-sided and
blind test performance. The Pearson gain plot shows the PCC gain obtained calculated from the standard GSEA permutation test. For the false discovery rate
by replacing gene expression with embeddings. Each dot represents a drug, (FDR) value, adjustments were made for multiple comparisons. NES, normalized
with the y axis indicating the gained PCC values and the x axis representing the enrichment score.
rank. Higher-ranked drugs have a higher PCC gain. In the PCC plot, each dot
Article https://doi.org/10.1038/s41592-024-02305-7
0.04
0.03
0.02
0.01
0
−0.01
Sorafenib Etoposide
PL
X472 0
the averaged mean square error (MSE) of the top 20 differentially perturbations in test set, and we found that the scFoundation-based
expressed (DE) genes between pre- and post-gene expression profiles model achieved a higher PCC compared with the baseline (Fig. 5e).
for evaluation. The scFoundation-based model achieved lower MSE Then, we ranked two-gene perturbations by predicted magnitude
values compared with the original GEARS baseline model. On the more scores, considering the top 20 as potential synergy and the bot-
challenging two-gene perturbations predictions, the model achieved tom 20 as suppressor GIs. The Venn plot in Fig. 5f revealed that the
the lowest averaged MSE in the 0/2 unseen case and outperformed scFoundation-based model identified a higher number of true pertur-
GEARS and another baseline called CPA56 model across all cases (Fig. 5b bations for both synergy and suppressor types.
and Supplementary Fig. 6). For each two-gene perturbation in the test These results highlighted that the cell-specific gene context
set, we further examined the proportion of the top 20 DE genes with embeddings obtained from scFoundation served as valuable foun-
mean predicted values falling in the 45–55% quantile of the true expres- dational representations for perturbation prediction. The analysis of
sion distribution interval. The scFoundation-based model exhibited two-gene perturbations underscored the model’s capability to accu-
a higher percentage compared with the baseline (Fig. 5c), indicating rately classify different types of GI.
it predicted a more reasonable distribution of post-gene expression
values. Figure 5d showcased the top 20 genes’ expression changes of Annotating cell types
two-gene perturbation ETS2 + CEBPE. Cell type annotation is crucial in single-cell studies, and various meth-
One application for predicting two-gene perturbations was to ods have been developed for this purpose. To assess the performance
classify two-gene perturbation into different genetic interaction (GI) of scFoundation, we conducted experiments using the Zheng68K
types. We identified synergy and suppressor GI types by using the mag- dataset30 and the Segerstolpe dataset57 that were shown to be chal-
nitude score (Methods). We first computed the PCC of magnitude score lenging in the previous study13. We fine-tuned only a single layer of the
between predicted and ground truth magnitude scores of all two-gene scFoundation encoder and added an MLP head for predicting labels.
Nature Methods | Volume 21 | August 2024 | 1481–1491 1487
erocs
LIS
12
10
8
6
4
2
0
erocs
HC
a
b
PLX4720 Etoposide
AUC 0.5 scFoundation Baseline
c d e
NVP-TAE684 Sorafenib scFoundation scFoundation Baseline
Resistant Sensitive Resistant Sensitive
PC1
Raw
0 0.2 0.4 0.6 0.8 1.0
Normalized EpiSen score
2CP
PC1
2CP
Bulk data
scFoundation
···
Single-cell data
···
0/1
label
Bulk embedding
Model transfer
0/1
response
Single-cell
embedding
scFoundation AUC: 0.84 scFoundation AUC: 0.84 scFoundation AUC: 0.66 scFoundation AUC: 0.68
0 0.2 0.4 0.6 0.8 1.0
25
20
15
10
5
0
0 5 10 15 20 25
25
20
15
10
5
0
noitadnuoFcs
enilesaB
knar
ytilibaborp
knar
ytilibaborp
noitadnuoFcs
enilesaB
knar
ytilibaborp
knar
ytilibaborp
NVP-TAE684 Sorafenib
0 0.2 0.4 0.6 0.8 1.0 0 0.2 0.4 0.6 0.8 1.0 0 0.2 0.4 0.6 0.8 1.0
False positive rate False positive rate False positive rate False positive rate
25
20
15
10
5
Spearman: 0.56 0 Spearman: –0.55
0 5 10 15 20 25
25
20
15
10
5
Spearman: 0.24 0 Spearman: –0.06
0 5 10 15 20 25 0 5 10 15 20 25
EpiSen rank EpiSen rank
etar
evitisop
eurT
1.0
0.8
0.6
0.4
0.2
0
etar
evitisop
eurT
1.0
0.8
0.6
0.4
0.2
0
etar
evitisop
eurT
1.0
0.8
0.6
0.4
0.2
0
etar
evitisop
eurT
1.0
0.8
0.6
0.4
0.2
Baseline AUC: 0.62 Baseline AUC: 0.56 Baseline AUC: 0.38 0 Baseline AUC: 0.66
Fig. 4 | Single-cell drug response classification tasks based on scFoundation probability and normalized EpiSen score. Each row corresponds to a model,
cell embeddings. a, Illustration of the scFoundation-based single-cell response and each column represents a drug. d, PCA plots of cells in the SSC47 single-cell
classification model. b, Receiver operating characteristic (ROC) curves for the dataset drawn with scFoundation embeddings and with raw data. Color denotes
four drugs. The red and blue lines represent the performance of the scFoundation- the reference EpiSen score. Cells with different EpiSen scores exhibit distinct
based model and the baseline SCAD model, respectively. AUC, area under the responses to drugs. e, The clustering performance on all three drug-related bulk
receiver operating characteristic curve. c, The correlation between drug-sensitivity datasets. Each bulk dataset has two types of label: sensitive and resistant.
Article https://doi.org/10.1038/s41592-024-02305-7
a
b
0.15
0.10
0.05
0
1
unseen
1
unseen
d
e f
We benchmarked scFoundation against the methods CellTypist58, from improvements in rare cell types such as CD4+ T helper 2 and
scBERT13, scANVI59, ACTINN60, Scanpy61 and SingleCellNet62 (Methods). CD34+ (Supplementary Table 5). We visualized scFoundation and Cell-
Supplementary Table 4 shows that scFoundation achieved the highest Typist predictions on the UMAP obtained from latent embeddings and
macro F1 score on both datasets. Compared with the second-place PCA components, respectively. Supplementary Figs. 7 and 8 showed
method CellTypist, the higher performance of scFoundation came that scFoundation had clear separations between different cell types.
Nature Methods | Volume 21 | August 2024 | 1481–1491 1488
ESM
c
scFoundation Baseline
10%
0.2 8%
scFoundation 6%
Baseline 0.1 4%
2%
0 0%
0/2
unseen
1/2
unseen
2/2
unseen
1
unseen
1
unseen
0/2
unseen
1/2
unseen
2/2
unseen
Dixit et al. Norman et al. Dixit et al. Norman et al.
lavretni
55–54
ni
tnecreP
ED
02
pot
fo
10%
8%
5%
2%
0%
3
2
1
0
−1
−2
AIF1 HBG2
T
MSB4X LST1 HBG1 HBZ CTSL CEBPE
T
MSB10
G
MFG GYPA UBAC1 ACT
S
B H3BGRL3 GYPB
LI
MD2
IFIT
M2 GAL ARHGDIB
GPS
M3
lortnoc
revo
atleD
ETS2 + CEBPE
scFoundation
Baseline
GT
2.0
1.5
1.0
0.5
0
0 0.5 1.0 1.5 2.0
Ground truth
enilesaB
2.0
1.5
1.0
0.5
0
0 0.5 1.0 1.5 2.0
Ground truth
noitadnuoFcs
···
··· scFoundation ··· ··· ··· ···
···
Cell-specific gene Perturbed
Unperturbed gene expression Gene context embeddings co-expression graph Perturbation gene expression
Magnitude Synergy Suppressor
scFoundation Baseline scFoundation Baseline
9 3 12 4 12 5
3
5 2 3
1
0
Pearson: 0.18 Pearson: 0.01
10 6
Ground truth Ground truth
Fig. 5 | Perturbation prediction tasks using scFoundation gene context truth post-gene distribution. For each gene, n = 313 cells were examined. The
embeddings. a, An illustration of the perturbation prediction model based on two edges of a box and horizontal bars inside a box indicate the interquartile and
cell-specific gene embeddings of scFoundation. b, MSE between predicted and median of all values, respectively. The length of the whiskers extends to 1.5 times
ground truth post-gene expressions. Results given by the scFoundation-based the interquartile range (IQR) from the quartiles. e, Magnitude scores computed
GEARS model and baseline GEARS model are shown in red and blue, respectively. for all test perturbing combinations on the Norman dataset. Each dot represents
c, The average proportion of predicted values of the top 20 DE genes falling a specific perturbing combination. The y axis shows the magnitude score
within 45–55% quantile of the corresponding true expression distribution computed from the prediction results, while the x axis represents the ground
interval. The dashed black lines represent the expected percentage (10%). truth magnitude score computed using real post-gene expression.
d, The predicted gene expression over control for the top 20 most DE genes f, Top 20 perturbations with synergistic and suppressor gene interaction types
after a combinatorial perturbation (ETS2 + CEBPE). The red and blue boxes identified using scFoundation and baseline methods. The Venn plot illustrates
indicate gene prediction results by the scFoundation-based GEARS model and the relationship between the identified perturbation set and the verified
the baseline GEARS model, respectively. The green boxes represent the ground perturbation set.
Article https://doi.org/10.1038/s41592-024-02305-7
These results indicated that scFoundation’s ability to utilize the expression values because the current data used as pretraining labels
entire gene set as input could lead to more accurate annotations, com- suffered from a high dropout rate and the model pretraining loss was
pared with other methods that unavoidably lose information by using not optimized to zero.
a gene subset or discretized gene expression. scFoundation still faces some limitations. Although the pretrain-
ing data contained virtually all human scRNA-seq data publicly avail-
Inferring gene modules and gene regulation networks able at the time of our curation, they may still not be sufficient to fully
One advantage of scFoundation is that it extends gene expression values reflect the complexity of human organ development and health states.
into context embeddings, compared with other architectures such as the The pretraining demands substantial computational resources, requir-
vanilla MLP model (Supplementary Note 6). These embeddings could ing further optimization for efficiency. The current model focused on
not only facilitate graph-based downstream methods such as GEARS, transcriptomic data only, and did not include genomic or epigenomic
but also be used to infer gene–gene networks. Here, we used the gene data. Also, its unsupervised pretraining process had the advantage of
embeddings from three immune cell types (monocytes, cytotoxic not relying on human annotation of the massive data but overlooked
CD8+ T cells and B cells) for validation and exploration of this usage the rich information in metadata. Including cells’ metadata with
(Methods). transcriptomic data in the model may have the potential to link cells’
We clustered genes into modules based on their embeddings’ molecular features with phenotypes.
similarity. Results showed that scFoundation could identify the differ- In the future, we will pretrain models with more parameters and
ential expressed gene modules of each cell type (Supplementary Figs. 9 larger datasets using our effective pretraining framework, and we
and 10). Gene enrichment analysis validated that the identified gene believe several works could be developed on the basis of the insights
modules were enriched in their respective cell types (Supplementary from scFoundation. For instance, designing more effective pretrain-
Fig. 11), indicating that the gene embeddings have learned functional ing tasks could potentially improve the model’s performance29. The
relations among genes. Further, we explored the gene network con- effect of various dataset characteristics on training performance
structed within the top 1 DE gene module of T cells (Supplementary also remains to be explored29. Furthermore, the emerging field of
Fig. 12). Genes CD8A and CD8B encoding chains of the CD8 molecule single-cell multiomics data67,68 presents opportunities for develop-
exhibited strong similarities, while the S100A8 gene showed limited ing models that can delineate multilevel complex laws of cells. One
correlation with other T cell markers as expected. This suggested doable case can be to predict gene expression values based on assay
that the embeddings could provide insights into gene relations within for transposase-accessible chromatin with sequencing (ATAC-seq)
modules. Additionally, we conducted experiments on gene regula- context and vice versa (Supplementary Note 7).
tory network (GRN) inference with the downstream model SCENIC63 The general applicability of scFoundation shown in the variety of
(Methods). We identified cell-specific regulators such as KLF6, SPIB and tasks indicates that it has succeeded in learning underlying relations
MXD4, which were confirmed by the previous work as the regulators among genes in their expressions in different types of cell. We expect
for monocyte64, B cell65 and CD8+ T cell66, respectively (Supplementary that the pretraining architecture and the pretrained scFoundation
Fig. 13). These examples underscored the potential of scFoundation model can serve as fundamental contributions supporting both stud-
gene embeddings for inferring GRNs. ies on large biological models and a variety of downstream research.
This work as well as other recent reports suggest that large biological
Discussion models pretrained on high-throughput single-cell data are opening a
Recent breakthroughs in LLMs motivated us to explore whether new route to deciphering and modeling complex molecular systems.
large-scale models can also be effective for learning the cellular and
molecular ‘languages’ of biology from single-cell transcriptomic data, Online content
which exhibit large data scales, complex biological patterns, diversity Any methods, additional references, Nature Portfolio reporting sum-
and technical noises. Combining the xTrimoGene architecture with maries, source data, extended data, supplementary information,
the RDA pretraining task, we developed scFoundation, a large-scale acknowledgements, peer review information; details of author contri-
foundation model with 100 million parameters pretrained on over butions and competing interests; and statements of data and code avail-
50 million single-cell data. Ablation experiments and applications on ability are available at https://doi.org/10.1038/s41592-024-02305-7.
downstream tasks showed the advantage of its design of the pretraining
task and the model. Supplementary Table 1 provides a comparison of References
the major features with the released similar models. 1. Srivastava, A. et al. Beyond the imitation game: quantifying and
scFoundation was pretrained as a general-purpose foundation extrapolating the capabilities of language models. Preprint at
model for many downstream tasks: it achieved superior performance arXiv https://doi.org/10.48550/arXiv.2206.04615 (2023).
in read-depth enhancement, drug response prediction, single-cell drug 2. Jovic, D. et al. Single-cell RNA sequencing technologies and
sensitivity prediction, perturbation predictions and cell type annota- applications: a brief overview. Clin. Transl. Med. 12, e694 (2022).
tion tasks. It also showed high potential in gene module inference and 3. Regev, A. et al. The Human Cell Atlas. eLife 6, e27041 (2017).
in better facilitating cell mapping by cooperating with downstream 4. Chen, S. et al. hECA: the cell-centric assembly of a cell atlas.
batch removal headers like BBKNN33. iScience 25, 104318 (2022).
The scFoundation model does not need further fine-tuning on 5. Snyder, M. P. et al. The human body at cellular resolution: the NIH
most tasks. This design reduced computational and time costs for Human Biomolecular Atlas Program. Nature 574, 187–192 (2019).
users and offered flexibility in downstream model design, allowing 6. The Tabula Sapiens Consortium. The Tabula Sapiens: a
scFoundation to better serve as a foundational model for a variety of multiple-organ, single-cell transcriptomic atlas of humans.
downstream tasks in the field of single-cell biology. Science 376, eabl4896 (2022).
We recommend using scFoundation to extract embeddings from 7. Li, M. et al. DISCO: a database of deeply integrated human
datasets without explicit batch-effect or modality differences. Given single-cell omics data. Nucleic Acids Res. 50, D596–D602 (2022).
that batch effects or modality differences may encompass a range of 8. Papatheodorou, I. et al. Expression Atlas update: from tissues to
variations, we took the strategy in scFoundation to consider only read single cells. Nucleic Acids Res. 48, D77–D83 (2020).
depth and leave other possible differences to cooperative methods 9. Svensson, V., Vento-Tormo, R. & Teichmann, S. A. Exponential
on downstream tasks, such as BBKNN and SCAD. Furthermore, we scaling of single-cell RNA-seq in the past decade. Nat. Protoc. 13,
suggest using cell and gene embeddings instead of the predicted gene 599–604 (2018).
Nature Methods | Volume 21 | August 2024 | 1481–1491 1489
Article https://doi.org/10.1038/s41592-024-02305-7
10. Brown, T. B. et al. Language models are few-shot learners. Adv. 35. Liu, Q., Hu, Z., Jiang, R. & Zhou, M. DeepCDR: a hybrid graph
Neural Inf. Process. Syst. 33, 1877–1901 (2020). convolutional network for predicting cancer drug response.
11. Zhao, W. X. et al. A survey of large language models. Preprint at Bioinformatics 36, i911–i918 (2020).
arXiv https://doi.org/10.48550/arXiv.2303.18223 (2023). 36. Barretina, J. et al. The Cancer Cell Line Encyclopedia enables
12. Zhang, R., Luo, Y., Ma, J., Zhang, M. & Wang, S. scPretrain: predictive modelling of anticancer drug sensitivity. Nature 483,
multi-task self-supervised learning for cell-type classification. 603–607 (2012).
Bioinformatics 38, 1607–1614 (2022). 37. Iorio, F. et al. A landscape of pharmacogenomic interactions in
13. Yang, F. et al. scBERT as a large-scale pretrained deep language cancer. Cell 166, 740–754 (2016).
model for cell type annotation of single-cell RNA-seq data. Nat. 38. Bellamy, D., Celi, L. & Beam, A. L. Evaluating progress on machine
Mach. Intell. 4, 852–866 (2022). learning for longitudinal electronic healthcare data. Preprint at
14. Cui, H., Wang, C., Maan, H. & Wang, B. scGPT: towards building a arXiv https://doi.org/10.48550/arXiv.2010.01149 (2020).
foundation model for single-cell multi-omics using generative AI. 39. Geeleher, P., Cox, N. J. & Huang, R. Clinical drug response can be
Nat Methods https://doi.org/10.1038/s41592-024-02201-0 predicted using baseline gene expression levels and in vitro drug
(2024). sensitivity in cell lines. Genome Biol. 15, R47 (2014).
15. Theodoris, C. V. et al. Transfer learning enables predictions in 40. Subramanian, A. et al. Gene set enrichment analysis: a
network biology. Nature https://doi.org/10.1038/s41586-023- knowledge-based approach for interpreting genome-wide
06139-9 (2023). expression profiles. Proc. Natl Acad. Sci. USA 102, 15545–15550
16. Choromanski, K. et al. Rethinking attention with performers. (2005).
Preprint at arXiv https://doi.org/10.48550/arXiv.2009.14794 41. Kanehisa, M. & Goto, S. KEGG: Kyoto Encyclopedia of Genes and
(2022). Genomes. Nucleic Acids Res. 28, 27–30 (2000).
17. Ma, X. et al. Luna: Linear Unified Nested Attention. Adv. Neural Inf. 42. Saddoughi, S. A., Song, P. & Ogretmen, B. in Lipids in Health and
Process. Syst. 34, 2441–2453 (2021). Disease (eds Quinn, P. J. & Wang, X.) 413–440 (Springer, 2008).
18. Gong, J. et al. xTrimoGene: an efficient and scalable 43. Kurundkar, D. et al. Vorinostat, an HDAC inhibitor attenuates
representation learner for single-cell RNA-seq data. Preprint at epidermoid squamous cell carcinoma growth by dampening
bioRxiv https://doi.org/10.1101/2023.03.24.534055 (2023). mTOR signaling pathway in a human xenograft murine model.
19. Chen, J. et al. Transformer for one stop interpretable cell type Toxicol. Appl. Pharmacol. 266, 233–244 (2013).
annotation. Nat. Commun. 14, 223 (2023). 44. Park, H. et al. Phase I dose-escalation study of the mTOR
20. He, K. et al. in Proc. IEEE/CVF Conference on Computer Vision and inhibitor sirolimus and the HDAC inhibitor vorinostat in patients
Pattern Recognition 16000–16009 (IEEE, 2022). with advanced malignancy. Oncotarget 7, 67521–67531
21. Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. in Proc. 2019 (2016).
Conference of the North American Chapter of the Association for 45. Zibelman, M. et al. Phase I study of the mTOR inhibitor
Computational Linguistics 4171–4186 (ACL, 2019). ridaforolimus and the HDAC inhibitor vorinostat in advanced
22. Edgar, R., Domrachev, M. & Lash, A. E. Gene Expression Omnibus: renal cell carcinoma and other solid tumors. Invest. N. Drugs 33,
NCBI gene expression and hybridization array data repository. 1040–1047 (2015).
Nucleic Acids Res. 30, 207–210 (2002). 46. Vasudevan, S. et al. Drug-induced resistance and phenotypic
23. Seal, R. L. et al. Genenames.org: the HGNC resources in 2023. switch in triple-negative breast cancer can be controlled via
Nucleic Acids Res. 51, D1003–D1009 (2023). resolution and targeting of individualized signaling signatures.
24. Kaplan, J. et al. Scaling laws for neural language models. Preprint Cancers 13, 5009 (2021).
at arXiv https://doi.org/10.48550/arXiv.2001.08361 (2020). 47. Zheng, Z. et al. Enabling single-cell drug response annotations
25. Lopez, R., Regier, J., Cole, M. B., Jordan, M. I. & Yosef, N. Deep from bulk RNA-seq using SCAD. Adv. Sci. 10, e2204113
generative modeling for single-cell transcriptomics. Nat. Methods (2023).
15, 1053–1058 (2018). 48. Ho, Y.-J. et al. Single-cell RNA-seq analysis identifies markers
26. van Dijk, D. et al. Recovering gene interactions from single-cell of resistance to targeted BRAF inhibitors in melanoma cell
data using data diffusion. Cell 174, 716–729.e27 (2018). populations. Genome Res. 28, 1353–1363 (2018).
27. Huang, M. et al. SAVER: gene expression recovery for single-cell 49. Kinker, G. S. et al. Pan-cancer single-cell RNA-seq identifies
RNA sequencing. Nat. Methods 15, 539–542 (2018). recurring programs of cellular heterogeneity. Nat. Genet. 52,
28. Li, W. V. & Li, J. J. An accurate and robust imputation method 1208–1218 (2020).
scImpute for single-cell RNA-seq data. Nat. Commun. 9, 997 50. Rood, J. E., Maartens, A., Hupalowska, A., Teichmann, S. A. &
(2018). Regev, A. Impact of the Human Cell Atlas on medicine. Nat. Med.
29. Kedzierska, K. Z., Crawford, L., Amini, A. P. & Lu, A. X. Assessing 28, 2486–2496 (2022).
the limits of zero-shot foundation models in single-cell biology. 51. Adamson, B. et al. A multiplexed single-cell CRISPR screening
Preprint at bioRxiv https://doi.org/10.1101/2023.10.16.561085 platform enables systematic dissection of the unfolded protein
(2023). response. Cell 167, 1867–1882 (2016).
30. Zheng, G. X. Y. et al. Massively parallel digital transcriptional 52. Dixit, A. et al. Perturb-Seq: dissecting molecular circuits with
profiling of single cells. Nat. Commun. 8, 14049 (2017). scalable single-cell RNA profiling of pooled genetic screens. Cell
31. Abdelaal, T. et al. A comparison of automatic cell identification 167, 1853–1866 (2016).
methods for single-cell RNA sequencing data. Genome Biol. 20, 53. Roohani, Y., Huang, K. & Leskovec, J. Predicting transcriptional
194 (2019). outcomes of novel multigene perturbations with GEARS. Nat.
32. Luecken, M. D. et al. Benchmarking atlas-level data integration in Biotechnol. https://doi.org/10.1038/s41587-023-01905-6
single-cell genomics. Nat. Methods 19, 41–50 (2022). (2023).
33. Polański, K. et al. BBKNN: fast batch alignment of single cell 54. Lotfollahi, M., Wolf, F. A. & Theis, F. J. scGen predicts single-cell
transcriptomes. Bioinformatics 36, 964–965 (2020). perturbation responses. Nat. Methods 16, 715–721 (2019).
34. Unger, F. T., Witte, I. & David, K. A. Prediction of individual 55. Lotfollahi, M. et al. Learning interpretable cellular responses to
response to anticancer therapy: historical and future complex perturbations in high-throughput screens. Preprint at
perspectives. Cell. Mol. Life Sci. 72, 729–757 (2015). bioRxiv https://doi.org/10.1101/2021.04.14.439903 (2021).
Nature Methods | Volume 21 | August 2024 | 1481–1491 1490
Article https://doi.org/10.1038/s41592-024-02305-7
56. Lotfollahi, M. et al. Predicting cellular responses to complex 65. Willis, S. N. et al. Environmental sensing by mature B cells
perturbations in high-throughput screens. Mol. Syst. Biol. 19, is controlled by the transcription factors PU.1 and SpiB. Nat.
e11517 (2023). Commun. 8, 1426 (2017).
57. Segerstolpe, Å. et al. Single-cell transcriptome profiling of human 66. Vasilevsky, N. A., Ruby, C. E., Hurlin, P. J. & Weinberg, A. D.
pancreatic islets in health and type 2 diabetes. Cell Metab. 24, OX40 engagement stabilizes Mxd4 and Mnt protein levels in
593–607 (2016). antigen-stimulated T cells leading to an increase in cell survival.
58. Domínguez Conde, C. et al. Cross-tissue immune cell analysis Eur. J. Immunol. 41, 1024–1034 (2011).
reveals tissue-specific features in humans. Science 376, eabl5197 67. Ma, S. et al. Chromatin potential identified by shared single-cell
(2022). profiling of RNA and chromatin. Cell 183, 1103–1116 (2020).
59. Xu, C. et al. Probabilistic harmonization and annotation of 68. Chen, S., Lake, B. B. & Zhang, K. High-throughput sequencing of
single-cell transcriptomics data with deep generative models. the transcriptome and chromatin accessibility in the same cell.
Mol. Syst. Biol. 17, e9620 (2021). Nat. Biotechnol. 37, 1452–1457 (2019).
60. Ma, F. & Pellegrini, M. ACTINN: automated identification of cell types
in single cell RNA sequencing. Bioinformatics 36, 533–538 (2020). Publisher’s note Springer Nature remains neutral with regard to
61. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell jurisdictional claims in published maps and institutional affiliations.
gene expression data analysis. Genome Biol. 19, 15 (2018).
62. Tan, Y. & Cahan, P. SingleCellNet: a computational tool to classify Springer Nature or its licensor (e.g. a society or other partner) holds
single cell RNA-seq data across platforms and across species. exclusive rights to this article under a publishing agreement with
Cell Syst. 9, 207–213 (2019). the author(s) or other rightsholder(s); author self-archiving of the
63. Aibar, S. et al. SCENIC: single-cell regulatory network inference accepted manuscript version of this article is solely governed by the
and clustering. Nat. Methods 14, 1083–1086 (2017). terms of such publishing agreement and applicable law.
64. Date, D. et al. Kruppel-like transcription factor 6 regulates
inflammatory macrophage polarization. J. Biol. Chem. 289, © The Author(s), under exclusive licence to Springer Nature America,
10318–10329 (2014). Inc. 2024
Nature Methods | Volume 21 | August 2024 | 1481–1491 1491
Article https://doi.org/10.1038/s41592-024-02305-7
Methods Encoder. The encoder only processed the embeddings of nonzero and
Pretraining data collection and preprocessing nonmasked values (that is, the expressed genes and two total count
Data collection. Many human scRNA-seq data were deposited in the numbers) so the input length of the encoder was about 10% of the full
Gene Expression Omnibus (GEO) repository, HCA, Single Cell Portal, gene length. Denoting SE={SE,SE,…,SE} as the index set of nonzero
0 1 K
EMBL-EBI and so on. There were also several studies to integrate human and nonmasked values with K elements, the input of encoder was
single cells from multiple resources, such as hECA4, DISCO7 and so on. defined as
Each dataset in these databases was linked to a published study and
thus had a corresponding DOI ID. We manually collected scRNA-seq XEnc−input=[Einput,Einput,…].
data from these databases and removed the dataset with a duplicated
SE
0
SE
1
ID. Most of the datasets provided the raw count matrix. For the data-
set with normalized expression profiles, we converted them back The design of encoder greatly reduced the required computational
to the raw count form: we treated the smallest nonzero value in the resources, making it possible for the encoder to employ a series of
original matrix as a raw count value of 1, all remaining nonzero values vanilla transformer blocks to capture gene dependency without any
were divided by this smallest value and the integer part was taken. For kernel or low-rank approximation. The outputs of encoder were inter-
the dataset with transcripts per million (TPM) or fragments per kilo- mediate embeddings Xinter:
base of transcript per million fragments mapped (FKPM) expression
profiles that cannot be converted back to raw counts, we kept them Xinter=Trm(XEnc−input)∈ℝK×d,
unchanged.
Our data collection comprises over 50 million single cells of where Trm represents a series of transformer blocks and the core
diverse organs and tissues from samples of healthy donors and of vari- function in these blocks is the attention mechanism that can be formu-
ous diseases and cancer types, representing a full spectrum of human lated as
single-cell transcriptomes. We split all data into training and validation
datasets. The validation dataset was randomly sampled and contained QKT
Att(Q,K,V)=D−1AV A=exp( ),D=diag(A1K),
100,000 single cells, and remained consistent for all test models. √d
Gene symbol unification. We unified the gene symbols of all raw where Q=XWq , K=XWk and V=XWv are linear transformation of the
count gene expression matrices by using the gene symbol mapping input X, and W⋅ are training parameters. 111K is the all-ones vector of
reference provided by HUGO Gene Nomenclature Committee. We length K, and diag(·) is a diagonal matrix with the input vector as the
included human protein-coding genes and common mitochondrial diagonal.
genes, constituting a total of 19,264 genes. If some symbols were miss- The intermediate embeddings Xinter had two usages: (1) they were
ing, we padded them with zero values. sent into the decoder with the zero and mask embeddings, and (2) they
were pooled as cell embeddings for downstream usages.
Quality control. To filter contaminated empty droplets, extremely
low-quality cells and damaged cells, we kept cells with over 200 genes Decoder. To establish a transcriptome-wide gene regulation relation-
expressed (that is, expression vector with nonzero value count >200) ship, the zero-expressed genes should also be considered for recover-
for pretraining by using the Seurat69 and Scanpy61 packages. ing expression values at mask positions. The intermediate embeddings
from encoder were concatenated with the zero and mask embeddings
scFoundation model architecture to form a decoder input tensor XDec−input with full gene length
We developed the xTrimoGene model as the backbone model of
scFoundation. It had three modules: the embedding module converted XDec−input=[Xinter,E0,…,E0 ,Em,…,Em ] T ∈ℝ19,266×d,
scalar value into embeddings that were required for the transformer
0 K0 0 Km
block; the encoder took the nonzero and nonmasked expressed genes
as input, used the vanilla transformer block and had large param- where K0 and Km were the number of zero and masked embeddings,
eter size; and the decoder took all genes as input, used the performer respectively. We used the kernel-based approximation transformer
block and had a relatively small parameter size. Ablation experiments variant Performer16 as the backbone in the decoder, since the attention
showed that such asymmetric design reduced the computational and calculation was challenging for long sequences16,70. In Performer, the
memory challenges compared with other architectures (Supplemen- kernelizable attention mechanism is used:
tary Table 6).
Att(Q,K,V)=D
−̂ 1
(∅(Q)(∅(K))
T
V)D
−̂ 1
=diag(∅(Q)(∅(K))
T
1K),
Embedding module. Given a cell’s gene expression value vector
Xinput∈ℝn=19,264, the expression value xinput of gene i was a continuous where ∅(•) is a kernel function that used for approximating the A matrix
i
scalar greater than or equal to zero. Unlike the previous language or in the original attention equation.
recently developed single-cell transformer-based model, for each gene The output of decoder is XOut, where
i the embedding module directly converted the expression scalar into
a learnable value embedding Ei without any discretization. Then, the XOut=Performer(XDec−input)∈ℝ19,266×f.
value embedding was added with gene name embeddings TG to form
i
the final input embeddings Einput. The value embeddings were a For predicting the expression value, the embeddings of T and S
i
weighted summarization of a set of embeddings, where the weights were dropped and an MLP was followed to project XOut to scalars.
were learned from the gene expression scalar values. The gene name These scalars formed a prediction vector P, where
embeddings were retrieved from a look-up table, where the embed-
dings in the table are randomly initialized and can be learned during P=MLP(XOut)∈ℝ19,264.
pretraining (Supplementary Note 8). The ablation of continuous
embeddings scheme showed that the benefit of our design All parameters Θ={Ei,TG
i
,ΘEncoder,ΘDecoder,ΘMLP} were optimized
compared with other value discretization methods (Supplementary during the pretraining. The detailed hyperparameter setting of differ-
Fig. 14). ent models can be found in Supplementary Table 7.
Nature Methods
Article https://doi.org/10.1038/s41592-024-02305-7
RDA pretraining task that concatenating the embeddings obtained by max-pooling and
We trained the model with an RDA gene expression prediction task. mean-pooling the embeddings of all genes, and the embeddings of the
For each raw pretraining single-cell gene expression vector, we used S token and T token, achieved the best performance (Supplementary
a hierarchical Bayesian downsampling strategy to generate its low Note 13 and Supplementary Tables 9 and 10). The concatenation of the
total counts variant or unchanged profiles as the input vector. We four embeddings built the new cell embeddings with 3,072 dimensions,
normalized and log-transformed the raw and input gene expression, and we trained the downstream model based on these cell embeddings.
and set the total counts of the raw and input vectors as two total count
indicators T and S, respectively. After normalizing gene expression, DeepCDR. We used the cell line and drug-paired data preprocessed
the original total count value of cells is removed. By reintroducing this by DeepCDR. The cell line data contain 697 gene expression profiles,
information through tokens, we believe it can enhance the model’s and we aligned these genes with our unified gene symbol list. The
pretraining performance since the dropout in cells is usually correlated drugs were represented as graphs with consistent feature matrices
with the total count value. Please refer to Supplementary Notes 9 and and adjacent matrix sizes. In total, 223 drugs and 561 cell lines data
10 for details of the sampling strategy and count indicators calculation. from 31 cancer types were considered. We followed the original study
Then we randomly masked the genes’ expressions of the input to randomly split 5% of data as the test set, resulting in 89,585 and 4,729
vector. In this study, we used 30% as the masking ratio for both zero cell line-drug samples for training and testing, respectively. For each
and nonzero values. Then the masked input vector was concatenated cell line, we set both indicators S and T equal to the sum of all gene
with two total count indicators T and S and fed into the model. After expression values. And we fed the nonzero gene expression values and
getting the model-predicted raw gene expression, we conducted the two indicators into the model encoder and got the context embed-
regression loss on the masked genes between the predicted and the raw ding for each gene. The bulk-level cell-line embedding was obtained
values (Supplementary Note 11). If the input vector was unchanged, the by the max-pooling operation for each embedding dimension across
model learned to capture the relation between genes within a single all genes.
cell. If the input vector was the low-total-count variant, the model We trained the baseline DeepCDR model by setting parameters
learned the relationship between cells with different read depths. ‘-use_gexp’ as True and ‘-use_mut’ and ‘-use_methy’ as False. Then for the
The ablation studies (Supplementary Note 1) of taking downsampling scFoundation-based model, we directly replaced the gene expression
strategy (Supplementary Table 8) and regression loss (Supplementary with the cell-line embedding and trained the DeepCDR with the same
Fig. 15) showed that the current setting could facilitate learning cell setting. For each gene, we computed the PCC between predicted IC
50
characteristics. and truth IC across all cell lines. For each cell line, we computed the
50
The overall model architecture of scFoundation is shown in Sup- PCC across all drugs conducted on this cell line.
plementary Fig. 16. For the model and pretraining implementation,
please refer to Supplementary Note 12. SCAD. We followed the same experimental setting as the original
SCAD study, conducting fivefold cross-validation. For each split, four
Read-depth enhancement analysis folds of the bulk and single-cell data were used to train the model, and
For the gene expression prediction evaluation, we sampled 10,000 cells the other fold was left for prediction, and we merged all split results
with high total counts (higher than 1,000) from 50 million single-cell to get the prediction for all cells. We used all genes and conducted
data as the validation dataset. These 10,000 cells were excluded at the weighted sampling in the model training process. For training the
the training stage. Then, we used a binomial distribution to generate baseline model, gene expression values were transformed into the
the low total counts gene expression vector and fed it into our model. z score in their provided processed data.
We only evaluate nonzero gene expression values considering that For training the scFoundation-based model, we used the normal-
0 expression values do not change in value after downsampling. In ized gene expression data. For bulk data, we set both S and T to the sum
addition to using MSE as the evaluation metric, we also used the MRE, of all gene expression values to maintain original cell line features. For
which can reflect the relative error single-cell data, we set token S to the sum of gene expression values
and token T to 10,000, the empirically maximum sequencing depth
MRE=
1
∑
|M| (Xi−Pi) 2
.
per cell. Then, the nonzero values of each sample and two indicators
|M|
i=0
Xi were fed into the encoder of the pretrained model. The outputs were
the context embeddings of genes for each sample and then condensed
For the clustering analysis, we got the cell embeddings from into the cell embeddings.
scFoundation and scVI encoder. For others, we got the imputed gene
expression profiles. All methods were used with the default parameter Perturbation prediction. We unified the gene symbol list to 19,264 and
setting. Then, we followed the SCANPY pbmc3k tutorial and got the cell generated the gene co-expression network on each dataset. Following
cluster by the function ‘sc.tl.leiden’. the original GEARS study, for one-gene perturbations, we randomly
For the evaluation of the clustering results, we first used ARI and assigned 75% of perturbations as training data. For two-gene perturba-
NMI (scikit-learn71 package) as indicators to evaluate the degree of tions, 75% of perturbations where both genes were in the seen set (0/2
consistency between the clustering results obtained by different meth- unseen) were designated as the training set, while all other combina-
ods and the actual cell type labels. Considering that the acquisition tions (1/2 and 2/2 unseen) were held out for testing. Then, we trained
of cluster labels will also be affected by the choice of the clustering the GEARS baseline model by setting epoch to 15 and batch size to 30.
algorithm, we used SIL as another evaluation indicator, which measures The CPA model does not have gene embeddings, and it takes the drug
the aggregation degree of true cell type labels on the cell neighbor- or gene perturbation embeddings as the input model. We trained the
hood maps given by different methods and, thus, is independent of CPA model with the same parameter setting used in the GEARS study.
the choice of clustering algorithm, reflecting the intrinsic properties Gene perturbations were encoded as one-hot vectors, and two-gene
of cell representation. perturbations were represented by the addition of two one-gene per-
turbation vectors. In the embedding-based model, each cell’s T and S
Downstream methods values equaled its total counts, with gene expression and indicators
All baseline models were trained with default parameters. We fed into the model. The scFoundation’s last MLP layer was dropped to
dumped the cell embeddings for DeepCDR and SCAD tasks, and gene extract gene context embeddings from the decoder, serving as node
embeddings for the GEARS task. As for cell embeddings, we found features for the co-expression graph. We froze scFoundation and solely
Nature Methods
Article https://doi.org/10.1038/s41592-024-02305-7
trained the downstream GEARS model, employing gradient accumula- expressed gene modules via the online EnrichR73 tools. We used the
tion to maintain consistent batch size with the baseline during training. ‘PanglaoDB Augmented 2021’ dataset and selected the term with the
We followed the definition and metrics used in GEARS. We focused lowest adjusted P value to interpret gene modules. As for gene network,
on the synergy and suppression gene intersection types since they were we computed the similarity of gene embeddings with a module, and
the most basic types. Identification of these two types was based on the marked the top 5 edges with the highest value.
magnitude score, which measured the similarity between the two-gene As for gene regulation inference, we got all known transcription
perturbation and combining two single-gene perturbations. Specifi- factor (TF)–target gene pairs from SCENIC and quantified their rela-
cally, let the mean change between post- and pre-A perturbed cells as tionships based on the similarity of their gene embeddings. For each
δga . A linear model was used to fit the effect of δga , δgb and δga+b : TF, we selected the top 1,000 pairs with high similarity as the candidate
pairs. Since transcriptomic data do not provide direct insights into
δga+b=ca×δga+cb×δgb+ϵ, TF–gene binding at the sequence level, we used RcisTarget module
of SCENIC to refine our selected pairs. Using the auc_cell module of
where ϵ captures the error in the model fit. We used the robust regres- SCENIC, we then derived the TF enrichment scores in cell types and
sion with a Theil–Sen estimator following the same procedure used identified the top-ranked cell-specific TFs. However, we would like
in previous study72. Using the values of the coefficients, magnitude to point out that directly calculating similarity from embeddings is
was defined as a simplistic approach that may not fully harness the rich information
within the vectors. Future endeavors could explore algorithms that
Magnitude=√c2
a
+c2
b
. leverage context embeddings for more sophisticated GRN inference,
such as those employing graph neural networks.
All test two-gene perturbations were ranked by magnitude score,
with the top- and bottom-ranked being considered synergistic and Reporting summary
repressive types, respectively. Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Cell type annotation. We randomly split each dataset into
train:valid:test of 8:1:1. For scFoundation, we added a two-layer MLP Data availability
with ReLU as the activation function after the encoder. The output of All data used in this study are publicly available and the usages are
MLP is the predicted label. Considering the imbalanced cell numbers illustrated in the Methods. The pretraining datasets were mainly
of different cell types, we used a weighted cross entropy loss. Given in downloaded from GEO (https://www.ncbi.nlm.nih.gov/geo/), Single
total C cell types, and cell type i has Ai cells, the weight of each cell type Cell Portal (https://singlecell.broadinstitute.org/single_cell), HCA
wi in the loss was defined as (https://data.humancellatlas.org/) and EMBL-EBI (https://www.ebi.
ac.uk/), and the detailed dataset list we used is in Supplementary
wi= ∑ C
i
B
=
i
1
Bi Bi=max( i=
m
1,…
a
A
x
, i C
Ai
,50),
D
l
m
o
a
a
o
t
d
h
a
e
u
1
d
a
a
n
f
n
r
g
d
o
x
m
/
2
S
.
A
t
T
h
V
h
e
E
e
f
R
o
d
-
l
p
a
l
t
o
a
a
p
w
s
e
i
e
n
r
t
)
g
s
; Z
u
li
h
s
n
e
e
k
d
n
s :
g
f
B
o
6
a
r
8
r
K
d
o
o
d
n
w
a
d
t
n
a
a
s
t
s
t
a
e
r
s
t
e
e
(
a
h
t
m
t
(
t
h
p
t
t
a
t
s
s
p
:/
k
s
/
s
w
:/
c
/
w
g
a
w
i
n
t
.
h
b
d
u
e
r
b
o
d
.
p
c
o
b
o
w
o
m
n
x
/
-
.
com/sh/w3yg2nucnng5v1u/AAAM8Ym_KU9XF4z51RT81eNEa?dl=0);
where Bi was the scaled number. We set the learning rate as 0.001, the Segerstolpe dataset (https://zenodo.org/records/3357167); CDR
gradient accumulation step as 5 and the batch size in each step was 64. dataset (https://github.com/kimmo1019/DeepCDR); Single cell drug
We got the model with highest F1 score on the validation dataset as the response classification dataset (https://github.com/CompBioT/
best model for testing. SCAD); Perturbation dataset (https://github.com/snap-stanford/
For scBERT, we converted the gene expression matrix to match GEARS); Simulated reference and query dataset used for cell mapping
their input required gene symbol list and fine-tuned their pretrained (https://doi.org/10.6084/m9.figshare.21456645.v4); and Organoid
model. We used the validation dataset to select the best model. For and in vivo data used for cell mapping (https://doi.org/10.17632/
methods CellTypist, scANVI, ACTINN and SingleCellNet, we fed the sm67hr5bpm.1). The processed gene expression data and the embed-
training and valid dataset into models and trained them with default dings generated by scFoundation can be found in our GitHub repository
parameter settings. We got the prediction results of test data from the (https://github.com/biomap-research/scFoundation) and figshare
corresponding function such as ‘celltypist.annotate’ of CellTypist. As (https://doi.org/10.6084/m9.figshare.24049200) (ref. 74).
for Scanpy, we used the ‘sc.tl.ingest’ function to transfer the cell type
label into the test data based on the PCA components, and treated the Code availability
transferred label as the prediction. For each method on the test split, The code for using the online API, the model codes and weight, a dem-
we computed the average macro F1 score of the top three performed onstration of inferring embeddings, codes of producing the results for
model replicates. the downstream tasks are at the GitHub repository at https://github.
com/biomap-research/scFoundation or Zenodo75. A summary of all
Gene module and gene regulation inference. We randomly selected code and data information is in Supplementary Data 3.
100 cells from the three cell types (Monocytes, CD8+ cytotoxic T cells,
and B cell) in Zheng68K data, resulting in a total of 300 cells. These data References
were processed through scFoundation to obtain the context embed- 69. Hao, Y. et al. Integrated analysis of multimodal single-cell data.
ding for all genes, resulting in a matrix of dimensions 300 × 19,264 × 512. Cell 184, 3573–3587 (2021).
After selecting the highly variable genes and averaging the gene embed- 70. Beltagy, I., Peters, M. E. & Cohan, A. Longformer: the
dings across cells, we derived 495 gene embeddings, each of 512 dimen- long-document transformer. Preprint at arXiv https://doi.
sions and used the Leiden clustering method to get 34 gene modules org/10.48550/arXiv.2004.05150 (2020).
based on embeddings. We then computed the average expression of 71. Pedregosa, F. et al. Scikit-learn: machine learning in Python.
each gene module across the 300 cells using the ‘scanpy.tl.score_genes’ J. Mach. Learn. Res. 12, 2825–2830 (2011).
function, producing a scoring matrix of 300 × 34. We conducted differ- 72. Norman, T. M. et al. Exploring genetic interaction manifolds
ential analysis on this score matrix to identify marker gene modules for constructed from rich single-cell phenotypes. Science 365,
each cell type. Then, we did the enrichment analysis on the differential 786–793 (2019).
Nature Methods
Article https://doi.org/10.1038/s41592-024-02305-7
73. Chen, E. Y. et al. Enrichr: interactive and collaborative HTML5 J.G., X. Zeng, C.L., T.W., X.C., J.M., L.S. and X. Zhang provided advice on
gene list enrichment analysis tool. BMC Bioinf. 14, 128 (2013). pretraining framework design and downstream tasks. M.H., J.G., J.M.,
74. Hao, M. scFoundation: large scale foundation model on L.S. and X. Zhang wrote the manuscript. All authors read and approved
single-cell transcriptomics - processed datasets. figshare. the final manuscript.
https://doi.org/10.6084/m9.figshare.24049200.v3 (2023).
75. Hao, M. code of scFoundation: large scale foundation model Competing interests
on single-cell transcriptomics. Zenodo https://doi.org/10.5281/ J.G., X.Ze., C.L, Y.G., X.C., T.W. and L.S. are employees of BioMap. M.H.
zenodo.8330924 (2023). contributed to this work while part-time interning at BioMap. The
remaining authors declare no competing interests.
Acknowledgements
We thank Q. Yin, L. Chao and Z. He from Biomap and Y. Chen, Additional information
C. Li, H. Bian, J. Li, T. Ma, L. Wei and R. Jiang from Bioinfo Division, Supplementary information The online version contains
Tsinghua University for discussions and comments. This work was supplementary material available at
partially supported by the National Key R&D Program of China https://doi.org/10.1038/s41592-024-02305-7.
(grant 2021YFF1200901), National Natural Science Foundation of
China (NSFC) (grants 62250005 and 61721003) and Tsinghua-Fuzhou Correspondence and requests for materials should be addressed to
Institute for Data Technology (TFIDT2021005). Jianzhu Ma, Xuegong Zhang or Le Song.
Author contributions Peer review information Nature Methods thanks the anonymous
M.H., J.M., L.S. and X. Zhang conceived the study. M.H. X. Zeng reviewers for their contribution to the peer review of this work. Primary
and Y.G. collected the downstream datasets involved in this article. Handling Editor: Lin Tang, in collaboration with the Nature Methods
Y.G. and L.S. developed data collection criteria and strategies for team. Peer reviewer reports are available.
pretraining. M.H., J.G., X. Zeng, C.L., T.W. and X.C. proposed the
pretraining framework. M.H., J.G., X. Zeng and C.L. implemented and Reprints and permissions information is available at
pretrained the models. M.H. and J.G. benchmarked all methods. www.nature.com/reprints.
Nature Methods
