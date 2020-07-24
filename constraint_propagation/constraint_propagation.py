#!usr/var/python3
import os
#Metod for propagation
def constraint_propagate(sudoku_constraints, domains, agenda):
    """Here we are going to code in python 4-methods of constraint propagation
    for sudoku problem. 
    
    1) Depth First Search,
    2) Depth First Search + Forward Checking
    3) Depth First Search + Forward Checking + propagation through singleton domains
    4) Depth First Search + Forward Checking + propagation through reduced domains

    This code is based on : http://web.mit.edu/dxh/www/6034-constraint.pdf    

    We will not print solution in this piece of code but only propagate constraints and save 
    the value for each instance from the benchmark sudoku puzzles!"""
    print(sudoku_constraints, domains)
    counter = 0
    solutions = [{'domains' : domains, 'open' : agenda + [], 'closed' : [],}]
    while solutions:
        csp = solutions.pop(0)
        print(csp)
        counter += 1
        
    return 0
#In sudoku we will have 3 distinct constraints and we will propagate them!
def row_constraint(variables) :
    return [[x, y, lambda a, b : a != b] 
            for x in variables for y in variables if x != y]

def column_constraint(variables) :
    return [[x, y, lambda a, b : a != b] 
            for x in variables for y in variables if x != y]

def sub_grid_constraint(variables) :
    return [[x, y, lambda a, b : a != b] 
            for x in variables for y in variables if x != y]

#create the variables according to the size of the sudoku %iA, %d form for 9 create 9 each so all will have same domain 1..9
v1 = {'A': [1]} #1 to N
v2 = {'A': [1]} #1 to N
v3 = {'A': [1]}#1 to N
sudoku_constraints = []
sudoku_constraints.extend(row_constraint(v1))
sudoku_constraints.extend(column_constraint(v2))
sudoku_constraints.extend(sub_grid_constraint(v3))

if True:
    constraint_propagate(sudoku_constraints,v1,['A'])