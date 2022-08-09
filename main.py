from pickle import TRUE
from Snake.game import *
from Snake.objects import *

game = Game()

while not game.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over = True
    
    game.clock.tick(60)

game.quit()