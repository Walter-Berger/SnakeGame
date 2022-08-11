from Snake.settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.title = pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.game_over = False

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
            
            self.clock.tick(60)

    def update(self):
        pygame.display.flip()

    def quit(self):
        pygame.quit()

