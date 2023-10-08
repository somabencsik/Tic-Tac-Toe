"""Define a game that holds together everything."""
from menu import Menu
from scene_manager import SceneManager
from tic_tac_toe import TicTacToe
from window import Window


class Game:
    def __init__(self) -> None:
        self.window = Window(800, 600, "Tic-Tac-Toe")
        self.scene_manager = SceneManager()
        self.scene_manager.add_scene(Menu("menu", self.window))
        # self.scene_manager.add_scene(TicTacToe("game", self.window))

    def start(self) -> None:
        current_scene = self.scene_manager.get_next_scene()
        current_scene.start()
