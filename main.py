from Game import *

run = True
game = Game()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    game.clock.tick(60)

game.quit()