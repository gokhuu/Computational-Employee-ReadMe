#python3
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

from tensorflow import keras
from keras.models import Sequential
from keras import layers
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

def base_model():
	model = Sequential([
		layers.Dense(units=10, activation='relu',input_shape=[8163]),
		layers.Dense(units=1, activation='sigmoid')
		])
	model.compile(
		loss='categorical_crossentropy',
		optimizer='adam',
		metrics=['accuracy']
		)

df = pd.read_csv('Organoid Files/all_autism_fpkm_iqr_1.5_outliers_multi_class.csv', header=0, index_col=0)
y = df.Autism
x = df.iloc[:,1:]

estimator = KerasClassifier(build_fn = base_model(), epochs=200, batch_size=5, verbose=0)
kfold = KFold(n_splits=5, shuffle=True)
results = cross_val_score(estimator, x, y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))