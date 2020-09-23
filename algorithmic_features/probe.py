from constraint import *

def Rooks_problem():
    problem = Problem()
    numpieces = 8
    cols = range(numpieces)
    rows = range(numpieces)
    problem.addVariables(cols, rows)
    for col1 in cols:
        for col2 in cols:
            if col1 < col2:
                problem.addConstraint(lambda row1, row2: row1 != row2,
                                    (col1, col2))
    solutions = problem.getSolutions()

    print (solutions)
def magic_square():
    problem = Problem()
    problem.addVariables(range(0, 16), range(1, 16+1))
    problem.addConstraint(AllDifferentConstraint(), range(0, 16))
    problem.addConstraint(ExactSumConstraint(34), [0,5,10,15])
    problem.addConstraint(ExactSumConstraint(34), [3,6,9,12])
    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34),
                            [row*4+i for i in range(4)])
    for col in range(4):
        problem.addConstraint(ExactSumConstraint(34),
                            [col+4*i for i in range(4)])
    solutions = problem.getSolutions()
    print(solutions)
Rooks_problem()
#magic_square()

