#python3
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df15 = pd.read_excel('16p11_fpkm.xlsx', header=0,index_col=0,engine='openpyxl')

subset = df15.iloc[:,:59]

print(subset.head())
subset.to_csv(r'16p11_fpkm_rep.csv')