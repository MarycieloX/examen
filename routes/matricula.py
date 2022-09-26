from flask import Blueprint,render_template, request
from models.curso import Curso
from models.estudiante import Estudiante
from models.matricula import Matricula
from models.escuela import Escuela
from utils.db import db

matricula = Blueprint('matricula',__name__)

@matricula.route('/')
def main():
    return render_template('layout.html')

@matricula.route('/vist')
def vist():
    vi=Matricula.query.all()
    vista=Escuela.query.all()
    vist=Estudiante.query.all()
    vis=Curso.query.all()
    return render_template('matricula-template/formulario.html',vista=vista,vist=vist,vis=vis,vi=vi)

@matricula.route('/add', methods=['POST'])
def add():
    id_escuela=request.form['id_escuela']
    id_estudiante=request.form['id_estudiante']
    id_curso=request.form['id_curso']
    matricula=Matricula(id_escuela, id_estudiante, id_curso)
    db.session.add(matricula)
    db.session.commit()

    return render_template('matricula-template/formulario.html')