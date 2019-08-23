import random
from helpers import helpers
import uuid

class Minesweeper(object):
    id = None
    mines_structure = None
    view_structure = None

    def __init__(self, id, mines, view):
        self.id = id
        self.mines_structure = mines
        self.view_structure = view

    @staticmethod
    def create(board):
        minesweeper_id = uuid.uuid4()
        minesweeper = Minesweeper(minesweeper_id, MinesStructure(minesweeper_id, None, board.get_mines_board()), ViewStructure(minesweeper_id, 0, board.get_view_board()))

        # save instances DB
        return minesweeper

    @staticmethod
    def get_minesweeper(id):
        minesweeper = Minesweeper()

        minesweeper.id = id
        #minesweeper.mines_structure = DB.get_mines_structure(id)
        #minesweeper.view_structure = DB.get_view_structure(id)

        return minesweeper

    def turn(self, cell):
        if cell.is_valid_cell(self.mines_structure):
            # turn cell - inc count
            # if cell == 9 -> set mines_structure.win = false
            # elif 0 - turn N cells / inc count
            # add turned cells in tunerd cells[(1,2),(4,5)]
            # set inc count in view structure - save db

            # if view_structure.game winned -> mines_structure.win = True - save db

            # return turned cells
            pass

        raise Exception

    def game_wined(self):
        return self.mines_structure.game_wined()

class MinesweeperBoard(object):
    size_x = None
    size_y = None
    mines = None
    mines_board = None
    view_board = None

    def __init__(self, x, y, mines):
        self.size_x = x
        self.size_y = y
        self.mines = mines
        self.mines_board = [[0] * x for i in range(y)]
        for row in range(x):
            for col in range(y):
                self.mines_board[row][col] = 0

        self.view_board = [[False] * x for i in range(y)]
        for row in range(x):
            for col in range(y):
                self.view_board[row][col] = False

    def get_mines_board(self):
        return self.mines_board

    def get_view_board(self):
        return self.view_board

    def load(self):
        for i in range(0, self.mines):
            mine = True
            while mine:
                row_mine = random.randrange(0, self.size_x)
                col_mine = random.randrange(0, self.size_y)
                mine = self.mines_board[row_mine][col_mine] == 9
            self.mines_board[row_mine][col_mine] = 9
            for row2 in range(helpers.get_max(0, row_mine - 1), helpers.get_min(self.size_x -1 , row_mine + 1) + 1):
                for col2 in range(helpers.get_max(0, col_mine - 1), helpers.get_min(self.size_y - 1, col_mine + 1) + 1):
                    if self.mines_board[row2][col2] != 9:
                        self.mines_board[row2][col2] = self.mines_board[row2][col2]+1


class MinesweeperCell(object):
    pos_y = None
    pos_x = None

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def is_valid_cell(self, structure):
        if self.pos_x < structure.get_sizex_board() and self.pos_y < structure.get_sizey_board():
            return True

        return False

class MinesStructure(object):
    id = None
    win = None
    board = None

    def __init__(self, id, win, board):
        self.id = id
        self.win = win
        self.board = board

    def game_wined(self):
        return self.win

class ViewStructure(object):
    id = None
    count_viewed = None
    board = None

    def __init__(self, id, count_viewed, board):
        self.id = id
        self.count_viewed = count_viewed
        self.board = board

    def get_sizex_board(self):
        return len(self.board[0])

    def get_sizey_board(self):
        return len(self.board)

    def game_wined(self):
        return self.count_viewed == len(self.board) * len(self.board[0])


class TurnCellResponse(object):
    turned_cells = None
    wined = None
    lose = None

    def __init__(self, turned_cells, wined, lose):
        self.turned_cells = turned_cells
        self.wined = wined
        self.lose = lose
