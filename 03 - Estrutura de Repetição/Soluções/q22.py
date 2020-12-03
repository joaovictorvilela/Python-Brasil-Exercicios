numero = int(input('Insira um número para teste: '))
multiplos = 0

for x in range(2,numero):
    if numero % x == 0:
        multiplos += 1
        print(f'{numero} é divísivel por {x}')
if numero >= 2 and multiplos == 0:
    print('É PRIMO')
else:
    print('Por isso não é primo')