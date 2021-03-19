class Shape:
    """A class used to represent the shape

    Attributes
    ----------
        color: 1 x 3 int tuple
            RGB values of the shape
        loc_center: 1 x 2 int tuple
            x, y coordinates of the center of the shape
        shape: list of 1 x 2 tuples
            coordinate from center to that is still part of the shape
    """
    def __init__(self):
        self.color = (0, 0, 0)
        self.loc_center = (0, 0)
        self.shape = []

    def get_color(self):
        return self.color

    def get_shape(self):
        return self.shape

    def get_loc_center(self):
        return self.loc_center

    def get_sides(self):
        """return the length from the center"""
        sides = [0, 0, 0, 0] # Up, Down, Left, Right
        for i, j in self.get_shape():
            if i < 0:
                sides[0] = max(sides[0], i * -1)
            elif i > 0:
                sides[1] = max(sides[1], i)

            if j < 0:
                sides[2] = max(sides[2], j * -1)
            elif j > 0:
                sides[3] = max(sides[3], j)
        return sides

    def set_loc_center(self, x, y):
        self.loc_center = [x, y]

    def rotate(self):
        # Update shape
        for i, coor in enumerate(self.shape):
            y, x = coor
            y *= -1
            self.shape[i] = (x, y)


class Z_shape(Shape):
    def __init__(self):
        self.color = (252,61,50)
        self.loc_center = (0, 0)
        self.shape = [
            (0, 0),
            (0, -1),
            (1, 0),
            (1, 1)
        ]

class S_shape(Shape):
    def __init__(self):
        self.color = (57,255,20)
        self.loc_center = (0, 0)
        self.shape = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, -1)
        ]
        
class L_shape(Shape):
    def __init__(self):
        self.color = (255,191,0)
        self.loc_center = (0, 0)
        self.shape = [
            (0, 0),
            (-1, 0),
            (1, 0),
            (1, 1)
        ]

class L_shape_mirror(Shape):
    def __init__(self):
        self.color = (173,216,230)
        self.loc_center = (0, 0)
        self.shape = [
            (0, 0),
            (-1, 0),
            (1, 0),
            (1, -1)
        ]

class T_shape(Shape):
    def __init__(self):
        self.color = (255,255,0)
        self.loc_center = (0, 0)
        self.shape = [
            (-1, 0),
            (0, 0),
            (0, -1),
            (0, 1)
        ]
        
class Square_shape(Shape):
    def __init__(self):
        self.color = (139,0,139)
        self.loc_center = (0, 0)
        self.shape = [
            (0, 0),
            (1, 0),
            (0, -1),
            (1, -1)
        ]
    def rotate(self):
        return

class Line_shape(Shape):
    def __init__(self):
        self.color = (0,0,220)
        self.loc_center = (0, 0)
        self.shape = [
            (-1, 0),
            (-2, 0),
            (0, 0),
            (1, 0)
        ]



