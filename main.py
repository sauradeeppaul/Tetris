import pygame
import random
from shapes import blocks, block_colors

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

#Dimensions
window_width = 800
window_height = 700
play_zone_width = 300  # 300 // 10 = 30 width per block
play_zone_height = 600  # 600 // 20 = 30 height per block
block_size = 30

top_left_x = (window_width - play_zone_width) // 2
top_left_y = window_height - play_zone_height


class Piece(object):
    pass


def create_grid(locked_positions={}):
    pass


def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def get_shape():
    pass


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, row, col):
    pass


def clear_rows(grid, locked):


def draw_next_shape(shape, surface):


def draw_window(surface):
    pass


def main():
    pass


def main_menu():
    pass


main_menu()  # start game