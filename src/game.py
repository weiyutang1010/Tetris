import pygame
import board
import shape
import random
import time
from copy import deepcopy

class Game():
    """A class used to represent the game

    Attributes
    ----------
        board_size: 1 x 2 int tuple, optional
            the number of cols and rows
        gameBoard: Board object
            the main board of the game
        shapeDisplay: Board object
            side board that shows the current falling shape
        board_mid: 1 x 2 int tuple
            the middle of the board at top row (initial position of new shape)
        curr_shape: int
            represent the index of current falling shape
        shapes: list of shapes
            contains one of every type of shape
        
        last_time: int
            the last time a key is pressed in ns
        interval: int
            the interval between key pressed
        flag: boolean
            if the current shape is at bottom
        bottom_time: int
            the time when the shape reaches the bottom in ns
        bottom_duration: int
            the time that user can move left/right before new shape is placed
    """
    def __init__(self,
                 surface,
                 board_size=(15, 10),
                 block_size=40,
                 board_start=(100,100)
                 ):
        """ 
        Parameters
        ----------
        surface: pygame display object
            the surface of the game
        board_size: 1 x 2 int tuple, optional
            the number of cols and rows
        block_size: int, optional
            the size of each square on the board
        board_start: 1 x 2 int tuple, optional
            starting coordinates of the board
        """
        self.board_size = board_size
        self.gameBoard = board.Board(*board_size, block_size, surface, *board_start)
        self.shapeDisplay = board.Board(8, 8, 30, surface, 560, 100)
        self.board_mid = (1, board_size[1]//2)
        self.curr_shape = None
        self.shapes = [
            shape.S_shape(),
            shape.Z_shape(),
            shape.L_shape(),
            shape.L_shape_mirror(),
            shape.T_shape(),
            shape.Square_shape(),
            shape.Line_shape()
        ]

        # Time and Intervals
        self.last_time = 0
        self.interval = 1.6E8
        self.flag = False
        self.bottom_time = 0
        self.bottom_duration = 3E8

    def display_curr_shape(self):
        """Display the current falling shape"""
        if not self.curr_shape: return
        self.shapeDisplay.reset_curr_shape()
        shape = deepcopy(self.shapes[self.curr_shape])
        self.shapeDisplay.place_shape(
            shape,
            self.shapeDisplay.rows//2-1,
            self.shapeDisplay.cols//2)

    def drop_random_shape(self):
        """Place a random new shape at the top of the board"""
        count = len(self.shapes)
        choice = random.randint(0, count-1)
        self.curr_shape = choice
        pos = (self.shapes[choice].get_sides()[0], self.board_size[1]//2)
        self.gameBoard.place_shape(self.shapes[choice], *pos)
        self.display_curr_shape()

    def shape_movement(self):
        """Move the shape based on key pressed"""
        if time.time_ns() > self.last_time + self.interval:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_UP]:
                self.gameBoard.rotate_curr_shape()
                self.last_time = time.time_ns()
            elif keys_pressed[pygame.K_DOWN] and self.gameBoard.in_bound():
                self.gameBoard.move_curr_shape("DOWN")
                self.last_time = time.time_ns()
            elif keys_pressed[pygame.K_LEFT]:
                self.gameBoard.move_curr_shape("LEFT")
                self.last_time = time.time_ns()
            elif keys_pressed[pygame.K_RIGHT]:
                self.gameBoard.move_curr_shape("RIGHT")
                self.last_time = time.time_ns()
            elif keys_pressed[pygame.K_ESCAPE]:
                return False
        return True
    
    def shape_at_bottom(self):
        """Check if the current shape is at bottom for some amount of time
        
        Return
        ------
            boolean
                True if shape is at the bottom for specified duration. False otherwise.
        """
        if self.gameBoard.at_bottom():
            if self.flag:
                if time.time_ns() > self.bottom_time + self.bottom_duration:
                    self.flag = False
                    return True
            else:
                self.flag = True
                self.bottom_time = time.time_ns()
        return False

    def render_game(self):
        """Render main and display boards"""
        self.shapeDisplay._render_blocks()
        self.gameBoard._render_blocks()

    def quit(self):
        """Exit from game"""
        pygame.display.quit()
        pygame.quit()
        quit()

