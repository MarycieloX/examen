from flask import Blueprint,render_template, request
from models.escuela import Escuela
from utils.db import db

escuela = Blueprint('escuela',__name__)

@escuela.route('/')
def main():
    return render_template('layout.html')

@escuela.route('/viste')
def viste():
    vista=Escuela.query.all()
    return render_template('escuela-template/formulario.html',vista=vista)


@escuela.route('/add_es', methods=['POST'])
def add_es():
    codigo=request.form['codigo']
    nombre=request.form['nombre']
    duracion=request.form['duracion']
    escuela=Escuela(codigo,nombre,duracion)
    db.session.add(escuela)
    db.session.commit()

    return render_template('escuela-template/formulario.html')