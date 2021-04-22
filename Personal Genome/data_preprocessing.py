#python3
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#Autism fpkm files
df = pd.read_csv('Organoid Files/all_autism_fpkm.csv',header=0, low_memory=False)


#apply threshold
y = df['Unnamed: 0']
df = df.drop('Unnamed: 0', axis=1)
df['Mean'] = df.mean(axis=1)

lst = []

for i in range(df.shape[0]):
	if df.Mean[i] < 2:
		lst.append(i)


df = df.drop(lst)
df = df.drop('Mean', axis=1)
print(df.head())

for i in lst:
	y = y.drop(i)
print(df.shape[0])
print(y.shape[0])

df = df.set_index(y)

df_t = df.T

df_t.to_csv(r'all_autism_fpkm_t_threshold.csv')
