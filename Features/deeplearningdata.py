#Convert all data into 0 and 1 according to empty or non-empty cells
# Make 2 different datasets 
# 1 for each order different
# and 1 for all data and if cells do not exist add 0 inplace of that

import pandas as pd 
import numpy as np   
import scipy
import os    
from time import time

from csv import writer

DATA_BASEPATH = '/home/raj/Music/SudokuSolvers/Features/benchmark_puzzles'
OUTPUT_BASEPATH = 'output'
all_out : list = []

#Loads the puzzles from the dataset
def load_path():
    #colum = ['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10']
    #df_add = pd.DataFrame(columns = colum)
    for k in range(3,10):
        for i in range(0, 105, 5):        
            for j in range(1,21):
                sta = 'puzzle' + str(j)            
                read_sudoku = pd.read_csv(os.path.join(DATA_BASEPATH,'benchmarks'+str(k)+'x'+str(k),str(i),sta +'.txt'), 'r')
                df = read_sudoku.iloc[1:, :]
                N = int(df.size)
                df_np = encode_sudoku_to_numpy(df, N)
                #print(df_np)
                call_feature_computation_class(df_np, N, i, "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(k,k,i,j))   
    return df_np, N

def call_feature_computation_class(df_np , N,  i, name):
    #todays_date = datetime.datetime.now().date()
    if N>0 :
        import compute_features
        model = compute_features.feature_computations(df_np, N, name)
        list_dl= model.deeplearning1()
        all_out.append(list_dl)
        #df = pd.DataFrame(list_dl)
        #df[1:].to_csv('/home/raj/Music/SudokuSolvers/Features/deeplearning.csv',index=False)
        #print(df)

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
    df_np, N = load_path()
    col = ["name"]
    for i in range(0, N):
        for j in range(0,N):
            col.append("col(%d,%d)"%(i,j))
    
    df = pd.DataFrame(all_out,index=None,columns=col)
    df.to_csv('/home/raj/Music/SudokuSolvers/Features/deeplearning1.csv',index=False)
    print(df)

    #print(all_out)



if __name__ == "__main__":
    main() 