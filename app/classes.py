from abc import ABC, abstractmethod
import validacoes

class Pessoa(ABC):
    def __init__(self, nome, idade, matricula):         #Método construtor da classe Pessoa
        self.nome = nome
        self.idade = idade
        self.__matricula = matricula                    #Matrícula é um atributo protegido que somente pode ser acessado por meio de métodos
        
    def get_matricula(self):                            #Método getter de matrícula
        return self.__matricula
        
    def set_matricula(self, matricula):                 #Método setter de matrícula
        self.matricula = matricula
    
    @abstractmethod
    def matricular(self):                               
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, matricula, materia=None, salario=None):  #Método construtor da classe Professor       
        super().__init__(nome, idade, matricula)
        self.materia = materia
        self.salario = salario
    
    def matricular(self):                              #Método usado para matricular professores
        self.materia = input("Materia: ")
        self.salario = int(input("Salário: "))
        validacoes.valida_nulo(self.salario)
        
    def __str__(self):                                 #Método dunder que define a representação textual dos objetos (professores)
        return f"\n{self.get_matricula()} || Nome: {self.nome} || Idade: {self.idade} || Materia: {self.materia} || Salário: {self.salario}\n"

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, ano=None, media=None, situacao=None):  #Método construtor da classe Aluno
        super().__init__(nome, idade, matricula)
        self.ano = ano
        self.media = media
        self.situacao = situacao
        
    def matricular(self):                              #Método usado para matricular alunos
        ciclo = input("O aluno está em qual ciclo? (fundamental/medio)").strip().lower()            
        self.ano = validacoes.valida_ciclo(ciclo)
        self.media = float(input("Média: "))
        validacoes.valida_media(self.media)
        self.calcula_situacao(self.media)
        
    def calcula_situacao(self, media):                 #Método usado para definir se um aluno foi aprovado ou reprovado
        if media < 6:
            self.situacao = "REPROVADO"
        else:
            self.situacao = "APROVADO"
        
    def __str__(self):                                 #Método dunder que define a representação textual dos objetos (alunos)
        return f"\n{self.get_matricula()} || Nome: {self.nome} || Idade: {self.idade} || Ano: {self.ano} || Média: {self.media} --> {self.situacao}\n"
        
        
class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Adms:
    def __init__(self, username, password):
        self.username = username
        self.password = password