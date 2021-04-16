#python3
import numpy as np 
import pandas as pd 
from collections import Counter
from funcs import count_elements, remove_low_count, get_gene_list, compare_lists, create_new_df

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


all_genes = count_elements(all_brain_genes)
common_genes = Counter(all_genes) 

brain_genes = ['MTATP6P1', 'FTL', 'TMSB10', 'FTH1', 'GFAP', 'MTND2P28', 'APOE', 'PTGDS', 'MT3', 
'ACTB', 'GAPDH', 'RPS18', 'CLU', 'MBP', 'RPS11', 'PLP1', 'RPS12', 'CALM2', 'TMSB4X', 'RPL13A', 
'PEA15', 'CKB', 'PEBP1', 'SPARCL1', 'CPE', 'COX6A1', 'RPLP1', 'NRGN', 'MTURN', 'KIF5A', 'NDRG2', 
'CST3', 'RPS25', 'RPL9', 'FAM107A', 'ACTG1', 'ITM2C', 'RPL19', 'EEF1A1', 'CALM1', 'RPL3', 'RPS27', 
'RPL35', 'CALM3', 'EEF2', 'SNAP25', 'ENO1', 'RPS27A', 'CAMK2N1', 'YWHAE', 'RPL10', 'RPS6', 'EEF1G', 
'RPL8', 'RPS16', 'RPL24', 'BCYRN1', 'ALDOC', 'PLEKHB1', 'NDUFS5', 'RPL38', 'FBXL16', 'RPL21', 'OAZ1', 
'PSAP', 'S100B', 'SELENOW', 'RPL34', 'HSP90AB1', 'PAQR6', 'SCD', 'UCHL1', 'HSP90AA1', 'RPLP2', 'CTXN1', 
'LDHB', 'RPL5', 'RPL4', 'RPSA', 'TUBA1A', 'PFDN5', 'RPL17', 'RPS13', 'ATP1A2', 'COX8A', 'APOD', 'RPS3A', 
'CA11', 'BEX3', 'RPS15', 'RPS7', 'BEX1', 'NSMF', 'FAM127A', 'RPL27', 'TMA7', 'YWHAH', 'RPL7A', 'RPS2', 'SLC1A2', 
'TUBA1B', 'EEF1A2', 'GLUL', 'ALDOA', 'SNCB', 'CAMK2A', 'AES', 'EIF4A2', 'SLC17A7', 'IDS', 'TSPAN7', 'PCSK1N', 'FKBP8', 
'NCS1', 'GAP43', 'ATP6V0C', 'PRDX5', 'PRDX2', 'GNAS', 'TMEM59L', 'BSG', 'NDUFA1', 'PPP1R1B', 'HPCA', 'PCP4', 'NCDN', 'GNG7', 
'SYNDIG1L', 'PKM', 'SPARC', 'HTRA1', 'DKK3', 'ENO2', 'LINC00599', 'ATP6V1G2', 'TUBB4A', 'STMN2', 'CBLN3', 'CBLN1', 'CHGB', 'PTMS', 
'ATP5B', 'SNRNP70', 'PHYHIP', 'HSPA8', 'HNRNPA2B1', 'RTN1', 'CPLX2', 'ZBTB18', 'TMEM178A', 'GDI1', 'CADM3', 'PRRT2', 'ATP1A1', 'TSPYL2',
'NDRG4', 'GABRD', 'H3F3B', 'APLP2', 'PRNP', 'NPDC1', 'ACAP3', 'VSNL1', 'VAMP2', 'SLC22A17', 'PDIA2', 'PVALB', 'PKD1', 'ATP1B2', 'DDX17',
'4-Sep', 'LENG8', 'ATN1', 'TLE2', 'PAGR1', 'RAB3A', 'TPI1', 'CEND1', 'RUNDC3A', 'CHN1', 'ATP1B1', 'APP', 'BASP1', 'YWHAG', 'NEFM', 'NEFL', 
'RTN3', 'CCK', 'SYP', 'TAGLN3', 'CRYAB', 'APLP1', 'MARCKSL1', 'TP53INP2', 'AVP', 'SNCG', 'SCG2', 'SARAF', 'MRFAP1', 'UBB', 'CHCHD2', 
'SERINC1', 'NNAT', 'CSRP1', 'TF', 'SPP1', 'MOBP', 'CLDND1', 'MAG', 'BCAS1', 'LGALS1', 'CNP', 'DBNDD2', 'FEZ1', 'HAPLN2', 'B2M', 'CD74', 
'MOG', 'GPM6B', 'DHCR24', 'RHOB', 'ERMN', 'PTMA', 'PMP2', 'HLA-B', 'ABCA2', 'PRDX1', 'PPDPF', 'HBB', 'EIF1', 'MT2A', 'QDPR', 'RPS28']

expressed_autism_genes = compare_lists(brain_genes,autism_genes)

subset_15q = create_new_df(df15q, expressed_autism_genes)
subset_16p11 = create_new_df(df16p11, expressed_autism_genes)

lst = []
for i in all_df:
	temp = []
	for j in expressed_autism_genes:
		temp.append(i[i["Gene Symbol"] == j])
		temp_df = pd.concat(temp)

	lst.append(temp_df)

