#python3
import numpy as np 
import pandas as pd 

#list of csv string names
list_of_csv = [
'VCFs/VCF_csv/ED1.csv','VCFs/VCF_csv/ED2.csv','VCFs/VCF_csv/ED3.csv','VCFs/VCF_csv/ED4.csv',
'VCFs/VCF_csv/ED5.csv','VCFs/VCF_csv/ED6.csv','VCFs/VCF_csv/ED7.csv','VCFs/VCF_csv/ED8.csv',
'VCFs/VCF_csv/ED9.csv','VCFs/VCF_csv/ED10.csv','VCFs/VCF_csv/ED11.csv','VCFs/VCF_csv/ED12.csv',
'VCFs/VCF_csv/ED13.csv','VCFs/VCF_csv/ED14.csv','VCFs/VCF_csv/ED15.csv','VCFs/VCF_csv/ED16.csv',
'VCFs/VCF_csv/ED17.csv','VCFs/VCF_csv/ED18.csv','VCFs/VCF_csv/ED19.csv','VCFs/VCF_csv/ED20.csv',
'VCFs/VCF_csv/ED21.csv','VCFs/VCF_csv/ED22.csv','VCFs/VCF_csv/ED23.csv','VCFs/VCF_csv/ED24.csv',
'VCFs/VCF_csv/ED25.csv','VCFs/VCF_csv/ED26.csv']

list_of_csv = [
'VCFs/VCF_csv/ED1.csv','VCFs/VCF_csv/ED2.csv','VCFs/VCF_csv/ED3.csv','VCFs/VCF_csv/ED4.csv',
'VCFs/VCF_csv/ED5.csv','VCFs/VCF_csv/ED6.csv','VCFs/VCF_csv/ED7.csv','VCFs/VCF_csv/ED8.csv',
'VCFs/VCF_csv/ED9.csv','VCFs/VCF_csv/ED10.csv','VCFs/VCF_csv/ED11.csv','VCFs/VCF_csv/ED12.csv',
'VCFs/VCF_csv/ED13.csv','VCFs/VCF_csv/ED14.csv','VCFs/VCF_csv/ED15.csv','VCFs/VCF_csv/ED16.csv',
'VCFs/VCF_csv/ED17.csv','VCFs/VCF_csv/ED18.csv','VCFs/VCF_csv/ED19.csv','VCFs/VCF_csv/ED20.csv',
'VCFs/VCF_csv/ED21.csv','VCFs/VCF_csv/ED22.csv','VCFs/VCF_csv/ED23.csv','VCFs/VCF_csv/ED24.csv',
'VCFs/VCF_csv/ED25.csv','VCFs/VCF_csv/ED26.csv']

#reference dictionary
reference_dict = {'0|0':'Homozygous Reference', '0|1':'Heterozygous Alternate', 
				'0|2': 'Heterozygous Alternate 2', '1|1': 'Homozygous Alternate', 
				'1|2': 'Heterozygous Alternate 2'}




for i in list_of_csv:
	df=pd.read_csv(i, header=0, index_col=0)
	genotype_category = []

	for j in range(df.Genotype.shape[0]):
		s = reference_dict[df.Genotype[j]]
		genotype_category.append(s)

	df['Genotype Category'] = genotype_category
	print(df.head())
	df.to_csv(i)

'''
df = pd.read_csv('testing.csv', header=0,index_col=0)

genotype_category = []

for i in range(df.Genotype.shape[0]):
	s = reference_dict[df.Genotype[i]]
	t = df.POS[i]
	
	genotype_category.append(s)

df['Genotype Category'] = genotype_category

df.to_csv(r'VCFs/VCF_csv/ED1_VCF.csv')
'''