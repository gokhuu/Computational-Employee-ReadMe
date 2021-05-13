import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('new_fpkm_threshold.csv', header=0, index_col = 0, low_memory=False)
df = df.drop('Autism',axis=1)

clustermap = sns.clustermap(df, metric='correlation',standard_scale=1,cmap='mako')
clustermap.savefig('heatmap.png')