#!usr/var/python

import pandas as pd 
import numpy as np 
import math 
from datetime import datetime 
import os 
from csv import writer

DATA_BASEPATH = 'benchmark_puzzles'
OUTPUT_BASEPATH = 'output'

#Loads the puzzles from the dataset
def load_path():
    colum = ['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10']
    df_add = pd.DataFrame(columns = colum)
    for k in range(3,10):
        for i in range(0, 105, 5):        
            for j in range(20):
                sta = 'puzzle' + str(j+1)            
                read_sudoku = pd.read_csv(os.path.join(DATA_BASEPATH,'benchmarks'+str(k)+'x'+str(k),str(i),sta +'.txt'))
                df = read_sudoku.iloc[1:, :]
                N = int(df.size)
                df_np = encode_sudoku_to_numpy(df, N)
                call_feature_computation_class(df_np, N, df_add, i)    
    return df_np, N 

def call_feature_computation_class(df_np , N, df_add, i):
    #todays_date = datetime.datetime.now().date()
    if N>0 :
        import compute_features
        model = compute_features.feature_computations(df_np, N)

        #x1 = model.add_numberOfNumbers()
        #x2 = model.add_MeanofPuzzle()
        #x3 = model.add_MedianOfPuzzle()
        #x4 = model.add_ModeOfPuzzle()
        #x5 = model.add_AverageOfPuzzle()
        #x6 = model.add_SumOfNumbers()
        #x7 = model.add_Percentile70()
        #x8 = model.add_Percentile80()
        #x9 = model.add_Percentile55()
        #x10 = model.add_Percentile45()
        x11 = model.add_manhattan_distance()
        #print(x11)
        #df_add = df_add.append({'col1': x1, 'col2': x2, 'col3': x3, 
                                            #'col4': x4, 'col5': x5, 'col6': x6,
                                            #'col7': x7, 'col8': x8, 'col9': x9, 'col10': x10}, 
                                            #ignore_index = True)
        #load_to_csv(df_add)

def load_to_csv(df_add):
    df_add.to_csv('features.csv', mode = 'a', header = False)

def encode_sudoku_to_numpy(df , N):
    a = df.to_numpy()
    s = [[]]
    for i in range(0, N):
        s = np.append(s, np.char.split(a[i][0],sep = "\t")) 
    k = np.zeros((N,N)).astype(np.int)
    for j in range(0, N):
        for i in range(0,N):
            x = int(s[j][i])
            if (x == -1):
                k[j][i] = 0
            else:
                k[j][i] = x
    return k

def main():
    #start here
    #load the path and iterate through all the instances to get the features
    df_np, N = load_path()



if __name__ == "__main__":
    main() 