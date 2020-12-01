lista_medias = []
for notas in range(0,3):
    soma = media = 0
    print(f'\nInforme as notas do {notas+1}º aluno')
    print('-=' * 18)
    for x in range(0,4):
        n = float(input(f'{x+1}ª nota: '))
        soma += n
    media = soma / 4
    lista_medias.append(media)

contador = 0

for media in lista_medias:
    if media >= 7:
        contador += 1

print(f'\nAo todo, {contador} alunos estão com média >= 7')
