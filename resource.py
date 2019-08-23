from flask import request, make_response
from flask_restful import Resource
import json
from schema import minesweeper_schema

class MinesweeperResource(Resource):

    def get(self):
        return {"Ok": "True"}

    def post(self):
        entity = minesweeper_schema.load(request.json).data

        return make_response(minesweeper_schema.dumps(entity).data, 201)