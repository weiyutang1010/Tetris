import pygame
import board
import block
import random
import time
from copy import deepcopy

class Game():
    def __init__(self,
                 surface,
                 board_size=(15, 10),
                 block_size=40,
                 board_start=(100,100)
                 ):
        self.board_size = board_size
        self.gameBoard = board.Board(*board_size, block_size, surface, *board_start)
        self.blockDisplay = board.Board(8, 8, 30, surface, 560, 100)
        self.board_mid = (1, board_size[1]//2)
        self.cur_block = None
        self.blocks = [
            block.S_shape(),
            block.Z_shape(),
            block.L_shape(),
            block.L_shape_mirror(),
            block.T_shape(),
            block.Square_shape(),
            block.Line_shape()
        ]
        self.last_time = 0
        self.interval = 1.6E8

    def display_cur_block(self):
        if not self.cur_block: return
        self.blockDisplay.reset_curr_block()
        block = deepcopy(self.blocks[self.cur_block])
        self.blockDisplay.place_block(
            block,
            self.blockDisplay.rows//2-1,
            self.blockDisplay.cols//2)

    def drop_random_blocks(self):
        count = len(self.blocks)
        choice = random.randint(0, count-1)
        self.cur_block = choice
        pos = (self.blocks[choice].get_sides()[0], self.board_size[1]//2)
        self.gameBoard.place_block(self.blocks[choice], *pos)
        self.display_cur_block()

    def block_movement(self):
        if time.time_ns() > self.last_time + self.interval:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_UP]:
                self.gameBoard.rotate_curr_block()
                self.last_time = time.time_ns()
            elif keys_pressed[pygame.K_DOWN]:
                self.gameBoard.move_curr_block("DOWN")
                self.last_time = time.time_ns()
            elif keys_pressed[pygame.K_LEFT]:
                self.gameBoard.move_curr_block("LEFT")
                self.last_time = time.time_ns()
            elif keys_pressed[pygame.K_RIGHT]:
                self.gameBoard.move_curr_block("RIGHT")
                self.last_time = time.time_ns()
            elif keys_pressed[pygame.K_ESCAPE]:
                return False
        return True

    def render_game(self):
        self.blockDisplay._render_blocks()
        self.gameBoard._render_blocks()

    def quit(self):
        pygame.display.quit()
        pygame.quit()
        quit()

