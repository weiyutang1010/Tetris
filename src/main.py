import pygame
import os

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 1080, 920
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris!")

FPS = 60

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        WIN.fill(WHITE)
        pygame.display.update()

if __name__ == '__main__':
    main()

