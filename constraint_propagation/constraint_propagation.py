#!usr/var/python3
import copy

assignments_only = 0
forward_checking = 1
prop_singletons = 2
prop_any = 3

#Metod for propagation

def constraint_propagate(sudoku_constraints, domains, agenda, propagation_style):
    """Here we are going to code in python 4-methods of constraint propagation
    for sudoku problem. 
    
    1) Depth First Search,
    2) Depth First Search + Forward Checking
    3) Depth First Search + Forward Checking + propagation through singleton domains
    4) Depth First Search + Forward Checking + propagation through reduced domains

    This code is based on : http://web.mit.edu/dxh/www/6034-constraint.pdf    

    We will not print solution in this piece of code but only propagate constraints and save 
    the value for each instance from the benchmark sudoku puzzles!"""
    counter = 0
    solutions = [{'domains' : domains, 'open' : agenda + [], 'closed' : [],}]
    while solutions:
        csp = solutions.pop(0)
        counter += 1
        if not all(csp['domains'].values()):
            print('Dead end')
            continue
        if csp['closed']:
            print(csp['closed'])
            #check whether variables have been assigned and if yes then do forward checking!!
            assigned_var = csp['closed'][0]
            assigned_val = csp['domains'][assigned_var][0]                
            print("\nassigning " + str(assigned_var) + " = " + str(assigned_val))
            # check consistency of assignments so far
            if not all([ test( csp['domains'][xvar][0], 
                               csp['domains'][yvar][0] )
                         for xvar, yvar, test in sudoku_constraints 
                         if xvar in csp['closed'] and yvar in csp['closed']]) :
                print("Assignments are inconsistent! Backtracking.")
                continue
                
            # do forward checking / propagation
            propagation_queue = [assigned_var] if propagation_style is not assignments_only else []

            any_empty_domains = False
            while propagation_queue and not any_empty_domains :
                domains_before  = copy.deepcopy(csp['domains'])
                propagated_var = propagation_queue.pop(0)

                print ("checking neighbors of " + str(propagated_var))

                for this_var, other_var, test in sudoku_constraints:
                    if this_var is propagated_var:
                        check = lambda w : any([test(v, w) for v in csp['domains'][propagated_var]])
                        
                        reduced_domain = filter(check, csp['domains'][other_var])
                        if csp['domains'][other_var] != reduced_domain :
                            # if this constraint just eliminated some options
                            print ("\t " + str(other_var) + " can't be " + str(filter(lambda x : x not in reduced_domain, csp['domains'][other_var])))
                            csp['domains'][other_var] = reduced_domain
                # collect all reduced variables; see if any need to be propagated

                affected_vars = [x for x in iter(csp['domains']) 
                                 if csp['domains'][x] != domains_before[x] 
                                 and should_propagate(csp['domains'][x])]
                propagation_queue.extend(affected_vars)
                    
                any_empty_domains = not all(csp['domains'].values())

                if affected_vars and not any_empty_domains :
                    print ("!! adding " + str(affected_vars) + " to prop queue")
                
            if any_empty_domains:
                print ("Dead end --- eliminated all values from " + str(filter(lambda x : not csp['domains'][x], agenda)) + ". backtrack.")
                continue
            else :
                print ("ok")
        if not csp['open'] : # no more vars left in the agenda --- solution found!
            print ("success! "+str(counter)+" extensions.")
            print ({x : csp['domains'][x][0] for x in agenda})
            return {x : csp['domains'][x][0] for x in agenda}
        else :
            # generate the next level
            current_var = csp['open'].pop(0)
            csp['closed'] = [current_var] + csp['closed']

            new_solns = []
            for v in csp['domains'][current_var] :
                new_csp = copy.deepcopy(csp)
                new_csp['domains'][current_var] = [v]
                
                new_solns.append(new_csp)

            print ("\ndrawing all branches for " + str(current_var) + ": " + str([v for v in csp['domains'][current_var]]))

                
            solutions = new_solns + solutions
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
    constraint_propagate(sudoku_constraints,v1,['A'],prop_singletons)


load_sudoku():