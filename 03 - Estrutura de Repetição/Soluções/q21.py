numero = int(input('Insira um número para teste: '))
multiplos = 0

for x in range(2,numero):
    if numero % x == 0:
        multiplos += 1

print('É PRIMO' if numero >= 2 and multiplos == 0 else 'NÃO É PRIMO')
