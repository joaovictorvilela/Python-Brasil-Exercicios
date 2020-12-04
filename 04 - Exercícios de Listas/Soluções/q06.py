lista_medias = []
# lista com as médias
for notas in range(0,3):
    # esse laço repete  3 vezes o laço de dentro, já que vamos pedir a nota de 3 alunos
    soma = media = 0
    print(f'\nInforme as notas do {notas+1}º aluno')
    print('-=' * 18)
    for x in range(0,4):
        # aqui, eu peço as 4 notas do aluno
        n = float(input(f'{x+1}ª nota: '))
        soma += n
        # faço a soma
    media = soma / 4
    # calculo a média
    lista_medias.append(media)
    # adiciono a média dentro da lista

contador = 0

for media in lista_medias:
    # percorrendo a lista com as médias
    if media >= 7:
        # se a média for maior ou igual a 7, adicione 1 ao contador
        contador += 1

# resultado
print(f'\nAo todo, {contador} alunos estão com média >= 7')
