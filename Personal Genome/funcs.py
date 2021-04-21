#python 3
import numpy as np 
import pandas as pd 

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

def compare_lists(brain, autism):
	lst = []

	for i in brain:
		for j in autism:
			if i == j:
				lst.append(i)
			else:
				continue
	return lst


def create_new_df(df,lst):
	l = []

	for i in lst:
		l.append(df[df['Short Gene Name'] == i])

	subset = pd.concat(l)

	return subset

def create_brain_df(df, genes):
	lst = []

	for i in genes:
		lst.append(df[df['Gene Symbol']]==i)

	subset = pd.concat(lst)

	return lst 

def concat_brain_df(brain,genes):
	lst = []

	for i in brain:
		lst.append(create_brain_df(i,genes))

	return lst