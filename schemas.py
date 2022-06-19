from marshmallow import Schema, fields


class NewsSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    short_description = fields.String()
    description = fields.String()
    type_id = fields.Integer()


class TypeSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    color_id = fields.Integer()


news_schema = NewsSchema()
alL_news_schema = NewsSchema(many=True)

type_schema = TypeSchema()
types_schema = TypeSchema(many=True)
