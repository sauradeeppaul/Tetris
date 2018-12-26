import pygame
from shapes import *
from dimensions import *
from game_strings import *
from colors import *
from values import *

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


def convert_shape_format(piece):
    positions = []
    orientation = piece.shape[piece.rotation % len(piece.shape)]

    for i, line in enumerate(orientation):
        rows = list(line)
        for j, column in enumerate(rows):
            if column == '0':
                positions.append((piece.x + j, piece.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - X_OFFSET, pos[1] - Y_OFFSET)

    return positions


def valid_space(piece, grid):
    valid_pos = [[(j, i) for j in range(PLAYZONE_WIDTH/BLOCK_SIZE) if grid[i][j] == PLAYZONE_COLOR] for i in range(PLAYZONE_HEIGHT/BLOCK_SIZE)]
    valid_pos = [j for sub in valid_pos for j in sub]

    converted_piece = convert_shape_format(piece)

    for pos in converted_piece:
        if pos not in valid_pos and pos[1] > -1:
            return False

    return True


def check_lost(positions):
    for x, y in positions:
        if y < 1:
            return True

    return False


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont(TEXT_GAME_FONT, size, bold=True)


def draw_grid(surface, grid):
    X = TOP_LEFT_X
    Y = TOP_LEFT_Y

    for i in range(len(grid)):
        pygame.draw.line(surface, GRID_COLOR, (X, Y + i*BLOCK_SIZE), (X + PLAYZONE_WIDTH, Y + i*BLOCK_SIZE))

    # TODO: Check
    for i in range(len(grid[0])):
        pygame.draw.line(surface, GRID_COLOR, (X + i*BLOCK_SIZE, Y), (X + i*BLOCK_SIZE, Y + PLAYZONE_HEIGHT))


def clear_rows(grid, locked):
    clear = 0

    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]

        if PLAYZONE_COLOR not in row:
            clear += 1
            removed_index = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if clear > 0:
        for pos in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = pos
            if y < removed_index:
                new_pos = (x, y + clear)
                locked[new_pos] = locked.pop(pos)

    return clear




def draw_next_shape(piece, surface):
    font = pygame.font.SysFont(TEXT_GAME_FONT, 30)
    text = font.render(TEXT_NEXT_SHAPE, 1, TITLE_COLOR)

    X = TOP_LEFT_X + PLAYZONE_WIDTH
    Y = TOP_LEFT_Y + PLAYZONE_HEIGHT/2

    orientation = piece.shape[piece.rotation % len(piece.shape)]

    for i, line in enumerate(orientation):
        rows = list(line)
        for j, column in enumerate(rows):
            if column == '0':
                pygame.draw.rect(surface, piece.color, (X + j*BLOCK_SIZE, Y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    surface.blit(text, (X + NEXT_POS_X, Y + NEXT_POS_Y))


def draw_window(surface, grid, score=0):
    surface.fill(BACKGROUND_COLOR)

    pygame.font.init()
    font = pygame.font.SysFont(TEXT_GAME_FONT, 60)
    title = font.render(TEXT_GAME_NAME, 1, TITLE_COLOR)

    surface.blit(title, (TOP_LEFT_X + (PLAYZONE_WIDTH - title.get_width())/2, TITLE_PADDING_Y))

    font = pygame.font.SysFont(TEXT_GAME_FONT, 30)
    text = font.render(TEXT_SCORE + str(score), 1, TITLE_COLOR)

    X = TOP_LEFT_X + PLAYZONE_WIDTH
    Y = TOP_LEFT_Y + PLAYZONE_HEIGHT / 2

    surface.blit(text, (X + 10, Y + 80))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface,
                             grid[i][j],
                             (TOP_LEFT_X + j*BLOCK_SIZE, TOP_LEFT_Y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                             0)

    pygame.draw.rect(surface, BORDER_COLOR, (TOP_LEFT_X, TOP_LEFT_Y, PLAYZONE_WIDTH, PLAYZONE_HEIGHT), BORDER_SIZE)

    draw_grid(surface, grid)


def main(surface):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()

    clock = pygame.time.Clock()

    fall_time = 0
    fall_speed = FALL_SPEED
    current_time = 0

    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        current_time += clock.get_rawtime()
        clock.tick()

        if current_time/1000 > SPEED_CHANGE:
            current_time = 0
            if fall_speed > 0.12:
                current_time -= SPEED_REDUCTION

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

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

        piece_pos = convert_shape_format(current_piece)

        for x, y in piece_pos:
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for p in piece_pos:
                # p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * SCORE_MULTIPLIER

        draw_window(surface, grid, score)
        draw_next_shape(next_piece, surface)

        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    pygame.display.quit()

def main_menu(win):
    main(win)


win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(TEXT_GAME_NAME)
main_menu(win)