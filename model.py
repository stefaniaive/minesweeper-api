
class Minesweeper(object):
    size_x = None
    size_y = None
    mines = None

    def __init__(self, x, y, mines):
        self.mines = mines
        self.size_x = x
        self.size_y = y
        self.mines = mines

