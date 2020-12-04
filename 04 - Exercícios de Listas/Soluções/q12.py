# gerando alturas aleatórias
alturas = [1.87,1.65,1.23,1.89,1.90,1.32,1.56,1.87,1.04,1.21,1.06,1.76,1.58,1.80,1.99,1.87,1.65,1.23,1.89,1.90,1.32,1.56,1.87,1.04,1.21,1.06,1.76,1.58,1.80,1.99]

# gerando idades aleatórias
idades = [23, 21, 22, 21, 22, 17, 21, 22, 19, 15, 22, 19, 17, 24, 17, 16, 17, 18, 23, 19, 18, 23, 18, 17, 18, 19, 23, 25, 15, 18]

# calculando a méida das alturas
media_alturas = sum(alturas) / len(alturas)
quantidade = 0

# usando o enumerate pra pegar a posição das idades e alturas
for posicao,idade in enumerate(idades):
    if idade > 13 and alturas[posicao] < media_alturas:
        # se a idade for > 13 e altura na posição idade for menor que a média
        quantidade += 1
        # adicione um ao contador
print(f'Total de {quantidade} alunos atendem ao requisito da questão.')
