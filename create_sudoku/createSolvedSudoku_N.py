#!usr/var/python3
import numpy as np 
import pandas as pd 
import csv 
from datetime import datetime 
import os
import sys
import argparse
import math 

def createSudokuSolved(N):
    #sud = np.zeros((N,N))
    print(int(math.sqrt(N)))
    print("")
    print(1)
    for i in range(N):
        print("")
        for j in range(N):
            print(-1, end="\t")

def main():
    parser = argparse.ArgumentParser(description='For creating solved sudoku problems:')
    parser.add_argument('sudoku_size', nargs='?', default='9', help='The size of the sudoku')

    args = parser.parse_args()
    N = int(args.sudoku_size)

    createSudokuSolved(N)

if __name__ == "__main__":
    main()