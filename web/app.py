from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


@dataclass
class Item(db.Model):
    id: int
    name: str

    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route("/db_add")
def db_add():
    db.session.add(Item(name='item_name'))
    db.session.commit()
    return jsonify({'status': 'ok'})


@app.route("/db_get")
def db_get():
    result = Item.query.all()
    return jsonify(result)