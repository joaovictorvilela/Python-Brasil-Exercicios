from time import sleep

lista_notas = []

for notas in range(0,4):
    lista_notas.append(float(input(f'Digite a {notas+1}ª nota: ')))
print()
# calculando a média das notas 
media = sum(lista_notas) / len(lista_notas)

# mostrando a nota e o índice dela, além da média
for indice,nota in enumerate(lista_notas):
    print(f'{indice+1}ª nota: {nota:.2f}')
print(f'\nCALCULANDO A MÉDIA...\n')
sleep(1)
print(f'Média: {media:.2f}')