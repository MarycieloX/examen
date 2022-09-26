from flask import Blueprint,render_template, request
from models.curso import Curso
from utils.db import db

curso = Blueprint('curso',__name__)

@curso.route('/')
def main():
    return render_template('layout.html')

@curso.route('/view')
def view():
    vista=Curso.query.all()
    return render_template('curso-template/formulario.html',vista=vista)


@curso.route('/add', methods=['POST'])
def add():
    codigo=request.form['codigo']
    nombre=request.form['nombre']
    credito=request.form['credito']
    curso=Curso(codigo,nombre,credito)
    db.session.add(curso)
    db.session.commit()

    return render_template('curso-template/formulario.html')