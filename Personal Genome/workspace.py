#python3
import numpy as np 
import pandas as pd 
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

x = [[9.3767168e-19]
 [2.5377483e-17]
 [8.2147295e-07]
 [4.6983253e-09]
 [5.1178428e-10]
 [9.7776828e-03]
 [3.6140591e-12]
 [9.9885249e-01]
 [1.4541023e-05]
 [3.2084659e-14]
 [1.2537835e-30]
 [1.5948765e-16]
 [2.7637839e-09]
 [1.7560311e-01]
 [8.3274297e-02]
 [1.6109642e-01]
 [5.6584686e-01]
 [9.9998271e-01]]

print(x)

