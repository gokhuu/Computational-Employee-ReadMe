#python3

import numpy as np 
import pandas as pd 
import math

def log_normalization(df):
	dim_x = len(df.columns)
	dim_y = len(df.iloc[:,0])

	for i in range(dim_x):
		for j in range(dim_y):
			df.iloc[j,i] = math.log2(1+df.iloc[j,i])

	return df

x = pd.read_csv('fpkm_expression_no_zero.csv')

x = x.drop('Unnamed: 0', axis=1)

y = log_normalization(x)

y.to_csv('fpkm_expression_log2.csv')