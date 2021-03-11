class Pixel:
    def __init__(self, loc, color):
        self.loc = loc
        self.color = color
        self.speed_x = 0
        self.speed_y = -1

    def get_loc(self):
        return self.loc

    def get_color(self):
        return self.color