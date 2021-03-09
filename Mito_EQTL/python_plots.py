#python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors

fpkm_log2_pvalues = pd.read_csv('fpkm_log2_pvalues.csv')

n, bins, patches = plt.hist(fpkm_log2_pvalues, 100, facecolor='blue', alpha=0.5)
plt.show()