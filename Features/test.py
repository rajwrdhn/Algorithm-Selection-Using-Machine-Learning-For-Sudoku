#!usr/var/python3
import pandas as pd 
import numpy as np 
import math 
from datetime import datetime 
import os 
from csv import writer

DATA_BASEPATH = '/home/raj/Music/SudokuSolvers/Features/benchmark_puzzles'
OUTPUT_BASEPATH = 'output'

#Loads the puzzles from the dataset
def load_path():
    for k in range(3,4):
        for i in range(5, 10, 5):        
            for j in range(1,2):
                sta = 'puzzle' + str(j)            
                read_sudoku = pd.read_csv(os.path.join(DATA_BASEPATH,'benchmarks'+str(k)+'x'+str(k),str(i),sta +'.txt'), 'r')
                df = read_sudoku.iloc[1:, :]
                N = int(df.size)
                df_np = encode_sudoku_to_numpy(df, N)
                #print(df_np)
                call_feature_computation_class(df_np, N, j,k, i)   
    return df_np, N 

def call_feature_computation_class(df_np , N,  j,k, i):
    #colum = ['col1','col2','col3','col4','col5','col6','col7','col8', 'col9', 'col10', ]
    df_add = pd.DataFrame()
    if N>0 :
        import compute_features
        model = compute_features.feature_computations(df_np, N, "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(k,k,i,j))        
        name_puzzle = "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(k,k,i,j)
        size_puzzle = model.sizeofpuzzle()

        s = model.calculateedgesnumber()
        print(s)
        
        #df_add = df_add.append({ 'name_puzzle' :name_puzzle, 'size_puzzle':size_puzzle},ignore_index = True)
        #print(df_add)
        #load_to_csv(df_add)

def load_to_csv(df_add):
    df_add.to_csv('features_sudoku_work_new1.csv', mode = 'a', header = False)

def encode_sudoku_to_numpy(df , N):
    a = df.to_numpy()
    s = [[]]
    for i in range(0, N):
        s = np.append(s, np.char.split(a[i][0],sep = "\t")) 
    k = np.zeros((N,N)).astype(int)
    for  j in range(0, N):
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
    #print(N, df_np)

def columnnames():
    colum = []
    for i in range(40):
        colum.append('col'+i)
        
    return colum

if __name__ == "__main__":
    main() 