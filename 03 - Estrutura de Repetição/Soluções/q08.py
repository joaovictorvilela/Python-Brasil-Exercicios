soma = media = 0

for x in range(0,5):
    numero = float(input(f'Informe o {x+1}º número: '))
    # soma recebe o valor de soma mais o numero digitado
    soma += numero
media = soma / 5
print(f'A soma dos números digitados vale: {soma}\nA média dos números digitados vale: {media}')
