from flask import Flask, jsonify
from models import db, Item
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


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