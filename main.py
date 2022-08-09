from Game import *

game = Game()

while game.run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.run = False
    
    game.clock.tick(60)

game.quit()