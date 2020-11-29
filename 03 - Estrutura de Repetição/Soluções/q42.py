numeros = 0
intervalo1 = intervalo2 = intervalo3 = intervalo4 = outros = 0
while numeros >= 0:
    numeros = int(input('Digite: '))
    if numeros >= 0:
        if numeros <= 25:
            intervalo1 += 1
        elif numeros <= 50:
            intervalo2 += 1
        elif numeros <= 75:
            intervalo3 += 1
        elif numeros <= 100:
            intervalo4 += 1
        else:
            outros += 1

print('-' * 35)
print(f'{"Intervalo":<15} {"Quantidade de Núm.":>15}') 
print('-' * 35)
print(f'{"[0-25]":<15} {intervalo1:>15}\n{"[26-50]":<15} {intervalo2:>15}\n{"[51-75]":<15} {intervalo3:>15}\n{"[76-100]":<15} {intervalo4:>15}\n{"Outros":<15} {outros:>15}')
print('-' * 35)