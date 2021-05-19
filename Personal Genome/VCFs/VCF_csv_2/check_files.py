#python3
import io
import os
import pandas as pd

list_of_csv = [
'ED1.csv','ED2.csv','ED3.csv','ED4.csv',
'ED5.csv','ED6.csv','ED7.csv',
'ED9.csv','ED10.csv','ED11.csv','ED12.csv',
'ED13.csv','ED14.csv','ED15.csv','ED16.csv',
'ED17.csv','ED18.csv','ED19.csv','ED20.csv',
'ED21.csv','ED22.csv','ED23.csv','ED24.csv',
'ED25.csv','ED26.csv']

lst = [pd.read_csv(i, header=0,index_col=0) for i in list_of_csv]

print(lst[0].head())

'''
count = 0
for i in lst:
	temp = i.iloc[:,11]
	for j in temp:	
		if j == 'Heterozygous Alternate 1/2':
			count += 1

print(count)
'''