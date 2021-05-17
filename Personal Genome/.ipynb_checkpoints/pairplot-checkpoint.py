#!/bin/python

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('new_fpkm_threshold.csv', header=0, index_col=0)
sns.set()
sns_pairplot = sns.pairplot(df, hue='Autism')
sns_pairplot.savefig('pairplot.png')