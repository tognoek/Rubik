import pygame
import sys
from rubik import Rubik

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

class game:
    def __init__(self, screen : pygame.Surface, clock : pygame.time.Clock):
        self.rubik = Rubik()
        self.angles = {'X' : 0, 'Y' : 0, 'Z' : 0}
        self.running = True
        self.screen = screen
        self.clock = clock
        self.update = {'X' : False, 'Y' : False, 'Z' : False}
        self.vector = {'X' : 1, 'Y' : 1, 'Z' : 1}

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.clock.tick(120)
            self.rubik.update(self.angles)
            self.rubik.render(self.screen)
            for i in self.update:
                if self.update[i]:
                    self.angles[i] += self.vector[i]
                    if self.angles[i] >= 360:
                        self.angles[i] = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_x]:
                        self.update['X'] = True
                        self.vector['X'] = 1
                if keys[pygame.K_y]:
                        self.update['Y'] = True
                        self.vector['Y'] = 1
                if keys[pygame.K_z]:
                        self.update['Z'] = True
                        self.vector['Z'] = 1

                if keys[pygame.K_SPACE] and keys[pygame.K_x]:
                        self.update['X'] = True
                        self.vector['X'] = -1
                if keys[pygame.K_SPACE] and keys[pygame.K_y]:
                        self.update['Y'] = True
                        self.vector['Y'] = -1
                if keys[pygame.K_SPACE] and keys[pygame.K_z]:
                        self.update['Z'] = True
                        self.vector['Z'] = -1


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_x:
                        self.update['X'] = False
                    if event.key == pygame.K_y:
                        self.update['Y'] = False
                    if event.key == pygame.K_z:
                        self.update['Z'] = False
            pygame.display.update()



if __name__ == "__main__":
    game = game(screen=screen, clock=clock)
    game.run()

pygame.quit()
sys.exit()