import sys
import pandas as pd
import math
gene=sys.argv[1]


for line in sys.stdin:
	l=line.strip().split("\t")
	if len(l)==9:
		if l[1]==gene:
			print(math.log2(float(l[6]) + 1))
	







#gene_id	gene_name	gene_type	unstranded	stranded_first	stranded_second	tpm_unstranded	fpkm_unstranded	fpkm_uq_unstranded
#N_unmapped			4850100	4850100	4850100			
#N_multimapping			8308196	8308196	8308196			
#N_noFeature			2173748	36760327	37016824			
#N_ambiguous			7782266	1870982	1859643			
#ENSG00000000003.15	TSPAN6	protein_coding	2370	1146	1224	23.2615	8.0689	9.7401
#ENSG00000000005.6	TNMD	protein_coding	1	0	1	0.0302	0.0105	0.0126
#ENSG00000000419.13	DPM1	protein_coding	2770	1397	1373	102.1729	35.4415	42.7820
#ENSG00000000457.14	SCYL3	protein_coding	621	521	503	4.0168	1.3933	1.6819
#ENSG00000000460.17	C1orf112	protein_coding	166	304	287	1.2379	0.4294	0.5183

