#python3
import numpy as np 
import pandas as pd 

#Autism fpkm files
df = pd.read_csv('Organoid Files/all_autism_fpkm_T.csv',header=0,index_col=0)

print(df.head())