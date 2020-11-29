print('-'*30)
print('COLECIONADOR DE CDs'.center(30))
print('-'*30)

NumeroTotalDeCds = int(input('Quantos CDs? '))
media = valorTotalGasto = soma = 0

for x in range(NumeroTotalDeCds):
    valorUnitario = float(input(f'Informe o valor gasto no {x+1}º CD: '))
    soma += valorUnitario

valorTotalGasto = soma 
media = soma / NumeroTotalDeCds

print(f'Valor Médio por CD R${media:.2f}')
print(f'Quantidade Total de CDs: {NumeroTotalDeCds}')
print(f'Valor total gasto R${valorTotalGasto:.2f}')

