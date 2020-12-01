# recebendo o valor total trabalhaddos em horas e o valor da hora
tot_horas = float(input('Total de horas trabalhadas no mês: '))
tot_valor = float(input('Valor da hora em R$: '))

# calculando o salário bruto, imposto de renda, INSS, Sindicato e salário líquido
salarioBruto = tot_horas * tot_valor
ir = (11/100) * salarioBruto
inss = (8/100) * salarioBruto
sindicado = (5/100) * salarioBruto
salario_liquido = salarioBruto - (ir+inss+sindicado)

# exibindo as informações
print(f'+ Salário Bruto: R$ {salarioBruto:.2f}')
print(f'- IR (11%): R$ {ir:.2f}')
print(f'- INSS (8%): R$ {inss:.2f}')
print(f'- Sindicado (5%): R$ {sindicado:.2f}')
print(f'= Salário líquido: R$ {salario_liquido:.2f}')
