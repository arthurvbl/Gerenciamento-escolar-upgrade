from bottle import route, request, template, redirect
from app.controllers.menu_controller import menu
from app.controllers.banco_dados_controller import load

@route('/<permission>/Login', method=['GET','POST'])
# Função que entra na conta de usuários já cadastrados
def login(permission):
    
    error = None
    # Opção caso o usuário seja comum
    if permission == 'User':
    
        if request.method == 'POST':                        
            username = request.forms.get('username')
            password = request.forms.get('password')
            
            users = load('user_model.json')
            
            if username in users["username"]:
                indice = users["username"].index(username)
                if users["password"][indice] == password:
                    return redirect('/menu')
            else:
                error = "Usuário ou senha incorretos."
    # Opção caso o usuário seja um administrador            
    else:
        
        if request.method == 'POST':                        
            username = request.forms.get('username')
            password = request.forms.get('password')
            
            adms = load('adm_model.json')
            
            if username in adms["username"]:
                indice = adms["username"].index(username)
                if adms["password"][indice] == password:
                    return redirect('/menu')
            else:
                error = "Usuário ou senha incorretos."
            
    return template("app/views/login_view", error= error, permission= permission)
