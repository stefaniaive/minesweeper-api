from marshmallow import Schema, fields, post_load, ValidationError
from model import Minesweeper

class MinesweeperSchema(Schema):
    sizeX = fields.Integer(attribute="size_x")
    sizeY = fields.Integer(attribute="size_y")
    mines = fields.Integer()

    def validations(self, data):
        if data['size_x'] == 0 or data['size_y'] == 0:
            raise ValidationError(errors="Size could not be 0")

        if data['mines'] > (data['size_x'] * data['size_y']):
            raise ValidationError(errors="Mines could not be higher than the dimension")

    @post_load()
    def make_object(self, data, **kwargs):
        self.validations(data)
        return Minesweeper(
            data["size_x"],
            data["size_y"],
            data["mines"]
        )


minesweeper_schema = MinesweeperSchema()