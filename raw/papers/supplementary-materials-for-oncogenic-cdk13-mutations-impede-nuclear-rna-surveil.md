---
source_path: /mnt/c/Users/Administrator/Zotero/storage/VEMFMCBI/science.abn7625_sm.pdf
ingested: 2026-04-23
sha256: a71a731726c9c410
---

Supplementary Materials for
Oncogenic CDK13 mutations impede nuclear RNA surveillance
Megan L. Insco et al.
Corresponding authors: Megan L. Insco, megan_insco@dfci.harvard.edu; Leonard I. Zon,
leonard.zon@enders.tch.harvard.edu
Science 380, eabn7625 (2023)
DOI: 10.1126/science.abn7625
The PDF file includes:
Materials and Methods
Figs. S1 to S5
Tables S1 to S8
References
Other Supplementary Material for this manuscript includes the following:
Data S1
MDAR Reproducibility Checklist
Materials and Methods
Human Patient Data
Driver gene analysis and clonality assessment: We downloaded all available whole-exome and whole-genome
sequencing datasets for cutaneous melanomas available from cBioPortal (http://cbioportal.org) and the ICGC Data
Portal (http://dcc.icgc.org), excluding datasets primarily focused on acral or desmoplastic melanoma. We excluded
duplicate or serial samples from the same individual and restricted analysis to only those samples with matched tumor-
normal sequencing. In total, we analyzed 1,347 samples drawn from 11 datasets (26), (27), (28), (29), (30), (24), (31),
(32), (33). All mutations were confirmed absent in matched germline samples.
We retrieved the pre-called mutation data from the cBioPortal database (collected mutation data from original
publication) and ICGC data portal (release_28; simple somatic mutations). We then limited all the mutations only to the
whole-exome regions for the downstream analysis. Samples were subsequently analyzed using OncodriveFM (34);
http://bg.upf.edu/group/projects/oncodrive-fm.php] to identify melanoma-specific drivers. Three algorithms were
incorporated in the analysis: SIFT, PolyPhen-2 (68), and Mutation Assessor (69). OncodriveFM calculates a metric of
functional impact using the scores predicted from these three algorithms followed by assessing how the functional
impact of variants found in a gene across tumor samples deviates from a null distribution.
For assessment of potential clonality, we utilized read depth data for reference and variant alleles where such data
were available for the TCGA PanCancer SKCM dataset. Specifically, we assessed the clonality of CDK13 mutations by
checking the location of CDK13 mutations in the distribution of variant allelic fraction (VAF) of all somatic mutations.
Due to the VAF being impacted by copy number alterations, we limited analysis to mutations located within copy neutral
regions. Finally, we compared VAFs of CDK13 mutations to tumor samples with mutations in well-established driver
genes (BRAF, NRAS, or NF1). We classified the clonality of CDK13 mutations as the following:
1) “Clonal”. A major peak with 0.15 < VAF < 0.5 (representing the clonal cluster of mutations) was observed
in the plot of VAF distribution. The VAF of CDK13 mutations were located within the clonal cluster or have
larger VAF than the clonal cluster. The VAF of mutation in known driver genes (e.g. NRAS, BRAF, or NF1) if
detected was also observed within the clonal cluster.
2) “Subclonal”. In addition to the clonal cluster, a second peak with lower VAF (representing the subclonal
cluster of mutations) in the plot of VAF distribution was observed. The VAF of CDK13 mutations were
located with the subclonal cluster or have an even smaller VAF than the subclonal cluster.
3) “Potentially clonal”: A major peak with very low (VAF<0.15, lower purity tumors) was observed in the
plot of VAF distribution. The VAF of CDK13 mutations are either larger than the VAF of mutations in the
driver genes or located very close to the peak.
4) “Unknown”. The VAF of CDK13 mutations was located between clonal and subclonal peaks, or
alternatively outside the clonal peak with lower VAF if no subclonal peak was detected.
For enrichment analyses, mutations were classified as high-impact if they were predicted deleterious or potentially
deleterious by any of the three prediction algorithms.
THOC2, ZFC3H1, ZC3H14, BRAF, NRAS, and MTR4 mutations were downloaded from melanoma TCGA data on
9/5/19 (287 patients with mutational and copy number data). ZFC3H1 and ZC3H18 recurrent mutations and mutational
frequency in cancer downloaded from cBioPortal’s “curated set of non-redundant studies” on 2/7/20. Transcriptional
CDK mutational frequency in melanoma was calculated from TCGA Skin Cutaneous Melanoma PanCancer from data
downloaded 10/20/22 (n=448 samples with mutational data) (24).
Patient survival analysis: Overall survival, mutation, and expression data (z-score values) from the TCGA melanoma
cohort (24) were downloaded on 4/7/17 using cBioPortal (70).low-function CDK13 group was defined by either having
a mutation in CDK13 and/or having low CDK13 expression, which was defined by z score equal or less than -1.0. The
difference in survival between low-function CDK13 vs. remaining cases was tested using a log-rank test. Multivariate
analysis was done using patient sex and age (Table S3). The difference in survival between low-function CDK13 stage
0, 1, or 2 patients were compared with remaining stage 0,1, or 2 patients.
5’ to 3’ RNA-seq gradient analysis: RNA-seq bams were downloaded on 7/27/18 from cutaneous melanoma patients
from The Cancer Genome Atlas (TCGA) (24) from 3 patients with somatic CDK13 kinase-domain mutations and 5 best
matched control WT CDK13 patients by 1) stage, 2) age, 3) sex, and 4) oncogene from the National Cancer Institute
(NCI) Genomic Data Commons (GDC) Data Portal (Patient characteristics and TCGA IDs in Table S4. Files were sorted
using SAMtools (71). All exons were assigned to one of the following classes: The first exon of every gene that contains
the most splice junctions to the next downstream exon is considered the ‘consensus’ isoform and is labeled as the first
exon. Any other first exons at alternative transcriptional start sites are then classified as alternative first (“Alt First”)
exons. Similarly, the terminal exon of a gene that has the most splice junctions associated is labeled the consensus last
exon, and any other terminal exons are labeled as alternative last (“Alt Last”) exons. Importantly, alternative last exons
are only thus classified if they do not have a 5’ splice site allowing them to be used as internal exons (in which case a
downstream polyadenylation site would be considered and Intronic Polyadenylation Site). Genomic coordinates are
from the hg38 human genome build. Exons were subjected to differential expression analysis using DEXSeq (72, 73).
The log2-fold changes in exons belonging to each class were plotted and the differences in the distribution of these
differential expression comparisons were determined using the non-parametric Wilcoxon rank sum test, two-sided. IGV
tools (http://www.broadinstitute.org/igv) (74)was used to generate TDF files for viewing.
ptRNA isoform quantification in CDK13mut cancers: Because 3’ end sequencing data were not available for TCGA
samples, we instead used the DEXseq-formatted GTF derived from mapping polyadenylation sites in A375 human
melanoma cells (see 3’ sequencing data processing, Human Cell Lines below). CDK13mut tumors were selected from
various cancer types to include missense mutations in the ATP binding region or nonsense mutations in the same region
that would be expected to produce a null allele. For each CDK13mut-carrying tumor sample, a closely matched control
tumor was chosen that carried no mutations or copy-number variations in CDK12, CDK13, ZC3H14, ZC3H18, or
ZFC3H1. The control set was matched as closely as possible by tumor type, molecular subtype, grade, stage, AJCC
pathologic TNM scoring, sex, and age at diagnosis (mean age CDK13mut =54.9, Control = 54.4 years). Patients noted in
Table S6. Hg38 STAR-mapped RNAseq BAM files were downloaded for each tumor sample. The DEXseq script
dexseq_count.py was used to obtain read counts for each sample using the DEXseq-formatted GTF. DEXseq was then
run with the full set of tumor samples, comparing the CDK13mut set against the control set to obtain log2-fold differences
at each intronic poly(A) site, distal (last exon) poly(A) site, and internal constitutive exon. The distributions of these
differences between the CDK13mut and control sets were plotted and statistical significance measured by Wilcoxon Rank
Sum tests.
In Vitro Experiments
Mutation visualization on crystal structure: Patient mutations in CDK13 were plotted on the crystalized kinase
domain (35)using PyMOL.
In vitro kinase assays: Radioactive kinase reactions were performed using recombinant human CDK13 (694-1039) and
Cyclin K (1-300) proteins. Purified recombinant wild type CDK13/CycK and mutant CDK13(R860Q)/CycK,
CDK13(W878L)/CycK, and CDK13(K734R)/ CycK were assayed for phosphorylation activity at a concentration of 0.2
µM in a final volume of 30 µL containing kinase buffer, CDK13 substrates (CTD and c-Myc, 10 µM), cold ATP (1
mM) and 3 mCi [32P]--ATP. The reaction mixture was incubated for 30 min at 30°C at 350 r.p.m. and terminated by
adding EDTA to a final concentration of 50 mM. Aliquots of 15 µl each were spotted onto P81 Whatman paper squares.
Paper squares were washed three times for 5 min with 0.75% (v/v) phosphoric acid, with at least 5 ml washing solution
per paper square. Radioactivity was counted in a Beckman Scintillation Counter (Beckman-Coulter) for max. 5 min.
Kinase assays were performed in duplicate and are represented as mean with s.d. One-way ANOVA for c-Myc substrate
had an “F” value of 1084 and 4 degrees of freedom (dof). One-way ANOVA for CTD52 had an “F” value of 195 and 4
dof.
For the ZC3H14 substrate, human wildtype CDK13 (694-1039) was co-purified together with human wildtype
Cyclin T1 (residues 1-272) T149E mutant and CAK1 from S.cerevisiae in Sf9 insect cells and purified as described
previously (35). Human ZC3H14 full-length (residues 1-736) was cloned into a pET28a-MBP vector and expressed in
E.coli BL21 pLys cells. Cell pellets were resuspended, sonicated, and centrifuged. Pellets were subjected to step-wise
ammonium sulfate precipitation MBP affinity and size exclusion chromatography using a Superdex S200 column
(Cytiva) in SEC buffer (20 mM Hepes pH 8.2, 150 mM NaCl, 1 mM TCEP).
For radioactive ZC3H14 in vitro kinase assays 0.5 µM kinase was incubated with 25 mM substrate and 0.2 mM
ATP containing 0.45 mCi [32P]-𝛾-ATP/mL (Perkin Elmer) in kinase buffer. Reactions were incubated for 0, 30, 60, 90,
120 and 240 min at 30 °C and stopped by addition of EDTA and . spotted onto Amersham Protran nitrocellulose
membrane (GE Healthcare). Counts per minutes were determined in a Beckman Liquid Scintillation Counter (Beckman-
Coulter) for 1 min. Measurements were performed in triplicates and represented as mean with standard deviation (SD).
For Western blots, 0.5 µM CDK13/Cyclin T1 was incubated with 25 mM MBP-ZC3H14 full-length wildtype
and S475A mutant with 2 mM ATP-y-S (Jena Bioscience) in kinase buffer. Reactions were incubated for 240 min at
30°C and stopped by addition of EDTA and alkylated with 2.5 mM para-nitrobenzylmesylate (PNBM; abcam) for 1
hour at room temperature. Samples were run on an SDS-PAGE gel, blotted onto nitrocellulose, blocked with 5% BSA,
incubated with anti-thiophosphate ester at 1:5000 (ab92570) (53), then detected with an HRP-linked secondary. A
second SDS gel stained with Coomassie Brilliant Blue was used as a loading control.
Zebrafish Experiments
Zebrafish melanoma model: Animal studies were approved by Boston Children’s Hospital Institutional Animal Care
and Use Committee (Protocol 17-10-3530R). Experiments were performed as published (38, 75). ARRIVE guidelines
have been followed where possible. Briefly, p53-/-; mitfa:BRAFV600E; mitfa-/- (hereafter referred to as Triples) one-cell
embryos were injected with either 20 ng/µL control or experimental DNA along with tol2 in vitro transcribed RNA for
integration. In all experiments, DNA which overexpresses a gene-of-interest or which uses CRISPR/Cas9 to inactivate
genes-of-interest is marked with an mitfa mini gene which rescues Mitfa, allowing cell autonomous melanocyte genetics.
In experiments where more than one vector was injected, DNA was prepared at 20 ng/µL but divided equally between
included vectors. In overexpression experiments, control vectors expressed EGFP. In CRISPR experiments, controls
had CRISPR-mediated inactivation of arhgap11a, a gene whose loss is neutral in zebrafish melanoma. Embryos were
sorted for melanocyte rescue at 5 days post fertilization (dpf) unless otherwise notes. As zebrafish with melanocyte-
specific cdk13 CRISPR-disruption or melanocyte-specific CDK13WT-expressing zebrafish had few melanocytes as
adults, tumor curves were not gathered. 20 zebrafish were raised per tank to control for density effects. Zebrafish were
scored for the emergence of raised melanoma lesions. Melanoma-free survival curves and Log-rank tests were generated
in Prism.
Zebrafish cloning: The MiniCoopR (MCR) Gateway system was used (38). Zebrafish MCR overexpression constructs
using the mitfa promoter, relevant coding sequence, 3’ pA tail, and the MCR destination vector were assembled with
LR Clonase II Plus (Thermofisher, 12538120). Human CDK13 coding sequence was obtained using HsCD00295573
from the Harvard Plasmid Repository. The human TP53 and SUV39H1 ptRNAswere synthesized. CDK13 in vitro
mutagenesis for K734R, R860Q, P869S, W878L, P881L, and P893L was performed. For CRISPR, the modified
CRISPR MCR vector was used as reported (Kaufman et al., 2016). Briefly, CRISPR/Cas9 MCR constructs include a
mitfa promoter driving Cas9 and a U6 promoter driving expression of the gRNA. gRNAs to cdk13, arhgap11a (control),
ccnT1, or ccnK were selected using CHOP CHOP (76, 77) in exons predicted to code for required protein domains
(Table S7).
CRISPR cutting verification: Prior to cloning into the in vivo system, gRNAs were tested for cutting efficacy in
embryos. Melanoma CRISPR cut site verification was done by extracting DNA, performing proofreading PCR across
the cut site, and deep sequencing of the PCR reads. Data sets were mapped to the Danio rerio genome (version GRCz11)
using Bowtie (version 0.12.9). CrispR Variants Lite was used to identify insertions and deletions (indels) around the
gRNA site. Indels at the gRNA cut site in >1% of reads were used in downstream calculations. Reads that were predicted
to maintain function included in-frame indels as well as wild type reads, while out-of-frame reads were predicted to
cause loss of function.
Western blotting: Protein was quantified using DC Protein Assay (Biorad, 5000116). The following antibodies were
used: anti-CDK13 antibody (Sigma HPA 059241, 1:1000), anti-beta actin (loading control) (CST, 3700S), anti-GFP
(Santa Cruz sc-9996, 1:1000). Rabbit or mouse secondary HRP antibodies were incubated for 1 hour at RT (CST 7074S
or 7076S, 1:2000). Films were developed with Pierce ECL substrate (Thermofisher, 32106).
qPCR: Fast Evagreen qPCR (Biotium, 31003) was used to verify TP53 ptRNA and SUV39H1 expression in zebrafish
melanomas vs. zebrafish gapdh. Deltadelta CT was calculated.
Zebrafish brightfield imaging: For cdk13 CRISPR, control CRISPR, CDK13WT expression, and cdk13 CRISPR +
CDK13WT expression, embryos were sorted for melanocyte rescue at 3 dpf, 20 embryos with the greatest melanocyte
number were imaged, and these images were used for quantification and normalized to zebrafish number. One-way
ANOVA was done with “F” = 13.14 and degrees of freedom = 3. All zebrafish for other timepoints were anesthetized
in tricaine and imaged using bright field microscopy. Melanocyte patterns from 9 weeks post fertilization (wpf) were
categorized into a) no melanocytes, b) minimal melanocytes (0-33% of zebrafish length covered), c) strong melanocytes
(34-100% of zebrafish length covered), or d) black patch (disrupts normal stripes & diameter distance between that
zebrafishes eyes).
Zebrafish melanoma IHC: CDK13W878L, CDK13P893L, and EGFP melanomas were isolated at 18 wpf. The first 10
melanomas with the control or cdk13 gRNA were collected as they arose. Zebrafish were fixed in 4% PFA and paraffin
embedded, sectioned, and stained for PH3 Serine 10 (CST 9701) at 1:200 and then stained with secondary HRP-goat
anti rabbit secondary (Dako K5007). The PH3 positive cells were counted and averaged from the two mm2 with the
most PH3 positive cells.
ChIP-Seq in zebrafish: Melanomas expressing either EGFP or CDK13W878L generated in Triples zebrafish were
disrupted and 100 micron filtered. Cells were fixed and counted. ChIP was performed as published (78). Spike-in
Drosophila chromatin was added with 10 ng per million cells (Active motif, 53083), and antibody 2 g was added to
the beads (Active Motif, 61686). IPs were performed using antibodies to hypophosphorylated RNAPII (abcam ab817,
clone 8WG16, lot GR313984-17) and RNAPII S2 CTD (ab5095; Lot G309257-1). Libraries were prepared using the
NEBNextMultiplex Oligos for Illumina kit (NEB) and sequenced on an Illumina HiSeq 2000.
ChIP-Seq processing and quantification: Raw reads were aligned twice: first to the dm6 revision of the D.
melanogaster genome to remove exogenous spike-in reads using bowtie version 1.2.2 (79) with parameters -k 1 -m 1;
unmapped reads were then aligned to the danRer10 revision of the zebrafish genome with default parameters.
Version 90 of the danRer10 Ensembl gene set was downloaded for zebrafish ChIP-Seq analysis. For statistical
analysis, reads-per-million-normalized ChIP-Seq signal was quantified in promoters (transcription start sites +/- 250bp)
for genes greater than 2kb in total length using bamToGFF (https://github.com/BradnerLab/pipeline) with parameters –
m 1 –r –e -200 –f 1. Reads-per-million-normalized ChIP-Seq signal was quantified using bamToGFF -m 1 -r -e 200 -f
1 in gene bodies (from 25%-75% of the span from the transcription start site to transcription termination site) for
statistical analysis. Two-tailed Student’s t test was used to determine the significance of differences between conditions.
Whole-gene metagenes across all genes greater than 2kb in length were constructed in three sections: -2kb upstream
of the transcription start site to the transcription start site, transcription start site to the transcription end site, and
transcription end site to 2kb downstream of the transcription end site. Matrices of coverage were calculated using
bamToGFF with parameters -m 50 -e 200 -r -f 1 for the upstream and downstream regions, and -m 150 -e 200 -r -f 1 for
the genic region. Genes with <= 1 RPM-normalized promoter coverage as described above were removed. The values
in each bin were averaged across the genes used, and similarly calculated mean values for corresponding input control
were subtracted from the ChIP signal.
RNA-Seq: Melanomas expressing EGFP or CDK13R860Q in Triples zebrafish were collected. Tissue was disrupted using
QIAshredder columns (Qiagen, 79656). DNA was removed and RNA was purified using columns (Qiagen, 74134).
Ribodepleted RNA libraries were prepped with random priming (NEBNext Ultra RNA Library Prep Kit for Illumina,
E7530) and sequenced on an Illumina HiSeq 2000.
RNA-Seq processing: Sequenced reads were mapped to a custom version of the danRer10 transcriptome where all
chromosomes were included plus human CDK13. Mapping used tophat 2.1.1 (80, 81) with parameters –library-type fr-
unstranded –no-novel-juncs and -G set to a GTF of Ensembl zebrafish genes (v90) that includes human CDK13.
Expression quantification was performed using htseq-count (43) using the same GTF as above and parameters -r name
-i gene_name –stranded=no -f bam -m intersection-strict. Gene-level transcription read counts were then normalized to
transcripts per million (TPM) (counts / bp in exons of all isoforms / 1000 / total counts across all genes / 1000000).
5’ to 3’ RNA-seq gradient analysis of RNA-seq: Bam files from CDK13R860Q (n=5) and EGFP (n=4) melanomas were
used as for 5’ to 3’ of patient sample RNA-seq samples except the zebrafish GRCz10 annotation was used.
3’ sequencing: Melanomas generated from CDK13R860Q (n=3) or EGFP (n=3) from same date of birth were isolated
from approximately equal cell number. Poly-A selection was undertaken (NEB, E7490). Tissue was disrupted (Qiagen,
79654), DNA was removed, and RNA was isolated (Qiagen, 741134). Samples were library prepped for 3’ sequencing
(Lexogen QuantSeq 3’ mRNA-Seq Library Prep Kit REV for Illumina, 016.24) and sequenced via NEXT-seq. Custom
sequencing primer was used and PhiX was avoided per protocol.
3’ sequencing data processing, identification of 3’ cleavage sites: Paired-end reads from 3’ sequencing were mapped
using STAR aligner version 2.7.2a (82). Genome assemblies for human GRCh38 and zebrafish GRCz11 were
downloaded from GENCODE and genome indexes were generated using the -sjbGTFfile flag. After mapping, we used
a custom Python script to filter reads from each BAM file based on the following parameters: 1) Proper mate pairing;
2) orientation of the putative 3’ cleavage end corresponding to the direction of transcription for the gene to which reads
mapped; 3) concordant mapping to known chromosomes; 4) no soft clippings; 5) skipped regions must be longer than
70 nucleotides. Following initial filtering of reads, bedtools cluster tool version 2.26.0 (83)and custom Python scripts
were used to generate read clusters by grouping any 3’ end coordinates that fell within 40 nucleotides of one another
into a single cluster. Clustering was performed on each individual replicate separately. Next, clusters or isolated
individual mapped reads were separated into two categories: those which were present only in one replicate of a
condition (control or CDK13R860Q), and those falling within a 40-nucleotide window in >1 replicate. The latter group
was considered to be bona fide termination sites as opposed to random termination events or mapping errors, and the
vast majority of reads fell within this group (82% for zebrafish and 96% for human). We took these high-confidence
clusters represented in multiple replicates and combined them. The combined set of cleavage sites reads were re-
clustered to define a complete and non-redundant set of 3’ cleavage sites from both conditions.
Quantification of 3’ cleavage site usage: The coordinates of the non-redundant cluster sites were converted into a GTF
for input into DEXseq (43) and run with the BAM files containing individual mapped 3’ sequencing reads from each
replicate for genome wide differential 3’ cleavage site usage analysis. Clusters with a padj < 0.05 were considered to be
significantly differentially utilized between conditions. The clusters were grouped according to whether they fell within
5’ or 3’ UTRs, introns, or exons.
Tandem mass spectrometry: Protein was isolated from EGFP (n=3) and CDK13W878L (n=3) zebrafish melanomas at
week 25.9 weeks post fertilization in RIPA buffer with BME and they were submitted to the Thermofisher Scientific
Center for Multiplexed Proteomics at Harvard Medical School for tandem mass spectrometry with isobaric tags and
synchronous precursor selection based MS3 technology. Peptides are selected for sequencing in MS1 scans. MS2 spectra
are used for identifying peptides, and MS3 spectra are used for quantification via TMT reporter ions. MS2 spectra were
searched using the SEQUEST algorithm against a Uniprot composite database derived from the Danio rerio proteome
containing its reversed complement and known contaminants. Peptide spectral matches were filtered to a 1% false
discovery rate (FDR) using the target-decoy strategy combined with linear discriminant analysis. Proteins were
quantified only from peptides with a summed SN threshold of >=100 and MS2 isolation specificity of 0.7 with
normalization for labeling. Using these parameters, 46,853 peptides with an FDR of <1% were identified which mapped
to 6601 proteins.
Tandem mass spectrometry data analysis: Data were filtered for peptides with unique identification. Peptide location
was determined by dividing the peptide start location by the protein length. Log2 fold change between CDK13W878L and
EGFP was calculated. A D’Agostino and Pearson normality test (p=0.3374) showed data were normal. To plot
proteome-wide changes, individual peptides that had a two-sided t-test p<0.1 were binned and plotted by % protein
length (3676 measurements). Linear regression showed a slope of -0.5349 and the p=0.0001 that the slope was non-
zero. R=-0.5901, p=0.001, best fit slope = -0.5349, Y intercept 0.8483, X intercept 1.586. To identify individual
candidate proteins two methods were used. First, the significantly differentially expressed peptides from above (3676
peptides) that had >1 measurement along the protein and a log2 fold changed slope of >-1 were considered as candidates.
Second, using all unique peptides, any protein with >3 peptide measurements was plotted for slope. Proteins with a
significantly negative slope with an F test (p<0.05) were also included as candidate truncated proteins.
In silico translation of intronic neopeptides: A custom python script was used to predict the peptide sequences
generated from translation of the regions spanning the 5’ splice site of the closest upstream exon (using Gencode exon
coordinates) and the cleavage site clusters. The reading frame of the upstream exon from Gencode annotation was used
to define the reading frame of the intronic sequence, and in silico translation was carried out until a stop codon was
reached. The predicted intronic peptides were added to the standard Danio rerio proteome for SEQUEST search of mass
spectrometry data as above.
Human Cell Line Experiments
Human cell lines: A375 human melanoma cells (ATCC CRL-1619) were identity-verified via STR analysis and then
used for transient transfections for IP-MS or for stable line generation. Mycoplasma testing was done within one week
of every experiment using human cell lines (Lonza, Mycoalert PLUS, LT07-710). All cell lines were mycoplasma
negative. Cells were grown in DMEM supplemented with 10% FBS, penicillin/streptomycin or selection antibiotics,
and L-glutamine.
Cloning: Full-length nuclear isoform of ZC3H14 was obtained from Dharmacon (Accession: BC011793 Clone ID:
4298961). Mutagenesis of ZC3H14 was completed using NEB Site Directed Mutagenesis (NEB, E0554S). Relevant
coding sequences were assembled via the Gateway system into either pLENTI CMV Blast destination vector (Addgene
17451) (84) for stable lines or into pcDNA3.2 C-terminal V5 tag destination vector (ThermoFisher 12489019) for IP-
MS transient transfections.
Stable line generation: CDK13WT, CDK13R860Q, CDK13W878L, CLOVER (fluorescent control), ZC3H14S475A,
ZC3H14S475E, CDK13R860Q + CLOVER, and CDK13R860Q +ZC3H14S475A cell lines were generated via lentiviral
transduction and stable antibiotic selection. Lines were made in biologic triplicate where possible and maintained in
selection antibiotics. Cell counts for CDK13 lines were done at 24, 48, 72, and 96 hours. Cell doubling times were
calculated in exponential growth phase. Antibiotics were removed for cell line growth experiments.
siRNA: Knockdown of ZFC3H1 (Dharmacon, L-020839-02-0005), ZC3H14 (Dharmacon, L-014468-01-0005), or a
control knockdown (Dharmacon, D-001810-01-05) were completed on A375 CLOVER cells and protein or RNA were
collected after 48 hours.
Western blotting: For CDK13 and ZFC3H1 westerns, protein was run on a 3-8% tris acetate gel and wet gel transfer
was performed. For other proteins, 10% tris glycine gels were used with semi-dry transfer. The following antibodies
were used: anti-CDK13 antibody (Sigma HPA 059241), anti-VCL (Sigma HPA 002131), anti-GFP (Santa Cruz sc-
9996), anti-ZFC3H1 (NB100-68267), anti-ZC3H14 (Sigma, HPA 049798), p53 (sc-126), Tubulin (ab6160), GAPDH
(Invitrogen PA1-987), Beta Actin (CST3700), MTR4 (ab70551), CCNT1 (CST 81464), CCNK (Bethyl A301-939A),
V5 (ab27671). N terminal antibodies used in Figure S3 include anti-CDK13 (gift from Arno Greenleaf) and anti-CRBN
(NBP-91810). Rabbit or mouse secondary antibodies were incubated for 1hr at RT (HRP secondaries: CST 7074S or
7076S; or fluorescent secondaries: Licor 926-32211 or 926-68070).IP westerns with HRP secondaries were developed
with Tidyblot (Biorad). Otherwise, westerns were performed as described above for zebrafish.
ChIP-Seq and ChIP-seq analysis: ChIP-seq was completed as above for zebrafish except 40x106 A375 human
melanoma cells expressing CLOVER or CDK13R860Q were used. Raw reads were aligned twice: first to the dm6 revision
of the D. melanogaster genome to remove exogenous spike-in reads using bowtie version 1.2.2 (79) with parameters -k
1 -m 1; unmapped reads were then aligned to the hg19 revision of the human genome with random chromosomes
removed with -k 2 -m 2 and -l set to read length. hg19 RefSeq gene positions included in ROSE
(https://bitbucket.org/young_computation/rose/) were used. The remaining methods were as above for zebrafish ChIP-
seq analysis except genes with <=1 RPM-normalized promoter coverage were included in whole-gene metagenes.
RNA-Seq: For siZFC3H1 (n=3), siZC3H14 (n=3), and siControl (n=3) samples, equal cell numbers were gathered and
ERCC probes were spiked in proportional to cell number. For ZC3H14S475E (n=3), ZC3H14S475A(n=2), and CLOVER
(n=3)-expressing samples, equal RNA amounts were used. RNA-isolation and genomic DNA removal was completed
using a column method as above for zebrafish. All samples were polyA selected (NEB, E7490) and NEBNext Ultra II
Directional RNA Library Prep Kit for Illumina (E7760S) was used. Samples were sequenced on a HiSeq 2500 with
paired end sequencing.
3’ Sequencing: 3’ seq was completed as above for zebrafish melanoma samples for A375 human melanoma cells
expressing: 1) pLENTI CMV CDK13R860Q (n=2), 2) pLENTI CMV CLOVER (n=2), 3) siZFC3H1 (n=3), 4) siZC3H14
(n=3), and 5) siControl (n=3).
RNA-seq/3’ sequencing data processing: Processing was performed as described above for zebrafish (see 3’
sequencing data processing, identification of 3’ cleavage sites) except data were mapped to hg38. As in the zebrafish
analysis, each set of replicates from the different conditions was first processed separately, and then combined to produce
a single set of non-redundant cleavage sites. To enable quantification in samples without available 3’ sequencing, we
performed the quantifications in a different manner. Rather than directly counting reads at each 3’ cleavage site as
before, we used the genomic locations of the combined cleavage site map combined with the RNA-seq splice junctions
to produce a GTF annotating global alternative polyadenylation sites. In the case of intronic polyadenylation sites, the
GTF contains an exon for each intronic site that spans from the 5’ end of the closest upstream exon to the 3’ end of the
cleavage site cluster. In the case of distal poly(A) sites, the exon spans from the 5’ end of the last exon in which the site
is contained, to the 3’ end of the cleavage cluster. DEXseq uses read density over these entire exon regions, rather than
the 3’end sequencing counts, to quantify polyadenylation site differential usage and can thus be performed using
standard poly(A)-selected RNA-seq data. The DEXseq script dexseq_count.py was used to obtain read counts for each
sample using the DEXseq-formatted GTF. DEXseq was then run on each pairwise knockdown or mutant overexpression
with its corresponding control to obtain log2-fold differences and statistical significance at each ptRNA, last exon, and
internal constitutive exon. RNA-seq bam files were visualized using IGV.
Each of the mutant-protein expressing samples from A375 cell RNAseq (ZC3H14 S475A, ZC3H14 S475A +
CDK13 R860Q, and CDK13 R860Q were compared by DEXSeq with the control CLOVER). To account for batch
effects, sequencing date was used as a covariate for the comparisons using the two conditions from the newer batch. To
enable comparison of the same ptRNA events across all conditions, the log2 fold-changes for events that were significant
for ZC3H14 S475A versus CLOVER were plotted in a scatterplot. The Pearson product-moment correlation coefficients
were calculated using R.
ddPCR: Equal cell numbers were collected from CDK13R860Q and CLOVER-expressing biologic duplicate lines.
Genomic DNA was removed, and RNA was isolated via columns (Qiagen 74134). PolyA selection was performed
(E7490 protocol) and cDNA was made (Thermofisher, 18080400). CDK13 concentration was measured from
CDK13R860Q-expressing and control human melanoma cells to verify CDK13R860Q expression with and without reverse
transcriptase to ensure genomic DNA elimination. ddPCR was completed with FAM probes designed to the first (or
second) and last exon of 4 genes with ptRNAs and 2 genes without ptRNAs. Thresholding was completed manually.
CDK13R860Q RNA concentration was divided by control CLOVER RNA concentration for each target. Measured cDNA
concentration was normalized to negative-control AGPAT’s last exon.
IP-mass spectrometry: Constructs were transiently transfected (Thermofisher, L3000008) in 15cm2 plate with
replicates into either A375s or CDK13R860Q expressing A375s. 48 hours after transfection, nuclei were isolated
(Thermofisher 78833) and lysed. Anti-V5 (Clone V5-10, V8012 Sigma) was conjugated to protein G beads
(Thermofisher 10004D). IPed proteins were eluted and submitted for mass spectrometry using the Taplin Mass
Spectrometry Facility at Harvard University. Proteins from the CDK13 pulldown experiment were included in analysis
if all replicates had >1 peptide and the CDK13 WT IP identified >3x signal over the control IP. For the ZC3H14 IP,
proteins were filtered if they had at least 4 peptides in each ZC3H14 replicate and were >3x enriched over control IP
(all control IPs were combined). Statistics were done using multiple t-tests assuming similar scatter using Prism.
ZC3H14 phosphorylation sites were reported if they were identified in all three biologic replicates with either 1)
modification score >10 or 2) >2 peptides calling the same site. Spectra are shown for the S475 phosphorylation which
is missing in the CDK13R860Q condition.
TT-seq and paired RNA-seq: Ribosome-depleted RNA-seq and TT-seq were executed on equal numbers of human
melanoma cells collected at the same time from pLENTI CMV CLOVER (n=3) and pLENTI CMV CDK13R860Q (n=3)
with spike-in ERCC probes added proportionally to cell number (RNA-seq and TT-seq) (Thermofisher, 4456740) and
4sU labeled Drosophila S2 cell RNA (just TT-seq). RNA was collected in Trizol per standard protocol. TT-seq 4sU
pulse was 5 min and is otherwise as published (44). NEBNext Ultra II Directional RNA Library Prep Kit for Illumina
(E7760S) was used for library prep and samples were sequenced with paired end sequencing on a HiSeq 2500.
TT-seq analysis: Gene Annotations: Using kallisto (85) ribosome-depleted RNA-seq in control and CDK13R860Q A375s
were aligned to Gencode v26 ‘basic’ annotations. Linearly grouped annotated transcript start sites (TSSs) within 100 bp
were clustered, assigned a sum of the transcripts per million (TPM) values across isoforms, and the highest expression
cluster was selected as the dominant TSS cluster. For clusters containing multiple TSSs, the highest-expressed TSS was
selected as the dominant TSS. For transcripts stemming from the dominant TSS cluster, we clustered the annotated
transcript end sites (TESs) within 100 bp, summed the TPM values, and selected the dominant TES cluster. For clusters
containing multiple TESs, the highest-expressed TES was selected as the dominant transcript. We removed overlapping
transcripts (on the same strand and within 1 kb of another transcript) and selected protein coding transcripts greater than
1 kb with a detected 3’ cleavage location within 1 kb of the annotated TES for further study (7452 transcripts in total).
RNA-seq and TT-seq mapping: We aligned RNA-seq and TT-seq data to hg38 and to the transcriptome (Gencode v26
‘basic’ annotations) with STAR (82). For data with spike-ins, we also aligned to the spike-in genomes, but as we
observed no statistically significant difference in percent spike-in reads we depth normalized both the RNA-seq and TT-
seq data.
Transcriptome metaplots: For transcriptome metaplots, we split transcripts into 100 equally sized bins and plotted the
transcriptome-aligned data over the dominant transcripts (n=7452). For TSS and TES flanking regions, we plotted +/- 1
kb from the hg38 alignments.
TES 3’ cleavage locations metaplots and boxplots: For TES metaplots, RNA-seq and TT-seq reads in 10 nt bins were
aligned by the closest 3’ cleavage locations and the average coverage in each bin was plotted. Genes used for this
analysis were those with greater than 50 reads in 3’ end sequencing located at a 3’ end cluster within 1 kb of the dominant
TES (n=6740). For TES boxplots, read coverage in each bin was summed from -400 to -100 and +100 to +400 from
each 3’ cleavage location. Any gene with 0 reads in the upstream or downstream window, in either control or CDK13
mutant cells were removed from these analyses. This resulted in analysis of 5775 and 6083 3’ end locations for the
RNA-seq and TT-seq data respectively.
Upregulated intronic 3’ cleavage locations metaplots and boxplots: 3’ cleavage locations located within dominant
transcript introns and at least 400 nt away from the nearest exon were filtered for those containing more than 20 3’ reads.
3’ cleavage locations with significantly higher signal in CDK13 mutant cells (q<0.1) from 3’ sequencing were used.
Regions without read coverage in RNA-seq or TT-seq were removed. This resulted in n=134 3’ cleavage locations for
analysis. For metaplots, RNA-seq and TT-seq data were aligned to the 3’ cleavage location and the average coverage in
each 40 nt bin is shown. For boxplots, mean read coverage was summed from -300 to -1 and +1 to +300 nt with respect
to 3’ cleavage locations.
Mouse Embryonic Stem Cells:
Cell culture and cell line generation: All cell lines were tested for mycoplasma contamination periodically via the
MycoAlert Mycoplasma Testing Kit (Lonza). Results were always negative for mycoplasma contamination. V6.5
(C57Bl/6-129) mESCs and derived cell lines were cultured on 0.2% gelatin-coated tissue culture plates in ES media:
Dulbecco’s Modified Essential Medium buffered with 10 mM HEPES and supplemented with 15% Fetal Bovine Serum,
1000 U/mL leukemia inhibitory factor, 1x non-essential amino acids, 2 mM L-glutamine, 0.11 mM ß-mercaptoethanol,
100 IU penicillin, and 100 µg/mL streptomycin.
Cdk13∆ clones were generated using CRISPR/Cas9 as follows. sgRNAs targeting intron 3 and intron 4 of the
endogenous Cdk13 locus were cloned into pX458 (Addgene plasmid #48138) (Ran et al., 2013) or pX330 (Addgene#
42230) (86) respectively (see Table S8 for sequences). Two independent pairs of sgRNAs (targeting intron 3 and 4,
respectively) were co-transfected into wildtype V6.5 mouse embryonic stem cells (Thermofisher, 11668027), and
single-cell sorted for GFP+ fluorescence (transfected cells) 24 hours after transfection. Clones were screened for
homozygous deletion of exon 4 by PCR and confirmed by Sanger sequencing. Knockout of endogenous Cdk13 was
confirmed by Western blot. One knockout clone from each sgRNA pair was used throughout the study to control for
off-target effects.
A doxycycline (Dox)-inducible Cdk13 transgene was stably introduced into the two Cdk13∆ clones used throughout
this studying using a piggybac retrotransposon system. N-terminal Flag- HA- tandem epitope-tagged Cdk13
(NP_001074527.1 isoform) was cloned via overlap extension PCR using two templates: (1) a synthetic gene block
containing the codon-optimized N-terminus of Cdk13 (first 1577 base pairs) to reduce the high GC content in the region
and (2) polyA-selected mouse cDNA from V6.5 cells. This PCR product was cloned into pCR8/GW/TOPO
(Thermofisher) followed by transfer into the Dox-inducible piggybac expression vector, PBNeoTetO-Dest (a gift from
A.W. Cheng), using standard TOPO and Gateway cloning kits (Thermofisher). The final Cdk13 transgene sequence is
provided in Data S1. This expression vector was co-transfected with pAC4 (constitutively expressing M2rtTA, the Dox-
inducible transactivator, flanked by piggybac recombination sites, A.W. Cheng) and mPBase (piggybac transposase
expression plasmid, A.W. Cheng). 24 hours after transfection, cells were selected with hygromycin and G418, and single
cell cloned. Clones were screened for near wild-type levels of CDK13 expression upon addition of 1 µg/mL Dox for 24
hours. Two clones (one from each sgRNA pair used for knockout) were used throughout the study.
Western blotting: Whole cell extract was harvested. Normalized lysates were run on NuPAGE 4-12% Bis-Tris Gels
(Thermofisher). Gels were transferred overnight (30 V) to PVDF in 10% methanol supplemented 1x NuPAGE Transfer
Buffer (NuPAGE Bis-Tris Gels). Primary antibodies used for blotting: Anti-HA High Affinity Antibody (Roche
11867423001), CDK13 (a gift from Arno L. Greenleaf), Enolase I (CST 3810S), alpha-tubulin (Genescript a01410).
Secondary antibodies used: ECL Anti-Rat IgG (GE Healthcare NA935V), ECL Anti-Mouse IgG (GE Healthcare
NA931V), and ECL Anti-Rabbit IgG (GE Healthcare NA934V).
RNA-Seq: Two independent Cdk13 clones with Dox-inducible Cdk13 were pre-treated with 1 µg/mL Dox daily for
at least 5 days prior to the start of the time course to express complementing levels of Cdk13 transgene in the Cdk13
background. Dox was withdrawn from these cells at time 0, which resulted in significant knockdown and undetectable
levels of CDK13 after 48- or 72- hours respectively. RNA was harvested in biological duplicate from both independent
clones from cells maintained in Dox at time 0 (+Cdk13) or withdrawn from Dox for 48 or 72 hours using Trizol and
then DNase treated. PolyA-selected libraries were made using the TruSeq Stranded mRNA Library Prep Kit (Illumina
RS-122-2102), and sequenced (75 base pair, paired-end reads) on one flow cell of an Illumina NextSeq500.
5’ to 3’ RNA-seq gradient analysis: The protocol was conducted as for patient data.
Euler plots: Overlapping mapped intronic polyadenylation sites (IPAs) quantified by DEXseq in the Cdk12 from (7)
and Cdk13-depleted mESCs were identified using Bedtools (83). Overlapping IPA sites that were significantly decreased
(220 sites) or increased (712 sites) in either or both Cdk12/13 depletions in the same direction were counted, and the
proportional Euler diagram was produced in R using the package eulerr 6.1.1 (Area-proportional Euler and Venn
Diagrams with Ellipses) in R version 3.6.3 (87).
Fig. S1.
CDK13 mutations are selected for in cancer.
A) CDK13 mutational frequency in melanoma collected from cBioPortal and ICGC. B) Distributions of variant allele
fraction for copy neutral somatic mutations in five patient melanomas. Blue = CDK13 mutations. Red = known driver
mutations. C) CDK13 mutational frequency in non-melanoma cancers. D-E) Overall patient survival from the TCGA
cohort with CDK13 low (D) or CDK13 mutated (E). F) Survival plot for patients with somatic CDK13 mutation or
CDK13 downregulation (z < or = -1.0) initially staged as 0/1/2 vs. remaining patients initially staged 0/1/2. p=0.0012.
Log-rank. n= patients. G) In vitro kinase assay using wild type and patient-mutated CDK13 activated by CCNK on c-
Myc substrate. One-way ANOVA with no kinase vs. all conditions; WT CDK13 ****=q=0.0001, all mutated CDK13
comparisons non-significant. Mean +/-SD. n=2 replicates. Right side = CDK13/CCNK after size exclusion
chromatography run on SDS-PAGE showed CDK13 maintained CCNK binding. H-K) Light micrographs from 3 days
post fertilization (dpf) Triples zebrafish injected with melanocyte-specific H) control CRISPR, I) cdk13 CRISPR, J)
overexpression of human CDK13WT, K) cdk13 CRISPR and overexpression of human CDK13WT. Scale bars = 100 µm.
L) % PCR reads across CRISPR cut predicted to maintain cdk13 function (in-frame). p=0.017 (t-test, two tailed). Mean
+/- SD. n=melanomas. M) Representative PH3 staining image from cdk13 and control melanocyte-specific CRISPR in
Triples zebrafish melanomas. Scale bars=200 m. N) Quantification of pigmentation patterns of 9-week-old Triples
zebrafish from Figure 1H with melanocyte-specific expression of EGFP, CDK13WT, patient-mutated CDK13, or control
catalytically dead CDK13K734R. White=no melanocytes, light gray = 0-33% zebrafish length with melanocytes, dark
gray = >33% zebrafish length with melanocytes, black = black patch. (n)=zebrafish. O) Melanoma-free survival curves
of EGFP and patient-mutant CDK13 melanomas. p<0.0001 for each comparison (log rank). (n)=zebrafish. P)
Immunoblot with anti-CDK13 and anti-GFP on protein from zebrafish melanomas from Figure 1I. n=2 zebrafish
melanomas. Q) Representative PH3 IHC image from EGFP- and CDK13W878L- expressing zebrafish melanomas. Scale
bars=200 m. R) Melanoma-free survival of zebrafish with melanocyte-specific CDK13W878L-expression and
melanocyte-specific CRISPR of a control gene or ccnK. p<0.0001 (log-rank). (n)=zebrafish. S) Melanoma-free survival
of zebrafish with melanocyte-specific CRISPR of a control gene or ccnK. ns=non-significant (log-rank). (n)=zebrafish.
T) % CRISPR insertion/deletions predicted to cause loss of function from zebrafish melanomas with expression of
CDK13R860Q + control gRNA, CDK13R860Q + ccnT1 gRNA, or CDK13R860Q + ccnK gRNA. Unpaired t-test, two tailed,
non-significant. Mean +/-SD. (n)=melanomas. U) Melanoma-free survival of Triples zebrafish with melanocyte-specific
CDK13R860Q expression and melanocyte-specific CRISPR of either a control gene or ccnT1. p=0.0002, log rank.
(n)=zebrafish. V) Anti-CDK13 and anti-GFP immunoblot on protein from CDK13 and CLOVER-expressing A375
melanoma cells. n=3 independently derived lines.
Fig. S2.
Characterization of CDK13/Cdk13 mutation/loss of function models for RNA analysis.
A) IGV image from zebrafish melanoma RNA-seq confirming mutant human CDK13 expression. B) Schematic for
generation of Cdk13-/- mouse embryonic stem cells (mESCs) with doxycycline-inducible Cdk13-HA complementation.
C) Representative immunoblot showing 4 mESC clones with loss of Cdk13. Orange=gRNA pair 1. Red=gRNA pair 2.
D) Representative immunoblot from a Cdk13 mutant clone with Cdk13-HA complementation at baseline and upon
doxycycline withdrawal. E) Overlap between Cdk12-/- and Cdk13-/- intronic polyadenylation sites detected in mouse
ES cells. F-G) IGV plots of upregulated intronic polyadenylation (IPA) site in F) CBFB and G) TP53. Red box =
upregulated intronic polyadenylation site in CDK13mut cells. H) CDK13 RNA expression from control CLOVER-
expressing (CDK13WT) or CDK13mut-expressing human melanoma cells as measured by ddPCR. RT = reverse
transcriptase. +/- SD.
Fig. S3.
CDK13 mutants have intact transcriptional elongation and translate prematurely terminated RNAs.
A) log2-fold normalized exon coverage from RNA-seq from CDK13mut- (n=3) vs. CLOVER-expressing (n=3) human
melanoma cells. Exons shown are from 7328 non-overlapping multi-exon transcripts, containing 72732 internal exons.
Two-sided Wilcoxon rank sum test. ****=p<2.2x10-16, F vs. L exon. For all box plots the horizontal line indicates the
median and whiskers extend to 1.5 x the interquartile range. B-C) Metagene plots of read coverage from TT-seq B) and
RNA-seq C) in CLOVER- (n=3) and CDK13mut- (n=3) expressing A375 human melanoma cells. Shown are the regions
flanking the 3’ cleavage location closest to the annotated TES at expressed, non-overlapping protein-coding genes.
Genes without read coverage in windows indicated were removed (TT-seq n=6083; RNA-seq n=5775). D) Average
RNA-seq read coverage surrounding intronic 3’ cleavage locations enriched in CDK13mut 3’sequencing (q<0.01) and
400 bp from the nearest exon from CLOVER- (n=3 biologic replicates) and CDK13R860Q-expressing (n=3 biologic
replicates) human melanoma cells (n=134 loci quantified). E) TT-seq and RNA-seq coverage plot for example gene
TP53. F-I) ChIP-seq metagenes for F) anti-RNAPII and G) anti-Ser2P RNAPII from human melanoma cells and H)
anti-RNAPII and I) anti-Ser2P RNAPII from zebrafish melanomas. RPM=reads per million. Two-tailed t-test using
RPM normalized values for transcriptional start site (TSS) +/- 1 kilobase and gene body (25%-75% of gene body). J)
Input-normalized ChIP-seq metagenes for RNAPII and anti-Ser2P RNAPII in control and CDK13mut conditions for
human melanoma cells (left) and zebrafish melanomas (right). K) Log2 fold change Tandem mass spectrometry protein
measurements CDK13mut/EGFP on the horizontal axis vs. -log p-value (t-test, two tailed) vertical axis. Red = lysosomal
and autophagic proteins. Blue = COP-I vesicle transport proteins. L) Heatmaps of proteins with evidence of truncation
in zebrafish CDK13mut as compared with EGFP melanomas. Left = heatmap of log2 CDK13mut vs. control slope
calculated from peptide measurements plotted along % protein length to identify truncated protein candidates. Right =
heatmap of F value (degree of significance) (p<0.05). M) Log2 CDK13mut- vs. EGFP-expressing zebrafish melanoma
peptide measurements plotted by % protein length for significantly affected proteins for Ikbkb (upper) and Idh2 (lower).
