#!/usr/bin/python3

import numpy as np 
import pandas as pd 
import math

from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

standardscaler = StandardScaler()
normalizer = Normalizer()
minmaxscaler = MinMaxScaler()
robustscaler = RobustScaler()

def basic_stats(df):
	return df.describe()

def threshold_data(df,n):
	df["Mean"] = df.mean(axis=1)
	l = len(df.iloc[:,0])
	lst = []

	for i in range(l):
		if df.Mean[i] < n:
			lst.append(i)

	return lst

def apply_scalers(df):
	df_standard_scaler = pd.DataFrame(standardscaler.fit_transform(df), columns=df.columns)
	df_normalizer = pd.DataFrame(normalizer.fit_transform(df), columns=df.columns)
	df_minmax_scaler = pd.DataFrame(minmaxscaler.fit_transform(df), columns=df.columns)
	df_robust_scaler = pd.DataFrame(robustscaler.fit_transform(df), columns=df.columns)

	return df_standard_scaler,df_normalizer,df_minmax_scaler,df_robust_scaler

def log_normalization(df):
	dim_x = len(df.columns)
	dim_y = len(df.iloc[:,0])

	for i in range(dim_x):
		for j in range(dim_y):
			df.iloc[j,i] = math.log2(1+df.iloc[j,i])

	return df

#Load Raw data
raw_read_count_data = pd.read_csv('count_expression.csv')
raw_fpkm_data = pd.read_csv('fpkm_expression.csv')

#Remove random column
raw_read_count_data = raw_read_count_data.drop(columns="Unnamed: 0")
raw_fpkm_data = raw_fpkm_data.drop(columns="Unnamed: 0")

#Apply Threshold Function
read_count_threshold_list = threshold_data(raw_read_count_data,10)
read_count_data = raw_read_count_data.drop(read_count_threshold_list)
read_count_data = read_count_data.drop('Mean', axis=1)

#Apply Threshold Function
fpkm_threshold_list = threshold_data(raw_fpkm_data,2)
fpkm_data = raw_fpkm_data.drop(fpkm_threshold_list)
fpkm_data = fpkm_data.drop('Mean', axis=1)

#Apply SK Learn preprocessing
read_count_data_standard, read_count_data_normalizer, read_count_data_minmax_scaler, read_count_data_robust_scaler = apply_scalers(read_count_data)
fpkm_data_standard, fpkm_data_normalizer, fpkm_data_minmax_scaler, fpkm_data_robust_scaler = apply_scalers(fpkm_data)

#apply log2+1 normalization
#fpkm_log = log_normalization(fpkm_data)
#read_count_data_log = log_normalization(read_count_data)




#Global Stats
#----------------------------------------------------------
#Raw stats
raw_read_count_data_description = basic_stats(raw_read_count_data)
raw_fpkm_data_description = basic_stats(raw_fpkm_data)

#Threshold applied stats
#n = 10
#read_count_data_description = basic_stats(read_count_data)
#read_count_below_threshold = len(read_count_threshold_list) #21605

#n = 2
fpkm_data_description = basic_stats(fpkm_data)
fpkm_below_threshold = len(fpkm_threshold_list) #26153

#Sk learn Preprocessing stats

read_count_data_standard_description = basic_stats(read_count_data_standard)
read_count_data_normalizer_description = basic_stats(read_count_data_normalizer)
read_count_data_minmax_scaler_description = basic_stats(read_count_data_minmax_scaler)
read_count_data_robust_scaler_description = basic_stats(read_count_data_robust_scaler)

fpkm_data_standard_description = basic_stats(fpkm_data_standard)
fpkm_data_normalizer_description = basic_stats(fpkm_data_normalizer)
fpkm_data_minmax_scaler_description = basic_stats(fpkm_data_minmax_scaler)
fpkm_data_robust_scaler_description = basic_stats(fpkm_data_robust_scaler)