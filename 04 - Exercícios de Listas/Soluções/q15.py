lista = []
soma = 0
while True:
    n = float(input('Digite: '))
    if n >= 0:
        soma += n
        lista.append(n)
    if n < 0:
        break

print(f'Tamanho da lista: {len(lista)}')
for x in lista:
    print(x)

for x in lista:
    print(x,end=' ')
print()

lista.sort(reverse=True)
for x in lista:
    print(x,end=' ')
print()

media = soma / len(lista)

print(f'Soma: {soma}')
print(f'Média: {media}')
print('Valores acima da média: ',end='')
for x in lista:
    if x > media:
        print(f'{x}',end=' ')
print()
print(f'Valores abaixo de 7: ',end=' ')
for x in lista:
    if x < int(7):
        print(x,end=' ')
print()
