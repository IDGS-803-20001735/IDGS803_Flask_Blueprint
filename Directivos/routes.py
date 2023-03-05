from flask import Blueprint
blueprint = Blueprint('blueprint',__name__)

directivos = Blueprint('directivos',__name__)

@directivos.route('/getdirectivos', methods = ['GET'])
def get_directivos():
    return {'key': 'Directivos'}