from flask import Blueprint
from flask_restx import Api

from apis.news_ns import news_ns
from apis.types_ns import types_ns

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

api.add_namespace(news_ns)
api.add_namespace(types_ns)