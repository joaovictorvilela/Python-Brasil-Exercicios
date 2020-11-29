from time import sleep

c = 0
maior_altura = menor_altura = identificacao = indentificacao2 = 0
while c < 4:
    numero = int(input('Insira o número do aluno: '))
    altura = float(input('Insira a altura (em cm): '))
    print('-' * 30)
    if c == 0:
        maior_altura = menor_altura = altura
        identificacao = numero
    else:
        if altura > maior_altura:
            maior_altura = altura
            identificacao = numero
        if altura < menor_altura:
            menor_altura = altura
            identificacao2 = numero
    c += 1

print('Obtendo resultado...')
sleep(1)
print(f'Maior altura: {maior_altura}\nIdentificação: {identificacao}\n')
print(f'Menor altura: {menor_altura}\nIdentificação: {identificacao2}')