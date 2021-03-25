import pygame
import shape
from copy import deepcopy

class Board:
    """A class used to represent the board

    Attributes
    ----------
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
            board starting x coordinate
        initY: int
            board starting y coordinate
        curr_shape: class Shape
            user control shape
    """
    def __init__(self, rows, cols, size, surface, initX, initY):
        """
            rows: int
                the number of rows
            cols: int
                the number of columns
            size: int
                size of each block on the board
            surface: pygame object
                surface for drawing lines and board
            initX: int
                board starting x coordinate
            initY: int
                board starting y coordinate
        """
        self.rows = rows
        self.cols = cols
        self.size = size
        self.board = [[(0,0,0)] * cols for _ in range(rows)]
        self.surface = surface
        self.initX = initX
        self.initY = initY
        self.curr_shape = shape.Shape()

    def place_shape(self, shape, x, y):
        """Place the center of the shape at (x, y)
        
        Parameters
        ----------
            shape: Shape object
                shape to be placed on the board
            x: int
                x coordinate of the board to place the block
            y: int
                y coordinate of the board to place the block

        Return
        ---------
            boolean
                True if the provided location is already occupied. False otherwise.
        """
        shape.set_loc_center(x, y)
        self.curr_shape = shape
        occupied = False

        # Fill in color of the given shape
        for i, j in shape.get_shape():
            if self.board[x + i][y + j] != (0,0,0):
                occupied = True
                break

        for i,j in shape.get_shape():
            self.board[x + i][y + j] = shape.get_color()
        
        return occupied

    def reset_curr_shape(self):
        """Remove current shape from the board"""
        shape = self.curr_shape
        x, y = shape.get_loc_center()

        # Set color to black
        for i, j in shape.get_shape():
            self.board[x + i][y + j] = (0, 0, 0)

    def _render_blocks(self):
        """Render each blocks"""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                pygame.draw.rect(self.surface, self.board[i][j],
                                 (self.initX+j*self.size, self.initY+i*self.size,
                                   self.size, self.size), 0)

    def _render_grid(self):
        """Render the grid around each blocks"""
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
        """Convert direction to i, j indexes
    
        Parameters
        -----------
            command: str, optional
                takes in "UP", "DOWN", "LEFT", "RIGHT" (default check 
                current position)

        Returns
        --------
            1 x 2 tuple
                return corresponding coordinates of the command
        """
        if command == "UP":
            return (-1, 0)
        elif command == "DOWN":
            return (1, 0)
        elif command == "LEFT":
            return (0, -1)
        elif command == "RIGHT":
            return (0, 1)
        else:
            return (0, 0)

    def in_bound(self, shape, command=""):
        """Check if moving in the direction causes out of bound

        Parameters
        -----------
            shape: class Shape()
                The shape block to be checked

            command: str, optional
                takes in "UP", "DOWN", "LEFT", "RIGHT" (default check 
                current position)

        Return
        --------
            boolean
                True if moving in given direction does not cause out of bound
                False otherwise
        """
        i, j = self.get_direction(command)
        x, y = shape.get_loc_center()
        up, down, left, right = shape.get_sides() 
        return  (x - up + i >= 0 and 
                x + down + i < self.rows and 
                y - left + j >= 0 and 
                y + right + j < self.cols)

    def not_blocked(self, shape, command=""):
        """ Check if the current shape is blocked by another 
            shape in the specified direction

        Parameters
        -----------
            command: str, optional
                takes in "UP", "DOWN", "LEFT", "RIGHT" (default check 
                current position)
        
        Return
        -----------
            boolean
                True if the shape is not blocked by another shape.
                False otherwise.
        """
        BLACK = (0, 0, 0)

        i, j = self.get_direction(command)
        x, y = shape.get_loc_center()

        # Find all coordinates of the current shape
        coordinates = {}
        if command != "":
            for a, b in shape.get_shape():
                coordinates[(x + a, y + b)] = 1

        for a, b in shape.get_shape():
            if (x + a + i, y + j + b) in coordinates:
                # skip if the coordinate is part of current shape
                continue
            elif  self.board[x + a + i][y + j + b] != BLACK:
                return False
        return True

    def move_curr_shape(self, command):
        """Move current shape to the provided direction

        Parameters
        -----------
            command: str
                takes in "UP", "DOWN", "LEFT", "RIGHT"
        """
        shape = self.curr_shape
        i, j = self.get_direction(command)
        x, y = self.curr_shape.get_loc_center()

        if (self.in_bound(shape, command) and self.not_blocked(shape, command)):
            self.reset_curr_shape() # Remove current shape
            self.curr_shape.set_loc_center(x + i, y + j) # Update center location
            self.place_shape(shape, x + i, y + j) # Render new shape

    def at_bottom(self):
        """Check if the shape can still move bottom"""
        return (not self.in_bound(self.curr_shape, "DOWN") or 
                not self.not_blocked(self.curr_shape, "DOWN"))

    def shift_horizontal(self, shape):
        """Shift the block horizontally to avoid out of bound"""
        x, y = shape.get_loc_center()
        if not self.in_bound(shape, "LEFT"):
            y = shape.get_sides()[2]
        elif not self.in_bound(shape, "RIGHT"):
            y = self.cols - shape.get_sides()[3] - 1
        return (x, y)

    def not_blocked_2(self, shape, shape2, command=""):
        BLACK = (0, 0, 0)

        i, j = self.get_direction(command)
        x, y = shape.get_loc_center()

        # Find all coordinates of the current shape
        coordinates = {}
        x2, y2 = shape2.get_loc_center()
        for a, b in shape2.get_shape():
            coordinates[(x2 + a, y2 + b)] = 1

        for a, b in shape.get_shape():
            if (x + a + i, y + j + b) in coordinates:
                # skip if the coordinate is part of current shape
                continue
            elif  self.board[x + a + i][y + j + b] != BLACK:
                return False
        return True

    def rotate_curr_shape(self):
        """Rotate current shape 90 deg clockwise"""
        x, y = self.curr_shape.get_loc_center()
        shape = deepcopy(self.curr_shape)

        # Stop rotation if the rotated shape collide with another shape
        shape.rotate()
        shape.set_loc_center(*self.shift_horizontal(shape))
        if not self.not_blocked_2(shape, self.curr_shape):
            return

        self.reset_curr_shape()
        self.curr_shape.rotate()

        # To avoid out of bound, shape will be shifted left or right
        new_x, new_y = self.shift_horizontal(self.curr_shape)
        self.curr_shape.set_loc_center(new_x, new_y)
        self.place_shape(self.curr_shape, new_x, new_y)

    def is_row_full(self, row):
        """Check if the row is full

        Parameters
        ----------
            row: int
                the index of the row

        Returns
        ----------
            boolean
                True if row is full. False otherwise.
        """
        BLACK = (0, 0, 0)

        for color in self.board[row]:
            if color == BLACK:
                return False
        return True

    def render_row_black(self, row):
        """Render the row of the board black

        Parameters
        ----------
            row: int
                the index of the row
        """
        BLACK = (0, 0, 0)

        for col in range(len(self.board[row])):
            self.board[row][col] = BLACK

    def shift_down(self, start_index):
        """Shift all color blocks above the index down by 1 block"""
        BLACK = (0, 0, 0)

        for i in range(start_index, 0, -1):
            for j in range(0, self.cols):
                if self.board[i][j] != BLACK:
                    self.board[i + 1][j] = self.board[i][j]
                    self.board[i][j] = BLACK
        return

    def lose_game(self):
        col_filled = [True] * len(self.board[0])

        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if col_filled[col]: col_filled[col] = (self.board[row][col] != (0,0,0))

        for col in col_filled:
            if col: return True
        return False
