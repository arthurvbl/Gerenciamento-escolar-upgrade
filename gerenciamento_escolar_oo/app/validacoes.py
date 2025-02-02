def valida_nulo(x):
    while True:
        if x <= 0:
            x = int(input("Número não pode ser negativo, digite novamente: "))
        else:
            break
    return x

def valida_media(x):
    while True:
        if x > 10 or x < 0:
            x = float(input("Número deve estar entre '0' e '10': "))
        else:
            break

def valida_ciclo(ciclo, ano):
    while ciclo not in ("fundamental", "medio"):
        ciclo = input("Escolha inválida! Insira 'fundamental' ou 'medio': ").strip().lower()    
    ano = int(input("Ano: "))
    if ciclo == "fundamental":
        while ano < 1 or ano > 9:
            ano = int(input("Ano inválido! Insira um ano de '1' a '9': "))
    else:
        while ano < 1 or ano > 3:
            ano = int(input("Ano inválido! Insira um ano de '1' a '3': "))
    return ano
