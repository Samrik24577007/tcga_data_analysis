import sys
disease_dict={}
disease=sys.argv[1]
a=disease.split("_")
disease_mod=" ".join(a)

for line in sys.stdin:
	l=line.strip().split("\t")
	if len(l)==8:
		if l[7]==disease_mod :
			disease_dict[l[0]]=l[1]
for directory in disease_dict:
	print(directory + "/" + disease_dict[directory])


#File ID	File Name	Data Category	Data Type	Project ID	Case ID	Sample ID	Sample Type
#eb8d5bd9-2b78-4798-97f9-6940ed8a2f78	TCGA_LUAD.4e1a2500-98ba-417b-a58a-973f98852496.wxs.VarScan2.somatic_annotation.vcf.gz	Simple Nucleotide Variation	Annotated Somatic Mutation	TCGA-LUAD	TCGA-86-8076, TCGA-86-8076	TCGA-86-8076-10A, TCGA-86-8076-01A	Blood Derived Normal, Primary Tumor
#c568fdc8-6942-44ff-a9d9-3f7a03fdc62a	367864dd-ccd2-473e-9661-6ff4342a4e64.rna_seq.augmented_star_gene_counts.tsv	Transcriptome Profiling	Gene Expression Quantification	TCGA-LUAD	TCGA-73-4658	TCGA-73-4658-01A	Primary Tumor
#b74d07c5-f539-48f3-9875-a1c5e91e8d90	nationwidechildrens.org_biospecimen.TCGA-73-4658.xml	Biospecimen	Biospecimen Supplement	TCGA-LUAD	TCGA-73-4658		
#96878182-c522-497b-992c-397711988e88	12c2f455-6d68-4a09-9cda-c38dfacc5824.wxs.aliquot_ensemble_raw.maf.gz	Simple Nucleotide Variation	Aggregated Somatic Mutation	TCGA-LUAD	TCGA-67-6217, TCGA-67-6217	TCGA-67-6217-01A, TCGA-67-6217-10A	Primary Tumor, Blood Derived Normal
#438dd401-2f54-42bd-9856-afceee33dc92	BURST_p_TCGA_b119_SNP_N_GenomeWideSNP_6_F02_787222.nocnv_grch38.seg.v2.txt	Copy Number Variation	Masked Copy Number Segment	TCGA-LUAD	TCGA-67-6217	TCGA-67-6217-10A	Blood Derived Normal
#61888a15-03d8-4ebe-9ce6-e00001857846	TCGA-LUAD.376f6da5-8562-4c23-ba9b-27462d735f99.arriba.rna_fusion.tsv	Structural Variation	Transcript Fusion	TCGA-LUAD	TCGA-49-6742	TCGA-49-6742-11A	Solid Tissue Normal
#06ef845a-839b-49ef-89b2-6c44b6589f35	BURST_p_TCGA_b119_SNP_N_GenomeWideSNP_6_D11_787164.CEL	Copy Number Variation	Raw Intensities	TCGA-LUAD	TCGA-73-4658	TCGA-73-4658-11A	Solid Tissue Normal
#94fc4ab9-cd9c-4d90-843b-219ad47901c2	TCGA-LUAD.6ca2a54e-7289-4076-ba92-65828fe98a87.arriba.rna_fusion.bedpe	Structural Variation	Transcript Fusion	TCGA-LUAD	TCGA-73-4658	TCGA-73-4658-01A	Primary Tumor
#1b4915fa-7d36-477a-8bdf-30a6ce5437e9	4d869897-10d0-4f49-922d-f7ee9fc3c591.mirbase21.mirnas.quantification.txt	Transcriptome Profiling	miRNA Expression Quantification	TCGA-LUAD	TCGA-49-6742	TCGA-49-6742-01A	Primary Tumor
