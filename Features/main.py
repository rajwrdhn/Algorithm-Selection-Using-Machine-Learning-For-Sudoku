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
    for k in range(4,10):
        for i in range(5, 100, 5):        
            for j in range(1,21):
                sta = 'puzzle' + str(j)            
                read_sudoku = pd.read_csv(os.path.join(DATA_BASEPATH,
                            'benchmarks'+str(k)+'x'+str(k),str(i),sta +'.txt'), 'r')
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
        model = compute_features.feature_computations(df_np, N, 
                "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(k,k,i,j))        
        name_puzzle = "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(k,k,i,j)
        size_puzzle = model.sizeofpuzzle()
        order_puzzle = model.orderofpuzzle()
        median_puzzle = model.medianofpuzzle()
        mode_puzzle = model.modeofpuzzle()
        mean_puzzle = model.meanofpuzzle()
        total_sum = model.sumofnumbers()        
        percent_puzzle = model.percentofnumbers()
        manhattan_puzzle = model.manhattandistance()
        smallest_row = model.sizeofsmallestrow()
        largest_row = model.sizeoflargestrow()
        smallest_column = model.sizeofsmallestcolumn()
        largest_column = model.sizeoflargestcolumn()
        smallest_subgrid = model.sizeofsmallestsubgrid()
        largest_subgrid = model.sizeoflargestsubgrid()
        minmax_subgrid = model.minmaxsubgrid()
        minmax_row = model.minmaxrow()
        minmax_column = model.minmaxcolumn()
        min_sd_subgrid = model.minsdsubgrid()
        min_sd_row = model.minsdrow()
        min_sd_column = model.minsdcolumn()
        subgrids_complete = model.numberofsubgridsfilledcompletely()
        subgrids_empty = model.numberofsubgridsempty()
        row_complete = model.numberofrowsfilledcompletely()
        row_empty = model.numberofrowsempty()
        column_complete = model.numberofcolumnsfilledcompletely()
        column_empty = model.numberofcolumnsempty()
        sum_puzzle, sd_puzzle = model.totalsumofnumbers()
        least_subgrid_sum = model.leastsubgridsum()
        highest_subgrid_sum = model.highestsubgridsum()
        least_highest_subgrid = model.leasthighestsubgrid()
        least_max_subgrid = model.leastmaxsubgrid() 
        highest_max_subgrid = model.highestmaxsubgrid()
        least_row_sum = model.leastrowsum()
        highest_row_sum = model.highestrowsum()
        least_highest_row = model.leasthighestrow()
        least_max_row = model.leastmaxrow()
        highest_max_row = model.highestmaxrow()
        highest_column_sum = model.highestcolumnsum()        
        least_column_sum = model.leastcolumnsum()        
        least_highest_column = model.leasthighestcolumn()
        least_max_column = model.leastmaxcolumn()
        highest_max_column = model.highestmaxcolumn()
        highest_occ_puzzle = model.highestoccurrenceofnumber()
        lowest_occ_puzzle = model.lowestoccurrenceofnumber()
        puzzle_diagonal = model.diagonalmatrix()
        max_clique = model.getmaxclique()
        least_condition_for_solution = model.leastnumberforonesolution()
        least_condition_bin = model.least_condition_binary()

        
        df_add = df_add.append({ 'name_puzzle' :name_puzzle, 
            'size_puzzle':size_puzzle,
            'order_puzzle':order_puzzle,
            'median_puzzle':median_puzzle,
            #'mode_puzzle':mode_puzzle,
            'mean_puzzle':mean_puzzle, 
            #'total_sum':total_sum,
            'percent_puzzle':percent_puzzle,
            'smallest_row':smallest_row,
            'largest_row':largest_row,
            'smallest_column':smallest_column,
            'largest_column':largest_column,
            'smallest_subgrid':smallest_subgrid,
            'largest_subgrid':largest_subgrid,
            'minmax_subgrid':minmax_subgrid,
            'minmax_row':minmax_row,
            'minmax_column':minmax_column,
            'min_sd_subgrid':min_sd_subgrid,
            'min_sd_row':min_sd_row,
            'min_sd_column':min_sd_column,
            'subgrids_complete':subgrids_complete,
            'subgrids_empty':subgrids_empty,
            'row_complete':row_complete,
            'row_empty':row_empty,
            'column_complete':column_complete,
            'column_empty':column_empty,
            'sum_puzzle':sum_puzzle, 'sd_puzzle':sd_puzzle,
            'least_subgrid_sum':least_subgrid_sum,
            'highest_subgrid_sum':highest_subgrid_sum,
            'least_highest_subgrid':least_highest_subgrid,
            'least_max_subgrid':least_max_subgrid,
            'highest_max_subgrid':highest_max_subgrid,
            'least_row_sum':least_row_sum,
            'highest_row_sum':highest_row_sum,
            'least_highest_row':least_highest_row,
            'least_max_row':least_max_row,
            'highest_max_row':highest_max_row,
            'highest_column_sum':highest_column_sum,     
            'least_column_sum':least_column_sum,       
            'least_highest_column':least_highest_column,
            'least_max_column':least_max_column,
            'highest_max_column':highest_max_column,
            'highest_occ_puzzle':highest_occ_puzzle,
            'lowest_occ_puzzle':lowest_occ_puzzle,
            'puzzle_diagonal':puzzle_diagonal,
            'max_clique': max_clique,
            'least_condition_for_solution': least_condition_for_solution,
            'least_condition_bin': least_condition_bin}, ignore_index = True)
        #print(df_add)
        load_to_csv(df_add)

def load_to_csv(df_add):
    df_add.to_csv('features_sudoku_work_new0.csv', mode = 'a', header = False)

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