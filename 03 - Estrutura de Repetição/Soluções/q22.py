numero = 0
while (numero <= 0):
    numero = int(raw_input('Voce quer ver se qual número é primo? '))
    if (numero <= 0):
        print('O número deve ser positivo!')

primo = True
for i in range(2, numero / 2 + 1):
    if (numero % i == 0):
        primo = False
        break

if (primo):
    print('O número é primo')
else:
    print('O número não é primo')
    print('Ele é divisível por ',end=' ')
    for i in range(1, numero + 1):
        if (numero % i == 0):
            print(i,end=' ')