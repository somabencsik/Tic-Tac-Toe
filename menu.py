"""Defines a menu for Tic-Tac-Toe game."""
import pygame

from button import Button
from scene import Scene
from tic_tac_toe import TicTacToe


class Menu(Scene):
    def __init__(self, name: str, window: pygame.Surface) -> None:
        super().__init__(name, window)

    def start(self) -> None:
        self.is_running = True

        self._create_menu()

        self.update()

    def update(self) -> None:
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for obj in self.objects:
                        if isinstance(obj, Button):
                            obj.click()

            self.window.window.fill((127, 127, 127))

            super().update()
            self.render()

            pygame.display.flip()

    def render(self) -> None:
        super().render()

    def _create_menu(self) -> None:
        button_new_game = Button(
            self.window.window.get_width() / 2 - 200,
            100,
            400,
            100,
            (69, 69, 69),
            2,
            "New Game",
        )
        button_new_game.callback_function(self._start_game)
        self.add_widget(button_new_game)

        button_open_settings = Button(
            self.window.window.get_width() / 2 - 200,
            250,
            400,
            100,
            (69, 69, 69),
            2,
            "Settings",
        )
        self.add_widget(button_open_settings)

        button_exit = Button(
            self.window.window.get_width() / 2 - 200,
            400,
            400,
            100,
            (69, 69, 69),
            2,
            "Exit",
        )
        button_exit.callback_function(lambda: exit())
        self.add_widget(button_exit)

    def _start_game(self) -> None:
        game = self._create_new_game()
        game.start()

    def _create_new_game(self) -> TicTacToe:
        game = TicTacToe(self.window, 3)  # Later set in the settings
        return game

    def _start_settings(self) -> None:
        """TODO: Create settings"""
