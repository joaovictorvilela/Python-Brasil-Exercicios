maior = 0
for n in range(0,5):
    # pedindo 5 valores inteiros ao usuário
    numero = int(input(f'Informe o {n+1}º número: '))
    # se for o primeiro valor lido, o maior será o número
    if n == 0:
        maior = numero
    else:
        # senão, faça as comparações e atualize o valor
        if numero > maior:
            maior = numero
# print do resultado
print(f'O maior número digitado foi o {maior}') 
