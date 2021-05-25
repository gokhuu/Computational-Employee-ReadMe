import numpy as np 
import pandas as pd

new_csv_lst = ['VCFs/chrm_split/chr1_replicates.csv', 'VCFs/chrm_split/chr2_replicates.csv','VCFs/chrm_split/chr3_replicates.csv','VCFs/chrm_split/chr4_replicates.csv','VCFs/chrm_split/chr5_replicates.csv',
'VCFs/chrm_split/chr6_replicates.csv','VCFs/chrm_split/chr7_replicates.csv','VCFs/chrm_split/chr8_replicates.csv','VCFs/chrm_split/chr9_replicates.csv','VCFs/chrm_split/chr10_replicates.csv',
'VCFs/chrm_split/chr11_replicates.csv','VCFs/chrm_split/chr12_replicates.csv','VCFs/chrm_split/chr13_replicates.csv','VCFs/chrm_split/chr14_replicates.csv','VCFs/chrm_split/chr15_replicates.csv',
'VCFs/chrm_split/chr16_replicates.csv','VCFs/chrm_split/chr17_replicates.csv','VCFs/chrm_split/chr18_replicates.csv','VCFs/chrm_split/chr19_replicates.csv','VCFs/chrm_split/chr20_replicates.csv',
'VCFs/chrm_split/chr21_replicates.csv','VCFs/chrm_split/chr22_replicates.csv','VCFs/chrm_split/chrX_replicates.csv','VCFs/chrm_split/chrY_replicates.csv']

def storage_lst(file_lst):
	lst = []
	for i in file_lst:
		df = pd.read_csv(i, header=0, index_col=0)
		lst.append(df)
	return lst

df_list = storage_lst(new_csv_lst)

df = pd.concat(df_list,ignore_index=True)

chrmPos = []
for i in range(df.shape[0]):
    s = str(df.CHROM[i]) + '@' + str(df.POS[i])
    chrmPos.append(s)
    
#append to dataframe and prep for analysis
df.insert(loc=0, column='Samples', value=chrmPos)
df = df.drop(['CHROM','POS'], axis=1)
df = df.set_index('Samples')
df = df.T

reference_dict = {'Homozygous Reference':0, 'Heterozygous Alternate':1, 
					'Heterozygous Alternate 1/2':2,'Homozygous Alternate':3}

df = df.replace(reference_dict)
for i in df.columns:
	if df.get(i).dtypes !='int64':
		print(df.i.head())
