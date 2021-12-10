#!usr/var/python3
import pandas as pd 
import numpy as np 
import math 
from datetime import datetime 
import os 
from csv import writer
import time

DATA_BASEPATH = '/home/raj/Music/SudokuSolvers/Features/benchmark_puzzles'
OUTPUT_BASEPATH = 'output'

# 11 to 12 mins computaion time
#Loads the puzzles from the dataset
def load_path():
    for k in range(4,10,1):
        for i in range(5, 100, 5):        
            for j in range(1,21,1):
                sta = 'puzzle' + str(j)            
                read_sudoku = pd.read_csv(os.path.join(DATA_BASEPATH,
                            'benchmarks'+str(k)+'x'+str(k),str(i),sta +'.txt'), 'r')
                df = read_sudoku.iloc[1:, :]
                N = int(df.size)
                df_np = encode_sudoku_to_numpy(df, N)
                call_feature_computation_class(df_np, N, j,k, i)   
    return df_np, N 

def call_feature_computation_class(df_np , N,  j,k, i):
    df_add = pd.DataFrame()    
    if N>0 :
        import compute_features
        model = compute_features.feature_computations(df_np, N, 
                "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(k,k,i,j))        
        name_puzzle = "benchmark_puzzles/benchmarks%dx%d/%d/puzzle%d.txt" %(k,k,i,j)
        size_puzzle = model.sizeofpuzzle() #size
        order_puzzle = model.orderofpuzzle() #order
        mean_puzzle = model.meanofpuzzle()  #mean    
        percent_puzzle = model.percentofnumbers() #percent
        smallest_row = model.sizeofsmallestrow() #size
        largest_row = model.sizeoflargestrow()
        smallest_column = model.sizeofsmallestcolumn()
        largest_column = model.sizeoflargestcolumn()
        smallest_subgrid = model.sizeofsmallestsubgrid()
        largest_subgrid = model.sizeoflargestsubgrid()
        rangeminmax_subgrid = model.rangeminmaxsubgrid()
        rangemintotalsubgrid = model.rangemintotalsubgrid()
        sdsizesubgrid = model.sdsizesubgrid()
        minratio_subgrid = model.minratiosubgrid()
        minmax_subgrid = model.minmaxsubgrid()
        minmax_row = model.minmaxrow()
        minratio_row = model.minratiorow()
        maxratio_row = model.maxratiorow()
        sdsize_row = model.sdsizerow()
        minratio_column = model.minratiocolumn()
        #sdsize_column = model.minsizecolumn()
        minmax_column = model.minmaxcolumn()
        #min_sd_subgrid = model.minsdsubgrid()
        #min_sd_row = model.minsdrow()
        #min_sd_column = model.minsdcolumn()
        subgrids_complete = model.numberofsubgridsfilledcompletely()
        subgrids_empty = model.numberofsubgridsempty()
        row_complete = model.numberofrowsfilledcompletely()
        row_empty = model.numberofrowsempty()
        column_complete = model.numberofcolumnsfilledcompletely()
        column_empty = model.numberofcolumnsempty()
        sum_range_puzzle, sum_ratio_puzzle = model.totalsumofnumbersrr()
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
        size_diagonal, puzzle_diagonal = model.diagonalmatrix()
        max_clique = model.getmaxclique()
        #min_clique = model.getminclique()
        #range_min_clique = model.getrangeminclique()
        range_max_clique = model.getrangemaxclique()
        #range_minmax_clique = model.getrangeminmaxclique()
        #ratio_minmax_clique = model.getratiominmaxclique()
        least_condition_for_solution = model.leastnumberforonesolution()
        least_condition_bin = model.leastconditionbinary()
        #r, ra = totalsumofnumbersrr()
        #multi_max_row = model.multiplymaxrow()
        #multi_max_column = model.multiplymaxcolumn()
        #multi_max_subgrid = model.multiplymaxsubgrid()
        #multi_min_row = model.multiplyminrow()
        #multi_min_column = model.multiplymincolumn()
        #multi_min_subgrid = model.multiplyminsubgrid()
        #range_mul_minmax_row = model.rangemultiplyminmaxrow()
        #range_mul_minmax_column = model.rangemultiplyminmaxcolumn()
        #range_mul_minmax_subgrid = model.rangemultiplyminmaxsubgrid()
        multiply_size = model.multiplyof()
        #mul_sd_row = model.sdrowmultiply()
        #mul_sd_column = model.sdcolumnmultiply()
        #mul_sd_subgrid = model.sdsubgridmultiply()
        mean_mul = model.meanofmul()
        mean_add = model.meanofadd()
        sd_row_add = model.sdrowaddition()
        sd_column_add = model.sdcolumnaddition()
        sd_subgrid_add = model.sdsubgridaddition()
        max_occurence, occ_max = model.maxofnumber()
        min_occurence, occ_min = model.minofnumber()
        total_edges = model.totaledges()
        max_degree = model.maxdegree()
        num_nodes = model.numnodes()
        missing_nodes = model.missingnodes()
        max_num_edges = model.maxnumedges()
        maxmissing_num_edges = model.maxmissingnumedges()
        set_cover = model.setcover()
        num_domain = model.numdomain()
        missing_domain = model.missingdomain()
        iqr_puzzle = model.interquartilerangeforsudoku()


        df_add = df_add.append({ 'name_puzzle' :name_puzzle, 
            'size_puzzle':size_puzzle,
            'order_puzzle':order_puzzle,
            'mean_puzzle':mean_puzzle, 
            'percent_puzzle':percent_puzzle,
            'smallest_row':smallest_row,
            'largest_row':largest_row,
            'smallest_column':smallest_column,
            'largest_column':largest_column,
            'smallest_subgrid':smallest_subgrid,
            'largest_subgrid':largest_subgrid,
            'minratio_subgrid':minratio_subgrid,
            'minmax_subgrid':minmax_subgrid,
            'minmax_row':minmax_row,
            'minratio_row':minratio_row, 
            'maxratio_row':maxratio_row, 
            'sdsize_row':sdsize_row, 
            'minratio_column':minratio_column, 
            #'sdsize_column':sdsize_column, 
            'minmax_column':minmax_column,
            #'min_sd_subgrid':min_sd_subgrid,
            #'min_sd_row':min_sd_row,
            #'min_sd_column':min_sd_column,
            'subgrids_complete':subgrids_complete,
            'subgrids_empty':subgrids_empty,
            'row_complete':row_complete,
            'row_empty':row_empty,
            'column_complete':column_complete,
            'column_empty':column_empty,
            'sum_puzzle':sum_puzzle, 
            'sum_ratio_puzzle':sum_ratio_puzzle,
            'least_subgrid_sum':least_subgrid_sum,
            'highest_subgrid_sum':highest_subgrid_sum,
            'least_highest_subgrid':least_highest_subgrid,
            'least_max_subgrid':least_max_subgrid,
            'highest_max_subgrid':highest_max_subgrid,
            'rangeminmax_subgrid' : rangeminmax_subgrid,
            'rangemintotalsubgrid' : rangemintotalsubgrid,
            'sdsizesubgrid' : sdsizesubgrid,
            #'minratio_subgrid':minratio_subgrid,
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
            'size_diagonal':size_diagonal,
            'puzzle_diagonal':puzzle_diagonal,
            'max_clique': max_clique,
            'least_condition_for_solution': least_condition_for_solution,
            'least_condition_bin': least_condition_bin,
            'range_max_clique':range_max_clique,        
            #'multi_max_row':multi_max_row,
            #'multi_max_column':multi_max_column,
            #'multi_max_subgrid':multi_max_subgrid,
            #'multi_min_row': multi_min_row,
            #'multi_min_column': multi_min_column,
            #'multi_min_subgrid': multi_min_subgrid, 
            #'range_mul_minmax_row':range_mul_minmax_row, 
            #'range_mul_minmax_column':range_mul_minmax_column, 
            #'range_mul_minmax_subgrid':range_mul_minmax_subgrid,
            'multiply_size':multiply_size,
            #'mul_sd_row':mul_sd_row ,
            #'mul_sd_column':mul_sd_column,
            #'mul_sd_subgrid':mul_sd_subgrid, 
            'mean_mul':mean_mul,       
            'mean_add':mean_add,
            'sd_row_add':sd_row_add,
            'sd_column_add':sd_column_add,
            'sd_subgrid_add':sd_subgrid_add, 
            'max_occurence':max_occurence,
            'occ_max':occ_max,
            'min_occurence':min_occurence,
            'occ_min':occ_min,
            'total_edges':total_edges,
            'max_degree':max_degree,
            'num_nodes':num_nodes, 
            'missing_nodes':missing_nodes, 
            'max_num_edges':max_num_edges, 
            'maxmissing_num_edges':maxmissing_num_edges, 
            'set_cover':set_cover,
            'num_domain':num_domain,
            'missing_domain':missing_domain,
            'iqr_puzzle': iqr_puzzle}, ignore_index = True)
            
        #print(df_add)
        load_to_csv(df_add)

def load_to_csv(df_add):
    df_add.to_csv('featurescompleteheader4_9.csv', mode = 'a', header = True)
    #df_add.columns = columnnames()

    #print(df_add['iqr_puzzle'])

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
    colum = ['name_puzzle', 
            'size_puzzle',
            'order_puzzle',
            'mean_puzzle', 
            'percent_puzzle',
            'smallest_row',
            'largest_row',
            'smallest_column',
            'largest_column',
            'smallest_subgrid',
            'largest_subgrid',
            'minratio_subgrid',
            'minmax_subgrid',
            'minmax_row',
            'minratio_row', 
            'maxratio_row', 
            'sdsize_row', 
            'minratio_column', 
            #'sdsize_column', 
            'minmax_column',
            #'min_sd_subgrid',
            #'min_sd_row',
            #'min_sd_column',
            'subgrids_complete',
            'subgrids_empty',
            'row_complete',
            'row_empty',
            'column_complete',
            'column_empty',
            'sum_puzzle', 
            'sum_ratio_puzzle',
            'least_subgrid_sum',
            'highest_subgrid_sum',
            'least_highest_subgrid',
            'least_max_subgrid',
            'highest_max_subgrid',
            'rangeminmax_subgrid' ,
            'rangemintotalsubgrid',
            'sdsizesubgrid',
            'least_row_sum',
            'highest_row_sum',
            'least_highest_row',
            'least_max_row',
            'highest_max_row',
            'highest_column_sum',     
            'least_column_sum',       
            'least_highest_column',
            'least_max_column',
            'highest_max_column',
            'highest_occ_puzzle',
            'lowest_occ_puzzle',
            'size_diagonal',
            'puzzle_diagonal',
            'max_clique',
            'least_condition_for_solution',
            'least_condition_bin',
            'range_max_clique',        
            'multi_max_row',
            'multi_max_column',
            'multi_max_subgrid',
            'multi_min_row',
            'multi_min_column',
            'multi_min_subgrid', 
            'range_mul_minmax_row', 
            'range_mul_minmax_column', 
            'range_mul_minmax_subgrid',
            'multiply_size',
            'mul_sd_row',
            'mul_sd_column',
            'mul_sd_subgrid', 
            'mean_mul',       
            'mean_add',
            'sd_row_add',
            'sd_column_add',
            'sd_subgrid_add', 
            'max_occurence',
            'occ_max',
            'min_occurence',
            'occ_min',
            'total_edges',
            'max_degree',
            'num_nodes', 
            'missing_nodes', 
            'max_num_edges', 
            'maxmissing_num_edges', 
            'set_cover',
            'num_domain',
            'missing_domain',
            'iqr_puzzle']  
    return colum

if __name__ == "__main__":
    main() 
    #print(columnnames())
