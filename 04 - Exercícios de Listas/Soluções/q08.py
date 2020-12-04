idades = []
alturas = []

# pedindo a altura e idade de 5 pessoas
for dados in range(5):
    idades.append(int(input('Idade: ')))
    alturas.append(float(input('Altura (em m): ')))

# deixando os valores na ordem inversa
idades.reverse()
alturas.reverse()

print('O inverso')
print('-=' * 30)

# percorrendo o vetor idades e pritando o valor de alturas na posição do I
for i in range(len(idades)):
    print(f'Idade: {idades[i]} anos | Altura: {alturas[i]:.2f}m')