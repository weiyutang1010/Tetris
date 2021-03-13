class Block:
    def __init__(self):
        self.color = (0, 0, 0)
        self.loc_center = [0, 0]
        self.shape = [[]]
        self.sides = [0, 0, 0, 0]

    def get_color(self):
        return self.color

    def get_shape(self):
        return self.shape

    def get_size(self):
        return self.size

    def get_loc_center(self):
        return self.loc_center

    def get_sides(self):
        return self.sides

    def set_loc_center(self, x, y):
        self.loc_center = [x, y]

class Z_shape(Block):
    def __init__(self):
        self.color = (252,61,50)
        self.loc_center = [0, 0]
        self.shape = [
            (0, 0),
            (0, -1),
            (1, 0),
            (1, 1)
        ]
        self.sides = [0, 1, 1, 1]

class S_shape(Block):
    def __init__(self):
        self.color = (57,255,20)
        self.loc_center = [0, 0]
        self.shape = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, -1)
        ]
        self.sides = [0, 1, 1, 1]

class L_shape(Block):
    def __init__(self):
        self.color = (255,191,0)
        self.loc_center = [0, 0]
        self.shape = [
            (0, 0),
            (-1, 0),
            (1, 0),
            (1, 1)
        ]
        self.sides = [1, 1, 0, 1]

class L_shape_mirror(Block):
    def __init__(self):
        self.color = (173,216,230)
        self.loc_center = [0, 0]
        self.shape = [
            (0, 0),
            (-1, 0),
            (1, 0),
            (1, -1)
        ]
        self.sides = [1, 1, 1, 0]

class T_shape(Block):
    def __init__(self):
        self.color = (255,255,0)
        self.loc_center = [0, 0]
        self.shape = [
            (-1, 0),
            (0, 0),
            (0, -1),
            (0, 1)
        ]
        self.sides = [1, 0, 1, 1]
        
class Square_shape(Block):
    def __init__(self):
        self.color = (139,0,139)
        self.loc_center = [0, 0]
        self.shape = [
            (0, 0),
            (1, 0),
            (0, -1),
            (1, -1)
        ]
        self.sides = [0, 1, 1, 0]

class Line_shape(Block):
    def __init__(self):
        self.color = (0,0,220)
        self.loc_center = [0, 0]
        self.shape = [
            (-1, 0),
            (-2, 0),
            (0, 0),
            (1, 0)
        ]
        self.sides = [2, 1, 0, 0]



