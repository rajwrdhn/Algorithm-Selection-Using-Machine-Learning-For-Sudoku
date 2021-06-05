from node import Vertex
class Graph:
    """Graph class for the conversion"""
    totalV = 0 # total vertices in the graph
    
    def __init__(self) : 
        """
        allNodes = Dictionary (key:value)
                   idx : Node Object
        """
        self.allNodes = dict()

    def addNode(self, idx) : 
        """ adds the node """
        if idx in self.allNodes : 
            return None
        
        Graph.totalV += 1
        nod = Vertex(idx=idx)
        self.allNodes[idx] = nod
        return nod

    def addNodeData(self, idx, data) : 
        """ set node data acc to idx """
        if idx in self.allNodes : 
            node = self.allNodes[idx]
            self.setData(data)
        else : 
            print("No ID to add the data.")

    def addEdge(self, src, dst, wt = 0) : 
        """
        Adds edge between 2 nodes
        Undirected graph

        src = node_id = edge starts from
        dst = node_id = edge ends at

        To make it a directed graph comment the second line
        """
        self.allNodes[src].addNeighbour(self.allNodes[dst], wt)
        self.allNodes[dst].addNeighbour(self.allNodes[src], wt)
    
    def isNeighbour(self, u, v) : 
        """
        check neighbour exists or not
        """
        if u >=1 and u <= 81 and v >=1 and v<= 81 and u !=v : 
            if v in self.allNodes[u].getConnections() : 
                return True
        return False



    def printEdges(self) : 
        """ print all edges """
        for idx in self.allNodes :
            node =  self.allNodes[idx]
            for con in node.getConnections() : 
                print(self.allNodes[idx].getID(), " --> ", 
                self.allNodes[con].getID())
    
    # getter
    def getNode(self, idx) : 
        if idx in self.allNodes : 
            return self.allNodes[idx]
        return None

    def getAllNodesIds(self) : 
        return self.allNodes.keys()
"""
TESTING
"""
def test() : 
    g = Graph()
    for i in range(6) :
        g.addNode(i)

    print("Vertices : ",g.getAllNodesIds())

    g.addEdge(src = 0, dst = 1, wt = 5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)

    g.printEdges()

if __name__ == "__main__" : 
    test()