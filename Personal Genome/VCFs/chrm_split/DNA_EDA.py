#python3
import numpy as np 
import pandas as pd 
import allel as al

#chrm list
lst = ['chr1_replicates.csv', 'chr2_replicates.csv','chr3_replicates.csv','chr4_replicates.csv','chr5_replicates.csv',
'chr6_replicates.csv','chr7_replicates.csv','chr8_replicates.csv','chr9_replicates.csv','chr10_replicates.csv',
'chr11_replicates.csv','chr12_replicates.csv','chr13_replicates.csv','chr14_replicates.csv','chr15_replicates.csv',
'chr16_replicates.csv','chr17_replicates.csv','chr18_replicates.csv','chr19_replicates.csv','chr20_replicates.csv',
'chr21_replicates.csv','chr22_replicates.csv','chrX_replicates.csv','chrY_replicates.csv']

def read_dna_csv(filename):

	#drops replicates list
	cols_to_drop=['PGP1-3', 'PGP1-2', 'GM25256-3', 'GM25256-2',
       'GM23720-3', 'GM23720-2', 'GM23716-3', 'GM23716-2', 'BXS0117-3',
       'BXS0117-2', 'BXS0116-3', 'BXS0116-2', 'BXS0115-3', 'BXS0115-2',
       'BXS0114-3', 'BXS0114-2', 'BYS0112-3', 'BYS0112-2', 'BXS0111-3',
       'BXS0111-2', 'BXS0110-3', 'BXS0110-2', '1001-3', '1001-2', '901-3',
       '901-2', '902-3', '902-2', '1401-3', '1401-2', '1601-3', '1601-2',
       '14781x16-3', '14781x16-2', '14739x3-2', '14824x13-3', '14824x13-2',
       '14746x8-2', '14858x3-3', '14858x3-2', '14799x1-3', '14799x1-2',
       '14763x7-3', '14763x7-2', '14765x2-3', '14765x2-2']

    #read csv
	df = pd.read_csv(filename, header=0, index_col=0)
	
	#drop replicates
	df = df.drop(cols_to_drop, axis=1)

	#create Chrm@Pos columns
	chrmPos = []
	for i in range(df.shape[0]):
		s = str(df.CHROM[i]) + '@' + str(df.POS[i])
		chrmPos.append(s)

    #append to dataframe and prep for analysis
	df.insert(loc=0, column='Samples', value=chrmPos)
	df = df.drop(['CHROM','POS'], axis=1)
	df = df.set_index('Samples')
	df = df.T

	return df

df_list = []
for i in lst:
	df_list.append(read_dna_csv(i))

df = pd.concat(df_list, ignore_index=True)

print(df.head())