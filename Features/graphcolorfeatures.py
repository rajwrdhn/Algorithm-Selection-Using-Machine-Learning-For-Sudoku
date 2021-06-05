import sudokuConnections
class GraphColorAsSudoku():
    """In this we will compute the graphical features 
        of the sudoku by transforming each puzzle into a 
        graph colorin problem"""
    def __init__(self, sudoku, size):
        self.sudoku = sudoku # see this
        self.size = size
        self.board = self.make_puzzle()        
        self.sudokuGraph = sudokuConnections.SudokuConnections()
        #self.mappedGrid = self.__getGridMatrix()  # Maps all the ids to the position in the matrix
    
    def make_puzzle(self):
        return self.sudoku.tolist()
    
    def InitilizeColorForGraph(self):
        """
            fill the already given colors
        """
        color = [0] * (self.sudokuGraph.graph.totalV+1)
        given = [] # list of all the ids whos value is already given. Thus cannot be changed
        for row in range(len(self.board)) : 
            for col in range(len(self.board[row])) : 
                if self.make_puzzle()!= 0 : 
                    #first get the idx of the position
                    idx = self.mappedGrid[row][col]
                    #update the color
                    color[idx] = self.board[row][col] # this is the main imp part
                    given.append(idx)
        return color, given
    def pri(self):
        print(self.sudoku)
        print(self.size)