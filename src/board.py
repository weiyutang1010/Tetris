import pygame
import block

class Board:
    def __init__(self, rows, cols, size, surface, initX, initY):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.board = [[(0,0,0)] * cols for _ in range(rows)]
        self.surface = surface
        self.initX = initX
        self.initY = initY
        self.curr_block = block.Block()
        self.blocks = []

    def place_block(self, block, x, y):
        block.set_loc_center(x, y)
        self.blocks.append(block)
        self.curr_block = block
        for i, j in block.get_shape():
            self.board[x + i][y + j] = block.get_color()

    def reset_block(self):
        block = self.curr_block
        x, y = block.get_loc_center()
        for i, j in block.get_shape():
            self.board[x + i][y + j] = (0, 0, 0)

    def _render_blocks(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                pygame.draw.rect(self.surface, self.board[i][j],
                                 (self.initX+j*self.size, self.initY+i*self.size,
                                   self.size, self.size), 0)

    def _render_grid(self):
        for i in range(len(self.board)):
            pygame.draw.line(self.surface, (255,255,255), (self.initX, self.initY+i*self.size),
                             (self.initX+self.cols*self.size, self.initY+i*self.size))
            for j in range(len(self.board[0])):
                pygame.draw.line(self.surface, (255,255,255), (self.initX+j*self.size, self.initY),
                                 (self.initX+j*self.size, self.initY+self.rows*self.size))

    def render_all(self):
        self._render_blocks()
        self._render_grid()

    def move_curr_block(self, i, j):
        block = self.curr_block
        x, y = self.curr_block.get_loc_center()

        if x + i >= 0 and x + i < self.rows and y + j >= 0 and y + j < self.cols:
            self.reset_block()
            self.curr_block.set_loc_center(x + i, y + j)
            self.place_block(block, x + i, y + j)

