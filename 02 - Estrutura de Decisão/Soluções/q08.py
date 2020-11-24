print('-' * 30)
print('Qual é o mais barato?'.upper().center(30))
print('-' * 30)

n1 = float(input('Preço do 1º Produto: '))
n2 = float(input('Preço do 2º produto: '))
n3 = float(input('Preço do 3º produto: '))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3

print(f'O produto mais barato custa R$ {menor:.2f}')