
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('fpkm_corr.csv', header=0, index_col=0, low_memory=False)
fig = sns.pairplot(df, hue='Autism')
fig.savefig('output.png')

