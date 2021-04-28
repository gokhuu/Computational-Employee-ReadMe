#python3
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
'''
#Autism fpkm files
df = pd.read_csv('Organoid Files/all_autism_fpkm_T.csv',header=0,index_col=0)

y = df.Autism
x = df.iloc[:,1:]

from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(x,y,random_state=1)

from tensorflow import keras
from tensorflow.keras import layers

clf = keras.Sequential([
	layers.Dense(units=11300, activation='relu', input_shape=[11300]),
	layers.Dense(units=1, activation='sigmoid')
	])

clf.compile(
	optimizer='adam',
	loss='binary_crossentropy',
	metrics=['accuracy']
	)

clf.fit(train_x,train_y,batch_size=50,epochs=1000,verbose=0)
print(clf.evaluate(train_x,train_y))
'''

df = pd.read_csv('Organoid Files/all_autism_fpkm_iqr_1.5_outliers.csv', header=0, index_col=0)

sns.pairplot(df,hue='Autism')
