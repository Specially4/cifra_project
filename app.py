from flask import Flask, request
from flask_restx import Api, Resource

from data_news import News, Type, db
from data_schema import NewsSchema, TypeSchema
from logger import new_logger

app = Flask(__name__)

api = Api(app)
news_ns = api.namespace('news')
types_ns = api.namespace('types')

app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

new_schema = NewsSchema()
news_schema = NewsSchema(many=True)

type_schema = TypeSchema()
types_schema = TypeSchema(many=True)


@news_ns.route('/')
class NewsView(Resource):
    def get(self):
        type_id = request.args.get('type_id')
        if type_id is not None:  # Получение новостей определенного типа.
            try:
                news = News.query.filter(News.director_id == type_id)
                return news_schema.dump(news), 200
            except Exception as e:
                return '', 404
        news = News.query.all()  # Получение всех новостей.
        return news_schema.dump(news), 200

    def post(self):
        data = request.json
        news_data = News(**data)
        with db.session.begin():
            db.session.add(news_data)
        return '', 200

    def put(self):
        pass

    def path(self):
        pass

    def delete(self):
        pass


@news_ns.route('/<int:nid>')
class NewView(Resource):
    def get(self, nid: int):
        news = News.query.filter(News.id == nid).first()
        if not news:
            return '', 404
        return new_schema.dump(news), 200

    def post(self, nid: int):
        pass

    def put(self, nid: int):
        news = News.query.get(nid)
        if not news:
            return '', 404
        data = request.json
        news.name = data.get("name")
        news.short_description = data.get("short_description")
        news.description = data.get("description")
        news.type_id = data.get("type_id")
        db.session.add(news)
        db.session.commit()
        return '', 204

    def path(self, nid: int):
        news = News.query.get(nid)
        if not news:
            return '', 404
        data = request.json
        if 'name' in data:
            news.name = data.get("name")
        if 'short_description' in data:
            news.short_description = data.get("short_description")
        if 'description' in data:
            news.description = data.get("description")
        if 'type_id' in data:
            news.type_id = data.get("type_id")
        db.session.add(news)
        db.session.commit()
        return '', 204

    def delete(self, nid: int):
        news = News.query.get(nid)
        if not news:
            return '', 404
        db.session.delete(news)
        db.session.commit()
        return '', 204


@types_ns.route('/')
class TypeView(Resource):
    def get(self):
        types = Type.query.all()  # Получение всех типов новостей.
        return types_schema.dump(types), 200

    def post(self):
        data = request.json
        types_data = Type(**data)
        with db.session.begin():
            db.session.add(types_data)
        return '', 200

    def put(self):

        pass

    def path(self):
        pass

    def delete(self):
        pass


@types_ns.route('/<int:tid>')
class TypeView(Resource):
    def get(self, tid: int):
        types = Type.query.filter(News.id == tid).first()
        if not types:
            return '', 404
        return new_schema.dump(types), 200
        pass

    def post(self, tid: int):
        pass

    def put(self, tid: int):
        types = Type.query.get(tid)
        if not types:
            return '', 404
        data = request.json
        types.name = data.get("name")
        types.color = data.get("color")
        db.session.add(types)
        db.session.commit()
        return '', 204

    def path(self, tid: int):
        types = Type.query.get(tid)
        if not types:
            return '', 404
        data = request.json
        if 'name' in data:
            types.name = data.get("name")
        if 'color' in data:
            types.color = data.get("color")
        db.session.add(types)
        db.session.commit()
        return '', 204

    def delete(self, tid: int):
        types = Type.query.get(tid)
        if not types:
            return '', 404
        db.session.delete(types)
        db.session.commit()
        return '', 204


if __name__ == '__main__':
    app.run(debug=True)
