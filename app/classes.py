from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade, matricula):         #Método construtor da classe Pessoa
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        

class Professor(Pessoa):
    def __init__(self, nome, idade, matricula, materia=None, salario=None):  #Método construtor da classe Professor       
        super().__init__(nome, idade, matricula)
        self.materia = materia
        self.salario = salario
        
    def to_dict(self):                                   # Método para converter os dados do objeto para um dicionário
        return {
            'matricula': self.matricula,
            'nome': self.nome,
            'idade': self.idade,
            'materia': self.materia,
            'salario': self.salario
        }

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, ano=None, media=None):  #Método construtor da classe Aluno
        super().__init__(nome, idade, matricula)
        self.ano = ano
        self.media = media
        
    def situacao(self):
        if self.media < 6:
            self.situacao = "REPROVADO"
            return self.situacao
        else:
            self.situacao = "APROVADO"
            return self.situacao
        
    def to_dict(self):
        return {
            'matricula': self.matricula,
            'nome': self.nome,
            'idade': self.idade,
            'ano': self.ano,
            'media': self.media,
            'situacao': self.situacao()
        }     
