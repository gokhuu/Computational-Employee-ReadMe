#python3

import numpy as np 
import pandas as pd 

df = pd.read_csv('16p11_pc.txt',sep='\t', header=None)

x = df.iloc[:,0]

x.to_csv('16p11_pc1.csv')