from doctest import FAIL_FAST
from pickle import FALSE
from Snake.settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.title = pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.game_over = False

        self.update
        self.quit

    def update(self):
        pygame.display.flip()

    def quit(self):
        pygame.quit()

