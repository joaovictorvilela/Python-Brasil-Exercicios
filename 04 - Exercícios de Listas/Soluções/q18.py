lista_jogadores = [] # lista com os votos
while True: 
    while True:
        numero = int(input('Número do jogador (0=fim): ')) # pedindo os números dos jogadores
        # criando condições para adicionar o número do jogador na lista
        if numero >= 0 and numero <= 24:
            if numero > 0 and numero <= 24: 
                lista_jogadores.append(numero)
            break
        # mensagem do erro caso o usuário digitasse um valor acima de 23 ou menor que 0
        print('Por favor, informe um valor entre 1 e 23 ou 0 para sair!')
    if numero == 0:
        break
# cabeçalho do resultado
print('-' * 50)
print(f'{"Nº jogador":<15} {"Votos":^15} {"% de votos":^15}')
print('-' * 50)

tamanho = len(lista_jogadores) # tamanho da lista com os votos, para calcular a porcentagem
# percorrendo a lista, imprimindo o número do jogador caso ele tenha pelo menos um voto
for votos in range(24):
    if lista_jogadores.count(votos) >= 1:
        # calculando a porcentagem
        print(f'{votos:<15} {lista_jogadores.count(votos):^15} {(lista_jogadores.count(votos) * 100) / tamanho:^15.2f}')
print(f'\nForam computados {sum(lista_jogadores)} votos.')
