#python3
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#import data
rna = pd.read_csv('Organoid Files/all_autism_fpkm_iqr_1.5_outliers_multi_class.csv', header=0,index_col=0)
dna = pd.read_csv('DNA_csv/dna_table_edit_t_mutli_replicates.csv', header=0,index_col=0)
print(rna.head())
print(dna.head())

#label endcoding
from sklearn.preprocessing import LabelEncoder
cat_features = [i for i in dna.columns]
encoder = LabelEncoder()

#merge data
merged = rna.merge(dna, how='inner', left_index = True, right_index=True)
merged[cat_features] = merged[cat_features].apply(encoder.fit_transform)
print(merged.head())

merged.to_csv(r'merged_data.csv')