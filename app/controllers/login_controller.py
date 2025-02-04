from bottle import route, request, template, redirect
from app.models.login_register_model import users, adms
from app.controllers.menu_controller import menu

@route('/<permission>/Login', method=['GET','POST'])
def login(permission):
    
    error = None
    
    if permission == 'User':
    
        if request.method == 'POST':                        # Se o método for POST, é coletado o nome de usuário e senha do usuário
            username = request.forms.get('username')
            password = request.forms.get('password')
            
            if username in users["username"]:
                indice = users["username"].index(username)
                if users["password"][indice] == password:
                    return redirect('/menu')
            else:
                error = "Usuário ou senha incorretos."
                
    else:
        
        if request.method == 'POST':                        # Se o método for POST, é coletado o nome de usuário e senha do usuário
            username = request.forms.get('username')
            password = request.forms.get('password')
            
            if username in adms["username"]:
                indice = adms["username"].index(username)
                if adms["password"][indice] == password:
                    return redirect('/menu')
            else:
                error = "Usuário ou senha incorretos."
            
    return template("app/views/login_view", error= error, permission= permission)
