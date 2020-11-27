par = impar = 0
for x in range(10):
    if x % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Quntidade de nº pares: {par}\nQuantidade de nº ímpares: {impar}')
