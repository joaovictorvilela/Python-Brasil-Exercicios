idades = []
alturas = []

for dados in range(2):
    idades.append(int(input('Idade: ')))
    alturas.append(float(input('Altura (em m): ')))

idades.reverse()
alturas.reverse()

print('O inverso')
print('-=' * 30)

for i in range(len(idades)):
    print(f'Idade: {idades[i]} anos | Altura: {alturas[i]:.2f}m')