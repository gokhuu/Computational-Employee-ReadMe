#python3
import numpy as np
import pandas as pd 

df15 = pd.read_csv('15q_dup_fpkm_avg.csv',header=0)

df15['Mean'] = df15.mean(axis=1)

lst = []
for i in range(df15.shape[0]):
	if df15.Mean[i] < 2:
		lst.append(i)

df15 = df15.drop(lst)
df15 = df15.drop('Mean',axis=1)

df15 = df15.set_index('Short Gene Name')

df15.to_csv(r'15q_dup_fpkm_avg_threshold.csv')