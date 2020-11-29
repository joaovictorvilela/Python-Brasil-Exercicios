print('Lojas Tabajara')
cont = 1
soma = 0
quantidade = 1
while cont != 0:
    cont = float(input(f'Produto {quantidade}: R$ '))
    quantidade += 1
    soma += cont
print(f'Soma: R$ {soma:.2f}')
dinheiro = float(input('Dinheiro: R$ '))
print(f'Troco: R$ {dinheiro - soma:.2f}')
