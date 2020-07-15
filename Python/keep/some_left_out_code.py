
        if (self.problem_size == 9 or self.problem_size == 'default'):
            self.sol = solve_sudoku(self.mtrx, self.problem_size)
        elif (self.problem_size == 16):
            self.sol = solve_sudoku(self.mtrx, self.problem_size)
        elif (self.problem_size == 25):
            print("I am here")
            self.sol = solve_sudoku(self.mtrx, self.problem_size)
        elif (self.problem_size == 36):
            self.sol = solve_sudoku(self.mtrx, self.problem_size)
        elif (self.problem_size == 49):
            self.sol = solve_sudoku(self.mtrx, self.problem_size)
        else:
            print("Problem size not defined properly!")



                               sudoku_init[i][j] = model_or_tool.NewIntVar(int(sudoku_to_do[i][j]), int(sudoku_to_do[i][j]),
                                                            'column: %i' % i)