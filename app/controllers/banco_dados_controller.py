import json

# Função que carrega os dados para uso no login
def load(model):
    try:
        with open(f'app/models/{model}','r') as file:
            dados = json.load(file)
            return dados
    except FileNotFoundError:
        return {{
    "username": [],
    "password": []
    }}

# Função que escreve dados novos para uso no login    
def write(dados):
    with open('app/models/user_model.json','w') as file:
        json.dump(dados, file, indent=4)
        
