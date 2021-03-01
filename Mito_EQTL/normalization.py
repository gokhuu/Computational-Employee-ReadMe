#python3
import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler 

count_exp = pd.read_csv('count_expression_no_index.csv')
fpkm_exp = pd.read_csv('fpkm_expression.csv')

scaler = StandardScaler()
'''
#################################################
count_exp['Mean'] = count_exp.mean(axis=1)
l = len(count_exp.iloc[:,0])
lst = []

for i in range(l):
	if count_exp.Mean[i] < 10:
		lst.append(i)

count_exp_edit = count_exp.drop(lst)
count_exp_edit = count_exp_edit.drop('Mean', axis=1)
count_exp_edit.to_csv('count_expression_no_zero.csv')

count_exp_log_norm = np.log1p(count_exp_edit)
count_exp_standard_norm = pd.DataFrame(scaler.fit_transform(count_exp_edit), columns=count_exp_edit.columns)

count_exp_log_norm.to_csv(r'count_expression_log_norm.csv')
count_exp_standard_norm.to_csv(r'count_expression_standard_norm.csv')

'''
#####################################################
fpkm_exp['Mean'] = fpkm_exp.mean(axis=1)
ll = len(fpkm_exp.iloc[:,0])
ls = []

for i in range(ll):
	if fpkm_exp.Mean[i] < 2:
		ls.append(i)

fpkm_exp_edit = fpkm_exp.drop(ls)
fpkm_exp_edit = fpkm_exp_edit.drop('Mean', axis = 1)

fpkm_exp_edit.to_csv('fpkm_expression_no_zero.csv')

fpkm_exp_log_norm = np.log1p(fpkm_exp_edit)
fpkm_exp_standrad_norm = pd.DataFrame(scaler.fit_transform(fpkm_exp_edit), columns=fpkm_exp_edit.columns)

fpkm_exp_log_norm.to_csv(r'fpkm_expression_log_norm.csv')
fpkm_exp_standrad_norm.to_csv(r'fpkm_expression_standrad_norm.csv')
