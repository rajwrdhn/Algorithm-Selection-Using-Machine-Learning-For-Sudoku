import pandas
 
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
from math import sqrt

from scipy.sparse import load_npz
import matplotlib.pyplot as plt

import argparse
import os
from datetime import datetime
import time

DATA_BASEPATH = 'data'
OUTPUT_BASEPATH = 'output'


def load_data(dataset_name):
    path = os.path.join(DATA_BASEPATH, dataset_name + '.npz')
    data = load_npz(path)
    
    X = data[:,:-1].todense()
    y = data[:,-1].todense()
   
    return X, y

def create_log_path(dataset_name, suffix):
    return os.path.join(OUTPUT_BASEPATH, dataset_name, datetime.now().strftime('%Y%m%d_%H%M%S_') + suffix)

def own_train_test_split(X, y):
    data_size = X.shape[0]
    train_size = int(data_size * 2 / 3)
    #train_size=int(data_size - 96)
    
    X_train = X[:train_size,:]
    y_train = y[:train_size]
    
    X_test = X[train_size:,:]
    y_test = y[train_size:]
    
    return X_train, X_test, y_train, y_test

def evaluate(model, X_test, y_test, log_basepath, show_plot = True, scale_factor = 1.0, scale_offset = 0.0):
    predicted = model.predict(X_test)
    
    if scale_factor != 1.0 or scale_offset != 0.0:
        predicted = predicted * scale_factor + scale_offset
    
    mse = metrics.mean_squared_error(y_test, predicted)
    mae = metrics.mean_absolute_error(y_test, predicted)
    r2 = metrics.r2_score(y_test, predicted)
    print('=== Result for', log_basepath, '===')
    print('MSE: ', mse)
    print('RMSE:', sqrt(mse))
    print('MAE: ', mae)
    print('R2:  ', r2)
    
    prediction_df = pandas.DataFrame(data={'truth': y_test.A1, 'predicted': predicted})
    prediction_df.to_csv(os.path.join(log_basepath, 'predictions.csv'))
    if show_plot:
        plt.figure()
        plot = prediction_df.plot()
        plt.show()
        
    with open(os.path.join(OUTPUT_BASEPATH, 'metrics.csv'), 'a+') as fo:
        for line in fo:
            if line.startswith(log_basepath):
                break
        
        fo.write(','.join([log_basepath, str(mse), str(sqrt(mse)), str(mae), str(r2)]) + '\n')
        
    return {'MSE': mse, 'RMSE': sqrt(mse), 'MAE': mae, 'R2': r2}
    
def check_nn_params(dataset_name):
    from keras_wrapper import KerasModel
    
    X, y = load_data(dataset_name)

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    for depth in [1, 2, 3, 4]:
        for width in [50, 100, 200, 300, 500]:
            for dropout in [0.0, 0.2, 0.4, 0.6]:
                log_basepath = create_log_path(dataset_name, '{}_{}_{}_NN'.format(depth, width, int(dropout * 100)))
                
                model = KerasModel(log_basepath, depth, width, dropout)
                model.train(X_train, y_train)
                evaluate(model, X_test, y_test, log_basepath, False)
    
def main():
    parser = argparse.ArgumentParser(description='Trains a regressor using either keras, or one of the existing linear models of scipy, prints evaluation metrics and plots the predictions.')
    parser.add_argument('dataset', nargs='?', default='traffic', help='The name of the dataset. A corresponding .npz file must be in the data/ folder.')
    parser.add_argument('regressor', nargs='?', default='LIN', help='One of LIN, NN, LOG, RF, SVR, or CONST, denoting the regressor to be used.')
    parser.add_argument('path', nargs='?', help='The basepath of an existing run, to evaluate the saved model instead of training a new one.')
    parser.add_argument('--noplot', action='store_true', help='If set, suppress plotting of predictions')
    parser.add_argument('--scale', '-s', action='store_true', help='If set, scales the target variable to [0; 1] before training and after evaluation')
    
    args = parser.parse_args()
    
    X, y = load_data(args.dataset)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
    if args.scale:
        lb = float(min(y))
        ub = float(max(y))
        y_train = (y_train - lb) / (ub - lb)
    
    if args.path:
        log_basepath = args.path
    else:
        log_basepath = create_log_path(args.dataset, args.regressor)
    
    if args.regressor.upper() == 'NN':
        import keras_wrapper
        model = keras_wrapper.KerasModel(log_basepath)
    elif args.regressor.upper() in ['LIN', 'LOG', 'CONST', 'RF', 'SVR']:
        import scipy_wrapper
        model = scipy_wrapper.ScipyModel(log_basepath, args.regressor)
    else:
        print('Unknown regressor type! Exiting...')
        return
    
    starttime = time.time()
    
    if args.path:
        model.load()
        print("Model loaded in {:.02f}s".format(time.time() - starttime))
    else:
        model.train(X_train, y_train)
        print("Model trained in {:.02f}s".format(time.time() - starttime))
    
    if args.scale:
        res = evaluate(model, X_test, y_test, log_basepath, not args.noplot, scale_factor=(ub - lb), scale_offset=lb)
    else:
        res = evaluate(model, X_test, y_test, log_basepath, not args.noplot)
    
    
    
    
    
if __name__ == '__main__':
    main()
    #check_nn_params('incidents_inc')
    #check_nn_params('incidents_qt')