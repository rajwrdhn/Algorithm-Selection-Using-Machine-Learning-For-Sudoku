class Vertex():
    def __init__(self, idx, data = 0):
        self.id = idx 
        self.data = data
        self.connectedTo = dict()
    
    def addNeighbour(self, neighbour, weight = 0):
        if neighbour.id not in self.connectedTo.keys() :  
            self.connectedTo[neighbour.id] = weight
    
    # setter
    def setData(self, data) : 
        self.data = data 

    #getter
    def getConnections(self) : 
        return self.connectedTo.keys()

    def getID(self) : 
        return self.id
    
    def getData(self) : 
        return self.data

    def getWeight(self, neighbour) : 
        return self.connectedTo[neighbour.id]

    def __str__(self) : 
        return str(self.data) + " Connected to : "+ \
         str([x.data for x in self.connectedTo])