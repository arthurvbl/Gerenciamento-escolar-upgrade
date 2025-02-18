import json
from bottle import route, template, request, redirect
from app.constructors.classes import Aluno, Professor

@route('/menu')
# Abre a página de menu
def menu():
    return template('app/views/menu_view')

# Carrega os dados armazenados no models
def carregar_dados_arquivo(nome_arquivo, modelo_padrao):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return modelo_padrao

# Salva os dados no models
def salvar_dados_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

@route('/matricular', method=["GET", "POST"])
# Função de matricula
def matricula():
    if request.method == 'POST':
        escolha = request.forms.get('escolha')

        if escolha == 'professor':
            redirect("/matricular/professor")
        else:
            redirect("/matricular/aluno")

    return template('app/views/matricular_view')

@route('/matricular/professor', method=["GET", "POST"])
# Função de matricula específica de professores
def professor():
    modelo_professor = {'professores': []}
    dados_professores = carregar_dados_arquivo('app/models/matricula_professor_model.json', modelo_professor)

    if request.method == 'POST':
        nome = request.forms.get('nome')
        idade = int(request.forms.get('idade'))
        matricula = request.forms.get('matricula')
        materia = request.forms.get('materia')
        salario = float(request.forms.get('salario'))
        
        if any(professor['matricula'] == matricula for professor in dados_professores['professores']):
            error = "Erro: Matrícula já cadastrada!"  
            return template('app/views/matricula_professor_view', error=error)

        professor = Professor(nome, idade, matricula, materia, salario)
        
        dados_professores['professores'].append(professor.to_dict())

        salvar_dados_arquivo('app/models/matricula_professor_model.json', dados_professores)
        return template('app/views/menu_view')
    
    return template('app/views/matricula_professor_view')

@route('/matricular/aluno', method=["GET", "POST"])
# Função de matricula específica de alunos
def matricula_aluno():
    modelo_aluno = {"alunos": []}
    dados_alunos = carregar_dados_arquivo('app/models/matricula_aluno_model.json', modelo_aluno)

    if request.method == 'POST':
        nome = request.forms.get('nome')
        idade = int(request.forms.get('idade'))
        matricula = request.forms.get('matricula')
        ano = request.forms.get('ano')
        media = float(request.forms.get('media'))
        
        if any(aluno['matricula'] == matricula for aluno in dados_alunos['alunos']):
            error = "Erro: Matrícula já cadastrada!"  
            return template('app/views/matricula_aluno_view', error=error)

        aluno = Aluno(nome, idade, matricula, ano, media)
        
        dados_alunos['alunos'].append(aluno.to_dict())

        salvar_dados_arquivo('app/models/matricula_aluno_model.json', dados_alunos)
        return template('app/views/menu_view')

    return template('app/views/matricula_aluno_view')

@route('/listar', method=['POST', 'GET'])
# Função que lista as matrículas e outras informações de cadastro      
def lista_matriculas():
    if request.method == 'POST':
        escolha = request.forms.get('escolha')
        if escolha == 'professor':
            redirect("/listar/professor")
        elif escolha == 'aluno':
            redirect("/listar/aluno")

    return template('app/views/listar_view')

@route('/listar/professor', method='GET')
# Lista matriculas e informações de professores
def lista_professor():
    return template('app/views/listar_professor_view')

@route('/listar/aluno', method='GET')
# Lista matriculas e informações de alunos
def lista_aluno():
    return template('app/view/listar_aluno_view')

@route('/remover')
#Função que exclui uma matrícula específica
def remove_matriculas(escolha, lista_prof, lista_alunos, lista_mat):
        matricula = input("Insira a matrícula que deseja excluir: ")
        if escolha == 'professor':
            for professor in lista_prof:
                if professor.get_matricula() == matricula:
                    lista_prof.remove(professor)
                    lista_mat.remove(matricula)
                    print(f"{matricula} removido!")
                    return  
        else:
            for aluno in lista_alunos:
                if aluno.get_matricula() == matricula:
                    lista_alunos.remove(aluno)
                    lista_mat.remove(matricula)
                    print(f"{matricula} removido!")
                    return
                
        print(f"{matricula} não é um {escolha}.")
        
        
        
@route('/logout')
# Realiza logout da conta cadastrada na página de login
def logout():
    pass
