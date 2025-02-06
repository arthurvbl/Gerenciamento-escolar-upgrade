from bottle import route, template

@route('/menu')
def menu():
    return template('app/views/menu_view')

@route('/matricular')
def matricula(escolha, lista_prof, lista_alunos, lista_mat):               #Função de matrícula
    
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    validacoes.valida_nulo(idade)
    while True:
        matricula = input("Matricula: ")                                   #Verificação de matrícula existente
        if matricula in lista_mat:
            print("A matrícula digitada já existe, insira outra.")
        else:
            lista_mat.add(matricula)
            break
    
    if (escolha == 'professor'):
        professor = Professor(nome, idade, matricula)
        professor.matricular()
        lista_prof.append(professor)
        
        print("----------- PROFESSOR MATRICULADO -----------")
        print(professor)
        input("Pressione qualquer telca para prosseguir")
        
    else:
        aluno = Aluno(nome, idade, matricula)
        aluno.matricular()
        lista_alunos.append(aluno)
        
        print("----------- ALUNO MATRICULADO -----------")
        print(aluno)
        input("Pressione qualquer telca para prosseguir")

@route('/listar')        
def lista_matriculas(escolha, lista_prof, lista_alunos):                   #Função que lista as matrículas
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
