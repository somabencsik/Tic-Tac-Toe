# TODO: May change "check_winning_position" for not only checking BOARD_SIZE for winning

import pygame
import time

MAX_WIDTH = 800
MAX_HEIGHT = 600
BOARD_SIZE = 3

window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

symbols_on_table = {}
for size in range(BOARD_SIZE):
    symbols_on_table[size] = ["" for _ in range(BOARD_SIZE)]

pygame.font.init()
font = pygame.font.SysFont("monospace", 75)
next_symbol = "x"
is_running = True

def draw_table(window: pygame.Surface, symbols_on_table: dict) -> None:
    """Draws the table based on the current state."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            cell_x = col * MAX_WIDTH / BOARD_SIZE
            cell_y = row * MAX_HEIGHT / BOARD_SIZE
            cell_width = cell_x + MAX_WIDTH / BOARD_SIZE
            cell_height = cell_y + MAX_HEIGHT / BOARD_SIZE

            if symbols_on_table[row][col] == "x":
                pygame.draw.line(window, (200, 0, 0), (cell_x + 50, cell_y + 50), (cell_width - 50, cell_height - 50), width=3)
                pygame.draw.line(window, (200, 0, 0), (cell_width - (cell_x + 50) + cell_x, cell_y + 50), (cell_width - (cell_width - 50) + cell_x, cell_height - 50), width=3)
            elif symbols_on_table[row][col] == "o":
                pygame.draw.circle(window, (0, 0, 200), ((cell_x + cell_width) / 2, (cell_y + cell_height) / 2), 50, width = 3)

    for width_multiplier in range(BOARD_SIZE):
        pygame.draw.line(window, (0, 0, 0), (MAX_WIDTH / BOARD_SIZE * width_multiplier, 0), (MAX_WIDTH / BOARD_SIZE * width_multiplier, MAX_HEIGHT), width=3)
    for height_multiplier in range(BOARD_SIZE):
        pygame.draw.line(window, (0, 0, 0), (0, MAX_HEIGHT / BOARD_SIZE * height_multiplier), (MAX_WIDTH, MAX_HEIGHT / BOARD_SIZE * height_multiplier), width=3)
        
def place_symbol(symbol: str, symbols_on_table: dict) -> bool:
    """Place current symbol in the given table returns True if success False if it is already occupied"""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            cell_x = col * MAX_WIDTH / BOARD_SIZE
            cell_y = row * MAX_HEIGHT / BOARD_SIZE
            cell_width = cell_x + MAX_WIDTH / BOARD_SIZE
            cell_height = cell_y + MAX_HEIGHT / BOARD_SIZE
            if mouse_x > cell_x and mouse_x < cell_width and mouse_y > cell_y and mouse_y < cell_height:
                if symbols_on_table[row][col] != "":
                    return False
                symbols_on_table[row][col] = symbol
    return True

def check_winning_position(symbols_on_table: dict) -> bool:
    """Returns True if there is a winning position, False if not."""
    
    # 1. Check rows
    for row in symbols_on_table:
        win_in_row = True
        for symbol in symbols_on_table[row][1:]:
            if symbols_on_table[row][0] == "" or (symbols_on_table[row][0] != symbol or symbol == ""):
                win_in_row = False
                continue
        if win_in_row:
            return True

    # 2. Check colums
    for col_idx in range(BOARD_SIZE):
        col = [ symbols_on_table[row][col_idx] for row in symbols_on_table ]
        if "" in col:
            continue
        if all( [col[0] == symbol for symbol in col[1:]] ):
            return True

    # 3. Check diagonals
    left_to_right_diagonal = [symbols_on_table[row][row] for row in symbols_on_table]
    if "" not in left_to_right_diagonal:
        if all([left_to_right_diagonal[0] == symbol for symbol in left_to_right_diagonal[1:]]):
            return True
        
    right_to_left_diagonal = [symbols_on_table[row][BOARD_SIZE - row - 1] for row in symbols_on_table]
    if "" not in right_to_left_diagonal:
        if all([right_to_left_diagonal[0] == symbol for symbol in right_to_left_diagonal[1:]]):
            return True

    return False

def check_full(symbols_on_table: dict) -> bool:
    """Check if the table is full with symbols."""
    for row in symbols_on_table:
        for symbol in symbols_on_table[row]:
            if symbol == "":
                return False
    return True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_placed = place_symbol(next_symbol, symbols_on_table)
            is_win = check_winning_position(symbols_on_table)
            is_full = check_full(symbols_on_table)

            if is_win:
                is_running = False
                window.fill((127, 127, 127))

                for i in range(3):
                    label = font.render(f"{next_symbol} is the winner!", 1, (0, 0, 0))
                    label2 = font.render(f"Exiting in {3 - i}", 1, (0, 0, 0))
                    window.blit(label, ( (MAX_WIDTH / 2) - (label.get_width() / 2), (MAX_HEIGHT / 2) - (label.get_height() / 2) ) )
                    window.blit(label2, ( (MAX_WIDTH / 2) - (label2.get_width() / 2), (MAX_HEIGHT / 2) - (label2.get_height() / 2) + label2.get_height() ) )
                    pygame.display.flip()
                    time.sleep(1)
                    window.fill((127, 127, 127))

            if not is_win and is_full:
                is_running = False
                window.fill((127, 127, 127))

                for i in range(3):
                    label = font.render(f"TIE!", 1, (0, 0, 0))
                    label2 = font.render(f"Exiting in {3 - i}", 1, (0, 0, 0))
                    window.blit(label, ( (MAX_WIDTH / 2) - (label.get_width() / 2), (MAX_HEIGHT / 2) - (label.get_height() / 2) ) )
                    window.blit(label2, ( (MAX_WIDTH / 2) - (label2.get_width() / 2), (MAX_HEIGHT / 2) - (label2.get_height() / 2) + label2.get_height() ) )
                    pygame.display.flip()
                    time.sleep(1)
                    window.fill((127, 127, 127))

            if is_placed:
                next_symbol = "x" if next_symbol != "x" else "o"

        window.fill((127, 127, 127))
        
        draw_table(window, symbols_on_table)
        
        pygame.display.flip()


