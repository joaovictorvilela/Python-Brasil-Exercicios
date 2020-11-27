menor = maior = soma = quantidade = 0
resposta = 'S'

while resposta == 'S':
    numero = float(input('Informe um número: '))
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
print(f'Maior: {maior}\nMenor: {menor}\nSoma: {soma}')
