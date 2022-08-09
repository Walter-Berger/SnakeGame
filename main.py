import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()