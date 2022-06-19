
from flask_sqlalchemy import SQLAlchemy

from app import app
db = SQLAlchemy(app)


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    short_description = db.Column(db.String(150))
    description = db.Column(db.Text)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    type = db.relationship('Type')


class Type(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    color = db.Column(db.String(50))


db.drop_all()
db.create_all()
