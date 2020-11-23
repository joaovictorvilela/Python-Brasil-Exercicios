area = float(input('Informe o tamanho em metros quadrados a serem pintados: '))
litros = area / 3

Valor_lata = 80
Capacidade_lata = 18

totLatas = int(litros/Capacidade_lata)
totValor = totLatas * Valor_lata

print(f'Total de latas: {totLatas}')
print(f'Valor total a ser pago: R$ {totValor:.2f}')