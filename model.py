import random
from helpers import helpers


class MinesweeperBoard(object):
    size_x = None
    size_y = None
    mines = None
    mines_structure = None
    view_structure = None

    def __init__(self, x, y, mines):
        self.size_x = x
        self.size_y = y
        self.mines = mines
        self.mines_structure = [[0] * x for i in range(y)]
        for row in range(x):
            for col in range(y):
                self.mines_structure[row][col] = 0

        self.view_structure = [[False] * x for i in range(y)]
        for row in range(x):
            for col in range(y):
                self.view_structure[row][col] = False

    def load(self):
        for i in range(0, self.mines):
            mine = True
            while mine:
                row_mine = random.randrange(0, self.size_x)
                col_mine = random.randrange(0, self.size_y)
                mine = self.mines_structure[row_mine][col_mine] == 9
            self.mines_structure[row_mine][col_mine] = 9
            for row2 in range(helpers.get_max(0, row_mine - 1), helpers.get_min(self.size_x -1 , row_mine + 1) + 1):
                for col2 in range(helpers.get_max(0, col_mine - 1), helpers.get_min(self.size_y - 1, col_mine + 1) + 1):
                    if self.mines_structure[row2][col2] != 9:
                        self.mines_structure[row2][col2] = self.mines_structure[row2][col2]+1

