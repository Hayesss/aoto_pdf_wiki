---
source_url: zotero://select/items/3N8YBT74
ingested: 2026-04-22
sha256: d823ad0da2a421e9
---

# Servant 等 - 2015 - HiC-Pro an optimized and flexible pipeline for Hi

> Zotero Item Key: 3N8YBT74
> Original File: Servant 等 - 2015 - HiC-Pro an optimized and flexible pipeline for Hi.pdf

## Extracted Text

Servantetal.GenomeBiology (2015) 16:259
DOI10.1186/s13059-015-0831-x
SOFTWARE Open Access
HiC-Pro: an optimized and flexible pipeline
for Hi-C data processing
Nicolas Servant1,2,3*, Nelle Varoquaux1,2,3, Bryan R. Lajoie4, Eric Viara5, Chong-Jian Chen1,2,3,6,7,8,
Jean-Philippe Vert1,2,3, Edith Heard1,6,7, Job Dekker9 and Emmanuel Barillot1,2,3
Abstract
HiC-ProisanoptimizedandflexiblepipelineforprocessingHi-Cdatafromrawreadstonormalizedcontactmaps.HiC-Pro
mapsreads,detectsvalidligationproducts,performsqualitycontrolsandgeneratesintra-andinter-chromosomal
contactmaps.Itincludesafastimplementationoftheiterativecorrectionmethodandisbasedonamemory-efficient
dataformatforHi-Ccontactmaps.Inaddition,HiC-Procanusephasedgenotypedatatobuildallele-specificcontact
maps.WeappliedHiC-ProtodifferentHi-Cdatasets,demonstratingitsabilitytoeasilyprocesslargedataina
reasonabletime.Sourcecodeanddocumentationareavailableathttp://github.com/nservant/HiC-Pro.
Keywords:Chromosomeconformation,Hi-C,Bioinformaticspipeline,Normalization
Introduction interactions [5, 6]. More recently, very large data sets with
High-throughput chromosome conformation capture deeper sequencing have been used to increase the Hi-C
methods are now widely used to map chromatin interac- resolution in order to detect loops across the entire
tions within regions of interest and across the genome. genome [7, 8].
The use of Hi-C has notably changed our vision of gen- As with any genome-wide sequencing data, Hi-C usu-
ome organization and its impact on chromatin and gene ally requires several millions to billions of paired-end se-
regulation [1, 2]. The Hi-C technique involves sequen- quencing reads, depending on genome size and on the
cing pairs of interacting DNA fragments, where each desired resolution. Managing these data thus requires
mate is associated with one interacting locus. Briefly, optimized bioinformatics workflows able to extract the
cells are crossed-linked, DNA is fragmented using a re- contact frequencies in reasonable computational time
striction enzyme [3] or a nuclease [4], and interacting and with reasonable resource and storage requirements.
fragments are ligated together. After paired-end sequen- The overall strategy to process Hi-C data is converging
cing, each pair of reads can be associated to one DNA among recent studies [9], but there remains a lack of
interaction. stable, flexible and efficient bioinformatics workflows to
In recent years, the Hi-C technique has demonstrated process such data. Solutions such as the HOMER [10],
that the genome is partitioned into domains of different HICUP [11], HiC-inspector [12], HiCdat [13] and HiC-
scale and compaction level. The first Hi-C application has box [14] pipelines are already available for Hi-C data
described that the genome is partitioned into distinct processing. HOMER offers several functions to analyze
compartments of open and closed chromatin [3]. Higher Hi-C data but does not perform the mapping of reads
throughput and resolution have then suggested the pres- nor the correction of systematic biases. HiCdat, HiC-
ence of megabase-long and evolutionarily conserved inspector and HiCbox do not allow chimeric reads to be
smaller domains. These topologically associating domains rescued during the mapping of reads. HICUP provides a
arecharacterizedbyahighfrequencyofintra-domainchro- complete pipeline until the detection of valid interaction
matin interactions but infrequent inter-domain chromatin products. Using HICUP together with the SNPsplit pro-
gram [15] allows the extraction of allele-specific inter-
action products whereas all other solutions do not allow
*Correspondence:nicolas.servant@curie.fr
1InstitutCurie,Paris,France allele-specific analysis. The HiCdat and HiCbox packages
2INSERM,U900,Paris,France offer a means of correcting contact maps for systematic
Fulllistofauthorinformationisavailableattheendofthearticle
©2015Servantetal.OpenAccessThisarticleisdistributedunderthetermsoftheCreativeCommonsAttribution4.0
InternationalLicense(http://creativecommons.org/licenses/by/4.0/),whichpermitsunrestricteduse,distribution,and
reproductioninanymedium,providedyougiveappropriatecredittotheoriginalauthor(s)andthesource,providealinkto
theCreativeCommonslicense,andindicateifchangesweremade.TheCreativeCommonsPublicDomainDedicationwaiver
(http://creativecommons.org/publicdomain/zero/1.0/)appliestothedatamadeavailableinthisarticle,unlessotherwisestated.
Servantetal.GenomeBiology (2015) 16:259 Page2of11
biases. Finally, none of these software were designed to chunk was mapped on the human genome using four
processverylargeamountsofdatainaparallelmode.The CPUs (two for each mate) and 7 GB of RAM Processing
hiclibpackageiscurrentlythemostcommonlyusedsolu- the 84 chunks in parallel allows extraction of the list of
tionforHi-C dataprocessing.However,hiclibisaPython valid interactions in less than 30 minutes. All chunks
library that requires programming skills, such as know- were then merged to generate and normalize the
ledge of Python and advanced Linux command line, and genome-wide contact map.
cannot be used in a single command-line manner. In In order to compare our results with the hiclib library,
addition, parallelization is not straightforward and it has we ran HiC-Pro on the same dataset, and without initial
limitations with regard to the analysis and normalization read splitting, using eight CPUs. HiC-Pro performed the
ofveryhigh-resolutiondata(Table1). complete analysis in less than 15 hours compared with
Here,wepresentHiC-Pro,aneasy-to-useandcomplete 28 hours for the hiclib pipeline. The main difference in
pipeline to process Hi-C data from raw sequencing reads speed is explained by our two-step mapping strategy
to normalized contact maps. HiC-Pro allows the process- compared with the iterative mapping strategy of hiclib,
ing of data from Hi-C protocols based on restriction en- which aligned the 35 base pair (bp) reads in four steps.
zyme or nuclease digestion such as DNase Hi-C [4] or Optimizationofthebinningprocessandimplementation
Micro-C[16].Whenphasedgenotypesareavailable,HiC- of the normalization algorithm led to a three-fold de-
Proisabletodistinguishallele-specificinteractionsandto crease in time to generate and normalize the genome-
buildbothmaternaland paternalcontact maps. Itisopti- wide contactmap.
mized and offers a parallel mode for very high-resolution The IMR90 sample from the Rao dataset (1.5 billion
data as well as a fast implementation of the iterative cor- read pairs split into 160 read chunks) was processed in
rectionmethod[17]. parallel using 320 CPUs to generate up to 5-kb contact
maps in 12 hours, demonstrating the ability of HiC-Pro
Results to analyze very large amounts of data in a reasonable
HiC-Proresultsandperformance time. At a 5-kb resolution, we observe the presence of
We processed Hi-C data from two public datasets: chromatin loops as described by Rao et al. [7] (Figure S1
IMR90 human cell lines from Dixon et al. [6] (IMR90) inAdditionalfile1).Themergedlistof validinteractions
and from Rao et al. [7] (IMR90_CCL186). The latter is was generated in less than 7.5 hours. Normalization of
currently one of the biggest datasets available, used to the genome-wide contact map at 1 Mb, 500 kb, 150 kb,
generate up to 5-kb contact maps. For each dataset, we 40 kb, 20 kb and 5 kb was performed in less than
ran HiC-Pro and generated normalized contact maps at 4 hours. Details about the results and the implementa-
20 kb, 40 kb, 150 kb, 500 kb and 1 Mb resolution. Nor- tion of the different solutions are available in Additional
malized contact maps at 5 kb were only generated for file1.
the IMR90_CCL186 dataset. The datasets were either Finally, we compared the Hi-C processing results of
used in their original form or split into chunks contain- hiclib and HiC-Pro on the IMR90 dataset. Although the
ing10or20million readpairs. processing and filtering steps of the two pipelines are not
Using HiC-Pro, the processing o

... [truncated]
