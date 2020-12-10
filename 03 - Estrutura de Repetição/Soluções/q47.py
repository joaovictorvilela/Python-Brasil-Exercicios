notas = []
soma = 0
# pedindo o nome
nome = str(input('Nome: ')).upper()
# pedindo as notas
for n in range(7):
    notas.append(float(input(f'Digite a {n+1}ª nota: ')))
    # somando as notas
    soma += notas[n]
# definindo o maior e menor valor
maior = menor = notas[0]
# percorrendo a lista e verificando o maior e menor valor
for i in notas:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
# subtraindo o maior e menor valor da soma
soma -= menor 
soma -= maior
# calculando a média
media = soma / 5
# exibindo os resultados
print('=' * 60)
print(f'{"RESULTADO FINAL":^60}')
print('=' * 60)
print(f'{"N. Atleta":^15} {"Melhor nota":^15} {"Pior nota":^15} {"Média":^15}')
print(f'{nome:^15} {maior:^15.1f} {menor:^15.1f} {media:^15.1f}')