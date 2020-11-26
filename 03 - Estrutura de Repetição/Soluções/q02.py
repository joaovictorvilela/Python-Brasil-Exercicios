user = password = ''

while user == password:
    user = str(input('Usuário: ')).strip().upper()
    password = str(input('Senha: ')).strip().upper()
    if user == password:
        print('Usuário e Senha não podem ser iguais!')
