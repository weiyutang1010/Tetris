import pygame
import os
import board

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 680, 920
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris!")

FPS = 60

def main():
    gameBoard = board.Board(15, 10, 40, WIN, 140, 100)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        WIN.fill(WHITE)
        gameBoard.render_all()
        pygame.display.update()

if __name__ == '__main__':
    main()

