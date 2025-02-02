from bottle import route, request, template, redirect
from app.models.login_register_model import users

@route('/Login', method=['GET','POST'])
def login():
    
    error = None
    
    if request.method == 'POST':                # Se o método for POST, é coletado o nome de usuário e senha do usuário
        username = request.forms.get('username')
        password = request.forms.get('password')
        
        if username in users and users[username] == password:
            return f"Bem vindo, {username}!"
        else:
            error = "Usuário ou senha incorretos."
            
    return template("app/views/login_view", error= error)
