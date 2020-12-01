# recebendo os dois números
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

# verificando qual dos dois números é o menor
if n2 < n1:
    print(f'O menor é {n2}')
elif n1 < n2:
    print(f'O menor é {n1}')
# caso em que os números sejam iguais
else:
    print('Os números informados são iguais')
