import numpy as np 
import pandas as pd 
import allel as al

lst = ['chr1_replicates.csv', 'chr2_replicates.csv','chr3_replicates.csv','chr4_replicates.csv','chr5_replicates.csv',
'chr6_replicates.csv','chr7_replicates.csv','chr8_replicates.csv','chr9_replicates.csv','chr10_replicates.csv',
'chr11_replicates.csv','chr12_replicates.csv','chr13_replicates.csv','chr14_replicates.csv','chr15_replicates.csv',
'chr16_replicates.csv','chr17_replicates.csv','chr18_replicates.csv','chr19_replicates.csv','chr20_replicates.csv',
'chr21_replicates.csv','chr22_replicates.csv','chrX_replicates.csv','chrY_replicates.csv']

new_lst = ['eqtl/chr1_replicates.csv', 'eqtl/chr2_replicates.csv','eqtl/chr3_replicates.csv','eqtl/chr4_replicates.csv','eqtl/chr5_replicates.csv',
'eqtl/chr6_replicates.csv','eqtl/chr7_replicates.csv','eqtl/chr8_replicates.csv','eqtl/chr9_replicates.csv','eqtl/chr10_replicates.csv',
'eqtl/chr11_replicates.csv','eqtl/chr12_replicates.csv','eqtl/chr13_replicates.csv','eqtl/chr14_replicates.csv','eqtl/chr15_replicates.csv',
'eqtl/chr16_replicates.csv','eqtl/chr17_replicates.csv','eqtl/chr18_replicates.csv','eqtl/chr19_replicates.csv','eqtl/chr20_replicates.csv',
'eqtl/chr21_replicates.csv','eqtl/chr22_replicates.csv','eqtl/chrX_replicates.csv','eqtl/chrY_replicates.csv']


ind_list = ['PGP1-1', 'PGP1-2', 'PGP1-3', 'GM23716-1', 'GM23716-2', 
'GM23716-3', 'GM23720-1', 'GM23720-2', 'GM23720-3', 'GM25256-1', 
'GM25256-2', 'GM25256-3', 'BXS0110-1', 'BXS0110-2', 'BXS0110-3', 
'BXS0111-1', 'BXS0111-2', 'BXS0111-3', 'BYS0112-1', 'BYS0112-2', 
'BYS0112-3', 'BXS0114-1', 'BXS0114-2', 'BXS0114-3', 'BXS0115-1', 
'BXS0115-2', 'BXS0115-3', 'BXS0116-1', 'BXS0116-2', 'BXS0116-3', 
'BXS0117-1', 'BXS0117-2', 'BXS0117-3', '902-1', '902-2', '902-3', 
'1601-1', '1601-2', '1601-3', '1401-1', '1401-2', '1401-3', '1001-1', 
'1001-2', '1001-3', '901-1', '901-2', '901-3', '14858x3-1', '14858x3-2', 
'14858x3-3', '14799x1-1', '14799x1-2', '14799x1-3', '14824x13-1', '14824x13-2', 
'14824x13-3', '14763x7-1', '14763x7-2', '14763x7-3', '14739x3-1', '14739x3-2', 
'14765x2-1', '14765x2-2', '14765x2-3', '14710x6-1', '14781x16-1', '14781x16-2', 
'14781x16-3', '14746x8-1', '14746x8-2']


df = pd.read_csv(lst[0], header=0, index_col=0)
cols_to_drop=['PGP1-3', 'PGP1-2', 'GM25256-3', 'GM25256-2',
       'GM23720-3', 'GM23720-2', 'GM23716-3', 'GM23716-2', 'BXS0117-3',
       'BXS0117-2', 'BXS0116-3', 'BXS0116-2', 'BXS0115-3', 'BXS0115-2',
       'BXS0114-3', 'BXS0114-2', 'BYS0112-3', 'BYS0112-2', 'BXS0111-3',
       'BXS0111-2', 'BXS0110-3', 'BXS0110-2', '1001-3', '1001-2', '901-3',
       '901-2', '902-3', '902-2', '1401-3', '1401-2', '1601-3', '1601-2',
       '14781x16-3', '14781x16-2', '14739x3-2', '14824x13-3', '14824x13-2',
       '14746x8-2', '14858x3-3', '14858x3-2', '14799x1-3', '14799x1-2',
       '14763x7-3', '14763x7-2', '14765x2-3', '14765x2-2']
df = df.drop(cols_to_drop, axis=1)

chrmPos = []
for i in range(df.shape[0]):
    s = str(df.CHROM[i]) + '@' + str(df.POS[i])
    chrmPos.append(s)
    
#append to dataframe and prep for analysis
df.insert(loc=0, column='Samples', value=chrmPos)
df = df.drop(['CHROM','POS'], axis=1)
df = df.set_index('Samples')
df = df.T


reference_dict = {'Homozygous Reference':[0,0], 'Heterozygous Alternate':[0,1], 
					'Heterozygous Alternate 1/2':[0,2],'Homozygous Alternate':[1,1]}

#df = df.replace(reference_dict)

#print(df.head())
gt_array =[]

for i in df.index:
	temp = []
	for j in df.loc[i]:
		temp.append(reference_dict[j])
	gt_array.append(temp)

g = al.GenotypeArray(gt_array)

print('Heterozygosity observed: ')
print(al.heterozygosity_observed(g)) 
print("")

af = g.count_alleles().to_frequencies()
print(al.heterozygosity_expected(af,ploidy=2))