import sys
import math
import pycosat
import networkx as nx
import time
def v(i,j,d, size):
    """
    i, j -> cell number
    d -> digit in the cell
    size -> size of the sudoku
    """
    return size*size *(i-1) + size * (j - 1) + d

def clauses_sudoku(size):
    """create all clauses for respective size of the puzzle
    """
    res = []
    # for all cells, ensure that the each cell:
    for i in range(1, size+1):
        for j in range(1, size+1):
            # denotes (at least) one of the size digits (1 clause)
            res.append([v(i, j, d, size) for d in range(1, size+1)])
            # does not denote two different digits at once 
            for d in range(1, size+1):
                for dp in range(d + 1, size+1):
                    res.append([-v(i, j, d, size), -v(i, j, dp, size)]) 

    def valid(cells):
        # Append clauses, corresponding to size of cells, to the result.
        # The size of cells are represented by a list tuples.  The new clauses
        # ensure that the cells contain distinct values.
        for i, xi in enumerate(cells):
            for j, xj in enumerate(cells):
                if i < j:
                    for d in range(1, size +1):
                        res.append([-v(xi[0], xi[1], d,size), -v(xj[0], xj[1], d, size)])

    # ensure rows and columns have distinct values
    for i in range(1, size+1):
        valid([(i, j) for j in range(1, size+1)])
        valid([(j, i) for j in range(1, size+1)])
    # ensure size sub-grids "regions" have distinct values
    for i in range(1,size,int(math.sqrt(size))):
        for j in range(1,size,int(math.sqrt(size))):
            valid([(i + k % int(math.sqrt(size)), j + k // int(math.sqrt(size))) for k in range(size)])
    #Test for size 9
    if (size == 9):
        assert len(res) == 81 * (1 + 36) + 27 * 324
    return res

def solve(grid, size):
    """
    solve a Sudoku grid inplace
    """
    clauses = clauses_sudoku(size)
    #print(clauses)
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            d = grid[i - 1][j - 1]
            # For each digit already known, a clause (with one literal).
            # Note:
            #     We could also remove all variables for the known cells
            #     altogether (which would be more efficient).  However, for
            #     the sake of simplicity, we decided not to do that.
            if d:
                clauses.append([v(i, j, d, size)])
    #print(clauses)
    # solve the SAT problem
    
    dpll = run_dpll(clauses)
    
    #sol = set(pycosat.solve(clauses))

    #def read_cell(i, j):
        # return the digit of cell i, j according to the solution
        #for d in range(1, size+1):
            #if v(i, j, d, size) in sol:
                #return d

    #for i in range(1, size +1):
        #for j in range(1, size+1):
            #grid[i - 1][j - 1] = read_cell(i, j)

def run_time_limit(x,y):
    x = time.time()

    y = time.time()

    if (y-x >= 2):
        print(y-x)
    else:
        print('here',y-x)
        #stop the program
    return y-x
    

def run_dpll(clauses):
    d_level = 0 
    Grph = nx.DiGraph()
    [Grph,conflict] = BCP(clauses,Grph,d_level)

    if (conflict):
        print("Unsatisfiable")
        return [False]
    
    while True: 
        d_level +=1
        [Grph, sat] = DECIDE(clauses, Grph, d_level)
        if (sat):
            node1 = find_node(Grph,'value',1)
            node0 = find_node(Grph,'value',0)
            node0 = [-1*i for i in node0]
            ans = sorted(node1+node0,key= abs)
            print('Satisfiable')
            return ans
        else:
            while True:
                [Grph, conflict] = BCP(clauses, Grph, d_level)
                if(not conflict):
                    break

                b_level = ANALYZE_CONFLICT(Grph)
                if (b_level==0):
                    print('Unsatisfiable')
                    return [False]
                else: 
                    d_level = b_level-1
                    Grph = BACK_TRACK(Grph, b_level, clauses)


def find_node(G, attr, value):
    result = []
    d = nx.get_node_attributes(G, attr)

    for key, v in d.items():
        if (v == value):
            result.append(key)
        
    
    return result

def find_max(G, attr): 
    maxi = -1

    d = nx.get_node_attributes(G, attr)
    
    v_list = [v for key,v in d.items()]

    if(v_list==[]):
        return 0
    else:
        return max(v_list)

def flatter(lst):
    x = []
    for i in lst:
        abs_lst = [abs(j) for j in i]
        x.extend(abs_lst)
    
    return x

def BCP(cnf,G,dl):
    fin = 0
    while fin==0: 
        fin = 1
        G_old = nx.DiGraph(G) 

        for i in range(len(cnf)):
            dec = 0 
            cnt = 0 
            for j in range(len(cnf[i])):
                if(cnf[i][j]<0):
                    cand = abs(cnf[i][j])
                    if(cand in list(G_old.nodes)): 
                        if(G_old.nodes[cand]['value']==0): 
                            dec=1
                            break
                    else: 
                        cnt += 1
                        fct = i
                        target = cnf[i][j]

                elif(cnf[i][j]>0): 
                    cand = cnf[i][j]
                    if(cand in list(G_old.nodes)):
                        if(G_old.nodes[cand]['value']==1):
                            dec=1
                            break
                    else:
                        cnt += 1
                        fct = i
                        target = cnf[i][j]

            if(dec==0 and cnt==0): 
                return [G,True]
            
            if(dec==0 and cnt==1): #unit-clause
                fin = 0

                wl_max = 0
                for j in list(set(cnf[fct])-{target}):
                    tmp = G.nodes[abs(j)]['w_level']
                    if(tmp>wl_max):
                        wl_max = tmp
                p_list = []
                for j in list(set(cnf[fct])-{target}): 
                    if(G.nodes[abs(j)]['w_level']==wl_max):
                        p_list.append(abs(j))
                wl = wl_max + 1

                if(target<0):
                    name = abs(target)
                    v = 0
                else:
                    name = target
                    v = 1

                if(not(name in list(G.nodes))): 
                    G.add_node(name, value = v, d_level = dl, w_level = wl) 
                    for k in p_list: 
                            G.add_edge(k,name,factor=fct)
                else: 
                    if(G.nodes[name]['value']==v): 
                        for k in p_list: 
                                G.add_edge(k,name,factor=fct)
                    else: 
                        return [G,True]
    return [G,False]

def DECIDE(cnf,G,dl):
    for i in range(len(cnf)):
        dec=0 
        for j in range(len(cnf[i])):
            if(cnf[i][j]<0):
                cand = abs(cnf[i][j])
                if(cand in list(G.nodes)):
                    if(G.nodes[cand]['value']==0):
                        dec=1
                        break
                else:
                    target = cnf[i][j]
            else: 
                cand = cnf[i][j]
                if(cand in list(G.nodes)):
                    if(G.nodes[cand]['value']==1):
                        dec=1
                        break
                else:
                    target = cnf[i][j]
        if(dec==0): 
            break

    if(dec==1): 
        return [G,True]
    else: 
        wl = find_max(G, 'w_level')
        if(wl==0):
            wl =1

        if(target<0):
            name = abs(target)
            v = 0
        else:
            name = target
            v = 1

        G.add_node(name, value = v, d_level = dl, w_level = wl)
        return [G,False]

def ANALYZE_CONFLICT(G):
    maxi = find_max(G,'d_level')
    return maxi

def BACK_TRACK(G,b_level,cnf):
    dl_lst = find_node(G,'d_level',b_level)
    
    min_wl = find_max(G,'w_level')
    for i in dl_lst:
        tmp = G.node[i]['w_level']
        if(tmp<min_wl):
            min_wl = tmp
    
    wl_lst = find_node(G,'w_level',min_wl) 
    
    new_fct = [] 
    for i in wl_lst:
        if(G.node[i]['value']==0):
            new_fct.append(i)
        if(G.node[i]['value']==1):
            new_fct.append(-1*i)

    new_fact = sorted(new_fct,key=abs)
    cnf.append(new_fact) 

    G.remove_nodes_from(dl_lst)

    return G

if __name__ == '__main__':
    from pprint import pprint

    # hard Sudoku problem,
    hard = [[3, 2, 0, 0],
            [0, 0, 0, 0],
            [1, 3, 4, 0],
            [0, 0, 0, 1]]
    solve(hard, 4)
    #pprint(hard)
