from bottle import  run , route
import app.controllers.login_controller
import app.controllers.register_controller
from app.models.login_register_model import users

@route('/')
def index():
    return "<h1>Bem vindo ao gerenciamento escolar! Deseja fazer <a href='/Login'>Login</a> ou <a href='/Register'>Registro</a>?</h1>"


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)