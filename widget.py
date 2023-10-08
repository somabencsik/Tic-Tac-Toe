"""Define a widget."""
from abc import ABC, abstractmethod


class Widget(ABC):
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @abstractmethod
    def update(self) -> None:
        ...

    @abstractmethod
    def render(self) -> None:
        ...
