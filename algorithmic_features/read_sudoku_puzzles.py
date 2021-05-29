#!usr/var/python3
import pandas as pd 
import numpy as np 
import math 
from datetime import datetime 
import os 
from csv import writer

DATA_BASEPATH = '/home/raj/Music/SudokuSolvers/algorithmic_features/data/benchmark_puzzles'
OUTPUT_BASEPATH = 'output'

#Loads the puzzles from the dataset
def load_path():
    for k in range(3,9):
        for i in range(20, 25, 5):        
            for j in range(1,2):
                sta = 'puzzle' + str(j)            
                read_sudoku = pd.read_csv(os.path.join(DATA_BASEPATH,'benchmarks'+str(k)+'x'+str(k),str(i),sta +'.txt'), 'r')
                df = read_sudoku.iloc[1:, :]
                N = int(df.size)
                df_np = encode_sudoku_to_numpy(df, N)
                #print(df_np)
                call_feature_computation_class(df_np, N, j,k, i)   
    return df_np.tolist(), N 

def call_feature_computation_class(df_np , N,  j,k, i):
    #todays_date = datetime.datetime.now().date()
    colum = ['col1','col2','col3','col4','col5','col6','col7','col8', 'col9', 'col10']
    df_add = pd.DataFrame(columns = colum)
    if N>0 :
        import dpll_probe
        #print(df_np)
        model = dpll_probe.Dpll(df_np, N, "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(k,k,i,j))        
        print(model.numberofclauses(N))
        #x0 = "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(k,k,i,j)
        #x1 = model.add_MeanofPuzzle()
        #x2 = model.add_MedianOfPuzzle()
        #x3 = model.add_ModeOfPuzzle()
        #x4 = model.sizeofpuzzle()
        #x5 = model.add_SumOfNumbers()        
        #x6 = model.add_percentOfNumbers()
        #x7 = model.add_manhattan_distance()
        #x8 = model.orderofpuzzle()
        #x9 = model.add_NumberOfEmptyRows()
        #x10 = model.add_NumberOfEmptyColumns()       
        #print(x17)
        #model.deeplearning2()
        #model.calculate_gcp_features()
        #print(x1)
        #df_add = df_add.append({'col0': x0, 'col1': x1, 'col2': x2, #'col3': x3, 
        #                                   'col4': x4, 'col5': x5, 'col6': x6,
        #                                   'col7': x7, 'col8': x8, 'col9': x9 , 'col10': x10} , 
        #                                   ignore_index = True)
        #print(df_add)
        #load_to_csv(df_add)

def load_to_csv(df_add):
    df_add.to_csv('features.csv', mode = 'a', header = False)

def encode_sudoku_to_numpy(df , N):
    a = df.to_numpy()
    s = [[]]
    for i in range(0, N):
        s = np.append(s, np.char.split(a[i][0],sep = "\t")) 
    k = np.zeros((N,N)).astype(int)
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
    #print(N, df_np)

if __name__ == "__main__":
    main() 