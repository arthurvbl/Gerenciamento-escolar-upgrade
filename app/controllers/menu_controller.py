import json
from bottle import route, template, request, redirect
from app.classes import Aluno, Professor


@route('/menu')
def menu():
    return template('app/views/menu_view')

def carregar_dados_arquivo(nome_arquivo, modelo_padrao):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return modelo_padrao

def salvar_dados_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

@route('/matricular', method=["GET", "POST"])
def matricula():
    error = None
    success = None

    if request.method == 'POST':
        escolha = request.forms.get('escolha')

        if escolha == 'professor':
            redirect("/matricular/professor")
        else:
            redirect("/matricular/aluno")

    return template('app/views/matricular_view')

@route('/matricular/professor', method=["GET", "POST"])
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

@route('/listar')        
def lista_matriculas(escolha, lista_prof, lista_alunos):
    if escolha == "professor":
        if not lista_prof:
            print("Nenhum professor matriculado!")
        else:
            for professores in lista_prof:
                print(professores)
    else:
        if not lista_alunos:
            print("Nenhum aluno matriculado!")
        else:
            for alunos in lista_alunos:
                print(alunos)

@route('/remover')                
def remove_matriculas(escolha, lista_prof, lista_alunos, lista_mat):       #Função que exclui uma matrícula específica
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
def logout():
    pass
