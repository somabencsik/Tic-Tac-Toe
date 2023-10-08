"""Define button widget for game."""
import pygame

from widget import Widget


class Button(Widget):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        color: tuple,
        border: int,
        title: str,
    ) -> None:
        super().__init__(x, y, width, height)
        self.color = color
        self.border = border
        self.title = title
        pygame.font.init()
        self.font = pygame.font.SysFont("monospace", 50)
        self.is_hover = False
        self.callback = None

    def update(self) -> None:
        self.is_hover = self._check_mouse_hover()

    def render(self, window: pygame.Surface) -> None:
        color = list(self.color[:])
        if self.is_hover:
            color[0] += 20
            color[1] += 20
            color[2] += 20

        pygame.draw.rect(
            window,
            color,
            (self.x, self.y, self.width, self.height),
            width=0,
        )
        pygame.draw.rect(
            window,
            (0, 0, 0),
            (self.x, self.y, self.width, self.height),
            width=self.border,
        )
        button_label = self.font.render(self.title, 1, (0, 0, 0))
        window.blit(
            button_label,
            (
                (self.x + self.width / 2) - (button_label.get_width() / 2),
                (self.y + self.height / 2) - (button_label.get_height() / 2),
            ),
        )

    def _check_mouse_hover(self) -> bool:
        """Check when the mouse hovers over the button."""
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if (
            mouse_x > self.x
            and mouse_x < self.x + self.width
            and mouse_y > self.y
            and mouse_y < self.y + self.height
        ):
            return True
        return False

    def click(self) -> None:
        if not self.is_hover:
            return
        if self.callback is not None:
            self.callback()

    def callback_function(self, func: callable) -> None:
        self.callback = func
