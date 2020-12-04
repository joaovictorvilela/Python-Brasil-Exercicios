from time import sleep

vetor = list()
soma = 0
multiplicacao = 1

# pedindo 5 valores e  adicionando eles na lista
for numeros in range(0,5):
    vetor.append(int(input(f'Insira o {numeros+1}º número: ')))

# percorrendo o vetor e fazendo a multiplicação e a soma deles
for numero in vetor:
    soma += numero
    multiplicacao *= numero

# print do resultado
print(f'Os valores digitados foram: {vetor}\n')
print(f'CALCULANDO A SOMA E A MULTIPLICAÇÃO...')
sleep(1)
print(f'Soma: {soma}\nMultiplicação: {multiplicacao}')
