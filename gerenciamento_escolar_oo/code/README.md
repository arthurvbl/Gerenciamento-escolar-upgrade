# Sistema de gerenciamento escolar

Este projeto se trata de uma atividade livre da matéria de Orientação a Objetos provido pela UnB. Consiste em um sistema de gestão de matrículas que permite gerenciar alunos e professores, podendo adicionar, listar ou remover as matrículas dos integrantes de uma escola. O sistema em questão foi feito inteiramente em Python, utilizando os conceitos: Encapsulamento, Herança e Polimorfismo.

## Funcionalidades

**1. Matricular:**

- Permite cadastrar alunos e professores utilizando dados como nome, idade, matrícula e outras informações específicas. 

**2. Remover Matrícula:**

- Remove registros de alunos ou professores cadastrados no sistema com base na matrícula.

**3. Listar Matrículas:**

- Lista todos os alunos ou professores cadastrados, exibindo suas informações.

**4. Salvar Dados:**

- Serializa os dados em arquivos utilizando o formato pickle para persistência.

**5. Sair:**

- Encerra o sistema.

## Classes

### Pessoa

Classe abstrata que define os atributos de <u>nome</U>, <u>idade</u> e <u>matrícula</u> para as demais classes.
    
- **Métodos:**
        
    - <u>get_matricula()</u>: Método "getter" do atributo matrícula

    - <u>set_matricula</u>(): Método "setter" do atributo matrícula 

    - <u>matricular</u>(): Método abstrato a ser usado nas classes filhas

### Professor

Classe que herda de Pessoa e recebe atributos específicos de <u>materia</u> e <u>salário</u>.

- **Métodos:**

    - <u>matricular</u>(): Método de matrícula que implementa os atributos de materia e salário aos objetos

    - <U>__str__</u>(): Método dunder que altera a exibição de cada objeto

### Aluno

Classe que herda de Pessoa e recebe atributos específicos de <U>ano</u>, <u>media</U> e <u>situacao</u>.

- **Métodos:**

    - <u>matricular</u>(): Método de matrícula que implementa os atributos de ano, media e situação aos objetos

    - <U>__str__</u>(): Método dunder que altera a exibição de cada objeto

## Utilização de terminal para IO

Clone o repositório:

    git clone <url_do_repositorio>
    cd <nome_do_repositorio>

Execute o programa:

    python3 main_file.py

## Autor

- **Nome:** Arthur Vilas Boas Laterza
- **Matrícula:** 232037374