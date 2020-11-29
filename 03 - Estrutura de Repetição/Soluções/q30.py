print('Preço do Pão R$ 0.18\nPanificadora Pão de Ontem - Tabela de preços')
soma = 0
for x in range(1,51):
    valorUnitario = 0.18
    soma += valorUnitario
    print(f'{x} - R$ {soma:.2f}')
    