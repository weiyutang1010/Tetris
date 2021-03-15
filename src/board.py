import pygame
import block

class Board:
    def __init__(self, rows, cols, size, surface, initX, initY):
        """
            rows: int
                the number of rows
            cols: int
                the number of columns
            size: int
                size of each block
            board: 2d list of tuple
                board[i][j] contains the color of the board
            surface: pygame object
                surface for drawing lines and board
            initX: int
                ?
            initY: int
                ?
            curr_block: class Block
                user control block
        """
        self.rows = rows
        self.cols = cols
        self.size = size
        self.board = [[(0,0,0)] * cols for _ in range(rows)]
        self.surface = surface
        self.initX = initX
        self.initY = initY
        self.curr_block = block.Block()

    def place_block(self, block, x, y):
        """Place the center of the block at (x, y)"""
        block.set_loc_center(x, y)
        self.curr_block = block

        # Fill in color of the given block
        for i, j in block.get_shape():
            self.board[x + i][y + j] = block.get_color()

    def reset_curr_block(self):
        """Remove current block from the board"""
        block = self.curr_block
        x, y = block.get_loc_center()

        # Set color to black
        for i, j in block.get_shape():
            self.board[x + i][y + j] = (0, 0, 0)

    def _render_blocks(self):
        """???"""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                pygame.draw.rect(self.surface, self.board[i][j],
                                 (self.initX+j*self.size, self.initY+i*self.size,
                                   self.size, self.size), 0)

    def _render_grid(self):
        """???"""
        for i in range(len(self.board)):
            pygame.draw.line(self.surface, (255,255,255), (self.initX, self.initY+i*self.size),
                             (self.initX+self.cols*self.size, self.initY+i*self.size))
            for j in range(len(self.board[0])):
                pygame.draw.line(self.surface, (255,255,255), (self.initX+j*self.size, self.initY),
                                 (self.initX+j*self.size, self.initY+self.rows*self.size))

    def render_all(self):
        """Render board's grid and block"""
        self._render_blocks()
        self._render_grid()

    def get_direction(self, command):
        """Convert direction to i, j indexes"""
        if command == "UP":
            return (-1, 0)
        elif command == "DOWN":
            return (1, 0)
        elif command == "LEFT":
            return (0, -1)
        elif command == "RIGHT":
            return (0, 1)

    def in_bound(self, command):
        i, j = self.get_direction(command)
        x, y = self.curr_block.get_loc_center()
        up, down, left, right = self.curr_block.get_sides() 
        return  (x - up + i >= 0 and 
                x + down + i < self.rows and 
                y - left + j >= 0 and 
                y + right + j < self.cols)

    def not_blocked(self, command):
        i, j = self.get_direction(command)
        x, y = self.curr_block.get_loc_center()
        up, down, left, right = self.curr_block.get_sides()

        return True

    def move_curr_block(self, command):
        """
        Move current block to the provided direction
        --------
            command: str
                takes in "UP", "DOWN", "LEFT", "RIGHT"
        """
        block = self.curr_block
        i, j = self.get_direction(command)
        x, y = self.curr_block.get_loc_center()

        if (self.in_bound(command) and self.not_blocked(command)):
            self.reset_curr_block() # Remove current block
            self.curr_block.set_loc_center(x + i, y + j) # Update center location
            self.place_block(block, x + i, y + j) # Render new block

    def at_bottom(self):
        i, j = self.get_direction("DOWN")
        x, y = self.curr_block.get_loc_center()
        up, down, left, right = self.curr_block.get_sides() 
        return  x + down + i == self.rows

    def rotate_curr_block(self):
        block = self.curr_block
        x, y = self.curr_block.get_loc_center()

        self.reset_curr_block()
        block.rotate()
        self.place_block(block, x, y)

