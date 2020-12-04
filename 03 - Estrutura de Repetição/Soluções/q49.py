termos = int(input('Informe a quantidade de termos que deseja: '))

serie = 0.0
denominador = 1
for i in range(1, termos + 1):
    serie += i / denominador
    denominador += 2

print(f'Série: {serie}')