vetor = []
for numeros in range(0,10):
    vetor.append(float(input(f'Insira o {numeros+1}º número: ')))
print(f'Os valores digitados na ordem inversa são:')
print('-=' * 40)
vetor.sort(reverse=True)
print(vetor)