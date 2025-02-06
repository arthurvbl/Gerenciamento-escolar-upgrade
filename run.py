from bottle import run, route, static_file
import app.controllers.login_controller
import app.controllers.register_controller
from app.models.login_register_model import users, adms

# ----------- SERVIR CSS -----------
@route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='./static')

# ----------- ROTA INICIAL ----------- 

@route('/')
def index():
    return """
    <html>
    <head>
        <title>Gerenciamento Escolar</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #ececec, #2575fc);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                max-width: 400px;
                width: 100%;
            }
            h1 {
                color: #333;
                font-size: 24px;
                margin-bottom: 15px;
            }
            a {
                display: inline-block;
                margin-top: 10px;
                padding: 10px 20px;
                text-decoration: none;
                color: white;
                background: #2575fc;
                border-radius: 5px;
                transition: background 0.3s;
            }
            a:hover {
                background: #6a11cb;
            }
        </style>
    </head>
    <body>
        <div class='container'>
            <h1>Bem-vindo ao Gerenciamento Escolar!</h1>
            <p>Escolha seu perfil para continuar:</p>
            <div class='button-container'>
                <a href='/Adm'>Coordenador</a>
                <a href='/User'>Aluno/Professor</a>
            </div>
        </div>
    </body>
    </html>
    """

# ----------- PERMISSÕES -----------

@route('/Adm')
def adm():
    return """
    <html>
    <head>
        <title>Gerenciamento Escolar - Administrador</title>
       <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #ececec, #2575fc);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                max-width: 400px;
                width: 100%;
            }
            h1 {
                color: #333;
                font-size: 24px;
                margin-bottom: 15px;
            }
            a {
                display: inline-block;
                margin-top: 10px;
                padding: 10px 20px;
                text-decoration: none;
                color: white;
                background: #2575fc;
                border-radius: 5px;
                transition: background 0.3s;
            }
            a:hover {
                background: #6a11cb;
            }
        </style>
    </head>
     <body>
     <div class='container'>
        <h1>Deseja realizar? </h1>
     </div>
        <div class='button-container'>
            <a href='/Adm/Login'>Login</a>  
            <a href='/Adm/Register'>Registrar-se</a>
        </div>
    </body>
    </html>
    """

@route('/User')
def user():
    return """
    <html>
    <head>
        <title>Gerenciamento Escolar - Usuário</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #ececec, #2575fc);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                max-width: 400px;
                width: 100%;
            }
            h1 {
                color: #333;
                font-size: 24px;
                margin-bottom: 15px;
            }
            a {
                display: inline-block;
                margin-top: 10px;
                padding: 10px 20px;
                text-decoration: none;
                color: white;
                background: #2575fc;
                border-radius: 5px;
                transition: background 0.3s;
            }
            a:hover {
                background: #6a11cb;
            }
        </style>
    </head>
    <body>
    <div class='container'>
        <h1>Deseja realizar? </h1>
     </div>
        <div class='button-container'>
            <a href='/User/Login'>Login</a> <a href='/User/Register'>Registrar-se</a>
        </div>
    </body>
    </html>
    """

# ----------- EXECUÇÃO -----------
    
if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
