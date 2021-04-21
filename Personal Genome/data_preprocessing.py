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
print(df.Mean)

#lst = []
'''
for i in range(df.shape[0]):
	if df.Mean[i] < 2:
		lst.append(i)

df = df.drop(lst,axis=1)
df = df.drop('Mean', axis=1)
print(lst)
df.set_index('Unnamed: 0')
print(df.head())
'''