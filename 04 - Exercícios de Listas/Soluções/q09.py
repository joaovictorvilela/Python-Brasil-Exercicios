from time import sleep

vetor = []
for numeros in range(0,10):
    vetor.append(int(input('Digite: ')))
soma = 0
for valor in vetor:
    soma += (valor**2)

print('CALCULANDO A SOMA DOS QUADRADOS DOS VALORES...')
sleep(1)
print(f'A soma vale: {soma}')