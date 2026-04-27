---
source_path: /mnt/c/Users/Administrator/Zotero/storage/8PBNI6C8/Wang 等 - 2024 - rMATS-turbo an efficient and flexible computational tool for alternative splicing analysis of large.pdf
ingested: 2026-04-23
sha256: 7b078e937111cbfd
---

nature protocols https://doi.org/10.1038/s41596-023-00944-2
Protocol Check for updates
rMATS-turbo: an efficient and flexible
computational tool for alternative splicing
analysis of large-scale RNA-seq data
Yuanyuan Wang1,2,6, Zhijie Xie 2,6, Eric Kutschera 2, Jenea I. Adams 2,3, Kathryn E. Kadash-Edmondson 2 & Yi Xing 2,4,5
Abstract Key points
Pre-mRNA alternative splicing is a prevalent mechanism for diversifying • This protocol provides detailed
guidelines for using rMATS-turbo,
eukaryotic transcriptomes and proteomes. Regulated alternative splicing
the latest implementation of
plays a role in many biological processes, and dysregulated alternative splicing the popular software for the
discovery and quantification
is a feature of many human diseases. Short-read RNA sequencing (RNA-seq) is
of alternative splicing events
now the standard approach for transcriptome-wide analysis of alternative
from RNA sequencing data.
splicing. Since 2011, our laboratory has developed and maintained Replicate The software is exemplified in
two representative scenarios.
Multivariate Analysis of Transcript Splicing (rMATS), a computational tool
for discovering and quantifying alternative splicing events from RNA-seq • rMATS-turbo incorporates
a revamped computational
data. Here we provide a protocol for the contemporary version of rMATS,
workflow with a substantial
rMATS-turbo, a fast and scalable re-implementation that maintains the improvement in speed and data
statistical framework and user interface of the original rMATS software, storage efficiency. The software
scales up to massive RNA
while incorporating a revamped computational workflow with a substantial
sequencing datasets with tens
improvement in speed and data storage efficiency. The rMATS-turbo software of thousands of samples.
scales up to massive RNA-seq datasets with tens of thousands of samples.
To illustrate the utility of rMATS-turbo, we describe two representative
Key references
application scenarios. First, we describe a broadly applicable two-group
comparison to identify differential alternative splicing events between two
Phillips, J. W. et al. Proc. Natl
sample groups, including both annotated and novel alternative splicing events.
Acad. Sci. USA 117, 5269–5279
Second, we describe a quantitative analysis of alternative splicing in a large-scale (2020): https://doi.org/10.1073/
pnas.1915975117
RNA-seq dataset (~1,000 samples), including the discovery of alternative
splicing events associated with distinct cell states. We detail the workflow and Shen, S. et al. Proc. Natl Acad.
Sci. USA 111, E5593–E5601
features of rMATS-turbo that enable efficient parallel processing and analysis
(2014): https://doi.org/10.1073/
of large-scale RNA-seq datasets on a compute cluster. We anticipate that this pnas.1419161111
protocol will help the broad user base of rMATS-turbo make the best use of this
software for studying alternative splicing in diverse biological systems.
1Bioinformatics Interdepartmental Graduate Program, University of California, Los Angeles, Los Angeles, CA, USA.
2Center for Computational and Genomic Medicine, The Children’s Hospital of Philadelphia, Philadelphia, PA, USA.
3Genomics and Computational Biology Graduate Program, University of Pennsylvania, Philadelphia, PA, USA.
4Department of Pathology and Laboratory Medicine, University of Pennsylvania, Philadelphia, PA, USA. 5Department
of Biomedical and Health Informatics, The Children’s Hospital of Philadelphia, Philadelphia, PA, USA. 6These authors
contributed equally: Yuanyuan Wang, Zhijie Xie. e-mail: xingyi@chop.edu
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1083
Protocol
Introduction
Alternative splicing is a prevalent RNA regulatory mechanism for diversifying the transcriptomic
and proteomic output of eukaryotic cells1. During the splicing of precursor mRNA, introns are
removed and exons are joined together to generate mature mRNA product2. Alternative choices
of exons and splice sites during pre-mRNA splicing (i.e., alternative splicing) can therefore
generate multiple mRNA isoforms from a single gene. Alternative splicing is controlled by
cis-acting splicing regulatory elements within the pre-mRNA and trans-acting splicing factors
that interact with these cis elements3,4. Regulated alternative splicing plays a role in many
biological processes, such as cell differentiation and tissue development5,6. Dysregulated
alternative splicing is a feature of many human diseases and frequently contributes to disease
pathogenesis and progression7.
RNA sequencing (RNA-seq) on massively parallel sequencers is now the standard approach
for transcriptome analysis8. Contemporary short-read sequencers are capable of generating
tens to hundreds of millions of RNA-seq reads at a modest cost, allowing transcriptome-wide
discovery and quantification of alternative splicing events on any RNA sample9. Three classic
papers in 2008 demonstrated the utility of RNA-seq for alternative splicing analysis10–12. In
the past decade, various computational tools have been developed for analyzing alternative
splicing using RNA-seq data (summarized in refs. 9,13,14). Although early RNA-seq studies
of alternative splicing were limited to a small number of conditions and samples, it is now
routine for a single RNA-seq study to examine tens to hundreds of samples15. Large-scale
genomics projects, such as The Cancer Genome Atlas (TCGA) program and the Genotype-Tissue
Expression (GTEx) project, have generated and released RNA-seq data on tens of thousands of
samples16,17. Therefore, there is a need for computational tools that can efficiently extract and
analyze alternative splicing profiles from large-scale RNA-seq datasets.
We previously developed Replicate Multivariate Analysis of Transcript Splicing (rMATS),
a statistical model and software program for quantifying alternative splicing and identifying
differential alternative splicing events between two groups of RNA-seq samples with
replicates18. rMATS uses a generalized linear mixed model to simultaneously consider the
following: (1) splicing levels of an alternative exon or splice site in individual samples, often
denoted as ‘percent spliced in’ or PSI (Ψ) values19, (2) estimation uncertainty of PSI, which is
influenced by RNA-seq read coverage for a given event in a given sample and (3) variability in
PSI values among replicates. Since its release, rMATS has been widely used by the research
community, including being adopted as the splicing analysis tool in the ENCODE 3 RNA flagship
paper20. However, the original rMATS software was developed at a time when a typical RNA-seq
study would involve a small number of samples. The software was computationally inefficient
and did not scale well to large-scale datasets.
To address the need for analyzing massive RNA-seq datasets (e.g., tens of thousands of
samples), we redesigned the workflow and refactored the rMATS software. The resulting
contemporary version of rMATS—called rMATS-turbo, i.e., rMATS version 4.0.1 or above—
maintains the statistical framework and user interface of the original rMATS software but has
substantial improvements in speed and data storage efficiency. The rMATS-turbo software
was initially released in 2017 (version 4.0.1), and the open-source versions (version 4.1.0 and
above) have been available in GitHub since 2020 (https://github.com/Xinglab/rmats-turbo).
Due to its high computational efficiency, we and many other users of rMATS have transitioned
to rMATS-turbo, as evidenced by numerous publications that used the rMATS-turbo software
(for a small number of representative examples, see refs. 21–30). However, the workflow and
features of rMATS-turbo have not been systematically introduced in any publication. Therefore,
the goal of this article is to provide a detailed protocol of rMATS-turbo, helping its many users
make the best use of this software for studying alternative splicing in diverse biological systems.
Applications of rMATS-turbo
The rMATS-turbo software is a general-purpose computational tool for analyzing alternative
splicing using short-read RNA-seq data. It can work with large-scale RNA-seq datasets with
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1084
Protocol
thousands to tens of thousands of samples, to discover and quantify alternative splicing events
corresponding to all major types of alternative splicing patterns. When provided with two
groups of RNA-seq samples, each with multiple (three or more) replicates, rMATS-turbo can
identify differential alternative splicing events between the groups. The two groups could
represent different biological conditions (e.g., normal versus diseased tissue, treatment
versus control). Gene set and pathway enrichment analysis could be performed to identify the
gene sets and pathways affected by alternative splicing27. Moreover, the alternative splicing
profiles generated by rMATS-turbo, including the RNA-seq read counts and estimated PSI
values for alternative splicing events, can be used for customized downstream analyses
when incorporating complex design matrices, such as identifying alternative splicing events
associated with disease progression27, or identifying splicing quantitative trait loci using
population-scale genotype and RNA-seq data31. Importantly, rMATS-turbo is organism agnostic
and has been applied to diverse animals and plants21–30.
Overview of the rMATS-turbo workflow
Figure 1 provides an overview of the rMATS-turbo computational workflow. rMATS-turbo uses
an efficient weighted splicing graph data structure and its associated data format (.rmats)
to store splicing information extracted from raw RNA-seq data. In the splicing graph, exons
are represented as nodes, and splice junctions are represented as edges, with edge weights
corresponding to RNA-seq read counts for individual splice junctions32,33. rMATS-turbo has
two steps, ‘prep’ and ‘post’. In the prep step, input files (.FASTQ or .BAM) are processed and
transformed into splicing graphs, and an .rmats file is saved to store information of weighted
splicing graphs for each RNA-seq sample. In the post step, .rmats files are read and integrated
across samples to discover and quantify alternative splicing events. Five basic types of
alternative splicing patterns are discovered and analyzed: skipped exon (SE), alternative
5′ splice sites (A5SS), alternative 3′ splice sites (A3SS), mutually exclusive exons (MXE) and
retained intron (RI) (Supplementary Fig. 1). The post step also incorporates a statistical model,
as introduced in the original rMATS paper18, for identifying differential alternative splicing
events between two sample groups. The prep step can be run independently or in parallel on
different subsets of input files. The post step can combine independently generated .rmats files,
allowing computations to be run at different times or on different compute nodes. New samples
can be easily added to an analysis by only having to re-run the post step to integrate existing
and newly generated .rmats files. Box 1 provides a detailed description of the command line
arguments of rMATS-turbo, including the argument for running the prep and post steps.
In summary, the decoupled two-step process for prep and post steps is an essential novel
feature of rMATS-turbo. Through the parallel processing of input FASTQ or BAM files by
separate prep steps and a summarizing post step, rMATS-turbo is remarkably competent for
alternative splicing analysis of large-scale RNA-seq data, as shown in numerous publications21–30
and in the detailed usage examples below.
Development of the protocol
The rMATS-turbo software can discover and quantify alternative splicing events corresponding
to the five basic alternative splicing patterns (Fig. 1). To quantify alternative splicing, rMATS-turbo
adopts the widely used PSI (or Ψ) metric19. Specifically, PSI represents the percentage of
transcripts that include a specific exon or splice site, as calculated from RNA-seq read counts
supporting specific exons or splice junctions, normalized by the effective lengths of distinct
transcript isoforms (e.g., exon included versus skipped). For example, for an SE event, PSI can be
calculated from the following formula:
I
Ψ=
lI
I S
+
lI lS
where I and S represent read counts for the exon inclusion isoform and exon skipping isoform,
respectively, and l and l represent the effective lengths for the exon inclusion isoform and
I S
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1085
Protocol
exon skipping isoform, respectively. Supplementary Fig. 1 provides a detailed illustration of
the supporting RNA-seq reads, as well as the calculation of effective lengths and PSI values for
different alternative splicing patterns. Each alternative splicing pattern has a corresponding set
of output files, which are described in Box 2. The PSI values of alternative splicing events can be
used for customized downstream analyses, such as sample clustering and correlation tests with
qualitative or quantitative features.
Although rMATS-turbo maintains the statistical framework and user interface of the
original rMATS software, the software is substantially optimized and incorporates numerous
new features to improve its computational efficiency and expand its functionalities. Notable
features of rMATS-turbo include the following:
1. The dramatic improvement of rMATS-turbo in computational efficiency and flexibility
over the original rMATS implementation is enabled by a two-step procedure (prep and
post) for RNA-seq data processing and analysis (Fig. 1). Specifically, by using the ‘--task
prep’ and ‘--task post’ options, rMATS-turbo can process RNA-seq files individually via the
prep step, and then summarize the alternative splicing profiles across all RNA-seq files via
the post step. Decoupling the prep and post steps has two main benefits. First, individual
RNA-seq files can be processed in parallel in the prep step. This feature is particularly
useful for large-scale datasets, as the prep step can be run on distinct subsets of RNA-seq
files in a distributed manner over a compute cluster. Second, new RNA-seq samples can be
conveniently added to an ongoing analysis. The discovery of alternative splicing events
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1086
pets
perP
pets
tsoP
Parallel processing of FASTQ/BAM files Fig. 1 | An overview of the rMATS-turbo workflow to discover and quantify
FASTQ (optional) alternative splicing events in large-scale RNA-seq datasets. rMATS-turbo
uses an efficient weighted splicing graph data structure and its associated data
format (.rmats) to store splicing information extracted from raw RNA-seq data.
FASTQ FASTQ FASTQ rMATS-turbo has two main steps, ‘prep’ and ‘post’. In the prep step, input files
(.FASTQ or .BAM) are processed and transformed into splicing graphs. Note that
users can either start from FASTQ files or from pre-aligned BAM files. An .rmats
file is saved to store information of weighted splicing graphs for each RNA-seq
sample. The prep step can be run independently or in parallel on different subsets
of input files. In the post step, .rmats files are read and integrated across samples
to discover and quantify alternative splicing events. Five basic types of alternative
splicing patterns are discovered and analyzed: SE, A5SS, A3SS, MXE and RI.
BAM BAM BAM The post step also incorporates a statistical model for identifying differential
alternative splicing events between two sample groups.
.rmats .rmats .rmats
Alternative splicing detection and quantification
Skipped exon
Alternative 5′ splice sites
Alternative 3′ splice sites
Mutually exclusive exons
Retained intron
Protocol
Box 1
Description of command line arguments of rMATS-turbo
-h, --help Show this help message and exit
--version Show program’s version number and exit
--gtf GTF An annotation of genes and transcripts in GTF format
--b1 B1 A text file containing a comma separated list of the BAM files for sample_1. (Only if using BAM)
--b2 B2 A text file containing a comma separated list of the BAM files for sample_2. (Only if using BAM)
--s1 S1 A text file containing a comma separated list of the FASTQ files for sample_1. If using paired reads
the format is “:” to separate pairs and “,” to separate replicates. (Only if using fastq)
--s2 S2 A text file containing a comma separated list of the FASTQ files for sample_2. If using paired
reads the format is “:” to separate pairs and “,” to separate replicates. (Only if using fastq)
--od OD The directory for final output from the post step
--tmp TMP The directory for intermediate output such as “.rmats” files from the prep step
-t {paired,single} Type of read used in the analysis: either “paired” for paired-end data or “single” for single-end
data. Default: paired
--libType {fr-unstranded, Library type. Use fr-firststrand or fr-secondstrand for strand-specific data. Only relevant to the
fr-firststrand,fr-secondstrand} prep step, not the post step. Default: fr-unstranded
--readLength READLENGTH The length of each read. Required parameter, with the value set according to the RNA-seq read
length
--variable-read-length Allow reads with lengths that differ from --readLength to be processed. --readLength will still be
used to determine IncFormLen and SkipFormLen
--anchorLength ANCHORLENGTH The “anchor length” or “overhang length” used when counting the number of reads spanning
splice junctions. A minimum number of “anchor length” nucleotides must be mapped to each
end of a given splice junction. The minimum value is 1 and the default value is set to 1 to make
use of all possible splice junction reads
--tophatAnchor TOPHATANCHOR The “anchor length” or “overhang length” used in the aligner. At least “anchor length” nucleotides
must be mapped to each end of a given splice junction. The default is 6. (Only if using fastq)
--bi BINDEX The directory name of the STAR binary indices (name of the directory that contains the suffix
array file). (Only if using fastq)
--nthread NTHREAD The number of threads. The optimal number of threads should be equal to the number of
CPU cores. Default: 1
--tstat TSTAT The number of threads for the statistical model. If not set then the value of --nthread is used
--cstat CSTAT The cutoff splicing difference. The cutoff used in the null hypothesis test for differential
alternative splicing. The default is 0.0001 for 0.01% difference. Valid: 0 ≤ cutoff < 1. Does not
apply to the paired stats model
--task {prep,post,both,inte,stat} Specify which step(s) of rMATS-turbo to run. Default: both. prep: preprocess BAM files and
generate .rmats files. post: load .rmats files into memory, detect and count alternative splicing
events, and calculate P value (if not --statoff). both: prep + post. inte (integrity): check that the
BAM filenames recorded by the prep task(s) match the BAM filenames for the current command
line. stat: run statistical test on existing output files
--statoff Skip the statistical analysis
--paired-stats Use the paired stats model
--novelSS Enable detection of novel splice sites (unannotated splice sites). Default is no detection of novel
splice sites
--mil MIL Minimum Intron Length. Only impacts --novelSS behavior. Default: 50
--mel MEL Maximum Exon Length. Only impacts --novelSS behavior. Default: 500
--allow-clipping Allow alignments with soft or hard clipping to be used
--fixed-event-set A directory containing fromGTF.[AS].txt files to be used instead of detecting a new set of events
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1087
Protocol
Box 2
Output files of rMATS-turbo
In rMATS-turbo, each alternative splicing pattern has a corresponding – FDR: false discovery rate calculated from P value (only available
set of output files. In the filename templates below, [AS_Event] is if statistical model is on)
replaced by one of the five basic alternative splicing patterns: SE, – IncLevel1: inclusion level for sample 1. Replicates are comma
A5SS, A3SS, MXE or RI. As shown in Supplementary Fig. 1, the number separated. Calculated from normalized counts
of supporting reads can be counted by the junction reads only (JC) – IncLevel2: inclusion level for sample 2. Replicates are comma
or by both the junction and exon reads (JCEC). The output files from separated. Calculated from normalized counts
different counting methods are also indicated in the file name. – IncLevelDifference: average(IncLevel1) −
--od contains the final output files from the post step: average(IncLevel2)
• [AS_Event].MATS.JC.txt: final output that contains the list of • Event specific columns (event coordinates):
events and read counts. Only splice junction reads are counted – SE: exonStart_0base exonEnd upstreamES upstreamEE
• [AS_Event].MATS.JCEC.txt: final output that contains the list downstreamES downstreamEE. The inclusion form includes
of events and read counts. Both splice junction reads and exon the target exon (exonStart_0base, exonEnd)
body reads are counted – MXE: 1stExonStart_0base 1stExonEnd
• fromGTF.[AS_Event].txt: all identified alternative splicing (AS) 2ndExonStart_0base 2ndExonEnd upstreamES
events derived from the GTF file and RNA-seq data upstreamEE downstreamES downstreamEE. If the
• fromGTF.novelJunction.[AS_Event].txt: AS events derived strand is +, then the inclusion form includes the first exon
from novel combinations of splice sites annotated in the GTF file. (1stExonStart_0base, 1stExonEnd) and skips the second
Does not include events with an unannotated splice site exon. If the strand is –, then the inclusion form includes the
• fromGTF.novelSpliceSite.[AS_Event].txt: this file second exon (2ndExonStart_0base, 2ndExonEnd) and skips
contains only events that include an unannotated splice site. Only the first exon
relevant if --novelSS is enabled – A3SS, A5SS: longExonStart_0base longExonEnd
• JC.raw.input.[AS_Event].txt: event counts including only shortES shortEE flankingES flankingEE. The inclusion
reads that span junctions defined by rMATS form includes the long exon (longExonStart_0base,
• JCEC.raw.input.[AS_Event].txt: event counts including longExonEnd) instead of the short exon (shortES, shortEE)
both reads that span junctions defined by rMATS and reads that – RI: riExonStart_0base riExonEnd upstreamES
do not cross an exon boundary upstreamEE downstreamES downstreamEE. The
• Shared columns: inclusion form includes (retains) the intron (upstreamEE,
– ID: rMATS event id downstreamES)
– GeneID: gene id • summary.txt: brief summary of all alternative splicing event
– geneSymbol: gene name types. Includes the total event counts and significant event
– chr: chromosome counts. By default, events are counted as significant if FDR ≤0.05.
– strand: strand of the gene Summary can be regenerated with different criteria by running
– IJC_SAMPLE_1: inclusion counts for sample 1. Replicates are rMATS_P/summary.py
comma separated
– SJC_SAMPLE_1: skipping counts for sample 1. Replicates are --tmp contains the intermediate files generated by the prep step:
comma separated • [datetime]_[id].rmats: summary generated from processing
– IJC_SAMPLE_2: inclusion counts for sample 2. Replicates are a BAM file
comma separated • [datetime]_bam[sample_num]_[replicate_num]/Aligned.
– SJC_SAMPLE_2: skipping counts for sample 2. Replicates are sortedByCoord.out.bam: result of mapping input FASTQ files
comma separated • [datetime]_read_outcomes_by_bam.txt: counts of the reads
– IncFormLen: length of inclusion form, used for normalization used from each BAM file along with counts of the reasons that
– SkipFormLen: length of skipping form, used for normalization reads could not be used
– PValue: significance of splicing difference between the two
sample groups (only available if the statistical model is on)
is dataset dependent, as it requires the observation of RNA-seq evidence for mutually
exclusive splicing events of a single gene. In a conventional alternative splicing analysis
workflow (e.g., in rMATS and many other tools), adding a new sample to an already
analyzed dataset would require re-running the entire workflow on the combined dataset
from scratch. In contrast, rMATS-turbo can process new RNA-seq files in a separate prep
step. Then, the splicing graphs (.rmats files) of newly processed RNA-seq files can be
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1088
Protocol
combined with the splicing graphs of already processed RNA-seq files in a single post step,
to summarize the alternative splicing profiles of the combined dataset. This convenient
feature saves substantial computational time when adding new RNA-seq files to an ongoing
RNA-seq study.
2. rMATS-turbo enables discovery of alternative splicing events that involve novel
(unannotated) splice sites or exons in the genome via the ‘--novelSS’ option. This feature is
particularly useful for discovering novel splice sites or exons that are activated in a specific
cellular state or disease. For example, mutations or altered expression or activity of splicing
factors can lead to activation of unannotated cryptic splice sites in the genome34,35. One
example of using the ‘--novelSS’ option of rMATS-turbo to study novel splice sites in human
tissues can be found in ref. 36.
3. rMATS-turbo includes an option (‘--fixed-event-set’) to read a user-defined set of alternative
splicing events and perform quantification using RNA-seq data. This feature may simplify
alternative splicing analysis across multiple datasets or by multiple laboratories, when
users wish to focus on a predefined set of alternative splicing events.
4. Although originally developed for two-group comparison of differential alternative splicing
events18, rMATS-turbo now allows users to discover and quantify alternative splicing events
on any set of RNA-seq files without dividing the samples into two groups. Furthermore,
the statistical analysis can be decoupled from the discovery and quantification steps.
Taken together, these optimizations greatly facilitate alternative splicing analysis for
datasets with more than two conditions (e.g., in time-course studies). Specifically, to enable
alternative splicing discovery and quantification on a single sample or the entire set of
samples as a single group, users can provide the ‘--b1’ or ‘--s1’ option and omit the ‘--b2’ or
‘--s2’ option, to list the BAM (‘--b1’) or FASTQ (‘--s1’) files as the input files for rMATS-turbo
in a single-group mode. The ‘--statoff’ flag can be used to disable the statistical test, under
either the single-group or two-group mode. The output files of rMATS-turbo include (1) event
files listing all identified alternative splicing events corresponding to all five basic types of
alternative splicing patterns, (2) count files listing RNA-seq read counts of all alternative
splicing events across all samples and (3) final output files concatenating information
from both event files and count files, as well as calculated PSI values and results from
statistical tests (filled with NAs if using the ‘--statoff’ flag) (Box 2). If users wish to identify
differential alternative splicing events between any two user-defined subsets of samples,
they can extract count data for those two subsets from output count files (Box 2) by using
the provided code (rMATS_P/prepare_stat_inputs.py) rather than reprocessing the input
files for those samples from scratch. The ‘--task stat’ option can then be invoked to only
perform the statistical test for differential alternative splicing analysis using the extracted
count data.
5. Whereas the default statistical test treats two groups of RNA-seq samples as unpaired,
rMATS-turbo now provides an option (‘--paired-stat’) to invoke PAIRADISE, a new and
improved statistical model that we recently introduced for differential alternative splicing
analysis of RNA-seq data with paired replicates (e.g., case-control matched pairs)37.
6. Other minor improvements to the flexibility of the rMATS-turbo workflow include allowing
variable length of RNA-seq reads in input files, by using the ‘--variable-read-length’ flag,
and allowing hard or soft clipping of RNA-seq reads in RNA-seq alignments, by using the
‘--allow-clipping’ flag.
7. Alternative splicing events analyzed by rMATS-turbo can be visualized using our companion
rmats2sashimiplot software (https://github.com/Xinglab/rmats2sashimiplot), which was
designed specifically for the rMATS-turbo output.
Alternative methods
Computational tools for short-read RNA-seq analysis of alternative splicing can be classified
into three major methodological categories: isoform based, exon based and event based.
Isoform-based tools (e.g., Cufflinks38, kallisto39) estimate the abundances and proportions
of full-length transcript isoforms using short-read RNA-seq data, and can be used to detect
novel transcript isoforms as well as isoform switches between biological conditions.
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1089
Protocol
However, transcript isoform discovery and quantification using short-read RNA-seq data are
computationally challenging, as short-read RNA-seq only examines transcript fragments but
cannot completely render full-length transcripts14. Moreover, many genes contain multiple
alternatively spliced regions, and it is not trivial to associate the observed isoform switches
to specific exons or splice sites. Exon-based tools (e.g., DEXseq40) use exon counts to detect
differential exon usage, but do not provide information about the alternative splicing
events that cause changes in exon counts. Due to these limitations, the third category of
event-based tools represents the most widely used strategy. Many computational tools have
been developed for event-based alternative splicing analysis using short-read RNA-seq data
(for a nonexhaustive summary, see refs. 9,13,14). Some notable examples include classic tools
developed on small-scale datasets in the early days of RNA-seq, such as MISO19 and SpliceTrap41,
and contemporary tools that scale up to large-scale datasets, such as SUPPA/SUPPA242,43,
MAJIQ44, LeafCutter45 and our own rMATS/rMATS-turbo18. Differences among these tools
include, but are not limited to, their RNA-seq data processing workflows and read-counting
procedures (e.g., alignment based versus alignment free), definitions of alternative splicing
events (basic versus complex), and statistical models for quantifying alternative splicing
events and testing for differential alternative splicing. Nonetheless, multiple studies have
shown that different tools tend to generate concordant PSI estimates on the same set of
alternative splicing events42,46,47.
Although benchmark comparisons are outside the scope of this protocol,
rMATS-turbo has performed favorably or comparably to alternative tools in multiple
benchmark studies46,48–50. The software has consistently been broadly used by the research
community, as evidenced by its high citation count compared with other aforementioned
contemporary tools, probably in part due to its ease of use and interpretation, as well as
its scalability to large-scale datasets.
Limitations of rMATS-turbo
The rMATS-turbo software is designed for short-read RNA-seq data, and has limitations inherent
to short-read RNA-seq analysis of alternative splicing9. First, rMATS-turbo discovers and
quantifies five basic types of alternative splicing patterns that involve binary splicing choices from
an alternatively spliced region (Fig. 1). This analytic strategy is adopted by many existing tools9,13.
The focus on basic alternative splicing events simplifies data representation and interpretation.
However, the tradeoff is that this approach is not well suited for more complex alternative splicing
events, in which basic types of alternative splicing patterns are combined to produce more than
two splicing choices from an alternatively spliced region45,51. Second, rMATS-turbo and all other
aforementioned tools are limited by the fact that short-read RNA-seq does not directly sequence
full-length transcripts and cannot reveal long-range coupling between distant alternative splicing
events within a gene. Ultimately, the increasingly popular long-read RNA-seq technology may
overcome the limitations of short-read RNA-seq for alternative splicing analysis, but will require
the development of a new generation of computational tools to address the unique challenges and
opportunities of long-read RNA-seq data52–54.
Experimental design
To illustrate the utility of rMATS-turbo, we describe in detail two representative application
scenarios. The procedures described below can be generalized to many other studies and
datasets. Datasets for the procedures below are described in the ‘Materials—required data’
section and are publicly available; detailed information is given in Supplementary Tables 1 and 2.
Procedure 1
This example shows a broadly applicable two-group comparison to identify differential
alternative splicing events between two sample groups, including both annotated
and novel alternative splicing events. We run rMATS-turbo with a one-line command
combining the prep and post steps, using RNA-seq data from the PC3E and GS689 prostate
cancer cell lines with contrasting phenotypes55. Each dataset has three biological replicates.
The ‘--novelSS’ flag is turned on to enable the discovery of alternative splicing events that
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1090
Protocol
involve novel (unannotated) splice sites or exons. The PC3E cell line has epithelial cell-like
features, whereas the GS689 cell line has mesenchymal and invasive characteristics56. The
rMATS-turbo analysis of these two cell lines is biologically relevant, as it reveals alternative
splicing events that occur during the epithelial–mesenchymal transition (EMT), a fundamental
cellular process associated with cell migration, invasion and metastasis in development,
fibrosis and cancer57. Procedure 1 takes ~5.5 h with 11 GB peak random-access memory (RAM).
Procedure 2
This example shows a fast analysis of alternative splicing in a large-scale RNA-seq dataset using
a compute cluster. We analyze RNA-seq data of 1,019 human cancer cell lines from the Cancer
Cell Line Encyclopedia (CCLE)58. Given the size of the dataset, we run rMATS-turbo with the prep
and post steps decoupled. Specifically, we first process CCLE RNA-seq files individually via the
prep step, with the work distributed over a compute cluster. We then summarize the alternative
splicing profiles across all CCLE cell lines via the post step. Moreover, to illustrate the use of
rMATS-turbo-generated alternative splicing profiles for customized downstream analyses, we
use an established gene signature-based metric59,60 to score the EMT status of all CCLE cell lines,
and identify alternative splicing events associated with the EMT score. Procedure 2 takes ~3 d
when running in a distributed manner on a compute cluster (24 GB peak RAM), but the time
usage may vary depending on resource availability.
Levels of expertise required
Understanding and executing the step-by-step protocol requires readers to have general
knowledge and experience with Unix-based command line operations. General understanding
of alternative splicing is needed to interpret the results.
Materials
Equipment
Hardware
• A computer with Unix-based operating system
• At least 32 GB of RAM is recommended for RNA-seq read alignment to the human genome
using STAR if FASTQ files are used as input
• A compute cluster is needed for running the prep step of rMATS-turbo in a distributed
manner over multiple computers. It is also possible to run rMATS-turbo on a local computer
if using pre-aligned BAM files as input for datasets with a small sample size
▲ CrItICAl The memory usage of rMATS-turbo is dependent on multiple factors, including
the number of samples, depth of RNA-seq reads, and whether the ‘--novelSS’ option is
turned on. We recommend increasing the memory allocation when running rMATS-turbo
on a large-scale RNA-seq dataset with the ‘--novelSS’ option turned on.
Software
• rMATS-turbo 4.1.1 (https://github.com/Xinglab/rmats-turbo)
• rmats2sashimiplot 2.0.4 (https://github.com/Xinglab/rmats2sashimiplot)
• rMATS-turbo dependencies
– Python 2.7 (Python 3 is also supported, tested on Python 3.6.12)
– Python libraries (Cython 0.27.3, numpy 1.16.6)
– BLAS and LAPACK 0.3.7
– gcc 4.8.5
– gfortran 4.8.5
– cmake 3.14.0
– PAIRADISE (optional, only needed in the statistical test part if samples in the two
groups represent paired replicates) (https://github.com/Xinglab/PAIRADISE)
– samtools 1.10 (optional, only needed if using FASTQ files as input)
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1091
Protocol
• rmats2sashimiplot dependencies
– Python 2.7 (Python 3 can be used after running 2to3.sh)
– Python libraries (scipy 1.2.1, matplotlib 2.2.3, pysam 0.15.4)
– samtools 1.10
– bedtools 2.29.2
• sratoolkit 2.9.2: for downloading the FASTQ files from the Sequence Read Archive (SRA)
• STAR 2.7.1a: for RNA-seq read alignment of FASTQ files
• R 3.6.1 (optional)
• conda 4.8.3 (optional)
• wget 1.14 (optional)
required data
• Procedure 1: RNA-seq data for PC3E and GS689 cell lines (n = 3 for each cell line) can
be downloaded from the SRA archive under accession BioProject PRJNA438990
(Supplementary Table 1)
• Procedure 2: RNA-seq data for the 1,019 CCLE human cancer cell lines can be downloaded
from the SRA archive under accession BioProject PRJNA523380 (Supplementary Table 2)
• Human hg19 reference genome (ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_
human/release_31/GRCh37_mapping/GRCh37.primary_assembly.genome.fa.gz)
• Human hg19 transcript annotation GTF file (ftp://ftp.ebi.ac.uk/pub/databases/gencode/
Gencode_human/release_31/GRCh37_mapping/gencode.v31lift37.annotation.gtf.gz)
• Human hg19 transcript annotation GFF3 file (ftp://ftp.ebi.ac.uk/pub/databases/gencode/
Gencode_human/release_31/GRCh37_mapping/gencode.v31lift37.annotation.gff3.gz)—this
input file is needed by the rmats2sashimiplot software when visualizing the alternative
splicing events by sashimi plot based on genome coordinates
Equipment setup
Downloading and installing rMAtS-turbo
rMATS-turbo and all required dependencies can be installed through conda by using the
following command:
conda install -c conda-forge -c bioconda rmats
▲ CrItICAl This should be done in a dedicated conda environment to avoid package conflicts.
Alternatively, after the required dependencies are installed, rMATS-turbo can be downloaded
and installed through the GitHub repository:
git clone https://github.com/Xinglab/rmats-turbo
cd rmats-turbo
./build_rmats
▲ CrItICAl All rMATS-turbo dependencies must have already been installed before installing
rMATS-turbo through the GitHub repository.
Downloading and installing rmats2sashimiplot
The rmats2sashimiplot software can be downloaded from the GitHub repository:
git clone https://github.com/Xinglab/rmats2sashimiplot
cd rmats2sashimiplot
rmats2sashimiplot is written in Python 2. If using Python 3, the following command must first be
run to convert the package to Python 3 script:
bash 2to3.sh
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1092
Protocol
Next, rmats2sashimiplot can be installed by running the setup.py file:
python ./setup.py install
The software can also be used without installation by providing the path to
the script:
python ./src/rmats2sashimiplot/rmats2sashimiplot.py
Downloading and preparing the required data
The human hg19 reference genome and corresponding transcript annotation GTF and
GFF3 files can be downloaded by using wget with the following commands:
wget \
ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_31/
GRCh37_mapping/GRCh37.primary_assembly.genome.fa.gz
wget \
ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_31/
GRCh37_mapping/gencode.v31lift37.annotation.gtf.gz
wget \
ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_31/
GRCh37_mapping/gencode.v31lift37.annotation.gff3.gz
rMATS-turbo can take either FASTQ or BAM files as input files. If FASTQ files are used, rMATS-turbo
will first call the STAR software to perform RNA-seq read alignment. Nonetheless, we recommend
that users perform the RNA-seq read alignment separately and use pre-aligned BAM files as the
input for rMATS-turbo. FASTQ files for the RNA-seq datasets used for Procedure 1 (PC3E and
GS689 cell lines) and Procedure 2 (1,019 CCLE cell lines) can be downloaded from the SRA archive
with the sratoolkit software, and then aligned to the human hg19 reference genome by STAR61
as follows:
1. Download the .sra files to the workspace of sratoolkit (sra_workspace, specified while
installing sratoolkit) and then convert the files to FASTQ files.
./sratoolkit.2.9.2-ubuntu64/bin/prefetch.2.9.2 $SRA_RUN && \
./sratoolkit.2.9.2-ubuntu64/bin/fastq-dump.2.9.2 --outdir ./ \
--split-files $sra_workspace/$SRA_RUN.sra
$SRA_RUN represents the SRA accession number for each RNA-seq sample. A full list of
SRA accession numbers and corresponding sample information for Procedure 1 (PC3E
and GS689 cell lines; BioProject PRJNA438990) and Procedure 2 (1,019 CCLE cell lines;
BioProject PRJNA523380) are available in Supplementary Tables 1 and 2.
2. Generate a reference genome index for STAR using the downloaded hg19 reference genome
and the corresponding transcript annotation GTF file.
STAR --runThreadN 4 --runMode genomeGenerate \
--genomeDir STAR_index/gencode.v31lift37 \
--genomeFastaFiles GRCh37.primary_assembly.genome.fa \
--sjdbGTFfile gencode.v31lift37.annotation.gtf
The index will be generated to the STAR_index/gencode.v31lift37 folder, as indicated by the
‘--genomeDir’ argument.
3. Align RNA-seq reads to the hg19 reference genome by STAR.
STAR --genomeDir STAR_index/gencode.v31lift37 \
--readFilesIn $sample_name_1.fastq $sample_name_2.fastq \
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1093
Protocol
--outFileNamePrefix ./$sample_name/ --outSAMunmapped Within \
--outSAMattributes NH HI AS NM MD XS --twopassMode Basic \
--alignSJDBoverhangMin 1 --alignSJoverhangMin 8 --alignEndsType EndToEnd \
--runThreadN 6 --outSAMtype BAM SortedByCoordinate --outSAMstrandField
intronMotif
$sample_name_1.fastq and $sample_name_2.fastq represent two unzipped FASTQ files
corresponding to read pairs from paired-end RNA-seq data.
▲ CrItICAl To improve the discovery and quantification of alternative splicing events that
involve novel (unannotated) splice sites or exons, we recommend that users run STAR under
the two-pass alignment mode (--twopassMode Basic), as recommended in ref. 62.
▲ CrItICAl It is recommended that STAR be provided with at least 32 GB of RAM for
mapping RNA-seq reads to the human genome.
Procedure 1: general two-group comparison to identify differential alternative splicing events
between PC3E and GS689 cell lines
▲ CrItICAl Also see Fig. 2.
Set up the working directory and input files for rMATS-turbo analysis
● tIMInG ~5 min
1. Set up the working directory where all outputs will be generated.
mkdir -p PC3E-GS689/rmats
cd PC3E-GS689/rmats
2. Generate configuration files (b1.txt and b2.txt) as input files for rMATS-turbo. These
two files contain comma-separated lists of FASTQ or BAM files for sample groups 1 and 2,
respectively.
ls $prefix_dir_group1 | tr '\n' ',' | sed 's/,$/\n/' > ./b1.txt
ls $prefix_dir_group2 | tr '\n' ',' | sed 's/,$/\n/' > ./b2.txt
$prefix_dir_group1: folder containing all FASTQ or BAM files for sample group 1.
$prefix_dir_group2: folder containing all FASTQ or BAM files for sample group 2.
Here is an example of what the content of a configuration file looks like:
group1_sample1.bam, group1_sample2.bam, group1_sample3.bam
▲ CrItICAl StEP Either FASTQ files or BAM files can be used by rMATS-turbo.
If FASTQ files are provided, rMATS-turbo will perform RNA-seq read alignment using
the STAR software.
▲ CrItICAl StEP A minimum of three samples per group is recommended for
between-group differential alternative splicing analysis.
Run rMATS-turbo to identify differential alternative splicing events, using the ‘--task
both’ option to run the prep and post steps in a single run
● tIMInG ~4 h 45 min
3. Run rmats.py with specified parameters.
python $rmats_dir/rmats.py --gtf $GTF --tmp prep --od post \
--readLength 101 --b1 b1.txt --b2 b2.txt -t paired \
--anchorLength 1 --nthread 1 --libType fr-unstranded --task both \
--variable-read-length --novelSS
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1094
Protocol
$rmats_dir: directory where rMATS-turbo is installed. If rMATS-turbo was installed through
conda, users can find it by typing ‘which rmats.py’.
$GTF: file path of the unzipped GTF annotation file. The GTF file should be the same
GTF file used for RNA-seq read alignment, to ensure that the same annotation is used across
the whole workflow and that the chromosome nomenclature is consistent in the GTF file and the
BAM files.
The ‘--novelSS’ option enables the discovery of alternative splicing events that involve novel
(unannotated) splice sites or exons. Please refer to Box 1 and Box 2 for detailed descriptions of
all command line arguments and output files, respectively.
▲ CrItICAl StEP If BAM files are used, the configuration file(s) should be specified by ‘--b1’
and/or ‘--b2’; if FASTQ files are used, the configuration file(s) should be specified by ‘--s1’
and/or ‘--s2’.
▲ CrItICAl StEP The ‘--paired-stats’ option can be turned on if each sample in ‘--b1’ is paired
with its corresponding sample in ‘--b2’, for an RNA-seq dataset with paired replicates. Under the
‘--paired-stats’ mode, the PAIRADISE software will be invoked to identify differential alternative
splicing events based on a paired statistical model37.
▲ CrItICAl StEP rMATS-turbo can run on multiple threads (specified by the ‘--nthread’
argument) to shorten its runtime.
◆ troublESHootInG
Perform downstream analysis and visualization of rMATS-turbo results
● tIMInG ~30 min
4. Select statistically significant events from the two-group differential alternative splicing
analysis. The following criteria are recommended:
• Read coverage: average RNA-seq read count ≥10 in both sample groups
• PSI value: filter out events with average PSI value <0.05 or >0.95 in both sample groups
• False discovery rate (FDR): FDR ≤0.01
• Between-group PSI value difference: |ΔPSI| ≥0.05
The read counts, PSI values, FDR values and ΔPSI values can be retrieved from the
following columns in the output file (Box 2): IJC_SAMPLE_1 (IJC_SAMPLE_2), SJC_SAMPLE_1
(SJC_SAMPLE_2), IncLevel1 (IncLevel2), FDR and IncLevelDifference, respectively. The
suffixes of ‘1’ and ‘2’ represent the corresponding values for group 1 and group 2, respectively.
The source code, as well as input and output files for this step are described in detail in the
tutorial on the GitHub repository (https://github.com/Xinglab/rmats-turbo-tutorial63).
5. Run rmats2sashimiplot to generate sashimi plots for visualizing alternative splicing events
of interest.
mkdir -p PC3E-GS689/rmats2sashimi
cd PC3E-GS689/rmats2sashimi
rmats2sashimiplot --b1 $bam1,$bam2,$bam3 --b2 $bam4,$bam5,$bam6 \
--event-type SE -e sashimi_events.txt --l1 PC3E_rep --l2 GS689_rep \
--exon_s 1 --intron_s 5 -o ./output --group-info sashimi_groupInfo.txt
Detailed descriptions of all command line arguments can be found in the rmats2sashimiplot
GitHub repository (https://github.com/Xinglab/rmats2sashimiplot). Specifically:
• -e represents the path to a file containing alternative splicing events for which
sashimi plots will be generated. The format of this file should be the same as the
rMATS-turbo output files (e.g., SE.MATS.JC.txt). One sashimi plot per event in the file
will be generated
• --l1 and --l2 are labels for sample groups 1 and 2, respectively
• --group-info represents the path to a file that contains the grouping information of RNA-seq
samples. When the --group-info argument is used, one aggregated sashimi plot will be
generated for each sample group, in contrast to the default behavior of one sashimi plot
per sample. Each line of the file defines a sample group and is formatted as ‘group name:
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1095
Protocol
a c
RI 12,909
SE 60,577
MXE 46,844
A3SS 20,428 A5SS 14,298
b
RI 1,410
SE 6,061
MXE 3,798
A3SS 1,964 A5SS 977
d e
USO1 PC3E PSI = 0.91 MAST3 PC3E PSI = 0.09
498 471
60
GS689 PSI = 0.05 GS689 PSI = 0.41
36 24
448
f
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1096
MKPR
Delta PSI (GS689 – PC3E)
4 5
49
27 27
39
)RDF(
gol–
01
≥15
Not significant
High in GS689 (n = 2,658)
High in PC3E (n = 3,403)
ssecorp_lacigoloiB
tnenopmoc_ralulleC
noitcnuf_raluceloM
10
5
0
–1.0 –0.5 0 0.5 1.0
4
3
2
1
4
3
2
1
Exon 12 Exon 13 Exon 14 Exon 4 Exon 5
Cellular protein modification process (GO:0006464)
Regulation of apoptotic process (GO:0042981)
Regulation of transcription from RNA polymerase II promoter (GO:0006357)
Cellular protein metabolic process (GO:0044267)
Organelle assembly (GO:0070925)
Cytoskeleton organization (GO:0007010)
Positive regulation of transcription, DNA−templated (GO:0045893)
Plasma membrane bounded cell projection assembly (GO:0120031)
Vesicle-mediated transport (GO:0016192)
Regulation of intracellular signal transduction (GO:1902531)
Microtubule organizing center (GO:0005815)
Cytoskeleton (GO:0005856)
Centrosome (GO:0005813)
Lysosome (GO:0005764)
Focal adhesion (GO:0005925)
Lytic vacuole membrane (GO:0098852)
Microtubule cytoskeleton (GO:0015630)
Lysosomal membrane (GO:0005765)
Nucleolus (GO:0005730)
Golgi subcompartment (GO:0098791)
Cadherin binding (GO:0045296)
RNA binding (GO:0003723)
Protein kinase activity (GO:0004672)
Actin binding (GO:0003779)
Protein homodimerization activity (GO:0042803)
Protein serine/threonine kinase activity (GO:0004674)
Purine ribonucleoside triphosphate binding (GO:0035639)
GTPase regulator activity (GO:0030695)
Kinase binding (GO:0019900)
Rho guanyl−nucleotide exchange factor activity (GO:0005089)
0 4 8 12 16
Odds ratio 2.0 2.5 3.0 3.5 −log (adjusted P value)
10
MKPR
26.0
19.5
13.0
6.5
26.0
19.5
13.0
6.5
164/863
135/677
204/1,186
91/400
78/326
39/110
163/914
57/210
82/363
81/359
114/472
106/454
103/439
91/366
84/334
60/211
80/340
66/258
122/636
85/404
83/296
231/1,292
97/437
58/207
107/523
77/337
73/349
54/232
74/371
20/54
Protocol
Fig. 2 | General two-group comparison to identify differential alternative showing differential alternative splicing events between the PC3E and GS689
splicing events between PC3E and GS689 cell lines using rMATS-turbo. In cell lines, involving exon 13 in USO1 (d) and a novel exon in MAST3 (e). The black
this example, we ran rMATS-turbo with a one-line command combining the prep bars and dashed lines at the bottom represent exons and introns, respectively.
and post steps. Using RNA-seq splice junction reads, rMATS-turbo identified Density graphs represent reads per kilobase per million (RPKM) mapped to each
alternative splicing events in the PC3E (n = 3) and GS689 (n = 3) cell lines. genomic position. Arcs represent splice junctions. Numbers represent counts of
a, Summary pie chart of total alternative splicing events identified by rMATS-turbo reads mapped to splice junctions. PSI values are shown on top of the sashimi plots.
in the PC3E and GS689 cell lines, after filtering out events supported by <10 reads Numbers and PSI values of events shown in the figure are calculated based on RNA-
in either sample group, as well as events with extreme PSI values (average PSI seq splice junction reads. f, GO enrichment analysis of differentially spliced genes
value <0.05 or >0.95 in both sample groups). b, Summary pie chart of differential (SE events). The bar graphs show top ten enriched GO terms for Biological Process,
alternative splicing events identified by rMATS-turbo between the PC3E and GS689 Cellular Component and Molecular Function. The bar lengths depict Benjamini–
cell lines, after filtering for FDR value (≤0.01) and absolute delta PSI value (≥0.05) Hochberg-adjusted P values calculated from a hypergeometric test. Odds ratios of
reported by rMATS-turbo. c, A volcano plot of SE events in b. Each dot represents enrichment are indicated by opacity of bars. Two numbers shown beside each bar
one SE event. Horizontal and vertical dashed lines mark the threshold of FDR represent the number of differentially spliced genes and the total number of genes
value (≤0.01) and absolute delta PSI value (≥0.05), respectively. d,e, Sashimi plots with the corresponding GO term, respectively.
indices of RNA-seq files’. The content of the sashimi_groupInfo.txt file used in Procedure 1
is as follows:
PC3E:1-3
GS689:4-6
6. Perform Gene Ontology (GO) enrichment analysis on genes with differential alternative splicing
events. The source code as well as input and output files for this step are described in detail in
the tutorial on the GitHub repository (https://github.com/Xinglab/rmats-turbo-tutorial63).
▲ CrItICAl StEP Note that there is an inherent bias toward detecting differential
alternative splicing events in highly expressed genes. To mitigate this bias, the background
gene list used for the GO enrichment analysis should exclude nonexpressed or lowly
expressed genes in the dataset analyzed.
▲ CrItICAl StEP Genes with multiple differential alternative splicing events should not be
double counted in the GO enrichment analysis.
◆ troublESHootInG
Procedure 2: fast analysis of alternative splicing in a large-scale rnA-seq dataset (CClE) using
a compute cluster
▲ CrItICAl Also see Fig. 3.
Set up the working directory and input files for rMATS-turbo analysis with the prep
and post steps separated
● tIMInG ~5 min
1. Set up the working directory where all outputs will be generated.
mkdir -p CCLE/rmats
cd CCLE/rmats
2. Generate configuration files for the prep step of rMATS-turbo.
mkdir -p bamConfiguration_prep
ls $bam1 > ./bamConfiguration_prep/bam1.txt
ls $bam2 > ./bamConfiguration_prep/bam2.txt
…
ls $bam1019 > ./bamConfiguration_prep/bam1019.txt
$bamX: file path of input BAM file.
Nature Protocols | Volume 19 | April 2024 | 1083–1104 1097
