numero = 0
while (numero <= 0):
    numero = int(input('Você quer ver se qual numero é primo?  '))
    if (numero <= 0):
        print('O número deve ser positivo!')

primo = True
for i in range(2, numero / 2 + 1):
    if (numero % i == 0):
        primo = False

if (primo):
    print('O número é primo')
else:
    print('O número não é primo')