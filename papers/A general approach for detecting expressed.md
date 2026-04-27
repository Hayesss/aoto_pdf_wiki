---
marker_extracted: true
title: "A general approach for detecting expressed"
created: 2026-04-23
updated: 2026-04-23
type: paper
tags: ["paper"]
sources: [raw/papers/a-general-approach-for-detecting-expressed.md]
confidence: medium
year: 2019
---

# A general approach for detecting expressed

> 原文: [[a-general-approach-for-detecting-expressed]]

## 摘要

v i e fic bu m il u t ta u t p io o n n s p w la it t h e- v b a a r s i e a d bl s e c s R e N ns A it - i s v e i q ty2 t 0 e , c 2 h 1. nologies to baseupto10kbpawayfromthe5′transcriptionstartsiteofthe gene. Coverage metrics for 200 cancer-relevant genes are sum- The ability to detect CNAs in single cells has advanced the marized in Supplementary Data 2 and provided at nucleotide study of cancers where structural alterations and/or aneuploidy arecommon3–10,13,14,18.However,CNAsarerareinsometumor resolution at Sub- sequent sequencing and analyses were performed using only the types, such as AML22,23. Moreover, CNAs rarely capture the 5′ workflow application. complete subclonal complexity of any tumor, and are often We then asked whether bulk and single-cell RNA-seq data subclonal progression-associated events24. The ability to detect capturethesametranscriptstructureforthemutatedgenesinthis multiple,arbitrarySNVsinscRNA-seqreadsisanidealattribute study. Using one canonical isoform for each gene, we compared for any generally-applicable approach to the study of intratu- coverage in the single-cell data (unique barcode/UMI pairs at m th o at ra s l o h m e e ter S o N g V en s ei c t a y n . A b l e th id ou en g t h ifi p e r d ev f i r o o u m s s f t u u l d l- i l e e s ng h t a h ve cD es N ta A b s li

## 背景与目的

sh lo e w d eachposition)tothatinthebulkRNA-seqdata(quantifiedusing numbers of identified mutant cells made downstream analyses bamCoverage and 1bp bins), and visualized it using the UCSC dif I fi n cu w lt o 4 r ,5 k ,1 in 4. g with the 10x Genomics Chromium Single Cell 3′ G ea e c n h o g m e e ne B s r t o u w d s ie e d r , ( b M u e lk th - o a d n s d ). s T in h g e le- r c e e su ll lt d s at d a em id o e n n s ti t fi ra e t d e t t h h e at s , am fo e r (v2) and 5′ (v1) Gene Expression workflows, we observed setoftranscripts(Fig.1c).Coverageplotsforallmutatedgenesin sequence coverage far from the 3′ and 5′ ends of genes (respec- this study are provided at scrna_mutations. tively).Thiswasunexpected,giventheend-biasoftheChromium librarydesign,andraisedthepossibilitythattheresultingscRNA- seqdatacouldbeusedforvariantdetection.Becausethisplatform Mutation identification in single cells. We next sought to can sample up to 10,000 cells per library, we hypothesized that identify cells containing any of the somatic variants discovered even sparse transcript coverage – which would permit the iden- usingeWGS.ForeachcellandeachvariantpositionintheeWGS tification of mutations in a fraction of cells – might allow us to data, unique wild-type, and mutant reads were counted using combine variant detection with high-throughput transcriptome cb_sniffer, a tool that extends the PySam library to do barcode- characterization.

## 主要发现

