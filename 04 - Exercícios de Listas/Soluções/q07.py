from time import sleep

vetor = list()
soma = 0
multiplicacao = 1

for numeros in range(0,5):
    vetor.append(int(input(f'Insira o {numeros+1}º número: ')))

for numero in vetor:
    soma += numero
    multiplicacao *= numero

print(f'Os valores digitados foram: {vetor}\n')
print(f'CALCULANDO A SOMA E A MULTIPLICAÇÃO...')
sleep(1)
print(f'Soma: {soma}\nMultiplicação: {multiplicacao}')
