# enfeite do código
print('-'*30)
print('POSTO PYTHON 3.8'.center(30))
print('-'*30)

# variáveis auxliares
quantidade = float(input('Quantidade de combustível em litros (l): '))
tipo = str(input('Tipo de combustível usado: A - Álcool / G - Gasolina: ')).upper()

if tipo == 'A':
    precoLitro = 1.90
    if quantidade <= 20:
        desc = 0.03
        valor = (precoLitro * quantidade) - (desc * (precoLitro * quantidade))
    elif quantidade > 20:
        desc = 0.05
        valor = (precoLitro * quantidade) - (desc * (precoLitro * quantidade))
elif tipo == 'G':
    precoLitro = 2.50
    if quantidade <= 20:
        desc = 0.04
        valor = (precoLitro * quantidade) - (desc * (precoLitro * quantidade))
    elif quantidade > 20:
        desc = 0.06
        valor = (precoLitro * quantidade) - (desc * (precoLitro * quantidade))

print(f'Combustível: {tipo}\nQuantidade: {quantidade}l\nPreço: R${valor:.2f}')
