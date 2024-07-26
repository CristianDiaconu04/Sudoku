import pygame
import sys
from cell import Cell
from puzzles import PUZZLE1

from constants import HEIGHT
from constants import WIDTH
from constants import CELLS_PER_SIDE
from constants import CELL_SIDE_LENGTH
from constants import SIDEBAR_WIDTH
from constants import BUTTON_WIDTH
from constants import BUTTON_HEIGHT
from constants import BUTTON_MARGIN

from draw import drawButton
from draw import drawGrid
from draw import drawSidebar
from draw import drawSelectedCell

from solver import SudokuSolver
from sudokuGenerator import SudokuGenerator

pygame.init()

screen = pygame.display.set_mode((WIDTH + SIDEBAR_WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
screen.fill((255, 255, 255))  # Makes it white

# Set up the grid of cells (2D list, 9x9)
theGrid = [[Cell(x, y) for y in range(CELLS_PER_SIDE)] for x in range(CELLS_PER_SIDE)]
for x in range(CELLS_PER_SIDE):
    for y in range(CELLS_PER_SIDE):
        theGrid[x][y].x = x 
        theGrid[x][y].y = y 

quitButton = drawButton(screen, BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 100, "Quit")
defaultButton = drawButton(screen, BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 775, "Default")
customButton = drawButton(screen, BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 700, "Custom")
solveButton = drawButton(screen, BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 625, "Solve it")

def runGame():
    running = True
    gameStarted = False
    gameDefault = False
    customMode = False

    puzzle = []
    selectedCell = None
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if quitButton.collidepoint(pos):
                        sys.exit()
                    
                    elif defaultButton.collidepoint(pos):
                        gameDefault = True
                        customMode = False
                        puzzle = PUZZLE1
                        gameStarted = True
                        
                        # Mark original cells
                        for x in range(CELLS_PER_SIDE):
                            for y in range(CELLS_PER_SIDE):
                                theGrid[x][y].num = puzzle[x][y]
                                theGrid[x][y].original = puzzle[x][y] != 0

                    elif customButton.collidepoint(pos):
                        gameDefault = False
                        customMode = True
                        gameStarted = True
                        generator = SudokuGenerator()
                        puzzle = generator.generatePuzzle()
                        
                        # Mark original cells
                        for x in range(CELLS_PER_SIDE):
                            for y in range(CELLS_PER_SIDE):
                                theGrid[x][y].num = puzzle[x][y]
                                theGrid[x][y].original = puzzle[x][y] != 0

                    elif solveButton.collidepoint(pos):
                        if gameStarted:
                            solver = SudokuSolver(puzzle)
                            solver.solve()
                            # Update the grid with the solved puzzle
                            for x in range(CELLS_PER_SIDE):
                                for y in range(CELLS_PER_SIDE):
                                    theGrid[x][y].num = puzzle[x][y]

                    elif pos[0] < WIDTH and gameStarted:
                        x = pos[1] // CELL_SIDE_LENGTH
                        y = pos[0] // CELL_SIDE_LENGTH
                        selectedCell = (int(x), int(y))

            elif event.type == pygame.KEYDOWN and gameStarted and selectedCell:
                if event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
                    x, y = selectedCell
                    if customMode or not theGrid[x][y].original:
                        puzzle[x][y] = int(event.unicode)
                        theGrid[x][y].num = int(event.unicode)

        screen.fill((255, 255, 255))
        drawGrid(screen, theGrid, gameStarted, puzzle)
        drawSidebar(screen)

        # Highlight selected cell
        drawSelectedCell(screen, selectedCell)  
        
        pygame.display.flip()

runGame()
