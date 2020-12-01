vetor = []
for numeros in range(0,5):
    vetor.append(int(input(f'Digite o {numeros+1}º número: ')))
print()
for indice,valor in enumerate(vetor):
    print(f'O {indice+1} número digitado foi o {valor}')