#python3
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from collections import Counter


def storage_lst(file_lst):
	lst = []
	for i in file_lst:
		df = pd.read_csv(i, header=0, index_col=0)
		lst.append(df)
	return lst

def extract_chr(df,chrom):
	new_df = df[df['CHROM'] == chrom]
	return new_df

def get_pos_dict(df_lst):
	lst = []
	for i in df_lst:
		p = i.POS
		for j in p:
			lst.append(j)
	d = Counter(lst)
	return d

def get_common_pos(d):
	lst = []
	for item in d:
		if d[item] == 26:
			lst.append(item)
	return lst

#list of csv file paths
list_of_csv = ['VCFs/VCF_csv/ED1.csv','VCFs/VCF_csv/ED2.csv','VCFs/VCF_csv/ED3.csv','VCFs/VCF_csv/ED4.csv',
'VCFs/VCF_csv/ED5.csv','VCFs/VCF_csv/ED6.csv','VCFs/VCF_csv/ED7.csv','VCFs/VCF_csv/ED8.csv',
'VCFs/VCF_csv/ED9.csv','VCFs/VCF_csv/ED10.csv','VCFs/VCF_csv/ED11.csv','VCFs/VCF_csv/ED12.csv',
'VCFs/VCF_csv/ED13.csv','VCFs/VCF_csv/ED14.csv','VCFs/VCF_csv/ED15.csv','VCFs/VCF_csv/ED16.csv',
'VCFs/VCF_csv/ED17.csv','VCFs/VCF_csv/ED18.csv','VCFs/VCF_csv/ED19.csv','VCFs/VCF_csv/ED20.csv',
'VCFs/VCF_csv/ED21.csv','VCFs/VCF_csv/ED22.csv','VCFs/VCF_csv/ED23.csv','VCFs/VCF_csv/ED24.csv',
'VCFs/VCF_csv/ED25.csv','VCFs/VCF_csv/ED26.csv']

chromesome_lst = ['chr1', 'chr2','chr3','chr4','chr5','chr6','chr7',
'chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
'chr17','chr18','chr19','chr20','chr21','chr22','chr1','chr1','chr1',
'chr1','chrX','chrY']

#store dataframes
dataframes = storage_lst(list_of_csv)

'''
chrom1 = []
for i in dataframes:
	chrom1.append(extract_chr(i,'chr1'))

chrom1_pos_dict = get_pos_dict(chrom1)
print(len(chrom1_pos_dict))
print('')
chrom1_common_pos = get_common_pos(chrom1_pos_dict)
print(len(chrom1_common_pos))

temp = dataframes[0]
print(temp[temp.POS.isin(chrom1_common_pos)])
'''
