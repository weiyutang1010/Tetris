import pygame
import shape

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
        """Place the center of the shape at (x, y)"""
        shape.set_loc_center(x, y)
        self.curr_shape = shape

        # Fill in color of the given shape
        for i, j in shape.get_shape():
            self.board[x + i][y + j] = shape.get_color()

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

    def in_bound(self, command=""):
        """Check if moving in the direction causes out of bound

        Parameters
        -----------
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
        x, y = self.curr_shape.get_loc_center()
        up, down, left, right = self.curr_shape.get_sides() 
        return  (x - up + i >= 0 and 
                x + down + i < self.rows and 
                y - left + j >= 0 and 
                y + right + j < self.cols)

    def not_blocked(self, command):
        """ Check if the current shape is blocked by another 
            shape in the specified direction

        Parameters
        -----------
            command: str
                takes in "UP", "DOWN", "LEFT", "RIGHT"
        
        Return
        -----------
            boolean
                True if the shape is not blocked by another shape.
                False otherwise.
        """
        BLACK = (0, 0, 0)

        shape = self.curr_shape
        i, j = self.get_direction(command)
        x, y = shape.get_loc_center()

        # Find all coordinates of the current shape
        coordinates = {}
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

        if (self.in_bound(command) and self.not_blocked(command)):
            self.reset_curr_shape() # Remove current shape
            self.curr_shape.set_loc_center(x + i, y + j) # Update center location
            self.place_shape(shape, x + i, y + j) # Render new shape

    def at_bottom(self):
        """Check if the shape can still move bottom"""
        return not self.in_bound("DOWN") or not self.not_blocked("DOWN")

    def rotate_curr_shape(self):
        """Rotate current shape 90 deg clockwise"""
        x, y = self.curr_shape.get_loc_center()

        self.reset_curr_shape()
        self.curr_shape.rotate()

        # To avoid out of bound, shape will be shifted left or right
        if not self.in_bound("LEFT"):
            y = self.curr_shape.get_sides()[2]
        elif not self.in_bound("RIGHT"):
            y = self.cols - self.curr_shape.get_sides()[3] - 1

        self.place_shape(self.curr_shape, x, y)

