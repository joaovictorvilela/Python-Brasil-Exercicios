# recebendo o total de horas trabalhadas e o valor da hora
tot_horas = float(input('Total de horas trabalhadas no mês: '))
tot_valor = float(input('Valor da hora em R$: '))
# calculando o salário multiplicando os valores acima
salario = tot_horas * tot_valor
# print das informações
print(f'O seu salário é igual a R${salario:.2f}')
