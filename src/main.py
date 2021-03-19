import pygame
import os
from pygame.constants import USEREVENT
import board
import block
import game

# Color Constant
WHITE = (255, 255, 255)

# Pygame Window
pygame.init()
WIDTH, HEIGHT = 880, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris!")

# Pygame FPS
clock = pygame.time.Clock()
FPS = 24

# Initialize Board
myGame = game.Game(surface=WIN)

# Events
MOVE_DOWN = USEREVENT + 1
pygame.time.set_timer(MOVE_DOWN, 350)


run = True
myGame.drop_random_blocks()
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            myGame.quit()
        elif event.type == MOVE_DOWN:
            myGame.gameBoard.move_curr_block("DOWN")
    
    if (myGame.gameBoard.at_bottom()):
        myGame.drop_random_blocks()
    else:
        run = myGame.block_movement()
    
    WIN.fill(WHITE)
    myGame.render_game()
    pygame.display.update()

myGame.quit()
