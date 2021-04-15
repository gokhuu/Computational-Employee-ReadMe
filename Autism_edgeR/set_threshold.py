#python3
import numpy as np
import pandas as pd 

df15 = pd.read_csv('16p11_fpkm_rep.csv',header=0)

df15['Mean'] = df15.mean(axis=1)

lst = []
for i in range(df15.shape[0]):
	if df15.Mean[i] < 2:
		lst.append(i)

df15 = df15.drop(lst)
df15 = df15.drop('Mean',axis=1)

df15 = df15.set_index('Short Gene Name')

#df15.to_csv(r'16p11_fpkm_rep_threshold.csv')

print(df15.columns)