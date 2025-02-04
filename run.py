from bottle import  run , route
import app.controllers.login_controller
import app.controllers.register_controller
from app.models.login_register_model import users, adms

# ----------- ROTA INICIAL ----------- 

@route('/')
def index():
    return "<h1>Bem vindo ao gerenciamento escolar!<br> Deseja entrar como <a href='/Adm'>Coordenador</a> ou <a href='/User'>Aluno/Professor</a>?</h1>"

# ----------- PERMISSÕES -----------

@route('/Adm')
def adm():
    return '<h1>Deseja realizar <a href= /Adm/Login>Login</a> ou <a href= /Adm/Register>Registrar-se</a>?</h1>'

@route('/User')
def user():
    return '<h1>Deseja realizar <a href= /User/Login>Login</a> ou <a href= /User/Register>Registrar-se</a>?</h1>'

# ----------- ----------- -----------
    
if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)