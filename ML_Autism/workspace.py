#python3
import numpy as np 
import pandas as pd 
from collections import Counter
from funcs import count_elements, remove_low_count, get_gene_list, create_whole_df

#GTEx brain genes
amyg = pd.read_csv("Brain CSV Files/Amygdala.csv",header=0)
acc = pd.read_csv("Brain CSV Files/Anterior cingulate cortex.csv",header=0)
cau = pd.read_csv("Brain CSV Files/Caudate.csv",header=0)
ch = pd.read_csv("Brain CSV Files/Cerebellar Hemisphere.csv",header=0)
cere = pd.read_csv("Brain CSV Files/Cerebellum.csv",header=0)
cort = pd.read_csv("Brain CSV Files/Cortex.csv",header=0)
fc = pd.read_csv("Brain CSV Files/Frontal Cortex.csv",header=0)
hippo = pd.read_csv("Brain CSV Files/Hippocampus.csv",header=0)
hypo = pd.read_csv("Brain CSV Files/Hypothalamus.csv",header=0)
na = pd.read_csv("Brain CSV Files/Nucleus Accumbens.csv",header=0)
puta = pd.read_csv("Brain CSV Files/Putamen.csv",header=0)
sc = pd.read_csv("Brain CSV Files/Spinal Cord.csv",header=0)
an = pd.read_csv("Brain CSV Files/Substantia nigra.csv",header=0)

#Autism fpkm files
df15q = pd.read_csv('Organoid Files/15q_dup_fpkm.csv',header=0)
df16p11 = pd.read_csv('Organoid Files/16p11_fpkm.csv', header=0)

all_df = [amyg, acc, cau, ch, cere, cort, fc, hippo, hypo, na, puta, sc, an]

all_brain_genes = [amyg.iloc[:,1],acc.iloc[:,1],cau.iloc[:,1],ch.iloc[:,1],cere.iloc[:,1],cort.iloc[:,1],fc.iloc[:,1],
hippo.iloc[:,1],hypo.iloc[:,1],na.iloc[:,1],puta.iloc[:,1],sc.iloc[:,1],an.iloc[:,1]]

autism_genes = list(df15q.iloc[:,0])


for i in autism_genes:
	for j in amyg


'''
all_genes = count_elements(all_files)
common_genes = Counter(all_genes) 
cgene = remove_low_count(common_genes)
common_list = get_gene_list(cgene)

gene_lst = create_whole_df(all_df,common_list)
'''

