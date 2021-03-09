#python3

import numpy as np 
import pandas as pd

def gene_list(lst1, lst2):
	final = []

	for i in lst1:
		final.append(lst2[i])

	return final

#Load data

#read count data
raw_rc_data = pd.read_csv('count_expression.csv')
rc_data = pd.read_csv('count_expression_no_zero.csv')
#rc_data_log2 = pd.read_csv('count_expression_log2.csv')
#rc_data_int = pd.read_csv('Count_expression_INT.csv')

#fpkm data
raw_fpkm_data = pd.read_csv('fpkm_expression.csv')
fpkm_data = pd.read_csv('fpkm_expression_no_zero.csv')
#fpkm_data_log2 = pd.read_csv('fpkm_expression_log2.csv')
#fpkm_data_int = pd.read_csv('fpkm_expression_INT.csv')

#Load gene list
gene_data = pd.read_csv('expression_desc.csv')
gene_id = gene_data.iloc[:,3]

#threshold_list
col = rc_data.iloc[:,0]
cols = fpkm_data.iloc[:,0]


rc_gene_col = gene_list(col, gene_id)
fpkm_gene_col = gene_list(cols, gene_id)


#raw_rc_data.insert(0, 'Gene', gene_id)
#rc_data.insert(0, 'Gene', rc_gene_col)
#rc_data_log2.insert(0, 'Gene', rc_gene_col)
#rc_data_int.insert(0,'Gene', rc_gene_col)
'''

#print(len(fpkm_data_log2.iloc[:,0]))

#raw_fpkm_data.insert(0, 'Gene', gene_id)
#fpkm_data.insert(0, 'Gene', fpkm_gene_col)
#fpkm_data_log2.insert(0, 'Gene', fpkm_gene_col)
#fpkm_data_int.insert(0,'Gene', fpkm_gene_col)

'''

df = pd.Series((v for v in fpkm_gene_col))
df.to_csv(r'fpkm_gene.csv')