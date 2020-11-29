from time import sleep

maior_altura = menor_altura = 0 
maior_peso = menor_peso = 0
pessoas = soma_peso = soma_altura = 0

codigo = 1

while codigo != 0:
    codigo = int(input('Código: '))
    if codigo != 0:
        altura = float(input('Altura (em m): '))
        soma_altura += altura
        peso = float(input('Peso (em Kg): '))
        soma_peso += peso
        pessoas += 1
        if pessoas == 1:
            maior_altura = menor_altura = altura
            menor_peso = maior_peso = peso
        else:
            if altura > maior_altura:
                maior_altura = altura
            if altura < menor_altura:
                menor_altura = altura
            if peso > maior_peso:
                maior_peso = peso
            if peso < menor_peso:
                menor_peso = peso

media_peso = soma_peso / pessoas
media_altura = soma_altura / pessoas

print('Obtendo resultado...')
print('-' * 40)
sleep(1)
print(f'Maior Peso: {maior_peso}Kg\nMenor Peso: {menor_peso}Kg')
print('-' * 40)
print(f'Maior altura: {maior_altura}m\nMenor altura: {menor_altura}m')
print('-' * 40)
print(f'Média das alturas: {media_altura}m\nMédia dos pesos: {media_peso}Kg')
print('-' * 40)
