from flask import Blueprint,render_template, request
from models.matricula import Matricula
from utils.db import db

matricula = Blueprint('matricula',__name__)

@matricula.route('/')
def main():
    return render_template('layout.html')

@matricula.route('/view')
def view():
    vista=matricula.query.all()
    return render_template('matricula-template/formulario.html',vista=vista)

@matricula.route('/add', methods=['POST'])
def add():
    id_escuela=request.form['id_escuela']
    id_estudiante=request.form['id_estudiante']
    id_curso=request.form['id_curso']
    matricula=Matricula(id_escuela, id_estudiante, id_curso)
    db.session.add(matricula)
    db.session.commit()

    return render_template('matricula-template/formulario.html')