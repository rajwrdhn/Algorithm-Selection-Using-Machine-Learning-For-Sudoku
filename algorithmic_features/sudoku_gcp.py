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