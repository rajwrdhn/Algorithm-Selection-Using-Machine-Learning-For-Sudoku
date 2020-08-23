import copy 

# Updated: 18/Oct/2014

# THE FOUR METHODS OF CONSTRAINT PROPAGATION
# 0 : check assignments only
# 1 : dfs + forward checking 
# 2 : dfs + fc + prop-1
# 3 : dfs + fc + prop-any

assignments_only = 0
forward_checking = 1
prop_singletons = 2
prop_any = 3


# HERE IS THE ALGORITHM. SCROLL DOWN FOR SAMPLE PROBLEMS.

def solve_csp(constraints, domains, agenda, propagation_style=forward_checking) :
    
    if propagation_style is prop_singletons :
        should_propagate = lambda domain : len(domain) == 1
    elif propagation_style is prop_any:
        should_propagate = lambda domain : True
    else:
        should_propagate = lambda domain : False


    extension_count = 0
    solns = [{'domains' : domains, 'open' : agenda + [], 'closed' : [],}]
    while solns :
        csp = solns.pop(0)
        extension_count += 1
        if not all(csp['domains'].values()) : # some domains are empty
            print ("dead end ")
            continue

        if csp['closed'] : 
            # have any variables been assigned? if so, check consistency and do forward checking, etc.
            assigned_var = csp['closed'][0]
            assigned_val = csp['domains'][assigned_var][0]
                
            print ("\nassigning " + str(assigned_var) + " = " + str(assigned_val))

            # check consistency of assignments so far
            if not all([ test( csp['domains'][xvar][0], 
                               csp['domains'][yvar][0] )
                         for xvar, yvar, test in constraints 
                         if xvar in csp['closed'] and yvar in csp['closed']]) :
                print ("Assignments are inconsistent! Backtracking.")
                continue
                
            # do forward checking / propagation
            propagation_queue = [assigned_var] if propagation_style is not assignments_only else []

            any_empty_domains = False
            while propagation_queue and not any_empty_domains :
                domains_before  = copy.deepcopy(csp['domains'])
                propagated_var = propagation_queue.pop(0)

                print ("checking neighbors of " + str(propagated_var))

                for this_var, other_var, test in constraints :
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
            print ("success! ("+str(extension_count)+" extensions.)")
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

                
            solns = new_solns + solns
    print ("Terminal failure: no solution exists.")        


                         
                        
                
            

### ******************* SAMPLE PROBLEMS

def require_distinct(variables) :
    return [[x, y, lambda a, b : a != b] 
            for x in variables for y in variables if x != y]

def require_equal(variables) :
    return [[x, y, lambda a, b : a == b] 
            for x in variables for y in variables if x != y]

def require_buffer_zone(variables) :
    return [[x, y, lambda a, b : abs(a-b) > 1] 
            for x in variables for y in variables if x != y]


def require_neighbor(variables) :
    return [[x, y, lambda a, b : abs(a-b) == 1] 
            for x in variables for y in variables if x != y]
    

time_constraints = []
time_constraints.extend(require_distinct(["B","C","N"]))
time_constraints.extend(require_distinct(["L","P","N"]))
time_constraints.extend(require_distinct(["S","P"]))
time_constraints.extend(require_distinct(["L","C"]))
time_constraints.extend(require_distinct(["T","L","N"]))
time_constraints.extend(require_distinct(["C","P"]))


if False :
    solve_csp(time_constraints, 
               {"T" : [1],
                "L" : [1, 2, 3, 4],
                "B" : [1, 2, 3, 4],
                "C" : [1, 2, 3, 4],
                "P" : [1, 2, 3, 4],
                "S" : [1, 2, 3, 4],
                "N" : [1, 2, 3, 4]},
               list("TLBCSPN"),
               prop_singletons)









zoo_constraints = []
zoo_constraints.extend(require_distinct(["L", "EL"]))
zoo_constraints.extend(require_equal(["M", "B"]))

zoo_constraints.extend(require_distinct(["H", "L"]))
zoo_constraints.extend(require_distinct(["H", "HB"]))
zoo_constraints.extend(require_distinct(["H", "M"]))
zoo_constraints.extend(require_distinct(["H", "B"]))
zoo_constraints.extend(require_distinct(["H", "A"]))

zoo_constraints.extend(require_distinct(["EL", "M"]))
zoo_constraints.extend(require_distinct(["EL", "B"]))
zoo_constraints.extend(require_distinct(["EL", "HB"]))

