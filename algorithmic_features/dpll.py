import math
import numpy as np 
import itertools
import pycosat
matrx = """\
8........
..36.....
.7..9.2..
.5...7...
....457..
...1...3.
..1....68
..85...1.
.9....4..
"""
def get_cnf(size):
    N = size 
    sub_grid_size = int(math.sqrt(size))
    vars = (np.arange(N * N * N).reshape(N, N, N) + 1).astype('object')
    cnf = []

    # At least one digit per square
    for i in range(N):
        for j in range(N):
            cnf.append(vars[i, j, :].tolist())

    # Only one digit per square
    for i in range(N):
        for j in range(N):
            cnf += list(itertools.combinations(-vars[i, j, :], 2))
    
    #Sub grids need all different numbers
    for i in range(sub_grid_size):
        for j in range(sub_grid_size):
            for d in range(N):
                cnf += list(itertools.combinations(-vars[i*sub_grid_size:i*sub_grid_size+sub_grid_size,
                    j*sub_grid_size:j*sub_grid_size+sub_grid_size, d].ravel(), 2))
        
    # Each row and each column must contain N different digits from 1 to N
    for i in range(N):
        for d in range(N):
            cnf += list(itertools.combinations(-vars[i,:,d].ravel(), 2))
            cnf += list(itertools.combinations(-vars[:,i,d].ravel(), 2))

    # Tranform sudoku board to CNF
    for i, x in enumerate(matrx.split()):
        for j, y in enumerate(x):
            if y == '.':
                continue
            d = int(y) - 1
            cnf.append([vars[i, j, d]])
    print(cnf)
    
    return [list(x) for x in cnf]

x = get_cnf(9)

#print(x)

