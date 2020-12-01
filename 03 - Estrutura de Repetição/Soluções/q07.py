maior = 0
for n in range(0,5):
    numero = int(input(f'Informe o {n+1}º número: '))
    if n == 0:
        maior = numero
    else:
        if numero > maior:
            maior = numero
print(f'O maior número digitado foi o {maior}') 
