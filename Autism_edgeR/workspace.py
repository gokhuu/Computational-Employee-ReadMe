#python3
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('workspace.csv',header=0)

gene = list(df.gene)

ref = list(df.Ref)

comp = list(df.new)
comp = comp[:11205]

d = {i:j for i in ref for j in gene}

lst = [d[i] for i in comp]
