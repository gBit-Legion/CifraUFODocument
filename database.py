from app import db


class Document(db.Model):
    __tablename__ = 'documents_all'

    id = db.Column(db.integerpo, primary_key=True)
    file = db.Column(db.text())
    status = db.Column(db.integer())

    def __init__(self, file, status):
        self.file = file
        self.status = status
