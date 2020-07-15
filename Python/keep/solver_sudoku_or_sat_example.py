#!usr/var/python

from ortools.sat.python import cp_model
import numpy as np
from datetime import datetime
def solve_with_cp(grid: np.matrix) -> (np.matrix, float):
    '''Solve Sudoku instance (np.matrix) with CP modeling. Returns a tuple with the resulting matrix and the execution time in seconds.'''
    assert grid.shape == (9,9)
    
    grid_size = 9
    region_size = 3 #np.sqrt(grid_size).astype(np.int)
    model = cp_model.CpModel() # Step 1

    # Begin of Step2: Create and initialize variables.
    x = {}
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] != 0:
                x[i, j] = grid[i, j] # Initial values (values already defined on the puzzle).
            else:
                x[i, j] = model.NewIntVar(1, grid_size, 'x[{},{}]'.format(i,j) ) # Values to be found (variyng from 1 to 9).
    # End of Step 2.

    # Begin of Step3: Values constraints.
    # AllDifferent on rows, to declare that all elements of all rows must be different.
    for i in range(grid_size):
        model.AddAllDifferent([x[i, j] for j in range(grid_size)])

    # AllDifferent on columns, to declare that all elements of all columns must be different.
    for j in range(grid_size):
        model.AddAllDifferent([x[i, j] for i in range(grid_size)])

    # AllDifferent on regions, to declare that all elements of all regions must be different.
    for row_idx in range(0, grid_size, region_size):
        for col_idx in range(0, grid_size, region_size):
            model.AddAllDifferent([x[row_idx + i, j] for j in range(col_idx, (col_idx + region_size)) for i in range(region_size)])
    # End of Step 3.

    solver = cp_model.CpSolver() # Step 4
    start = datetime.now()
    status = solver.Solve(model) # Step 5
    exec_time = datetime.now() - start
    result = np.zeros((grid_size, grid_size)).astype(np.int)

    # Begin of Step 6: Getting values defined by the solver
    print(status)
    print(cp_model.FEASIBLE)
    if status == cp_model.FEASIBLE:
        for i in range(grid_size):
            for j in range(grid_size):
                result[i,j] = int(solver.Value(x[i,j]))
    else:
        raise Exception('Unfeasible Sudoku')
    # End of Step 6

    return result, exec_time.total_seconds()

res, _ = solve_with_cp(np.matrix([[5, 4, 9, 0, 0, 1, 7, 3, 8],
        [3, 6, 7, 0, 0, 8, 0, 0, 1],
        [2, 0, 0, 0, 7, 3, 0, 4, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 5],
        [0, 0, 0, 7, 0, 5, 4, 6, 0],
        [1, 3, 5, 8, 4, 0, 0, 7, 0],
        [0, 0, 4, 0, 0, 0, 3, 0, 7],
        [7, 8, 0, 3, 5, 0, 0, 0, 6],
        [0, 2, 3, 0, 8, 0, 0, 0, 0]]))
cp_solution = encode_sudoku(res) 

assert cp_solution == sample['solution'] # must show the same solution for the puzzle found on the dataset
res