#python3

import numpy as np 
import pandas as pd 
import math

'''
def threshold_data(df,l,n):
	df["Mean"] = df.mean(axis=1)
	lst = []

	
	for i in range(l):
		if df.Mean[i] < n:
			lst.append(i)

	return lst

raw_fpkm = pd.read_csv('fpkm_expression.csv')

l = len(raw_fpkm.iloc[:,0])

x = threshold_data(raw_fpkm, l, 2)

print(x)
'''

x = pd.read_csv('fpkm_expression_no_zero.csv')

print(x.iloc[:,0])