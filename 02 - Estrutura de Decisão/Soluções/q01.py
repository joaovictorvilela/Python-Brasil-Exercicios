n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

menor = n1

if n2 < n1:
    print(f'O menor é {n2}')
elif n1 < n2:
    print(f'O menor é {n1}')
else:
    print('Os números informados são iguais')
