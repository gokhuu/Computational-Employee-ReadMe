#python3
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df15 = pd.read_csv('15q_dup_pval.csv',header=0)

sns.distplot(df15['p_value w/ covariate'],hist=True, kde=True,bins=int(180/5),color='darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})


plt.title('15q_dup w/covariate pval density histogram')
plt.xlabel('P Value')
plt.ylabel('Density')

plt.show()