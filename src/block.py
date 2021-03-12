class Block:
    def __init__(self):
        self.color = (0, 0, 0)
        self.loc_center = [0, 0]
        self.shape = [[]]

    def get_color(self):
        return self.color

    def get_shape(self):
        return self.shape

    def get_size(self):
        return self.size

    def get_loc_center(self):
        return self.loc_center

    def set_loc_center(self, x, y):
        self.loc_center = [x, y]

class Z_shape(Block):
    def __init__(self):
        self.color = (50,205,50)
        self.loc_center = [0, 0]
        self.shape = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, -1)
        ]

