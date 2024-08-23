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
        self.rubik = Rubik(screen)
        self.running = True
        self.screen = screen
        self.clock = clock
        self.rubik.start()

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.clock.tick(40)
            self.rubik.runLoop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_x]:
                    self.rubik.controlRotation((1, 0, 0))
                if keys[pygame.K_y]:
                    self.rubik.controlRotation((0, 1, 0))
                if keys[pygame.K_z]:
                    self.rubik.controlRotation((0, 0, 1))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_d:
                        self.rubik.addRotation('D')
                    elif event.key == pygame.K_f:
                        self.rubik.addRotation('F')
                    elif event.key == pygame.K_b:
                        self.rubik.addRotation('B')
                    elif event.key == pygame.K_l:
                        self.rubik.addRotation('L')
                    elif event.key == pygame.K_r:
                        self.rubik.addRotation('R')
                    elif event.key == pygame.K_u:
                        self.rubik.addRotation('U')
                    if event.key == pygame.K_s:
                        print("Write Datas")
                        self.rubik.write()
                        
            pygame.display.update()



if __name__ == "__main__":
    game = game(screen=screen, clock=clock)
    game.run()

pygame.quit()
sys.exit()