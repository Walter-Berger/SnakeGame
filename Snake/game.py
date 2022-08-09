from Snake.settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = SCREEN
        self.title = TITLE
        self.clock = pygame.time.Clock()
        self.run = True

    def update(self):
        pygame.display.flip()

    def quit(self):
        pygame.quit()