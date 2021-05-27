#python3

csv_lst = ['VCFs/chrm_split/chr1.csv', 'VCFs/chrm_split/chr2.csv','VCFs/chrm_split/chr3.csv','VCFs/chrm_split/chr4.csv','VCFs/chrm_split/chr5.csv',
'VCFs/chrm_split/chr6.csv','VCFs/chrm_split/chr7.csv','VCFs/chrm_split/chr8.csv','VCFs/chrm_split/chr9.csv','VCFs/chrm_split/chr10.csv',
'VCFs/chrm_split/chr11.csv','VCFs/chrm_split/chr12.csv','VCFs/chrm_split/chr13.csv','VCFs/chrm_split/chr14.csv','VCFs/chrm_split/chr15.csv',
'VCFs/chrm_split/chr16.csv','VCFs/chrm_split/chr17.csv','VCFs/chrm_split/chr18.csv','VCFs/chrm_split/chr19.csv','VCFs/chrm_split/chr20.csv',
'VCFs/chrm_split/chr21.csv','VCFs/chrm_split/chr22.csv','VCFs/chrm_split/chrX.csv','VCFs/chrm_split/chrY.csv']

def storage_lst(file_lst):
	lst = []
	for i in file_lst:
		df = pd.read_csv(i, header=0, index_col=0)
		lst.append(df)
	return lst

df_list = storage_lst(csv_lst)