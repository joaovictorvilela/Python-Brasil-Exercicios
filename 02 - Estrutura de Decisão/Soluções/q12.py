horas = float(input('Digite quantas horas você trabalhou: '))
valor_horas = float(input('Valor da hora R$: '))

salario_bruto = valor_horas * horas
inss = 0.1 * salario_bruto
fgts = 0.11 * salario_bruto

if salario_bruto <= 900:
    ir = 0 
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = 0.05 * salario_bruto
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = 0.1 * salario_bruto
elif salario_bruto > 2500:
    ir = 0.2 * salario_bruto

desc_total = ir + inss
liquido =  salario_bruto - desc_total 

print(f'Salário Bruto: R${salario_bruto:.2f}')
print(f'(-) IR (5%): R${ir:.2f}')
print(f'(-) INSS (10%): R${inss:.2f}')
print(f'FGTS (11%): R${fgts:.2f}')
print(f'Total dos descontos: R${desc_total:.2f}')
print(f'Salário Líquido: R${liquido:.2f}')