print('-'*40)
print('escola olá, mundo!'.center(40).upper())
print('-'*40)

n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
n3 = float(input('3ª nota: '))
print()

media = (n1+n2+n3) / 3

if media >= 7:
    print(f'Média: {media:.2f} pontos\nStatus: Aprovado')
elif media < 7:
    print(f'Média: {media:.2f} pontos\nStatus: Reprovado')
elif media == 10:
    print(f'Média: {media:.2f} pontos\nStatus: Aprovado com dinstinção')