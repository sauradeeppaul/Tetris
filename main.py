import pygame
import random
from shapes import *
from dimensions import *
from game_strings import *
from colors import *

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
"""

pygame.font.init()



class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = block_colors[blocks.index(shape)]
        self.rotation = 0


def create_grid(locked_positions={}):
    # Setting color to black
    grid = [[PLAYZONE_COLOR for _ in range(PLAYZONE_WIDTH/BLOCK_SIZE)] for _ in range(PLAYZONE_HEIGHT/BLOCK_SIZE)]

    # Setting locked blocks
    # TODO: Check if this works
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #

    for (j, i) in locked_positions:
        grid[i][j] = locked_positions[(j, i)]

    return grid



def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            pygame.draw.rect(surface,
                             grid[i][j],
                             (TOP_LEFT_X + j*BLOCK_SIZE, TOP_LEFT_Y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                             0)

    pygame.draw.rect(surface, BORDER_COLOR, (TOP_LEFT_X, TOP_LEFT_Y, PLAYZONE_WIDTH, PLAYZONE_HEIGHT), BORDER_SIZE)


def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


def draw_window(surface, grid):
    surface.fill(BACKGROUND_COLOR)

    pygame.font.init()
    font = pygame.font.SysFont(game_font, 60)
    title = font.render(game_name, 1, TITLE_COLOR)

    surface.blit(title, TOP_LEFT_X + (WINDOW_WIDTH - title.get_width())/2, TITLE_PADDING_Y)

    draw_window(surface, grid)
    pygame.display.update()


def main():
    pass


def main_menu():
    pass


main_menu()  # start game