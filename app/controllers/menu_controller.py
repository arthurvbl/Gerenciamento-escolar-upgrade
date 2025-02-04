from bottle import route, template

@route('/menu')
def menu():
    return template('menu_view')