import re

def verifica_senha(senha):
    #verifica o tamanho
    if len(senha) < 6 or len(senha)>32:
        return False

    #verifica se possui apenas numeros e letras
    if not re.match(r'^[A-Za-z0-9]*$',senha):
        return False

    #verifica se há pelo menos uma letra maiuscula
    if not re.match(r'^.*[A-Z].*$',senha):
        return False

    #verifica se há pelo menos uma letra minuscula
    if not re.match(r'^.*[a-z].*$',senha):
        return False

    #verifica se há pelo menos um numero
    if not re.match(r'^.*[0-9].*$',senha):
        return False

    return True

while True:
    try:
        senha = input()
        if verifica_senha(senha):
            print('Senha valida.')
        else:
            print('Senha invalida.')
    except:
        break