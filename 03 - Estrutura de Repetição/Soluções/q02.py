# definindo duas variáveis vazias para o laço funcionar
user = password = ''

while user == password:
    # enquanto usuário e senha forem iguais
    user = str(input('Usuário: ')).strip().upper()
    password = str(input('Senha: ')).strip().upper()
    # pedindo a senha/nome de usuário
    if user == password:
        # print do erro
        print('Usuário e Senha não podem ser iguais!')
