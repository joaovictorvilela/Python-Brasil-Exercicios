salario = float(input('Salário: '))
percentual = 1.5
ano = 1996

while ano <= 2000:
    print(f'R$ {salario:.2f}\nPercentual {percentual}%\nAno: {ano}')
    salario += (salario * (percentual/100))
    percentual *= 2
    ano += 1
print(f'Salário atual do funcionário R$: {salario:.2f}')