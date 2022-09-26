from utils.db import db

class Escuela(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(60), nullable=False)
    duracion = db.Column(db.Integer, nullable=False)
    def __init__(self,codigo,nombre,duracion):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion