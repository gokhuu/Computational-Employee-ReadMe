#python3
'''
Author: Brandon Khuu
Last update: 5/4/2021

Import a large number of csv files and 
concat them into one larger dataframe
'''

#import libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from collections import Counter
from functools import reduce

list_of_csv = [
'VCFs/VCF_csv_2/ED1.csv','VCFs/VCF_csv_2/ED2.csv','VCFs/VCF_csv_2/ED3.csv','VCFs/VCF_csv_2/ED4.csv',
'VCFs/VCF_csv_2/ED5.csv','VCFs/VCF_csv_2/ED6.csv','VCFs/VCF_csv_2/ED7.csv','VCFs/VCF_csv_2/ED8.csv',
'VCFs/VCF_csv_2/ED9.csv','VCFs/VCF_csv_2/ED10.csv','VCFs/VCF_csv_2/ED11.csv','VCFs/VCF_csv_2/ED12.csv',
'VCFs/VCF_csv_2/ED13.csv','VCFs/VCF_csv_2/ED14.csv','VCFs/VCF_csv_2/ED15.csv','VCFs/VCF_csv_2/ED16.csv',
'VCFs/VCF_csv_2/ED17.csv','VCFs/VCF_csv_2/ED18.csv','VCFs/VCF_csv_2/ED19.csv','VCFs/VCF_csv_2/ED20.csv',
'VCFs/VCF_csv_2/ED21.csv','VCFs/VCF_csv_2/ED22.csv','VCFs/VCF_csv_2/ED23.csv','VCFs/VCF_csv_2/ED24.csv',
'VCFs/VCF_csv_2/ED25.csv','VCFs/VCF_csv_2/ED26.csv']

chromesome_lst = ['chr1', 'chr2','chr3','chr4','chr5','chr6','chr7',
'chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
'chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']

reference_dict = {
'ED1':'14765x2','ED2':'14763x7','ED3':'14799x1','ED4':'14858x3','ED5':'14746x8','ED6':'14824x13',
'ED7':'14739x13','ED8':'','ED9':'14710x6','ED10':'14781x16','ED11':'1601','ED12':'1401',
'ED13':'902','ED14':'901','ED15':'1001','ED16':'BXS0110','ED17':'BXS0111','ED18':'BYS0112',
'ED19':'BXS0114','ED20':'BXS0115','ED21':'BXS0116','ED22':'BXS0117','ED23':'GM23716','ED24':'GM23720',
'ED25':'GM25256','ED26':'PGP1'}

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

def converge_list(lst):
	#sort by POS
	for i in lst:
		i = i.sort_values(by='POS')

	#create base dataframe to merge onto
	df = lst[0]

	#create and merge series
	for i in range(1,len(lst)):
		temp = lst[i]
		series = temp.iloc[:,1:]

		df = df.merge(series, on='POS')

	return df

def create_chrm_split(df_lst, chrm_lst):
	lst = [] #final list

	#iterate through chromosome list
	for i in chrm_lst:
		
		#create chromesome dataframe list
		temp_lst = [extract_chr(j,i) for j in df_list]
		
		#create position set
		pos_set = create_pos_set(temp_lst)

		#add homozygous reference SNPs
		temp = [add_homo_ref(j, pos_set, i) for j in temp_lst]

		#append to lst
		lst.append(temp)
	
	return lst

df_list = storage_lst(list_of_csv)
chrm_split_list = create_chrm_split(df_list, chromesome_lst)
merged_split_list = [converge_list(i) for i in chrm_split_list]

df = pd.concat(merged_split_list,ignore_index=True)
df.to_csv(r'SNP_data.csv')