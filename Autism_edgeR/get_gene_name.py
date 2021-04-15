#python3

import numpy as np 
import pandas as pd 

df = pd.read_csv('16p11_fpkm_avg.csv',header=0)

df15 = pd.read_csv('16p11_table.csv',header=0)

lst =[]
for i in range(df15.shape[0]):
	x = df15.iloc[i,0]
	lst.append(df.iloc[x,0])

df15['Short Gene Name'] = lst

df15.to_csv(r'16p11_table_names.csv')