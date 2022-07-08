import pygame
import configs


class PlaneGame:

    def __init__(self):
        pygame.init()  # initialize the game

        # set the window of game
        self.screen = pygame.display.set_mode((configs.Config.SCREEN_WIDTH, configs.Config.SCREEN_HEIGHT))

        # game title
        pygame.display.set_caption(configs.Config.TITLE)




if __name__ == '__main__':
    # create object
    game = PlaneGame()
    game.start_game()
