import os

from waitress import serve

from flask import Flask, jsonify, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import TableExtractor as te
import OcrToTableTool as ottt
import DocumentEditor as de

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

# Первый параметр - путь к фотографии, которую нужно обработать
# Второй параметр - путь, куда будет сохранен результат в виде .docx файла
def model(path_to_image, path_to_result):
    table_extractor = te.TableExtractor(path_to_image)
    table_extractor.execute()

    ocr_to_table_tool_code_table = ottt.OcrToTableTool('9_perspective_corrected_3.jpg')
    code_table = ocr_to_table_tool_code_table.execute()

    ocr_to_table_tool_medium_table = ottt.OcrToTableTool('9_perspective_corrected_2.jpg')
    medium_table = ocr_to_table_tool_medium_table.execute()

    ocr_to_table_tool_medium_table = ottt.OcrToTableTool('9_perspective_corrected_1.jpg')
    large_table = ocr_to_table_tool_medium_table.execute()

    editor = de.DocumentEditor()
    editor.execute(path_to_result, code_table, medium_table, large_table)

@app.route("/", methods=["GET"])
def start_page():
    return "frontend/public/index.html"


@app.route('/documents', methods=["GET", "POST"])
def render_drag_and_drop_window():
    if request.method == "POST":
        f = request.files.getlist('files')
        print(f)
        for file in f:

            file.save(os.path.join(app.config['save/'], file.filename))
        return 'g'
    else:
        return "unsuccess"


if __name__ == "__main__":
    app.run(host="26.234.143.237", port=8080)
