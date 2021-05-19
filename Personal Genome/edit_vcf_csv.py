#python3
'''
Author: Brandon Khuu
Last updated: 5/4/2021

En masse, add a column for genotype and genotypic category
'''
#Import libraries
import numpy as np 
import pandas as pd 

#list of csv string names
list_of_csv = [
'VCFs/VCF_csv_2/ED1.csv','VCFs/VCF_csv_2/ED2.csv','VCFs/VCF_csv_2/ED3.csv','VCFs/VCF_csv_2/ED4.csv',
'VCFs/VCF_csv_2/ED5.csv','VCFs/VCF_csv_2/ED6.csv','VCFs/VCF_csv_2/ED7.csv',
'VCFs/VCF_csv_2/ED9.csv','VCFs/VCF_csv_2/ED10.csv','VCFs/VCF_csv_2/ED11.csv','VCFs/VCF_csv_2/ED12.csv',
'VCFs/VCF_csv_2/ED13.csv','VCFs/VCF_csv_2/ED14.csv','VCFs/VCF_csv_2/ED15.csv','VCFs/VCF_csv_2/ED16.csv',
'VCFs/VCF_csv_2/ED17.csv','VCFs/VCF_csv_2/ED18.csv','VCFs/VCF_csv_2/ED19.csv','VCFs/VCF_csv_2/ED20.csv',
'VCFs/VCF_csv_2/ED21.csv','VCFs/VCF_csv_2/ED22.csv','VCFs/VCF_csv_2/ED23.csv','VCFs/VCF_csv_2/ED24.csv',
'VCFs/VCF_csv_2/ED25.csv','VCFs/VCF_csv_2/ED26.csv']

#reference dictionary
reference_dict = {'0|0':'Homozygous Reference', '0|1':'Heterozygous Alternate', 
				'0|2': 'Heterozygous Alternate 2', '1|1': 'Homozygous Alternate', 
				'1|2': 'Heterozygous Alternate 1/2'}

new_col = [
'14765x2','14763x7','14799x1','14858x3','14746x8','14824x13',
'14739x13','14710x6','14781x16','1601','1401',
'902','901','1001','BXS0110','BXS0111','BYS0112',
'BXS0114','BXS0115','BXS0116','BXS0117','GM23716','GM23720',
'GM25256','PGP1']

#iterate through list of CSV files
for i in range(len(list_of_csv)):
	#open csv file as dataframe
    df=pd.read_csv(list_of_csv[i], header=0, index_col=0)
	
    #create empty list
    genotype_category = []

	#iterate through elements in genotype list to create genotypic category
    for j in range(df.Genotype.shape[0]):
    	s = reference_dict[df.Genotype[j]]
    	genotype_category.append(s)

	#create genotype category column
    df[new_col[i]] = genotype_category

    #write to csv file
    df.to_csv(list_of_csv[i])
