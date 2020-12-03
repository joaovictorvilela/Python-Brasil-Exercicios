numero = int(input('Insira um número para teste: '))
divisores = 0

for x in range(2,numero):
    if numero % x == 0:
        divisores += 1
        print(f'{numero} é divísivel por {x}')
if numero >= 2 and divisores == 0:
    print('É PRIMO')
else:
    print('Por isso não é primo')