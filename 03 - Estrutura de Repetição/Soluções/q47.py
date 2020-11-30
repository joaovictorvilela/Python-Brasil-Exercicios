notas = []
soma = 0

nome = str(input('Nome: ')).upper()
for n in range(7):
    notas.append(float(input(f'Digite a {n+1}ª nota: ')))
    soma += notas[n]

maior = menor = notas[0]

for i in notas:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

soma -= menor 
soma -= maior
media = soma / 5

print('=' * 60)
print(f'{"RESULTADO FINAL":^60}')
print('=' * 60)
print(f'{"N. Atleta":^15} {"Melhor nota":^15} {"Pior nota":^15} {"Média":^15}')
print(f'{nome:^15} {maior:^15.1f} {menor:^15.1f} {media-(maior-menor):^15.1f}')