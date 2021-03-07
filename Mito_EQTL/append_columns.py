#python3

import numpy as np 
import pandas as pd


def threshold_list(df,n):
	df["Mean"] = df.mean(axis=1)
	l = len(df.iloc[:,0])
	lst = []

	for i in range(l):
		if df.Mean[i] < n:
			lst.append(i)

	return lst

def drop_genes(lst, gene):
	for i in lst:
		gene = gene.drop(i)

	return gene

#Load data
#read count data
raw_rc_data = pd.read_csv('count_expression.csv')
rc_data = pd.read_csv('count_expression_no_zero.csv')
rc_data_log2 = pd.read_csv('count_expression_log2.csv')
rc_data_int = pd.read_csv('Count_expression_INT.csv')

#fpkm data
raw_fpkm_data = pd.read_csv('fpkm_expression.csv')
fpkm_data = pd.read_csv('fpkm_expression_no_zero.csv')
fpkm_data_log2 = pd.read_csv('fpkm_expression_log2_normalization.csv')
fpkm_data_int = pd.read_csv('fpkm_expression_INT.csv')

#Load gene list
gene_data = pd.read_csv('expression_desc.csv')
gene_id = gene_data.iloc[:,3]

#threshold_list
rc_thresh_list = threshold_list(raw_rc_data,10)

rc_genes = drop_genes(rc_thresh_list,gene_id)

print(len(rc_thresh_list))