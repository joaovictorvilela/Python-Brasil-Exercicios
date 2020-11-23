limite = 50
multa_porKG = 4
excesso = multaTot = 0

peso = float(input('Informe o peso total de peixes pescados: '))
if peso > 50:
    excesso = peso - 50
    multaTot = excesso * multa_porKG
print(f'Valor total em Kg: {peso:.2f}Kg\nExcesso: {excesso:.2f}Kg\nMulta por Kg excedente: R${multa_porKG:.2f}\nLimite de Kg: {limite:.2f}kg\nValor total a ser pago: R${multaTot:.2f}')
