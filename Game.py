import pygame, sys
pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.run = True

    def update():
        pygame.display.flip()

    def quit():
        pygame.quit()
        sys.exit()