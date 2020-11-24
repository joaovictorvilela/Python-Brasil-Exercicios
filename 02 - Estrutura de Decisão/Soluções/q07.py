n1 = float(input('1º número: '))
n2 = float(input('2º número: '))
n3 = float(input('3º número: '))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3

print(f'O menor número digitado foi o {menor}')

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3

print(f'O maior número digitado foi o {maior}')