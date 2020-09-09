"""This model implements a sudoku solver."""

from __future__ import print_function

from ortools.sat.python import cp_model
import math
from datetime import datetime
import pandas 

class Solver_cpsat():
    def __init__(self, matrx, N):
        self.matrx = matrx
        self.N = N
    def solve_sudoku(self, matrx, N):
        #start = datetime.now()
        """Solves the sudoku problem with the CP-SAT solver."""
        # Create the model.
        model = cp_model.CpModel()

        cell_size = int(math.sqrt(N))
        line_size = N
        line = list(range(0, line_size))
        cell = list(range(0, cell_size))

        initial_grid = matrx

        grid = {}
        for i in line:
            for j in line:
                grid[(i, j)] = model.NewIntVar(1, line_size, 'grid %i %i' % (i, j))

        # AllDifferent on rows.
        for i in line:
            model.AddAllDifferent([grid[(i, j)] for j in line])

        # AllDifferent on columns.
        for j in line:
            model.AddAllDifferent([grid[(i, j)] for i in line])

        # AllDifferent on cells.
        for i in cell:
            for j in cell:
                one_cell = []
                for di in cell:
                    for dj in cell:
                        one_cell.append(grid[(i * cell_size + di,
                                            j * cell_size + dj)])

                model.AddAllDifferent(one_cell)

        # Initial values.
        for i in line:
            for j in line:
                if initial_grid[i][j]:
                    model.Add(grid[(i, j)] == initial_grid[i][j])
        
        start = datetime.now()
        # Solve and print out the solution.
        solver = cp_model.CpSolver()
        # Sets a time limit of in seconds.
        solver.parameters.max_time_in_seconds = 100000.0
        status = solver.Solve(model)
        exec_time = datetime.now() - start
        
        if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:						
            print('solved')
            #for i in line:
                #print([int(solver.Value(grid[(i, j)])) for j in line])
        else:
            print('unsolved')
        
        return exec_time.total_seconds()

