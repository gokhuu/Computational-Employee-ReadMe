import numpy as np 
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('SNP_data.csv', header=0, index_col=0)

le = LabelEncoder()
cols = [i for i in df.columns]
cols.pop(0)
cols.pop(0)

df[cols] = df[cols].apply(le.fit_transform)
print(df.describe())