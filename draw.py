import pygame
import sys
from cell import Cell

from constants import HEIGHT
from constants import WIDTH
from constants import CELLS_PER_SIDE
from constants import CELL_SIDE_LENGTH
from constants import SIDEBAR_WIDTH
from constants import BUTTON_WIDTH
from constants import BUTTON_HEIGHT
from constants import BUTTON_MARGIN

def drawButton(screen, width, height, x, y, name):
    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (100, 100, 100), button)
    font = pygame.font.Font(None, 24)
    text_surface = font.render(name, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button.center)
    screen.blit(text_surface, text_rect)
    return button

def drawGrid(screen, theGrid, gameStarted, puzzle):
    for i in range(CELLS_PER_SIDE + 1):
        line_width = 1 if i % 3 != 0 else 3
        pygame.draw.line(screen, (0, 0, 0), (i * CELL_SIDE_LENGTH, 0), (i * CELL_SIDE_LENGTH, HEIGHT), line_width)
        pygame.draw.line(screen, (0, 0, 0), (0, i * CELL_SIDE_LENGTH), (WIDTH, i * CELL_SIDE_LENGTH), line_width)

    if gameStarted:
        font = pygame.font.Font(None, 48)
        for x in range(CELLS_PER_SIDE):
            for y in range(CELLS_PER_SIDE):
                num = puzzle[x][y]
                if num != 0:
                    # Use different colors for original and user-entered numbers
                    color = (0, 0, 0) if theGrid[x][y].original else (150, 150, 150)
                    text_surface = font.render(str(num), True, color)
                    text_rect = text_surface.get_rect(center=(y * CELL_SIDE_LENGTH + CELL_SIDE_LENGTH / 2, x * CELL_SIDE_LENGTH + CELL_SIDE_LENGTH / 2))
                    screen.blit(text_surface, text_rect)

def drawSidebar(screen):
    pygame.draw.rect(screen, (200, 200, 200), (WIDTH, 0, SIDEBAR_WIDTH, HEIGHT))
    drawButton(screen, BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 100, "Quit")
    drawButton(screen, BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 775, "Default")
    drawButton(screen, BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 700, "Custom")
    drawButton(screen, BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 625, "Solve it")

def drawSelectedCell(screen, selectedCell):
    if selectedCell:
        x, y = selectedCell
        rect = pygame.Rect(y * CELL_SIDE_LENGTH, x * CELL_SIDE_LENGTH, CELL_SIDE_LENGTH, CELL_SIDE_LENGTH)
        pygame.draw.rect(screen, (0, 0, 255), rect, 3)
