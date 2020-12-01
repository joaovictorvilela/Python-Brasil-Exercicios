from time import sleep

lista_palavras = []

for palavra in range(0,10):
    lista_palavras.append(str(input(f'Insira a {palavra+1}ª palavra: ')))

contaConsoante = 0
print()
print(f'{"OBTENDO RESULTADOS..."}')
for palavra in lista_palavras:
    sleep(1)
    print(f'\nNa palavra {palavra} nós temos ',end='')
    for letra in palavra:
        if letra in 'bcdfghjklmnpqrstvwxyz':
            contaConsoante += 1
            print(f'{letra}',end=' ')
print()
sleep(1)
print(f'Ao todo, foram digitados {contaConsoante} consoantes')
