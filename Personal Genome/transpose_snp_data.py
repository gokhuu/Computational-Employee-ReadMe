import numpy as np 
import pandas as pd 

df = pd.read_csv('SNP_data.csv',header=0)

ref = {'110-1':'BXS0110-1','110-2':'BXS0110-2','110-3':'BXS0110-3',
		'111-1':'BXS0111-1','111-2':'BXS0111-2','111-3':'BXS0111-3',
       '112-1':'BYS0112-1','112-2':'BYS0112-2','112-3':'BYS0112-3',
       '114-1':'BXS0114-1','114-2':'BXS0114-2','114-3':'BXS0114-3',
       '115-1':'BXS0115-1','115-2':'BXS0115-2','115-3':'BXS0115-3',
       '116-1':'BXS0116-1','116-2':'BXS0116-2','116-3':'BXS0116-3',
       '117-1':'BXS0117-1','117-2':'BXS0117-2','117-3':'BXS0117-3'}

df.rename(columns=ref, inplace=True)
chrmPos = []

for i in range(df.shape[0]):
	s = str(df.CHROM[i]) + "@" + str(df.POS[i])
	chrmPos.append(s)

df.insert(loc=0, column='Samples', value=chrmPos)

df = df.drop(['CHROM','POS'], axis=1)

df_t=df.T
print(df_t.head())
df_t.to_csv(r'SNP_data_T.csv')