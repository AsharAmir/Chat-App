from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flaskconvoapp import db

class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)


    db.create_all()