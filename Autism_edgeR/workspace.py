#python3

import numpy as np 
import pandas as pd 

df = pd.read_csv("results_lm2_del_vs_ctrl.txt", sep='\t')


df.to_csv(r'16p11.csv')

