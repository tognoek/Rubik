import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
    screen.fill((0, 0, 0))
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    pygame.display.update()

pygame.quit()
sys.exit()