zoo_constraints.extend(require_buffer_zone(["L", "A"]))
zoo_constraints.extend(require_buffer_zone(["EL", "A"]))

zoo_constraints.extend(require_distinct(["L", "HB"]))


if False:
    solve_csp(zoo_constraints, 
               {"L" : [1],
                "HB" : [2, 3, 4],
                "A" : [3, 4],
                "EL" : [2, 3, 4],
                "H" : [2, 3, 4],
                "M" : [1, 2, 3, 4],
                "B" : [1, 2, 3, 4]},
               ["L","HB", "A", "EL", "H", "M", "B"],
               prop_any
               )









pokemon_constraints = []
pokemon_constraints.extend(require_distinct(["fastest", "slowest"]))
pokemon_constraints.extend(require_equal(["heaviest", "slowest"]))

pokemon_constraints.extend(require_distinct(["shortest", "heaviest"]))
pokemon_constraints.extend(require_distinct(["shortest", "fastest"]))

pokemon_constraints.extend(require_equal(["footprint", "fastest"]))



# 20, assignments only
# 9, forward checking
# 8, singletons
# 7, reduced

if False :
    # 2012Q2 Part B
    solve_csp(pokemon_constraints, 
               {"slowest" : list("ABCE"),
                "heaviest" : list("BCD"),
                "shortest" : list("BCD"),
                "fastest" : list("BCD"),
                "footprint" : list("ACE")},
               ["slowest","heaviest", "shortest", "fastest", "footprint"],
              assignments_only)
if False :
    # 2012Q2 Part D
    # reordered vars, prop singletons
    solve_csp(pokemon_constraints, 
               {"slowest" : list("ABCE"),
                "heaviest" : list("BCD"),
                "shortest" : list("BCD"),
                "fastest" : list("BCD"),
                "footprint" : list("ACE")},
               ["fastest", "slowest","heaviest", "shortest", "footprint"],
               prop_singletons)


mtg_constraints = []
mtg_constraints.extend(require_equal(["Ajani","Elspeth"]))

mtg_constraints.extend(require_distinct(["Bolas","Ajani"]))
mtg_constraints.extend(require_distinct(["Bolas","Chandra"]))
mtg_constraints.extend(require_distinct(["Bolas","Dack"]))
mtg_constraints.extend(require_distinct(["Bolas","Elspeth"]))
mtg_constraints.extend(require_distinct(["Bolas","Gideon"]))


mtg_constraints.extend(require_neighbor(["Chandra","Dack"]))

mtg_constraints.extend(require_buffer_zone(["Gideon","Dack"]))
mtg_constraints.extend(require_buffer_zone(["Gideon","Chandra"]))



if False :
    solve_csp(mtg_constraints, 
              {"Ajani" : [1, 2, 3, 4, 5 ],
               "Bolas" :  [1, 2, 3, 4],
               "Chandra" :  [1, 2, 3, 4, 5],
               "Dack" :  [1, 4], # 4
               "Elspeth" :  [3],
               "Gideon" :  [1, 2, 3, 4, 5]},
              ["Ajani", "Elspeth","Dack", "Gideon", "Bolas", "Chandra"],
              prop_singletons)




    
zig_constraints = []
zig_constraints.extend(require_equal(["A","B"]))
zig_constraints.extend(require_equal(["B","Z"]))
zig_constraints.extend(require_distinct(["Z","D"]))
zig_constraints.extend(require_equal(["D","C"]))


# solve_csp(zig_constraints, 
#           {"A" : [2 ],
#            "B" :  [1, 2, 3],
#            "C" :  [2, 3],
#            "D" :  [1, 2, 3], # 4
#            "Z" :  [1, 2, 3]
#           },
#           list("ABZDC"),
#           prop_any)

# 13
# 7
# 7
# 6


def require_greater(variables) :
    return [[x, y, lambda x,y : x > y] for (x,y) in zip(variables,variables[1:])]

zag_constraints = []
zag_constraints.extend(require_greater(["B","E","F"]))
zag_constraints.extend(require_equal(["A","D"]))
zag_constraints.extend(require_equal(["D","C"]))
zag_constraints.extend(require_distinct(["D","E"]))


greater_constraints = require_greater(list("ABCD"))


for method in (assignments_only, forward_checking, prop_singletons, prop_any) :
    print ("-"*36)
    solve_csp(greater_constraints, 
              {"A" : [1, 2, 3, 4],
               "B" :  [1, 2, 3, 4],
               "C" :  [1, 2, 3, 4],
               "D" :  [1, 2, 3, 4]
           },
              list("ABCD"),
              method)
