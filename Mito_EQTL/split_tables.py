#python3
import numpy as np 
import pandas as pd 

df_genotype = pd.read_csv('mito_genotypes.csv')
df_expression = pd.read_csv('Expression_Profile.GRCh37.gene.txt', sep='\t')

#genotype dataframe
allele = df_genotype.iloc[:,6]

#expression dataframe (count)
count_expression = df_expression.iloc[:,9:68]
#count_expression.to_csv(r'count_expression.csv')

#expression dataframe (fpkm)
fpkm_expression = df_expression.iloc[:,68:]
#fpkm_expression.to_csv(r'fpkm_expression.csv')

'''
gender = df_genotype.iloc[:,7]
age = df_genotype.iloc[:,8]
race = df_genotype.iloc[:,9]

temp_gen = []
temp_age = []
temp_race = []

for i in range(len(gender)):
	temp_gen.append(gender[i])
	temp_age.append(age[i])
	temp_race.append(race[i])

temp = [temp_gen, temp_age, temp_race]
covariates = pd.DataFrame(temp)

covariates.to_csv(r'mito_covariates.csv')
'''

'''
#transpose and export allele dataframe
temp = []
for i in allele:
	temp.append(i)

allele_transpose = pd.DataFrame([temp])
allele_transpose.to_csv(r'allele.csv')
'''
