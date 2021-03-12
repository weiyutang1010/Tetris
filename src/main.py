import pygame
import os
import board
import block

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 680, 920
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris!")

FPS = 60

gameBoard = board.Board(15, 10, 40, WIN, 140, 100)
someBlock = block.Z_shape()
gameBoard.place_block(someBlock, 5, 5)


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


