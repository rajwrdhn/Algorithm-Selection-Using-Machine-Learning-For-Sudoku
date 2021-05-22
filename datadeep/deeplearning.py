import pandas as pd 
import sklearn.metrics as metrics
from math import sqrt
import matplotlib.pyplot as plt
import argparse
import os
from datetime import datetime

DATA_BASEPATH = 'data'
OUTPUT_BASEPATH = 'output'

def load_data(dataset_name):
    path = os.path.join(DATA_BASEPATH, dataset_name + '.csv')
    df = pd.read_csv(path)

    X = df.iloc[:, -1].values
    y = df.iloc[:, -1].values

    return X, y

def create_log_path(dataset_name, suffix):
    return os.path.join(OUTPUT_BASEPATH, dataset_name, datetime.now().strftime('%Y%m%d_%H%M%S_') + suffix)
    
def train_test_split(X, y):
    data_size = X.shape[0]
    train_size = int(data_size * 2 / 3)
 
    X_train = X[:train_size,:]
    y_train = y[:train_size]
    
    X_test = X[train_size:,:]
    y_test = y[train_size:]
    
    return X_train, X_test, y_train, y_test

def evaluate(model, X_test, y_test, log_basepath, show_plot = True):
    predicted = model.predict(X_test)
    
    mse = metrics.mean_squared_error(y_test, predicted)
    mae = metrics.mean_absolute_error(y_test, predicted)
    r2 = metrics.r2_score(y_test, predicted)
    print('=== Result for', log_basepath, '===')
    print('MSE: ', mse)
    print('RMSE:', sqrt(mse))
    print('MAE: ', mae)
    print('R2:  ', r2)
    print('Max Error')
    print('Explained Variance Score')
    print('Median Absolute Error')
    print('Mean Poisson Deviance')
    
    prediction_df = pd.DataFrame(data={'truth': y_test, 'predicted': predicted})
    prediction_df.to_csv(os.path.join(log_basepath, 'predictions.csv'))
    if show_plot:
        plt.figure()
        prediction_df.plot()        
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
    parser = argparse.ArgumentParser(description='Trains a regressor using keras, or one of the existing linear models of scipy, prints evaluation metrics and plots the predictions.')
    parser.add_argument('dataset', nargs='?', default='traffic', help='The name of the dataset. A corresponding .csv file must be in the data folder.')
    parser.add_argument('regressor', nargs='?', default='LIN', help='One of NN or CONST, denoting the regressor to be used.')
    parser.add_argument('path', nargs='?', help='The basepath of an existing run, to evaluate the saved model instead of training a new one.')
    parser.add_argument('--noplot', action='store_true', help='If set, suppress plotting of predictions')
    
    args = parser.parse_args()
    
    X, y = load_data(args.dataset)

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    
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
        
    if args.path:
        model.load()
    else:
        model.train(X_train, y_train)
    
    if args.noplot:
        evaluate(model, X_test, y_test, log_basepath, False)
    else:
        evaluate(model, X_test, y_test, log_basepath)
    
      
if __name__ == '__main__':
    main()
    
