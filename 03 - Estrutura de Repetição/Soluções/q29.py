print('Lojas Quase Dois - tabela de Preços')
soma = 0
for x in range(1,51):
    valorUnitario = 1.99
    soma += valorUnitario
    print(f'{x} - R$ {soma:.2f}')
    