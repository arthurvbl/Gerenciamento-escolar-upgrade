import validacoes                                                  
import pickle                                                      
from classes import Aluno, Professor                               

def menu():                                                                 #Menu de opções
    print("""Escolha uma das opções:                                    
1: Matricular
2: Remover uma matricula
3: Listar matriculas
4: Salvar dados
5: Sair
""")

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
        
def salva_dados(lista_prof, lista_alunos, lista_mat, arq="data.pkl"):     #Função usada para registrar os dados em binário (pickle)
    try:
        with open(arq, "wb") as f:
            pickle.dump((lista_prof, lista_alunos, lista_mat), f)
        print("Dados salvos!")
    except Exception:
        print("Erro ao salvar os dados!")   

def main():
    
    try:                                                                  #Carrega os dados do arquivo "data.pkl" se ele existir
        with open("data.pkl", "rb") as arq:
            lista_prof, lista_alunos, lista_mat = pickle.load(arq)
    except FileNotFoundError:
        lista_prof, lista_alunos, lista_mat = [], [], set()
    except Exception:
        lista_prof, lista_alunos, lista_mat = [], [], set()
    
    while True:
        menu()
        opcao = input("Opção: ")
        
        match opcao:                                                    #Seleciona uma das opções do menu
            case "1":
                escolha = input("Deseja matricular um aluno ou professor? (aluno/professor)").strip().lower()
                while escolha not in ('aluno', 'professor'):  
                    escolha = input("Escolha inválida! Insira 'professor' ou 'aluno': ").strip().lower()
                matricula(escolha, lista_prof, lista_alunos, lista_mat)
            case "2":
                escolha = input("Deseja alterar uma matrícula de um aluno ou de um professor? (aluno/professor)").strip().lower()
                while escolha not in ('aluno', 'professor'):  
                    escolha = input("Escolha inválida! Insira 'professor' ou 'aluno': ").strip().lower()
                remove_matriculas(escolha, lista_prof, lista_alunos, lista_mat)
            case "3":
                escolha = input("Deseja listar as matriculas dos alunos ou professores? (aluno/professor)").strip().lower()
                while escolha not in ('aluno', 'professor'):  
                    escolha = input("Escolha inválida! Insira 'professor' ou 'aluno': ").strip().lower()
                lista_matriculas(escolha, lista_prof, lista_alunos)
            case "4":
                salva_dados(lista_prof, lista_alunos, lista_mat)
            case "5":
                "Tarefa finalizada!"
                break
            case _:
                print("Opção inváldia, insira um dos números do menu:")
        
        
if __name__ == "__main__":
    main()   


