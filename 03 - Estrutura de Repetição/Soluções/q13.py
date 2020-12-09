# pedindo base e expoente
base = int(input('Base: '))
expoente = int(input('Expoente: '))

# resultado com valor 1
resultado = 1
if expoente == 1:
    print(f'Resultado: {base}')
elif expoente == 0:
    print('Resultado: 1')
elif expoente < 0:
    print('expoente deve ser positivo')
else:
    # fazendo um for no expoente e multiplicando ele por base
    for x in range(1,expoente+1):
        resultado *= base
    print(f'Resultado: {resultado}')