**eWGS and bulk RNA-sequencing.** Four cases of de novo AML and one of secondary AML were selected for study (clinical details in <a href="https://github.com/genome/scrna\_mutations">https://github.com/genome/scrna\_mutations</a>). eWGS was used in conjunction with well-established variant detection pipelines to generate a set of high-confidence mutation calls for

each case, and bulk RNA-sequencing was used to determine which mutations were expressed in each tumor sample (Methods). eWGS (Fig. 1a) revealed that these cases were genetically representative of AML, containing on average 26 mutations within coding regions, with many in well-established driver genes (e.g. *DNMT3A*, *FLT3*, *NPM1*, *TP53*, *NRAS*, *IDH1*, *CEBPA*, etc.). To define the clonal architecture of each tumor, the SciClone algorithm was used to cluster mutations and infer subclones. At least one subclone was identified in every case (Table 1, Supplementary Data 1). Bulk RNA-sequencing showed that on average, fewer than half of the mutations detected by eWGS were expressed (Table 1).

Single-cell transcript coverage and representation. We first compared genome-wide transcript coverage obtained from the 5' (v1) and 3' (v2) 10x Genomics Chromium Single Cell Gene Expression workflows. For one case, UPN 508084, we generated two scRNA-seq libraries with each workflow, and sequenced them to high depth, targeting 200,000 reads/cell. Transcriptomewide coverage for each data set was assessed using 20,090 genes, each having one annotated isoform (Methods). Both workflows yielded consistent low-level coverage at least 10 kbp from the 5' and 3' ends of the average transcript (Fig. 1b). However, the 5' kit yielded slightly higher transcript-wide coverage in distal regions of transcripts. For the average gene assayed using that kit, at least 2.5% of the unique sequenced transcripts mapped to any given base up to 10 kbp away from the 5' transcription start site of the gene.


## 方法概述

**Ethical approval and consent.** Samples were obtained as part of a study that was approved by the Human Research Protection Office at Washington University School of Medicine (HRPO # 201011766). All the patients provided written informed consent that permitted whole-genome sequencing, in accordance with a protocol that was approved by the institutional review board at the Washington University School of Medicine.

**eWGS**, **germline SNP detection**, **and somatic variant detection**. For each case, we performed enhanced whole-genome sequencing (eWGS) on bone marrow and matched normal tissue to identify germline and somatic variants. eWGS combines whole-genome sequencing with targeted exon capture to yield high coverage

(~150×) of the exome, and lower genome-wide coverage in the tumor (~45×) and normal (~25x) samples. Using a previously described protocol, eWGS sequencing libraries, including WGS libraries (350 bp inserts) and targeted libraries (250 bp inserts), were constructed with a KAPA HTP kit on a SciClone instrument. Targeted libraries were captured with the IDT exome reagent spiked with AML recurrently mutated genes (~40 Mb). These were sequenced on an Illumina HiSeq4000, producing ~150X coverage of each enhanced region. Sequence data were aligned to reference sequence build GRCh37-lite-build37 using BWA-MEM version 0.7.10 (params: -t 8), then merged and deduplicated using Picard version 1.113 (https://broadinstitute.github.io/picard/). Germline mutations were called using GATK HaplotypeCaller v3.5 (parameters -stand\_emit\_conf 10 -stand\_call\_conf 30) and filtered using recommended parameters (-filterExpression "QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0"). SNVs were detected using an ensemble mutation calling approach that considers the union of four callers: (1) Samtools version r982 (params: mpileup -BuDs) intersected with Somatic Sniper version 1.0.


## 讨论与结论

The ability to link genetic and transcriptomic information in single cells has important implications for the study of heterogeneous cell populations. By combining eWGS and scRNA-seq data from a high-throughput platform, we can distinguish between tumor and non-tumor cells, identify tumor cells displaying lineage infidelity, evaluate the differentiation state of individual tumor samples, derive mutation-associated expression signatures, study transcriptional heterogeneity within confirmed tumor cells, and identify cell-surface markers that can be used to isolate specific cells for downstream studies. Further, the approach described here should be applicable—without additional modifications or customization—to virtually any tumor type.

Previous studies have demonstrated that CNAs and specific genetic variants, such as the BCR-ABL fusion, can be identified with high sensitivity in full-length transcripts from dozens to hundreds of single cells using plate-based techniques such as the Fluidigm C1/Smartseq platform, and that SNVs can also be identified, albeit with lower sensitivity, using that data. Because CNAs rarely reflect the complete clonal architecture of a tumor (and are rare in most AML samples), we were interested in finding a way to identify SNVs in single cells. We noticed that the 10x Genomics Chromium Single Cell 3' and 5' Gene Expression workflows yield unexpectedly high transcript coverage far from the 3' and 5' ends of transcripts. Although this distal coverage is sparse, it is sufficient for low-sensitivity variant detection in single cells: SNVs were detectable in 22.7% of the cells in our samples, on average. Coupled with the high throughput of the platform, this sensitivity enables the detection of SNVs in hundreds to thousands of cells per sample. Although these cells can be studied in isolation, we analyzed them in the context of the entire sample, thereby leveraging the expression information provided by the additional, non-genotyped cells.


## 关键词

approach, detecting, expressed, general

## 相关实体

细胞类型: AML
方法: RNA-seq, scrna, single-cell
疾病: cancer, tumor

---

> 本笔记基于自动提取生成，已标准化为 AIMRaD 结构。
