import random
from tools.helpers import helpers
import uuid
from redis_cli.client import redis_mines_structure, redis_view_structure
import pickle
from werkzeug.exceptions import NotFound

class Minesweeper(object):
    id = None
    mines_structure = None
    view_structure = None

    def __init__(self, id, mines_structure, view_structure):
        self.id = id
        self.mines_structure = mines_structure
        self.view_structure = view_structure

    @staticmethod
    def create(board):
        minesweeper_id = uuid.uuid4()
        minesweeper_mines = MinesStructure(None, board.get_mines_board(), board.get_cant_mines())
        minesweeper_view = ViewStructure(0, board.get_view_board())

        minesweeper = Minesweeper(minesweeper_id, minesweeper_mines,minesweeper_view)

        pickled_minesweeper_mines = pickle.dumps(minesweeper_mines)
        redis_mines_structure.set(str(minesweeper_id), pickled_minesweeper_mines)

        pickled_minesweeper_view = pickle.dumps(minesweeper_view)
        redis_view_structure.set(str(minesweeper_id), pickled_minesweeper_view)

        return minesweeper

    @staticmethod
    def get_minesweeper(id):
        try:
            return Minesweeper(id, pickle.loads(redis_mines_structure.get(str(id))), pickle.loads(redis_view_structure.get(str(id))))
        except TypeError:
            raise NotFound()

    def turn(self, cell, turned_cells=[]):
        if cell.is_valid_cell(self.view_structure):
            if not self.view_structure.board[cell.get_row_number()][cell.get_col_number()]:
                self.view_structure.board[cell.get_row_number()][cell.get_col_number()] = True
                self.view_structure.count_viewed = self.view_structure.count_viewed + 1
                cell.set_value(self.mines_structure.board[cell.get_row_number()][cell.get_col_number()])
                turned_cells.append(cell)
                if self.mines_structure.board[cell.get_row_number()][cell.get_col_number()] == 0:
                    for row2 in range(helpers.get_max(0, cell.get_row_number() - 1),
                                      helpers.get_min(self.view_structure.get_sizex_board() - 1, cell.get_row_number() + 1) + 1):
                        for col2 in range(helpers.get_max(0, cell.get_col_number() - 1),
                                          helpers.get_min(self.view_structure.get_sizey_board() - 1, cell.get_col_number() + 1) + 1):
                            if self.mines_structure.board[row2][col2] != 9:
                                self.turn(MinesweeperCell(row2, col2), turned_cells)
                            else:
                                self.mines_structure.win = False
                if self.mines_structure.board[cell.get_row_number()][cell.get_col_number()] == 9:
                    self.mines_structure.win = False

        if self.mines_structure.win != False and self.view_structure.game_wined(self.mines_structure):
            self.mines_structure.win = True

        pickled_minesweeper_mines = pickle.dumps(self.mines_structure)
        redis_mines_structure.set(str(self.id), pickled_minesweeper_mines)

        pickled_minesweeper_view = pickle.dumps(self.view_structure)
        redis_view_structure.set(str(self.id), pickled_minesweeper_view)

        return turned_cells

    def game_wined(self):
        return self.mines_structure.game_wined()

    def game_lost(self):
        return self.mines_structure.game_lost()

    def unfinished(self):
        return not self.game_wined() and not self.game_wined()

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

    def get_cant_mines(self):
        return self.mines

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
    value = None

    def __init__(self, x, y, value=None):
        self.pos_x = x
        self.pos_y = y
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_row_number(self):
        return self.pos_x

    def get_col_number(self):
        return self.pos_y

    def is_valid_cell(self, structure):
        if self.pos_x < structure.get_sizex_board() and self.pos_y < structure.get_sizey_board():
            return True

        return False

class Structure(object):
    board = None

    def get_sizex_board(self):
        return len(self.board[0])

    def get_sizey_board(self):
        return len(self.board)


class MinesStructure(Structure):
    win = None
    mines = None

    def __init__(self, win, board, mines):
        self.win = win
        self.board = board
        self.mines = mines

    def game_wined(self):
        return self.win == True

    def game_lost(self):
        return self.win == False

class ViewStructure(Structure):
    id = None
    count_viewed = None

    def __init__(self, count_viewed, board):
        self.count_viewed = count_viewed
        self.board = board

    def game_wined(self, mines_structure):
        return self.count_viewed == (len(self.board) * len(self.board[0])) - mines_structure.mines


class TurnCellResponse(object):
    turned_cells = None
    wined = None
    lost = None

    def __init__(self, turned_cells, wined, lost):
        self.turned_cells = turned_cells
        self.wined = wined
        self.lost = lost
