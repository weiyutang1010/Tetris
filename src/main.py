import pygame
import os
from pygame.constants import USEREVENT
import game
import time

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
pygame.time.set_timer(MOVE_DOWN, 500)


run = True
myGame.drop_random_shape()
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            myGame.quit()
        elif event.type == MOVE_DOWN:
            myGame.gameBoard.move_curr_shape("DOWN")
    
    if myGame.shape_at_bottom():
        myGame.remove_full_lines()
        # user lose when new shape is occupied
        run = not myGame.drop_random_shape()
    else:
        run = myGame.shape_movement()
    
    WIN.fill(WHITE)
    myGame.render_game()
    pygame.display.update()

# pause for 2 second before quit
time.sleep(2)
myGame.quit()
