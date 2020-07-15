#!usr/var/python
import numpy as np 
import pandas as pd 
from datetime import datetime
from ortools.sat.python import cp_model

import math

class Solver_or():
    def __init__(self, mtrx, problem_size):
        self.mtrx = mtrx
        self.problem_size = problem_size

    def solve_sudoku(self, matrx, N):
        assert matrx.shape == (N, N) # unit test 1

        size_sub_grid = int(math.sqrt(N))
        model = cp_model.CpModel()
        x = {} 
        for i in range(N):
            for j in range(N):
                if matrx[i][j] != 0:  # If block of sudoku is filled
                    x[i, j] = int(matrx[i][j])
                else:
                    x[i, j] = model.NewIntVarFromDomain(cp_model.Domain.FromValues([1, N]), 
                        'x[{},{}]'.format(i,j) )
        # Constraint in row
        for i in range(N):
            model.AddAllDifferent( [x[i, j] for j in range(N) ] )
        # Constraint in column
        for j in range(N):
            model.AddAllDifferent([x[i, j] for i in range(N)])

        # Constraint in sub_grid
        for row_idx in range(0, N, size_sub_grid):
            for col_idx in range(0, N, size_sub_grid):
                model.AddAllDifferent([x[row_idx + i, j] 
                    for j in range(col_idx, (col_idx + size_sub_grid)) 
                        for i in range(size_sub_grid)])

        #start timer
        start = datetime.now()
        # Initialize the solver
        solver = cp_model.CpSolver()        
        # Solving       
        status = solver.Solve(model)
        exec_time = datetime.now() - start
        print(solver.StatusName(status))
        result = np.zeros((N, N)).astype(np.int)
        print(cp_model.INFEASIBLE)
        #see if solved
        if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
            for i in range(N):
                for j in range(N):
                    result[i,j] = int(solver.Value(x[i,j]))
            return exec_time.total_seconds()
        else:
            exit
        



