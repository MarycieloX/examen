from flask import Blueprint,render_template,request
from models.estudiante import Estudiante
from utils.db import db

estudiante = Blueprint('estudiante',__name__)

@estudiante.route('/')
def home():
    return render_template('layout.html')

@estudiante.route('/vista')
def vista():
    vist=Estudiante.query.all()
    return render_template('estudiante-template/formulario.html',vist=vist)


@estudiante.route('/agregar', methods=['POST'])
def agregar():
    dni=request.form['dni']
    apellidos=request.form['apellidos']
    nombres=request.form['nombres']
    fecha_nacimiento=request.form['fecha_nacimiento']
    sexo=request.form['sexo']
    estudiante=Estudiante(dni,apellidos,nombres,fecha_nacimiento,sexo)
    db.session.add(estudiante)
    db.session.commit()

    return render_template('estudiante-template/formulario.html')