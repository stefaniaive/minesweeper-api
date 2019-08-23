from flask import request, make_response
from flask_restful import Resource
from schema import minesweeper_board_schema

class MinesweeperResource(Resource):

    def get(self):
        return {"Ok": "True"}

    def post(self):
        board = minesweeper_board_schema.load(request.json).data
        board.load()

        return make_response(minesweeper_board_schema.dumps(board).data, 201)