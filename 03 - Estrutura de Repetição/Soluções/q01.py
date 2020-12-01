# criando uma condição para o laço while funcionar
nota = -1
while nota < 0 or nota > 10:
    nota = int(input('Digite nota: '))
    # imprimindo uma mensagem caso a nota esteja fora do intervalo
    if nota < 0 or nota > 10:
        print('Valor inválido, tente novamente!')
    