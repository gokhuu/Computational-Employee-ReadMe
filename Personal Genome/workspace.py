#python3
import numpy as np 
import pandas as pd 

#Autism fpkm files
df = pd.read_csv('Organoid Files/all_autism_fpkm_T.csv',header=0,index_col=0)

y = df.Autism
x = df.iloc[:,1:]

from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(x,y,random_state=1)

from tensorflow import keras
from tensorflow.keras import layers

clf = keras.Sequential([
	layers.Dense(units=20, activation='relu', input_shape=[11300]),
	layers.Dense(units=10, activation='relu'),
	layers.Dense(units=5, activation='relu'),
	layers.Dense(units=1)
	])

clf.compile(
	optimizer='adam',
	loss='mae',
	metrics=['accuracy']
	)

clf.fit(train_x,train_y,batch_size=50,epochs=100,verbose=0)
print(clf.evaluate(train_x,train_y))