from utils.db import db

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(40), nullable=False)
    credito = db.Column(db.Integer, nullable=False)
    def __init__(self,codigo,nombre,credito):
        self.codigo = codigo,
        self.nombre = nombre,
        self.credito = credito

