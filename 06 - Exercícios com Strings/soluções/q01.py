def main():
    # pedindo as mensagens ao usuário
    str1 = str(input('Digite uma msg: '))
    str2 = str(input('Digite outra msg: '))

    # imprimrindo o conteúdo das strings lidas
    print(f'String 1 - {str1}\nString 2 - {str2}')

    # imprimindo o tamanho delas/conteúdo
    print(f'Tamanho de "{str1}": {len(str1)} caracteres')
    print(f'Tamanho de "{str2}": {len(str2)} caracteres')

    # verificando o tamanho das strings lidas
    if len(str1) != len(str2):
        print('As strings possuem tamanhos diferentes')
    else:
        print('As strings possuem tamanhos iguais')

    # verificando o conteúdo das strings lidas
    if str1 == str2:
        print('As strings possuem o mesmo conteúdo')
    else:
        print('As strings possuem conteúdos diferentes')
main()
