import random

class SudokuGenerator:
    def __init__(self, numClues = 30):
        self.numClues = numClues
        self.grid = [[0] * 9 for _ in range(9)]
        self.numbers = list(range(1, 10))

    def fillGrid(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    random.shuffle(self.numbers)

                    for num in self.numbers:
                        if self.isValid(row, col, num):
                            self.grid[row][col] = num
                            if self.fillGrid():
                                return True
                            self.grid[row][col] = 0
                            
                    return False
        return True

    def isValid(self, row, col, num):
        for x in range(9):
            if self.grid[row][x] == num:
                return False
            
            if self.grid[x][col] == num:
                return False

        startRow = 3 * (row // 3)
        startCol = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[startRow + i][startCol + j] == num:
                    return False

        return True

    def removeCells(self):
        count = 81 - self.numClues
        while count > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)

            while self.grid[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            
            self.grid[row][col] = 0
            count -= 1

    def generatePuzzle(self):
        self.fillGrid()
        self.removeCells()
        return self.grid
