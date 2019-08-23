from flask import request, make_response
from flask_restful import Resource
from schema import minesweeper_board_schema, minesweeper_cell_schema, turn_cell_response_schema
from model import Minesweeper, TurnCellResponse
import uuid

class MinesweeperCollectionResource(Resource):

    def post(self):
        board = minesweeper_board_schema.load(request.json).data
        board.load()

        Minesweeper.create(board)

        return make_response(minesweeper_board_schema.dumps(board).data, 201)


class MinesweeperEntityResource(Resource):

    def patch(self, id):
        #minesweeper = get_minesweeper(id)
        minesweeper =  Minesweeper(uuid.uuid4(), None, None)
        cell = minesweeper_cell_schema.load(request.json).data

        turned_cells = minesweeper.turn(cell)
        response = TurnCellResponse(turned_cells, minesweeper.game_winned())

        return make_response(turn_cell_response_schema.dumps(response).data, 200)


