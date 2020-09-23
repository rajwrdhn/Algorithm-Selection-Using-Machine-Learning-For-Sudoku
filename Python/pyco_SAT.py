#!usr/var/python
import pycosat
import numpy as np
import itertools
import math 
from datetime import datetime
import pandas


class Solver_pycosat():
    def __init__(self, sudoku, size, **kwargs):
        self.sudoku = sudoku
        self.size = size 
        
    def solve_sudoku(self, matrx, N):
        size_sub_grid = int(math.sqrt(N))
        vars = (np.arange(N * N * N).reshape(N, N, N) + 1).astype('object')
        cnf = []

        #for i,j in enumerate(matrx.split()):
            #for x, y in enumerate(j):
                #print(x,y)

        # At least one digit per square
        for i in range(N):
            for j in range(N):
                cnf.append(vars[i, j, :].tolist())
        
        # Only one digit per square
        for i in range(N):
            for j in range(N):
                cnf += list(itertools.combinations(-vars[i, j, :], 2))
        
        #Sub grids need all different numbers
        for i in range(size_sub_grid):
            for j in range(size_sub_grid):
                for d in range(N):
                    cnf += list(itertools.combinations(-vars[i*size_sub_grid:i*size_sub_grid+size_sub_grid,
                        j*size_sub_grid:j*size_sub_grid+size_sub_grid, d].ravel(), 2))
        
        # Each row and each column must contain N different digits from 1 to N
        for i in range(N):
            for d in range(N):
                cnf += list(itertools.combinations(-vars[i,:,d].ravel(), 2))
                cnf += list(itertools.combinations(-vars[:,i,d].ravel(), 2))
        j = 0 
        # Tranform sudoku board to CNF
        for i, x in enumerate(matrx.split()):
            for y in x.split('.'):
                d = int(y) - 1                
                cnf.append([vars[i, j, d]])
            j += 1

        return [list(x) for x in cnf]
    
    def print_solution(self, solution, N):
        solution_a = np.array(solution).reshape(N,N,N)
        for i in range(N):
            for j in range(N):
                for d in range(N):
                    if solution_a[i, j, d] > 0:
                        print(d + 1, end="\t")
            print("")
        
    def pyco_solve(self, cnf, N):
        start = datetime.now()
        print(pycosat.solve(cnf))
        #pycosat.solve(cnf)
        #print(pycosat.solve(cnf))
        #print(cnf)
        exec_time = datetime.now() - start
        run_time = exec_time.total_seconds()
        return run_time 