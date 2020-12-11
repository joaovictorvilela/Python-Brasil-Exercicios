cod_menor = cod_maior = int(input("Digite o código da cidade: "))
media_veic = int(input("Número de veículos de passeio: "))
acid_maior = acid_menor = int(input("Digite o número de acidentes: "))
media_acid = cont = 0

if media_veic < 2000:
    media_acid += acid_maior
    cont += 1

for i in range(4):
    cod = int(input("Digite o código da cidade: "))
    veic = int(input("Número de veículos de passeio: "))
    acid = int(input("Digite o número de acidentes: "))

    if veic < 2000:
        media_acid += acid
        cont += 1

    media_veic += veic

    if acid < acid_menor:
        cod_menor = cod
        acid_menor = acid

    if acid > acid_maior:
        cod_maior = cod
        acid_maior = acid

if cont > 0:
    media_acid /= cont

media_veic /= 5

print(f"O maior índice de acidentes {acid_maior} pertence a cidade {cod_maior}")
print(f"O menor índice de acidentes {acid_menor} pertence a cidade {cod_menor}")
print(f"Média de Veículos: {media_veic}")
print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acid}")