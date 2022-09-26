from utils.db import db

class Matricula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_escuela = db.Column(db.Integer, db.ForeignKey('Escuela.id'))
    id_estudiante = db.Column(db.Integer, db.ForeignKey('Estudiante.id'))
    id_curso = db.Column(db.Integer, db.ForeignKey('Curso.id'))
    def _init_(self,id_escuela,id_estudiante,id_curso):
        self.id_escuela = id_escuela
        self.id_estudiante = id_estudiante
        self.id_curso = id_curso