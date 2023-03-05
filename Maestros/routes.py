from flask import Blueprint
blueprint = Blueprint('blueprint',__name__)

maestros = Blueprint('maestros',__name__)

@maestros.route('/getmaestros', methods = ['GET'])
def get_maestros():
    return {'keys':'Maestros'}