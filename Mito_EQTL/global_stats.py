#!/usr/bin/python3

import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

def global_stats(df):
	return df.describe()

def threshold_data(df,n):
	df["Mean"] = df.mean(axis=1)
	l = len(df.iloc[:,0])
	lst = []

	for i in range(l):
		if df.Mean[i] < n:
			lst.append(i)

	return lst

#Load Raw data
raw_read_count_data = pd.read_csv('count_expression.csv')
raw_fpkm_data = pd.read_csv('fpkm_expression.csv')

#Remove random column
raw_read_count_data = raw_read_count_data.drop(columns="Unnamed: 0")
raw_fpkm_data = raw_fpkm_data.drop(columns="Unnamed: 0")

#Apply Threshold Function
read_count_threshold_list = threshold_data(raw_read_count_data,10)
read_count_data = raw_read_count_data.drop(read_count_threshold_list)
read_count_data = raw_read_count_data.drop('Mean', axis=1)

#Apply Threshold Function
fpkm_threshold_list = threshold_data(raw_fpkm_data,2)
fpkm_data = raw_fpkm_data.drop(fpkm_threshold_list)
fpkm_data = fpkm_data.drop('Mean', axis=1)

#Apply SK Learn preprocessing


#Global Stats
#----------------------------------------------------------
#Raw stats
raw_read_count_data_description = global_stats(raw_read_count_data)
raw_fpkm_data_description = global_stats(raw_fpkm_data)

#Threshold applied stats
#n = 10
read_count_data_description = global_stats(read_count_data)
#n = 2
fpkm_data_description = global_stats(fpkm_data)


