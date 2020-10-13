import pandas

from tensorflow import keras
from keras.models import Sequential, load_model
from keras.layers import Activation, Dense, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint, CSVLogger

import tensorflow as tf          

import matplotlib.pyplot as plt
import shutil
import os

class KerasModel():
    def __init__(self, log_basepath, hidden_layers=1, layer_width = 300, dropout = 0.2):
        self.log_basepath = log_basepath
        self.model = None
        self.hidden_layers = hidden_layers
        self.layer_width = layer_width
        self.dropout = dropout
        
    def get_path(self, filename):
        return os.path.join(self.log_basepath, filename)
        
    def get_suffix(self):
        return 'NN'

    def create_model(self, input_dim):
        model = Sequential()
        model.add(Dense(self.layer_width, input_dim=input_dim, activation='relu', kernel_initializer='normal'))
        for i in range(self.hidden_layers):
            model.add(Dense(self.layer_width, activation='relu', kernel_initializer='normal'))
        model.add(Dropout(self.dropout))
        model.add(Dense(input_dim, activation='relu', kernel_initializer='normal'))
        model.add(Dense(1, kernel_initializer='normal'))
        model.compile(loss='mean_squared_error', optimizer='rmsprop')
        return model

    def create_callbacks(self):
        callbacks = []
        callbacks.append(EarlyStopping(patience=10))
        callbacks.append(ModelCheckpoint(self.get_path('model.hdf5'), save_best_only=True))
        return callbacks
        
    def train(self, X_train, y_train): 
        model = self.create_model(X_train.shape[1])
        
        os.makedirs(self.log_basepath)
        with open(self.get_path('architecture.json'), 'w') as fo:
            fo.write(model.to_json())
        
        callbacks = self.create_callbacks()
        
        res = model.fit(X_train, y_train, epochs=100, validation_split=0.3, callbacks=callbacks)
        
        history_df = pandas.DataFrame(res.history)
        plot = history_df.plot()
        plot.get_figure().savefig(self.get_path('loss.png'))
        
        history_df.to_csv(self.get_path('history.csv'))
        
        shutil.copyfile(__file__, self.get_path('wrapper.py'))

        self.model = model

    def load(self):
        self.model = load_model(self.get_path('model.hdf5'))
        
    def predict(self, X):
        assert self.model != None
        return self.model.predict(X)[:,0]
    