termos = int(input('Informe a quantidade de termos que deseja: '))

serie = 0.0
for i in range(1, termos + 1):
    serie += 1 / i
    
print(f'Série: {serie}')