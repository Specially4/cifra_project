from flask import request
from flask_restx import Namespace, Resource

from setup_db import db
from models import News
from schemas import news_schema, alL_news_schema

news_ns = Namespace('news')

@news_ns.route('/')
class NewsView(Resource):
    def get(self):
        type_id = request.args.get('type_id')
        if type_id:  # Получение новостей определенного типа.
            news = News.query.filter(News.director_id == type_id)
            return alL_news_schema.dump(news), 200
        news = News.query.all()  # Получение всех новостей.
        return alL_news_schema.dump(news), 200

    def post(self):
        data = request.json
        news_data = News(**data)
        with db.session.begin():
            db.session.add(news_data)
        return 'News appended', 204

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


@news_ns.route('/<int:nid>')
class NewsView(Resource):
    def get(self, nid: int):
        news = News.query.filter(News.id == nid).first()
        if not news:
            return 'News not found', 404
        return news_schema.dump(news), 200

    def post(self, nid: int):
        pass

    def put(self, nid: int):
        news = News.query.get(nid)
        if not news:
            return 'News not found', 404
        data = request.json
        news.name = data.get("name")
        news.short_description = data.get("short_description")
        news.description = data.get("description")
        news.type_id = data.get("type_id")
        db.session.commit()
        return 'Movie updated', 204

    def patch(self, nid: int):
        news = News.query.get(nid)
        if not news:
            return 'News not found', 404
        data = request.json
        if 'name' in data:
            news.name = data.get("name")
        if 'short_description' in data:
            news.short_description = data.get("short_description")
        if 'description' in data:
            news.description = data.get("description")
        if 'type_id' in data:
            news.type_id = data.get("type_id")
        db.session.commit()
        return 'Movie updated', 204

    def delete(self, nid: int):
        news = News.query.get(nid)
        if not news:
            return 'News not found', 404
        db.session.delete(news)
        db.session.commit()
        return 'Movie updated', 204
