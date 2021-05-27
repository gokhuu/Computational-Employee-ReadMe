import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.decomposition import PCA

'''
new_csv_lst = ['VCFs/chrm_split/chr1_replicates.csv', 'VCFs/chrm_split/chr2_replicates.csv','VCFs/chrm_split/chr3_replicates.csv','VCFs/chrm_split/chr4_replicates.csv','VCFs/chrm_split/chr5_replicates.csv',
'VCFs/chrm_split/chr6_replicates.csv','VCFs/chrm_split/chr7_replicates.csv','VCFs/chrm_split/chr8_replicates.csv','VCFs/chrm_split/chr9_replicates.csv','VCFs/chrm_split/chr10_replicates.csv',
'VCFs/chrm_split/chr11_replicates.csv','VCFs/chrm_split/chr12_replicates.csv','VCFs/chrm_split/chr13_replicates.csv','VCFs/chrm_split/chr14_replicates.csv','VCFs/chrm_split/chr15_replicates.csv',
'VCFs/chrm_split/chr16_replicates.csv','VCFs/chrm_split/chr17_replicates.csv','VCFs/chrm_split/chr18_replicates.csv','VCFs/chrm_split/chr19_replicates.csv','VCFs/chrm_split/chr20_replicates.csv',
'VCFs/chrm_split/chr21_replicates.csv','VCFs/chrm_split/chr22_replicates.csv','VCFs/chrm_split/chrX_replicates.csv','VCFs/chrm_split/chrY_replicates.csv']

def storage_lst(file_lst):
	lst = []
	for i in file_lst:
		df = pd.read_csv(i, header=0, index_col=0)
		lst.append(df)
	return lst

df_list = storage_lst(new_csv_lst)

df = pd.concat(df_list,ignore_index=True)

chrmPos = []
for i in range(df.shape[0]):
    s = str(df.CHROM[i]) + '@' + str(df.POS[i])
    chrmPos.append(s)
    
#append to dataframe and prep for analysis
df.insert(loc=0, column='Samples', value=chrmPos)
df = df.drop(['CHROM','POS'], axis=1)
df = df.set_index('Samples')
df = df.T

reference_dict = {'Homozygous Reference':1, 'Heterozygous Alternate':2, 
					'Heterozygous Alternate 1/2':3,'Homozygous Alternate':4}

df = df.replace(reference_dict)


dic = {'PGP1-3':0, 'PGP1-2':0, 'GM25256-3':0, 'GM25256-2':0, 'GM23720-3':0, 'GM23720-2':0,
       'GM23716-3':0, 'GM23716-2':0, 'BXS0117-3':0, 'BXS0117-2':0, 'BXS0116-3':0,
       'BXS0116-2':0, 'BXS0115-3':0, 'BXS0115-2':0, 'BXS0114-3':0, 'BXS0114-2':0,
       'BYS0112-3':0, 'BYS0112-2':0, 'BXS0111-3':0, 'BXS0111-2':0, 'BXS0110-3':0,
       'BXS0110-2':0, '1001-3':1, '1001-2':1, '901-3':1, '901-2':1, '902-3':0, '902-2':0,
       '1401-3':1, '1401-2':1, '1601-3':1, '1601-2':1, '14781x16-3':2, '14781x16-2':2,
       '14739x3-2':2, '14824x13-3':2, '14824x13-2':2, '14746x8-2':2, '14858x3-3':2,
       '14858x3-2':2, '14799x1-3':2, '14799x1-2':2, '14763x7-3':2, '14763x7-2':2,
       '14765x2-3':2, '14765x2-2':2, '14765x2-1':2, '14763x7-1':2, '14799x1-1':2,
       '14858x3-1':2, '14746x8-1':2, '14824x13-1':2, '14739x3-1':2, '14710x6-1':2,
       '14781x16-1':2, '1601-1':1, '1401-1':1, '902-1':0, '901-1':1, '1001-1':1,
       'BXS0110-1':0, 'BXS0111-1':0, 'BYS0112-1':0, 'BXS0114-1':0, 'BXS0115-1':0,
       'BXS0116-1':0, 'BXS0117-1':0, 'GM23716-1':0, 'GM23720-1':0, 'GM25256-1':0,
       'PGP1-1':0}

autism = [dic[i] for i in dic]
df.insert(loc=0, column='Autism', value=autism)


pca = PCA(n_components=2)
x_pca = pca.fit_transform(df)
plot = plt.scatter(x_pca[:,0], x_pca[:,1], c=df['Autism'])
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')

plot.figure.savefig('DNA_PCA.png')


clustermap = sns.clustermap(df, metric='correlation',standard_scale=1,cmap='mako')
clustermap.savefig('dna_heatmap.png')
'''

df = pd.read_csv('new_fpkm_threshold.csv',header=0, index_col=0)

lst = [i for i in df.index]
print(lst)