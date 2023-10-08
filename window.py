"""Creates game window."""

import pygame


class Window:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
