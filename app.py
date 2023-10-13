import os

from waitress import serve

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:1234@10.0.0.100:5432/document'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

CORS(app)


@app.route("/", methods=["GET"])
def start_page():
    return "Hello my dr friends"


@app.route('/documents', methods=["GET"])
def document_turnover():
    return jsonify('Super_Hero" : "1')


if __name__ == "__main__":
    serve(app, host="26.234.143.237", port=8080)
