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
    return a , N

def nparr_to_string(matr):
    x = '\n'.join('.'.join(str(cell) for cell in row) for row in matr)
    return x

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
    parser = argparse.ArgumentParser(description='For running sudoku problems:')
    parser.add_argument('sudoku_instance', nargs='?', default='sudoku_1', help='The name of the sudoku instance. A corresponding .txt file must be in the sud_data/ folder.')
    parser.add_argument('algo', nargs='?', default='OR', help='One of OR, Pycosat, Pycosat2, Picat, ILP denoting the tool/Algorithm to be used.')

    args = parser.parse_args()
    mtrx_np , N = load_data(args.sudoku_instance)
    # starting time
    start = time.time()

    # call algorithm
    if args.algo.upper() in ['PYCOSAT']:
        import pyco_SAT
        out_arr = nparr_to_string(mtrx_np)
        model = pyco_SAT.Solver_pycosat(out_arr, N)
        cnf = model.solve_sudoku(out_arr, N)
        time_ms = model.pyco_solve(cnf, N)
        print(time_ms)
    elif args.algo.upper() in ['PYWRAP']:
        import sudoku_pywrapcp
        model = sudoku_pywrapcp.Solver_pywrapcp(mtrx_np, N)
        time_ms = model.solver_wrap(mtrx_np, N)
        print(time_ms)
    elif args.algo.upper() in ['CPSAT']:
        import cp_sat
        model = cp_sat.Solver_cpsat(mtrx_np, N)
        time_ms = model.solve_sudoku(mtrx_np, N)
        
        print(time_ms)
    elif args.algo.upper() in ['PYCO']:
        import pyco_SAT
        out_arr = nparr_to_string(np.zeros((49,49)).astype(int))
        model = pyco_SAT.Solver_pycosat(out_arr, 49)
        cnf = model.solve_sudoku(out_arr, 49)
        time_ms = model.pyco_solve(cnf, 49)
    else:
        print("Unknown Algorithm or tool. Exit")
        return
    # end time
    end = time.time()

if __name__== "__main__":
    main()