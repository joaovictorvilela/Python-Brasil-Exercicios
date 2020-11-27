menor = maior = soma = quantidade = 0
resposta = 'S'

while resposta == 'S':
    numero = float(input('Informe um número: '))
    if numero >= 0 and numero <= 1000:
        soma += numero
        quantidade += 1
        resposta = str(input('Quer continuar? S/N: ')).upper()
        if quantidade == 1:
            maior = menor = numero
        else:
            if numero > maior: 
                maior = numero
            if numero < menor:
                menor = numero
    else:
        print('valores inválidos na entrada')
print(f'Maior: {maior}\nMenor: {menor}\nSoma: {soma}')
