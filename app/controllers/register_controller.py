from bottle import route, request, template, redirect
from jinja2 import Template
from app.models.login_register_model import users, adms

@route('/<permission>/Register', method=['GET', 'POST'])
def register(permission):
    
    error= None
    success= None
    
    if request.method == 'POST':
        username = request.forms.get('username')
        password = request.forms.get('password')
        
        if username in users:
            error = "Usuário existente."
        else:
            users["username"].append(username)
            users["password"].append(password)
            success = "Usuário registrado!"
        
            
    return template('app/views/register_view', error=error, success= success, permission= permission)