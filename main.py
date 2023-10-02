from window import Window
from game import Game

def main():
    window = Window(800, 600, "Tic-Tac-Toe")
    game = Game(window, 3)
    game.start()

if __name__ == "__main__":
    main()
