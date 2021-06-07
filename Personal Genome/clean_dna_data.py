import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import allel as al
from scipy.spatial.distance import squareform

new_csv_lst = ['VCFs/cleaned_dna/chr1_replicates.csv', 'VCFs/cleaned_dna/chr2_replicates.csv','VCFs/cleaned_dna/chr3_replicates.csv','VCFs/cleaned_dna/chr4_replicates.csv','VCFs/cleaned_dna/chr5_replicates.csv',
'VCFs/cleaned_dna/chr6_replicates.csv','VCFs/cleaned_dna/chr7_replicates.csv','VCFs/cleaned_dna/chr8_replicates.csv','VCFs/cleaned_dna/chr9_replicates.csv','VCFs/cleaned_dna/chr10_replicates.csv',
'VCFs/cleaned_dna/chr11_replicates.csv','VCFs/cleaned_dna/chr12_replicates.csv','VCFs/cleaned_dna/chr13_replicates.csv','VCFs/cleaned_dna/chr14_replicates.csv','VCFs/cleaned_dna/chr15_replicates.csv',
'VCFs/cleaned_dna/chr16_replicates.csv','VCFs/cleaned_dna/chr17_replicates.csv','VCFs/cleaned_dna/chr18_replicates.csv','VCFs/cleaned_dna/chr19_replicates.csv','VCFs/cleaned_dna/chr20_replicates.csv',
'VCFs/cleaned_dna/chr21_replicates.csv','VCFs/cleaned_dna/chr22_replicates.csv','VCFs/cleaned_dna/chrX_replicates.csv','VCFs/cleaned_dna/chrY_replicates.csv']

csv_lst = ['VCFs/chrm_split/chr1_replicates.csv', 'VCFs/chrm_split/chr2_replicates.csv','VCFs/chrm_split/chr3_replicates.csv','VCFs/chrm_split/chr4_replicates.csv','VCFs/chrm_split/chr5_replicates.csv',
'VCFs/chrm_split/chr6_replicates.csv','VCFs/chrm_split/chr7_replicates.csv','VCFs/chrm_split/chr8_replicates.csv','VCFs/chrm_split/chr9_replicates.csv','VCFs/chrm_split/chr10_replicates.csv',
'VCFs/chrm_split/chr11_replicates.csv','VCFs/chrm_split/chr12_replicates.csv','VCFs/chrm_split/chr13_replicates.csv','VCFs/chrm_split/chr14_replicates.csv','VCFs/chrm_split/chr15_replicates.csv',
'VCFs/chrm_split/chr16_replicates.csv','VCFs/chrm_split/chr17_replicates.csv','VCFs/chrm_split/chr18_replicates.csv','VCFs/chrm_split/chr19_replicates.csv','VCFs/chrm_split/chr20_replicates.csv',
'VCFs/chrm_split/chr21_replicates.csv','VCFs/chrm_split/chr22_replicates.csv','VCFs/chrm_split/chrX_replicates.csv','VCFs/chrm_split/chrY_replicates.csv']

'''
cols_to_drop=['PGP1-3', 'PGP1-2', 'GM25256-3', 'GM25256-2',
       'GM23720-3', 'GM23720-2', 'GM23716-3', 'GM23716-2', 'BXS0117-3',
       'BXS0117-2', 'BXS0116-3', 'BXS0116-2', 'BXS0115-3', 'BXS0115-2',
       'BXS0114-3', 'BXS0114-2', 'BYS0112-3', 'BYS0112-2', 'BXS0111-3',
       'BXS0111-2', 'BXS0110-3', 'BXS0110-2', '1001-3', '1001-2', '901-3',
       '901-2', '902-3', '902-2', '1401-3', '1401-2', '1601-3', '1601-2',
       '14781x16-3', '14781x16-2', '14739x3-2', '14824x13-3', '14824x13-2',
       '14746x8-2', '14858x3-3', '14858x3-2', '14799x1-3', '14799x1-2',
       '14763x7-3', '14763x7-2', '14765x2-3', '14765x2-2']
'''

reference_dict = {'Homozygous Reference':[0,0], 'Heterozygous Alternate':[0,1], 
					'Heterozygous Alternate 1/2':[0,2],'Homozygous Alternate':[1,1]}
#iterate through list
for df in range(len(new_csv_lst)):
	#initalize dataframe
	dna = pd.read_csv(csv_lst[df], header=0)
	dna = dna.drop('Unnamed: 0', axis=1)
	
	#drop replicates
	#dna = dna.drop(cols_to_drop, axis=1)

	#create snp names
	chrmPos = []
	for i in range(dna.shape[0]):
		s = str(dna.CHROM[i] + '@' + str(dna.POS[i]))
		chrmPos.append(s)
	dna.insert(loc=0, column='Samples', value=chrmPos)
	dna = dna.drop(['CHROM', 'POS'], axis=1)
	dna = dna.set_index('Samples')

	#create genotype array
	gt_array =[]
	for i in dna.index:
		temp = []
		for j in dna.loc[i]:
			temp.append(reference_dict[j])
		gt_array.append(temp)

	#perform linkage disequalibirum correlation
	g = al.GenotypeArray(gt_array)
	gn = g.to_n_alt(fill=-1)
	r = al.rogers_huff_r(gn)
	corr = squareform(r**2)
	
	#convert to dataframe
	corr_df = pd.DataFrame(corr)
	corr_df = corr_df.fillna(0)
	
	#remove linkage disequalibirum
	corr_df['Mean']  = corr_df.mean(axis=0)
	below_threshold = []
	snp_to_drop = []
	for i in range(corr_df.Mean.shape[0]):
		if corr_df.Mean[i] < 0.05:
			below_threshold.append(i)

	for i in below_threshold:
		snp_to_drop.append(dna.index[i])

	dna = dna.drop(snp_to_drop,axis=0)
	dna.to_csv(new_csv_lst[df])