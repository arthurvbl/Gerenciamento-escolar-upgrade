from bottle import route, request, template, redirect
from app.controllers.banco_dados_controller import load, write

@route('/<permission>/Register', method=['GET', 'POST'])
# Função que registra usuários na página de login
def register(permission):
    
    error= None
    success= None
    # Opção caso o usuário seja comum
    if permission == 'User':
    
        if request.method == 'POST':
            users = load('user_model.json')
            
            username = request.forms.get('username')
            password = request.forms.get('password')
            
            if username in users["username"]:
                error = "Usuário existente."
                return(redirect('/User/Register'))
            else:
                users["username"].append(username)
                users["password"].append(password)
                
                write(users)
                success = "Usuário registrado!"
                return(redirect('/User/Login'))
    # Opção caso o usuário seja um administrador            
    else:
        
        if request.method == 'POST':
            adms = load('adm_model.json')
            
            username = request.forms.get('username')
            password = request.forms.get('password')
            
            if username in adms["username"]:
                error = "Usuário existente."
                return(redirect('/Adm/Register'))
            else:
                adms["username"].append(username)
                adms["password"].append(password)
                
                write(adms)
                success = "Usuário registrado!"
                return(redirect('/Adm/Login'))
        
            
    return template('app/views/register_view', error=error, success= success, permission= permission)