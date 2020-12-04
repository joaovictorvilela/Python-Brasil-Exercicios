vetor = []
for numeros in range(0,5):
    # pedindo 5 valores ao usuário
    vetor.append(int(input(f'Digite o {numeros+1}º número: ')))
print()
# print pra pular uma linha
for indice,valor in enumerate(vetor):
    # utilizei o enumerate pra mostrar a posição e o número dentro da lista
    print(f'O {indice+1} número digitado foi o {valor}')