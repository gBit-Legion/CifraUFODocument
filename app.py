import os

from waitress import serve

from flask import Flask, jsonify, request, redirect
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


class Document(db.Model):
    __tablename__ = 'documents_all'

    id = db.Column(db.INTEGER, primary_key=True)
    file = db.Column(db.TEXT())
    status = db.Column(db.INTEGER())

    def __init__(self, file, status):
        self.file = file
        self.status = status


migrate = Migrate(app, db)

CORS(app)


@app.route("/", methods=["GET"])
def start_page():
    return "Hello my dr friends"


@app.route('/documents', methods=["GET", "POST"])
def document_turnover():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            new_document = Document(file=data['file'], status=2)
            db.session.add(new_document)
            db.session.commit()
            return {"message": f"document {new_document.file} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}


if __name__ == "__main__":
    serve(app, host="26.234.143.237", port=8080)
