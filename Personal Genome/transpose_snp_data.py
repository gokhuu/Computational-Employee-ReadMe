import numpy as np 
import pandas as pd 

df = pd.read_csv('SNP_data.csv', header=0, index_col=0)

ref = {'Genotype Category: 14765x2':'14765x2',
       'Genotype Category: 14763x7':'14763x7', 'Genotype Category: 14799x1':'14799x1',
       'Genotype Category: 14858x3':'14858x3', 'Genotype Category: 14746x8':'14746x8',
       'Genotype Category: 14824x13':'14824x13', 'Genotype Category: 14739x13':'14739x13',
       'Genotype Category: 14704x7':'14704x7', 'Genotype Category: 14710x6':'14710x6',
       'Genotype Category: 14781x16':'14781x16', 'Genotype Category: 1601':'1601',
       'Genotype Category: 1401':'1401', 'Genotype Category: 902':'902',
       'Genotype Category: 901':'901', 'Genotype Category: 1001':'1001',
       'Genotype Category: 110':'110', 'Genotype Category: 111':'111',
       'Genotype Category: 112':'112', 'Genotype Category: 114':'114',
       'Genotype Category: 115':'115', 'Genotype Category: 116':'116',
       'Genotype Category: 117':'117', 'Genotype Category: GM23716':'GM23716',
       'Genotype Category: GM23720':'GM23720', 'Genotype Category: GM25256':'GM25256',
       'Genotype Category: PGP1':'PGP1'}

df.rename(columns=ref, inplace=True)
chrmPos = []

for i in range(df.shape[0]):
	s = str(df.CHROM[i]) + "@" + str(df.POS[i])
	chrmPos.append(s)

df.append(chrmPos)
df = df.set_index()
print(df.head())