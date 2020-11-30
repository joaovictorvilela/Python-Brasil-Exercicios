valor = float(input('Valor da Dívida R$: '))
print()

parcelas  = (1, 3, 6, 9, 12)
juros = (0,10,15,20,25)

print('-' * 75)
print(f'{"Valor da dívida":^16} {"Valor dos juros":^18} {"Nº de parcelas":^16} {"Valor das Parcelas":^16}') 
print('-' * 75)
c = 0
for dados in parcelas:
    valorJuros = (juros[c] / 100) * valor
    valorDivida = valorJuros + valor
    valorParcela = valorDivida / dados
    c += 1
    print(f'{valorDivida:^16.2f} {valorJuros:^18.2f} {dados:^16} R${valorParcela:^16.2f}')
print('-' * 75)
