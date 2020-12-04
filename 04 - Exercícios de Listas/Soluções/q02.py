vetor = []
for numeros in range(0,10):
    vetor.append(float(input(f'Insira o {numeros+1}º número: ')))
    # pedindo 10 valores e adicionado no vetor
print(f'Os valores digitados na ordem inversa são:')
print('-=' * 40)
# utilizando a função de reverse do python
vetor.sort(reverse=True)
print(vetor)