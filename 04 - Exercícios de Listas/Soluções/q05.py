vetorGERAl = [[],[],[]]

for numeros in range(0,20):
    numero = int(input('insira um número: '))
    vetorGERAl[0].append(numero)
    if numero % 2 == 0:
        vetorGERAl[1].append(numero)
    elif numero % 2 != 0:
        vetorGERAl[2].append(numero)

print(f'Números pares: {vetorGERAl[1]}\nNúmeros ímpares: {vetorGERAl[2]}\nTodos os números: {vetorGERAl[0]}')