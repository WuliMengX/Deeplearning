import pygame
from configs import Config
import sys


class PlaneGame:

    def __init__(self):
        pygame.init()  # initialize the game

        # set the window of game
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

        # set game title
        pygame.display.set_caption(Config.TITLE)

    def start_game(self):
        print("游戏开始")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == '__main__':
    # create object
    game = PlaneGame()
    game.start_game()
