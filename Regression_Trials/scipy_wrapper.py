import pandas

import sklearn.linear_model as lin_models
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR, LinearSVR
import sklearn.dummy
import pickle

import matplotlib.pyplot as plt
import shutil
import os

class ScipyModel():
    def __init__(self, log_basepath, regressor_suffix, **kwargs):
        self.log_basepath = log_basepath
        self.suffix = regressor_suffix.upper()
        
        if self.suffix == 'LIN':
            self.model = lin_models.LinearRegression(**kwargs)
        elif self.suffix == 'LOG':
            self.model = lin_models.LogisticRegression(**kwargs)
        elif self.suffix == 'CONST':
            self.model = dummy.DummyRegressor(**kwargs)
        elif self.suffix == 'RF':
            self.model = RandomForestRegressor(n_estimators = 100, random_state = 42, max_depth = 30, **kwargs)
        elif self.suffix == 'SVR':
            self.model = SVR(epsilon=0.1, tol=0.0001, **kwargs)
        else:
            self.model = None
        
    def get_path(self, filename):
        return os.path.join(self.log_basepath, filename)
        
    def get_suffix(self):
        return self.suffix
        
    def train(self, X_train, y_train): 
        self.model.fit(X_train, y_train.A1)
        
        os.makedirs(self.log_basepath)
        with open(self.get_path('model.pk1'), 'wb') as fo:
            pickle.dump(self.model, fo)
        
        shutil.copyfile(__file__, self.get_path('wrapper.py'))

    def load(self):
        with open(self.get_path('model.pk1'), 'rb') as fo:
            self.model = pickle.load(fo)
        
    def predict(self, X):
        return self.model.predict(X)
    