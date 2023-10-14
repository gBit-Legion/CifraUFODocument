import os

from waitress import serve

from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:1234@10.0.0.100:5432/document'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Document(db.Model):
    __tablename__ = 'documents_all'

    id = db.Column(db.INTEGER, primary_key=True)
    file = db.Column(db.TEXT())
    status = db.Column(db.INTEGER())

    def __init__(self, file, status):
        self.file = file
        self.status = status


@app.route("/", methods=["GET"])
def start_page():
    return "index.html"


@app.route('/documents', methods=["GET", "POST"])
def render_drag_and_drop_window():
    pass


if __name__ == "__main__":
    serve(app, host="26.234.143.237", port=8080)
