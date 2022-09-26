from utils.db import db

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.Integer, nullable=False)
    apellidos = db.Column(db.String(60), nullable=False)
    nombres = db.Column(db.String(60), nullable=False)
    fecha_nacimiento = db.Column(db.String(30), nullable=False)
    sexo = db.Column(db.String(20), nullable=False)
    def __init__(self,dni,apellidos,nombres,fecha_nacimiento,sexo):
        self.dni = dni
        self.apellidos = apellidos
        self.nombres = nombres
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
       