import io
import os
import numpy as np 
import pandas as pd 

#read vcf 
def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_csv(
        io.StringIO(''.join(lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str},
        sep='\t'
    ).rename(columns={'#CHROM': 'CHROM'})

#extract and create genotype column
def add_genotype_col(df):
	sample_col=df.iloc[:,9]
	genotype = []

	for i in sample_col:
		s = i.split(':')
		genotype.append(s[0].replace('/','|'))
	df['Genotype'] = genotype

	return df

def drop_cols(df):
	lst = ['ID', 'QUAL', 'ID','REF','ALT','FILTER', 'INFO', 'FORMAT', 'Genotype']
	return df.drop(lst,axis=1)

#create subset selecting for chromosome
def extract_chr(df,chrom):
	new_df = df[df['CHROM'] == chrom]
	new_df = drop_cols(new_df)
	new_df = new_df.drop(new_df.columns[2], axis=1)
	return new_df

def create_pos_set(lst):
	pos_nested_list = [i.POS for i in lst]
	pos_list = [j for i in pos_nested_list for j in i]
	pos_set = set(pos_list)

	return pos_set

def add_homo_ref(df, pos_set,chrm):
	#create list of current position
	curr_pos = [i for i in df.POS]

	#create list of positions the df does not have
	not_in_lst = [i for i in pos_set if i not in curr_pos]

	#create new dataframe with new positions
	to_append = [[chrm, i, 'Homozygous Reference'] for i in not_in_lst]
	col_names = df.columns
	temp = pd.DataFrame(to_append, columns = col_names)
	
	#append dataframes
	new_df = pd.concat([df, temp])
	return new_df

def convert_genotype(df):
	#reference dictionary
	reference_dict = {'0|0':'Homozygous Reference', '0|1':'Heterozygous Alternate', 
					'0|2': 'Heterozygous Alternate 2', '1|1': 'Homozygous Alternate', 
					'1|2': 'Heterozygous Alternate 2'}

	genotype_category = []
	for i in range(df.Genotype.shape[0]):
		s = reference_dict[df.Genotype[i]]
		genotype_category.append(s)

	df['Genotype Category'] = genotype_category

	return df

list_of_filenames = [
'/project/umw_elaine_lim/eqtl/vcfs/ED1.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED2.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED3.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED4.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED5.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED6.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED7.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED8.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED9.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED10.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED11.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED12.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED13.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED14.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED15.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED16.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED17.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED18.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED19.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED20.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED21.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED22.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED23.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED24.Filtered.Variants.vcf','/project/umw_elaine_lim/eqtl/vcfs/ED25.Filtered.Variants.vcf',
'/project/umw_elaine_lim/eqtl/vcfs/ED26.Filtered.Variants.vcf']


