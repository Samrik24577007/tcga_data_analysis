Here I have not downloaded the tcga_data.tar.gz, that shold be downloaded and unzipped in the working directory.
the rule extracting_directory takes any file of the form of {sample}_sample_sheet.tsv as input and gives output in disease_type_list/{disease}_sample_{sample}_files_list.tsv that contains all the filepaths in a column corresponding to the specific disease type
The next rule tpm_dist takes output of the previous rule and gives output file as TPM_val_list/{disease}_sample_{sample}_{gene}_TPM_vals.tsv, that contains TPM value for the specific gene in the specific disease type
The scripts/file_read.sh reads takes each file path line by line and reads contains of the file line by line to scripts/TPM_val.py that searches for the gene and its corresponding TPm value
The boxplot_R rule takes output of the previous rule for two different diseases and gives output in form of boxplot_tpm_val/disease1_and_disease2_sample_{sample}_{gene}_TPM_boxplot.png
The plot contains comparison of the gene expression in two different types disease using boxplot and calculates p_value
To get the output we have to run "snakemake -p -j1 --snakefile tpm_val_list.smk boxplot_tpm_val/Solid_Tissue_Normal_and_Primary_sample_gdc_NXK2-1_TPM_boxplot.png
