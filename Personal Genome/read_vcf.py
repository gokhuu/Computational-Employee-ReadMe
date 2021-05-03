#python3
import io
import os
import pandas as pd
'''
Script to convert VCF file into CSV
By: Brandon khuu 
last updated 5/3/2021
'''


#function to read vcf files
def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM'})

#function to extract and create genotype column
def add_genotype_col(df):

	genotype = []
	sample_col = df.iloc[:,9]

	for i in sample_col:
		s = i.split(':')
		genotype.append(s[0].replace('/','|'))

	df['Genotype'] = genotype


	return df

list_of_filenames = [
'VCFs/ED1.Filtered.Variants.vcf','VCFs/ED2.Filtered.Variants.vcf','VCFs/ED3.Filtered.Variants.vcf',
'VCFs/ED4.Filtered.Variants.vcf','VCFs/ED5.Filtered.Variants.vcf','VCFs/ED6.Filtered.Variants.vcf',
'VCFs/ED7.Filtered.Variants.vcf','VCFs/ED8.Filtered.Variants.vcf','VCFs/ED9.Filtered.Variants.vcf',
'VCFs/ED10.Filtered.Variants.vcf','VCFs/ED11.Filtered.Variants.vcf','VCFs/ED12.Filtered.Variants.vcf',
'VCFs/ED13.Filtered.Variants.vcf','VCFs/ED14.Filtered.Variants.vcf','VCFs/ED15.Filtered.Variants.vcf',
'VCFs/ED16.Filtered.Variants.vcf','VCFs/ED17.Filtered.Variants.vcf','VCFs/ED18.Filtered.Variants.vcf',
'VCFs/ED19.Filtered.Variants.vcf','VCFs/ED20.Filtered.Variants.vcf','VCFs/ED21.Filtered.Variants.vcf',
'VCFs/ED22.Filtered.Variants.vcf','VCFs/ED23.Filtered.Variants.vcf','VCFs/ED24.Filtered.Variants.vcf',
'VCFs/ED25.Filtered.Variants.vcf','VCFs/ED26.Filtered.Variants.vcf',
]


list_of_csv = [
'VCFs/VCF_csv/ED1.csv','VCFs/VCF_csv/ED2.csv','VCFs/VCF_csv/ED3.csv','VCFs/VCF_csv/ED4.csv',
'VCFs/VCF_csv/ED5.csv','VCFs/VCF_csv/ED6.csv','VCFs/VCF_csv/ED7.csv','VCFs/VCF_csv/ED8.csv',
'VCFs/VCF_csv/ED9.csv','VCFs/VCF_csv/ED10.csv','VCFs/VCF_csv/ED11.csv','VCFs/VCF_csv/ED12.csv',
'VCFs/VCF_csv/ED13.csv','VCFs/VCF_csv/ED14.csv','VCFs/VCF_csv/ED15.csv','VCFs/VCF_csv/ED16.csv',
'VCFs/VCF_csv/ED17.csv','VCFs/VCF_csv/ED18.csv','VCFs/VCF_csv/ED19.csv','VCFs/VCF_csv/ED20.csv',
'VCFs/VCF_csv/ED21.csv','VCFs/VCF_csv/ED22.csv','VCFs/VCF_csv/ED23.csv','VCFs/VCF_csv/ED24.csv',
'VCFs/VCF_csv/ED25.csv','VCFs/VCF_csv/ED26.csv',
]


#iterate through the list
for i in range(len(list_of_filenames)):
	#get filename
	filename = i
	
	#create dataframe, call read_vcf function
	df = read_vcf(list_of_filenames[i])
	
	#call function to add genotype column
	df = add_genotype_col(df)

	#output to csv
	df.to_csv(list_of_csv[i])
