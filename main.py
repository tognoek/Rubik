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
        self.running = True
        self.screen = screen
        self.clock = clock
        self.rubik.update(True)

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.clock.tick(120)
            self.rubik.render(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        self.rubik.update()
                        
            pygame.display.update()



if __name__ == "__main__":
    game = game(screen=screen, clock=clock)
    game.run()

pygame.quit()
sys.exit()