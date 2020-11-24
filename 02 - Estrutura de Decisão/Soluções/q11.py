print('-'*40)
print('ORGANIZAÇÕES TABAJARA'.center(40).upper())
print('-'*40)

salario = float(input('Informe seu salário R$ '))
reajuste = 0
percentual = 0

if salario <= 280:
    percentual = 20
    reajuste = (percentual * salario / 100) + salario
elif salario > 280 and salario <= 700:
    percentual = 15
    reajuste = (percentual * salario / 100) + salario
elif salario > 700 and salario <= 1500:
    percentual = 10
    reajuste = (percentual * salario / 100) + salario
elif salario > 1500:
    percentual = 5
    reajuste = (percentual * salario / 100) + salario

print('-'*40)
print('Salário após o reajuste'.center(40).upper())
print('-'*40)

print(f'Salário antes do reajuste: R$ {salario:.2f}')
print(f'{percentual}% de aumento')
print(f'Valor em R$ {percentual*salario/100:.2f}')
print(f'Salário com o reajuste R$ {reajuste:.2f}')