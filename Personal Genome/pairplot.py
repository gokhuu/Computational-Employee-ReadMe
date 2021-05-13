#!/bin/python

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('new_fpkm_threshold.csv', header=0, index_col=0, low_memory=False)

y = df.Autism
x = df.iloc[:,1:]

cols = [i for i in x.columns]

fig,ax = plt.subplots()
im = ax.imshow(x)

ax.set_xticks(range(len(cols)))
ax.set_yticks(range(len(cols)))

ax.set_xticklabels(cols)
ax.set_yticklabels(cols)

plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
fig.tight_layout()
plt.savefig('heatmap_dendro.png', dpi=4000.0)