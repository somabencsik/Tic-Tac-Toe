"""Define a scene in a game."""
from abc import ABC, abstractmethod

import pygame


class Scene(ABC):
    """Define a base scene for game."""

    def __init__(self, name: str, window: pygame.Surface) -> None:
        self.name = name
        self.window = window
        self.is_running = False
        self.objects: list["Widget"] = []

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def update(self) -> None:
        for obj in self.objects:
            obj.update()

    @abstractmethod
    def render(self) -> None:
        for obj in self.objects:
            obj.render(self.window.window)

    def add_widget(self, w) -> None:
        self.objects.append(w)
