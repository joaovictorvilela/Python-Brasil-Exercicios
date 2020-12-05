# dados fictícios dados pela questão
lista_carros = ['fusca','gol','uno','Vectra','Peugeout']
lista_consumo = [7,10,12.5,9,14.5]

print(f'\n{"RELATÓRIO FINAL":^63}')
print('-' * 63)
print(f'{"CARRO":<10} {"Km/Litro":^10} {"Consumo 1000km":^20} {"Valor (em R$)":^20}')
print('-' * 63)

for i in range(len(lista_carros)):
    # pegando o valor do menor consumo e imprimindo o modelo do carro correspondete a esse valor
    consumo = 1000 / lista_consumo[i]
    if lista_consumo[i] < consumo:
        carroEconomico = lista_carros[i]
    # calculando o consumo, e o valor do consumo
    print(f'{lista_carros[i].upper():<10} {lista_consumo[i]:^10.2f} {1000/lista_consumo[i]:^20.2f} {(1000/lista_consumo[i])*2.25:^20.2f}')
print('-' * 63)
print(f'Carro + econômico: {carroEconomico}')
