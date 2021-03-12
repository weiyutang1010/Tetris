import pygame
import os
from pygame.constants import USEREVENT
import board
import block

# Color Constant
WHITE = (255, 255, 255)

# Pygame Window
pygame.init()
WIDTH, HEIGHT = 680, 920
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris!")

# Pygame FPS
clock = pygame.time.Clock()
FPS = 12

# Initialize Board
gameBoard = board.Board(15, 10, 40, WIN, 140, 100)
someBlock = block.Z_shape()
gameBoard.place_block(someBlock, 5, 5)

# Events
MOVE_DOWN = USEREVENT + 1
my_event = pygame.event.Event(MOVE_DOWN, move_down=gameBoard.move_curr_block_down)
pygame.time.set_timer(my_event, 400)


run = True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == MOVE_DOWN:
            event.move_down()

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


