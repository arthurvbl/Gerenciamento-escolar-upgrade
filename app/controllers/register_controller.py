from bottle import route, request, template, redirect
from app.models.login_register_model import users, adms

@route('/<permission>/Register', method=['GET', 'POST'])
def register(permission):
    
    error= None
    success= None
    
    if permission == 'User':
    
        if request.method == 'POST':
            username = request.forms.get('username')
            password = request.forms.get('password')
            
            if username in users["username"]:
                error = "Usuário existente."
            else:
                users["username"].append(username)
                users["password"].append(password)
                success = "Usuário registrado!"
                redirect('/User/Login')
                
    else:
        
        if request.method == 'POST':
            username = request.forms.get('username')
            password = request.forms.get('password')
            
            if username in adms["username"]:
                error = "Usuário existente."
            else:
                adms["username"].append(username)
                adms["password"].append(password)
                success = "Usuário registrado!"
                redirect('/Adm/Login')
        
            
    return template('app/views/register_view', error=error, success= success, permission= permission)