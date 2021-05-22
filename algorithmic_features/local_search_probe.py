import cspbase
import itertools
import math

def enforce_general_AC(constraint_list):
    Q = []

    for n in constraint_list:
        Q.append(n)
    
    while len(Q) > 0:
        C = cspbase.Q.pop(0)

        for V in C.scope:
            for d in V.cur_domain():
                if not C.has_support(V, d):
                    V.prune_value(d)

                    if V.cur_domain() == []:
                        return False
                    else:
                        Q = GAC_enq(constraint_list, Q, V)
    
    return True

def GAC_enq(cList, Q, V):
    for C in cList:
        if (V in C.scope) and (not (C in Q)):
            Q.append(C)
    
    return Q 

def sudoku_enforce_gac_model_1(sudoku_puzzle, size):
    variables = sudoku_variables(sudoku_puzzle, size)
    subgrids = group_subgrids(variables, size)
    cols = group_cols(variables, size)
    constraints = []
    checker = []
    for r in variables:
        for c1 in r:
            for c2 in r[r.index(c1) + 1:]:
                cons = cspbase.Constraint("BIN-ROW: (R" + str(variables.index(r)) + \
                                  ", C" + str(r.index(c1)) +") and (R" + str(variables.index(r)) + \
                                  ", C" + str(r.index(c2)) + ")", [c1, c2])
                cons.add_satisfying_tuples(sudoku_binary_permutations(c1, c2))
                constraints.append(cons)
                checker.apeend()
    
    for r in cols:
        for c1 in r:
            for c2 in r[r.index(c1) + 1: ]:
                if (c1, c2) not in checker:
                    cons = cspbase.Constraint("BIN-COL: (R" + str(cols.index(r)) + \
                                  ", C" + str(r.index(c1)) +") and (R" + str(cols.index(r)) + \
                                  ", C" + str(r.index(c2)) + ")", [c1, c2])
                    cons.add_satisfying_tuples(sudoku_binary_permutations(c1, c2))
                    constraints.append(cons)
                    checker.append((c1, c2))
    
    for r in subgrids:
        for c1 in r:
            for c2 in r[r.index(c1) +1:]:
                if (c1,c2) not in checker:
                    cons = cspbase.Constraint("BIN-BOX: (R" + str(subgrids.index(r)) + \
                                  ", C" + str(r.index(c1)) +") and (R" + str(subgrids.index(r)) + \
                                  ", C" + str(r.index(c2)) + ")", [c1, c2]) 
                    cons.add_satisfying_tuples(sudoku_binary_permutations(c1, c2))
                    constraints.append(cons)
                    checker.append((c1, c2))

    result_list = [] 
    for j in range(size): result_list.append([])

    e = enforce_general_AC(constraints)

    for r in variables:
        for c in r:
            result_list[variables.index(r)].append(c.cur_domain())

    return result_list                        

def sudoku_variables(sudoku, size):
    vars = []    
    
    for i in range(size): vars.append([])

    #setup variables for each cell
    for row in sudoku:
        for col in row:
            V = cspbase.Variable("CELL(" + str(sudoku.index(row)) + ", " + str(col) + ")")

            if col == 0:
                V.add_domain_values(range(size + 1) [1:])
            else:
                V.add_domain_values(col)
            
            vars[sudoku.index(row)].append(V)
    
    return vars

def sudoku_binary_permutations(D1, D2):
    L = []
    for n in D1.domain():
        for m in D2.domain():
            if n !=m:
                L.append([n,m])

    return L

def all_diff_permutations(V, permutations):
    fixed = []
    L = []

    for v in V:
        if len(v.cur_domain()) == 1:
            fixed.append((V.index(v), v.cur_domain()[0]))
    
    for p in permutations:
        test = True  
        for f in fixed:
            if p[f[0]] != f[1]:
                test = False   
                break 
        
        if (test): L.append(p)
    
    return L 

def group_cols(varibales, size):
    temp = range(size)
    cols = []
    for j in range(size): cols.append([])

    for i in temp:
        for j in temp:
            cols[i].append(varibales[j][i])


    return cols    

def group_subgrids(variables, size):
    subgrid = []

    temp = range(size)
    temp1 = int(math.sqrt(size))

    block = range(0, temp1)

    for j in range(size): subgrid.append([])

    for k in temp:
        for i in block:
            for j in block:
                one_block = []
                for di in block:
                    for dj in block:
                        one_block.append(variables[i+j][di+dj])

                subgrid[k].append(one_block)
    
    return subgrid