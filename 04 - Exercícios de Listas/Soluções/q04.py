from time import sleep

lista_palavras = []

# vetor que irá pedir as 10 palavras
for palavra in range(0,10):
    lista_palavras.append(str(input(f'Insira a {palavra+1}ª palavra: ')))

# contador da consoantes
contaConsoante = 0
print()
print(f'{"OBTENDO RESULTADOS..."}')

# esse laço irá percorrer a lista com as palavras
for palavra in lista_palavras:
    sleep(1)
    print(f'\nNa palavra {palavra} nós temos ',end='')
    # print parcial do resultado, sem quebra de linha
    for letra in palavra:
        # esse laço irá percorrer cada elemento (palavra) dentro de nossa lista
        if letra in 'bcdfghjklmnpqrstvwxyz':
            # verificando se a letra é conosante
            contaConsoante += 1
            print(f'{letra}',end=' ')
            # print da letra
print()
sleep(1)
print(f'Ao todo, foram digitados {contaConsoante} consoantes')
