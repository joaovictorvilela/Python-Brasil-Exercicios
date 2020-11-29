resposta = 'S'
soma = pessoas = 0

while resposta == 'S':
    idade = int(input('Informe sua idade: '))
    soma += idade
    pessoas += 1
    resposta = str(input('Quer continuar? [S/N] ')).upper()[0]

media = soma / pessoas

if media <= 25:
    print('Jovem')
elif media <= 60:
    print('Adulto')
elif media > 60:
    print('Idoso')
    