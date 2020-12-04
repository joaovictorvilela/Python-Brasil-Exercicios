from time import sleep

num = int(input('Digite um número: '))
print(f'\nAnalisando o número {num}...\n'.upper())
sleep(1)

# pegando a divisão inteira e depois o módulo por 10
U = num // 1 % 10
D = num // 10 % 10
C = num // 100 % 10
M = num // 1000 % 10

print(f'Unidades: {U}')
print(f'Dezenas: {D}')
print(f'Centenas: {C}')
print(f'Milhar: {M}')
