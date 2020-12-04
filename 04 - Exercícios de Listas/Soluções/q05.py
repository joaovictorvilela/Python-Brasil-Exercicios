vetorGERAl = [[],[],[]]
# aqui eu criei uma lista de listas

for numeros in range(0,20):
    numero = int(input('insira um número: '))
    # pedindo 20 números ao usuário
    vetorGERAl[0].append(numero)
    # adicionando todos os números na posição 0 da lista
    if numero % 2 == 0:
        vetorGERAl[1].append(numero)
        # se ele for par, adicione na posição 1
    elif numero % 2 != 0:
        vetorGERAl[2].append(numero)
        # se ele não for par, adicione na posição 2

# print do resultado
print(f'Números pares: {vetorGERAl[1]}\nNúmeros ímpares: {vetorGERAl[2]}\nTodos os números: {vetorGERAl[0]}')