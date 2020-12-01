# recebendo as notas e calculando a média
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2) / 2

# definindo o conceito e o resultado
conceito = result = ''

if media >= 0 and media <= 4:
    conceito = 'E'
    result = 'REPROVADO'
elif media > 4 and media <= 6:
    conceito = 'D'
    result = 'REPROVADO'
elif media > 6 and media <= 7.5:
    conceito = 'C'
    result = 'APROVADO'
elif media > 7.5 and media <= 9:
    conceito = 'B'
    result = 'APROVADO'
elif media > 9 and media <= 10:
    conceito = 'A'
    result = 'APROVADO'
    
print('-'*40)
print(f'N1: {n1:.2f} pontos\nN2: {n2:.2f} pontos\nMédia: {media:.2f} pontos\nConceito: {conceito}\nStatus: {result}')
print('-'*40)