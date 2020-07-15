#!usr/var/python
import os
import datetime
import argparse
import numpy as np
import pandas as pd 
import csv 


DATA_BASEPATH = 'benchmark_puzzles/benchmarks5x5'
OUTPUT_BASEPATH = 'output'
#A batch program to get features from all sudoku instances

def save_feature_into_dataset():
    import compute_features
    np_arr_dataset = compute_features.feature_computations(df, N, **kwargs)
    with open(r'f_dataset.csv', 'a') as f:
        fwriter = csv.writer(f)
        writer.writerow(fields)

#remove \t and -1 represent them by space and zero
def remove_tabs_neg(df):
    print(df.replace(-1, np.nan))
    df.replace('\t',' ')
    
    return df

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

def load_puzzles():
    for i in range(0, 20,5):        
        for j in range(20):
            sta = 'puzzle' + str(j+1)            
            read_sudoku = pd.read_csv(os.path.join(DATA_BASEPATH,str(i),sta +'.txt'))
            df_sudoku_puzzle = read_sudoku.iloc[1:, :]
            df_new = remove_tabs_neg(read_sudoku)
            #print(df_new)
            #save_feature_into_dataset(df_sudoku_puzzle)
    return 0 


load_puzzles()






