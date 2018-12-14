import pygame
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
    font = pygame.font.SysFont(GAME_FONT, 60)
    title = font.render(GAME_NAME, 1, TITLE_COLOR)

    surface.blit(title, TOP_LEFT_X + (WINDOW_WIDTH - title.get_width())/2, TITLE_PADDING_Y)

    draw_window(surface, grid)
    pygame.display.update()


def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()

    clock = pygame.time.Clock()

    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        draw_window(surface, grid)


def main_menu():
    pass


win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(GAME_NAME)
main_menu()