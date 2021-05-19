import numpy as np 
import pandas as pd

#rna = pd.read_csv('new_fpkm_threshold.csv',header=0, index_col=0, low_memory=False)
dna = pd.read_csv('SNP_data.csv',header=0,low_memory=False)

#Transpose and edit DNA dataframe
ref = {'110-1':'BXS0110-1','110-2':'BXS0110-2','110-3':'BXS0110-3',
		'111-1':'BXS0111-1','111-2':'BXS0111-2','111-3':'BXS0111-3',
       '112-1':'BYS0112-1','112-2':'BYS0112-2','112-3':'BYS0112-3',
       '114-1':'BXS0114-1','114-2':'BXS0114-2','114-3':'BXS0114-3',
       '115-1':'BXS0115-1','115-2':'BXS0115-2','115-3':'BXS0115-3',
       '116-1':'BXS0116-1','116-2':'BXS0116-2','116-3':'BXS0116-3',
       '117-1':'BXS0117-1','117-2':'BXS0117-2','117-3':'BXS0117-3'}

reference_dict = {'Homozygous Reference':'0', 'Heterozygous Alternate':'1', 
					'Heterozygous Alternate 2':'3','Homozygous Alternate':'2'}


dna = dna.drop('0',axis=1)

dna.rename(columns=ref, inplace=True)
chrmPos = []

for i in range(dna.shape[0]):
	s = str(dna.CHROM[i]) + "@" + str(dna.POS[i])
	chrmPos.append(s)

dna.insert(loc=0, column='Samples', value=chrmPos)

dna = dna.drop(['CHROM','POS'], axis=1)
dna = dna.set_index('Samples')
dna = dna.T
#print(dna.head())
#Merge dataframes
#df = rna.merge(dna, how='left', left_index=True, right_index=True)

#remove SNPs that are all Homo Ref

same = []
count = 0
for i in dna.columns:
	temp = dna.get(i)
	#count = 0
	for j in temp:
		if j == 'Heterozygous Alternate 2':
			count+=1
	#if count >= 69:
print(count)

#dna = dna.drop(same, axis=1)
#print(dna.head())

'''
to_drop = []
for i in dna.columns:
	temp = dna.get(i)
	count = 0
	for j in temp:
		if j != 'Homozygous Reference':
			count+=1
	if count <= 25:
		to_drop.append(i)
dna = dna.drop(to_drop, axis=1)
print(dna.head())


#Encode DNA columns
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
cat_features = [i for i in dna.columns]
dna[cat_features] = dna[cat_features].apply(encoder.fit_transform)
'''