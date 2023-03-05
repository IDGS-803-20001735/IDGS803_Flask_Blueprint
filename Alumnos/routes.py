from flask import Blueprint
blueprint = Blueprint('blueprint',__name__)

alumnos = Blueprint('alumnos',__name__)

@alumnos.route('/getalumnos', methods = ['GET'])
def get_alumnos():
    return {'key':'Alumnos'}

@alumnos.route('/guardaralumnos', methods = ['POST'])
def save_alumnos():
    return {'key':'Alumnos'}