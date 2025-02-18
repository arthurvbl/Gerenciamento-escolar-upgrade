import json
from bottle import route, template, request, redirect
from app.classes import Aluno, Professor
import app.validacoes


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
    models_professor = {'matricula': [], 'nome': [], 'idade': [], 'materia': [], 'salario': []}
    dados_professores = carregar_dados_arquivo('app/models/matricula_professor_model.json', models_professor)

    if request.method == 'POST':
        matricula = request.forms.get('matricula')
        nome = request.forms.get('nome')
        idade = int(request.forms.get('idade'))
        materia = request.forms.get('materia')
        salario = float(request.forms.get('salario'))

        professor = Professor(nome, idade, matricula)

        dados_professores['matricula'].append(matricula)
        dados_professores['nome'].append(nome)
        dados_professores['idade'].append(idade)
        dados_professores['materia'].append(materia)
        dados_professores['salario'].append(salario)

        salvar_dados_arquivo('app/models/matricula_professor_model.json', dados_professores)
        return template('app/views/matricula_professor_view')
    
    return template('app/views/matricula_professor_view')

@route('/matricular/aluno', method=["GET", "POST"])
def matricula_aluno():
    modelo_aluno = {'matricula': [], 'nome': [], 'idade': [], 'ano': [], 'media': [], 'situacao': []}
    dados_alunos = carregar_dados_arquivo('app/models/matricula_aluno_model.json', modelo_aluno)

    if request.method == 'POST':
        matricula = request.forms.get('matricula')
        nome = request.forms.get('nome')
        idade = int(request.forms.get('idade'))
        ano = request.forms.get('ano')
        media = float(request.forms.get('media'))

        aluno = Aluno(nome, idade, matricula)
        situacao = aluno.calcula_situacao(media)

        dados_alunos['matricula'].append(matricula)
        dados_alunos['nome'].append(nome)
        dados_alunos['idade'].append(idade)
        dados_alunos['ano'].append(ano)
        dados_alunos['media'].append(media)
        dados_alunos['situacao'].append(situacao)

        salvar_dados_arquivo('app/models/matricula_aluno_model.json', dados_alunos)
        return template('app/views/matricula_aluno_view')

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
