from graph import Graph

class sudoku_connections:
    def __init__(self, size):
        self.size = size
        self.rows = size
        self.cols = size
        self.total_blocks = size * size #81 in 9 sudoku-problem
        self.__generateGraph() # Generates all the nodes for the sudoku problem
        self.connectEdges() # connects all the nodes according to the constraints of the problem

        self.allIds = self.graph.getAllNodesIds() # storing all the ids in a list what will this do

    def __generateGraph(self) : 
        """
        Generates nodes with id from 1 to size*size.
        Both inclusive!!
        """
        for idx in range(1, self.total_blocks+1) : 
            _ = self.graph.addNode(idx)
    
    def connectEdges(self):
        """ 
        Connect rows, cols and subgrids according to the size and problem constraints. 
        """
        matrix = self.__getGridMatrix() 

        head_connections = dict()

        for row in range(self.size):
            for col in range(self.size):
                head = matrix[row][col]
                connections = self.__whatToConnect(matrix, row, col)
                head_connections[head] = connections
        self.__connectThose(head_connections=head_connections)

    def __connectThose(self, head_connections) : 
        for head in head_connections.keys() : #head is the start idx
            connections = head_connections[head]
            for key in connections :  #get list of all the connections
                for v in connections[key] : 
                    self.graph.addEdge(src=head, dst=v)

    def __getGridMatrix(self) : 
        """
        Generates the 9x9 grid or matrix consisting of node ids.
        
        This matrix will act as amapper of each cell with each node 
        through node ids
        """
        matrix = [[0 for cols in range(self.cols)] 
        for rows in range(self.rows)]

        count = 1
        for rows in range(9) :
            for cols in range(9):
                matrix[rows][cols] = count
                count+=1
        return matrix 

    def __whatToConnect(self, matrix, rows, cols) :

        """
        matrix : stores the id of each node representing each cell
        returns dictionary
        connections - dictionary
        rows : [all the ids in the rows]
        cols : [all the ids in the cols]
        blocks : [all the ids in the block]
        
        ** to be connected to the head.
        """
        connections = dict()

        row = []
        col = []
        block = []

        # ROWS
        for c in range(cols+1, self.size) : 
            row.append(matrix[rows][c])
        
        connections["rows"] = row

        # COLS 
        for r in range(rows+1, self.size):
            col.append(matrix[r][cols])
        
        connections["cols"] = col

        # BLOCKS
        
        if rows%3 == 0 : 

            if cols%3 == 0 :
                
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])

            elif cols%3 == 1 :
                
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])
                
            elif cols%3 == 2 :
                
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])

        elif rows%3 == 1 :
            
            if cols%3 == 0 :
                
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])

            elif cols%3 == 1 :
                
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                
            elif cols%3 == 2 :
                
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])

        elif rows%3 == 2 :
            
            if cols%3 == 0 :
                
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])

            elif cols%3 == 1 :
                
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                
            elif cols%3 == 2 :
                
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
        
        connections["blocks"] = block
        return connections