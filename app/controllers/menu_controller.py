from bottle import route, template

@route('/menu')
def menu():
    return template('app/views/menu_view')