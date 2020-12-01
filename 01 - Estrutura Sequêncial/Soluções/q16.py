# recebendo o valor da área
area = float(input('Informe o tamanho em metros quadrados a serem pintados: '))

# calculando o valor em litros
litros = area / 3

Valor_lata = 80
Capacidade_lata = 18

# pegando a parte inteira de litros/capacidade da lata
totLatas = int(litros/Capacidade_lata)
totValor = totLatas * Valor_lata

# exibindo os resultados
print(f'Total de latas: {totLatas}')
print(f'Valor total a ser pago: R$ {totValor:.2f}')