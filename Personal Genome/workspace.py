import numpy as np 
import pandas as pd
csv_lst = ['VCFs/chrm_split/chr1.csv', 'VCFs/chrm_split/chr2.csv','VCFs/chrm_split/chr3.csv','VCFs/chrm_split/chr4.csv','VCFs/chrm_split/chr5.csv',
'VCFs/chrm_split/chr6.csv','VCFs/chrm_split/chr7.csv','VCFs/chrm_split/chr8.csv','VCFs/chrm_split/chr9.csv','VCFs/chrm_split/chr10.csv',
'VCFs/chrm_split/chr11.csv','VCFs/chrm_split/chr12.csv','VCFs/chrm_split/chr13.csv','VCFs/chrm_split/chr14.csv','VCFs/chrm_split/chr15.csv',
'VCFs/chrm_split/chr16.csv','VCFs/chrm_split/chr17.csv','VCFs/chrm_split/chr18.csv','VCFs/chrm_split/chr19.csv','VCFs/chrm_split/chr20.csv',
'VCFs/chrm_split/chr21.csv','VCFs/chrm_split/chr22.csv','VCFs/chrm_split/chrX.csv','VCFs/chrm_split/chrY.csv']

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

def add_replicates(df):
	cols = df.iloc[:,2:]

	for i in cols.columns:
		if i == '14710x6':
			df.rename(columns={'14710x6': '14710x6-1'},inplace=True)
		elif i == '14746x8':
			t2 = list(df.get(i))
			s2 = i+'-2'
			df.rename(columns={'14746x8': '14746x8-1'},inplace=True)
			df.insert(loc=0, column=s2, value=t2)
		elif i == i =='14739x3':
			t2 = list(df.get(i))
			s2 = i+'-2'
			df.rename(columns={'14739x3': '14739x3-1'},inplace=True)
			df.insert(loc=0, column=s2, value=t2)
		else:
			t2 = list(df.get(i))
			t3 = list(df.get(i))
			s1 = i+'-1'
			s2 = i+'-2'
			s3 = i+'-3'
			df.rename(columns={i: s1},inplace=True)
			df.insert(loc=0, column=s2, value=t2)
			df.insert(loc=0, column=s3, value=t2)

	chrom = df.pop('CHROM')
	pos = df.pop('POS')
	df.insert(loc=0, column='POS', value=pos)
	df.insert(loc=0, column='CHROM', value=chrom)
	return df


def fix_col_name (df):

	for i in df.columns:
		temp = i
		
		for j in range(len(temp)):
			if j == '-':
				s = temp[:j]
				df.rename(column={i:s},inplace=True)
	return df

df_list = storage_lst(csv_lst)

for i in df_list:
	i = fix_col_name(i)

print(df_list[2].columns)
'''
for i in df_list:
	i = add_replicates(i)
'''
for i in range(len(csv_lst)):
	df_list[i].to_csv(new_csv_lst[i])
