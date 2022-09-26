from flask import Flask

from routes.escuela import escuela
from routes.estudiante import estudiante
from routes.curso import curso
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# add datebase
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:123456789@dbaws.cwntvuamkmig.us-east-1.rds.amazonaws.com/SisAcademico'
app.config['SQLALCHEMY_TRACK_MODEFICATIONS'] = False

SQLAlchemy(app)


app.register_blueprint(curso)

app.register_blueprint(estudiante)

app.register_blueprint(escuela)




