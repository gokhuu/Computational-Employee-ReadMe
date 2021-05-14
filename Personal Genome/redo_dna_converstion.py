#python3
'''
Author: Brandon Khuu
Last update: 5/4/2021

Import a large number of csv files and 
concat them into one larger dataframe
'''
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from collections import Counter
from functools import reduce

list_of_csv = [
'VCFs/VCF_csv/ED1.csv','VCFs/VCF_csv/ED2.csv','VCFs/VCF_csv/ED3.csv','VCFs/VCF_csv/ED4.csv',
'VCFs/VCF_csv/ED5.csv','VCFs/VCF_csv/ED6.csv','VCFs/VCF_csv/ED7.csv','VCFs/VCF_csv/ED8.csv',
'VCFs/VCF_csv/ED9.csv','VCFs/VCF_csv/ED10.csv','VCFs/VCF_csv/ED11.csv','VCFs/VCF_csv/ED12.csv',
'VCFs/VCF_csv/ED13.csv','VCFs/VCF_csv/ED14.csv','VCFs/VCF_csv/ED15.csv','VCFs/VCF_csv/ED16.csv',
'VCFs/VCF_csv/ED17.csv','VCFs/VCF_csv/ED18.csv','VCFs/VCF_csv/ED19.csv','VCFs/VCF_csv/ED20.csv',
'VCFs/VCF_csv/ED21.csv','VCFs/VCF_csv/ED22.csv','VCFs/VCF_csv/ED23.csv','VCFs/VCF_csv/ED24.csv',
'VCFs/VCF_csv/ED25.csv','VCFs/VCF_csv/ED26.csv']

chromesome_lst = ['chr1', 'chr2','chr3','chr4','chr5','chr6','chr7',
'chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
'chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']

#data frame storage list
def storage_lst(file_lst):
	lst = []
	for i in file_lst:
		df = pd.read_csv(i, header=0, index_col=0)
		lst.append(df)
	return lst

def drop_cols(df):
	lst = ['ID', 'QUAL', 'ID','REF','ALT','FILTER', 'INFO', 'FORMAT', 'Genotype']
	return df.drop(lst,axis=1)

#create subset selecting for chromosome
def extract_chr(df,chrom):
	new_df = df[df['CHROM'] == chrom]
	new_df = drop_cols(new_df)
	new_df = new_df.drop(new_df.columns[2], axis=1)
	return new_df

def create_pos_set(lst):
	pos_nested_list = [i.POS for i in lst]
	pos_list = [j for i in pos_nested_list for j in i]
	pos_set = set(pos_list)

	return pos_set

def add_homo_ref(df, pos_set,chrm):
	#create list of current position
	curr_pos = [i for i in df.POS]

	#create list of positions the df does not have
	not_in_lst = [i for i in pos_set if i not in curr_pos]

	#create new dataframe with new positions
	to_append = [[chrm, i, 'Homozygous Reference'] for i in not_in_lst]
	col_names = df.columns
	temp = pd.DataFrame(to_append, columns = col_names)
	
	#append dataframes
	new_df = pd.concat([df, temp])
	return new_df




df_list = storage_lst(list_of_csv)

chrm1 = [extract_chr(i, chromesome_lst[0]) for i in df_list]
pos_set = create_pos_set(chrm1)

temp_df_list = []
for i in chrm1:
	temp_df = add_homo_ref(i,pos_set,chromesome_lst[0])
	temp_df_list.append(temp_df.set_index('CHROM','POS').sort_index())

temp = temp_df_list[0].join(temp_df_list[1:], how='left')


'''
new_df_lst = []
for i in chromesome_lst:
	chrm_df_list = [extract_chr(j,i) for j in df_list]

	pos_set = create_pos_set(chrm_df_list)

	temp_df_list = []
	for j in chrm_df_list:
		temp_df = add_homo_ref(j,pos_set,i)
		temp_df_list.append(temp_df)

	temp = pd.concat(temp_df_list, ignore_index=True)
	new_df_lst.append(temp)







chrm1 = [extract_chr(i,'chr1') for i in df_list]
pos_nested_list = [i.POS for i in chrm1]
pos_list =[]
for i in pos_nested_list:
	for j in i:
		pos_list.append(j)
pos_set = set(pos_list)
temp = chrm1[0]
temp_pos_lst = [i for i in temp.POS]

not_in_lst = []
for i in pos_set:
	if (i not in temp_pos_lst):
		not_in_lst.append(i)

to_append = [['chr1', i, 'Homozygous Reference'] for i in not_in_lst]
col_names = temp.columns
to_add = pd.DataFrame(to_append, columns=col_names)
new_temp = pd.concat([temp, to_add])
print(temp.head())
'''