quantidadeDeEleitores =  c1 = c2 = c3 = 0

quantidadeDeEleitores = int(input('Forneça o número total de eleitores: '))

for x in range(quantidadeDeEleitores):
    voto = int(input('Digite o nº correspondente ao candidato:\n[1] - Para Candidato 1\n[2] - Para Candidato 2\n[3] - Para Candidato 3\n>>> '))
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1

print(f'Candidato 1: {c1} votos')
print(f'Candidato 2: {c2} votos')
print(f'Candidato 3: {c3} votos')
