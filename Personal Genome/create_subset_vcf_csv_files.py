#python3
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from collections import Counter
from functools import reduce


def storage_lst(file_lst):
	lst = []
	for i in file_lst:
		df = pd.read_csv(i, header=0, index_col=0)
		lst.append(df)
	return lst

def extract_chr(df,chrom):
	new_df = df[df['CHROM'] == chrom]
	return new_df

def get_common_pos(d):
	lst = [item for item in d if d[item] == 26]
	return lst

def get_pos_dict(df_lst):
	lst = []
	for i in df_lst:
		p = i.POS
		for j in p:
			lst.append(j)
	d = Counter(lst)
	pos_lst = get_common_pos(d)
	return pos_lst

def get_chrom_subset(df_list, chrm):
	chrm_subset_lst = [extract_chr(i,chrm) for i in df_list]
	pos_list = get_pos_dict(chrm_subset_lst)
	guide = chrm_subset_lst[0]
	guide_df = guide[guide.POS.isin(pos_list)] 
	subset_lst = [x[x.POS.isin(pos_list)] for x in chrm_subset_lst]
	subset = reduce(lambda j,k: pd.merge(j,k, on=('CHROM','POS', 'REF', 'ALT')), subset_lst)
	return subset

def drop_cols(df):
	lst = ['ID_x', 'QUAL_x', 'FILTER_x', 'INFO_x', 'FORMAT_x', 'Genotype_x',
	'ID_y', 'QUAL_y', 'FILTER_y', 'INFO_y', 'FORMAT_y', 'Genotype_y']
	
	return df.drop(lst,axis=1)

#def create_sample_csv()
#list of csv file paths
list_of_csv = ['VCFs/VCF_csv/ED1.csv','VCFs/VCF_csv/ED2.csv','VCFs/VCF_csv/ED3.csv','VCFs/VCF_csv/ED4.csv',
'VCFs/VCF_csv/ED5.csv','VCFs/VCF_csv/ED6.csv','VCFs/VCF_csv/ED7.csv','VCFs/VCF_csv/ED8.csv',
'VCFs/VCF_csv/ED9.csv','VCFs/VCF_csv/ED10.csv','VCFs/VCF_csv/ED11.csv','VCFs/VCF_csv/ED12.csv',
'VCFs/VCF_csv/ED13.csv','VCFs/VCF_csv/ED14.csv','VCFs/VCF_csv/ED15.csv','VCFs/VCF_csv/ED16.csv',
'VCFs/VCF_csv/ED17.csv','VCFs/VCF_csv/ED18.csv','VCFs/VCF_csv/ED19.csv','VCFs/VCF_csv/ED20.csv',
'VCFs/VCF_csv/ED21.csv','VCFs/VCF_csv/ED22.csv','VCFs/VCF_csv/ED23.csv','VCFs/VCF_csv/ED24.csv',
'VCFs/VCF_csv/ED25.csv','VCFs/VCF_csv/ED26.csv']

to_csv_lst = ['DNA_csv/ED1.csv','DNA_csv/ED2.csv','DNA_csv/ED3.csv','DNA_csv/ED4.csv',
'DNA_csv/ED5.csv','DNA_csv/ED6.csv','DNA_csv/ED7.csv','DNA_csv/ED8.csv',
'DNA_csv/ED9.csv','DNA_csv/ED10.csv','DNA_csv/ED11.csv','DNA_csv/ED12.csv',
'DNA_csv/ED13.csv','DNA_csv/ED14.csv','DNA_csv/ED15.csv','DNA_csv/ED16.csv',
'DNA_csv/ED17.csv','DNA_csv/ED18.csv','DNA_csv/ED19.csv','DNA_csv/ED20.csv',
'DNA_csv/ED21.csv','DNA_csv/ED22.csv','DNA_csv/ED23.csv','DNA_csv/ED24.csv',
'DNA_csv/ED25.csv','DNA_csv/ED26.csv']

chromesome_lst = ['chr1', 'chr2','chr3','chr4','chr5','chr6','chr7',
'chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
'chr17','chr18','chr19','chr20','chr21','chr22','chr1','chr1','chr1',
'chr1','chrX','chrY']

#store dataframes
dataframes = storage_lst(list_of_csv)

#temp = get_chrom_subset(dataframes,chromesome_lst[0])
#new_temp = drop_cols(temp)
temp_lst = []
for i in chromesome_lst:
	temp_df = get_chrom_subset(dataframes,i)
	new_temp_df = drop_cols(temp_df)
	temp_lst.append(new_temp_df)

temp = pd.concat(temp_lst, ignore_index=True)
temp.to_csv(r'testing.csv')