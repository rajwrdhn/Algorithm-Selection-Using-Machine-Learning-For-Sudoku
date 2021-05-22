import pandas as pd 
import numpy as np   
import scipy
import os    
from time import time

from csv import writer
import matplotlib.pyplot as plt

def main():
    df1 = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/deeplearning3x3.csv")
    df2 = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/deeplearning4x4.csv")
    df3 = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/deeplearning5x5.csv")
    df4 = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/deeplearning6x6.csv")
    df5 = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/deeplearning7x7.csv")
    df6 = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/deeplearning8x8.csv")
    df7 = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/deeplearning9x9.csv")

    dfcplex = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/cplex")
    dfgurobi = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/gurobi")
    dfchuf = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/chuf")
    dfhy_ls = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/hy_ls")
    dfor = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/or")
    dfsa = pd.read_csv("/home/raj/Music/SudokuSolvers/datadeep/sa")

    df8 = pd.concat([df4,dfsa], ignore_index=True)
    df9 = pd.concat([df4,dfcplex], ignore_index=True)
    df10 = pd.concat([df4,dfgurobi], ignore_index=True)
    df11 = pd.concat([df4,dfchuf], ignore_index=True)
    df12 = pd.concat([df4,dfhy_ls], ignore_index=True)
    df13 = pd.concat([df4,dfor], ignore_index=True)
    #df14 = pd.concat([df4,dfcplex], ignore_index=True)

    #print(dfcplex.dtypes)
    #df = pd.concat([df8,df9,df10,df11,df12,df13], ignore_index=True)
    #df.to_csv('/home/raj/Music/SudokuSolvers/datadeep/df_all_sudoku.csv',index=False)
    #dfcplex.iloc[1].plot.bar()
    print(dfcplex.info(verbose=True))
    print(dfcplex)

main()
