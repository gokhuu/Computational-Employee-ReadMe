#python 3

def test():
	print('hello world')

def count_elements(lst):
	l = []
	for i in lst:
		for j in i:
			l.append(j)
	return l

def remove_low_count(dic):
	lst = []
	for i in dic:
		if dic[i] != 13:
			lst.append(i)

	for i in lst:
		dic.pop(i)

	return dic

def get_gene_list(dic):
	lst = []
	for i in dic:
		lst.append(i)

	return lst

def create_whole_df(lst_df, lst_gene):
	lst = []

	for i in lst_gene:
		temp = []
		for j in lst_df:
			temp.append(j[j['Gene Symbol'] == i])
		lst.append(temp)

	return lst