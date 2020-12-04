# nesse exercício vou utilizar dicionário,lista e tupla
listaSaltos = []
lista_geral = []
atleta = {}
saltos = ('Primeiro Salto:', 'Segundo Salto:', 'Terceiro Salto:', 'Quarto Salto:', 'Quinto Salto:')

while True:
    # precisamos esvaziar o dicionário atleta e a lista de saltos para não dá problema
    atleta.clear()
    listaSaltos.clear()
    atleta['Nome'] = str(input('Nome do alteta: ')).upper()
    # adicionando o nome do atleta
    if atleta['Nome'] == '':
        break
    # condição de parada
    for i in range(5):
        # pedindo os saltos
        listaSaltos.append(float(input(f'{saltos[i]} ')))
        atleta['Saltos'] = listaSaltos[:]
        # adicioando uma cópia da lista de saltos, tem que ser uma cópia, caso contrário dá problema
        media = sum(listaSaltos) / 5
        mediaF = round(media,1)
        # calculando a média simples
    atleta['Media'] = mediaF
    # adicionando uma cópia de atleta na lista geral
    lista_geral.append(atleta.copy())

# enfeite do código
print('-' * 80)
print(f'{"Atleta N°":^10} {"Nome":^20} {"Saltos":^20} {"Média":^30}')
print('-' * 80)
# pegando os números do jogador + 1
for indice,valor in enumerate(lista_geral):
    print(f'{indice+1:^10} ',end=' ')
    for v in valor.values():
        # percorendo os dicionário dentro da lista e exibindo os valores com uma formatação
        #  A FORMATAÇÃO DA MÉDIA SAI UM POUCO DESALINHADA QUANDO O SALTO TEM VALOR 10 EM DIANTE, EM BREVE VOU CORRIGIR
        print(f'{str(v):^20}',end=' ')
    # esse print é pra pular uma linha
    print()
print()