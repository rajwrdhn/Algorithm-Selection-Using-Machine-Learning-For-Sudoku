#!usr/var/python
import argparse
import os
import datetime
import time

import numpy as np 
import pandas as pd

DATA_BASEPATH = 'data'
OUTPUT_BASEPATH = 'output'

def load_data(sudoku_instance):
    path = os.path.join(DATA_BASEPATH, sudoku_instance + '.txt')
    read_sudoku = pd.read_csv(path)
    df = read_sudoku.iloc[1:, :]
    N = int(df.size)
    a = encode_sudoku_to_numpy(df, N)
    #print(a)
    return a , N

def nparr_to_string(matr):
    x = '\n'.join(','.join(str(cell) for cell in row) for row in matr)
    return x

def encode_sudoku_to_numpy(df , N):
    a = df.to_numpy()
    #print(a)
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
    #tolist gets the list format
    print(k.tolist())
    return k

def main():
    parser = argparse.ArgumentParser(description='For running sudoku problems:')
    parser.add_argument('sudoku_instance', nargs='?', default='', help='The name of the sudoku instance. A corresponding .txt file must be in the sud_data/ folder.')
    parser.add_argument('algo', nargs='?', default='GET', help='Get the Features.')

    args = parser.parse_args()
    mtrx_np , N = load_data(args.sudoku_instance)
    # starting time
    start = time.time()

    # call algorithm
    if args.algo.upper() in ['GET']:
        out_arr = nparr_to_string(mtrx_np)
        #print(out_arr)
 
    else:
        print("Unknown Algorithm or tool. Exit")
        return
    # end time
    end = time.time()

if __name__== "__main__":
    main()