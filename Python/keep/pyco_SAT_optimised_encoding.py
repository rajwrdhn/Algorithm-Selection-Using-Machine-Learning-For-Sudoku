#!usr/var/python

import pycosat 
import numpy
import math
import itertools

class solver_Pycosat_optimised_encoding():
    def __init__(self, matrx, N):
        self.matrx = matrx
        self.N = N
    
    def solve_sudoku(self):
        assert 