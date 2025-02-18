import json

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
    
def write(dados):
    with open('app/models/user_model.json','w') as file:
        json.dump(dados, file, indent=4)
        
