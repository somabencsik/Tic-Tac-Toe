"""Defines the Tic-Tac-Toe game."""
import time

import pygame


class TicTacToe:
    """Class for Tic-Tac-Toe."""

    def __init__(self, window: "Window", board_size: int) -> None:
        self.window = window
        self.board_size = board_size

        self.is_running = False
        self.background_color = (127, 127, 127)

    def start(self) -> None:
        """Start the game initialize basic variables."""
        self.is_running = True
        self.next_symbol = "x"
        pygame.font.init()
        self.font = pygame.font.SysFont("monospace", 75)

        self.symbols_on_table: dict[int, list] = {}
        for size in range(self.board_size):
            self.symbols_on_table[size] = ["" for _ in range(self.board_size)]

        self.game_loop()

    def game_loop(self) -> None:
        """Infinite game loop."""
        while self.is_running:
            self.process_input()

            self.update()
            self.render()

    def process_input(self) -> None:
        """Process the user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_placed = self._place_symbol()
                is_win = self._check_winning_position()
                is_full = self._check_full()

                should_close = self._show_winner(is_win, is_full)

                if should_close:
                    self.is_running = False

                if is_placed:
                    self.next_symbol = "x" if self.next_symbol != "x" else "o"

    def update(self) -> None:
        """Update the game."""

    def render(self) -> None:
        """Render game components."""
        self.window.window.fill(self.background_color)
        self._draw_game_board()
        pygame.display.flip()

    def _draw_game_board(self) -> None:
        for row in range(self.board_size):
            for col in range(self.board_size):
                cell_x = col * self.window.width / self.board_size
                cell_y = row * self.window.height / self.board_size
                cell_width = cell_x + self.window.width / self.board_size
                cell_height = cell_y + self.window.height / self.board_size

                if self.symbols_on_table[row][col] == "x":
                    pygame.draw.line(
                        self.window.window,
                        (200, 0, 0),
                        (cell_x + 50, cell_y + 50),
                        (cell_width - 50, cell_height - 50),
                        width=3,
                    )
                    pygame.draw.line(
                        self.window.window,
                        (200, 0, 0),
                        (cell_width - (cell_x + 50) + cell_x, cell_y + 50),
                        (cell_width - (cell_width - 50) + cell_x, cell_height - 50),
                        width=3,
                    )
                elif self.symbols_on_table[row][col] == "o":
                    pygame.draw.circle(
                        self.window.window,
                        (0, 0, 200),
                        ((cell_x + cell_width) / 2, (cell_y + cell_height) / 2),
                        50,
                        width=3,
                    )

        for width_multiplier in range(self.board_size):
            pygame.draw.line(
                self.window.window,
                (0, 0, 0),
                (self.window.width / self.board_size * width_multiplier, 0),
                (
                    self.window.width / self.board_size * width_multiplier,
                    self.window.height,
                ),
                width=3,
            )
        for height_multiplier in range(self.board_size):
            pygame.draw.line(
                self.window.window,
                (0, 0, 0),
                (0, self.window.height / self.board_size * height_multiplier),
                (
                    self.window.width,
                    self.window.height / self.board_size * height_multiplier,
                ),
                width=3,
            )

    def _place_symbol(self) -> bool:
        """Place current symbol in the given table returns True if success False if it is already occupied"""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for row in range(self.board_size):
            for col in range(self.board_size):
                cell_x = col * self.window.width / self.board_size
                cell_y = row * self.window.height / self.board_size
                cell_width = cell_x + self.window.width / self.board_size
                cell_height = cell_y + self.window.height / self.board_size
                if (
                    mouse_x > cell_x
                    and mouse_x < cell_width
                    and mouse_y > cell_y
                    and mouse_y < cell_height
                ):
                    if self.symbols_on_table[row][col] != "":
                        return False
                    self.symbols_on_table[row][col] = self.next_symbol
        return True

    def _check_winning_position(self) -> bool:
        """Returns True if there is a winning position, False if not."""

        # 1. Check rows
        for row in self.symbols_on_table:
            win_in_row = True
            for symbol in self.symbols_on_table[row][1:]:
                if self.symbols_on_table[row][0] == "" or (
                    self.symbols_on_table[row][0] != symbol or symbol == ""
                ):
                    win_in_row = False
                    continue
            if win_in_row:
                return True

        # 2. Check colums
        for col_idx in range(self.board_size):
            col = [self.symbols_on_table[row][col_idx] for row in self.symbols_on_table]
            if "" in col:
                continue
            if all([col[0] == symbol for symbol in col[1:]]):
                return True

        # 3. Check diagonals
        left_to_right_diagonal = [
            self.symbols_on_table[row][row] for row in self.symbols_on_table
        ]
        if "" not in left_to_right_diagonal:
            if all(
                [
                    left_to_right_diagonal[0] == symbol
                    for symbol in left_to_right_diagonal[1:]
                ]
            ):
                return True

        right_to_left_diagonal = [
            self.symbols_on_table[row][self.board_size - row - 1]
            for row in self.symbols_on_table
        ]
        if "" not in right_to_left_diagonal:
            if all(
                [
                    right_to_left_diagonal[0] == symbol
                    for symbol in right_to_left_diagonal[1:]
                ]
            ):
                return True

        return False

    def _check_full(self) -> bool:
        """Check if the table is full with symbols."""
        for row in self.symbols_on_table:
            for symbol in self.symbols_on_table[row]:
                if symbol == "":
                    return False
        return True

    def _show_winner(self, is_win: bool, is_full: bool) -> bool:
        """Display end message if smbd won or it is tie."""
        if not is_win and not is_full:
            return False

        if is_win:
            is_running = False
            self.window.window.fill((127, 127, 127))

            for i in range(3):
                label = self.font.render(
                    f"{self.next_symbol} is the winner!", 1, (0, 0, 0)
                )
                label2 = self.font.render(f"Exiting in {3 - i}", 1, (0, 0, 0))
                self.window.window.blit(
                    label,
                    (
                        (self.window.width / 2) - (label.get_width() / 2),
                        (self.window.height / 2) - (label.get_height() / 2),
                    ),
                )
                self.window.window.blit(
                    label2,
                    (
                        (self.window.width / 2) - (label2.get_width() / 2),
                        (self.window.height / 2)
                        - (label2.get_height() / 2)
                        + label2.get_height(),
                    ),
                )
                pygame.display.flip()
                time.sleep(1)
                self.window.window.fill((127, 127, 127))

            return True

        if not is_win and is_full:
            is_running = False
            self.window.window.fill((127, 127, 127))

            for i in range(3):
                label = self.font.render(f"TIE!", 1, (0, 0, 0))
                label2 = self.font.render(f"Exiting in {3 - i}", 1, (0, 0, 0))
                self.window.window.blit(
                    label,
                    (
                        (self.window.width / 2) - (label.get_width() / 2),
                        (self.window.height / 2) - (label.get_height() / 2),
                    ),
                )
                self.window.window.blit(
                    label2,
                    (
                        (self.window.width / 2) - (label2.get_width() / 2),
                        (self.window.height / 2)
                        - (label2.get_height() / 2)
                        + label2.get_height(),
                    ),
                )
                pygame.display.flip()
                time.sleep(1)
                self.window.window.fill((127, 127, 127))

            return True

        return False
