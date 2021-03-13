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
s_block = block.S_shape()
z_block = block.Z_shape()
l_block = block.L_shape()
lm_block = block.L_shape_mirror()
t_block = block.T_shape()
square_block = block.Square_shape()
line_block = block.Line_shape()
gameBoard.place_block(t_block, 7, 4)
gameBoard.place_block(s_block, 3, 2)

# Events
MOVE_DOWN = USEREVENT + 1
my_event = pygame.event.Event(MOVE_DOWN, move_down=gameBoard.move_curr_block)
pygame.time.set_timer(my_event, 400)


run = True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.display.quit()
            pygame.quit()
        elif event.type == MOVE_DOWN:
            event.move_down("DOWN")

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        gameBoard.rotate_curr_block()
    elif keys_pressed[pygame.K_DOWN]:
        gameBoard.move_curr_block("DOWN")
    elif keys_pressed[pygame.K_LEFT]:
        gameBoard.move_curr_block("LEFT")
    elif keys_pressed[pygame.K_RIGHT]:
        gameBoard.move_curr_block("RIGHT")
    elif keys_pressed[pygame.K_ESCAPE]:
        run = False
        pygame.display.quit()
        pygame.quit()

    WIN.fill(WHITE)
    gameBoard.render_all()
    pygame.display.update()


