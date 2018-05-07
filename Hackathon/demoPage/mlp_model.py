
# coding: utf-8

# In[13]:

import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from sklearn.metrics import mean_squared_error



# In[15]:
def normalize(test):
	test_x = test.iloc[:,0:-1].values #returns a numpy array
	test_y = test.iloc[:,-1].values.reshape(-1,1)

	min_max_scaler = preprocessing.MinMaxScaler()
	x_scaled = min_max_scaler.fit_transform(test_x)
	test_df = pd.DataFrame(x_scaled)

	min_max_scaler = preprocessing.MinMaxScaler()
	x_scaled = min_max_scaler.fit_transform(test_y)
	test_y = pd.DataFrame(x_scaled)


	y_test = test_y.as_matrix()
	x_test = test_df.iloc[:,:-1].as_matrix()
	return (x_test, y_test)

def mlp_model(x_test):

	model = Sequential()
	model.add(Dense(units=4, input_dim=7))
	model.add(Activation('relu'))
	model.add(Dropout(0.2))
	model.add(Dense(units=4, input_dim=4))
	model.add(Activation('relu'))
	model.add(Dropout(0.2))
	model.add(Dense(units=2, input_dim=4))
	model.add(Activation('relu'))
	model.add(Dense(units=1, input_dim=2))
	model.load_weights('my_doctor_weights.h5')
	predict_y = model.predict(x_test)
	print(mean_squared_error(y_test, predict_y))
	return predict_y


# In[21]:

def denormalize(df, normalized_value): 
    df = df.values.reshape(-1,1)
    normalized_value = normalized_value.reshape(-1,1)
    
    #return df.shape, p.shape
    min_max_scaler = preprocessing.MinMaxScaler()
    a = min_max_scaler.fit_transform(df)
    new = min_max_scaler.inverse_transform(normalized_value)
    return new


# In[ ]:
def DL_model(filename):
	test = pd.read_csv(filename)
	x_test, y_test = normalize(test)
	predict_y = mlp_model(x_test)
	predict = denormalize(test.iloc[:,-1], predict_y)
	return predict



# DL_model('./train_data/test_data.csv')
# In[ ]:



