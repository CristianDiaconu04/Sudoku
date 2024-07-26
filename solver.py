class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def isValid(self, row, col, num):
        for x in range(9):
            if self.puzzle[row][x] == num:
                return False

        for x in range(9):
            if self.puzzle[x][col] == num:
                return False
            
            
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.puzzle[i + startRow][j + startCol] == num:
                    return False

        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == 0:
                    for num in range(1, 10):
                        
                        if self.isValid(row, col, num):
                            self.puzzle[row][col] = num
                            if self.solve():
                                return True
                            self.puzzle[row][col] = 0

                    return False
        return True
