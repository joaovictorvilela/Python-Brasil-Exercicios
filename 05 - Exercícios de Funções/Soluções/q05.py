def somaImposto(taxaImposto=0, custo=0):
    valor_novo = custo + ((taxaImposto / 100) * custo)
    return f'O valor acrescido do imposto é R${valor_novo:.2f}'

imposto = float(input('Informe o valor do imposto (em %): '))
custo = float(input('Informe o valor do produto (em R$): '))
print(somaImposto(imposto,custo))
