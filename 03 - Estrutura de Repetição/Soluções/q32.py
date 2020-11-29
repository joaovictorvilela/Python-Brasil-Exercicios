print('-'*40)
print('cálculo de fatorial'.center(40).upper())
print('-'*40)

fatorial = int(input('Informe o nº para ver o fatorial: '))
c = fatorial
resultado = 1
print(f'{fatorial}! =',end=' ')
while fatorial != 0:
    resultado *= fatorial
    print(f'{c}',end='')
    print(' . ' if fatorial > 1 else ' = ',end='')
    fatorial -= 1
    c-=1
print(resultado)