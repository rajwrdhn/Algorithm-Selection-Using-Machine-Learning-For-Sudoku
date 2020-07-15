#!usr/var/python
import numpy as np 
import math
from ortools.constraint_solver import pywrapcp
from datetime import datetime

class Solver_pywrapcp():
  def __init__(self, matrx, N, **kwargs):
    self.matrx = matrx
    self.N = N
  
  def solver_wrap(self, matrx, N):
    sub_grid = int(math.sqrt(N))

    # Create the solver.
    #solver = pywrapcp.Solver('sudoku', solver_parameters)
    
    solver = pywrapcp.Solver('sudoku')
    block_size = sub_grid
    line_size = N
    line = range(0, line_size)
    block = range(0, block_size)

    initial_grid = matrx

    grid = {}
    for i in line:
      for j in line:
        grid[(i, j)] = solver.IntVar( i , N, 'grid %i %i' % (i, j) )

    # AllDifferent on rows.
    for i in line:
      solver.Add(solver.AllDifferent([grid[(i, j)] for j in line]))

    # AllDifferent on columns.
    for j in line:
      solver.Add(solver.AllDifferent([grid[(i, j)] for i in line]))

    # AllDifferent on sub grids.
    for i in block:
      for j in block:
        one_block = []
        for di in block:
          for dj in block:
            one_block.append(grid[i * block_size + di, j * block_size + dj])

        solver.Add(solver.AllDifferent(one_block))

    # Initial values.
    for i in line:
      for j in line:
        if initial_grid[i][j]:
          solver.Add(grid[(i, j)] == initial_grid[i][j])

    all_vars = [grid[(i, j)] for i in line for j in line]

    db = solver.Phase(all_vars,
                      solver.INT_VAR_SIMPLE,
                      solver.INT_VALUE_SIMPLE)
    
    start = datetime.now()
        
    # And solve.
    solver.NewSearch(db)

    while solver.NextSolution():
      for i in line:
        print ([int(grid[i, j].Value()) for j in line])

    print ("num_solutions:", solver.Solutions())
    print ("failures:", solver.Failures())
    print ("branches:", solver.Branches())
    print ("wall_time:", solver.WallTime())
    exec_time = datetime.now() - start
    run_time = exec_time.total_seconds()
    return run_time