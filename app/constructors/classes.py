from abc import ABC, abstractmethod

class Pessoa(ABC):
    # Método construtor da classe Pessoa
    def __init__(self, nome, idade, matricula):                              
        self.nome = nome
        self.idade = idade
        self.__matricula = matricula            # Atributo privado
        
    # Método getter
    def get_matricula(self):
        return self._matricula
    
    # Método setter
    def set_matricula(self, nova_matricula):
        self._matricula = nova_matricula
        

class Professor(Pessoa):
    # Método construtor da classe Professor       
    def __init__(self, nome, idade, matricula, materia=None, salario=None):
        super().__init__(nome, idade, matricula)
        self.materia = materia
        self.salario = salario

    # Método para converter os dados do objeto para um dicionário  
    def to_dict(self):                           
        return {
            'matricula': self.matricula,
            'nome': self.nome,
            'idade': self.idade,
            'materia': self.materia,
            'salario': self.salario
        }

class Aluno(Pessoa):
    # Método construtor da classe Aluno
    def __init__(self, nome, idade, matricula, ano=None, media=None):
        super().__init__(nome, idade, matricula)
        self.ano = ano
        self.media = media
    
    # Método que define situação de um objeto Aluno    
    def situacao(self):
        return "REPROVADO" if self.media < 6 else "APROVADO"
    
    # Método para converter os dados do objeto para um dicionário    
    def to_dict(self):
        return {
            'matricula': self.matricula,
            'nome': self.nome,
            'idade': self.idade,
            'ano': self.ano,
            'media': self.media,
            'situacao': self.situacao()
        }     
