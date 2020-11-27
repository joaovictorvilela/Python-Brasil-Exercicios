base = int(input('Base: '))
expoente = int(input('Expoente: '))

resultado = 1
if expoente == 1:
    print(f'Resultado: {base}')
elif expoente == 0:
    print('Resultado: 1')
elif expoente < 0:
    print('expoente deve ser positivo')
else:
    for x in range(1,expoente+1):
        resultado *= base
    print(f'Resultado: {resultado}')