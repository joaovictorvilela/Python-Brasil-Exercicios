# recebendo a temperatura em °F
grausF = float(input('Informe a temperatura em graus Fahrenheit: '))
# transformando ela em °C
grausC = ((grausF - 32) * 5/9)
# print da informação
print(f'A temperatura em graus Celsius é {grausC:.2f}°C')
