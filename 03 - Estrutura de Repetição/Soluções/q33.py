print('-'*40)
print('Departamento Estadual de Meteorologia'.center(40).upper())
print('-'*40)
maior = menor = media = soma = quantidade = 0
continua = 'S'
while continua == 'S':
    temp = float(input('Informe a temperatura: '))
    soma += temp
    quantidade += 1
    continua = str(input('Quer Continuar? [S/N]: ')).upper().strip()
    if quantidade == 1:
        maior = menor = temp
    else:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
media = soma / quantidade
print(f'\nMaior Temperatura: {maior}\nMenor Temperatura: {menor}\nMédia das Temperaturas: {media:.2f}')
