from flask import Flask, jsonify

from Alumnos.routes import alumnos
from Directivos.routes import directivos
from Maestros.routes import maestros

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ['GET', 'POST'])
def home():
    return jsonify({'Datos':'Home'})

app.register_blueprint(alumnos)
app.register_blueprint(directivos)
app.register_blueprint(maestros)

if __name__ == '__main__':
    app.run(debug =  True, port = 3000)