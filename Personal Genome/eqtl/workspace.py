import numpy as np 
import pandas as pd 
import allel as al

lst = ['chr1_replicates.csv', 'chr2_replicates.csv','chr3_replicates.csv','chr4_replicates.csv','chr5_replicates.csv',
'chr6_replicates.csv','chr7_replicates.csv','chr8_replicates.csv','chr9_replicates.csv','chr10_replicates.csv',
'chr11_replicates.csv','chr12_replicates.csv','chr13_replicates.csv','chr14_replicates.csv','chr15_replicates.csv',
'chr16_replicates.csv','chr17_replicates.csv','chr18_replicates.csv','chr19_replicates.csv','chr20_replicates.csv',
'chr21_replicates.csv','chr22_replicates.csv','chrX_replicates.csv','chrY_replicates.csv']

df = pd.read_csv(lst[0], header=0, index_col=0)
print(df.head())
