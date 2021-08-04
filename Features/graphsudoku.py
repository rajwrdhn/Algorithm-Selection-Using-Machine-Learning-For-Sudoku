#!usr/var/python3
import numpy as np 
# Adjacency list representation
class SudokuGraph: 
    def __init__(self, df, size): 
        self.df = df  
        self.size = size
        self.adj = [[] for i in range(size*size)]
    
    def edgehelper(self):
        for i in range(self.size):
            for j in range(self.size):
                if (self.df[i][j] > 0 ):
                    self.addedge(i,j)

    # add edge to graph  
    def addedge (self, u, v): 
        self.adj[u].append(v)  
        self.adj[v].append(u) 
    
    # max degree
    def maxdegree(self, a , b ):
        if (a>b):
            return a 
        else: return b

    # Returns count of edge in undirected graph  
    def countedges(self): 
        count = 0
      
        # traverse all vertex  
        for i in range(self.V): 
      
            # add all edge that are linked  
            # to the current vertex  
            count += len(self.adj[i])  
      
        # The count of edge is always even   
        # because in undirected graph every edge   
        # is connected twice between two vertices  
        return count // 2

# Driver Code 
if __name__ == '__main__': 
    hard = np.array([ (3, 2, 0, 0),
            (0, 0, 0, 0),
            (1, 3, 4, 0),
            ( 2, 4, 0, 1)])
    g = SudokuGraph(hard, 4)
    g.edgehelper()
    print(g.adj)