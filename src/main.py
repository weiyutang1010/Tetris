import pygame
import os
import board
import block

pygame.init()

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 680, 920
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris!")

FPS = 12

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

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        gameBoard.move_curr_block(0, -1)
    elif keys_pressed[pygame.K_RIGHT]:
        gameBoard.move_curr_block(0, 1)
    elif keys_pressed[pygame.K_DOWN]:
        gameBoard.move_curr_block(1, 0)
    elif keys_pressed[pygame.K_UP]:
        gameBoard.move_curr_block(-1, 0)

    WIN.fill(WHITE)
    gameBoard.render_all()
    pygame.display.update()


