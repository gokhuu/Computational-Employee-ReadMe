# python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df15 = pd.read_csv('16p11_table.csv', header=0)

print(df15.head())

sns.distplot(df15['PValue'], hist=True, kde=True, bins=int(150 / 5), color='darkblue', hist_kws={'edgecolor': 'black'}, kde_kws={'linewidth': 4})


plt.title('16p11 w/covariate pval density histogram')
plt.xlabel('P Value')
plt.ylabel('Density')

plt.show()
