import pygame
import board
import block
import random

class Game():
    def __init__(self,
                 surface,
                 board_size=(15, 10),
                 block_size=40,
                 board_start=(140,100)
                 ):
        self.board_size = board_size
        self.gameBoard = board.Board(*board_size, block_size, surface, *board_start)
        self.board_mid = (1, board_size[1]//2)
        self.blocks = [
            block.S_shape(),
            block.Z_shape(),
            block.L_shape(),
            block.L_shape_mirror(),
            block.T_shape(),
            block.Square_shape(),
            block.Line_shape()
        ]

    def drop_random_blocks(self):
        count = len(self.blocks)
        choice = random.randint(0, count-1)
        pos = (self.blocks[choice].get_sides()[0], self.board_size[1]//2)
        self.gameBoard.place_block(self.blocks[choice], *pos)

    def block_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            self.gameBoard.rotate_curr_block()
        elif keys_pressed[pygame.K_DOWN]:
            self.gameBoard.move_curr_block("DOWN")
        elif keys_pressed[pygame.K_LEFT]:
            self.gameBoard.move_curr_block("LEFT")
        elif keys_pressed[pygame.K_RIGHT]:
            self.gameBoard.move_curr_block("RIGHT")
        elif keys_pressed[pygame.K_ESCAPE]:
            return False
        return True

    def render_game(self):
        self.gameBoard.render_all()

