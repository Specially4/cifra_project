from flask import request
from flask_restx import Namespace, Resource

from setup_db import db
from models import Type
from schemas import type_schema, types_schema

types_ns = Namespace('types')


@types_ns.route('/')
class TypesView(Resource):
    def get(self):
        types = Type.query.all()  # Получение всех типов новостей.
        return types_schema.dump(types), 200

    def post(self):
        data = request.json
        types_data = Type(**data)
        with db.session.begin():
            db.session.add(types_data)
        return 'Types appended', 200

    def put(self):

        pass

    def path(self):
        pass

    def delete(self):
        pass


@types_ns.route('/<int:tid>')
class TypeView(Resource):
    def get(self, tid: int):
        types = Type.query.filter(Type.id == tid).first()
        if not types:
            return 'Type not found', 404
        return type_schema.dump(types), 200
        pass

    def post(self, tid: int):
        pass

    def put(self, tid: int):
        types = Type.query.get(tid)
        if not types:
            return 'Type not found', 404
        data = request.json
        types.name = data.get("name")
        types.color = data.get("color")
        db.session.add(types)
        db.session.commit()
        return 'Type updated', 204

    def path(self, tid: int):
        types = Type.query.get(tid)
        if not types:
            return 'Type not found', 404
        data = request.json
        if 'name' in data:
            types.name = data.get("name")
        if 'color' in data:
            types.color = data.get("color")
        db.session.add(types)
        db.session.commit()
        return 'Type updated', 204

    def delete(self, tid: int):
        types = Type.query.get(tid)
        if not types:
            return 'Type not found', 404
        db.session.delete(types)
        db.session.commit()
        return 'Type deleted', 204
