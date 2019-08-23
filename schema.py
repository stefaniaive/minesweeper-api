from marshmallow import Schema, fields, post_load, ValidationError
from model import MinesweeperBoard, MinesweeperCell, Minesweeper, MinesStructure, ViewStructure

class MinesStructureSchema(Schema):
    id = fields.UUID()
    win = fields.Boolean(allow_none=True)
    board = fields.List(fields.List(fields.Integer))

    @post_load()
    def make_object(self, data):
        return MinesStructure(data["id"], data["win"], data["board"])


class ViewStructureSchema(Schema):
    id = fields.UUID()
    countViewed = fields.Integer(attribute="count_viewed")
    board = fields.List(fields.List(fields.Integer))

    @post_load()
    def make_object(self, data):
        return ViewStructure(data["id"], data["count_viewed"], data["board"])

class MinesweeperSchema(Schema):
    id = fields.UUID()
    minesStructure = fields.Nested(MinesStructureSchema, attribute="mines_structure", load_only=True)
    viewStructure = fields.Nested(ViewStructureSchema, attribute="view_structure", load_only=True)

    @post_load()
    def make_object(self, data):
        return Minesweeper(data['id'], data['mines_structure'], data['view_structure'])


minesweeper_schema = MinesweeperSchema()

class MinesweeperBoardSchema(Schema):
    sizeX = fields.Integer(attribute="size_x",)
    sizeY = fields.Integer(attribute="size_y")
    mines = fields.Integer()

    def validations(self, data):
        if data['size_x'] == 0 or data['size_y'] == 0:
            raise ValidationError(errors="Size could not be 0")

        if data['mines'] > (data['size_x'] * data['size_y']):
            raise ValidationError(errors="Mines could not be higher than the dimension")

    @post_load()
    def make_object(self, data):
        return MinesweeperBoard(
            data["size_x"],
            data["size_y"],
            data["mines"]
        )


minesweeper_board_schema = MinesweeperBoardSchema()


class MinesweeperCellSchema(Schema):
    posX = fields.Integer(attribute="pos_x")
    posY = fields.Integer(attribute="pos_y")
    value = fields.Integer()

    @post_load()
    def make_object(self, data):
        return MinesweeperCell(data['pos_x'], data['pos_y'])


minesweeper_cell_schema = MinesweeperCellSchema()


class TurnCellResponseSchema(Schema):
    turnedCells = fields.Nested(MinesweeperCellSchema, attribute="turned_cells", many=True)
    wined = fields.Boolean()
    lost = fields.Boolean()


turn_cell_response_schema = TurnCellResponseSchema()