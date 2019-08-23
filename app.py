from resource import MinesweeperCollectionResource, MinesweeperEntityResource
from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(MinesweeperCollectionResource, '/minesweeper')
api.add_resource(MinesweeperEntityResource, '/minesweeper/<id>')
